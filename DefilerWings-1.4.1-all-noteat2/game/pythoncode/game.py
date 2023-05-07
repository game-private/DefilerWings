# coding=utf-8

import random
import data
import girls_data
import mob_data
import girls
import treasures
import chronik
import love
import rape
import summon
from historical import historical
from data import get_modifier
from copy import deepcopy
import renpy.exports as renpy
import renpy.store as store
from characters import Fighter, Mortal, Talker, Thief, Knight, Enemy
from utils import call, tuples_sum, get_random_image
from points import Mobilization, Poverty, Army
from lair import Lair

class Game(store.object):
    _win = False
    _defeat = False
    _dragons_used = 0  # Количество использованных за игру драконов
    lair = None
    _quest = None
    _quest_threshold = None
    _quest_text = None

    def __init__(self, adv_character=None, nvl_character=None):
        """
        :param adv_character: Базовый класс для ADV-режима
        :param nvl_character: Базовый класс для NVL-режима
        """
        self.adv_character = adv_character
        self.nvl_character = nvl_character
        self.mobilization = Mobilization()  # Мобилизацию нужно ввести до того как появится первый дракон
        self.poverty = Poverty()
        self.army = Army()
        self._year = 0  # текущий год
        self.witch_force = 0
        self.vini_vidi_vici = False
        self._quest_time = 0  # год окончания квеста
        self.currentCharacter = None  # Последний говоривший персонаж. Используется для поиска аватарки.
        self.unique = []  # список уникальных действий для квестов
        self.lastQuest = None

        self._dragon = None

        self.narrator = Talker(game_ref=self, kind='nvl')
        self.foe = None
        self.girl = None
        self.romeo = None # Инициализируем Ромео

        self.dragon_parent = None

        self.history = None
        self.history_mod = []  # Список исторических модификаторов
        self.history = historical( name='test',end_year=None,desc='Тест прошёл успешно',image=None)
        self.history_mod.append(self.history)
#        self.historical=historical.historicalgame_ref=self
        self.chronik = chronik.chronik(game_ref=self)  # Инициализируем летопись
        self.chronik.chronik_first_centure()
        self.love = love.love(game_ref=self)  # Инициализируем любовь
        self.rape = rape.rape(game_ref=self)  # Инициализируем изнасилования
        self.summon = summon.summon(game_ref=self)  # Инициализируем призыв деммонов
        self.desperate = 0    # В начале игры отчаяние равно нулю.
        self.mistress_alive = True # Жива ли Тёмная Госпожа
        self.first_meet = True  # Возможна ли первая встреча
        
    @property
    def dragon(self):
        return self._dragon

    @dragon.setter
    def dragon(self, new_dragon):
        self.mobilization.reset()
        new_dragon._gift = None
        self._dragon = new_dragon
        if self._dragons_used > 0:  # Если это не первый дракон, то
          for i in xrange(10):  # цикл по годам
            self.year += 1  # накидываем 10 лет на вылупление и прочие взращивание-ботву
            self.check_history()
#            if (self.year+1)%100==0:
#              self.chronik.chronik_next_century()
        self._dragons_used += 1
        if self.dragon.level == 3:
          self.poverty.reset()
        if not store.freeplay:
            self.set_quest()
        self.thief = None  # Вора не создаем, потому что его по умолчанию нет. Он возможно появится в первый сон.
        self.knight = None  # Рыцаря не создаем, потому что его по умолчанию нет. Он возможно появится в первый сон.
        self.girls_list = girls.GirlsList(game_ref=self, base_character=self.adv_character)
        self.girls_list.spawn_list = []
        self.fear=0       # Страха нет
        self.create_lair()
        self.chronik.remember_dragon(self.dragon)
#        self.chronik.temp_massive(self.dragon.level)

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value >= self._year:
            self._year = value
        else:
            raise Exception("Время не может течь назад")

    # @staticmethod
    def save(self, isFreeGame=False, inBeginGame=False):
        """
        Логика сохранения игры.
        """

        if isFreeGame:
            type=2
        else:
            type=1

        # Пробегает 3, 2, 1
        if not inBeginGame:
            for i in range(3, 0, -1):
                # new = f"{type}-{i}"
                # old = f"{type}-{i+1}"
                new = "%d-%d" % (type, i)
                old = "%d-%d" % (type, i+1)
                renpy.rename_save(new, old)  # Переименовываем старый сейв

            renpy.take_screenshot()  # Делаем скриншот для отображения в сейве
            renpy.save(str(type) + "-1")  # Сохраняем игру


        if self.quest_time % 8 == 7 or inBeginGame:
            renpy.save(str(type) + "-5")

        if self.quest_time % 22 == 21 or inBeginGame:
            renpy.save(str(type) + "-6")


        return True


    def next_year(self):
        """
        Логика смены года.
        Проверки на появление/левелап/рейд рыцаря/вора.
        Изменение дурной славы.
        Попытки бегства женщин.
        Что-то ещё?
        """
        renpy.show_screen("controls_overwrite")
        call(data.game_events["sleep_new_year"])
        self.year += 1
        self.dragon.age += 1

        # @fdsc Размножение девушек в армии
        self.army.girl_breeding()

        # Проверяем номер столетия
#        if (self.year+1)%100==0:
#           self.chronik.chronik_next_century()
        # Платим за службу, проверяется в начале года
        for upgrade in self.lair.upgrades.keys():

            #if type(self.lair.upgrades) == type(self.lair.upgrades[upgrade]) and \
            # if type(self.lair.upgrades[upgrade]) == dict and \
            upgrade_object = self.lair.upgrades[upgrade]
            if 'keys' in dir(upgrade_object) and \
                    'cost' in self.lair.upgrades[upgrade].keys() and \
                    self.lair.upgrades[upgrade]['cost'] != None:
                salary = self.lair.treasury.get_salary(self.lair.upgrades[upgrade]['cost'])
#                self.narrator(u"%s" % salary)
#                self.narrator(u"%s" % salary)
                if salary:
                    if renpy.config.debug:
                        summ = 0
                        for salary_i in salary:
                            summ += salary_i.cost
                        salary_tuple = (self.lair.upgrades[upgrade]['name'], summ - self.lair.upgrades[upgrade]['cost'])
                        self.narrator(u"%s в качестве платы за год воруют: %s ф." % salary_tuple)
                    salary = self.lair.treasury.treasures_description(salary)
                    salary_tuple = (self.lair.upgrades[upgrade]['name'], ' '.join(salary))
                    self.narrator(u"%s в качестве платы за год получают:\n %s" % salary_tuple)
                else:
                    self.narrator(u"%s не получили обещанной платы и уходят." % self.lair.upgrades[upgrade]['name'])
                    if upgrade=='smuggler_guards':
                      self.girls_list.romeo_check()
                    del self.lair.upgrades[upgrade]

        # Проверка на наличие охранников и слуг. Одни без других работать не могут.
        if not ('servant' in self.lair.upgrades or 'gremlin_servant' in self.lair.upgrades):
          if 'smuggler_guards' in self.lair.upgrades:
            self.narrator(u"В отсутствии драконьих слуг контрабандисты не могут обеспечивать себя всем необходимым. Они снимаются с места и уходят. Разумеется, о возвращении полученной платы не может быть и речи!")
            self.girls_list.romeo_check()
            del self.lair.upgrades['smuggler_guards']
          if 'regular_guards' in self.lair.upgrades:
            self.narrator(u"В отсутствии драконьих слуг стражи перессорились, передрались и отправились бесчинствовать в Королевство.")
            self.poverty.value += 1
            del self.lair.upgrades['regular_guards']
          if 'elite_guards' in self.lair.upgrades:
            self.narrator(u"В отсутствии драконьих слуг элитные стражи мгновенно подъели все запасы и оправились  бесчинствовать в Королевство.")
            self.poverty.value += 1
            del self.lair.upgrades['elite_guards']
          if 'poison_guards' in self.lair.upgrades:
            self.narrator(u"Как ни странно, ядовитые стражи оказались самыми диcциплинированными. Они остались на своём посту, временами делая вылазки в ближайшие окрестности. Увы, они не в состоянии ни проследить за пленницами, ни позаботиться о них!")
        # Теперь уходят слуги
        if 'regular_guards' not in self.lair.upgrades and 'elite_guards' not in self.lair.upgrades and 'smuggler_guards' not in self.lair.upgrades:
          if 'servant' in self.lair.upgrades:
            self.narrator(u"Узнав, что они беззащитны перед кровожадными рыцарями и безжалостными героями, драконьи слуги в панике разбежались.")
            self.poverty.value += 1
            del self.lair.upgrades['servant']
          if 'gremlin_servant' in self.lair.upgrades:
            self.narrator(u"Узнав, что они беззащитны перед кровожадными рыцарями и безжалостными героями, гремлины в панике разбежались. Разумеется, о возвращении полученной платы не может быть и речи!")
            del self.lair.upgrades['gremlin_servant']


        # Применяем разруху, накопленную за год, с учетом отстройки
        self.poverty.value -= 1
        for spawn_i in xrange(len(self.girls_list.spawn_list)):
          self.active_spawn=self.girls_list.spawn_list[spawn_i]
#          call("lb_spawn_devastation")
        self.girls_list.spawn_list=[]

        self.poverty.apply_planned()


        # Изменяем уровень мобилизации
        # Для начала считаем желаемый уровень мобилизации
        desired_mobilization = self.dragon.reputation.level - self.poverty.value
        # Затем
        # Затем считаем есть ли разница с текущим уровнем мобилизации
        mobilization_delta = desired_mobilization - self.mobilization.level
        if mobilization_delta != 0:  # И если есть разница
            # Увеличиваем  или  уменьшаем на единицу 
            if mobilization_delta > 0:
                self.mobilization.level += 1
            else:
                self.mobilization.level -= 1
        
        self.fear = self.dragon.reputation.level-self.mobilization.level  # Уровень страха - разность между репутацией дракона и уровнем мобилизации
        self.check_history()  # Просматриваем исторические модификаторы, удаляем те, срок действия которых вышел.

        noPause = 0

        # Если вора нет, то пробуем создать его
        if self.thief is None or self.thief.is_dead:
          self._create_thief()
          if self.thief is None:
              if renpy.config.debug:
                  self.narrator(u"Вор не появился.")
              call(data.game_events["no_thief"])
              noPause += 1
          else:
              if renpy.config.debug:
                  self.narrator(u"Вор появился.")
              self.thief.event("spawn")
        else:  # Иначе пробуем его пустить на дело
          self.thief.event("prepare")
          if random.randint(1,3) == 1:  # C 33% шансом получаем шмотку
#            if random.randint(1,1) == 1:  # C 33% шансом получаем шмотку
            self.thief.event("prepare_usefull")
            self.thief.receive_item(lair=self.lair,)
          else:
            self.thief.event("prepare_useless")
          # @fdsc Было range(6)
          if self.thief.forced_to_rob or random.choice(range(2 + self.dragon.reputation.points)) in range(      1 + len(self.thief.items)):  # Шанс 1 + количество шмота на воре, что он пойдет на дело
 #             self.thief.new_lair=False
            if self.thief.new_lair: # Упс, а дракона-то и нет!
              self.thief.event("no_dragon")
              self.thief.forced_to_rob=False
              self.thief.new_lair=False
            else:
              # Идем на дело
              self.thief.forced_to_rob=True
              self.thief.steal(lair=self.lair, dragon=self.dragon)
          else:
            self.thief.event("find_useless")  # Не смог найти логово дракона
  
        # Если рыцаря нет, то пробуем создать его
        if self.knight is None or self.knight.is_dead:
          self._create_knight()
          if self.knight is None:
            call(data.game_events["no_knight"])
            noPause += 1
          else:
            self.knight.event("spawn")
        else:  # Иначе пробуем его пустить на дело
            # Рыцарь пробует подготовиться получше.
          self.knight.event("prepare")
          if random.randint(1,3) == 1:  # C 33% шансом получаем шмотку
#          if random.randint(1,1) == 1:  # C 33% шансом получаем шмотку
            self.knight.event("prepare_usefull")
            self.knight.enchant_equip(lair=self.lair)
#            self.narrator(u"Рыцарь получил %s" % self.knight.last_received_item.name)
          else:
            self.knight.event("prepare_useless")
          # Шанс 1 + количество небазового шмота на рыцаре из 7, что он пойдет на дело
          # @fdsc Уменьшил шанс, чтобы рыцарь мог собрать больше вещей (было range(7))
          if self.knight.forced_to_challenge or random.choice(range(3 + self.dragon.reputation.points)) in range( 1 + self.knight.enchanted_equip_count):
                # Идем на дело
            if self.knight.new_lair: # Упс, а дракона-то и нет!
              self.knight.event("no_dragon")
              self.knight.forced_to_challenge=False
              self.knight.new_lair=False
            else:
              # if noPause < 1:
              self.pauseForSkip()

              self.knight.forced_to_challenge=True
              self.knight.go_challenge(self.lair,self.dragon)
          else:
            self.knight.event("find_useless")  # Не смог найти логово дракона

        if noPause < 2:
            self.pauseForSkip()

        pc = self.girls_list.prisoners_count_virgins_pregnant()
        # Действия с девушками каждый год
        self.girls_list.next_year()

        # Делаем паузу, если изменилось количество девственниц, беременных, 
        if self.girls_list.prisoners_count_virgins_pregnant(pc):
            self.pauseForSkip()

        return

    # @fdsc
    # https://www.renpy.org/doc/html/store_variables.html?highlight=skip#var-_skipping
    # self.pauseForSkip()
    def pauseForSkip(self):

        if not renpy.config.skipping:
            return

        renpy.config.skipping = False
        # renpy.say(self.narrator, '')
        # self.narrator('')
        ch = self.nvl_character()
        ch('')
        renpy.config.skipping = True

    def isSkip(self):
        return renpy.config.skipping

    def sleep(self):
        """
        Рассчитывается количество лет которое дракон проспит.
        Сброс характеристик дракона.
        """
#        renpy.show_screen("controls_overwrite")
#        call("lb_controls_overwrite")
        if self.witch_st1==4:
          self.witch_st1=5
        call(data.game_events["sleep_start"])
        time_to_sleep = self.dragon.injuries + 1
		# @fdsc
        # Сбрасываем характеристики дракона
        self.dragon.rest(time_to_sleep)
        # Действия с девушками до начала сна
        self.girls_list.before_sleep()
        # Спим
        i = 0
        while self.dragon.is_alive and i < time_to_sleep:
            i += 1
            self.next_year()

            # По идее тут мы должны завершить сон
            # if self.dragon.is_dead:
            #    return
        # Обнуляем накопленные за бодрствование очки мобилизации
        self.dragon.reputation.reset_gain()
        # Действия с девушками после конца сна    
        self.girls_list.after_awakening()
        # Проверка срока выполнения квеста

        # @fdsc Если условия квеста выполнены, позволяем дракону играть дальше без загрузки нового квеста
        if (self.quest_time <= 0) and not store.freeplay and not self.is_quest_has_been_completed:
            mistress_flag = True
            if self.is_quest_complete:
                self.is_quest_has_been_completed = True
                self.quest_time = 1000
                mistress_flag = call('lb_location_mordor_questtime_completed')

            if mistress_flag:
                if self.girls_list.prisoners_count > 0:
                  self.dragon.third(u"Тёмная госпожа призывает своё дитя. Дракон выпускает пленниц.")
                self.girls_list.free_all_girls()
                self.girls_list.next_year()
                self.remove_history()
    #                break
                call('lb_location_mordor_questtime')

        call(data.game_events["sleep_end"])

    def create_foe(self, foe_type):
        """ Создание противника заданного типа

        :param foe_type: Тип создаваемого противника
        :return:
        """
        self.foe = Enemy(foe_type)

    def _create_thief(self, thief_level=None):
        """
        Проверка на появление вора.
        :param thief_level: Начальный уровень вора. Если не указан, то уровень определяется исходя из Дурной славы.
        """
        # Если уровень вора не указан, то идет стандартная проверка на появление.
        if thief_level is None and random.choice(range(1, 5 + (self.dragon.reputation.level + 1), 1)) in \
                    range(self.dragon.reputation.level + 1):
            thief_level = Thief.start_level(self.dragon.reputation.level)
        if thief_level > 0:
            self.thief = Thief(level=thief_level, treasury=self.lair.treasury, game_ref=self)
        else:
            self.thief = None

    def _create_knight(self, knight_level=None):
        """
        Создание рыцаря.
        """
        # Если уровень рыцаря не указан, то идет стандартная проверка на появление.
        if knight_level is None and random.choice(range(1, 5 + (self.dragon.reputation.level + 1), 1)) in \
                    range(self.dragon.reputation.level + 1):
            knight_level = Knight.start_level(self.dragon.reputation.level)
        if knight_level > 0:
            self.knight = Knight(level=knight_level, game_ref=self)
        else:
            self.knight = None

    def create_lair(self, lair_type=None):
        """
        Создание нового логова.
        """
        # Бегут влюблённые
        for girl_i in reversed(xrange(self.girls_list.prisoners_count)):
          self.girl = self.girls_list.prisoners[girl_i]
          if self.girl.love is not None:
            text = u'Благодаря суматохе переезда влюблённые получили отличный шанс на побег!'
            self.narrator(u"%s" %text)
            self.chronik.write_chronik(text,self.dragon.level,self.girl.girl_id)
            self.girls_list.love_escape_ind()


        if lair_type is not None:
        # Выпускаем всех женщин в прошлом логове на свободу. 
            if 'regular_guards' not in self.lair.upgrades and 'elite_guards' not in self.lair.upgrades and len(self.girls_list.prisoners)>0:
              call("lb_lair_without_guards")
              self.girls_list.free_all_girls()
            # Если меняется логово на лучшее - сохраняем сокровищницу
            call("lb_lair_guards_disappear")
            save_treas = self.lair.treasury
            # Создаем новое логово
            self.lair = Lair(lair_type)
            data.achieve_target(self.lair.type_name, "lair")#событие для ачивок
            # Копируем сокровищницу из прошлого логова
            self.lair.treasury = save_treas
        else:
            # определяем логово по умолчанию
            lair_list = []
            mods = self.dragon.modifiers()
            for lair in data.lair_types.iterkeys():
                # просматриваем логова, выдаваемые автоматически при выполнении требований
                if 'prerequisite' in data.lair_types[lair]:
                    prerequisite_list = data.lair_types[lair]['prerequisite']  # получаем список требований к дракону
                    prerequisite_exists = True  # временная переменная для требований
                    for prerequisite in prerequisite_list:  # просматриваем список требований
                        # удостоверяемся, что список требований выполнен
                        prerequisite_exists = prerequisite_exists and prerequisite in mods
                    if prerequisite_exists:
                        # если список требований выполнен, добавляем логово к списку
                        lair_list.append((data.lair_types[lair].name, lair))
            if len(lair_list) == 0:
                lair_type = 'impassable_coomb'  # список логов пуст, выбираем начальное
            elif len(lair_list) == 1:
                lair_type = lair_list[0][1]  # в списке одно логово, выбираем его автоматически
            else:
                lair_list.append((u"Буреломный овраг",'impassable_coomb'))
                lair_list.insert(0, (u"Выберите логово:", None))
                lair_type = renpy.display_menu(lair_list)  # в списке больше одного логова, даём список на выбор
            self.lair = Lair(lair_type)
            data.achieve_target(self.lair.type_name, "lair")# событие для ачивок
        if self.thief is not None:
          self.thief.other_lair()
        if self.knight is not None:
          self.knight.other_lair()
        
        # @fdsc Сохраняем игру в начале каждого квеста
        self.save(store.freeplay, True)


    def set_quest(self):
        # @fdsс
        self.is_quest_has_been_completed = False

        lvl = self.dragon.level
        # проходим весь список квестов
        quests = []
        for quest_i in xrange(len(data.quest_list)):
            quest = data.quest_list[quest_i]

            # находим квест, подходящий по уровню, не уникальный или ещё не выполненный за текущую игру
            is_applicable = ('prerequisite' not in quest or quest['prerequisite'] in self.unique)
            is_applicable = is_applicable and ('unique' not in quest or quest['unique'] not in self.unique)
            is_applicable = is_applicable and quest['min_lvl'] <= lvl <= quest['max_lvl']
            if 'anatomy_required' in quest:
                any_applicable = False
                for require in quest['anatomy_required']:
                    curr_applicable = True
                    for subrequire in require.keys():
                        curr_applicable = curr_applicable and \
                            self.dragon.modifiers().count(subrequire) >= require[subrequire]
                    any_applicable = any_applicable or curr_applicable
                is_applicable = is_applicable and any_applicable
            if is_applicable:
                quests.append(quest)
#        for i in xrange(len(quests)):
#            self.narrator(u"%s, %s" %(quests[i]['task'], lvl))

        # Здесь мы проверяем в цикле, т.к. иногда бывает такое, что последний квест - единственный возможный сейчас (хотя, вообще, странно)
        while self.lastQuest != None and self.lastQuest['task'] == self._quest['task']:
            self._quest    = random.choice(quests)
            if len(quests) <= 1:
                break

        self.lastQuest = self._quest

        # Задание года окончания выполнения квеста
        self._quest_time = self._year
        if 'fixed_time' in self._quest:
            self._quest_time += self._quest['fixed_time']
        if 'lvlscale_time' in self._quest:
            self._quest_time += lvl * self._quest['lvlscale_time']
        # Задание порогового значения, если это необходимо
        self._quest_threshold = 0
        if 'fixed_threshold' in self._quest:
            self._quest_threshold += self._quest['fixed_threshold']
        if 'lvlscale_threshold' in self._quest:
            self._quest_threshold += int( lvl * self._quest['lvlscale_threshold'] )
        self._quest_text = self._quest['text'].format(*[self._quest_threshold])

        # @fdsc Запоминаем количество девушек, которое было в начале выполнения квеста (для квеста girls)
        self._quest_girls  = self.army.girls
        self._quest_elites = self.army.elites


    @property
    def is_quest_complete(self):
        """
        Проверяет выполнен ли квест
        TODO: проверки на выполнение квестов. Сразу после добавления квестов.
        """
        if store.freeplay:
          return False
        task_name = self._quest['task']
        current_level = 0
        reached_list = []
        if task_name == 'autocomplete':  # задача всегда выполнена
            return True
        elif task_name == 'reputation':  # проверка уровня репутации
            current_level = self.dragon.reputation.level
        elif task_name == 'wealth':  # проверка стоимости всех сокровищ
            current_level = self.lair.treasury.wealth
        elif task_name == 'gift':  # проверка стоимости самого дорогого сокровища
            current_level = self.lair.treasury.most_expensive_jewelry_cost
        elif task_name == 'poverty':  # проверка понижения уровня мобилизации из-за разрухи
            current_level = self.mobilization.decrease
        elif task_name == 'offspring':  # проверка рождения потомка
            reached_list.extend(self.girls_list.offspring)
        elif task_name == 'lair':  # проверка типа логова и его улучшений
            reached_list.extend(self.lair.upgrades.keys())
            reached_list.append(self.lair.type_name)
        elif task_name == 'event':  # проверка событий
            reached_list.extend(self.dragon.events)
        # @fdsc Проверка количества девушек, поступивших на службу к Владычице
        elif task_name == 'girls':  # проверка событий
            current_level = self.army.girls - self._quest_girls
        # @fdsc Проверка количества элитных войск, поступивших на службу к Владычице
        elif task_name == 'elite':  # проверка событий
            current_level = self.army.elites - self._quest_elites

        # проверка требований
        if 'task_requirements' in self._quest and type(self._quest['task_requirements']) is str:
            quest_complete = self._quest['task_requirements'] in reached_list
        elif 'task_requirements' in self._quest:
            quest_complete = True
            for require in self._quest['task_requirements']:
                # нужно выполнить весь список требований
                if type(require) is str:
                    reached_requirements = require in reached_list
                else:
                    reached_requirements = False
                    for sub_require in require:
                        if type(sub_require) is str:
                            variant_reached = sub_require in reached_list
                        else:
                            # для этого требования в списке достаточно выполнить один из нескольких вариантов
                            variant_reached = True
                            for var_sub_require in sub_require:
                                variant_reached = variant_reached and var_sub_require in reached_list
                        reached_requirements = reached_requirements or variant_reached
                quest_complete = quest_complete and reached_requirements
        else:
            quest_complete = True
        # проверка препятствий выполнения квеста
        if 'task_obstruction' in self._quest:
            for obstruction in self._quest['task_obstruction']:
                quest_complete = quest_complete and obstruction not in reached_list
        quest_complete = quest_complete and current_level >= self._quest_threshold
        return quest_complete

    def mobilization_description(self):


        ml=self.mobilization.level
        d = []
#        d.append(u"Уровень мобилизации: %s " % ml)
        if ml==0:
          d.append(u" Какой дракон?! В королевстве ничего не слышали ни о каких драконах! (Любые панические доклады полностью игнорируются) \n Земли Вольных народов подобны целочке, жаждущей визита могучего ящера.")
        elif ml>0 and ml<4:
          d.append(u"Королевство полностью отмобилизовано и абсолютно готово к любой атаке. Да. Именно так. Об этом написано в отчётах, а отчёты не могут лгать! \n В реальности же дракон может встретить какое-то сопротивление, но пройдут годы, прежде чем Вольные смогут выделить силы на борьбу с ящером.")
        elif ml>3 and ml<7:
          d.append(u"Усилия людей приносят плоды. Шестерёнки военного механизма пусть со скрипом, но двигаются. Конечно, силы, отправленные Вольными на борьбу с драконом, вряд ли справятся со своей задачей. \n Но тенденция настораживает.")
        elif ml>6 and ml<11:
          d.append(u"Люди медленно запрягают, но быстро ездят. Уже сейчас в охоте на дракона занято столько войск, что их вполне хватит для победы в какой-нибудь маленькой победоносной войне. Грабить и насиловать с каждым годом становится всё сложнее. \n Похоже, с этим пора что-то делать. И срочно. ")
        elif ml>10 and ml<16:
          d.append(u"А вот теперь всё серьёзно. Правители Вольных выжали из своих народов все соки, но смогли-таки организовать надёжную оборону. Все уязвимые места патрулируют всадники на грифонах, океан рассекают многопушечные фрегаты, а сверху за всем этим безобразием следят воздушные корабли цвергов. На земле, в небесах и на море - дракону нигде не укрыться от справедливого возмездия! ")
        elif ml>15:
          d.append(u"Пройдут века, но барды продолжут слагать песни об этом времени. Страдания невинных переполнили чашу терпения высших сил. Тритоны поднялись из морских пучин, ангелы спустились с Небес. Земли Вольных народов защищены настолько надёжно, насколько это вообще возможно. Дракон не пройдёт. \n Если же и это не поможет... значит, для Вольных народов надежды больше нет. ")
        return u"\n".join(d)

    def poverty_description(self):
        ml=self.poverty.value
        d = []
#        d.append(u"Уровень разрухи: %s " % ml)
        if ml==0:
          d.append(u"Вольные народы процветают. Урожаи обильны, рыцари благородны, а девы прекрасны и невинны. \n Пожалуй, после всех испытаний в мире и вправду наступил золотой век.")
        elif ml>0 and ml<4:
          d.append(u"Вольные народы процветают, но в благостную картину то и дело вплетаются тягостные нотки. Разорённые деревни, голодные люди... впрочем, у королевства хватит сил, чтобы помочь всем нуждающимся.  \n Но если отродья Тёмной Госпожи продолжат нападения, ситуация может измениться.")
        elif ml>3 and ml<7:
          d.append(u"В Землях Вольных народов настали трудные времена. Всё больше и больше сожжённых сёл, всё больше и больше голодных беженцев... \n Впрочем, королевство справляется. Пока справляется.")
        elif ml>6 and ml<11:
          d.append(u"В королевстве наступили чёрные дни. Страну заполонили отродья дракона, а армия не в силах прикрыть все опасные направления. Продуктов не хватает, кое-где в городах начинается голод. В народе всё шире и шре ходят слухи о конце света. Союзники людей помогают чем могут, но и у них самих обстановка немногим лучше. \n Планы Тёмной Госпожи планомерно претворяются в жизнь. ")
        elif ml>10 and ml<16:
          d.append(u"Обстановка критическая. В королевстве зреют голодные бунты. Нет семьи, которая не потеряла бы родных из-за драконьих бесчинств. Армия едва-едва прикрывает самые важные направления. \n Может быть, со временем Вольные смогут отстроить потерянное. Но это будет очень, очень нескоро... ")
        elif ml>15:
          d.append(u"Мор, глад и хлад воцарились в Землях Вольных. На мили драконьего полёта - лишь смрад пожарищ и гниющие трупы. Люди прикрывают столицу и ещё несколько ключевых точек, но даже там они не чувствуют себя в безопасности. Всё остальное отдано на откуп дракону. \n Даже спустя века барды станут слагать песни об этом времени, и слёзы выступят на глазах у зрителей. \n Если они вообще будут, эти барды.")
        return u"\n".join(d)

    def fear_description(self):
        ml=self.fear
        d = []
#        d.append(u"Уровень страха: %s " % ml)
        if ml<4:
          d.append(u"Даже если дракон где-то бесчинствует, это проходит мимо массового сознания. Люди твёрдо уверены в том, что Королевство  способно защитить их от любой опасности. \n И так ли это далеко от истины?")
        elif ml>3 and ml<7:
          d.append(u"Люди взволнованы. Злодеяния дракона остаются без ответа, лорды отделываются обещаниями, а не действиями. Победа над ящером маячит в туманной дымке, и не всем доведётся дожить до неё.\n Впрочем, королевство справляется. Пока справляется.")
        elif ml>6 and ml<11:
          d.append(u"В королевстве начинаются волнения. Со всех сторон доносится вопль 'Доколе?!', вопль, остающийся без ответа. Слишком умело действует дракон, не позволяя защитникам скопить достаточные силы. А люди, подавленные происходящим, всё чаще и чаще окунаются в пучины массового психоза. \n Планы Тёмной Госпожи планомерно претворяются в жизнь. ")
        elif ml>10 and ml<16:
          d.append(u"Паника захлестнула королевство. В окрестностях множатся тёмные и изуверские культы, практикующие человечесские жертвоприношения - всё ради победы над драконом, разумеется. Быть красивой девушкой - опасно, разъярённая толпа запросто может линчевать 'драконью подстилку'. Власть лордов и рыцарей с каждым днём становится всё более и более иллюзорной. \n Если так пойдёт и дальше, Вольные с успехом истребят себя сами. ")
        elif ml>15:
          d.append(u"Кто угодно. Абсолютно кто угодно. Ради победы над драконом люди примут любую помощь - чернокнижников, демонов, да хоть самого Ктунху. Лорды... собственно, лорды согласны с мнением своих подданных. \n Похоже, народы решили, что лучше ужасный конец, чем ужас без конца..")
        return u"\n".join(d)

    def desperate_description(self):
        ml=self.desperate
        d = []
#        d.append(u"Уровень отчаяния: %s " % ml)
        if ml==0:
          d.append(u"Несмотря ни на что, Вольные верят в победу. Пока на страже их земель стоят могущественные и непобедимые защитники: тритоны, чащобные стражи, титаны, големы и ангелы - дракон не пройдёт.")
        elif ml==1:
          d.append(u"Один Чемпион пал. Неужели даже самые могущественные защитники бессильны пред этим исчадием Ада?")
        elif ml==2:
          d.append(u"Два Чемпиона пало. Какая судьба ждёт простых людей? ")
        elif ml==3:
          d.append(u"Три Чемпиона пало. Да есть ли хоть кто-то, способный противостоять этому порождению Бездны?!")
        elif ml==4:
          d.append(u"Остался последний непобеждённый Чемпион. Неужели... Вольные... обречены? ")
        elif ml==5:
          d.append(u"Защитники пали. Надежды нет.")
        return u"\n".join(d)

    def summon_description(self): # Процедура призыва демонов активирована
        d = []
        if not self.historical_check('angel_fall'):  # Ангел
          d.append(u"Летают ещё птенчики белопёрые, морали читают, творят добро и причиняют справедливость. Мешают жить честным людям. Вот бы им кто-нибудь перья повыдёргивал, а?\n\n")
        else:
          d.append(u"Всё, отлетались курицы. Боятся со своих сияющих высот сходить, больше издалека мозги полощут. И хорошо. Заканчивается их времечко!\n\n")
        if not self.historical_check('golem_fall'):  # Голем
          d.append(u"Громыхают ещё у цвергов их железные бандуры, а сами коротышки от этого гордятся и наглеют без меры. Цены ломят так, что честным людям торговать невмочь! Вот бы их бандуру кто-нибудь раздолбал, а? \n\n")
        else:
          d.append(u"Всё, сломалась цвергова гордость, и сами коротышки присмирели. Теперь к честным людям с оглядкой подходят, с почтеньицем. И хорошо. Заканчивается их времечко!\n\n")
        if not self.historical_check('triton_fall'):  # Тритон
          d.append(u"Плавают ещё эти снулые рыбины, размахивают своими трезубцами. Обожают честных людей досматривать, торговать мешают. Народ воем воет, сплошной грабёж и разорение. Вот бы этих карасиков кто-нибудь бы прищучил, а? \n\n")
        else:
          d.append(u"Всё, доплавались тритончики, ко дну пошли. Теперь никто к честным людям не пристаёт, торговать не мешает. И хорошо. Заканчивается их времечко!\n\n")
        if not self.historical_check('treant_fall'):  # Чащобные сстражи
          d.append(u"Сидят ещё эти деревья в лесах, ветвями размахивают. Честным людям до этого дела мало, вот только цыпочки лесные гордятся сильно, от простого народа нос воротят. Вот бы это деревце кто-нибудь на дрова бы пустил, а? \n\n")
        else:
          d.append(u"Всё, сгорела эта деревяшка чадным пламенем! И цыпочки эти лесные стали такими хмурыми-хмурыми, смирными-смирными - благодать! Теперь честным людям легче расслабляться стало, отдыхать и душой, и телом. И хорошо. Заканчивается их времечко!\n\n")
        if not self.historical_check('titan_fall'):  # Титаны
          d.append(u"Парят ещё эти гордецы в своих облачных замках, честных людей молниями пужают. Народ, в общем-то,  к грозам привычный, но всё равно непорядок! Вот бы этих переростков кто-нибудь с небес на землю спустил, а? \n\n")
        else:
          d.append(u"Всё, попадали эти грохочущие великаны на землю, да с громким треском! И сразу честным людям жить стало спокойней, так сказать, без опаски перед карой небесной. И хорошо. Заканчивается их времечко!\n\n")
        return u"".join(d)

    def seal_description(self):
        ml=self.summon.seal
        d = []
#        d.append(u"Уровень страха: %s " % ml)
        if ml<=0.2*data.max_summon:
          d.append(u"Мой приятель-маг бает, что культисты для борьбы с драконом хотят демона призвать, да пока что-то у них не выходит. Как по мне, дурная идея. Демон скорее на самих магов кинется, а не с драконом пойдёт махаться. Впрочем, честным людям эти разборки безразличны.")
        elif ml>0.2*data.max_summon and ml<=0.4*data.max_summon:
          d.append(u"Мой приятель-маг бает, что культисты взялись за дело всерьёз. Печати ещё крепки, но долго это не продержится. Помяни моё слово, это добром не кончится!")
        elif ml>0.4*data.max_summon and ml<=0.6*data.max_summon:
          d.append(u"Мой приятель-маг бает, что многие лорды и рыцари присоединились к культистам. Тьфу, просто демоническое помешательство какое-то! Да и печати слабеть начали. Не к добру это, не к добру!")
        elif ml>0.6*data.max_summon and ml<=0.8*data.max_summon:
          d.append(u"Мой приятель-маг бает, что теперь культисты действуют с разрешения короля, да выступит чирей на его заднице. Тьфу! Неужели только честной люд здравомыслие сохранил? Да и печати серьёзно ослабели, ещё немного - и рухнут.")
        elif ml>0.8*data.max_summon and ml<=1.0*data.max_summon:
          d.append(u"Мой приятель-маг сам присоединился к культистам. Бает, что демонополонники теперь есть даже среди альвов и титанов. От печатей - одно название, рухнуть в любой момент могут. Ну что за идиоты, а?")
        elif ml>1.0*data.max_summon and not self.historical_check('archimonde_was'):
          d.append(u"Печати рухнули. Демоны войдут в мир со дня на день. Пойду за солониной и огнивами.")
        elif self.historical_check('archimonde_was'):
          d.append(u"Ну вот, Князь Ада Архитот посетил этот мир. И что, стало от этого кому-нибудь легче?")
        return u"\n".join(d)

    def history_description(self): # Описание модификаторов
        event = False # Проверяем, было ли там вообще хоть что-то.
        d = []
        for i in xrange(len(self.history_mod)):
          if self.history_mod[i].historical_name == 'cathedral_ruined':
            event = True
            d.append(u"Говорят, что на столичный Собор напало какое-то чудо-юдо. Теперь там пусто, голые стены одни, поживиться нечем. По слухам, его в %s э.д. заново украсят. \n\n" %self.history_mod[i].historical_end_year)
          if self.history_mod[i].historical_name == 'brothel_ruined':
            event = True
            d.append(u"Говорят, что на столичный бордель напало какое-то чудо-юдо. Теперь там пусто, только остов остался, ни одной цыпочки не встретишь. По слухам, его в %s э.д. хотят заново открыть. \n\n" %self.history_mod[i].historical_end_year)
          if self.history_mod[i].historical_name == 'brothel_robbed':
            event = True
            d.append(u"Говорят, что хозяйка столичного борделя осерчала ни с того ни с сего, на честных людей со скалкой кидается. Заходить страшно. Но ничего, в %s э.д. успокоится! \n\n" %self.history_mod[i].historical_end_year)
          if self.history_mod[i].historical_name == 'elf_ruined':
            event = True
            d.append(u"Говорят, что дракон осквернил священное Древо альвов, и теперь их народ скитается по лесам, не имея надёжного пристанища. Правда, они посадили новое семечко, но оно только в %s э.д. проклюнется. \n\n" %self.history_mod[i].historical_end_year)
          if self.history_mod[i].historical_name == 'dwarf_ruined':
            event = True
            d.append(u"Говорят, что цверги опять свои Подгорные чертоги потеряли. Ничего, они коротышки упорные, изберут себе нового короля и опять копать пойдут. Глядишь, в %s э.д. отстроят свою крепость заново. \n\n" %self.history_mod[i].historical_end_year)
          if self.history_mod[i].historical_name == 'night_watch':
            event = True
            d.append(u"Говорят, дракон совсем распоясался, приличных девушек со столичного рынка средь бела дня таскает, бесстыдник! Бургомистр наскипидарил городской дозор, чтобы они стражу несли, как положено. Только бесполезно это всё, уже к %s э.д. дозорные опять таверны начнут патрулировать. \n\n" %self.history_mod[i].historical_end_year)
          if self.history_mod[i].historical_name == 'cathedral_guard':
            event = True
            d.append(u"Говорят, дракон монахиню прямо из кафедрального Собора стащил! Храмовники бдят, но у них обеты, они простых людей защищать должны. Глядишь, к %s э.д. опять сельскую местность начнут патрулировать. \n\n" %self.history_mod[i].historical_end_year)
          if self.history_mod[i].historical_name == 'de_Ad':
            event = True
            d.append(u"Говорят, в замке маркиза де Ада опять какая-то мутная история произошла, и теперь его только в %s э.д. новый маркиз займёт. Что именно произошло? То ли дракон кого-то убил, то ли дракона кто-то убил, то ли дракон просто мимо проходил, а всех обитателей замка живые мертвецы съели. Последнее, конечно, враки. Ну кто в наше просвещённое время верит в живых мертвецов? Они бы ещё про суккуб рассказали!\n\n" %self.history_mod[i].historical_end_year)
        if event is False:
          return u"А в остальном тихо всё, спокойно. Ничего интересного."
        else:
          return u"".join(d)

    def check_history(self):  # Проверка истоических модификаторов
#        remove_this=[] # Массив для индексов, подлежащих удалению
        for i in reversed(xrange(len(self.history_mod))):
          if self.year>=self.history_mod[i].historical_end_year and self.history_mod[i].historical_end_year is not None:
#            remove_this.append(i)  
            if self.history_mod[i].historical_desc is not None:
              if self.history_mod[i].historical_image is not None:
                self.historical_image=self.history_mod[i].historical_image
                self.historical_desc=self.history_mod[i].historical_desc
                call ('lb_historical_image')
              else:
                self.narrator(self.history.historical_desc)
#            self.narrator(u"%s" % self.history_mod[i].historical_name)
            if self.history_mod[i].historical_name == 'witch_st1':
              self.witch_st2=1
            del self.history_mod[i]
#        for j in xrange(len(remove_this)):
#            del self.history_mod[remove_this[j]]
    
    def historical_check(self,desc): # Есть ли исторический модификатор?
        name = False
        for i in xrange(len(self.history_mod)):     
          if self.history_mod[i].historical_name == desc:
            name = True
        return name

    def remove_history(self):
        for i in reversed(xrange(len(self.history_mod))):
          if self.history_mod[i].historical_name == 'brothel_known':
            del self.history_mod[i]
        for i in reversed(xrange(len(self.history_mod))):
          if self.history_mod[i].historical_name == 'caravan_trade':
            del self.history_mod[i]

    def complete_quest(self):
        """
        Посчитать текущий квест выполненным
        """
        # добавляем всё неправедно нажитое богатство в казну Владычицы
        self.army.money += self.lair.treasury.wealth
        # указываем, что уникальный квест уже выполнялся
        if 'unique' in self._quest:
            self.unique.append(self._quest['unique'])

    @property
    def quest_task(self):
        return self._quest['task']

    @property
    def quest_text(self):
        return self._quest_text

    @property
    def quest_time(self):
        """
        Сколько лет осталось до конца квеста
        """
        return self._quest_time - self._year

    @quest_time.setter
    def quest_time(self, value):
        self._quest_time = self._year + value

    @property
    def quest_time_text(self):
        number = self.quest_time
        
        post_str = "";
        if self._quest['task'] == 'girls':
            current_level = self.army.girls - self._quest_girls
            post_str = u"\n\nКоличество девушек, поступивших на службу: " + str(current_level)
        elif self._quest['task'] == 'elite':
            current_level = self.army.elites - self._quest_elites
            post_str = u"\n\nКоличество элитных бойцов, поступивших на службу: " + str(current_level)


        if number == 1:
            return u"Последний год на выполнение задания!" + post_str
        elif 1 < number < 5:
            return u"Тебе нужно выполнить задание за %s года!" % str(number) + post_str
        elif (number % 100 > 20) and (number % 10 == 1):
            return u"Задание нужно выполнить за %s год." % str(number) + post_str
        elif (number % 100 > 20) and (1 < number % 10 < 5):
            return u"Задание нужно выполнить за %s года." % str(number) + post_str
        else:
            return u"Задание нужно выполнить за %s лет." % str(number) + post_str

    def choose_spell(self, back_message=u"Вернуться"):
        """
        Выводит меню для выбора заклинания
        :param back_message: название для пункта меню с отказом от выбора.
        :return: При выборе какого-либо заклинания кастует его и возвращает True,
                 при отказе от выбора возвращает False.
        """
        spells_menu = []
        for spell in self.spell_list.keys():

            to_add = False
            # Добавляем в список только актуальные заклинания.
            if spell not in self.dragon.spells and self.spell_list[spell][0] not in self.dragon.modifiers() and spell != 'spellbound_trap':
#                self.narrator(' %s %s' %(spell, self.spell_list[spell][0]))
                to_add = True
            else:
                if spell == 'spellbound_trap':
                    if 'magic_traps' not in self.lair.upgrades:
                        spells_menu.append((self.spell_list_rus['spellbound_trap'], 'spellbound_trap'))
                    elif 'magic_traps2' not in self.lair.upgrades and self.dragon.mana >= 3:
                        spells_menu.append((self.spell_list_rus['spellbound_trap'], 'spellbound_trap2'))
                    elif 'magic_traps3' not in self.lair.upgrades and self.dragon.mana >= 6:
                        spells_menu.append((self.spell_list_rus['spellbound_trap'], 'spellbound_trap3'))
                    elif 'magic_traps4' not in self.lair.upgrades and self.dragon.mana >= 11:
                        spells_menu.append((self.spell_list_rus['spellbound_trap'], 'spellbound_trap4'))

            if to_add:
                spells_menu.append((self.spell_list_rus[spell], spell))

        spells_menu = sorted(spells_menu, key=lambda spell: spell[0])
        spells_menu.append((back_message, 'back'))
        spell_name = renpy.display_menu(spells_menu)
        if spell_name == 'back':
            return False
        else:
            # @fdsc
            if spell_name == 'spellbound_trap':
                self.lair.add_upgrade('magic_traps')
            elif spell_name == 'spellbound_trap2':
                self.lair.add_upgrade('magic_traps2')
                self.dragon.drain_mana(2)   # Всего - 3
            elif spell_name == 'spellbound_trap3':
                self.lair.add_upgrade('magic_traps3')
                self.dragon.drain_mana(5)   # Всего - 6
            elif spell_name == 'spellbound_trap4':
                self.lair.add_upgrade('magic_traps4')
                self.dragon.drain_mana(10)   # Всего - 11
            else:
                self.dragon.add_effect(spell_name)
            return True

    def buff_description(self):
        if len(self.dragon.spells)==0:
          return ''
        else:
          desc=u'{font=fonts/PFMonumentaPro-Regular.ttf}{size=+1} Наложенные чары значительно усиливают дракона \n\n{/size}{/font}'
          for spell in self.dragon.spells:
            desc += data.spell_description_list[spell][0]
          return desc

    def interpolate(self, text):
        """
        Функция заменяющая переменные в строке на актуальные данные игры
        """
        return text % self.format_data

    @property
    def format_data(self):
        substitutes = {
            "dragon_name": self.dragon.name,
            "dragon_name_full": self.dragon.fullname,
            "dragon_type": self.dragon.kind,
#            "girl_name": self.girl.name,
        }
        if self.foe is not None:
            substitutes["foe_name"] = self.foe.name
        return substitutes

    @property
    def is_won(self):
        # Проверка параметров выиграна уже игра или нет
        if not self._win:
            # Проверяем выиграли ли мы
            pass
        return self._win

    def win(self):
        """
        Форсируем выиграть игру
        """
        self._win = True

    @property
    def is_lost(self):
        # Проверка параметров проиграна уже игра или нет
        if not self._defeat:
            # Проверяем проиграли ли мы
            pass
        return self._defeat

    def defeat(self):
        """
        Форсируем проиграть игру
        """
        self._defeat = True