#!/usr/bin/env python
# coding=utf-8

import random
from pythoncode import girls_data, data, mob_data
import renpy.exports as renpy
from fighter import Fighter
from pythoncode.utils import call, get_random_image
from copy import deepcopy


class Knight(Fighter):
    """
    Класс рыцаря.
    """
    last_received_item = None

    def __init__(self, level=1, *args, **kwargs):
        """
        Здесь должна быть генерация нового рыцаря.
        """
        super(Knight, self).__init__(*args, **kwargs)
        self._alive = True
        self.name = u"Сер Ланселот Озёрный"
        self.name = u"Сэр %s %s" % (random.choice(data.knight_first_names), random.choice(data.knight_last_names))
        # Проверка что мы можем создать рыцаря указанного уровня
        if level < 1:
            level = 1
        elif level > Knight.max_level():
            level = Knight.max_level()
        self.power = level
        self._title = data.knight_titles[level - 1]
        self.abilities = data.Container("knight_abilities")
        ability_list = [a for a in data.knight_abilities]  # Составляем список из возможных способностей
        ab = random.choice(ability_list)
        self.abilities.add(ab, deepcopy(data.knight_abilities[ab]))
        self._add_equip_slots(["vest", "spear", "sword", "shield", "horse", "follower"])
        self.equip_basic()
        self.bg = random.choice(filter(lambda path: path.startswith("img/scene/fight/knight/"), renpy.list_files()))
        self.kind = 'knight'
        for description in mob_data.mob[self.kind]['descriptions']:
            descript = deepcopy(description)  # Создаём новый объект для описания
            if len(descript) == 2:
                descript.append(0)  # Добавляем число использований описания
            elif type(descript[2]) is not int:
                descript[2] = 0
            if len(descript) > 3:
                descript = descript[:3]
                # Отсекание лишних данных, если таковые есть
            self.descriptions.append(descript)  # Добавляем в список
        self.avatar = get_random_image(u"img/avahuman/knight")
        self.forced_to_challenge = False    # Обязан ли рыцарь бросить вызов дракону, когда тот пойдет спать.
        self.new_lair = False    # Поменял ли дракон логово.

    def description(self):
        """
        Описание рыцаря, возвращает строку с описанием.
        """
        d = []
        if self.is_dead:
            d.append(u"О рыцаре уже давно никто ничего не слышал")
            return u"\n".join(d)
        d.append(u"Сила: %s (%d)" % (self.title, self.power))
        if self.abilities:
            d.append(u"Способности: ")
            for ability in self.abilities:
                d.append(u"    %s: %s" % (self.abilities[ability].name, self.abilities[ability].description))
        else:
            d.append(u"Способности отсутствуют")
        if self.items:
            d.append(u"Вещи:")
            for item in self.items:
                d.append(u"    %s: %s" % (self.items[item].name, self.items[item].description))
        else:
            d.append(u"Вещи отсутствуют")

        return u"\n".join(d)

    def modifiers(self):
        return self._modifiers + self._ability_modifiers() + self._item_modifiers()

    def _ability_modifiers(self):
        """Возвращает список модификторов из способностей
        :rtype: list
        :return: Cписок модификторов из способностей
        """
        result = []
        for i in self.abilities:
            result.extend(self.abilities[i].modifiers)
        # Освободитель
        #   +1 к защите за каждую крестьянку,
        #   +1 к атаке за каждую богатую и
        #   +1 к атаке и защите за любую другую не великаншу томящуюся в логове дракона
        # богатая - princess
        if 'liberator' in self.abilities:
            for girl in self._gameRef.girls_list.prisoners:
                if girl.type == 'peasant':
                    result += ['def_up']
                elif girl.type == 'princess':
                    result += ['atk_up']
                elif not girls_data.girls_info[girl.type]['giantess']:
                    result += ['atk_up', 'def_up']
        return result

    def _item_modifiers(self):
        """Возвращает список модификторов от вещей
        :rtype : list
        :return: Cписок модификторов от вещей
        """
        result = []
        for i in self.items:
            if self.items[i] is None:
              continue
            result.extend(self.items[i].modifiers)
        if 'mirror_shield' in self.items and (
            'red' in self._gameRef.dragon.heads
            or 'white' in self._gameRef.dragon.heads
            or 'black' in self._gameRef.dragon.heads
            or 'fire_heart' in self._gameRef.dragon.spells
            or 'ice_heart' in self._gameRef.dragon.spells
            or 'poison_heart' in self._gameRef.dragon.spells
            or 'thunder_heart' in self._gameRef.dragon.spells
            or 'lightning_heart' in self._gameRef.dragon.spells
        ):
            result += ['sdef_up', 'sdef_up']
        # В условии указано, что дракон не ранен, потому, что он "вместо" атаки теряет голову.
        if 'dragonslayer_spear' in self.items:
            if self._gameRef.dragon.injuries == 0:
                result += ['atk_up']
            else:
                result += ['decapitator']
        return result

    def attack(self):
        a = super(Knight, self).attack()
        a_base = list(a['base'])
        a_base[0] += self.power
        a['base'] = tuple(a_base)
        return a

    def protection(self):
        p = super(Knight, self).protection()
        p_base = list(p['base'])
        p_base[0] += self.power
        p['base'] = tuple(p_base)
        return p

    @property
    def title(self):
        """Текстовое представление 'звания' рыцаря.
        :rtype : str
        :return: Текстовое представление 'звания' рыцаря.
        """
        return self._title

    def event(self, event_type, *args, **kwargs):
        """

        :type event_type: str
        :param event_type: Строка-идентификатор события из data.knight_events
        :return: None
        :raise Exception: Генерируется исключение если событие не найдено.
        """
        retval = None
        if event_type in data.knight_events:
            if data.knight_events[event_type] is not None:
                retval = call(data.knight_events[event_type], *args, knight=self, **kwargs)
        else:
            raise Exception("Unknown event: %s" % event_type)
        return retval

    def enchant_equip(self, item=None,lair=None):
        """
        Рыцарь готовится к бою улучшая шмот.
        :type item: str
        :param item: id новой вещи для рыцаря, ключ в словаре data.knight_items.
            Если не указан, то будет выбрана не базовая вещь для слотав, в который экипирована базовая.
        :rtype: None
        """
        if self.forced_to_challenge:  # Знает местонахождение логова
          horse_list=[]  # Список коней, необходимых для проникновения в логово
          for i in data.knight_items.select([('type', "horse")]): 
            req=True
            for pr in lair.requirements():
#              self (u"%s" % pr)
              if pr not in data.knight_items[i].list("provide"):
                req=False
                break
            if req:
              horse_list.append(i)
          item=random.choice(horse_list)
#          self (u"%s" % item)

        # Вещь которую надеваем указана
        if item is not None:
            # Проверяем что такая вещь существует
            if item not in data.knight_items:
                raise Exception("Item %s not in data.knight_items")
            new_item_id = item
        # Вещь которую надеваем не указана, определяем что надеть
        else:
            basic_types = [i for i in self.items if self.items[i].basic]  # Какой шмот у рыцаря базового типа
            if len(basic_types) > 0:  # У рыцаря есть не улучшенный шмот
                enchanted_type = random.choice(basic_types)
                new_item_id = random.choice(data.knight_items.select([('type', enchanted_type), ("basic", False)]))
            # Все уже улучшено
            else:
                return
        new_item = deepcopy(data.knight_items[new_item_id])
        new_item.id=new_item_id
        # Implementation of 'magic_vest' modifiers
        if new_item_id == 'magic_vest':
            random_element = random.choice([attack_type
                                            for attack_type
                                            in data.attack_types
                                            if attack_type != 'base'])
            new_item['modifiers'] += [random_element + '_immunity']
        self.equip(new_item)
        self.last_received_item = new_item
        self.event("receive_item", item=new_item)

    @property
    def enchanted_equip_count(self):
        """ Количество небазового шмота на рыцаре.
        :rtype: int
        :return: Количество небазового шмота на рыцаре.
        """
        return len([i for i in self.items if not self.items[i].basic])

    def equip_basic(self):
        """ Одевает рыцаря в базовый шмот
        :return:
        """
        self.equip(deepcopy(data.knight_items.basic_vest))
        self.equip(deepcopy(data.knight_items.basic_spear))
        self.equip(deepcopy(data.knight_items.basic_sword))
        self.equip(deepcopy(data.knight_items.basic_shield))
        self.equip(deepcopy(data.knight_items.basic_horse))
        self.equip(deepcopy(data.knight_items.basic_follower))

    @staticmethod
    def start_level(reputation=0):
        """Начальный уровень рыцаря
        :type reputation: int
        :param reputation: Уровень дурная славы дракона. Чем больше, тем выше будет уровень рыцаря.
        :rtype : int
        :return: сумму (reputation + 2) бросков 1 к 3
        """
        skill = 0
        for i in range(2 + reputation):
            if random.choice(range(3)) == 0:
                skill += 1
        return skill if skill < Knight.max_level() else Knight.max_level()

    @staticmethod
    def max_level():
        return len(data.knight_titles)

    @property
    def intro(self):
        return random.choice([d for d in mob_data.mob['knight']['descriptions'] if 'foe_intro' in d[0]])[1]

    def go_challenge(self,lair=None, dragon=None):
        if not lair.reachable(self.abilities.list("provide") + self.items.list("provide")):
          # Добраться не можем
          self.event("lair_unreachable")
          for i in self.items: # Нет ли у нас ненужной лошади

            if i=="horse" and not self.items[i].basic:
#              self (u"%s,%s" % (self.items[i].basic,i))
              self.event("refuse_horse",item=self.items[i])
              self.equip(deepcopy(data.knight_items.basic_horse)) # Отказываемся от лошади
          return
        if len(self._gameRef.girls_list.prisoners)>0:
          for i in xrange(3):
            girl=random.choice(self._gameRef.girls_list.prisoners)
#            self(u"%s, %s" %(girl.name,girl.girl_id))
          self.event("go_to_lair",girl=girl)
          self.talk_to_girl(girl)
#          self (u"%s" % girl.name)
        else:
          self.event("no_girls")
          self.challenge_begin()

    def talk_to_girl(self,girl):  # Разговор с девушкой
        if girl.cripple: # Калеки
          self.event("talk_cripple",girl=girl)
          self.challenge_begin()
        elif girl.blind: # Слепые
          self.event("talk_blind",girl=girl)
          self.challenge_begin()
        else: # Все остальные
          if girl.love is None:  # Нет возлюбленного
            if girl.type=='mermaid' or girl.nature=='proud': # Подговаривают к самоубийству
              self.event("talk_proud",girl=girl)
              self.challenge_begin()
            elif girl.nature=='lust': # Получают удовльствие
              if girl.type=='ogre': # О, закуска пришла!
                self.event("talk_ogre",girl=girl)
                self.die()
              else:
                self.event("talk_lust",girl=girl)
                self.die()
            elif girl.nature=='innocent': # Пытаются убежать
              self.event("talk_innocent",girl=girl)
          else:  # Есть возлюбленный
            if girl.love.type == 'lizardman':
              self.event("talk_lizardman",girl=girl)
              self.die()
            elif girl.love.type == 'smuggler':
              self.event("talk_smuggler",girl=girl)
            



    def challenge_begin(self,repeate=False):  # Бой всё-таки начался
        self.battle_decision=True
        self.event("challenge_start",repeate=repeate)
        if self.battle_decision:
            fight_result = self.fight_dragon()
            self.event("challenge_end", result=fight_result)


    def fight_dragon(self):
        """Рыцарь отправляется на схвату с драконом
        :return: Результат битвы дракона с рыцарем. 'win'|'defeat'|'retreat'
        :rtype: str
        """
        retval = call("lb_fight", foe=self)
        if renpy.config.debug:
            self("knight post fight %s" % retval)
        if retval == "win":
            self._gameRef.dragon.add_event('knight_killer')
        return retval


    def other_lair(self):  # Дракон меняет логово
        if not self.is_dead and self.forced_to_challenge:  # Если рыцарь уже побывал в логове дракона
          self.new_lair = True 

    def get_pic(self,relative_path):
        files = [f for f in renpy.list_files() if f.startswith(relative_path) and not f.endswith('Thumbs.db')] 
        return random.choice(files)  # получаем название файла

