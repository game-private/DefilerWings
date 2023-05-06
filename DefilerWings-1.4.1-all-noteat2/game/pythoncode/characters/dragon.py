# coding=utf-8

import random
import math

from copy import deepcopy

from pythoncode import data
from pythoncode.data import get_modifier
from pythoncode.utils import get_random_image
from pythoncode.points import Reputation

from pythoncode import treasures
from pythoncode import utils

from fighter import Fighter

# @fdsc Теперь дракон может добывать металлы
class Miner(object):
    def __init__(self, dragon, parent=None):
        
        self.silver     = 0
        self.gold       = 0
        self.mithril    = 0
        self.adamantine = 0
        
        self.gems       = 0
        self.allMines   = 0
        
        self.dragon     = dragon

        if parent != None:
            self.silver     = parent.silver
            self.gold       = parent.gold
            self.mithril    = parent.mithril
            self.adamantine = parent.adamantine
            self.gems       = parent.gems


    # Эффективность добычи металлов. 'gems' - эффективность добычи камней
    def effectiveness(self, metall='gems'):
        allMines = 1 + math.log(1 + self.allMines) / math.log(16)

        if metall == 'gems':
            return 1 + math.log(1 + self.__getattribute__(metall)) / math.log(16) * allMines

        return 1 + math.log(1 + self.__getattribute__(metall)) / math.log(1.41) * allMines


    # Добываем металл
    def mine(self, metall):
        metal = treasures.Ingot(metall)

        k = self.dragon.sizeForMine
        while random.randint(1, 3) <= 2:
            k += 0.5

        metal.weight = self.effectiveness(metall) * k / treasures.metal_types[metall]
        self.__setattr__(metall, self.__getattribute__(metall) + k)

        k = 1
        while random.randint(1, 3) == 1:
            k += 1

        self.dragon.drain_energy(k, True)
        self.allMines += 1

        return metal

    # processing устанавливается в cut_mod. Объявлены в treasures.Gem.cut_dict
    def mineGems(self, entireDay=False):

        minedGems = []

        while self.dragon.energy() > 0:

            effect    = self.effectiveness('gems') * self.dragon.sizeForMine
            choices = [
                ("rough",    100),
                ("polished", 8 * self.gems),
                ("faceted",  int(   1 * self.gems * math.log(1+self.gems)   ))
            ]
            processing = utils.weighted_random(choices)

            if random.randint(0, 100) < effect:
                gems     = treasures.gem_types.keys()
                gemsLen  = len(gems)
                gemIndex = random.randint(0, gemsLen-1)

                # sizes     = treasures.Gem.size_dict.keys()

                choices = [
                ("small",       int(   36 * effect/math.log(1+effect)   )),
                ("common",      int(   24 * effect   )),
                ("large",       int(   12 * effect*math.log(effect)   )),
                ("exceptional", int(   1  * effect   )),
                ]
                size = utils.weighted_random(choices)

                minedGem  = treasures.Gem(g_type=gems[gemIndex], size=size, cut=processing)
                minedGems.append(minedGem)


            self.gems += 1

            k = 1
            while random.randint(1, 3) == 1:
                k += 1

            self.dragon.drain_energy(k, True)
            self.allMines += 1

            if not entireDay:
                break


        return minedGems


    def getStringOfMinedGems(self, minedGems):
        
        def addSpace(str1, str2 = " "):
            if len(str1) > 0:
                return str1 + str2

            return str1

        gems_counts = dict()
        for gem in minedGems:
            nm  = gem.g_type + "|" + gem.cut
            cnt = 0
            if nm in gems_counts:
                cnt = gems_counts[nm][0]

            gems_counts[nm]  = [cnt + 1, gem.g_type, gem.cut]

        names = u""
        for nm in gems_counts:
            cnt   = gems_counts[nm][0]
            cnt10 = cnt % 10
            if cnt10 == 1:
                names += addSpace(treasures.gem_cut_description_rus[gems_counts[nm][2]]['he']['nominative'])
                names +=          treasures.gem_description_rus    [gems_counts[nm][1]]['he']['nominative'] + "\n"
            elif cnt10 >= 2 and cnt10 <= 4:
                names += str(cnt) + " "
                names += addSpace(treasures.gem_cut_description_rus[gems_counts[nm][2]]['they']['genitive'])
                names +=          treasures.gem_description_rus    [gems_counts[nm][1]]['he']  ['genitive'] + "\n"
            else:
                names += str(cnt) + " "
                names += addSpace(treasures.gem_cut_description_rus[gems_counts[nm][2]]['they']['genitive'])
                names +=          treasures.gem_description_rus    [gems_counts[nm][1]]['they']['genitive'] + "\n"


        effect = self.effectiveness('gems')
        streff = str(effect * self.dragon.sizeForMine)
        if names == "":    
            names  = u"Ничего не добыто. Наверное, не хватило опыта. Эффективность добычи " + streff + u"\n(с увеличением размера и количества лап у дракона эффективность повышается при том же опыте; острые когти и бронзовая голова повышают эффективность)"
        else:
            names += u"\nЭффективность добычи " + streff

        return [gems_counts, names]


class Dragon(Fighter):
    """
    Класс дракона.
    """

    def __init__(self, parent=None, used_gifts=None, used_avatars=None, *args, **kwargs):
        """
        parent - родитель дракона, если есть.
        """
        super(Dragon, self).__init__(*args, **kwargs)
        # TODO: pretty screen for name input
        # self._first_name = u"Старый"
        # self._last_name = u"Охотник"
        self.name = random.choice(data.dragon_names)
        self.surname = random.choice(data.dragon_surnames)
        self._age = 0
        self.reputation = Reputation()
        self._tiredness = 0  # увеличивается при каждом действии
        self.bloodiness = 0  # range 0..5
        self.lust = 3  # range 0..3, ресурс восстанавливается до 3 после каждого отдыха
        self.hunger = 3  # range 0..3, ресурс восстанавливается до 3 после каждого отдыха
        self.health = 2  # range 0..2, ресурс восстанавливается до 2 после каждого отдыха
        self._mana_used = 0  # количество использованной маны
        self.spells = []  # заклинания наложенные на дракона(обнуляются после сна)
        self._base_energy = 3  # Базовая энергия дракона, не зависящая от модификторов
        self.special_places = {}  # Список разведанных "достопримечательностей"
        self.events = []  # список событий с этим драконом
        self.Treasure_master = 0 # Мастерство при создании украшений
        if parent != None:
            self.Treasure_master = parent.Treasure_master

        if parent == None:
            self.miner = Miner(self)
        else:
            self.miner = Miner(self, parent.miner)

        self._gift = None  # Дар Владычицы
        if used_gifts is None:
            used_gifts = []
        # Головы
        if parent is not None:
            self.heads = deepcopy(parent.heads)  # Копируем живые головы родителя
            self.heads.extend(parent.dead_heads)  # И прибавляем к ним мертвые
            self.level = parent.level + 1  # Уровень дракона
        else:
            self.heads = ['green']  # головы дракона
            self.level = 1  # Начальный уровень дракона
        self.dead_heads = []  # мертвые головы дракона

        # Анатомия
        if parent is None:
            self.anatomy = ['size']
        else:
            self.anatomy = deepcopy(parent.anatomy)
        self._gift = self._get_ability(used_gifts=used_gifts)
        if self._gift == 'head':
            self.heads.append('green')
        elif self._gift in data.dragon_heads.keys():
            self.heads[self.heads.index('green')] = self._gift
        else:
            self.anatomy.append(self._gift)
        self.avatar = get_random_image("img/avadragon/" + self.color_eng, used_avatars)  # Назначаем аватарку

    @property
    def fullname(self):
        return self.name + u' ' + self.surname

    @property
    def description(self):
        ddescription = u'  '
        mods = self.modifiers()
        ddescription += self._accentuation(data.dragon_size[self.size - 1], self._gift == 'size') + u' '
        ddescription += self._accentuation(self.color, self.color_eng == self._gift) + u' '
        ddescription += self.kind + u'. '
        ddescription += self._accentuation(data.dragon_size_description[self.size - 1], self._gift == 'size')
        for i in xrange(len(self.heads)):
            dscrptn = u"Его %s голова " % data.head_num[i] + data.head_description[self.heads[i]]
            dscrptn = self._accentuation(dscrptn, self.heads[i] == self._gift)
            if self._gift == 'head':
                dscrptn = self._accentuation(dscrptn, i == len(self.heads) - 1)
            ddescription += u"\n  " + dscrptn

        if self.wings == 0 and self.paws == 0:
            ddescription += '\n  ' + data.wings_description[0]
        else:
            if self.wings > 0:
                ddescription += '\n  ' + self._accentuation(data.wings_description[self.wings], self._gift == 'wings')

            if self.paws > 0:
                ddescription += '\n  ' + self._accentuation(data.paws_description[self.paws], self._gift == 'paws')

        for i in xrange(len(data.special_features)):
            if data.special_features[i] in mods:
                ddescription += '\n  ' + self._accentuation(data.special_description[i],
                                                            self._gift == data.special_features[i])
        if 'cunning' in self.modifiers():
            if self.modifiers().count('cunning') <= 3:
                dscrptn = data.cunning_description[self.modifiers().count('cunning') - 1]
                ddescription += '\n  ' + self._accentuation(dscrptn, self._gift == 'cunning')
            else:
                dscrptn = data.cunning_description[-1]  # Выдаем последнее описание (как самое мощное)
                ddescription += '\n  ' + self._accentuation(dscrptn, self._gift == 'cunning')

        [dp1, dp2] = self.defence_power()
        [at1, at2] = self.attack_strength()
        ddescription += u'\n Защита: сильная %d, слабая %d. Атака: сильная %d, слабая %d\nСтрах %d, мана %d, энергия %d, мастерство ювелира %d, уровень %d (1-13), добыча камней %d' % (dp2, dp1, at2, at1, self.fear, self.magic, self.max_energy(), int(self.getTreasureMasterEffect(isNominal=True) * 100), self.level, int(self.miner.effectiveness() * self.sizeForMine))

        return ddescription

    @property
    def short_description(self):   # Краткое описание дракона одной фразой
        ddescription = u'  '
        mods = self.modifiers()
        ddescription += self._accentuation(data.dragon_size[self.size - 1], self._gift == 'size') + u' '
        ddescription += self._accentuation(self.color, self.color_eng == self._gift) + u' '
        ddescription += self.kind + u'. '
        return ddescription


    @staticmethod
    def _accentuation(text, condition):
        if condition:
            return '{b}' + text + '{/b}'
        else:
            return text

    def modifiers(self):
        """
        :return: Список модификаторов дракона
        """
        return self.anatomy + \
            [mod for head_color in self.heads for mod in data.dragon_heads[head_color]] + \
            [mod for spell in self.spells if spell in data.spell_unknown for mod in data.spell_unknown[spell]] + \
            [mod for effect in self.spells if effect in data.effects_list for mod in data.effects_list[effect]]

    def max_energy(self):
        """
        :return: Максимальная энергия(целое число)
        """
        return self._base_energy + sum([get_modifier(mod).max_energy for mod in self.modifiers()])

    def energy(self):
        """
        :return: Оставшаяся энергия(целое число)
        """
        return self.max_energy() - self._tiredness

    def drain_energy(self, drain=1, always = False, useEnergyModifier = True):
        """
        :param drain: количество отнимаемой у дракона энергии.
        :return: True если успешно, иначе False.
        """
        # @fdsc
        if self.energy() - drain >= 0 or always:
            self._tiredness += drain

            if useEnergyModifier and 'energy' in self.modifiers():
                for i in range(1, drain):
                    while random.randint(0, 99) <= 20:
                        self._tiredness -= 1

            return True

        return False

    def gain_rage(self, gain=1):
        """
        Увеличивает раздражение дракона на :gain:
        """
        if self.bloodiness + gain <= 5:
            self.bloodiness += gain
            return True
        else:
            self.bloodiness = 5
            return True         
        return False

    @property
    def magic(self):
        """
        :return: Магическая сила(целое число)
        """
        return sum([get_modifier(mod).magic for mod in self.modifiers()])

    @property
    def mana(self):
        """
        :return: Количество текущей маны (магическая сила - использованная мана, целое число)
        """
        return self.magic - self._mana_used

    def drain_mana(self, drain=1):
        """
        :param drain: количество отнимаемой у дракона маны.
        :return: True если успешно, иначе False.
        """
        if self.mana - drain >= 0:
            self._mana_used += drain
            return True
        return False

    @property
    def fear(self):
        """
        :return: Значение чудовищности(целое число)
        """
        return sum([get_modifier(mod).fear for mod in self.modifiers()])

    def rest(self, time_to_sleep):
        
        # @fdsc Сохраняем часть непотраченной энергии
        if time_to_sleep > 1:
            self._tiredness = -self.max_energy() / 2
        else:
            me = self.max_energy()
            self._tiredness = self._tiredness - me + 3 - self.lust + 2 - self.health
            if self._tiredness < -me / 2:
                self._tiredness = -me / 2

        # @fdsc Сохраняем часть непотраченной энергии
        # self._tiredness = 0  # range 0..max_energy
        self.bloodiness = 0  # range 0..5
        self.lust = 3  # range 0..3
        self.hunger = 3  # range 0..3
        self.spells = []  # заклинания сбрасываются
        self._mana_used = 0  # использованная мана сбрасывается
        self.health = 2

    @property
    def color(self):
        """
        :return: Текстовое представление базового цвета дракона
        """
        return data.heads_name_rus[self.color_eng]

    @property
    def color_eng(self):
        """
        :return: Текстовое представление базового цвета дракона
        """
        return self.heads[0]

    @property
    def kind(self):
        """
        :return: Текстовое представление 'вида' дракона
        """
        wings = self.wings
        paws = self.paws
        heads = len(self.heads)
        # Защита от ошибок в случае мёртвого дракона
        if heads == 0:
            return u"останки дракона"
        if wings == 0:
            if heads == 1:
                if paws == 0:
                    return u"ползучий гад"
                else:
                    return u"линдвурм"
            else:
                return u"гидрус"
        else:
            if paws == 0 and heads == 1:
                return u"летучий гад"
            elif paws == 0 and heads > 1:
                return u"многоглавый летучий гад"
            elif paws == 1 and heads == 1:
                return u"виверн"
            elif paws == 1 and heads > 1:
                return u"многоглавый виверн"
            elif paws == 2 and heads == 1:
                return u"дракон"
            elif paws > 1 and heads > 1:
                return u"многоглавый дракон"
            else:
                return u"дракон"  # название для дракона с paws == 3 and heads == 1

    @property
    def size(self):
        """
        :return: Размер дракона(число от 1 до 6)
        """
        return self.modifiers().count('size')

    @property
    def wings(self):
        """
        :return: Количество пар крыльев
        """
        return self.modifiers().count('wings')

    @property
    def paws(self):
        """
        :return: Количество пар лап
        """
        return self.modifiers().count('paws')
    
    @property
    def sizeForMine(self):
        k = 1.0

        if 'clutches' in self.modifiers():
            k = 2.0

        if 'bronze' in self.heads:
            k *= 2.0

        if 'gold' in self.heads:
            k *= 1.1

        return math.sqrt(  self.size + self.paws  ) * k


    def _get_ability(self, used_gifts):
        """
        Возвращает способность, которую может получить дракон при рождении
        """
        dragon_leveling = 2 * ['head']
        if self.size < 6:
            dragon_leveling += (6 - self.size) * ['size']
        if self.paws < 3:
            dragon_leveling += 2 * ['paws']
        if self.wings < 3:
            dragon_leveling += 2 * ['wings']
        dragon_leveling += self.available_features
        # @fdsc < 3
        if self.modifiers().count('cunning') < 8:
            dragon_leveling += 2 * ['cunning']
        if self.heads.count('green') > 0:
            dragon_leveling += 5 * [self._colorize_head()]
        dragon_leveling = [item for item in dragon_leveling if item not in used_gifts]
        if len(dragon_leveling) == 0:
            raise StopIteration
        new_ability = random.choice(dragon_leveling)
        return new_ability

    @property
    def available_head_colors(self):
        return [color for color in data.dragon_heads if color not in self.heads and color not in self.dead_heads]

    @property
    def available_features(self):
        ret = []
        ret += [feature for feature in data.special_features
                if feature not in self.modifiers() and feature != 'clutches']
        if 'clutches' not in self.modifiers() and self.paws > 0:
            ret.append("clutches")
        return ret

    def _colorize_head(self):
        # На всякий случай проверяем есть ли зеленые головы.
        assert self.heads.count('green') > 0
        # На всякий случай проверяем есть ли доступные цвета
        assert len(self.available_head_colors) > 0
        # Возвращаем один из доступных цветов
        return random.choice(self.available_head_colors)

    def decapitate(self):
        """Дракону отрубает голову.
        :rtype: list[str]
        :return:
        """
        if 'unbreakable_scale' in self.spells:
            # потеря заклинания защиты головы
            self.spells.remove('unbreakable_scale')
            return ['lost_head', 'lost_virtual']
        else:
            data.achieve_fail("lost_head")# событие для ачивок
            # жизни закончились, рубим голову (последнюю в списке)
            lost_head = self.heads.pop()
            # ставим её на первое место, чтобы после объединения списков порядок голов не изменился
            self.dead_heads.insert(0, lost_head)
            # потеря головы, если головы закончились - значит смертушка пришла
            if self.heads:
                return ['lost_head', 'lost_' + lost_head]
            else:
                self.die()
                return ['dragon_dead']

    def struck(self):
        """
        вызывается при получении удара, наносит урон, отрубает головы и выдает описание произошедшего
        :return: описание результата удара
        """
        if self.health:
            # до удара self.health > 1 - дракон ранен, self.health = 1 - тяжело ранен
            self.health -= 1
            if self.health:
                return ['dragon_wounded']
            else:
                return ['dragon_wounded', 'dragon_heavily_wounded']
        else:
            return self.decapitate()

    @property
    def injuries(self):
        """ Количество ран дракона
        0 - дракон не ранен
        >0 - ранен
        :rtype: int
        :return: Количество ран дракона
        """
        # TODO: заменить "магическое" число 2
        return 2 - self.health

    @property
    def age(self):
        """ Возраст дракона.
        :rtype: int
        :return: Возраст дракона
        """
        return self._age

    @age.setter
    def age(self, value):
        assert value >= 0
        if hasattr(self, '_age'):
            if int(value) >= self._age:
                self._age = int(value)
        self._age = int(value)

    def add_effect(self, effect_name):
        if effect_name not in self.spells:
            if effect_name in data.spell_unknown or effect_name in data.effects_list:
                self.spells.append(effect_name)
            else:
                raise Exception("Unknown effect: %s" % effect_name)

    @property
    def can_fly(self):
        return 'wings' in self.modifiers() or 'wings_of_wind' in self.modifiers()

    @property
    def can_swim(self):
        return 'swimming' in self.modifiers()

    @property
    def special_places_count(self):
        return len(self.special_places)

    def add_special_place(self, place_name, stage=None):
        """
        :param place_name: название достопримечательности для добавления - ключ для словаря.
        :param      stage: на каком этапе достопримечательность,
            ключ для словаря data.special_places, из которого берется надпись в списке и название локации для перехода.
        Если стадия не указана (None), то ключ удаляется из словаря.
        """
        assert stage is None or stage in data.special_places, "Unknown stage: %s" % stage
        if stage:
            self.special_places[place_name] = stage
        else:
            if place_name in self.special_places:
                del self.special_places[place_name]

    def del_special_place(self, place_name):
        """
        :param place_name: название достопримечательности для удаления - ключ для словаря.
        """
        self.add_special_place(place_name)

    def add_event(self, event):
        assert event in data.dragon_events, "Unknown event: %s" % event
        if event not in self.events:
            self.events.append(event)

    # @fdsc
    def getTreasureMasterEffect(self, QK = 0, isNominal=False):
        QM = self.mana
        QE = self.energy() + QK
        
        if isNominal:
            QM = self.magic
            QE = self.max_energy()

        QM3 = QM*QM*QM
        QE2 = QE*QE
        Q1  = QM3*QE2 + 0.01

        return 1 + QK + math.log(1+self.Treasure_master*Q1+QM3+QE2) / math.log(100)

    def attractiveness(self, girl, lair=False):
        # Страшный дракон существено повышает проблемы с ухаживаниями
        girlQ  = girl.quality + 2 + int(self.fear) + self.bloodiness
        # За девушкой проще ухаживать, если ты крылатый дракон - можно покатать её :)))
        girlQ -= self.wings
        
        # Коэффициент умножения
        K = 1

        # Целоваться с драконом нравится всем девушкам
        if 'tongue' in self.modifiers():
            K += 1

        
        # Если логово украшено, ухаживать за девушками проще
        if lair != False:
            girlQ -= lair.summBrilliance()

        # Ухаживать за девушкой проще, если дракон - драгоценный, а девушка - не "невинная"
        if girl.nature != 'innocent':
            if 'gold' in self.heads:
                girlQ -= K + int(girl.goldWeakness * K / 2)
            if 'silver' in self.heads:
                girlQ -= K
        else:
            if 'silver' in self.heads:
                girlQ -= K
            if 'gold' in self.heads:
                girlQ -= int(girl.goldWeakness * K / 2)

        # Тени могут напугать "невинную" девушку дополнительно к общему страху от головы
        if girl.nature == 'innocent':
            if 'shadow' in self.heads:
                girlQ += 1

        # "Развратным" нравится повышенное влечение
        if girl.nature == 'lust':
            if 'spermtoxicos' in self.modifiers():
                girlQ -= K


        if girl.nature == 'proud':
            # Если девушка гордая, то она чувствует тени и за ней проще ухаживать
            if 'shadow' in self.heads:
                # +2 - компенсация страха и ещё +2 от упрощения к ухаживанию
                girlQ -= 2 + 2

            # "Гордым" не нравится повышенное влечение
            if 'spermtoxicos' in self.modifiers():
                girlQ += 2

        # Золотая сияющая чешуя соблазняет всех девушек
        if 'gold_scale' in self.modifiers():
            girlQ -= 2 + girl.goldWeakness * K

        if girlQ <= 0:
            if girl.quality < 0:
                girlQ = 1
                girlW = 0
            else:
                girlW  = 100 - girlQ * 100 / (girl.quality + 1)
                girlQ  = 1
        else:
            girlW  = 100 / girlQ

        return [girlW, girlQ]

