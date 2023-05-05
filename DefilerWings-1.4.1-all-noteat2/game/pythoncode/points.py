# coding=utf-8

import math

import renpy.store as store
import girls_data
from utils import call
from data import reputation_levels, reputation_gain, game_events, achieve_target, get_description_by_count, dark_army


class Mobilization(store.object):
    base = 0  # Начальная мобилизация
    max = 0  # Масимальная
    _lvl = 0
    decrease = 0  # Уменьшение мобилизации

    def __getinitargs__(self):
        return self.level

    def __init__(self, level=0):
        """
        level - уровень мобилизации
        """
        self.level = level

    @property
    def level(self):  # Текущая мобилизация
        return self._lvl

    @level.setter
    def level(self, value):
        value = int(value)
        if value >= 0:
            if value > self._lvl:
                self.max = value
                self._lvl = value
                if game_events["mobilization_increased"] is not None:
                    call(game_events["mobilization_increased"])
            if value < self._lvl:
                self.decrease += self._lvl - value
                self._lvl = value

    def reset_base(self):
        self.base = self._lvl

    def reset_max(self):
        self.max = self._lvl

    def reset_decrease(self):
        self.decrease = 0

    def reset(self):
        self.reset_base()
        self.reset_max()
        self.reset_decrease()

    @property
    def gain(self):  # Изменение текущей мобилизации от базовой
        return self._lvl - self.base


class Reputation(store.object):
    """
    Дурная слава дракона.
    """
    _rp = 0
    _gain = 0
    _last_gain = 0

    @property
    def points(self):
        """
        Количество очков дурной славы
        """
        return self._rp

    @points.setter
    def points(self, value):  # @fdsc Использовать репутацию
        if value >= 0:
            delta = int(value - self._rp)
            if delta in reputation_gain:
                self._last_gain = delta
                self._gain += delta
                self._rp = int(value)
                achieve_target(self.level, "reputation")
            else:
                if delta > 0:
                    raise Exception("Cannot raise reputation. Invalid gain.")
                else:
                    delta = int(value - self._rp)
                    self._last_gain = delta
                    self._gain += delta
                    self._rp = int(value)
                    achieve_target(self.level, "reputation")

    @property
    def gain_description(self):
        if self._last_gain in reputation_gain:
            return reputation_gain[self._last_gain]
        else:
            # Это только на случай отрицательного прироста
            return reputation_gain[-1]

    @property
    def points_gained(self):
        return self._gain

    def reset_gain(self):
        """
        Обнуляет прибавку к очкам дурной славы. Используется когда, например, дракон спит.
        """
        self._gain = 0

    @property
    def level(self):
        key = 0
        for i in sorted(reputation_levels.keys()):
            if self._rp >= int(i):
                key = int(i)
        return reputation_levels[key]


class Poverty(store.object):
    """
    Счетчик разрухи. При попытке опустить разруху ниже нуля она примет нулевое значение.
    Использование:
    Poverty.value - возвращает текущий уровень разрухи
    Poverty.value += 1 - планирует увеличение разрухи на единицу
    Poverty.value -= 1 - планирует уменьшение разрухи на единицу
    Poverty.apply_value() - Применяет запланированное изменение разрухи
    """
    _value = 0
    _planned = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._planned += value - self._value

    def apply_planned(self):
        """
        Применяем запланированные изменения в разрухе
        """
        callback = False
        
        if self._planned > 0:
            callback = True
        if self._value + self._planned >= 0:
            self._value += self._planned
        else:
            self._value = 0
        self._planned = 0
        if callback and game_events["poverty_increased"] is not None:
            call(game_events["poverty_increased"])

    def reset(self):
        self._value = 0
        self._planned = 0        


class Army(store.object):
    """
    Класс для армии Тьмы
    """

    def __init__(self):
        self._grunts = {'goblin': 1}  # словарь для хранения рядовых войск
        self._elites = {}  # словарь для хранения элитных войск
        self.money = 0  # деньги в казне Владычицы
        self._force_residue = 100  # процент оставшейся силы армии - мощь армии
        self.girls = 0 # Количество девушек-воспроизводителей
        self.girls_derivatives = 0 # Количество уже размножившихся девушек

    # @fdsc Размножение девушек
    # Вызывается в game.py next_year
    def girl_breeding(self):

        # if 'girls' not in dir(self):
        #    self.girls = 0
        # if 'girls_derivatives' not in dir(self):
        #    self.girls_derivatives = 0

        self.girls_derivatives += self.girls


    def add_warrior(self, warrior_type, girls=0):
        """
        Добавляет воина  в армию тьмы. warrior_type - название типа добавляемого воина из словаря girls_data.spawn_info
        """
        if 'girls' not in dir(self):
            self.girls = 0

        if 'elite' in girls_data.spawn_info[warrior_type]['modifier']:
            # воин элитный, добавляется в список элитных 
            warriors_list = self._elites
        else:
            # рядовой воин, добавляется в список рядовых 
            warriors_list = self._grunts
        if warrior_type in warriors_list:
            # такой тип воина уже в списке, просто увеличиваем их число
            warriors_list[warrior_type] += 1
        else:
            # такого типа воина нет в списке, добавляем
            warriors_list[warrior_type] = 1

        # @fdsc Размножение девушек
        if girls > 0:
            self.girls += girls


    @property
    def grunts(self):
        """
        Возвращает число рядовых войск в армии тьмы
        """
        grunts_count = 0
        for grunts_i in self._grunts.values():
            grunts_count += grunts_i
        return grunts_count

    @property
    def grunts_power(self):
        """
        Возвращает число элитных войск в армии тьмы
        """
        res=0
        for name, count in self._grunts.iteritems():
            res += girls_data.spawn_info[name]['power']*count

        return res // 5


    @property
    def grunts_list(self):
        """
        Возвращает список рядовых войск в армии тьмы
        """
        grunts_list = u""
        for grunt_name, grunt_count in self._grunts.iteritems():
            grunts_list += u"%s: %s. " % (girls_data.spawn_info[grunt_name]['name'], grunt_count)
        return grunts_list

    @property
    def elites(self):
        """
        Возвращает число элитных войск в армии тьмы
        """
        elites_count = 0
        for elites_i in self._elites.values():
            elites_count += elites_i
        return elites_count
    
    @property
    def elites_power(self):
        """
        Возвращает число элитных войск в армии тьмы
        """
        res=0
        for elite_name, elite_count in self._elites.iteritems():
            res += girls_data.spawn_info[elite_name]['power']*elite_count

        return res // 5

    @property
    def elites_list(self):
        """
        Возвращает список элитных войск в армии тьмы
        """
        elites_list = u""
        for elite_name, elite_count in self._elites.iteritems():
            elites_list += u"%s: %s. " % (girls_data.spawn_info[elite_name]['name'], elite_count)
        return elites_list

    @property
    def diversity(self):
        """
        Возвращает разнообразие армии тьмы
        """
        # @fdsc Размножение девушек
        diversity = len(self._elites) + (self.girls // 4)
        dominant_number = sorted(self._grunts.values())[-1] // 2
        for number_i in self._grunts.values():
            if dominant_number <= number_i:
                diversity += 1
        return diversity

    @property
    def money_requirements_for_equipment(self):
        return (self.grunts + self.elites*3) * 1000
    
    @property
    def equipment(self):
        """
        Возвращает уровень экипировки армии тьмы
        """
        equipment = 1
        aod_money = self.money
        # @fdsc Было просто (self.grunts + self.elites)
        aod_cost = self.money_requirements_for_equipment
        while aod_money >= aod_cost:
            aod_money //= 2
            equipment += 1
        return equipment

    @property
    def force(self):
        """
        Возвращает суммарную силу армии тьмы по формуле
        (force) = (grunts + 3 * elites) * diversity * equipment * текущий процент мощи
        """
        self.force_clear= (self.grunts_power + 3 * self.elites_power) * self.diversity * self.equipment * math.log(self.girls_derivatives+2)/math.log(2) // 10
#        self.force_clear=1800.

        return self.force_clear* self._force_residue // 100

#    @property
    def power_percentage(self):
        """
        Возвращает текущий процент мощи армии тьмы
        """
        new_force=self.force-200000./self.force
        self._force_residue=100.*new_force/self.force_clear
        return self._force_residue

#    @power_percentage.setter
 #   def power_percentage(self, value):
        """
        Устанавливает текущий процент мощи армии тьмы
        """
#        self._force_residue = value

    @property
    def army_description(self):
        description_str = get_description_by_count(dark_army['grunts'], self.grunts) + '\n'
        description_str += get_description_by_count(dark_army['elites'], self.elites) + '\n'
        description_str += get_description_by_count(dark_army['diversity'], self.diversity - (self.girls//4)) + '\n'
        description_str += get_description_by_count(dark_army['equipment'], self.equipment) + '\n'
        description_str += get_description_by_count(dark_army['force'], self.force) + '\n'

        description_str += u"Бойцы (сила): " + str(self.grunts) + ' (' + str(self.grunts_power) + ')' + ',    ' + str(self.elites) + ' (' + str(self.elites_power) + ')' + "\n"
        description_str += u"Снаряжение: " + str(self.money/self.money_requirements_for_equipment * 100 // 4) + '%\n'
        description_str += u"Девушки и разнообразие: " + str(self.girls) + ", " + str(self.girls_derivatives) + ', '  + str(self.diversity - (self.girls//4)) + '\n'
        description_str += u"Сила: " + str(int(self.force*100/1800)) + '%\n'

        return description_str
