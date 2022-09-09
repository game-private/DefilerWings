# coding=utf-8
import girls_data
from pythoncode import treasures

class chronik(object):
    def __init__(self,game_ref):
        self.game = game_ref
        self.chronik_girl_name=[]
        self.chronik_girl_desc=[]
        self.chronik_girl_nature=[]
        self.chronik_girl_story=[]
        self.chronik_girl_avatar=[]
        self.tot_girl_id=0  # Общее количество оперируемых девушек
        self.death_reason={}  # Причины несчастных исходов
        self.tot_dead=0   # Общее количество смертей
        self.live_reason={}  # Счастливые исходы
        self.tot_live=0   # Общее количество счастливых исходов
        self.chronik_dragon=[]      # Текущий дракон
        self.chronik_dragon_desc=[] # Описание (краткое) дракона
        self.birth_date=[]     # Дата рождения
        self.death_date=[]     # Дата смерти
        self.chronik_image=[]  # Изображение бг.
        self.chronik_centuary_number=0 # Номер столетия
        self.chronik_century=[] # Название столетия
        self.chronik_history=[] # Летопись по столетиям

#        self.chronik_girl_name=u"Даша"


    def remember_dragon(self,current_dragon): # Запоминает дракона        
        self.chronik_dragon.append(current_dragon.fullname)
        self.chronik_dragon_desc.append(current_dragon.short_description)
        self.chronik_girl_name.append([])  
        self.chronik_girl_desc.append([])
        self.chronik_girl_nature.append([])
        self.chronik_girl_story.append([])
        self.chronik_girl_avatar.append([])
        self.birth_date.append([])
        self.death_date.append([])
        self.chronik_image.append([])
        self.girl_id = -1



    def remember_girl(self,dragon_lev,current_girl,girl_year):  # Я тебя никогда не забуду...
        dragon_lev -=1  # Потому что в Питоне, в отличие от нормальных языков программирования, индексы начинаются с нуля
        self.chronik_girl_name[dragon_lev].append(current_girl.name)
        self.chronik_girl_desc[dragon_lev].append(girls_data.girls_info[current_girl.type]['description'])
        self.chronik_girl_nature[dragon_lev].append(girls_data.nature_info[current_girl.nature])
        self.chronik_girl_story[dragon_lev].append(u"{font=fonts/PFMonumentaPro-Regular.ttf}\n Год %s эпохи дракона \n{/font}" % self.game.year)
        self.chronik_girl_avatar[dragon_lev].append(current_girl.avatar)
        # Определяем дату рождения девушки
        if girl_year is None:
          if current_girl.type == 'elf':
            bd=self.game.year-118
          elif current_girl.type == 'ice' or current_girl.type == 'fire' or current_girl.type == 'ogre' or current_girl.type == 'titan' or current_girl.type == 'siren':
            bd=self.game.year-318
          else:
            bd=self.game.year-18   # Все персонажи совершеннолетние :-) :D
        else:   # Дата задана прямо
          bd=girl_year
        if bd<0:
          bd=-1*bd
          self.birth_date[dragon_lev].append(u"%s до э.д." % bd)
          bd=-1*bd
        else:
          self.birth_date[dragon_lev].append(u"%s э.д." % bd)
        self.death_date[dragon_lev].append(u"н.в.")
        self.chronik_image[dragon_lev].append(None)
        return bd
#u"Даша"

# Описание для кнопки
    def botton_dragon_description(self):    # Описание кнопки дракона
        d = u"{font=fonts/AnticvarShadow.ttf}%s, %s {/font}" % (self.chronik_dragon[self.active_dragon_botton], self.chronik_dragon_desc[self.active_dragon_botton])
        return d

    def botton_description(self):
        d = u"{font=fonts/AnticvarShadow.ttf} %s, %s, %s (%s - %s){/font}" % (self.chronik_girl_name[self.active_dragon][self.active_girl_botton], self.chronik_girl_desc[self.active_dragon][self.active_girl_botton], self.chronik_girl_nature[self.active_dragon][self.active_girl_botton], self.birth_date[self.active_dragon][self.active_girl_botton], self.death_date[self.active_dragon][self.active_girl_botton])
        return d



    def description(self):
        d = u"{font=fonts/AnticvarShadow.ttf}{size=+5} %s, %s, %s {/size}{/font} \n %s" % (self.chronik_girl_name[self.active_dragon][self.active_girl], self.chronik_girl_desc[self.active_dragon][self.active_girl], self.chronik_girl_nature[self.active_dragon][self.active_girl], self.chronik_girl_story[self.active_dragon][self.active_girl] )
        return d

    def set_active_girl(self, girl_i):
# Сохраняем индекс выбранной девушки
#        self.game.girl = self.prisoners[index]
        self.active_girl = girl_i

    def set_active_girl_botton(self, girl_i):
# Сохраняем индекс выбранной девушки. Нужно делать дважды - для кнопки и основного описания
#        self.game.girl = self.prisoners[index]
        self.active_girl_botton = girl_i

    def set_active_dragon(self, dragon_i):
# Сохраняем индекс выбранного дракона
        self.active_dragon = dragon_i

    def set_active_dragon_botton(self, dragon_i):
# Сохраняем индекс выбранного дракона. Это - для кнопки
        self.active_dragon_botton = dragon_i

    def set_active_centure(self, scroll_i):
# Сохраняем индекс выбранного столетия
        self.active_centure = scroll_i

# Здесь мы вынимаем строку из массива, добавляем описание и засовываем обратно
    def write_chronik(self,text,dragon_lev,girl_i):
        dragon_lev -=1  # Потому что в Питоне, в отличие от нормальных языков программирования, индексы начинаются с нуля
        edit_text=self.chronik_girl_story[dragon_lev][girl_i]
        edit_text += text
        self.chronik_girl_story[dragon_lev][girl_i]= edit_text

    def write_image(self,image,dragon_lev,girl_i):  # Запоминаем изображение
        dragon_lev -=1  # Потому что в Питоне, в отличие от нормальных языков программирования, индексы начинаются с нуля
        self.chronik_image[dragon_lev][girl_i]=image

    @property
    def chronik_girl_count(self):
# Возвращает количество запомненных девушек
        return len(self.chronik_girl_name[self.active_dragon])

    @property
    def chronik_dragon_count(self):
# Возвращает количество запомненных драконов
        return len(self.chronik_dragon)

    def chronik_first_centure(self):
        self.chronik_century.append(u"{font=fonts/PFMonumentaPro-Regular.ttf}\n Век %s э.д.  \n{/font}" % self.chronik_centuary_number )
        self.chronik_history.append([])
        self.chronik_history[self.chronik_centuary_number]=u"{font=fonts/AnticvarShadow.ttf}{size=+10} Век %s Эпохи Достатка \n\n {/size}{/font} \n Се летопись славных деяний Королевства нашего,  которое существовало бессчётные века, и будет существовать вечно. Се перечень событий, радостных и печальных, которые ожидают нас в грядущем. Да будут они записаны здесь без гнева и страха, без скорби и ликования, мной и теми, кто будет после меня. \n\n Знайте же, люди и прочие Народы Вольные, что нам пришлось пройти чрез страшные времена. Тёмная Госпожа, олицетворение зла и блуда, возжелала захватить Земли Вольных и сами Небеса. Неисчислимы были полчища её, затмевали они землю от края до края. Но сплотились Вольные Народы. Громыхала техника цвергов, лёгким был шаг детей Дану, вскипали воды от гнева детей Дагона, и сами титаны сошли со своих Небес. Сплотились Народы вокруг Королевства, и вся мощь Тёмной Госпожи, блудливого порождения ада, оказалась бессильна. \n\n Сбежала демоница в бесплодные пустоши, забрав с собой остатки воинств своих. Исчезла опасность, грозившая Народам Вольным, и в честь события этого уговорились мы начать отсчёт новой эпохи, названной Эпохой Достатка. Ибо хотя остались недобитки Тёмной Госпожи в землях наших, и шныряют странные ящерицы, драконами именуемые, безоблачно будущее Королевства. Воистину, нет теперь препятствий для устойчивого развития!" % self.chronik_centuary_number

    def chronik_next_century(self):
        self.chronik_centuary_number=((self.game.year+1)%100)-1 # Номер столетия
        self.chronik_century.append(u"{font=fonts/PFMonumentaPro-Regular.ttf}\n Век %s э.д.  \n{/font}" % self.chronik_centuary_number) # Запоминаем название столетия
        self.chronik_history.append=([])
        self.chronik_history[self.chronik_centuary_number]=u"{font=fonts/AnticvarShadow.ttf}{size=+10} Век %s Эпохи Достатка \n\n {/size}{/font}" % self.chronik_centuary_number

    def list_of_types(self,cost=0):
    # Список типов всех наших сокровищ
        self.list_of_treasures = []
        self.list_of_treasures.append([])
        self.list_of_types_of_treasures = []
        for tres_i in xrange(len(self.game.lair.treasury.jewelry)):
          item = True
          for type_i in xrange(len(self.list_of_types_of_treasures)): # Цикл по типам сокровищ
            if treasures.treasure_description_rus[self.game.lair.treasury.jewelry[tres_i].treasure_type]['pluralia'] == self.list_of_types_of_treasures[type_i]: # Такой тип сокровищ нам уже встретился
              item = False
              if self.game.lair.treasury.jewelry[tres_i].cost<cost:
                continue   # Это сокровище игнорируется
#              desc=self.game.lair.treasury.jewelry[tres_i].description()
              self.list_of_treasures[type_i].append(self.game.lair.treasury.jewelry[tres_i])  # Запоминаем сокровище
              break   # Конец цикла
          # Если безделушки такого типа ещё не было, вносим её в список
          if item:
            if self.game.lair.treasury.jewelry[tres_i].cost<cost:
              continue   # Это сокровище игнорируется
            desc=treasures.treasure_description_rus[self.game.lair.treasury.jewelry[tres_i].treasure_type]['pluralia']
            self.list_of_types_of_treasures.append(desc)
            self.list_of_treasures.append([])  # Запоминаем тип сокровища
            type_i=0
            type_i=len(self.list_of_types_of_treasures)
            self.list_of_treasures[type_i-1].append(self.game.lair.treasury.jewelry[tres_i])  # Запоминаем сокровище

    def set_active_treasure_type(self, type_i):
# Сохраняем индекс выбранного дракона. Это - для кнопки
        self.active_treasure_type = type_i   

    def set_active_treasure(self, treasury_i,cost,gift_mod):
# Сохраняем индекс выбранного дракона. Это - для кнопки
        self.active_treasure = treasury_i  
        self.active_cost = cost
        self.active_gift_mod = gift_mod
#        self.active_gift=None

    def death(self,reason,current_image):
        drg_lvl=self.game.dragon.level-1
        self.death_date[drg_lvl][self.game.girl.girl_id]=u"%s э.д." % self.game.year
        if current_image is not None:
          self.write_image(current_image,drg_lvl+1,self.game.girl.girl_id)
        if reason not in self.death_reason.keys():  # Если этой смерти ещё не было
          self.death_reason[reason]=[]  # Записываем причину
        self.death_reason[reason].append([drg_lvl,self.game.girl.girl_id])
        self.tot_dead += 1
#        self.game.girl.death = reason

    def set_active_death(self, death_i):
# Сохраняем выбранную смерть
        self.active_death = death_i

    def live(self,reason,current_image):
        drg_lvl=self.game.dragon.level-1
        self.death_date[drg_lvl][self.game.girl.girl_id]=u"?? э.д." 
        if current_image is not None:
          self.write_image(current_image,drg_lvl+1,self.game.girl.girl_id)
        if reason not in self.live_reason.keys():  # Если этой жизни ещё не было
          self.live_reason[reason]=[]  # Записываем причину
        self.live_reason[reason].append([drg_lvl,self.game.girl.girl_id])
        self.tot_live += 1
#        self.game.girl.live = reason

    def set_active_live(self, live_i):
# Сохраняем выбранную жизнь
        self.active_live = live_i