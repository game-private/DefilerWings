# coding=utf-8

import random

from pythoncode import girls_data
from pythoncode.utils import get_random_image

from talker import Talker

import math


class Girl(Talker):
    """
    Базовый класс для всего, с чем можно заниматься сексом.
    """

    def __init__(self, girl_type='peasant', girl_id=0,name_number=None,family=None,*args, **kwargs):
        # Инициализируем родителя
        super(Girl, self).__init__(*args, **kwargs)
        # Указываем тип девушки (крестьянка, гигантша..)
        self.type = girl_type
        # Подбираем аватарку
        self.avatar = get_random_image("img/avahuman/" + girls_data.girls_info[girl_type]['avatar'])
        
        # @Alex: Added haicolor taken from avatar:
        hair_colors = ["black", "blond", "brown", "red", "unknown"]
        fn = self.avatar.split("/")[-1]
        for i in hair_colors:
            if i in fn:
                self.hair_color = i
                break
        else:
            if self.type == 'fire':
              self.hair_color='red'
            elif self.type == 'ice':
              self.hair_color='blond'
            elif self.type == 'titan':
              self.hair_color='blond'
            elif self.type == 'ogre':
              self.hair_color='brown'
            else:
#              self.hair_color = None
              self.hair_color = ''

        # девственность = пригодность для оплодотворения драконом
        self.virgin = True
        self.in_brothel = 0
        self.years_in_brothel = 0
        # беременность: 0 - не беременна, 1 - беременна базовым отродьем, 2 - беременна продвинутым отродьем
        self.pregnant = 0
        self.willing  = False
        # @fdsc Ухаживать за девушкой
        self.willingPercent = 0
        self.goldWeakness = random.randint(0,4) # Девушки по-разному воспринимают золотую чешую и золотую голову дракона
        # Репродуктивное качество женщины.
        # Если коварство дракона превышает её репродуктивное качество, то отродье будет продвинутым. Иначе базовым.
        self.quality = girls_data.girls_info[girl_type]['magic_rating']
        # У девушки есть право на одну неудачную попытку побега из логова. Вторая попытка обязательно удачна.
        self.attemp = False
        # генерация имени
        # Если указано имя берем имя
        if girl_type + '_first' in girls_data.girls_names:
            if name_number is None:
              name_number=random.choice(girls_data.girls_names[girl_type + '_first'].keys())
            self.name = girls_data.girls_names[girl_type + '_first'][name_number][0]
            # Родительный
            self.name_r = girls_data.girls_names[girl_type + '_first'][name_number][1]
            # Дательный
            self.name_d = girls_data.girls_names[girl_type + '_first'][name_number][2]
            # Винительный
            self.name_v = girls_data.girls_names[girl_type + '_first'][name_number][3]
            # Творительный
            self.name_t = girls_data.girls_names[girl_type + '_first'][name_number][4]
            # Предложный
            self.name_p = girls_data.girls_names[girl_type + '_first'][name_number][5]
            # Если есть фамилия, прибавляем к имени фамилию
            if family is not None:
              self.name += " " + family
            elif girl_type + '_last' in girls_data.girls_names:
                self.name += " " + random.choice(girls_data.girls_names[girl_type + '_last'])
        # Не найти имя для девушки, считаем ее неизвестной
        else:
            self.name = 'Неизвестная Красавица'
        self.jailed = False  # была ли уже в тюрьме, пригодится для описания
        self.treasure = []
# Выбираем характер девушки (невинная, гордая, похотливая)
        self.nature = random.choice(girls_data.girls_info[girl_type]['nature'])
# Записываем индекс, под которым девушка войдёт в историю
        self.girl_id = girl_id
        self.love = None # Истинная любовь
        self.dead = False
        self.blind = False  # Слепота
        self.cripple = False # Инвалидность
        self.cripple_image = None # Изображение для инвалидок
        self.gift = None  # Подарок от дракона
        self.talk_was=False  # Был ли разговор о подарке
#        self.death = None # Причина смерти
#        self.live = None # Причина жизни
        if not girls_data.girls_info[self.type]['giantess']:
          self.size=1
        else:
          self.size=3
        
    @property
    def sex_expression(self):
        if self.cripple:
          if self.type == "elf":
            return "elf_amputee"
          else:
            return "amputee"
        else:
          if self.type == "mermaid" or self.type == "elf":
            return self.type
          elif self.type == "siren":
            return "mermaid"
          elif self.type == "danu":
            return "elf"
          else:
            return "girl"

    # @fdsc Стоимость девушек в борделе дракона
    @property
    def get_brothel_price(self):
        if self.cripple or self.blind or self.pregnant > 0 or self.quality < 0:
            return 0

        ye = 1 + pow( self.years_in_brothel, girls_data.girl_brothel_tired_k[self.nature])
        price = girls_data.girl_brothel_price_k[self.nature]
        price = price / ye

        price *= girls_data.girls_info[self.type]['endurance']
        # price /= girls_data.girls_info[self.game.girl.type]['dignity']

        # Чем выше репутация у дракона, тем больше у него посетителей
        # Чем больше разруха, тем меньше посетителей
        # Чем лучше украшено логово, тем больше посетителей
        base_count  = self._gameRef.dragon.reputation.level * (self.quality + 1)
        base_count -= self._gameRef.poverty.value        
        base_count += self._gameRef.lair.summBrilliance()

        if base_count < self.quality:
            base_count = self.quality

        # Это количество мужчин, которые они за год перебирают
        if self.virgin:
            price *= base_count + 10
        else:
            price *= base_count

        return int(math.floor(price))

