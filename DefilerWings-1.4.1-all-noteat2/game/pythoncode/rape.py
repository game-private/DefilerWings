# coding=utf-8
import random
import girls_data
from utils import get_random_image

class rape(object):
    def __init__(self,game_ref):
        self.game = game_ref

    def define_full_health(self):   # Задаём полное здоровье
        health=random.randint(80,100)
        endurance=girls_data.girls_info[self.game.girl.type]['endurance']
        self.full_health=health*endurance
        self.actual_health=self.full_health
        self.fail=False  # Конфуза пока не произошло
#       Задаём анатомию девушки
        self.head=True
        self.left_breast=True
        self.right_breast=True
        self.stomach=True
        self.pussy=True

#       Задаём анатомию дракона
        self.fire=False
        self.ice=False
        self.lightning=False
        self.poison=False
        self.sound=False
        self.fear=False
        self.clutches=False
        self.fangs=False
        self.horns=False
        self.string=False
#       Список использованных модификаторов
        self.fire_used=False
        self.ice_used=False
        self.lightning_used=False
        self.poison_used=False
        self.sound_used=False
        self.fear_used=False
        self.clutches_used=False
        self.fangs_used=False
        self.horns_used=False
        self.string_used=False
#       Задаём модификаторы
        if 'fire_breath' in self.game.dragon.modifiers() or 'attackFVirgin' in self.game.dragon.modifiers():
            if not self.game.girl.type == 'fire':
                self.fire=True   # Огонь (кроме головы)
        if 'ice_breath' in self.game.dragon.modifiers() or 'attackIVirgin' in self.game.dragon.modifiers():
            if not self.game.girl.type == 'ice':
                self.ice=True    # Лёд (кроме головы)
        if 'lightning_breath' in self.game.dragon.modifiers() or 'silver_magic' in self.game.dragon.modifiers() or 'attackLVirgin' in self.game.dragon.modifiers():
            if not self.game.girl.type == 'titan':
                self.lightning=True # Электричество (кроме головы)
        if 'poison_breath' in self.game.dragon.modifiers() or 'attackPVirgin' in self.game.dragon.modifiers():
          self.poison=True   # Ядовитое дыхание  (кроме головы)
        if 'sound_breath' in self.game.dragon.modifiers() or 'attackSVirgin' in self.game.dragon.modifiers():
          self.sound=True   # Звук (голова)
        if 'fear_of_dark' in self.game.dragon.modifiers() or 'aura_of_horror' in self.game.dragon.modifiers() or 'ugly' in self.game.dragon.modifiers() or 'uglyVirgin' in self.game.dragon.modifiers():
          self.fear=True   # Ужас тьмы (голова)
        if 'clutches' in self.game.dragon.modifiers():
          self.clutches=True   # Когти (груди, влагалище и голова)
        if 'fangs' in self.game.dragon.modifiers():
          self.fangs=True   # Клыки (груди)
        if 'horns' in self.game.dragon.modifiers():
          self.horns=True   # Рога (Голова)
        if 'poisoned_sting' in self.game.dragon.modifiers():
          self.string=True   # Жало (Груди и влагалище)

#       Определяем размер дракона при изнасиловании
        if not girls_data.girls_info[self.game.girl.type]['giantess']:
          if self.game.dragon.size > 3:
            self.size=3
          elif self.game.dragon.size < 4:
            self.size=self.game.dragon.size
        else:
          if self.game.dragon.size > 3:
            self.size=self.game.dragon.size-3
          elif self.game.dragon.size < 4:
            self.size=1
#       Определяем физиологию


    def define_full_proud(self):   # Задаём полную гордость
        dignity=random.randint(80,100)
        proud=girls_data.girls_info[self.game.girl.type]['dignity']
        self.full_proud=dignity*proud
        if self.game.girl.nature == 'proud':
          self.actual_proud=self.full_proud
        elif self.game.girl.nature == 'innocent':
          
          self.actual_proud=0.66*self.full_proud
        elif self.game.girl.nature == 'lust':
          self.actual_proud=0.33*self.full_proud

    def define_rage(self):
        self.rage=10*self.game.dragon.bloodiness

    def define_freedom(self):  # Определяем свободу
        self.arms=True
        self.legs=True
        self.body=True
        self.erection=0  # Эрекция дракона

# Определяем грудь
    def set_breast(self,side):
        self.breast=side

    @property
    def left_breast_possible(self):   # Левая грудь
        if self.left_breast and(self.fire or self.ice or self.lightning or self.poison or self.clutches or self.fangs or self.string):
          left_breast=True
        else:
          left_breast=False
        return left_breast

    @property
    def right_breast_possible(self): # Левая грудь
        if self.right_breast and(self.fire or self.ice or self.lightning or self.poison or self.clutches or self.fangs or self.string):
          right_breast=True
        else:
          right_breast=False
        return right_breast

    @property
    def head_possible(self): # Голова
        if self.head and(self.sound or self.fear or ((self.horns or self.clutches) and not (self.game.girl.type == 'afrodita' or self.game.girl.type == 'danu') )):
          head=True
        else:
          head=False
        return head

    @property
    def stomach_possible(self): # Живот
        if self.stomach and(self.fire or self.ice or self.lightning or self.poison):
          stomach=True
        else:
          stomach=False
        return stomach

    @property
    def pussy_possible(self): # Лоно
        if self.pussy and(self.fire or self.ice or self.lightning or self.poison or self.clutches or self.string):
          pussy=True
        else:
          pussy=False
        return pussy

    @property
    def is_bdsm_possible(self):
        if self.left_breast_possible or self.right_breast_possible or self.head_possible or self.stomach_possible or self.pussy_possible:
          bdsm=True
        else:
          bdsm=False
        return bdsm

    def blind_avatar(self):
        girl_type = self.game.girl.type
        if girl_type == 'fire' or girl_type == 'ice' or girl_type == 'titan' or girl_type == 'ogre' or girl_type == 'mermaid' or girl_type == 'siren':
          self.game.girl.avatar = get_random_image(u"img/blind/" + girls_data.girls_info[girl_type]['avatar'])
        elif girl_type == 'jasmine':
          self.game.girl.avatar = u"img/blind/jasmine.jpg"
        elif self.game.girl.avatar == u"img/avahuman/peasant/black.jpg":
          self.game.girl.avatar = u"img/blind/peasant_black_01.jpg"
        elif self.game.girl.avatar == u"img/avahuman/peasant/black (10).jpg":
          self.game.girl.avatar = u"img/blind/peasant_black_10.jpg"
        elif self.game.girl.avatar == u"img/avahuman/princess/blond (9).jpg":
          self.game.girl.avatar = u"img/blind/princess_blond_09.jpg"  
        elif self.game.girl.avatar == u"img/avahuman/princess/blond (11).jpg":
          self.game.girl.avatar = u"img/blind/princess_blond_11.jpg" 
        elif self.game.girl.avatar == u"img/avahuman/princess/red (2).jpg":
          self.game.girl.avatar = u"img/blind/princess_red_02.jpg"  
        elif self.game.girl.avatar == u"img/avahuman/princess/red (04).jpg":
          self.game.girl.avatar = u"img/blind/princess_red_04.jpg" 
        else:
          self.game.girl.avatar = get_random_image(u"img/blind/" + girls_data.girls_info[girl_type]['avatar'] + "_" + self.game.girl.hair_color)          

        return



        
        

