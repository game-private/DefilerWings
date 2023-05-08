# coding=utf-8

from copy import deepcopy

# @fdsc math для среднегеометрического
import math
import data
import treasures


class Lair(object):
    def __init__(self, lair_type="impassable_coomb"):
        self.type_name = lair_type
        self.type = data.Container(lair_type, data.lair_types[lair_type])
        # Список модификаций(ловушки, стражи и.т.п.)
        self.upgrades = data.Container('lair_upgrades')
        if 'provide' in self.type:
            for upgrade in self.type['provide']:
                self.add_upgrade(upgrade)
        # Сокровищиница
        self.treasury = treasures.Treasury()
        self.beast = None   # Нужно, чтобы пленница случайно не завела роман с горгульей.
        
        # @fdsc Повышается защита логова из-за ритуалов
        self.inaccByGirls = 0

    def reachable(self, abilities):
        """
        Функция для проверки доступности логова
        :param abilities: - список способностей у того, кто пытается достичь логова,
            например, для вора: [ 'alpinism', 'swimming' ]
        :return: Возращает True ,если до логова можно добраться и False если нет
        """
        for r in self.requirements():
            if r not in abilities:
                return False
        return True

    # @fdsc
    def reachableSumm(self, abilities):
        """
        Функция для проверки доступности логова
        :param abilities: - список способностей у того, кто пытается достичь логова,
            например, для вора: [ 'alpinism', 'swimming' ]
        :return: Возращает True ,если до логова можно добраться и False если нет
        """
        cnt = 0
        for r in self.requirements():
            if r not in abilities:
                cnt += 1
        return cnt

    def requirements(self):
        """
        :return: Возвращает список способностей которые нужны чтобы достичь логова.
        """
        r = []
        if self.type.require:  # Если тип логова что-то требует добавляем что оно требует
            r += self.type.require
        for u in self.upgrades:  # Тоже самое для каждого апгрейда
            if self.upgrades[u].require:
                r += self.upgrades[u].require
        return r

    @property
    def inaccessability(self):
        # return self.type.inaccessability + self.upgrades.sum("inaccessability")
        # @fdsc
        # Почему-то то, что выше, не работает с магическими ловушками
        
        if not 'inaccByGirls' in dir(self):
            self.inaccByGirls = 0

        return self.type.inaccessability  +\
               self.summInaccessability() +\
               int(self.inaccByGirls // 100)

    # @fdsc
    def summInaccessability(self):
        r = 0
        for u in self.upgrades.values():
            if 'inaccessability' in dir(u) and not u.inaccessability is None:
                r += u.inaccessability

        return int(r)
    
    # @fdsc
    def summProtection(self):
        r = 0
        for u in self.upgrades.values():
            if 'protection' in dir(u) and not u.protection is None:
                r += u.protection

        return int(r)
    
    # @fdsc
    def summBrilliance(self):
        r = 0
        for u in self.upgrades.values():
            if 'brilliance' in dir(u) and not u.brilliance is None:
                r += u.brilliance

        return int(r)

    def add_upgrade(self, upgrade):
        """
        Функция для улучшения логова
        :param upgrade: - название добавляемого апгрейда
        """

        # @fdsc Возможность добавить улучшение повторно
        if upgrade not in self.upgrades:
            #self.upgrades.add(upgrade, deepcopy(data.lair_upgrades[upgrade]))
            self.upgrades.add(upgrade, LairUpgrade(upgrade, data.lair_upgrades[upgrade]))
        else:
            # self.upgrades[upgrade].protection += data.lair_upgrades[upgrade].protection
            old = self.upgrades[upgrade]
            a = data.lair_upgrades[upgrade].protection
            b = old.protection
            old.protection = pow( a*a + b*b  , 0.5)

            self.upgrades[upgrade] = LairUpgrade(upgrade, old)

        # замена улучшений, если это необходимо
        if 'replaces' in self.upgrades[upgrade].keys() and \
            self.upgrades[upgrade]['replaces'] in self.upgrades:
            del self.upgrades[self.upgrades[upgrade]['replaces']]

    @property
    def size(self):  # Функция для определения размера логова
        return 3.+self.inaccessability*3


class LairUpgrade(object):
    def __init__(self, service_name, lair_up_data):
        self.service_name = service_name
        self.name = lair_up_data.name
        self.cost = lair_up_data.cost
        self.inaccessability = lair_up_data.inaccessability
        self.require    = lair_up_data.require
        self.protection = lair_up_data.protection
        self.replaces   = lair_up_data.replaces
        self.success    = deepcopy(lair_up_data.success)
        self.fail       = deepcopy(lair_up_data.fail)
        self.brilliance = lair_up_data.brilliance

    def keys(self):
        return self.__dict__.keys();

    def __getitem__(self, name):
        if name == 'replaces':
            return self.replaces
        if name == 'name':
            return self.name
        if name == 'cost':
            return self.cost

        return None;

