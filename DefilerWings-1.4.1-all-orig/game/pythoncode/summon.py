# coding=utf-8
# Вызвали демона. Бедный демон.
from pythoncode import summon_data
import renpy.exports as renpy
import renpy.store as store
import random
from pythoncode.utils import call, weighted_random

class summon(object):
    def __init__(self,game_ref):
        self.game = game_ref
        self.seal=0

    def battle_init(self): #делаем аватарку для диалогового окна
        self.live={'angel':True,
            'titan':True,
            'golem':True,
            'dragon':True}
        if self.game.mistress_alive:
          self.mistress_help=True
        else:
          self.mistress_help=False
#          self.game.narrator(u"%s" %self.mistress_help)
        self.tank_known=False
        self.dd_approve=True
        self.dragon_dict()   # Словарь для дракона

    def dragon_dict(self):
        self.imps=int(3782)
        summon_data.fighters['dragon']['immune']=[]
        summon_data.fighters['dragon']['protection']=[]
        summon_data.fighters['dragon']['attack']=[]
        if 'fire_immunity' in self.game.dragon.modifiers(): # Огонь
          summon_data.fighters['dragon']['immune'].append('fire')
        if 'ice_immunity' in self.game.dragon.modifiers():  # Лёд
          summon_data.fighters['dragon']['immune'].append('ice')
        if 'lightning_immunity' in self.game.dragon.modifiers(): # Электричество
          summon_data.fighters['dragon']['immune'].append('lightning')
        if 'sound_immunity' in self.game.dragon.modifiers(): # Звук
          summon_data.fighters['dragon']['immune'].append('sound')
        if 'poison_immunity' in self.game.dragon.modifiers(): # Яд
          summon_data.fighters['dragon']['immune'].append('poison')
        if self.game.dragon.size>=5:    # Дробящий
          summon_data.fighters['dragon']['immune'].append('mass')
        if 'tough_scale' in self.game.dragon.modifiers(): # Колющий
          summon_data.fighters['dragon']['immune'].append('prick')
        if 'horns' in self.game.dragon.modifiers():       # Рубящий
          summon_data.fighters['dragon']['immune'].append('cut')
        if self.game.dragon.size==4:    # Защита от дробящего урона
          summon_data.fighters['dragon']['protection'].append('mass')
        # Теперь атаки
        if self.game.dragon.size>=5:    # Дробящий
          summon_data.fighters['dragon']['attack'].append('mass') 
        if 'clutches' in self.game.dragon.modifiers():           # Рубящий
          summon_data.fighters['dragon']['attack'].append('cut')  
        if 'fangs' in self.game.dragon.modifiers():              # Колющий
          summon_data.fighters['dragon']['attack'].append('prick') 
        if 'fire_breath' in self.game.dragon.modifiers():        # Огненный
          summon_data.fighters['dragon']['attack'].append('fire')
        if 'ice_breath' in self.game.dragon.modifiers():         # Ледяной
          summon_data.fighters['dragon']['attack'].append('ice')    
        if 'lightning_breath' in self.game.dragon.modifiers():   # Электрический
          summon_data.fighters['dragon']['attack'].append('lightning')  
        if 'poison_breath' in self.game.dragon.modifiers() or 'poisoned_sting' in self.game.dragon.modifiers() :                           # Ядовитый
          summon_data.fighters['dragon']['attack'].append('poison') 
        if 'sound_breath' in self.game.dragon.modifiers():       # Звуковой
          summon_data.fighters['dragon']['attack'].append('sound')    
#        if 'virtual_head' in self.game.dragon.modifiers(): # Дополнительное очко жизни
 #         summon_data.fighters['dragon']['max_hp']=3
        
    def battle_st1(self):
        renpy.show("bg", what=store.Image("img/archimonde/archimonde_intro.jpg"))
 #       summon_data.fighters['dragon']['max_hp']=2
        self.hp={'titan':summon_data.fighters['titan']['max_hp'],
            'angel':summon_data.fighters['angel']['max_hp'],
            'golem':summon_data.fighters['golem']['max_hp'],
            'dragon':summon_data.fighters['dragon']['max_hp'],
            'architot':summon_data.archimonde['max_hp'] }
        self.mp={'angel':summon_data.fighters['angel']['max_mp'],
            'dragon':self.game.dragon.mana*10}
        self.act_mana=0 # Мана, которая доступна в данный момент.
        self.witch1_used=False
        self.witch2_used=False
        self.witch3_used=False
        self.witch4_used=False
        self.third_phase=False  # Третья фаза
        self.position=['round','forward'] # По умолчанию все стоят спереди
        while self.hp['architot']>0:
          self.dragon_att_chosen=False  # Выбрана ли атака дракона
          self.magic_used=False  # Использовал ли дракон магию
#          self.hp['architot'] -= 1
          self.talk=random.choice(summon_data.archimonde['talk'])
          call("lb_archimonde_talk")
          self.arch_melee_list=[]
          self.desc=u''

          # Первая атака - всегда рукопашная
          kind_attack='att_melee_might'
          self.attack_melee(kind_attack)

          # Вторая атака - на 50% магическая.
          kind_attack=random.choice(['att_melee_might','att_melee_magic'])
          self.attack_melee(kind_attack)

          # Третья атака - на 70% магическая.
          choices = [
              ("att_melee_might", 30),
              ("att_melee_magic", 70)]
          kind_attack=weighted_random(choices)
          self.attack_melee(kind_attack)

          # AOE-атака по  рейду.
          self.arch_range_list=[]
          self.arch_range_type_list=[]
          self.desc += u'\n'
          for i in xrange(1):
            self.attack_range()
#          self.attack_unic()

          # Защита Архитота
          self.arch_def_list=[]
          self.desc += u'\n'
          for i in xrange(3):
            self.arch_defence()
          self.game.narrator("%s" % (self.desc) )
          call ('lb_clear')
          # Целители запасают ману
          for i in self.healer_list: 
            self.mana_shortage=3-self.act_mana
            if (self.mp[i]-self.mana_shortage) >= 0: # Проверяем, осталась ли у нас ещё мана
              self.act_mana+=self.mana_shortage  # Если да, то прибавляем её к актуальной.
              self.mp[i]-=self.mana_shortage  # И вычитаем из резерва
            else:  # Если нет
              self.act_mana+=self.mp[i]  # То подбираем остатки
              self.mp[i]=0
              if self.act_mana ==0:  # Если же и остатков нет...
                self.healer_list.remove(i)
                self.dd_list.append(i)  # То переквалифицируемся из целителей в дд.
                self.game.narrator(u"У целителя иссякла божественная благотать! %s стремглав бросается на врага. Если не закончить бой в ближайшее время, Князь Ада уничтожит всех!" % (summon_data.fighters[i]['name']))
                  
                break  # И ломаем цикл
          call ('lb_clear')
          # Архитот атакует танка
          if (((self.mp['angel']+self.act_mana)<4 and 'angel' in self.healer_list) or ((self.mp['dragon']+self.act_mana)<4 and 'dragon' in self.healer_list)) and 'titan' in self.tank_list and self.live['golem']:
          # Если мана у ангела на исходе, титан и голем меняются местами
            self.game.narrator(u"Понимая, что целитель вот-вот будет не в силах лечить, титан отходит в сторону, уступая место защитника голему.")
            self.tank_list.remove('titan')
            self.tank_list.append('golem')
            self.dd_list.remove('golem')
            self.dd_list.append('titan')
          elif self.hp['angel']<1 and self.tank_list[0]=='titan' and self.live['golem']:
          # Если  ангел не справляется с лечением, титан и голем меняются местами
            self.game.narrator(u"Понимая, что ангел вот-вот погибнет, титан отходит в сторону, уступая место защитника голему.")
            self.tank_list.remove('titan')
            self.tank_list.append('golem')
            self.dd_list.remove('golem')
            self.dd_list.append('titan')
          for i in self.tank_list:
            self.archimonde_attacks_tank(i)  # Атака по танку.
            if not self.live[i]:  # Смерть танка
              if i == 'golem' and self.live['titan']:
                self.game.narrator(u"Увидев, что голем повержен, титан отважно занимает его место.")
                self.tank_list.remove('golem')
                self.dd_list.remove('titan')
                self.tank_list.append('titan')
              elif i == 'golem' and not self.live['titan'] and self.live['angel']:
                self.tank_list.remove('golem')
                self.game.narrator(u"После смерти титана и голема Архитот с лёгкостью уничтожил ангела.")
                self.live['angel']==False
                call('lb_death_angel')
                self.game.narrator(u"В одиночку дракон не продержался против Князя Ада и нескольких секунд.")
                self.live['dragon']==False
                call('lb_death_dragon')
                return
              elif i == 'golem' and not self.live['titan'] and not self.live['angel']:
                self.game.narrator(u"В одиночку дракон не продержался против Князя Ада и нескольких секунд.")
                self.live['dragon']==False
                call('lb_death_dragon')
                return
              elif i== 'titan' and self.live['golem']:  
# ГИПОТЕТИЧЕСКАЯ ситуация, в которой титан-танк погибает раньше голема.
# Такого быть не должно. Но мало ли...
                self.game.narrator(u"Увидев, что титан повержен, голем бесстрастно занимает его место.")
                self.tank_list.remove('titan')
                self.dd_list.remove('golem')
                self.tank_list.append('golem')
              elif i== 'titan' and self.live['angel'] and not self.live['golem']:
                self.game.narrator(u"После смерти титана и голема Архитот с лёгкостью уничтожил ангела.")
                self.live['angel']==False
                call('lb_death_angel')
                self.game.narrator(u"В одиночку дракон не продержался против Князя Ада и нескольких секунд.")
                self.live['dragon']==False
                call('lb_death_dragon')
                return
              elif i== 'titan' and not self.live['angel'] and not self.live['golem']:
                self.game.narrator(u"Когда пал последний защитник, дракон не продержался против Князя Ада и нескольких секунд.")
                self.live['dragon']==False
                call('lb_death_dragon')
                return
              elif i=='dragon':
                return
            self.game.narrator(u"Защитник атакует Князя Ада. Улита едет, когда-то будет.")
            self.hp['architot'] -= 1
          call ('lb_clear')

          # Атака по дамагерам
          for i in self.dd_list:
            self.archimonde_attackes_range(i)  # Атака по рэнджам.
            if not self.live[i] and i=='dragon':
              return
          for i in self.dd_list:
            if not self.live[i]:
              self.dd_list.remove(i)

              
# Архитот атакует целителей
          for i in self.healer_list: 
            self.archimonde_attackes_range(i)  # Атака по рэнджам.
            if not self.live[i] and i=='dragon':
              return
          for i in self.healer_list:
            if not self.live[i]:
              self.healer_list.remove(i)


          call ('lb_clear')
          # Целители лечат
          if 'dragon' in self.healer_list:
            call ('lb_screen_archimonde_main')  # Лечит дракон.
            # Но он может и отказаться от лечения
          if 'dragon' not in self.healer_list:
            for i in self.healer_list:
              for j in self.tank_list: # Наши танки
                if j == 'golem':  # Извините, големов не обслуживаем
                  continue
                self.angel_heal(j)   # Божественное исцеление
              if self.act_mana ==0:
                break
              for j in self.healer_list: # Потом лечим целителей
                self.angel_heal(j)   # Божественное исцеление
              if self.act_mana ==0:
                break
              for j in self.dd_list: # И только потом доходит дело до дд
                if j == 'golem':  # Нет, големов по-прежнему не обслуживаем!
                  continue
                self.angel_heal(j)   # Божественное исцеление
                if self.act_mana ==0:
                  break

          call ('lb_clear')
# Начинаем цикл по дамагерам заново! Теперь пришло их время атаковать
          for i in self.dd_list:
            attack_dd=None  # Чем мы, собственно, Архитота атаковать собрались
            if i == 'dragon':
              call ('lb_screen_archimonde_main')
              if self.dragon_att_chosen in self.arch_def_list: # Если от этой атаки Архитот поставил защиту
                self.game.narrator("%s" % (summon_data.fighters[i]['defence_win'][self.dragon_att_chosen] ))
              else:  # А если не поставил
                self.game.narrator("%s" % (summon_data.fighters[i]['defence_loose'][self.dragon_att_chosen] ))
                self.hp['architot'] -= 2
            else:
            # Атакуют дамагеры
              for k in summon_data.fighters[i]['attack']:  # Перебираем список всех доступных атак
                if k not in self.arch_def_list: # Если от этой атаки Архитот не поставил защиту
                  attack_dd=k   # Выбираем её
                  self.game.narrator("%s" % (summon_data.fighters[i]['defence_loose'][attack_dd] ))
                  self.hp['architot'] -= 2
                  break   # И ломаем цикл
              if attack_dd is None: # Если так ничего и не выбрали
                attack_dd=random.choice(summon_data.fighters[i]['attack'])
                # Выбираем любую.
                self.game.narrator("%s" % (summon_data.fighters[i]['defence_win'][attack_dd] )) # Всё равно не поможет.
          
            
          call ('lb_clear')
#          self.game.narrator(u"Здоровье демона: %s, здоровье голема: %s, резерв маны: %s, актуальная мана: %s" % (self.hp['architot'], self.hp['golem'], self.mp['angel'], self.act_mana))



    def attack_melee(self,kind_attack):   
        # Выбираем ключ атаки
        i=0
        while i<500:  # Мог бы поставить while true, но не люблю бесконечных циклов.
          i+=1
          attack=random.choice(summon_data.archimonde[kind_attack].keys())
          if attack not in self.arch_melee_list:
            break
        # Получаем описание атаки
        self.desc +=summon_data.archimonde[kind_attack][attack] + u'\n'
        self.arch_melee_list.append(attack)

    def attack_range(self): #Здесь мы набираем дистанционные атаки
        # Определяем тип атаки (огненный, ледяной, режущий и т.д.)
        # Проверяем, не выпадала ли такая атака до этого
        i=0
        while i<500:  # Мог бы поставить while true, но не люблю бесконечных циклов.
          i+=1
          kind_attack=random.choice(summon_data.archimonde['att_range'].keys())
          if kind_attack not in self.arch_range_list:
            break
        # Определяем конфигурацию атаки (вперёд, назад или всем вокруг)
        i=0
        while i<500:  # Мог бы поставить while true, но не люблю бесконечных циклов.
          i+=1
          attack=random.choice(summon_data.archimonde['att_range'][kind_attack].keys())
          if attack in self.position:   # Если конфигурация атаки совпадает с местоположением рейда
            break
        self.desc += summon_data.archimonde['att_range'][kind_attack][attack] + u'\n'
        self.arch_range_list.append(kind_attack)
        self.arch_range_type_list.append(attack)

    def attack_unic(self): #Здесь мы набираем дистанционные атаки
        # Определяем тип атаки (огненный, ледяной, режущий и т.д.)
        # Проверяем, не выпадала ли такая атака до этого
        kind_attack=random.choice(summon_data.archimonde['att_unic'].keys())
        attack=random.choice(summon_data.archimonde['att_unic'][kind_attack].keys())
        self.desc += summon_data.archimonde['att_unic'][kind_attack][attack] + u'\n'
        self.arch_range_list.append(kind_attack)
        self.arch_range_type_list.append(attack)

    def arch_defence(self):   # Здесь задаётся защита Архитота.
        # Выбираем ключ защиты
        i=0
        while i<500:  # Мог бы поставить while true, но не люблю бесконечных циклов.
          i+=1
          defence=random.choice(summon_data.archimonde['defence'].keys())
          if defence not in self.arch_def_list:
            break
        # Получаем описание атаки
        self.desc +=summon_data.archimonde['defence'][defence] + u'\n'
        self.arch_def_list.append(defence)

    def archimonde_attackes_range(self,i):  # Архимонд реализует свои дистанционные атаки
          # Атаки Архитота
          for j in xrange(len(self.arch_range_list)):
            attack=self.arch_range_list[j]
            if self.arch_range_type_list[j] not in self.position: 
            # Атака прошла в сторону
              self.game.narrator("%s" % (summon_data.fighters[i]['attack_missed']))
            elif attack in summon_data.fighters[i]['immune']:
            # Атака нарвалась  на иммунитет.
              self.game.narrator("%s" % (summon_data.fighters[i]['attack_useless'][attack] ))
            elif attack in summon_data.fighters[i]['protection']:
            # Атака нарвалась  на защиту.
              if (random.randint(0,1) == 1): # Защита сработала
                self.game.narrator("%s" % (summon_data.fighters[i]['attack_useless'][attack] ))
              else:   # Защита не сработала
                if self.hp[i] == 0 and i=='dragon' and 'unbreakable_scale' in self.game.dragon.spells:
                # потеря заклинания защиты головы
                  self.game.dragon.spells.remove('unbreakable_scale')
                  self.game.narrator(u"Даже великим свойственно ошибаться. Князь Ада Архитот отсёк виртуальную голову дракона, но не смог задеть его самого!")
                else:
                  self.game.narrator("%s" % (summon_data.fighters[i]['attack_hit'][attack] ))
                  self.hp[i] -= 1
            else:  # Атака прошла   
              if self.hp[i] == 0 and i=='dragon' and 'unbreakable_scale' in self.game.dragon.spells:
                # потеря заклинания защиты головы
                self.game.dragon.spells.remove('unbreakable_scale')
                self.game.narrator(u"Даже великим свойственно ошибаться. Князь Ада Архитот отсёк виртуальную голову дракона, но не смог задеть его самого!")
              else:
                self.game.narrator("%s" % (summon_data.fighters[i]['attack_hit'][attack] ))
                self.hp[i] -= 1
            if self.hp[i] <0:
              death = 'lb_death_' + i
              call(death)
              self.live[i]=False
              if i == 'dragon':
                return
              break # Ломаем цикл по атакам  
            # Боец убит
            self.game.dragon.health=self.hp['dragon']

    def archimonde_attacks_tank(self,i):  # Архимонд реализует свои атаки ближнего боя
          # Манёвры вокруг Архитота 
          move=False
          if i == 'titan':
            if self.arch_range_type_list[0]==self.position[1]:
              self.game.narrator(u"Постоянно удерживая внимание демона на себе, титан аккуратно обходит вокруг Князя Ада, вынуждая его повернуться в другую сторону. Это облегчит положение остальных, но теперь гиганту сложнее сосредоточиться на собственной защите.")
              move=True
              self.change_position()
          elif i == 'dragon':
            call ('lb_screen_archimonde_main')
            i=self.tank_list[0]
          # Атаки Архитота
          for j in xrange(len(self.arch_melee_list)):
            attack=self.arch_melee_list[j]
            if attack in summon_data.fighters[i]['immune']:
            # Атака нарвалась  на иммунитет.
              self.game.narrator("%s" % (summon_data.fighters[i]['tank_attack_useless'][attack] ))
            elif attack in summon_data.fighters[i]['protection']:
            # Атака нарвалась  на защиту.
              if (random.randint(0,1) == 1) and not move: # Защита сработала
                self.game.narrator("%s" % (summon_data.fighters[i]['tank_attack_useless'][attack] ))
              else:   # Защита не сработала
                if self.hp[i] == 0 and i=='dragon' and 'unbreakable_scale' in self.game.dragon.spells:
                # потеря заклинания защиты головы
                  self.game.dragon.spells.remove('unbreakable_scale')
                  self.game.narrator(u"Даже великим свойственно ошибаться. Князь Ада Архитот отсёк виртуальную голову дракона, но не смог задеть его самого!")
                else:
                  self.game.narrator("%s" % (summon_data.fighters[i]['tank_attack_hit'][attack] ))
                  self.hp[i] -= 1
            else:  # Атака прошла  
              if self.hp[i] == 0 and i=='dragon' and 'unbreakable_scale' in self.game.dragon.spells:
                # потеря заклинания защиты головы
                self.game.dragon.spells.remove('unbreakable_scale')
                self.game.narrator(u"Даже великим свойственно ошибаться. Князь Ада Архитот отсёк виртуальную голову дракона, но не смог задеть его самого!")
              else:
                self.game.narrator("%s" % (summon_data.fighters[i]['tank_attack_hit'][attack] ))
                self.hp[i] -= 1
            
            # Боец убит
            if self.hp[i] <0:
              death = 'lb_death_' + i
              call(death)
              self.live[i]=False
              if i == 'dragon':
                return
              break # Ломаем цикл по атакам  
            self.game.dragon.health=self.hp['dragon']

    def angel_heal(self,j):   # Божественное исцеление
        if (summon_data.fighters[j]['max_hp']-self.hp[j])==0:
          return  # Лечение не нужно.
        if (summon_data.fighters[j]['max_hp']-self.hp[j])<=self.act_mana:
          # Если маны хватает - вылечим полностью!
          self.act_mana-=summon_data.fighters[j]['max_hp']-self.hp[j]
          self.hp[j]=summon_data.fighters[j]['max_hp']
          self.game.dragon.health=self.hp['dragon']
          self.game.narrator(u"Повинуясь воле ангела, божественная энергия вливается в жертву Архитота. %s полностью излечивается!" % (summon_data.fighters[j]['name']))
        else: # Ну если нет, то частично.
          self.hp[j]+=self.act_mana
          self.game.dragon.health=self.hp['dragon']
          self.act_mana=0
          self.game.narrator(u"Повинуясь воле ангела, божественная энергия вливается в жертву Архитота. Увы, %s излечивается лишь частично - даже у могущества посланца Небес есть свои пределы!" % (summon_data.fighters[j]['name']))

    def change_position(self):  # Сменить позицию
        if self.position[1]=='forward':
          self.position.remove('forward')
          self.position.append('back')
        elif self.position[1]=='back':
          self.position.remove('back')
          self.position.append('forward')

    def battle_st2(self):  # Вторая серия
      while self.minute>0:  # Цикл по минутам
        call ('lb_clear')
        renpy.hide("bg")
        renpy.show("bg", what=store.Image("img/archimonde/imps.jpg"))
        self.game.narrator(u'Осталось всего %s минут, а количество живых бесов - %s!' %(self.minute, self.imps))
        for i in self.dd_list: # Цикл по живым бойцам
          if i=='dragon': # С драконом отдельная история
            call ('lb_clear')
            renpy.hide("bg")
            renpy.show("bg", what=store.Image("img/archimonde/imps.jpg"))
            if self.minute==11:
              renpy.say(self.game.dragon.third, u"%s крайне аккуратно приближается к орде бесов." % self.game.dragon.fullname)
            elif self.minute==10:
              renpy.say(self.game.dragon.third, u"%s осторожно подходит к орде бесов." % self.game.dragon.fullname)
            elif self.minute==9:
              renpy.say(self.game.dragon.third, u"%s бесстрашно врывается в орду бесов." % self.game.dragon.fullname)
            else:
              imp_abil=['mass','fire','ice','sound','poison','lightning']
              self.imp_def=random.choice(imp_abil)
              imp_abil.remove(self.imp_def)
              self.imp_vul=random.choice(imp_abil)
              renpy.say(self.game.dragon.third, u"%s презрительно смотрит на орду бесов." % self.game.dragon.fullname)
              renpy.say(self.game.narrator, u"Бесы лихорадочно колдуют, получая защиту от {color=#ff8100}%s{/color} и уязвимость к {color=#ff8100}%s{/color}." % (summon_data.imp_defence[self.imp_def],summon_data.imp_vulnerable[self.imp_vul]))
            call ('lb_archimonde_dragon_st2')

                
          else:
            x_min=85
            x_max=120
            num=self.num_imps(x_min,x_max)  # Чтобы не убить слишком много бесов
            if i=='angel':
              renpy.hide("bg")
              renpy.show("bg", what=store.Image("img/scene/fight/angel.jpg"))
              self.game.narrator(u'Посланник Небес отважно бросается в толпу адских отродий. Количество бесов, погибших от его меча: %s' % num)
              self.imps=self.imps-num
            if i=='golem':
              renpy.hide("bg")
              renpy.show("bg", what=store.Image("img/scene/fight/golem.jpg"))
              self.game.narrator(u'Боевая машина цвергов бесстрастно вклинивается в бушующую толпу. Количество бесов, задавленных гигантом: %s' % num)
              self.imps-=num
            if i=='titan': 
              renpy.hide("bg")
              renpy.show("bg", what=store.Image("img/scene/fight/titan.jpg"))
              self.game.narrator(u'С рук великана срываются ветвистые молнии. Количество бесов, поверженных титаном: %s' % num)
              self.imps-=num
          if self.imps==1: # Остался один имп
            break
        if self.imps==1: # Остался один имп
          break
        self.minute-=1


    def num_imps(self,x_min,x_max):   # Количество импов
        num=random.randint(x_min,x_max)
#        self.game.narrator(u'%s' % num)
        if num>self.imps-1:
          num=self.imps-1
        return num
   
# Третья фаза   
    def battle_st3(self):
        renpy.show("bg", what=store.Image("img/archimonde/archimonde_intro.jpg"))
 #       summon_data.fighters['dragon']['max_hp']=2
        hp=self.hp['golem']
        summon_data.archimonde['max_hp']=50.
        self.hp={'titan':summon_data.fighters['titan']['max_hp'],
            'angel':summon_data.fighters['angel']['max_hp'],
            'golem':hp,
            'dragon':summon_data.fighters['dragon']['max_hp'],
            'architot':summon_data.archimonde['max_hp'] } # Попробуем пока так
        self.mp={'angel':summon_data.fighters['angel']['max_mp']}
        self.act_mana=self.mp['angel'] # Мана, которая доступна в данный момент.
        self.position=['round','forward'] # По умолчанию все стоят спереди
        self.third_phase=True  # Третья фаза
        while self.hp['architot']>0:
          self.dragon_att_chosen=False  # Выбрана ли атака дракона
          self.magic_used=False  # Использовал ли дракон магию
#          self.hp['architot'] -= 1
          self.talk=random.choice(summon_data.archimonde['talk'])
          call("lb_archimonde_talk")

          # AOE-атака по  рейду.
          self.arch_range_list=[]
          self.arch_range_type_list=[]
          self.desc = u'\n'
#          self.desc += u'%s, %s, %s \n' % (self.hp['architot'],self.hp['golem'],self.act_mana)
          for i in xrange(3):
            self.attack_range()

          # Защита Архитота
          self.arch_def_list=[]
          self.desc += u'\n'
          for i in xrange(5):
            self.arch_defence()
          if len(self.dd_list)==1:
            self.attack_unic()
          self.game.narrator("%s" % (self.desc) )
          call ('lb_clear')   
# Начинаем цикл по дамагерам заново! Теперь пришло их время атаковать
          for i in self.dd_list:
            attack_dd=None  # Чем мы, собственно, Архитота атаковать собрались
            if i == 'dragon':
              call ('lb_screen_archimonde_main')
              if self.dragon_att_chosen in self.arch_def_list: # Если от этой атаки Архитот поставил защиту
                self.game.narrator("%s" % (summon_data.fighters[i]['defence_win'][self.dragon_att_chosen] ))
              else:  # А если не поставил
                self.game.narrator("%s" % (summon_data.fighters[i]['defence_loose'][self.dragon_att_chosen] ))
                self.hp['architot'] -= 2
            else:
            # Атакуют дамагеры
              for k in summon_data.fighters[i]['attack']:  # Перебираем список всех доступных атак
                if k not in self.arch_def_list: # Если от этой атаки Архитот не поставил защиту
                  attack_dd=k   # Выбираем её
                  self.game.narrator("%s" % (summon_data.fighters[i]['defence_loose'][attack_dd] ))
                  self.hp['architot'] -= 2
                  break   # И ломаем цикл
              if attack_dd is None: # Если так ничего и не выбрали
                attack_dd=random.choice(summon_data.fighters[i]['attack'])
                # Выбираем любую.
                self.game.narrator("%s" % (summon_data.fighters[i]['defence_win'][attack_dd] )) # Всё равно не поможет.          
          if self.hp['architot']<=0:  # Если мы УЖЕ убили Архитота
            break  
          call ('lb_clear')

          # Атака по дамагерам
          for i in self.dd_list:
            self.archimonde_attackes_range(i)  # Атака по рэнджам.
            if not self.live[i] and i=='dragon':
              return
          for i in self.dd_list:
            if not self.live[i]:
              self.dd_list.remove(i)
#                call('lb_death_dragon')
                  
# Ангел лечит
          for i in self.healer_list:
            if self.act_mana ==0:
              break
            for j in self.dd_list: # И только потом доходит дело до дд
              if j == 'golem':  # Нет, големов по-прежнему не обслуживаем!
                continue
              self.angel_heal(j)   # Божественное исцеление
              self.mp['angel']=self.act_mana
              if self.act_mana ==0:
                break

    def get_archimonde_pic(self):
        relative_path = "img/archimonde/sex"   # Относительный путь для движка ренпи
        files = [f for f in renpy.list_files() if f.startswith(relative_path) and not f.endswith('Thumbs.db')] 
        return random.choice(files)  # получаем название файла