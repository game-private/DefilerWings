# coding=utf-8

import random
import data
import renpy.exports as renpy
import renpy.store as store
import girls_data
from treasures import gen_treas
from utils import call
from utils import weighted_random
from characters import Girl
from data import achieve_target
from points import Mobilization

class GirlsList(object):
    def __init__(self, game_ref, base_character):
        self.game = game_ref
        self.character = base_character
        self.prisoners = []  # список заключенных девушек
        self.free_list = []  # список свободных девушек
        self.sultan_list = []  # список девушек, проданных в Султанат
        self.whore_list = [] # список проституток
        self.whore = False
        self.spawn = []  # список отродий, приходящих после пробуждения
        self.active = 0  # номер текущей девушки
        self.offspring = []  # типы потомков для выполнения квеста

    def new_girl(self, girl_type='peasant',girl_nature=None,girl_hair=None,tres=True,girl_year=None,name_number=None,family=None,avatar=None):
        """
        Генерация новой девушки указанного типа.
        """
        self.game.chronik.girl_id +=1  # Увеличиваем индекс девушки
        self.game.chronik.tot_girl_id +=1  # Увеличиваем общий индекс девушки
        while True:
          self.game.girl = Girl(game_ref=self.game, girl_type=girl_type,girl_id=self.game.chronik.girl_id, name_number=name_number,family=family)
          if girl_hair is None:
            break
          elif self.game.girl.hair_color == girl_hair:
            break
        if avatar is not None:
          self.game.girl.avatar=avatar
        if girl_nature is not None:
          self.game.girl.nature=girl_nature
        if tres:
          self.game.girl.treasure = self.gen_tres()
        self.game.girl.birth_year=self.game.chronik.remember_girl(self.game.dragon.level, self.game.girl,girl_year)
        
        self.game.girl.willing=False  # Согласится ли она на секс добровольно
        self.game.girl.willing_attemp=True  # Можно ли попытаться соблазнить
#        self.game.narrator('%s' %name_number)
        self.game.girl.old=False  # Слишком стара, чтобы рожать
#        self.game.narrator('%s' %name_number)

        return self.description('new') + ", " + '%s' %girls_data.nature_info[self.game.girl.nature] 

    def gen_tres(self):
        """
        Создание списка индивидуальных сокровищ для текущей девушки
        """
        g_type = self.game.girl.type  # упрощение обращения к типу девушки
        girl_info = girls_data.girls_info[g_type]  # упрощение обращения к информации для данного типа девушки
        count = random.randint(girl_info['t_count_min'], girl_info['t_count_max'])
        t_list = girl_info['t_list']
        if self.game.girl.nature == 'innocent':
          for i in reversed(xrange(len(t_list))):
            if t_list[i]=='phallos':
              del t_list[i]              
        alignment = girl_info['t_alignment']
        min_cost = girl_info['t_price_min']
        max_cost = girl_info['t_price_max']
        obtained = u"Принадлежало красавице по имени %s" % self.game.girl.name
        return gen_treas(count, t_list, alignment, min_cost, max_cost, obtained,girl_id=self.game.girl.girl_id)

    def impregnate(self):
        """
        Осеменение женщины.
        """
        # self.description('prelude', True)
        # self.description('sex', True)
        # self.description('impregnate', True)
        self.game.girl.virgin = False
        if self.game.girl.quality < self.game.dragon.magic or \
                'impregnator' in self.game.dragon.modifiers():
            self.game.girl.pregnant = 2
        else:
            self.game.girl.pregnant = 1
        self.game.dragon.lust -= 1
        achieve_target(self.game.girl.type, "impregnate")
        return self.description('shout')

    def rape_impregnate(self):
        """
        Осеменение женщины в ходе изнасилования.
        """
        self.game.girl.virgin = False
        self.game.girl.pregnant = 2
        achieve_target(self.game.girl.type, "impregnate")
        if self.game.girl.cripple:
          return self.description('shout_cripple')
        else:
          return self.description('shout')

    def free_girl(self):
        """
        Выпустить текущую девушку на свободу.
        """

        if self.game.girl.jailed:
          if self.game.girl.blind:
            return self.description('free_prison_blind')
          elif self.game.girl.cripple:
            return self.description('free_prison_cripple')
          else:
            return self.description('free_prison')
            
        else:
          if self.game.girl.blind:
            return self.description('free_blind')
          elif self.game.girl.cripple:
            return self.description('free_cripple')
          else:
            return self.description('free')
        # девушка отслеживается только если беременна
#        if self.game.girl.pregnant:
#            self.free_list.append(self.game.girl)

    def free_all_girls(self):
        """
        Выпустить на свободу всех девушек.
        """
        for girl_i in reversed(xrange(self.prisoners_count)):
            self.game.girl = self.prisoners[girl_i]
            text = u'Покинув логово, %s выпустил на свободу всех пленниц. \n\n ' %(self.game.dragon.name )
            self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
            if self.game.girl.love is not None:
              self.love_escape_ind()
              continue
            self.try_to_go() 
        self.prisoners = []

    def knight_free_all_girls(self):
# Рыцарь выпускает девушек на свободу
        for girl_i in reversed(xrange(self.prisoners_count)):
            self.game.girl = self.prisoners[girl_i]
            if self.game.girl.love is None:
              text = self.description('knight_free')
              self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
              self.game.girl.third(text)
              self.free_list.append(self.game.girl)
            elif self.game.girl.love.type == 'smuggler':  # Рыцарь убивает контрабандиста
              call("lb_knight_kills_smuggler")
            elif self.game.girl.love.type == 'lizardman':  # Рыцарь убивает контрабандиста
              call("lb_knight_kills_lizardman")
        self.prisoners = []

    def lizardman_free_all_girls(self): # После победы ящерика и его возлюбленной пленницы оказываются на свободе.
        for girl_i in reversed(xrange(self.prisoners_count)):
            self.game.girl = self.prisoners[girl_i]
            if self.game.girl.love is None:
              text = self.description('lizardman_free')
              self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
              self.game.girl.third(text)
              self.free_list.append(self.game.girl)
            elif self.game.girl.love.type == 'lizardman':  # Если ящерика любит кто-то ещё - она тоже выходит на свободу.
              text = u"После того, как ещё одна влюблённая пара прогнала дракона из логова, все пленницы покинули свою темницу. \n\n"
              self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
              self.love_escape_ind()
        self.prisoners = []

    def chromi_free_all_girls(self): # Хроми освобождает пленниц.
        for girl_i in reversed(xrange(self.prisoners_count)):
            self.game.girl = self.prisoners[girl_i]
            if self.game.girl.love is None:
              text = self.description('chromi_free')
              self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
              self.game.girl.third(text)
              self.free_list.append(self.game.girl)
            else:
              text = u"После того, как Хроми спасла всех пленниц, ничего больше не стояло между девушкой и её любовью. \n\n"
              self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
              self.love_escape_ind()
        self.prisoners = []

    def pythoness_free_all_girls(self): # Хроми освобождает пленниц.
        for girl_i in reversed(xrange(self.prisoners_count)):
            self.game.girl = self.prisoners[girl_i]
            if self.game.girl.love is None:
              text = self.description('pythoness_free')
              self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
              self.game.girl.third(text)
              self.free_list.append(self.game.girl)
            else:
              text = u"После того, как ясновидящая спутница спасла всех пленниц, ничего больше не стояло между девушкой и её любовью. \n\n"
              self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
              self.love_escape_ind()
        self.prisoners = []

    def steal_girl(self):
        return self.description('steal')
# Mahariel_print
    def girl_in_prison(self):
#       Девушка томится в тюрьме
        g_type = self.game.girl.type     # упрощение обращения к типу девушки
        g_virg = self.game.girl.virgin   # упрощение обращения к девственности девушки
        g_preg = self.game.girl.pregnant # упрощение обращения к беременности девушки
        g_natu = self.game.girl.nature   # прощение обращения к характеру девушки
        if self.game.girl.cripple:
          return self.description('in_prison_cripple') 
        elif self.game.girl.blind:
          if g_preg>0:
            return self.description('in_prison_blind_p') 
          else:
            return self.description('in_prison_blind_a')
        else:
          if self.game.girl.willing and (g_type=='peasant' or g_type=='citizen' or g_type=='princess'):
            will='_willing'
          else:
            will=''
          if g_virg:
            desc= 'in_prison_' + g_type + '_v_' + g_natu + will         
          elif g_preg>0:
            desc= 'in_prison_' + g_type + '_p_' + g_natu + will
          else:
            desc= 'in_prison_' + g_type + '_a_' + g_natu + will
          return self.description(desc)         

    def save_girl(self):
# Девушка выбралась из логова. Начинаем отслеживать, даже если она не беременна
        self.free_list.append(self.game.girl)

    def save_whore(self):
# Проститутка, оставшаяся в борделе
        self.whore_list.append(self.game.girl)
    
    def try_to_go(self):  # Слепым везёт
        if self.game.girl.blind and self.game.girl.pregnant>0:
          self.try_to_go_blind_fail()
        elif self.game.girl.blind and self.game.girl.pregnant==0:
          self.try_to_go_blind_success()
        elif self.game.girl.cripple:
          self.try_to_go_cripple()
        else:
          self.try_to_go_normal()

    def try_to_go_blind_fail(self):
# Возможная смерть девушки при её уходе из логова
        g_type = self.game.girl.type     # упрощение обращения к типу девушки
        text = u"%s оказалась на свободе. Теперь она должна найти путь домой... но слепой эта задача не под силу. " %(self.game.girl.name)
        self.game.narrator(u"%s" % text)
        self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
# Пытается уйти из-под воды
        if self.game.lair.type_name == 'underwater_grot' or self.game.lair.type_name == 'underwater_mansion':
          if g_type == 'mermaid' or g_type == 'siren':
            if (random.randint(1, 3) == 1): # Русалкам повезло
              call("lb_ttg_sea_blind1_mermaid_save")
            else:
              call("lb_ttg_sea_blind1_mermaid_dead")
          else:
            ("lb_ttg_sea_blind1_dead")
# Пытается слезть с горы
        elif self.game.lair.type_name == 'impregnable_peak':
          if self.is_giant and g_type is not 'siren':
            if (random.randint(1, 3) == 1): # Великаншам повезло 
              call("lb_ttg_mount_blind1_giant_save")
            else: 
              call("lb_ttg_mount_blind1_giant_dead")
          elif g_type == 'mermaid' or g_type == 'siren':
            call("lb_ttg_mount_blind1_mermaid_dead")
          else:
            call("lb_ttg_mount_blind1_dead")

# Пытается слезть с ледяной горы. Гораздо сложнее.
        elif self.game.lair.type_name == 'solitude_citadel' or self.game.lair.type_name == 'ice_citadel': 
          if g_type == 'ice':
            if (random.randint(1, 3) == 1): # Йотуншам повезло 
              call("lb_ttg_ice_blind1_ice_save")
            else: 
              call("lb_ttg_ice_blind1_ice_dead")
          else:
            call("lb_ttg_ice_blind1_dead")

# Пытается слезть с вулкана. Всё так же сложно.
        elif self.game.lair.type_name == 'vulcano_chasm' or self.game.lair.type_name == 'vulcanic_forge': 
          if g_type == 'fire':
            if (random.randint(1, 3) == 1): # Ифриткам повезло 
              call("lb_ttg_fire_blind1_fire_save")
            else: 
              call("lb_ttg_fire_blind1_fire_dead")
          else:
            call("lb_ttg_fire_blind1_dead")

# Пытается выйти из Подземных Чертогов. Для слепой - невозможно.
        elif self.game.lair.type_name == 'underground_palaces': 
          call("lb_ttg_gnome_blind1_dead")

# Пытается выйти из Дупла Великого Древа. Для слепой - невозможно.
        elif self.game.lair.type_name == 'forest_heart': 
          call("lb_ttg_elf_blind1_dead")

# Пытается выйти Облачного замка. Как это вообще возможно?.
        elif self.game.lair.type_name == 'cloud_castle':
          if g_type == 'titan':
             call("lb_ttg_cloud_blind1_titan_save")
          else:
             call("lb_ttg_cloud_blind1_dead")

# Все остальные типы логов.
        else:
          if self.is_giant and g_type is not 'siren':
            call("lb_ttg_usual_blind1_giant_save")
          elif g_type == 'mermaid' or g_type == 'siren':
            call("lb_ttg_usual_blind1_mermaid_dead")
          else:
            if (random.randint(1, 5) == 1):
              call("lb_ttg_usual_blind1_save")
            else:
              call("lb_ttg_usual_blind1_dead")

    def try_to_go_blind_success(self):
# Открывшие внутренне зрение спасаются всегда!
        g_type = self.game.girl.type     # упрощение обращения к типу девушки
# Пытается уйти из-под воды
        if self.game.lair.type_name == 'underwater_grot' or self.game.lair.type_name == 'underwater_mansion':
          if g_type == 'mermaid' or g_type == 'siren':
            text = u"Оказавшись в родной стихии, морская дева безошибочна поплыла домой. Слепота %s нимало не беспокоила.\n\n" % (self.game.girl.name_v)
            call("lb_ttg_save",'sea',text)
          else:
            text = u"Оказавшись посреди безбрежного морского простора, %s безошибочно выбрала верное направление и без особых проблем доплыла до берега. Слепота её нимало не беспокоила.\n\n" % (self.game.girl.name)
            call("lb_ttg_save",'sea',text)
# Пытается слезть с горы
        elif self.game.lair.type_name == 'impregnable_peak':
          if g_type == 'mermaid' or g_type == 'siren':
            text = u"Оказавшись посреди высокорного плато, морская дева доползла до стремительной горной реки и благополучно сплыла вниз, к бескрайним морским просторам. Слепота %s нимало не беспокоила.\n\n" % (self.game.girl.name_v)
            call("lb_ttg_save",'mountain',text)
          else:
            text = u"Оказавшись посреди высокорного плато, %s безошибочно выбрала верную тропу, спокойно прошла по опасному прижиму и без особых проблем спустилась к обжитым местам. Слепота её нимало не беспокоила.\n\n" % (self.game.girl.name)
            call("lb_ttg_save",'mountain',text)
# Пытается слезть с ледяной горы.
        elif self.game.lair.type_name == 'solitude_citadel' or self.game.lair.type_name == 'ice_citadel': 
          if g_type == 'ice':
            text = u"Слепая йотунша без каких-либо проблем дошла до родных мест. \n\n" % (self.game.girl.name)
            call("lb_ttg_save",'mountain',text)
          elif g_type == 'mermaid' or g_type == 'siren':
            text = u"Оказавшись посреди горного ледника, морская дева благополучно съехала вниз, доползла до истока стремительной горной реки и благополучно сплыла вниз, к бескрайним морским просторам. Слепота %s нимало не беспокоила.\n\n" % (self.game.girl.name_v)
            call("lb_ttg_save",'mountain',text)
          else:
            text = u"Оказавшись посреди горного ледника, %s благополучно съехала вниз, безошибочно выбрала верную тропу, спокойно прошла по опасному прижиму и без особых проблем спустилась к обжитым местам. Слепота её нимало не беспокоила.\n\n" % (self.game.girl.name)
            call("lb_ttg_save",'mountain',text)

# Пытается слезть с вулкана. 
        elif self.game.lair.type_name == 'vulcano_chasm' or self.game.lair.type_name == 'vulcanic_forge': 
          if g_type == 'fire':
            text = u"Слепая ифритка без каких-либо проблем дошла до родных мест. \n\n" % (self.game.girl.name)
            call("lb_ttg_save",'mountain',text)
          elif g_type == 'mermaid' or g_type == 'siren':
            text = u"Оказавшись посреди вулканического плато, морская дева доползла до истока горной реки, берущей начало в относительно прохладном гейзере, и благополучно сплыла вниз, к бескрайним морским просторам. Слепота %s нимало не беспокоила.\n\n" % (self.game.girl.name_v)
            call("lb_ttg_save",'mountain',text)
          else:
            text = u"Оказавшись посреди вулканического плато, %s спокойно обошла озеро лавы, безошибочно выбрала верную тропу, спокойно прошла по опасному прижиму и без особых проблем спустилась к обжитым местам. Слепота её нимало не беспокоила.\n\n" % (self.game.girl.name)
            call("lb_ttg_save",'mountain',text)

# Пытается выйти из Подземных Чертогов. 
        elif self.game.lair.type_name == 'underground_palaces': 
          if g_type == 'mermaid' or g_type == 'siren':
            text = u"Оказавшись в необозримом лабиринте пещер, морская дева доползла до подземной реки и благополучно сплыла вниз, к бескрайним морским просторам. Слепота %s нимало не беспокоила.\n\n" % (self.game.girl.name_v)
            call("lb_ttg_save",'undeground',text)
          else:
            text = u"Оказавшись в необозримом лабиринте пещер, %s быстро и безошибочно нашла путь наружу. Слепота её нимало не беспокоила.\n\n" % (self.game.girl.name)
            call("lb_ttg_save",'undeground',text)

# Пытается выйти из Дупла Великого Древа.
        elif self.game.lair.type_name == 'forest_heart': 
          if g_type == 'mermaid' or g_type == 'siren':
            text = u"Оказавшись в зловещем осквернённом лесу, морская дева доползла до речки и благополучно сплыла вниз, к бескрайним морским просторам. Слепота %s нимало не беспокоила.\n\n" % (self.game.girl.name_v)
            call("lb_ttg_save",'forest',text)
          else:
            text = u"Оказавшись в зловещем осквернённом лесу, %s обошла поляну с живой травой, убежала от плотоядного дуба, обогнула заросли ядовитого кустарника и без всяких проблем дошла до опушки.  Слепота её нимало не беспокоила.\n\n" % (self.game.girl.name)
            call("lb_ttg_save",'forest',text)

# Пытается выйти Облачного замка. Как это вообще возможно?.
        elif self.game.lair.type_name == 'cloud_castle':
          if g_type == 'titan':
            text = u"Оказавшись в родной стихии, титанида спокойно долетела до родных мест. Слепота %s нимало не беспокоила.\n\n" % (self.game.girl.name_v)
            call("lb_ttg_save",'sky',text)
          elif not is_giant:
            text = u"Спрыгнув с облачного замка, %s приземлилась прямо на спину парящего грифона, улыбнулась ошарашенному всаднику и сказала 'Привет!'\n\n" % (self.game.girl.name)
            call("lb_ttg_save",'sky',text)
          else:
            text = u"Спрыгнув с облачного замка, великанша приземлилась прямо на парящий внизу дирижабль, улыбнулась ошарашенным цвергам и сказала 'Привет!'\n\n"
            call("lb_ttg_save",'sky',text)

# Все остальные типы логов.
        else:
          if g_type == 'mermaid' or g_type == 'siren':
            text = u"Оказавшись в лесу, морская дева доползла до речки и благополучно сплыла вниз, к бескрайним морским просторам. Слепота %s нимало не беспокоила.\n\n" % (self.game.girl.name_v)
            call("lb_ttg_save",'forest',text)
          else:
            text = u"Оказавшись в лесу, %s быстро и без проблем добралась до обжитых мест. Слепота её нимало не беспокоила.\n\n" % (self.game.girl.name)
            call("lb_ttg_save",'forest',text)

    def try_to_go_cripple(self):
# Понятное дело, калеки никогда не спасаются.
        g_type = self.game.girl.type     # упрощение обращения к типу девушки
# Пытается уйти из-под воды
        if self.game.lair.type_name == 'underwater_grot' or self.game.lair.type_name == 'underwater_mansion':
          call("lb_ttg_underwater_cripple")
# Пытается слезть с горы
        elif self.game.lair.type_name == 'impregnable_peak':
          call("lb_ttg_peak_cripple")
# Пытается слезть с ледяной горы.
        elif self.game.lair.type_name == 'solitude_citadel' or self.game.lair.type_name == 'ice_citadel': 
          call("lb_ttg_ice_cripple")
# Пытается слезть с вулкана. 
        elif self.game.lair.type_name == 'vulcano_chasm' or self.game.lair.type_name == 'vulcanic_forge': 
          call("lb_ttg_fire_cripple")
# Пытается выйти из Подземных Чертогов. 
        elif self.game.lair.type_name == 'underground_palaces': 
          call("lb_ttg_underground_cripple")

# Пытается выйти из Дупла Великого Древа.
        elif self.game.lair.type_name == 'forest_heart': 
          call("lb_ttg_elf_cripple")

# Пытается выйти Облачного замка. Как это вообще возможно?.
        elif self.game.lair.type_name == 'cloud_castle':
          call("lb_ttg_cloud_cripple")

# Все остальные типы логов.
        else:
          if self.is_giant:
            call("lb_ttg_cripple")
          else:
            if (random.randint(1, 10) == 1):
              call("lb_ttg_cripple_save")
            else:
              call("lb_ttg_cripple")


    def try_to_go_normal(self):
# Возможная смерть девушки при её уходе из логова
        g_type = self.game.girl.type     # упрощение обращения к типу девушки
        l_access=self.game.lair.inaccessability       # Упрощение обращения к доступности логова

# Пытается уйти из-под воды
        if self.game.lair.type_name == 'underwater_grot' or self.game.lair.type_name == 'underwater_mansion':
          if g_type == 'citizen' or g_type == 'peasant' or g_type == 'princess' or g_type == 'elf':
             self.event('try_to_go_underwater_usual',g_type,l_access)  
          elif g_type == 'mermaid' or g_type == 'siren' or g_type == 'fire':
             desc = 'try_to_go_underwater_' + g_type
             self.event(desc,g_type,l_access)
          else:
             self.event('try_to_go_underwater_giant',g_type,l_access) 

# Пытается слезть с горы
        elif self.game.lair.type_name == 'impregnable_peak':          
          if g_type == 'citizen' or g_type == 'peasant' or g_type == 'princess' or g_type == 'elf':
             self.event('try_to_go_peak_usual',g_type,l_access) 
          elif g_type == 'mermaid' or g_type == 'siren':
             self.event('try_to_go_peak_mermaid',g_type,l_access)
          else:
             self.event('try_to_go_peak_giant',g_type,l_access) 

# Пытается слезть с ледяной горы. Гораздо сложнее.
        elif self.game.lair.type_name == 'solitude_citadel' or self.game.lair.type_name == 'ice_citadel': 
          if g_type == 'citizen' or g_type == 'peasant' or g_type == 'princess' or g_type == 'elf':
             self.event('try_to_go_ice_usual',g_type,l_access) 
          elif g_type == 'mermaid' or g_type == 'siren':
             self.event('try_to_go_ice_mermaid',g_type,l_access)
          elif g_type == 'fire':
             self.event('try_to_go_ice_fire',g_type,l_access)
          elif g_type == 'ice':
             self.event('try_to_go_ice_ice',g_type,l_access)
          else:
             self.event('try_to_go_ice_giant',g_type,l_access) 

# Пытается слезть с вулкана. Всё так же сложно.
        elif self.game.lair.type_name == 'vulcano_chasm' or self.game.lair.type_name == 'vulcanic_forge': 
          if g_type == 'citizen' or g_type == 'peasant' or g_type == 'princess' or g_type == 'elf':
             self.event('try_to_go_fire_usual',g_type,l_access) 
          elif g_type == 'mermaid' or g_type == 'siren':
             self.event('try_to_go_fire_mermaid',g_type,l_access)
          elif g_type == 'ice':
             self.event('try_to_go_fire_ice',g_type,l_access)
          elif g_type == 'fire':
             self.event('try_to_go_fire_fire',g_type,l_access)
          else:
             self.event('try_to_go_fire_giant',g_type,l_access) 

# Пытается выйти из Подземных Чертогов. Адски сложно.
        elif self.game.lair.type_name == 'underground_palaces': 
          if g_type == 'citizen' or g_type == 'peasant' or g_type == 'princess' or g_type == 'elf':
             self.event('try_to_go_underground_usual',g_type,l_access) 
          elif g_type == 'mermaid' or g_type == 'siren':
             self.event('try_to_go_underground_mermaid',g_type,l_access)
          elif g_type == 'fire':
             self.event('try_to_go_underground_fire',g_type,l_access)
          else:
             self.event('try_to_go_underground_giant',g_type,l_access) 

# Пытается выйти из Дупла Великого Древа. Всё так же адски сложно.
        elif self.game.lair.type_name == 'forest_heart': 
          if g_type == 'citizen' or g_type == 'peasant' or g_type == 'princess' or g_type == 'elf':
             self.event('try_to_go_elf_usual',g_type,l_access) 
          elif g_type == 'mermaid' or g_type == 'siren':
             self.event('try_to_go_elf_mermaid',g_type,l_access)
          else:
             self.event('try_to_go_elf_giant',g_type,l_access) 

# Пытается выйти Облачного замка. Как это вообще возможно?.
        elif self.game.lair.type_name == 'cloud_castle':
          if g_type == 'titan':
             self.event('try_to_go_cloud_titan',g_type,l_access)
          elif g_type == 'citizen' or g_type == 'peasant' or g_type == 'princess' or g_type == 'elf' or g_type == 'mermaid':
            if self.game.mobilization.level > 10:
               self.event('try_to_go_cloud_griffin',g_type,l_access) 
            else:
               self.event('try_to_go_cloud_usual',g_type,l_access)   
          else:
             self.event('try_to_go_cloud_usual',g_type,l_access)

# Все остальные типы логов.
        else:
          if g_type == 'citizen' or g_type == 'peasant' or g_type == 'princess' or g_type == 'elf':
             self.event('try_to_go_forest_usual',g_type,l_access) 
          elif g_type == 'mermaid' or g_type == 'siren':
             self.event('try_to_go_elf_mermaid',g_type,l_access)
          else:
             self.event('try_to_go_forest_giant',g_type,l_access) 

    def suicide_decision(self,girl_i):
                if self.game.girl.virgin == True:
                    text = self.description('think_innocent_virgin')
                    self.game.girl.third(text)
                elif self.game.girl.pregnant > 0:
                    text = self.description('think_innocent_pregnant')
                    self.game.girl.third(text)
                else:
                    text = self.description('think_innocent_after')
                    self.game.girl.third(text)
                if (random.randint(1, 3) == 1):  # Всё же решились на самоубийство
                  if self.game.girl.virgin == True:
                    text = u'Опасаясь бесчестья, %s решила поконочить с собой. \n\n' %(self.game.girl.name )
                    self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
                  else:
                    text = u'Будучи обесчещенной, %s решила поконочить с собой. \n\n' %(self.game.girl.name )
                    self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
                  text =  self.description('think_innocent_yes')
                  self.game.girl(text)
                  self.suicide_attemp()
                  if self.game.girl.attemp == True or (random.randint(1, 10) == 1):   # Успех
                      if self.game.girl.willing:
                        self.game.dragon.drain_energy()
                        self.game.chronik.live('willing_girl', None)
                        call("lb_willing_help_prison")
                      else:
                        self.game.girl.dead=True
                        del self.prisoners[girl_i]
                        self.suicide_sucsess()  
                  else:  # Неудача. Ничего, в другой раз повезёт.
                      self.suicide_fail() 
                      self.game.girl.attemp = True
                else: # Не решилась на самоубийство
                    text = self.description('think_innocent_no')
                    self.game.girl(text)  

    def escape_decision(self,girl_i):
                if self.game.girl.virgin == True:
                    text = self.description('think_proud_virgin')
                    self.game.girl.third(text) 
                elif self.game.girl.pregnant > 0:
                    text = self.description('think_proud_pregnant') 
                    self.game.girl.third(text)
                else:
                    text = self.description('think_proud_after') 
                    self.game.girl.third(text)

                # @fdsc Было 1, 3 вместо 1 + ina
                ina  = self.game.lair.inaccessability
                ina += self.game.lair.reachableSumm([]) * 8
                ina -= self.game.girl.quality * 12
                if ina < 1:
                    ina = 1
                # self.game.girl(u'Побег %s%%' % (100 / ina))

                if (random.randint(1, ina) == 1):   # Всё же решились на бегство
                  if self.game.girl.virgin == True:
                    text = u'Опасаясь бесчестья, %s решила бежать. ' %(self.game.girl.name )
                    self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
                  else:
                    text = u'Будучи обесчещенной, %s решила бежать. ' %(self.game.girl.name )
                    self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
                  text = self.description('think_proud_yes')
                  self.game.girl(text)
                  # @fdsc
                  # if self.game.girl.attemp == True or (random.randint(1, 10) == 1):  # Вторая попытка всегда успешная
                  ina  = self.game.lair.inaccessability + self.game.lair.summProtection()
                  ina -= self.game.girl.quality * 7
                  if ina < 1:
                    ina = 1
                  # self.game.girl(u'Побег %s%%' % (100 / ina))

                  if random.randint(1, ina) == 1:

                      text = u'Побег удался. \n\n' 
                      self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
                      self.game.girl.dead=True
                      del self.prisoners[girl_i]
                      self.event('escape')  # событие "побег из заключения"
                      self.try_to_go()
                  else:  # Неудача. Ничего, в другой раз повезёт.
                      text = u'Побег не удался. \n\n' 
                      self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
                      text = self.description('think_proud_fail')
                      self.game.girl(text)
                      self.game.girl.attemp = True
                else: # Не решилась на побег
                    text = self.description('think_proud_no') 
                    self.game.girl(text)

    def seduction_decision(self,girl_i):
                # @fdsc  Девушек никогда не съедают
                return
                if self.game.girl.virgin == True:
                    text = self.description('think_lust_virgin') 
                    self.game.girl.third(text)
                elif self.game.girl.pregnant > 0:
                    text = self.description('think_lust_pregnant')  
                    self.game.girl.third(text)
                else:
                    text = self.description('think_lust_after')  
                    self.game.girl.third(text)
                # @fdsc  Девушек никогда не съедают
                if (random.randint(1, 3) == 1):   # Всё же решились на соблазнение
                  if self.game.girl.virgin == True:
                    text = u'Желая испробывать радости секса, %s решила соблазнить драконьих слуг, и у неё это ' %(self.game.girl.name )
                    self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
                  else:
                    text = u'Скучая по сексу, %s решила соблазнить драконьих слуг, и у неё это ' %(self.game.girl.name )
                    self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
                  text = self.description('think_lust_yes') 
                  self.game.girl(text) 
                  if self.game.girl.attemp == True or (random.randint(1, 10) == 1):  # Вторая попытка всегда успешная
                      text = u'получилось. ' 
                      self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
                      self.game.girl.dead=True
                      del self.prisoners[girl_i]
                      self.event('girl_kitchen')
                  else:  # Неудача. Ничего, в другой раз повезёт.
                      text = u'не получилось. \n\n' 
                      self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
                      text = self.description('think_lust_fail')
                      self.game.girl(text)
                      self.game.girl.attemp = True
                else: # Не решилась на соблазнение
                    text = self.description('think_lust_no') 
                    self.game.girl(text)

    def suicide_attemp(self):
# После изнасилования некоторые девушки пытаются покончить жизнь самоубийством, не попавшись при этом слугам.
        if self.game.lair.type_name == 'underwater_grot' or self.game.lair.type_name == 'underwater_mansion':
          if self.game.girl.type == 'mermaid' or self.game.girl.type == 'siren':
            text = self.description('suicide_attemp_usual') 
          else:
            text = self.description('suicide_attemp_sea') 
        elif self.game.lair.type_name == 'impregnable_peak' or self.game.lair.type_name == 'solitude_citadel' or self.game.lair.type_name == 'ice_citadel': 
          if self.game.girl.type == 'ice':
            text = self.description('suicide_attemp_usual') 
          else:
            text = self.description('suicide_attemp_ice')  
        elif self.game.lair.type_name == 'vulcano_chasm' or self.game.lair.type_name == 'vulcanic_forge': 
          if self.game.girl.type == 'fire':
            text = self.description('suicide_attemp_usual') 
          else:
            text = self.description('suicide_attemp_fire') 
        elif self.game.lair.type_name == 'underground_palaces': 
          text = self.description('suicide_attemp_undeground') 
        elif self.game.lair.type_name == 'forest_heart': 
          text = self.description('suicide_attemp_elf') 
        elif self.game.lair.type_name == 'cloud_castle':
          if self.game.girl.type == 'titan':
            text = self.description('suicide_attemp_usual') 
          else:
            text = self.description('suicide_attemp_cloud')
        else:
          text = self.description('suicide_attemp_usual') 
        self.game.girl.third(text)


    def suicide_sucsess(self):
# Успешная попытка суицида
        text_chronik=None
        if self.game.lair.type_name=='impassable_coomb':
          current_image="img/bg/lair/ravine.jpg"
        elif self.game.lair.type_name=='impregnable_peak':
          current_image="img/bg/lair/cavelarge.jpg"   
        elif self.game.lair.type_name=='solitude_citadel':
          current_image="img/bg/lair/icecave.jpg"
        elif self.game.lair.type_name=='vulcano_chasm':
          current_image="img/bg/lair/volcanocave.jpg"
        elif self.game.lair.type_name=='underwater_grot':
          current_image="img/bg/lair/grotto.jpg"
        elif self.game.lair.type_name=='underground_burrow':
          current_image="img/bg/lair/burrow.jpg" 
        elif self.game.lair.type_name=='ogre_den':
          current_image="img/bg/lair/cave.jpg"
        elif self.game.lair.type_name=='broad_cave':
          current_image="img/bg/lair/cavelarge.jpg" 
        elif self.game.lair.type_name=='forest_heart':
          current_image="img/bg/lair/elfruin.jpg"
        elif self.game.lair.type_name=='tower_ruin':
          current_image="img/bg/lair/tower_lair.jpg"      
        elif self.game.lair.type_name=='dragon_castle':
          current_image="img/bg/lair/dragon_castle.jpg"
        elif self.game.lair.type_name=='castle':
          current_image="img/bg/lair/fortress_lair.jpg"     
        elif self.game.lair.type_name=='monastery_ruin':
          current_image="img/bg/lair/crypt_lair.jpg"
        elif self.game.lair.type_name=='fortress_ruin':
          current_image="img/bg/lair/castle_lair.jpg" 
        elif self.game.lair.type_name=='castle_ruin':
          current_image="img/bg/lair/palace_lair.jpg"
        elif self.game.lair.type_name=='ice_citadel':
          current_image="img/bg/lair/icecastle.jpg" 
        elif self.game.lair.type_name=='vulcanic_forge':
          current_image="img/bg/lair/volcanoforge.jpg"
        elif self.game.lair.type_name=='cloud_castle':
          current_image="img/bg/lair/cloud_castle.jpg"  
        elif self.game.lair.type_name=='underwater_mansion':
          current_image="img/bg/lair/underwater.jpg"
        elif self.game.lair.type_name=='underground_palaces':
          current_image="img/bg/lair/dwarfruin.jpg"   
        if self.game.lair.type_name == 'underwater_grot' or self.game.lair.type_name == 'underwater_mansion':
          if self.game.girl.type == 'mermaid' or self.game.girl.type == 'siren':
            self.suicide_sucsess_usual()
          else:
            text_chronik = u'%s утопилась в мелком бассейне. \n\n' %(self.game.girl.name )
            text = self.description('suicide_sucsess_sea')
            self.game.chronik.death('suicide_sucsess_sea',current_image)   
        elif self.game.lair.type_name == 'impregnable_peak' or self.game.lair.type_name == 'solitude_citadel' or self.game.lair.type_name == 'ice_citadel': 
          if self.game.girl.type == 'ice':
            self.suicide_sucsess_usual()
          else:
            text_chronik = u'%s нашла морозную комнату и скончалась от холода. \n\n' %(self.game.girl.name )
            text = self.description('suicide_sucsess_ice') 
            self.game.chronik.death('suicide_sucsess_ice',current_image) 
        elif self.game.lair.type_name == 'vulcano_chasm' or self.game.lair.type_name == 'vulcanic_forge': 
          if self.game.girl.type == 'fire':
            self.suicide_sucsess_usual()
          else:
            text_chronik = u'%s нашла горячую комнату и изжарилась живьём. \n\n' %(self.game.girl.name )
            text = self.description('suicide_sucsess_fire') 
            self.game.chronik.death('suicide_sucsess_fire',current_image) 
        elif self.game.lair.type_name == 'underground_palaces': 
          text_chronik = u'%s нашла герметичную комнату, закрыла её и погибла от медленного удушья. \n\n' %(self.game.girl.name )
          text = self.description('suicide_sucsess_undeground')
          self.game.chronik.death('suicide_sucsess_undeground',current_image) 
        elif self.game.lair.type_name == 'forest_heart': 
          text_chronik = u'%s нашла полянку с живой травой, которая проросла сквозь её тело. \n\n' %(self.game.girl.name )
          text = self.description('suicide_sucsess_elf')
          self.game.chronik.death('suicide_sucsess_elf',current_image) 
        elif self.game.lair.type_name == 'cloud_castle':
          if self.game.girl.type == 'ice':
            self.suicide_sucsess_usual()
          else:
            text_chronik = u'%s прыгнула с колоссальной высоты и разбилась. \n\n' %(self.game.girl.name )
            text = self.description('suicide_sucsess_cloud')
            self.game.chronik.death('suicide_sucsess_cloud',current_image)  
        else:
          self.suicide_sucsess_usual()
        if text_chronik is not None:
          self.game.chronik.write_chronik(text_chronik,self.game.dragon.level,self.game.girl.girl_id)
          self.game.girl.third(text)
 

    def suicide_sucsess_usual(self):
        # @fdsc  Девушек никогда не съедают
        return
        text_chronik = u'%s подружилась с драконьеми слугами и уговорила её съесть. ' %(self.game.girl.name )
        self.game.chronik.write_chronik(text_chronik,self.game.dragon.level,self.game.girl.girl_id)
        text = self.description('suicide_sucsess_usual')
        self.game.girl.third(text)
        self.event('girl_kitchen') 

    def suicide_fail(self):
# Слуги предотвращают самоубийство
        text_chronik=None
#        self.game.narrator(u"test")
        if self.game.lair.type_name == 'underwater_grot' or self.game.lair.type_name == 'underwater_mansion':
          if self.game.girl.type == 'mermaid' or self.game.girl.type == 'siren':
            self.suicide_fail_usual()
          else:
            text_chronik = u'%s попыталась утопиться в мелком бассейне, но её вовремя нашли и откачали. \n\n' %(self.game.girl.name )
            text = self.description('suicide_fail_sea') 
            self.game.chronik.write_chronik(text_chronik,self.game.dragon.level,self.game.girl.girl_id)
            self.game.girl.third(text)              
        elif self.game.lair.type_name == 'impregnable_peak' or self.game.lair.type_name == 'solitude_citadel' or self.game.lair.type_name == 'ice_citadel': 
          if self.game.girl.type == 'ice':
            self.suicide_fail_usual()
          else:
            text_chronik = u'%s попыталась замёрзнуть насмерть, но её вовремя нашли и откачали. \n\n' %(self.game.girl.name )
            text = self.description('suicide_fail_ice') 
            self.game.chronik.write_chronik(text_chronik,self.game.dragon.level,self.game.girl.girl_id)
            self.game.girl.third(text) 
        elif self.game.lair.type_name == 'vulcano_chasm' or self.game.lair.type_name == 'vulcanic_forge': 
          if self.game.girl.type == 'fire':
            self.suicide_fail_usual()
          else:
            text_chronik = u'%s попыталась запечься живьём, но её вовремя нашли и откачали. \n\n' %(self.game.girl.name )
            text = self.description('suicide_fail_fire') 
            self.game.chronik.write_chronik(text_chronik,self.game.dragon.level,self.game.girl.girl_id)
            self.game.girl.third(text) 
        elif self.game.lair.type_name == 'underground_palaces': 
          text_chronik = u'%s попыталась задохнуться в герметичной комнате, но её вовремя нашли и откачали. \n\n' %(self.game.girl.name )
          text = self.description('suicide_fail_undeground') 
          self.game.chronik.write_chronik(text_chronik,self.game.dragon.level,self.game.girl.girl_id)
          self.game.girl.third(text) 
        elif self.game.lair.type_name == 'forest_heart': 
          text_chronik = u'%s легла на живую траву, чтобы она проросла сквозь её тело, но девушку вовремя нашли и откачали. \n\n' %(self.game.girl.name )
          text = self.description('suicide_fail_elf') 
          self.game.chronik.write_chronik(text_chronik,self.game.dragon.level,self.game.girl.girl_id)
          self.game.girl.third(text) 
        elif self.game.lair.type_name == 'cloud_castle':
          if self.game.girl.type == 'titan':
            self.suicide_fail_usual()
          else:
            text_chronik = u'%s попыталась спрыгнуть с колоссальной высоты, но её вовремя нашли и спасли. \n\n' %(self.game.girl.name )
            text = self.description('suicide_fail_cloud')
            self.game.chronik.write_chronik(text_chronik,self.game.dragon.level,self.game.girl.girl_id)
            self.game.girl.third(text) 
        else:
          self.suicide_fail_usual()


    def suicide_fail_usual(self):
        text_chronik = u'%s подружилась с драконьими слугами, но они, опасаясь гнева хозяина, наотрез отказались её есть. \n\n' %(self.game.girl.name )
        self.game.chronik.write_chronik(text_chronik,self.game.dragon.level,self.game.girl.girl_id)
        text = self.description('suicide_fail_usual')
        self.game.girl.third(text)  
# End_Mahariel_print

    def jail_girl(self):
        """
        Посадить текущую девушку за решетку.
        """
        if self.game.girl.jailed:
            text = self.description('jailed')
            self.prisoners.insert(self.active, self.game.girl)
        else:
            text = self.description('jail')
            self.game.girl.jailed = True
            self.prisoners.append(self.game.girl)
        return text

    def set_active(self, index):
        """
        Достать девушку с номером index из темницы
        """
        self.game.girl = self.prisoners[index]
        self.active = index
        del self.prisoners[index]

    def eat_girl(self):
        """
        Скушать девушку.
        """
        self.game.dragon.hunger -= 1
        if self.game.dragon.lust < 3:
            self.game.dragon.lust += 1
        self.game.dragon.bloodiness = 0
        if self.game.girl.cripple:
          return self.description('eat_cripple')
        else:
          return self.description('eat')

    def rob_girl(self):
        """
        Ограбить девушку.
        """
        self.game.lair.treasury.receive_treasures(self.game.girl.treasure)
        return self.description('rob')

    def prisoners_list(self):
        """
        Возвращает список плененных девушек.
        """
        jail_list = []
        for girl_i in xrange(len(self.prisoners)):
            jail_list.append(self.prisoners[girl_i].name)
        return jail_list

    @property
    def prisoners_count(self):
        """
        Возвращает количество плененных девушек.
        """
        return len(self.prisoners)

    def description(self, status, say=False):
        """
        Генерация описания ситуации для текущей девушки (self.game.girl).
        status - кодовое описание ситуации
        say - если истина - описание выводится сразу на экран
        Возвращается текст описания или None, если текст в списке не найден
        """
        format_dict = {
            'dragon_name': self.game.dragon.name,
            'dragon_name_full': self.game.dragon.fullname,
            'dragon_type': self.game.dragon.kind,
            'girl_name': self.game.girl.name,
            'girl_title': girls_data.girls_info[self.game.girl.type]['description'],
            'g_natu': self.game.girl.nature,
        }
        girl_type = self.game.girl.type
        if girl_type not in girls_data.girls_texts or status not in girls_data.girls_texts[girl_type]:
            girl_type = 'girl'
        if status in girls_data.girls_texts[girl_type]:
          if status == 'shout':   # Крики при сексе зависят от характера девушки
              text = random.choice(girls_data.girls_texts[girl_type][status][self.game.girl.nature])
          else:
                text = random.choice(girls_data.girls_texts[girl_type][status])
          if self.spawn:
                # Если список отродий не пуст - получаем имя последнего для возможной подстановки
                format_dict['spawn_name'] = girls_data.spawn_info[self.spawn[-1]]['born'].capitalize()
          if status == 'rob':
                treas_description = self.game.lair.treasury.treasures_description(self.game.girl.treasure)
                treas_description = '\n'.join(treas_description) + u'.'
                self.game.girl.treasure = []
                format_dict['rob_list'] = treas_description
          text = text % format_dict
        else:
            text = None
        if say and text:
            self.game.girl.third(text)  # выдача сообщения
            store.nvl_list = []  # вариант nvl clear на питоне
        else:
            return text

    @staticmethod
    def event(event_type, *args, **kwargs):
        if event_type in girls_data.girl_events:
            if girls_data.girl_events[event_type] is not None:
                call(girls_data.girl_events[event_type], *args, **kwargs)
        else:
            raise Exception("Unknown event: %s" % event_type)
        return

    def before_sleep(self):
        """
        Все действия до начала сна - смерть с тоски, может быть что-то еще?
        """
        self.love_escape()  # Девушки бегут с возлюбленным
        self.escape_without_guard()  # Девушки бегут при отсутствии стражи
#        self.death_of_hunger()  # Девушки умирают от голода Больше не умирают.
# Девушки проявляют активность
        for girl_i in reversed(xrange(self.prisoners_count)):
          self.game.girl = self.prisoners[girl_i]
          self.event('dragon_lair')
          if (not self.game.girl.virgin) and (not self.game.girl.pregnant):
            if self.game.girl.cripple: # Аттракцион
              call("lb_cripple_impaled")
            elif self.game.girl.blind: # Успешный побег
              self.event('escape')  # событие "побег из заключения"
              self.try_to_go()
            else:
              if self.game.girl.nature == 'innocent':  # После рождения отродья невинные гарантированно совершают самоубийство.          
                # @fdsc  Девушек никогда не съедают и они не кончают жизнь самоубийством
                # self.suicide_attemp()
                # self.suicide_sucsess()
                None
              # @fdsc
              #elif self.game.girl.nature == 'proud': # После рождения отродья гордые гарантированно бегут.
              #  self.event('escape')  # событие "побег из заключения"
              #  self.try_to_go()
              #  del self.prisoners[girl_i]
              elif self.game.girl.nature == 'lust':  # После рождения отродья похотливых  гарантировано съедают.
                # @fdsc Девушек никогда не съедают
                #self.event('girl_kitchen')
                None
            # del self.prisoners[girl_i]
          elif self.game.girl.old: # Слишком стары
            # @fdsc  Здесь разрешаем съесть старых девушек
            self.event('girl_kitchen')
            del self.prisoners[girl_i]

            
    def next_year(self):
        """
        Все действия с девушками за год.
        """
        # плененные девушки
        self.love_escape()  # Девушки бегут с возлюбленным
        self.escape_without_guard()  # Девушки бегут при отсутствии стражи
#        self.death_of_hunger()  # Девушки умирают от голода
        for girl_i in reversed(xrange(self.prisoners_count)):
          self.game.girl = self.prisoners[girl_i]
          g_type = self.game.girl.type
          g_nature = self.game.girl.nature # упрощение обращения к характеру девушки
          self.event('dragon_lair')
        # Девушки проявляют активность
        # Влюблённость в контрабандиста
          if self.love_possible_smuggler:
            if self.game.girl.type == 'peasant' and (random.randint(1, 6) == 1):
              self.game.love.new_love_smuggler()
            elif self.game.girl.type == 'citizen' and (random.randint(1, 8) == 1):
              self.game.love.new_love_smuggler()
            elif self.game.girl.type == 'princess' and (random.randint(1, 10) == 1):
              self.game.love.new_love_smuggler()
            elif self.game.girl.type == 'elf' and (random.randint(1, 12) == 1):
              self.game.love.new_love_smuggler()
            else:
              self.decision(girl_i) # Думают, что им делать
          elif self.love_possible_lizardman:
            if self.game.girl.type == 'peasant' and (random.randint(1, 10) == 1):
              self.game.love.new_love_lizardman()
            elif self.game.girl.type == 'citizen' and (random.randint(1, 12) == 1):
              self.game.love.new_love_lizardman()
            elif self.game.girl.type == 'princess' and (random.randint(1, 14) == 1):
              self.game.love.new_love_lizardman()
            elif self.game.girl.type == 'elf' and (random.randint(1, 16) == 1):
              self.game.love.new_love_lizardman()
            else:
              self.decision(girl_i)                     
          else:

            self.decision(girl_i)  # Все остальные случаи
                    
# Беременность и рождение отродий
          if self.game.girl.pregnant>0 and not self.game.girl.dead:
              self.prison_birth()         # Рождение отродья в неволе
              if self.game.girl.pregnant < 0:  # Проверка на смерть после родов
                if self.game.girl.love is not None: # Проверка на любовника
                  if self.game.girl.love.type == 'lizardman':
                    call ("lb_love_die_lizardman")
                del self.prisoners[girl_i]
                continue
              self.game.girl.pregnant = 0
#          self.game.narrator(u"Проверка связи, %s" %(self.game.girl.old)) 
          # Девушки слишком стары, чтобы рожать
          if (self.game.girl.type == 'peasant' or  self.game.girl.type == 'citizen' or self.game.girl.type == 'princess') and self.game.girl.virgin and (self.game.year-self.game.girl.birth_year>30): 
            call("lb_old_maid")
        # свободные, в том числе только что сбежавшие. Отслеживаются только беременные
        for girl_i in xrange(len(self.free_list)):
#            self.game.narrator(u"%s" %(self.game.girl.name))
            self.game.girl = self.free_list[girl_i]
            g_type = self.game.girl.type
            g_nature = self.game.girl.nature # упрощение обращения к характеру девушки
            if self.game.girl.pregnant > 0: # Проверка на беременность. Да, теперь надо.
              if self.is_love: # Проверка на влюблённость
                pass
              elif self.game.girl.blind:
                call("lb_pregnant_blind")
              elif self.game.girl.cripple:
                call("lb_pregnant_cripple")
#              elif self.game.girl.willing:
#                call("lb_pregnant_willing")
              else:
                if not girls_data.girls_info[self.game.girl.type]['giantess']: # Чуть не забыл проверку на гигантов
                    self.event('pregnant_decision',g_type,g_nature)
              if self.game.girl.pregnant == 0: # Проверка, убита ли девушка
                  continue
              if self.game.girl.pregnant > 0: # Повторная проверка на беременность
                  girl_type = girls_data.girls_info[self.game.girl.type]
                  self.birth()
                  self.event('free_spawn', self.spawn_type)  # событие "рождение отродий на воле"
                  if self.game.girl.cripple and self.game.girl.love is None:  # История калеки
                    if (random.randint(1, 2) == 1):
                      enc = "lb_cripple_birth_fail" # Монстру не повезло
                    else:
                      self.free_spawn(girls_data.spawn_info[self.spawn_type]['power'],self.spawn_type)
                      enc = "lb_cripple_birth_success" # Монстру повезло
                    call(enc)
                  else:
                    self.free_spawn(girls_data.spawn_info[self.spawn_type]['power'],self.spawn_type)
                  if self.game.girl.pregnant < 0:  # Проверка на смерть после родов
                    continue
                  self.game.girl.pregnant = 0
            if self.is_love: # Проверка на влюблённость
              if not self.game.mistress_alive:
                death_coeff=0
              elif self.game.girl.blind:
                death_coeff=0
              else:
                if self.game.girl.nature == 'innocent':
                  death_coeff=0.2
                elif self.game.girl.nature == 'proud':
                  death_coeff=1.0
                elif self.game.girl.nature == 'lust':
                  death_coeff=20.0
              choices = [
                  ("lb_love_lizardman_mistress", 100*death_coeff),
                  ("lb_love_lizardman_uncle",  10)]
              enc = weighted_random(choices)  # Обработка результатов вернувшейся аристократки
              call(enc)
              continue
            if self.game.girl.blind: # Слепые
              enc="lb_return_" + g_type + "_blind"
              call(enc)
              continue
            if self.game.girl.cripple: # Калеки
#              enc="lb_return_" + g_type + "_cripple"
#              call (enc)
              call("lb_return_cripple")           
              pass # Пока нет
              continue
            if self.game.girl.virgin:   #Девушка сохранила девственность. Ну надо же
                if g_type == 'citizen' or g_type == 'peasant' or g_type == 'princess' or g_type == 'elf' or g_type == 'mermaid': 
                    enc = 'return_' + g_type + '_virgin'
                    self.event(enc)
                elif g_type == 'ogre':
                    self.event('return_ogre_virgin')
                elif g_type == 'siren' or g_type == 'ice' or g_type == 'fire' or g_type == 'titan':
                    enc = 'return_' + g_type
                    self.event(enc)
            else:            # Поматросил и бросил
                encWilling = 'return_' + g_type + '_virgin'
                if g_type == 'citizen': # Возвращается горожанка
                  if g_nature == 'innocent':
                    choices = [
                        ("return_citizen_virgin", 10),
                        ("return_citizen_raped",  30),
                        ("return_citizen_death",  60)]
                  elif g_nature == 'proud':
                    choices = [
                        ("return_citizen_virgin",  30),
                        ("return_citizen_raped",   20),
                        ("return_citizen_warrior", 50)]
                  elif g_nature == 'lust':
                    choices = [
                        ("return_citizen_virgin",  10),
                        ("return_citizen_brothel", 40),
                        ("return_citizen_murder",  50),]

                  enc = weighted_random(choices)  # Обработка результатов вернувшейся горожанки

                  # @fdsc Девушки не умирают просто так, если договорились с драконом
                  if self.game.girl.willing and enc != encWilling:
                    enc = encWilling
                    self.game.dragon.drain_energy(1, True)
                    self.game.chronik.live('willing_girl', None)
                    call("lb_willing_help")

                  self.event(enc)

                elif g_type == 'peasant':  # Возвращается крестьянка
                  if g_nature == 'innocent':
                    choices = [
                        ("return_peasant_virgin", 10),
                        ("return_peasant_raped",  30),
                        ("return_peasant_death",  60)]
                  elif g_nature == 'proud':
                    choices = [
                        ("return_peasant_virgin",  30),
                        ("return_peasant_raped",   20),
                        ("return_peasant_warrior", 50)]
                  elif g_nature == 'lust':
                    choices = [
                        ("return_peasant_virgin",  10),
                        ("return_peasant_brothel", 40),
                        ("return_peasant_murder",  50),]
                  enc = weighted_random(choices)  # Обработка результатов вернувшейся крестьянки
                  
                  # @fdsc Девушки не умирают просто так, если договорились с драконом
                  if self.game.girl.willing and enc != encWilling:
                    enc = encWilling
                    self.game.dragon.drain_energy(1, True)
                    self.game.chronik.live('willing_girl', None)
                    call("lb_willing_help")

                  self.event(enc)

                elif g_type == 'princess': # Возвращение аристократок
                  if g_nature == 'innocent':
                    choices = [
                        ("return_princess_virgin", 10),
                        ("return_princess_raped",  30),
                        ("return_princess_death",  60)]
                  elif g_nature == 'proud':
                    choices = [
                        ("return_princess_virgin",  30),
                        ("return_princess_raped",   20),
                        ("return_princess_warrior", 50)]
                  elif g_nature == 'lust':
                    choices = [
                        ("return_princess_virgin",  10),
                        ("return_princess_brothel", 40),
                        ("return_princess_murder",  50),]
                  enc = weighted_random(choices)  # Обработка результатов вернувшейся аристократки
                  
                  # @fdsc Девушки не умирают просто так, если договорились с драконом
                  if self.game.girl.willing and enc != encWilling:
                    enc = encWilling
                    self.game.dragon.drain_energy(1, True)
                    self.game.chronik.live('willing_girl', None)
                    call("lb_willing_help")

                  self.event(enc)

                elif g_type == 'elf': # Возвращение эльфиек
                  if g_nature == 'innocent':
                    choices = [
                        ("return_elf_virgin", 10),
                        ("return_elf_raped",  30),
                        ("return_elf_death",  60)]
                  elif g_nature == 'proud':
                    choices = [
                        ("return_elf_virgin",  30),
                        ("return_elf_raped",   20),
                        ("return_elf_warrior", 50)]
                  elif g_nature == 'lust':
                    choices = [
                        ("return_elf_virgin",  10),
                        ("return_elf_brothel", 40),
                        ("return_elf_murder",  50),]
                  enc = weighted_random(choices)  # Обработка результатов вернувшейся эльфийки
                  
                  # @fdsc Девушки не умирают просто так, если договорились с драконом
                  if self.game.girl.willing and enc != encWilling:
                    enc = encWilling
                    self.game.dragon.drain_energy(1, True)
                    self.game.chronik.live('willing_girl', None)
                    call("lb_willing_help")

                  self.event(enc)

                elif g_type == 'mermaid': # Возвращение русалок
                  if g_nature == 'innocent':
                    choices = [
                        ("return_mermaid_virgin", 10),
                        ("return_mermaid_raped",  30),
                        ("return_mermaid_death",  60)]
                  elif g_nature == 'proud':
                    choices = [
                        ("return_mermaid_virgin",  30),
                        ("return_mermaid_raped",   20),
                        ("return_mermaid_warrior", 50)]
                  elif g_nature == 'lust':
                    choices = [
                        ("return_mermaid_virgin",  10),
                        ("return_mermaid_brothel", 40),
                        ("return_mermaid_murder",  50),]
                  enc = weighted_random(choices)  # Обработка результатов вернувшейся эльфийки
                  
                  # @fdsc Девушки не умирают просто так, если договорились с драконом
                  if self.game.girl.willing and enc != encWilling:
                    enc = encWilling
                    self.game.dragon.drain_energy(1, True)
                    self.game.chronik.live('willing_girl', None)
                    call("lb_willing_help")

                  self.event(enc)

                elif g_type == 'ogre':    # Возвращение великанш
                    self.event('return_ogre_raped')
                elif g_type == 'siren' or g_type == 'ice' or g_type == 'fire' or g_type == 'titan':
                    enc = 'return_' + g_type
                    self.event(enc)
        self.free_list = []  # очистка списка - либо родила, либо убили - отслеживать дальше не имеет смысла
        for girl_i in xrange(len(self.whore_list)): # Проверка проституток
            self.game.girl = self.whore_list[girl_i]
            girl_type = girls_data.girls_info[self.game.girl.type]
            call("lb_pregnant_whore")
            self.birth()
            self.whore = True
            self.event('free_spawn', self.spawn_type)  # событие "рождение отродий на воле"
            self.free_spawn(girls_data.spawn_info[self.spawn_type]['power'],self.spawn_type)
            self.whore = False
            text = u'После этого %s долгие годы работала по своей прямой специальности и достигла в ней немалых высот.' %(self.game.girl.name)
            self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
            current_image='img/bg/city/brothel_girl.jpg'
            self.game.chronik.live('brothel_girl',current_image)
        self.whore_list = []
        # Проверка рабынь в Султанате
        for girl_i in xrange(len(self.sultan_list)):
            self.game.girl = self.sultan_list[girl_i]
            call("lb_sultan")
        self.sultan_list = []

        
        # @fdsc Обработка девушек в борделе
        for girl_i in reversed(xrange(self.prisoners_count)):
            self.game.girl = self.prisoners[girl_i]
            if self.game.girl.in_brothel:
                if self.game.girl.virgin:

                    self.game.lair.treasury.money += self.game.girl.get_brothel_price

                    text = u"%s лишилась невинности в борделе и заработала %i\n" % (self.game.girl.name, self.game.girl.get_brothel_price)
                    self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
                    self.game.girl.third(text)
                    
                    self.game.girl.virgin = False

                self.game.lair.treasury.money += self.game.girl.get_brothel_price

                text = u"%s отработала год в борделе и заработала %i\n" % (self.game.girl.name, self.game.girl.get_brothel_price)
                self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
                self.game.girl.third(text)

                self.game.girl.years_in_brothel += 1

        # Всем девушкам, которые к концу цикла остались в тюрьме, прибавляем следующий год в описание
        for girl_i in reversed(xrange(self.prisoners_count)):
            self.game.girl = self.prisoners[girl_i]
            text = u"{font=fonts/PFMonumentaPro-Regular.ttf}\n Год %s эпохи дракона \n{/font}" % self.game.year
            self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)

    def decision(self,girl_i):
        if self.game.girl.cripple: # Искалеченные
          if self.game.girl.pregnant>0:
            if (random.randint(1, 3) == 1):  # Калеки умирают
              call("lb_cripple_die")
              self.game.girl.pregnant = -1
              del self.prisoners[girl_i]
            else:
              call("lb_cripple_alive")
          else:
            call("lb_cripple_impaled")
            del self.prisoners[girl_i]
        elif self.game.girl.blind: # Слепые
          if self.game.girl.pregnant>0:
            call("lb_blind_alive")
          else:
            self.event('escape')  # событие "побег из заключения"
            self.try_to_go()  
            del self.prisoners[girl_i]
        elif self.game.girl.willing:  # Добровольцы
            # @fdsc Просто убрал лишнее сообщение
            # call("lb_willing_wait")
            None
        else:
          self.decision_common(girl_i)

    def decision_common(self,girl_i):  # Общее решение
        if self.game.girl.nature == 'innocent':  # Невинные, пытаются покончить жизнь самоубийством.
                        choices = [
                          ("suicide_decision", 50),
                          ("escape_decision", 10)]
        elif self.game.girl.nature == 'proud':  # Гордые пытаются убежать.
                        choices = [
                          ("suicide_decision", 10),
                          ("escape_decision", 50)]
        elif self.game.girl.nature == 'lust':  # Похотливые пытаются соблазнить слуг.   
                        choices = [
                          ("escape_decision", 10),
                          ("seduction_decision", 50)]
        enc = weighted_random(choices)
        if enc == 'suicide_decision':
          self.suicide_decision(girl_i)
        elif enc == 'escape_decision':
          self.escape_decision(girl_i)
        elif enc == 'seduction_decision':
          self.seduction_decision(girl_i)

    def prison_birth(self):
        girl_type = girls_data.girls_info[self.game.girl.type]
        self.birth()
        self.spawn.append(girl_type[self.spawn_class])
        self.event('spawn', girl_type[self.spawn_class])  # событие "рождение отродий"


    # noinspection PyTypeChecker
    def after_awakening(self):
        """
        Все действия после пробуждения - разбираемся с воспитанными отродьями.
        """
        for spawn_i in xrange(len(self.spawn)):
            spawn_type = self.spawn[spawn_i]  # упрощение обращения к типу отродий
            spawn = girls_data.spawn_info[spawn_type]  # упрощение обращения к данным отродий
            renpy.show("meow", what=store.Image("img/scene/spawn/%s.jpg" % spawn_type))
            spawn_mod = spawn['modifier']  # упрощение обращения к списку модификаторов отродий
            # Делаем проверку. Истина, если не морское отродье или морское в подводном логове
            # TODO: Возможно стоит сделать умирание слуги, если оно не морское и в морском логове.
            marine_check = ('marine' not in spawn_mod) or \
                           (self.game.lair.type.require and 'swimming' in self.game.lair.type.require)
            spawn_menu = [(u"К Вам приходит %s и просит назначения" % spawn['name'], None)]  # меню отродий
            # Возможные пункты меню
            # @fdsc
            # if ('poisonous' in spawn_mod) and ('poison_guards' not in self.game.lair.upgrades) and marine_check:
            if ('poisonous' in spawn_mod) and marine_check:
                spawn_menu.append((u"Выпустить в логово", u'poison_guards'))
            if ('servant' in spawn_mod) and ('servant' not in self.game.lair.upgrades) and marine_check:
            # if ('servant' in spawn_mod) and marine_check:
                spawn_menu.append((u"Сделать слугой", 'servant'))
            # if ('warrior' in spawn_mod) and ('regular_guards' not in self.game.lair.upgrades) and marine_check:
            if ('warrior' in spawn_mod) and marine_check:
                spawn_menu.append((u"Сделать охранником", 'regular_guards'))
            # if ('elite' in spawn_mod) and ('elite_guards' not in self.game.lair.upgrades) and marine_check:
            if ('elite' in spawn_mod) and marine_check:
                spawn_menu.append((u"Сделать элитным охранником", 'elite_guards'))
            spawn_menu.append((u"Выпустить в королевство", 'free'))
            if (('servant' in spawn_mod) or
                    ('warrior' in spawn_mod) or
                    ('elite' in spawn_mod)) and \
                    ('marine' not in spawn_mod):
                spawn_menu.append((u"Отправить в армию тьмы", 'army_of_darkness'))

            menu_action = renpy.display_menu(spawn_menu)

            if menu_action == 'free':
                renpy.say(self.game.narrator, u"%s отправляется бесчинствовать в королевстве." % spawn['name'])
                self.free_spawn(spawn['power'],spawn_type)
            elif menu_action == 'army_of_darkness':
                renpy.say(self.game.narrator, u"%s отправляется в армию тьмы." % spawn['name'])
                self.army_of_darkness(spawn_type)
            else:
                # выдача сообщения о начале работы
                renpy.say(self.game.narrator, u"%s приступает к выполнению обязанностей." % spawn['name'])
                # Если у нас ящерик, то в будущем пленница может завести с ним роман
                if spawn_type == 'lizardman':
                    self.game.lair.beast = 'lizardman'
                # выдача сообщения о конце работы, если это необходимо
                # @fdsc Выдаём сообщение, только если есть кому уходить
                if 'replaces' in data.lair_upgrades[menu_action].keys():
                    replace = data.lair_upgrades[menu_action]['replaces']

                    if replace in self.game.lair.upgrades:
                        renpy.say(self.game.narrator,
                              u"%s больше не требуются и уходят." % data.lair_upgrades[replace]['name'])

                # добавление в улучшение логова
                self.game.lair.add_upgrade(menu_action)
                # Узнав, что контрабандисты покинули логово, влюблённые девушки накладывают на себя руки.
                if 'smuggler_guards' not in self.game.lair.upgrades:
                  self.romeo_check()

        renpy.hide("meow")
        self.spawn = []
        # Прибытие каравана Хакима
        caravan_trade = self.game.historical_check('caravan_trade')
        if not caravan_trade:
          sultanat_trade_ultimate = self.game.historical_check('sultanat_trade_ultimate')
          if sultanat_trade_ultimate and self.game.dragon.reputation.level>=10:
            call("lb_caravan_trade")
            achieve_target("hakim", "sultan_trade")
#            if not freeplay:
 #             call ("lb_achievement_acquired")

           
        

    # Узнав, что контрабандисты покинули логово, влюблённые девушки накладывают на себя руки.
    def romeo_check(self):
        for girl_i in reversed(xrange(self.prisoners_count)):
          self.game.girl = self.prisoners[girl_i]
          if self.game.girl.love is not None:
            if self.game.girl.love.type == 'smuggler':
              text = u'Незадолго до ухода контрабандисты обнаружили, что %s крысятничал, и казнили его. Когда %s узнала о смерти своего любимого, жить ей стало незачем. \n\n' %(self.game.girl.love.name, self.game.girl.name )
              self.game.narrator(text)
              self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
              del self.prisoners[girl_i]
              if ('servant' not in self.game.lair.upgrades) and ('gremlin_servant' not in self.game.lair.upgrades):
                text = u'%s заморила себя голодом ' %(self.game.girl.name )
                self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
                self.event('hunger_death')  # событие "смерть девушки от голода"
              else:
                self.suicide_attemp()
                self.suicide_sucsess() 

    def free_spawn(self, power,spawn_type):
        """
        Действия отродий на свободе
        """
        # Растёт разруха. Надо проверить чтобы это срабатывало по одному разу на тип отродий.
        self.game.poverty.value += 1
#        self.game.narrator(u"%s " % self.game.poverty._planned)
        self.spawn_list.append(spawn_type)
#        self.spawn_list_girls.append()
        pass

    def army_of_darkness(self, warrior_type):
        """
        Отправка в армию тьмы
        """
        self.game.army.add_warrior(warrior_type)

    @property
    def is_mating_possible(self):
        """
        Возвращает возможность совокупления - истину или ложь.
        # TODO: проверка на превращение в человека
        """
        assert self.game.girl, "Girl not found"
        mating_possible = self.game.girl.virgin and self.game.dragon.lust > 0 and not self.game.girl.old
        if girls_data.girls_info[self.game.girl.type]['giantess']:
            mating_possible = self.game.dragon.size > 3 and mating_possible
        if not girls_data.girls_info[self.game.girl.type]['giantess']:
            mating_possible = self.game.dragon.size < 4 and mating_possible
        return mating_possible

    @property
    def is_giant(self):
        """
        Проверяет великанш
        """
        assert self.game.girl, "Girl not found"
        giant = girls_data.girls_info[self.game.girl.type]['giantess']
        return giant

    @property
    def is_love(self):
        """
        Проверка на влюблённость
        """
        assert self.game.girl, "Girl not found"
        if self.game.girl.love is None:
          return False
        else:
          if self.game.girl.love.type == 'lizardman':
            return True
          else:
            return False

    @property
    def love_possible_smuggler(self):
        """
        Проверяет возможность большой и чистой любви
        """
        assert self.game.girl, "Girl not found"
        possible = self.game.girl.love is None and 'smuggler_guards' in self.game.lair.upgrades and not girls_data.girls_info[self.game.girl.type]['giantess'] and not self.game.girl.type == 'mermaid' and not self.game.girl.blind and not self.game.girl.cripple and not self.game.girl.willing
        return possible

    @property
    def is_talk_possible(self):
        """
        Проверяет возможность соблазнения
        """
        assert self.game.girl, "Girl not found"
        possible = False
        if not self.game.girl.willing and self.game.girl.willing_attemp and self.game.girl.virgin and (self.game.girl.type=='peasant' or self.game.girl.type=='citizen' or self.game.girl.type=='princess'):
          if self.game.lair.treasury.most_expensive_jewelry_cost>data.gift_price[self.game.girl.type][self.game.girl.nature]:
            possible=True
        return possible


    @property
    def love_possible_lizardman(self):
        """
        Проверяет возможность ксенофилии с ящериком
        """
        assert self.game.girl, "Girl not found"
        possible = self.game.girl.love is None and self.game.lair.beast == 'lizardman' and not girls_data.girls_info[self.game.girl.type]['giantess'] and not self.game.girl.type == 'mermaid' and not self.game.girl.blind and not self.game.girl.cripple and not self.game.girl.willing
        return possible

    def girl_in_lair(self,girl_i):
        if self.game.girls_list.prisoners[girl_i].virgin:
          status = u"девственная"
        elif self.game.girls_list.prisoners[girl_i].pregnant>0:
          status = u"беременная"
        else:
          status = u"попользованная"
        if self.game.girls_list.prisoners[girl_i].love is not None:
          love = u", влюблённая"
        else:
          love = u""        
        if self.game.girls_list.prisoners[girl_i].blind:
          add = u", слепая"
        elif self.game.girls_list.prisoners[girl_i].cripple:
          add = u", искалеченная"
        else:
          add = u""
        if self.game.girls_list.prisoners[girl_i].in_brothel:
            add += u", в борделе (%d)" % self.game.girls_list.prisoners[girl_i].get_brothel_price

        girl = self.game.girls_list.prisoners[girl_i]
        d = u"%s, %s, %s, %s%s%s (качество: %d; %d лет)" %(girl.name, girls_data.girls_info[girl.type]['description'], girls_data.nature_info[girl.nature], status, love,add, girl.quality, self.game.year - girl.birth_year)
        return d

    def love_escape(self): # Побег девчонок и их возлюбленных из логова
        for girl_i in reversed(xrange(self.prisoners_count)):
          self.game.girl = self.prisoners[girl_i]
          self.event('dragon_lair')
# Проверка на побег влюблённых 
          if self.game.girl.love is not None: # Проверка на любовника
            if self.game.girl.love.type == 'smuggler':
              if self.game.girl.cripple:
                call ("lb_love_escape_smuggler_cripple")
              elif self.game.girl.blind:
                call ("lb_love_escape_smuggler_blind")
                del self.prisoners[girl_i]
              else:
                call ("lb_love_escape_smuggler")
                del self.prisoners[girl_i]
            elif self.game.girl.love.type == 'lizardman':
              if self.game.girl.cripple:
                call ("lb_love_lizardman_cripple")
              else:
                if self.game.girl.pregnant>0:
                  self.prison_birth()
                if self.game.girl.pregnant<0:
                  call ("lb_love_die_lizardman")
                else:
                  self.game.girl.pregnant = 0  # А то получится смешно
                  call ("lb_love_escape_lizardman")
              del self.prisoners[girl_i]

    def love_escape_ind(self): # Активируется в том случае, если пленницу отпускают из логова
        self.event('dragon_lair')
# Проверка на побег влюблённых 
        if self.game.girl.love.type == 'smuggler':
          if self.game.girl.cripple:
            call ("lb_love_smuggler_cripple")
          elif self.game.girl.blind:
            call ("lb_love_escape_smuggler_blind")
          else:
            call ("lb_love_escape_smuggler")
        elif self.game.girl.love.type == 'lizardman':
          if self.game.girl.cripple:
            call ("lb_love_lizardman_cripple")
          else:
#            if self.game.girl.pregnant>0:
#              self.prison_birth()
#            if self.game.girl.pregnant<0:
#              call ("lb_love_die_lizardman")
#            else:
              call ("lb_love_escape_lizardman")
            

    def escape_without_guard(self): # Охраны нет. Девушка убежала
        if 'regular_guards' not in self.game.lair.upgrades and 'elite_guards' not in self.game.lair.upgrades and 'smuggler_guards' not in self.game.lair.upgrades and not(('servant' in self.game.lair.upgrades) or ('gremlin_servant' in self.game.lair.upgrades)):
          for girl_i in reversed(xrange(self.prisoners_count)):
            self.game.girl = self.prisoners[girl_i]
#            a=not (self.game.girl.blind and self.game.girl.pregnant ==0)
#            self.game.narrator(u"%s" % a)
            del self.prisoners[girl_i]
#          if (random.randint(1, 2) == 1)  and 'regular_guards' not in self.game.lair.upgrades and 'elite_guards' not in self.game.lair.upgrades and 'smuggler_guards' not in self.game.lair.upgrades:
            if self.game.girl.cripple: # Некому заботиться. Инвалидки умирают с голоду.
              renpy.show("bg", what=store.Image(self.game.girl.cripple_image))
              current_image=u'%s' % self.game.girl.cripple_image
              text = u'Во время драконьего сна в логове не было ни слуг, ни охранников. Некому было позаботиться об инвалидке. %s умерла от голода и жажды. \n\n' %(self.game.girl.name )  
              self.game.narrator(u"%s" % text)  
              self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
              self.game.chronik.death('cripple_hunger',current_image)
            elif self.game.lair.type_name=='cloud_castle' and self.game.girl.type is not 'titan' and not(self.game.girl.blind and self.game.girl.pregnant ==0):  # Облачный замок. Нечего есть, некуда бежать, смерть с голода.
              text = u'Из-за безалаберности дракона %s умерла от голода. Перед смертью она распробывала собственные пальцы. ' %(self.game.girl.name )
              self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
              self.event('hunger_death')  # событие "смерть девушки от голода"
            else:   # Все остальные случаи. Пленницы радостно бегут из логова.
              self.event('dragon_lair')
              text = u'Пользуясь беспечностью дракона, %s сбежала из логова. \n\n' %(self.game.girl.name )
              self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
              self.event('escape')  # событие "побег из заключения"
              self.try_to_go() 
    
    def birth(self):
        girl_type = girls_data.girls_info[self.game.girl.type]
        if self.game.girl.pregnant == 1:
          self.spawn_class = 'regular_spawn'
        else:
          self.spawn_class = 'advanced_spawn'
        if 'educated_spawn' not in self.offspring:
          self.offspring.append('educated_spawn')
        if girl_type['giantess']:
          girl_size = 'giantess'
        else:
          girl_size = 'common_size'
        if girl_size not in self.offspring:
          self.offspring.append(girl_size)
        self.spawn_type = girls_data.girls_info[self.game.girl.type][self.spawn_class]
        text = u'В крови и муках %s родила %s. ' %(self.game.girl.name, girls_data.spawn_info[self.spawn_type]['name_genitive'])
        self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)

    def death_of_hunger(self):
        for girl_i in reversed(xrange(self.prisoners_count)):
          self.game.girl = self.prisoners[girl_i]
          self.event('dragon_lair')
          if not(('servant' in self.game.lair.upgrades) or ('gremlin_servant' in self.game.lair.upgrades)):
            text = u'Из-за безалаберности дракона %s умерла от голода. Перед смертью она распробывала собственные пальцы. ' %(self.game.girl.name )
            self.game.chronik.write_chronik(text,self.game.dragon.level,self.game.girl.girl_id)
            self.event('hunger_death')  # событие "смерть девушки от голода"
            del self.prisoners[girl_i]

    @property
    def free_size(self):  # Сколько может поместиться пленница
        if self.prisoners_count==0:
          return self.game.lair.size
        else:
          full=0
          for girl_i in reversed(xrange(self.prisoners_count)):
            full+=self.prisoners[girl_i].size
          return self.game.lair.size-full

