#!/usr/bin/env python
# coding=utf-8

# TODO: реврайт вора через modifiers

import random
from pythoncode import data
import renpy.exports as renpy
from pythoncode.utils import call, get_random_image
from pythoncode.data import achieve_fail
from copy import deepcopy
from mortal import Mortal
from talker import Talker
                
                
class Thief(Talker, Mortal):
    """
    Класс вора.
    """
    last_received_item = None

    def __init__(self, level=1, treasury=None, *args, **kwargs):
        super(Thief, self).__init__(*args, **kwargs)
        self._alive = True
        # Проверка что мы можем создать вора указанного уровня
        if level < 1:
            level = 1
        elif level > Thief.max_level():
            level = Thief.max_level()
        self._skill = level
        self._title = data.thief_titles[level - 1]
        self.name = "%s %s" % (random.choice(data.thief_first_names), random.choice(data.thief_last_names))
        self.abilities = data.Container("thief_abilities")
        self.items = data.Container("thief_items")
        # Определяем способности вора
        ability_list = [a for a in data.thief_abilities]  # Составляем список из возможных способностей
        ability_list += [None for _ in range(len(ability_list))]  # Добавляем невалидных вариантов
        for level in range(self._skill):
            ab = random.choice(ability_list)
            if ab is not None and ab not in self.abilities:
                self.abilities.add(ab, deepcopy(data.thief_abilities[ab]))
        # прочее
        self.treasury = treasury  # Ссылка на сокровищницу.
        self.avatar = get_random_image(u"img/avahuman/thief")
        self.forced_to_rob = False    # Обязан ли ограбить дракона, когда тот пойдет спать.
        self.new_lair = False    # Поменял ли дракон логово.

    @property  # Read-Only
    def skill(self):
        return self._skill + self.items.sum("level")

    @property
    def title(self):
        """
        :return: Текстовое представление 'звания' вора.
        """
        return self._title

    def receive_item(self, lair=None):
#        if self.forced_to_rob:
#        item_list = [i for i in data.thief_items if (i not in self.items and data.thief_items[i].provide[0] in lair.requirements)]
        item_list=[]
        for i in data.thief_items:
          if (i not in self.items):
            for req in lair.requirements():
              if req not in (self.abilities.list("provide") + self.items.list("provide")):
                for pr in data.thief_items[i].provide:
                  if req==pr:
                    item_list.append(i)
#                    self ("%s" % i)
        if len(item_list) == 0 or not self.forced_to_rob or self.new_lair:
            # Если логово ещё не найдено или все требования выполнены
#            self ("%s" % len(item_list)) 
          self.check_items(item_list) # Функция для проверки наличия предметов
#          item_list = [i for i in data.thief_items if i not in self.items]
        if len(item_list) > 0:               
          if random.randint(1,4)==1: # Получаем проклятую вещь
            new_item = data.thief_items_cursed[random.choice(item_list)]
          else:
            new_item = data.thief_items[random.choice(item_list)]
          self.items.add(new_item.id, new_item)
          self.last_received_item = new_item
          self.event('receive_item', item=new_item)
          return True
        else:
            return False

    def check_items(self,item_list): # Функция для проверки списка возможных вещей (чтобы не было дублей с способностями)
      for i in data.thief_items:
        if (i not in self.items):
          for j in (data.thief_items[i]["avoids"] + data.thief_items[i]["provide"]):
            if j not in (self.abilities.list("avoids") + self.abilities.list("provide")):
              item_list.append(i)

    def description(self):
        """
        Описание вора, возвращает строку с описанием.
        """
        d = []
        if self.is_dead:
            d.append(u"О воре уже давным-давно ничего не известно")
            return u"\n".join(d)
        d.append(u"Мастерство: %s (%d)" % (self.title, self.skill))
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

    def steal(self, lair=None, dragon=None):
        """
        Вор пытается урасть что-нибудь.
        :param lair: Логово из которого происходит кража
        :param dragon: Дракон, логово которого грабим
        """
        renpy.show_screen("controls_overwrite")
        thief = self

        if lair is None:  # Нет логова, нет краж. Вообще такого быть не должно.
            raise Exception("No lair available")
        if dragon is None:
            raise Exception("No dragon available")

#        self (u"%s" % (thief.items["warming_amulet"].name))
        # Для начала пытаемся понять можем ли мы попасть в логово:
        if not lair.reachable(thief.abilities.list("provide") + thief.items.list("provide")):
          # Добраться не можем
          thief.event("lair_unreachable")
          return
        # Из-за проклятых вещей погибаем в процессе входа в логово
        for req in lair.requirements():
          for pr in data.thief_items_provide[req]:
            if pr in self.items:
              if self.items[pr].cursed:
                ev=pr + "_death"
                thief.event(ev)
                dragon.add_event('thief_killer')
                thief.die()
                return

        thief.event("lair_enter")        
        
        luck = thief.skill
        # Проверка неприступности
#        self.event("checking_accessability")
        # Если нет схемы тайных проходов, то с 33% шансом снижаем удачу вора за каждую единицу неприступности
        if "scheme" in thief.items:
          if self.items["scheme"].cursed:
            x=1
          else:
            x=100
        else:
          x=3
        for i in range(lair.inaccessability):
          if random.choice(range(x)) == 0:
            luck -= 1

        # Проверка, осилили ли неприступность
        if luck < 0:
            thief.die("inaccessability")
            thief.event("die_inaccessability")
            return
#        else:
#            self.event("checking_accessability_success")

        # Проверка ловушек и стражей
#        self.event("trying_to_avoid_traps_and_guards")

        # Выбираем ловушки которые имеет смысл "обходить"
        # Обходим только ловушки с ненулевой защитой
        upgrades = (u for u in lair.upgrades if data.lair_upgrades[u].protection != 0)
        upgrades_sort = sorted(upgrades,key=lambda u: data.lair_upgrades[u].protection)
        for upgrade in upgrades_sort:

#            thief.event("start_trap", trap=upgrade)
            # Если у нас есть шмотка или скилл для обхода ловушки
            if upgrade in thief.abilities.list("avoids"):
              self.event("pass_trap", trap=upgrade,method='abilities')
              continue
            elif upgrade in thief.items.list("avoids"):
              self.event("pass_trap", trap=upgrade,method='items')
                # То переходим к следущей ловушке
              continue
            elif upgrade in thief.items.list("fails"):
              thief.event("die_trap", trap=upgrade,method='items')
              thief.die(upgrade)
              dragon.add_event('thief_killer')
              return

            # 1/3 что вора ловушка заденет
            for i in range(data.lair_upgrades[upgrade].protection):
                if random.choice(range(3)) > 0:
# Mahariel_print
# Удача вора изменяется на случайную величину: 1 или 2.
                    del_luck = random.randint(1,2)
                    luck -= del_luck
# End Mahariel_print


            if luck > 0:
                thief.event("pass_trap", trap=upgrade,method='luck')
            elif luck == 0:
                self.check_retreat()
                return
            elif luck < 0:
                thief.die(upgrade)
                thief.event("die_trap", trap=upgrade,method='unluck')
                dragon.add_event('thief_killer')
                return
            thief.event("end_trap", trap=upgrade)

        attempts = luck
        if "greedy" in thief.abilities:
          attempts += 1
        if "bottomless_sac" in thief.items:
          if not self.items["sleep_dust"].cursed:
            attempts *= 2
          else:
            attempts -= 1

        # У вора кончилась удача, отступаем
        if attempts == 0:
            self.check_retreat()
            return

        # На всякий случай проверяем что у нас еще осталась удача.
        assert attempts > 0

        # Начинаем вычищать логово
        self.event("starting_to_rob_the_lair")

        # Если сокровищница пуста, то вор уходит на пенсию
        if lair.treasury.wealth <= 0:
            self.event("lair_empty")
            # Закончили грабить. Уходим на пенсию.
            self.retire()
            return

        # Берем шмотки
        stolen_items = lair.treasury.rob_treasury(attempts)  # Вор что-то украл
#        thief(u"%s,%s" %(len(stolen_items), thief.skill))
        if 'greedy' in dragon.modifiers():
          por=0
        else:
          por=2
        for i in xrange(len(stolen_items)):
            if "trickster" in thief.abilities:
              self.event("took_an_item_trickster", item=stolen_items[i])
            elif "sleep_dust" in thief.items:
              if not self.items["sleep_dust"].cursed:
                self.event("took_an_item_dust", item=stolen_items[i])
              else:
                self.event("wrong_dust", item=stolen_items[i])
                thief.dragon_kill_thief(dragon,lair,stolen_items)
                return
            elif random.choice(range(10)) in range(por + thief.skill):
                self.event("took_an_item_luck", item=stolen_items[i])
            else:
                # Мы разбудили дракона
                self.event("took_an_item_unluck", item=stolen_items[i])
                thief.dragon_kill_thief(dragon,lair,stolen_items)
                return

        achieve_fail("lost_treasure")  # Отмечаем для ачивки, что потеряли сокровище из-за вора
        self.event('steal_items', items=stolen_items)
        # Закончили грабить. Уходим на пенсию.
        self.retire()
        return

    def check_retreat(self):  # Нужно ли пытаться залезть ещё раз, или пора отступать с концами
        item_list=[]
        self.check_items(item_list)
        if len(item_list)>0:
          self.event("retreat_and_try_next_year")
        else:
          self.event("total_retreat")
          self.retire()

    def dragon_kill_thief(self,dragon,lair,stolen_items):
        dragon.add_event('thief_killer')
        lair.treasury.receive_treasures(stolen_items)  # Дракон возвращает что награбил вор.
        self.event("awakened_the_dragon", stolen_items=stolen_items)
        self.die("wake_up")

    def other_lair(self):  # Дракон меняет логово
        if not self.is_dead and self.forced_to_rob:  # Если вор уже побывал в логове дракона
          self.new_lair = True 
    
    
    def die(self, reason=None):
        """
        Вор умирает
        """
        for i in self.items:
            self.treasury.thief_items.append(deepcopy(self.items[i]))
        self._alive = False

    def retire(self):
        self.event("retire")
        # Делаем вид что умерли и концы в воду.
        self._alive = False
        return

    @staticmethod
    def start_level(reputation=0):
        skill = 0
        for i in range(3 + reputation):
            if random.choice(range(3)) == 0:
                skill += 1
        return skill if skill < Thief.max_level() else Thief.max_level()

    @staticmethod
    def max_level():
        return len(data.thief_titles)

    def event(self, event_type, *args, **kwargs):
        if event_type in data.thief_events:
            if data.thief_events[event_type] is not None:
                call(data.thief_events[event_type], *args, thief=self, **kwargs)
        else:
            raise Exception("Unknown event: %s" % event_type)
        return
