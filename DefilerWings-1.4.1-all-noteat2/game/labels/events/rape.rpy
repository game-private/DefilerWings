# coding=utf-8
init:
    define vpunch_long = Move((10, 10), (10, -10), .10, bounce=True, repeat=True, delay=1.7)

python:
    import random

label lb_rape_eat_girl():
    $ current_image = rape.relative_path + "/ground.jpg"
    show expression current_image as bg
    game.dragon 'Сопротивляется, брыкается... одно мучение с ней! Может, стоит её сожрать?'
    menu:
        'Определённо, стоит!':
#            if game.girl.type
            $ text = u'%s - это не только аппарат для производства отродий, но и 50-60 килограмм диетического, легкоусвояемого мяса. %s сначала хотел надругаться над своей жертвой, но она была настолько аппетитна, что он не удержался и сожрал её.\n\n' % (game.girl.name, game.dragon.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            stop music fadeout 1.0
            call lb_eat from _call_lb_eat_6
            $ game.rape.rage = 0.
            $ game.girl.dead = True
            if game.girl.type =='afrodita':
              'Аватара Афродиты прямо во рту рассыпается мельчайшей пылью.'
            if game.girl.type =='danu':
              'Аватара Дану прямо во рту рассыпается мельчайшей пылью.'
            if game.girl.love is not None:
              if game.girl.love.type == 'lizardman':
                call lb_love_suicide_lizardman from _call_lb_love_suicide_lizardman_1
        'Может, пока не время?' if game.rape.rage < 50:
            call screen start_sex
    return

label lb_rape_kill_girl:
    $ current_image = rape.relative_path + "/ground.jpg"
    show expression current_image as bg
    game.dragon 'Сопротивляется, брыкается... одно мучение с ней! Может, стоит проверить, что там у неё внутри?'
    menu:
        'Определённо, стоит!':
            stop music fadeout 1.0
            play sound "sound/eat.ogg"
            show expression "img/scene/turn_apart.jpg" 
            pause (500.0)
            $ text = u'%s разорвал на части пленницу просто ради забавы. \n\n' % (game. dragon.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            $ game.chronik.death('turned_apart',"img/scene/turn_apart.jpg")
            $ game.girl.dead = True
            if game.girl.love is not None:
              if game.girl.love.type == 'lizardman':
                call lb_love_suicide_lizardman from _call_lb_love_suicide_lizardman_2
        'Может, пока не время?' if game.rape.rage < 50:
            call screen start_sex
    return

label lb_rape_erection:  # Непосредственное проникновение
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    $ ratio_proud=game.rape.actual_proud/game.rape.full_proud
    if game.rape.erection == 0:
      game.dragon.third '[game.dragon.name] неспешно раздвигает складки плоти, обнажая набрякший, огромный, увитый вздувшимися венами член'
    elif game.rape.erection == 1:
      if not girls_data.girls_info[game.girl.type]['giantess']:
        if game.girl.virgin:
          game.dragon.third '[game.dragon.name] раздвигает своим удом половые губы пленницы. Похоже, [game.girl.name] через несколько мгновений перестанет быть девственницей.'
        else:
          game.dragon.third '[game.dragon.name] ещё раз раздвигает своим удом половые губы пленницы. Ну, на этот-то раз всё пройдёт как по маслу?!'
      else:
        game.dragon.third '[game.dragon.name] раздвигает своим удом половые губы пленницы. Похоже, [game.girl.name] через несколько мгновений познает любовь дракона.'
    elif game.rape.erection == 2:
      game.dragon.third '[game.dragon.name], полностью отдавшись страсти, совершает энергичные фрикции'
    elif game.rape.erection == 3:
      game.dragon.third 'О, этот блаженный момент, когда сперма готова излиться в нетронутое лоно!'
# А вот получится ли?
    if game.rape.body and game.rape.arms:   # Девчонка свободна
      if ratio_proud>0.66:
        if not game.girl.willing:
          if game.girl.blind:
            game.girl.third '[game.girl.name], выкрикивая оскорбления, вселпую мечется по логову'
          else:
            game.girl.third '[game.girl.name], выкрикивая оскорбления, убегает от дракона'
          'Кажется, [game.dragon.name] делает что-то не так.'
          $ game.rape.rage += random.randint(5,8)
        else:
          game.girl.third '[game.girl.name] стоит, крепко сжав кулаки, и зло смотрит прямо в глаза дракона'
          $ game.rape.erection += 1
          call lb_rape_body from _call_lb_rape_body_1
          return
      elif ratio_proud>0.33 and ratio_proud <=0.66:
        if not game.girl.willing:
          game.girl.third '[game.girl.name] пятится прочь. От её визга закладывает уши'
          'Кажется, [game.dragon.name] делает что-то не так.'
          $ game.rape.rage += random.randint(3,5)
        else:
          game.girl.third '[game.girl.name] в панике зажмуривается и принимает классическую "позу стыдливости": одна рука прикрывает промежность, вторая пытается закрыть груди'
          $ game.rape.erection += 1
          call lb_rape_body from _call_lb_rape_body_2
          return
      elif ratio_proud>0 and ratio_proud <=0.33:
        if not game.girl.willing:
          game.girl.third '[game.girl.name] пятится прочь, заламывая руки и умоляя дракона отпустить её обратно'
          'Кажется, [game.dragon.name] делает что-то не так.'
          $ game.rape.rage += random.randint(1,3)
        else:
          if game.girl.type == 'afrodita':
            game.girl.third '[game.girl.name] подходит к дракону и начинает умело и старательно ласкать его член руками и ротиком. Кажется, у неё в таких вещах большой практический опыт!'
          else:
            game.girl.third '[game.girl.name] подходит к дракону и начинает неумело, но старательно ласкать его член руками'
          $ game.rape.erection += 1
          call lb_rape_body from _call_lb_rape_body_3
          return
      elif ratio_proud==0:
        call lb_rape_broken from _call_lb_rape_broken_1

# Руки свободны
    elif not game.rape.body and game.rape.arms:   # Руки у девчонки свободны
      if ratio_proud>0.66: # Честь превыше жизни
        if game.rape.erection == 0: # Приставить член к влагалищу
          if game.rape.size == 1: # Миниатюрный дракончик
            if not game.girl.willing:
              if random.randint(1,5) == 1: # Дракону не повезло
                if game.girl.blind:
                  game.girl.third '[game.girl.name] изворачивается и вслепую бьёт ребром ладони по восставшему драконьему члену!'
                else:
                  game.girl.third '[game.girl.name] изворачивается и одним точным ударом бьёт ребром ладони по восставшему драконьему члену!'
                call lb_rape_dragon_penis from _call_lb_rape_dragon_penis_1
              else:
                game.girl.third 'Когда член дракона упирается во влагалище девушки, [game.girl.name] начинает осыпать насильника градом резких и болезненных ударов. Эдак она и повредить что-нибудь может!'
                if 'tough_scale' in game.dragon.modifiers():
                  $ game.rape.rage += random.randint(10,16)
                else:
                  $ game.rape.rage += random.randint(12,18)
                $ game.rape.erection += 1
            else: # Согласна
              game.girl.third 'Когда член дракона упирается во влагалище девушки, [game.girl.name] отворачивается, прикусывает губу и изо всех сжимает кулаки. Похоже, маленький рост дракона искушает её ложной надеждой на успех - но [game.girl.name] всё-таки удерживается от сопротивления.'   
              $ game.rape.erection += 1
          elif game.rape.size == 2: # Средний дракон 
            if not game.girl.willing:
              if random.randint(1,8) == 1: # Дракону не повезло
                if game.girl.blind:
                  game.girl.third '[game.girl.name] изворачивается каким-то хитрым образом и вслепую бьёт ребром ладони по восставшему драконьему члену!'
                else:
                  game.girl.third '[game.girl.name] изворачивается каким-то хитрым образом и одним точным ударом бьёт ребром ладони по восставшему драконьему члену!'
                call lb_rape_dragon_penis from _call_lb_rape_dragon_penis_2
              else:
                game.girl.third 'Когда член дракона упирается во влагалище девушки, [game.girl.name] начинает осыпать тушу насильника градом резких ударов. Повредить-то оно не повредит, но раздражает и отвлекает, зараза!'
                if 'tough_scale' in game.dragon.modifiers():
                  $ game.rape.rage += random.randint(8,14)
                else:
                  $ game.rape.rage += random.randint(10,16)
                $ game.rape.erection += 1
            else: # Согласна
              game.girl.third 'Когда член дракона упирается во влагалище девушки, [game.girl.name] отворачивается, прикусывает губу и изо всех сжимает кулаки. Похоже, она пытается удерживаться от сопротивления. Успешно.'   
              $ game.rape.erection += 1
          elif game.rape.size == 3: # Матёрый драконище 
            if not game.girl.willing:            
              if random.randint(1,10) == 1: # Дракону не повезло
                if game.girl.blind:
                  game.girl.third '[game.girl.name] изворачивается каким-то немыслимым образом и вслепую бьёт ребром ладони по восставшему драконьему члену!'
                else:
                  game.girl.third '[game.girl.name] изворачивается каким-то немыслимым образом и одним точным ударом бьёт ребром ладони по восставшему драконьему члену!'
                call lb_rape_dragon_penis from _call_lb_rape_dragon_penis_3
              else:
                game.girl.third 'Когда член дракона упирается во влагалище девушки, [game.girl.name] начинает осыпать исполинскую тушу насильника градом ударов. [game.dragon.name] едва ощущает сопротивление пленницы, но всё равно: такое поведение весьма...   раздражает.'
                if 'tough_scale' in game.dragon.modifiers():
                  $ game.rape.rage += random.randint(6,10)
                else:
                  $ game.rape.rage += random.randint(8,12)
                $ game.rape.erection += 1
            else: # Согласна
              game.girl.third 'Когда член дракона упирается во влагалище девушки, [game.girl.name] отворачивается, прикусывает губу и изо всех сжимает кулаки. Впрочем, даже если бы она начала сопротивляться - это всё равно не помогло бы.'   
              $ game.rape.erection += 1

        elif game.rape.erection == 1: # Разорвать девственную плеву.
          if game.rape.size == 1: # Миниатюрный дракончик
            if not game.girl.willing:  
              if random.randint(1,3) == 1: # Дракону не повезло
                game.girl.third 'Осознавая близость неизбежного, [game.girl.name] вырывается изо всех сил и отбрасывет дракона от своего тела!'
                $ game.rape.define_freedom()
                $ game.rape.rage += random.randint(10,20)
              else:
                game.girl.third 'Пленница вырывается изо всех сил, но это не помогает. '
                if 'tough_scale' in game.dragon.modifiers():
                  $ game.rape.rage += random.randint(6,12)
                else:
                  $ game.rape.rage += random.randint(8,14)
                call lb_rape_women from _call_lb_rape_women_13
            else: # Согласна
              game.girl.third '[game.girl.name] изо всех сил стискивает зубы и сжимает кулаки, и когда член дракона разрывает её девственую плеву, не издаёт ни единого стона боли.'  
              call lb_rape_women from _call_lb_rape_women_19
          elif game.rape.size == 2: # Средний дракон 
            if not game.girl.willing:  
              if random.randint(1,10) == 1: # Дракону не повезло
                game.girl.third 'Осознание неизбежного придаёт [game.girl.name] сил. Совершив запредельное усилие, она вырывается из объятий дракона. '
                $ game.rape.define_freedom()
                $ game.rape.rage += random.randint(8,15)
              else:
                game.girl.third 'Пленница вырывается изо всех сил, но увы - дракон слишком велик. '
                call lb_rape_women from _call_lb_rape_women_12
                if 'tough_scale' in game.dragon.modifiers():
                  $ game.rape.rage += random.randint(6,10)
                else:
                  $ game.rape.rage += random.randint(8,12)
            else: # Согласна
              game.girl.third '[game.girl.name] изо всех сил стискивает зубы и сжимает кулаки, но когда член дракона разрывает её девственую плеву, с её уст срывается негромкий стон боли.'  
              call lb_rape_women from _call_lb_rape_women_20
          elif game.rape.size == 3: # Матёрый драконище 
            if not game.girl.willing:  
              game.girl.third 'Пленница вырывается изо всех сил, но никому не дано сбросить с себя объятия гиганта.'
              if 'tough_scale' in game.dragon.modifiers():
                $ game.rape.rage += random.randint(4,8)
              else:
                $ game.rape.rage += random.randint(6,10)
            else: # Согласна
              game.girl.third '[game.girl.name] изо всех сил стискивает зубы и сжимает кулаки. Тщетно: когда член дракона разрывает её девственую плеву, [game.girl.name] истошно орёт от боли и размахивает руками во все стороны.'  
            call lb_rape_women from _call_lb_rape_women_11

        elif game.rape.erection == 2: # Совершить половой акт.
          if game.rape.size == 1: # Миниатюрный дракончик
            if not game.girl.willing:  
              if random.randint(1,3) == 1: # Дракону не повезло
                game.girl.third 'Осознание произошедшего придаёт жертве сил. Пользуясь тем, что дракон полностью поглощён процессом, [game.girl.name] вырывается и отбрасывет дракона от своего тела!'
                $ game.rape.define_freedom()
                $ game.rape.rage += random.randint(10,20)
              else:
                game.girl.third '[game.girl.name] продолжает сопротивляться, мешая дракону сосредоточиться на приятном процессе'
                if 'tough_scale' in game.dragon.modifiers():
                  $ game.rape.rage += random.randint(6,10)
                else:
                  $ game.rape.rage += random.randint(8,12)
                $ game.rape.erection += 1
            else: # Согласна
              game.girl.third '[game.girl.name] сжимает кулаки и громко дышит сквозь сомкнутые зубы - и этим её участи в процессе и ограничивается. Лежит бревно-бревном. Честное слово, лучше бы брыкалась - хоть что-то интересное было бы!'   
              $ game.rape.erection += 1
          elif game.rape.size == 2: # Средний дракон 
            if not game.girl.willing:  
              if random.randint(1,10) == 1: # Дракону не повезло
                game.girl.third 'Осознание произошедшего придаёт [game.girl.name] сил. Пользуясь тем, что насильник полностью поглощён процессом, [game.girl.name] прилагает запредельное усилие и вырывается из объятий дракона. '
                $ game.rape.define_freedom()
                $ game.rape.rage += random.randint(8,15)
              else:
                game.girl.third 'Пленница вырывается изо всех сил, но увы - дракон слишком велик. Все её трепыхания лишь слегка мешают процессу '
                if 'tough_scale' in game.dragon.modifiers():
                  $ game.rape.rage += random.randint(4,8)
                else:
                  $ game.rape.rage += random.randint(6,10)
                $ game.rape.erection += 1
            else: # Согласна
              game.girl.third '[game.girl.name] сжимает кулаки и негромко постанывает сквозь сомкнутые зубы - и этим её участи в процессе и ограничивается. Лежит бревно-бревном. Честное слово, лучше бы брыкалась - хоть что-то интересное было бы!'   
              $ game.rape.erection += 1
          elif game.rape.size == 3: # Матёрый драконище 
            if not game.girl.willing:  
              game.girl.third 'Пленница вырывается изо всех сил, но никому не дано сбросить с себя объятия гиганта. Поглощённый процессом, [game.dragon.name] едва замечает её усилия'
              if 'tough_scale' in game.dragon.modifiers():
                $ game.rape.rage += random.randint(2,6)
              else:
                $ game.rape.rage += random.randint(4,8)
            else: # Согласна
              game.girl.third 'Несмотря на попытки сохранить неподвижность, [game.girl.name] нервно перебирает пальцами и громко стонет от боли. [game.dragon.name] улыбается - такой процесс явно пришёлся ему по вкусу!'   
            $ game.rape.erection += 1  
        elif game.rape.erection == 3: # Кончить.
          if game.rape.size == 1 and random.randint(1,3) == 1 and not game.girl.willing: # Миниатюрный дракончик
            game.girl.third 'Пользуясь тем, что дракон не обращает никакого внимание на её трепыхания, [game.girl.name] резким движением отшвыривает его от себя.'
            call lb_rape_fail from _call_lb_rape_fail_1 
          elif game.rape.size == 2 and random.randint(1,5) == 1 and not game.girl.willing: # Средний дракон 
            game.girl.third 'Пользуясь тем, что дракон не обращает никакого внимание на её трепыхания, [game.girl.name] резким движением вырывается из его объятий.'
            call lb_rape_fail from _call_lb_rape_fail_2 
          elif game.rape.size == 3 and random.randint(1,8) == 1 and not game.girl.willing: # Матёрый драконище 
            game.girl.third 'Пользуясь тем, что дракон не обращает никакого внимание на её трепыхания и слегка ослабил хватку, [game.girl.name] выныривает из объятий колоссального монстра'
            call lb_rape_fail from _call_lb_rape_fail_3
          else:
            game.dragon 'Блажееенство!!!'
            if game.girl.willing:
              if game.rape.size == 1:
                game.girl 'И всего-то? Просто физическое упражнение, даже не особо сложное.' 
                game.girl 'Хотя я с трудом удержалась от того, чтобы не избить тебя вот этими самыми руками'
              elif game.rape.size == 2:
                game.girl 'И всего-то? Сложное физическое упражнение, ничего особенного' 
                game.girl 'Хотя я с трудом удержалась от того, чтобы не избить тебя вот этими самыми руками'
              elif game.rape.size == 3:
                game.girl 'Это было сложно. Ничего, я не боюсь ни испытаний, ни пыток' 
                game.girl 'Руки оставались свободными... хотя вряд ли они бы мне помогли'
            $ game.rape.erection += 1

# Девушка яростно отбивается и шипит  сквозь стиснутые зубы
      if ratio_proud>0.33 and ratio_proud <=0.66: # Девушка яростно отбивается и шипит  сквозь стиснутые зубы
        if game.rape.erection == 0: # Приставить член к влагалищу
          if not game.girl.willing: 
            if game.rape.size == 1: # Миниатюрный дракончик
              if random.randint(1,10) == 1: # Дракону не повезло
                if game.girl.blind:
                  game.girl.third '[game.girl.name] изворачивается и вслепую бьёт ребром ладони по восставшему драконьему члену!'
                else:
                  game.girl.third '[game.girl.name] изворачивается и одним точным ударом бьёт ребром ладони по восставшему драконьему члену!'
                call lb_rape_dragon_penis from _call_lb_rape_dragon_penis_4
              else:
                game.girl.third 'Когда член дракона упирается во влагалище девушки, [game.girl.name] начинает избивать дракона кулаками. Вряд ли она сумеет причинить хоть какой-то вред, хотя... кто знает?'
                if 'tough_scale' in game.dragon.modifiers():
                  $ game.rape.rage += random.randint(6,10)
                else:
                  $ game.rape.rage += random.randint(8,12)
                $ game.rape.erection += 1
            elif game.rape.size == 2: # Средний дракон 
              if random.randint(1,16) == 1: # Дракону не повезло
                if game.girl.blind:
                  game.girl.third '[game.girl.name] изворачивается каким-то хитрым образом и вслепую бьёт ребром ладони по восставшему драконьему члену!'
                else:
                  game.girl.third '[game.girl.name] изворачивается каким-то хитрым образом и одним точным ударом бьёт ребром ладони по восставшему драконьему члену!'
                call lb_rape_dragon_penis from _call_lb_rape_dragon_penis_5
              else:
                game.girl.third 'Когда член дракона упирается во влагалище девушки, [game.girl.name] начинает избивать дракона кулаками. Повредить-то оно не повредит, но раздражает и отвлекает, зараза!'
                if 'tough_scale' in game.dragon.modifiers():
                  $ game.rape.rage += random.randint(4,8)
                else:
                  $ game.rape.rage += random.randint(6,10)
                $ game.rape.erection += 1
            elif game.rape.size == 3: # Матёрый драконище 
              if random.randint(1,20) == 1: # Дракону не повезло
                if game.girl.blind:
                  game.girl.third '[game.girl.name] изворачивается каким-то немыслимым образом и вслепую бьёт ребром ладони по восставшему драконьему члену!'
                else:
                  game.girl.third '[game.girl.name] изворачивается каким-то немыслимым образом и одним точным ударом бьёт ребром ладони по восставшему драконьему члену!'
                call lb_rape_dragon_penis from _call_lb_rape_dragon_penis_6
              else:
                game.girl.third 'Когда член дракона упирается во влагалище девушки, [game.girl.name] начинает избивать исполинскую тушу кулаками. [game.dragon.name] едва ощущает сопротивление пленницы, но всё равно: такое поведение слегка...   раздражает.'
                if 'tough_scale' in game.dragon.modifiers():
                  $ game.rape.rage += random.randint(0,4)
                else:
                  $ game.rape.rage += random.randint(2,6)
                $ game.rape.erection += 1
          else: # Согласна
            game.girl.third '[game.girl.name] молитвенно складывает руки и начинает истово молиться.'   
            $ game.rape.erection += 1  

        elif game.rape.erection == 1: # Разорвать девственную плеву.
          if game.rape.size == 1: # Миниатюрный дракончик
            if not game.girl.willing: 
              if random.randint(1,10) == 1: # Дракону не повезло
                game.girl.third 'Осознавая близость неизбежного, [game.girl.name] вырывается изо всех сил и отбрасывет дракона от своего тела!'
                $ game.rape.define_freedom()
                $ game.rape.rage += random.randint(10,20)
              else:
                game.girl.third 'Пленница пытается вырваться, но это не помогает. '
                call lb_rape_women from _call_lb_rape_women_10
                if 'tough_scale' in game.dragon.modifiers():
                  $ game.rape.rage += random.randint(4,8)
                else:
                  $ game.rape.rage += random.randint(6,10)
            else: # Согласна
              game.girl.third 'Короткий стон прерывает молитву, но [game.girl.name] быстро приходит в себя, вновь прижимает ладони друг к другу и начинает молиться ещё истовее. '  
              call lb_rape_women from _call_lb_rape_women_21
          elif game.rape.size == 2: # Средний дракон 
            if not game.girl.willing: 
              game.girl.third 'Пленница пытается вырваться, но увы - дракон слишком велик.'
              if 'tough_scale' in game.dragon.modifiers():
                $ game.rape.rage += random.randint(2,6)
              else:
                $ game.rape.rage += random.randint(4,8)
            else: # Согласна
              game.girl.third 'Молитва заканчивается громким стоном. Впрочем, [game.girl.name] всё же приходит в себя, вновь прижимает ладони друг к другу и начинает молиться ещё истовее. '  
            call lb_rape_women from _call_lb_rape_women_9
          elif game.rape.size == 3: # Матёрый драконище 
            if not game.girl.willing: 
              game.girl.third 'Пленница пытается вырваться, но никому не дано сбросить с себя объятия гиганта.'
              if 'tough_scale' in game.dragon.modifiers():
                $ game.rape.rage += random.randint(0,4)
              else:
                $ game.rape.rage += random.randint(2,6)
            else: # Согласна
              game.girl.third 'Молитва заканчивается криком боли. [game.girl.name] лихорадочно размахивает руками и пытается прийти в себя. Кажется, с молитвами на сегодня всё. '  
            call lb_rape_women from _call_lb_rape_women_8

        elif game.rape.erection == 2: # Совершить половой акт.
          if game.rape.size == 1: # Миниатюрный дракончик
            if not game.girl.willing: 
              if random.randint(1,10) == 1: # Дракону не повезло
                game.girl.third 'Осознание произошедшего придаёт жертве сил. Пользуясь тем, что дракон полностью поглощён процессом, [game.girl.name] вырывается и отбрасывет дракона от своего тела!'
                $ game.rape.define_freedom()
                $ game.rape.rage += random.randint(10,20)
              else:
                game.girl.third '[game.girl.name] продолжает сопротивляться,  но уже без прежней ярости. Похоже, произошедшее сломило её, и пленница смирилась со своей участью.'
                if 'tough_scale' in game.dragon.modifiers():
                  $ game.rape.rage += random.randint(2,6)
                else:
                  $ game.rape.rage += random.randint(4,8)
                $ game.rape.erection += 1
            else: # Согласна
              game.girl.third '[game.girl.name] продолжает молиться, то и дело постанывая от боли. Она сосредатачивается на соединённых вместе ладонях, пытаясь отрешиться от того, что происходит там, внизу.' 
              $ game.rape.erection += 1
          elif game.rape.size == 2: # Средний дракон 
            if not game.girl.willing: 
              game.girl.third '[game.girl.name] продолжает сопротивляться, но тщетно: дракон слишком велик. Похоже, произошедшее сломило её, и пленница смирилась со своей участью. '
              if 'tough_scale' in game.dragon.modifiers():
                $ game.rape.rage += random.randint(0,2)
              else:
                $ game.rape.rage += random.randint(2,4)
            else: # Согласна
              game.girl.third 'Молитва [game.girl.name_r] то и дело прерывается криками боли. Она сосредатачивается на соединённых вместе ладонях, пытаясь отрешиться от того, что происходит там, внизу. Тщетно.' 
            $ game.rape.erection += 1
          elif game.rape.size == 3: # Матёрый драконище 
            if not game.girl.willing: 
              game.girl.third '[game.girl.name] продолжает сопротивлятья, но никому не дано сбросить с себя объятия гиганта. Тщетность усилий очевидна; похоже, произошедшее сломило её, и пленница смирилась со своей участью.'
              if 'tough_scale' in game.dragon.modifiers():
                $ game.rape.rage += random.randint(0,1)
              else:
                $ game.rape.rage += random.randint(1,2)
            else: # Согласна
              game.girl.third 'Отдельные слова молитв тонут в криках боли. [game.girl.name] размахивает руками во все стороны, пытаясь хоть как-то облегчить эту пытку.' 
            $ game.rape.erection += 1  

        elif game.rape.erection == 3: # Кончить.
          if game.rape.size == 1 and random.randint(1, 10)>5 and not game.girl.willing: # Миниатюрный дракончик
            game.girl.third 'Пользуясь тем, что дракон не обращает никакого внимание на её трепыхания, [game.girl.name] резким движением отшвыривает его от себя. Смирение было наигранным!'
            call lb_rape_fail from _call_lb_rape_fail_4 
          elif game.rape.size == 2 and random.randint(1, 10)>6 and not game.girl.willing: # Средний дракон 
            game.girl.third 'Пользуясь тем, что дракон не обращает никакого внимание на её жалкие трепыхания, [game.girl.name] резким движением вырывается из его объятий. Смирение было наигранным!'
            call lb_rape_fail from _call_lb_rape_fail_5 
          elif game.rape.size == 3 and random.randint(1, 10)>7 and not game.girl.willing: # Матёрый драконище 
            game.girl.third 'Пользуясь тем, что дракон не обращает никакого внимание на её жалкие трепыхания и слегка ославбил хватку, [game.girl.name] выныривает из объятий колоссального монстра. Смирение было наигранным!'
            call lb_rape_fail from _call_lb_rape_fail_6
          else:
            game.dragon 'Блажееенство!!!'
            if game.girl.willing:
              if game.rape.size == 1:
                game.girl 'Да простит мой грех Небесный Отец. К счастью, это оказалось легче, чем я боялась.' 
                game.girl 'Спасибо, что оставил мне руки свободными'
              elif game.rape.size == 2:
                game.girl 'Да простит мой грех Небесный Отец. Это было ужасно' 
                game.girl 'Спасибо, что хоть руки оставил свободными'
              elif game.rape.size == 3:
                game.girl 'Небесный Отец... наказывает меня... за грехи мои... Если бы я знала заранее, то сопротивлялась бы изо всех сил.' 
            $ game.rape.erection += 1

# Девушка заламывает руки и молит о пощаде
      elif ratio_proud>0 and ratio_proud <=0.33:  # Заламывает руки и умоляет прекратить
        if game.rape.erection == 0: # Приставить член к влагалищу
          if game.rape.size == 1 and random.randint(1,10) == 10 and not game.girl.willing: # Миниатюрный дракончик
            game.girl.third 'Пленнице удаётся вырваться из объятий дракона'
            'Эх, руки ей тоже надо было зафиксировать!'
            $ game.rape.define_freedom()
            $ game.rape.rage += random.randint(4,8)
          else:
            if not game.girl.willing:
              game.girl.third '[game.girl.name] вяло отбивается и умоляет дракона о милосердии'
              if 'tough_scale' in game.dragon.modifiers():
                $ game.rape.rage += random.randint(0,4)
              else:
                $ game.rape.rage += random.randint(2,6)
            else: # Согласна
              if game.girl.type == 'afrodita':
                game.girl.third '[game.girl.name] ласкает руками член дракона. Кажется, богиня любви стремится доставить ему как можно больше удовольствия.'
              else:
                game.girl.third '[game.girl.name], замирая от какого-то необъяснимого чувства, ласкает руками член дракона.' 
            $ game.rape.erection += 1

        elif game.rape.erection == 1: # Разорвать девственную плеву.
          game.girl.third 'Пленница коротко, но сладко вскрикивает от боли.'
          call lb_rape_women from _call_lb_rape_women_7
          if 'tough_scale' in game.dragon.modifiers():
            $ game.rape.rage += random.randint(0,3)
          else:
            $ game.rape.rage += random.randint(1,4)

        elif game.rape.erection == 2: # Совершить половой акт.
          if game.rape.pussy: # Лоно не повреждено
            game.girl.third 'Похоже, [game.girl.name] входит во вкус. Положив руки  на плечи ящера, она задаёт ритм, активно подмахивая своими бёдрами. С её губ всё чаще и чаще срываются стоны наслаждения, смешивающиеся с порыкиваниями дракона. Происходящее нравится ящеру всё больше и больше!'
          else:
            game.girl.third 'Повреждения, нанесённые драконом при ухаживании, слишком серьёзны. Каждое движение дракона отдаётся жгучей болью в женском местечке, и [game.girl.name] потрясённо понимает, что ей... это... нравится! Страдание причудливо смешивается с наслаждением, и [game.girl.name] жаждет больше - и того, и другого.'
            game.girl 'Быстрее... глубже... сильнее... Порви меня!!!'
          $ game.rape.erection += 1 

        elif game.rape.erection == 3: # Кончить.
          game.girl.third 'Ритм ускоряется, [game.girl.name] двигается всё энергичнее, всё страстнее, и когда драконье семя заполняет её лоно, издаёт долгий крик удовольствия '
          game.dragon 'Блажееенство!!!'
          if game.rape.pussy: # Лоно не повреждено
            if game.girl.blind:
              game.girl.third '[game.girl.name] счастливо улыбается куда-то в пустоту. Сейчас ей кажется, что потеря зрения - крошечная плата за пережитоте блаженство. [game.girl.name] на седьмом небе от счастья и мечтает о повторном заходе!'
            else:
              if game.girl.type == 'afrodita':
                game.girl.third '[game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Лицо её расплывается в радостной, счастливой улыбке. Кажется, произошедший позор её нимало не беспокоит - да она и позором это не считает! Что бы ни задумала богиня любви - её план только что блистательно осуществился.'
              elif game.girl.type == 'danu':
                game.girl.third '[game.girl.name] смотрит на дракона со счастливой улыбкой. Сейчас неважно, что она - богиня, что её только что изнасиловал самый страшный враг альвов. После всего пережитого [game.girl.name] отказывается от своего народа и становится верной игрушкой дракона!'
              else:
                game.girl.third '[game.girl.name] смотрит на дракона со счастливой улыбкой. Сейчас неважно, кем она была раньше, что было между ними до того. [game.girl.name] на седьмом небе от счастья и мечтает о повторном заходе!'
          else:
            if game.girl.nature == 'proud':
              game.girl.third '[game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Низ живота пульсирует жгучей болью, и эта боль - самое классное, что было в её жизни. Жаль, что успокоившись, она возненавидит своего мучителя.\n Поэтому прямо сейчас ей хочется одного - умереть. Умереть счастливой.'
            elif game.girl.nature == 'innocent':
              if game.girl.type == 'danu':
                game.girl.third 'Богиня [game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Низ живота пульсирует жгучей болью, и эта боль - самое лучшее, что было в её божественно-долгой жизни. \n Похоже, после пережитого богиня Дану отказается от своего народа и становится верной игрушкой дракона'
              elif game.girl.type == 'afrodirta':
                game.girl.third '[game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Низ живота пульсирует жгучей болью, но эта боль - ничто по сравнению с осознанием выполненого долга. Безумный план [game.girl.name_r] только что блистательно осуществился!'
              else:  
                game.girl.third '[game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Низ живота пульсирует жгучей болью, и эта боль - самое классное, что было в её жизни. Жаль, что успокоившись, она придёт в ужас от произошедшего.\n Поэтому прямо сейчас ей хочется одного - умереть. Умереть счастливой.'
            elif game.girl.nature == 'lust':
              if game.girl.type == 'afrodita':
                game.girl.third '[game.girl.name] смотрит на дракона со счастливой улыбкой. Кажется, богиню нисколько не беспокоит та боль, что причинил ей дракон.'
              else:
                game.girl.third '[game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Низ живота пульсирует жгучей болью, и эта боль - самое классное, что было в её жизни. Даже успокоившись, она никогда не забудет первой близости со своим мучителем. Вот только такое никогда не повторится.\n Поэтому прямо сейчас ей хочется одного - умереть. Умереть счастливой.'
          $ game.rape.erection += 1
          if game.girl.type == 'afrodita':
            $ game.history = historical( name='afrodita_win',end_year=game.year+1,desc=None,image=None)
            $ game.history_mod.append(game.history)
          elif game.girl.type == 'danu':
            $ game.history = historical( name='danu_broken',end_year=game.year+1,desc=None,image=None)
            $ game.history_mod.append(game.history)
 
# Полностью сломлена
      elif ratio_proud==0:  
        call lb_rape_broken from _call_lb_rape_broken_2 

# Тело свободно, руки в захвате
    elif game.rape.body and not game.rape.arms:   # Руки у девчонки свободны
      if ratio_proud>0.66: # Честь превыше жизни
        if game.rape.erection == 0: # Приставить член к влагалищу
          if game.rape.size == 1: # Миниатюрный дракончик
            if not game.girl.willing:
              if random.randint(1, 10)>2: # Дракону не повезло
                if game.girl.blind:
                  game.girl.third '[game.girl.name] слепо пинается во все стороны и случайно попадает по восставшему драконьему члену!'
                else:
                  game.girl.third '[game.girl.name] изо всей силы пинает ногой по восставшему драконьему члену!'
                call lb_rape_dragon_penis from _call_lb_rape_dragon_penis_7
              else:
                if game.girl.blind:
                  game.girl.third '[game.girl.name] пытается пнуть ногой по восставшему драконьему члену, но для слепой эта задача не под силу.'
                else:
                  game.girl.third '[game.girl.name] пытается пнуть ногой по восставшему драконьему члену, но промахивается.'
                $ game.rape.rage += random.randint(12,16)
                $ game.rape.erection += 1
            else: # Согласна
              game.girl.third 'Когда член дракона упирается во влагалище девушки, [game.girl.name] отворачивается, прикусывает губу и передёргивается всем телом. Похоже, маленький рост дракона искушает её ложной надеждой на успех - но [game.girl.name] всё-таки удерживается от сопротивления.'   
              $ game.rape.erection += 1
          elif game.rape.size == 2: # Средний дракон 
            if not game.girl.willing:
              if random.randint(1, 10)>3: # Дракону не повезло
                if game.girl.blind:
                  game.girl.third '[game.girl.name] слепо пинается во все стороны совершенно случайно попадает по восставшему драконьему члену!'
                else:
                  game.girl.third '[game.girl.name] метко пинает ногой по восставшему драконьему члену!'
                call lb_rape_dragon_penis from _call_lb_rape_dragon_penis_8
              else:
                if game.girl.blind:
                  game.girl.third '[game.girl.name] пытается пнуть ногой по восставшему драконьему члену, но для слепой эта задача не под силу.'
                else:
                  game.girl.third '[game.girl.name] пытается пнуть ногой по восставшему драконьему члену, но немного промахивается.'
                $ game.rape.rage += random.randint(10,14)
                $ game.rape.erection += 1
            else: # Согласна
              game.girl.third 'Когда член дракона упирается во влагалище девушки, [game.girl.name] отворачивается, прикусывает губу и передёргивается всем телом. Похоже, она пытается не начать пинаться.'   
              $ game.rape.erection += 1
          elif game.rape.size == 3: # Матёрый драконище 
            if not game.girl.willing:
              if random.randint(1, 10)>4: # Дракону не повезло
                if game.girl.blind:
                  game.girl.third '[game.girl.name] слепо пинается во все стороны совершенно случайно попадает по восставшему драконьему члену! \n\nИногда и не такие совпадения бывают!'
                else:
                  game.girl.third '[game.girl.name] изворачивается каким-то немыслимым образом и метко пинает ногой по восставшему драконьему члену!'
                call lb_rape_dragon_penis from _call_lb_rape_dragon_penis_9
              else:
                if game.girl.blind:
                  game.girl.third '[game.girl.name] пытается пнуть ногой по восставшему драконьему члену, но для слепой эта задача не под силу.'
                else:
                  game.girl.third '[game.girl.name] изворачивается каким-то немыслимым образом и пытается пнуть ногой по восставшему драконьему члену, но немного промахивается.'
                $ game.rape.rage += random.randint(8,12)
                $ game.rape.erection += 1
            else: # Согласна
              game.girl.third 'Когда член дракона упирается во влагалище девушки, [game.girl.name] отворачивается, прикусывает губу и передёргивается всем телом. Впрочем, даже если бы она начала сопротивляться - это всё равно не помогло бы. Хотя.. меткий пинок... нет. Плохая идея. '   
              $ game.rape.erection += 1

        elif game.rape.erection == 1: # Разорвать девственную плеву.
          if game.rape.size == 1: # Миниатюрный дракончик
            if not game.girl.willing:  
              if random.randint(1,3) == 1: # Дракону не повезло
                game.girl.third 'Осознавая близость неизбежного, [game.girl.name] бьётся изо всех сил и вырывает свои руки из лап дракона!'
                $ game.rape.define_freedom()
                $ game.rape.rage += random.randint(10,20)
              else:
                game.girl.third 'Пленница вырывается изо всех сил, но [game.dragon.name] держит её за руки слишком крепко.'
                call lb_rape_women from _call_lb_rape_women_6
                $ game.rape.rage += random.randint(8,14)
            else: # Согласна
              game.girl.third '[game.girl.name] изо всех сил стискивает зубы, и когда член дракона разрывает её девственую плеву, не издаёт ни единого стона боли.'  
              call lb_rape_women from _call_lb_rape_women_24
          elif game.rape.size == 2: # Средний дракон
            if not game.girl.willing:    
              if random.randint(1,10) == 1: # Дракону не повезло
                game.girl.third 'Осознание неизбежного придаёт [game.girl.name] сил. Совершив запредельное усилие, она вырывает свои руки из лап дракона. '
                $ game.rape.define_freedom()
                $ game.rape.rage += random.randint(8,15)
              else:
                game.girl.third 'Пленница вырывается изо всех сил, но увы - дракон слишком велик.'
                call lb_rape_women from _call_lb_rape_women_5
                $ game.rape.rage += random.randint(8,12)
            else: # Согласна
              game.girl.third '[game.girl.name] изо всех сил стискивает зубы, но когда член дракона разрывает её девственую плеву, с её уст срывается негромкий стон боли.'  
              call lb_rape_women from _call_lb_rape_women_25
          elif game.rape.size == 3: # Матёрый драконище 
            if not game.girl.willing:  
              game.girl.third 'Пленница вырывается изо всех сил, но никому не дано разжать лапы гиганта.'
              $ game.rape.rage += random.randint(6,10)
            else: # Согласна
              game.girl.third '[game.girl.name] изо всех сил стискивает зубы. Тщетно: когда член дракона разрывает её девственую плеву, [game.girl.name] истошно орёт от боли и бессильно дрыгает ногами.'  
            call lb_rape_women from _call_lb_rape_women_18

        elif game.rape.erection == 2: # Совершить половой акт.
          if game.rape.size == 1: # Миниатюрный дракончик
            if not game.girl.willing:  
              if random.randint(1,3) == 1: # Дракону не повезло
                game.girl.third 'Осознание произошедшего придаёт жертве сил. Пользуясь тем, что дракон полностью поглощён процессом, [game.girl.name] дёргается и вырывает свои руки из лап насильника!'
                $ game.rape.define_freedom()
                $ game.rape.rage += random.randint(10,20)
              else:
                game.girl.third '[game.girl.name] продолжает брыкаться, мешая дракону сосредоточиться на приятном процессе'
                $ game.rape.rage += random.randint(8,12)
                $ game.rape.erection += 1
            else: # Согласна
              game.girl.third '[game.girl.name] громко дышит сквозь сомкнутые зубы - и этим её участи в процессе и ограничивается. Лежит бревно-бревном, даже не дёргается. Честное слово, лучше бы брыкалась - хоть что-то интересное было бы!'   
              $ game.rape.erection += 1
          elif game.rape.size == 2: # Средний дракон 
            if not game.girl.willing:
              if random.randint(1,10) == 1: # Дракону не повезло
                game.girl.third 'Осознание произошедшего придаёт [game.girl.name] сил. Пользуясь тем, что насильник полностью поглощён процессом, [game.girl.name] прилагает запредельное усилие и вырывает свои руки из лап дракона. '
                $ game.rape.define_freedom()
                $ game.rape.rage += random.randint(8,15)
              else:
                game.girl.third 'Пленница вырывается изо всех сил, но увы - дракон слишком велик. Все её трепыхания лишь слегка мешают процессу '
                $ game.rape.rage += random.randint(6,10)
                $ game.rape.erection += 1
            else: # Согласна
              game.girl.third '[game.girl.name] негромко постанывает сквозь сомкнутые зубы - и этим её участи в процессе и ограничивается. Лежит бревно-бревном и не дёргается. Честное слово, лучше бы брыкалась - хоть что-то интересное было бы!'   
              $ game.rape.erection += 1
          elif game.rape.size == 3: # Матёрый драконище 
            if not game.girl.willing:
              game.girl.third 'Пленница вырывается изо всех сил, но никому не дано разжать лапы гиганта. Поглощённый процессом, [game.dragon.name] едва замечает её усилия'
              $ game.rape.rage += random.randint(4,8)
            else: # Согласна
              game.girl.third 'Несмотря на попытки сохранить неподвижность, [game.girl.name] дрыгает ногами и громко стонет от боли. [game.dragon.name] улыбается - такой процесс явно пришёлся ему по вкусу!'
            $ game.rape.erection += 1  

        elif game.rape.erection == 3: # Кончить.
          if game.rape.size == 1 and random.randint(1, 10)>5 and game.girl.willing: # Миниатюрный дракончик
            game.girl.third 'Пользуясь тем, что дракон не обращает никакого внимание на её трепыхания, [game.girl.name] резким движением вырывает руки из захвата и отшвыривает его от себя.'
            call lb_rape_fail from _call_lb_rape_fail_7 
          elif game.rape.size == 2 and random.randint(1, 10)>6 and game.girl.willing: # Средний дракон 
            game.girl.third 'Пользуясь тем, что дракон не обращает никакого внимание на её трепыхания, [game.girl.name] резким движением вырывает руки из захвата.'
            call lb_rape_fail from _call_lb_rape_fail_8 
          elif game.rape.size == 3 and random.randint(1, 10)>7 and game.girl.willing: # Матёрый драконище 
            game.girl.third 'Пользуясь тем, что дракон не обращает никакого внимание на её трепыхания и слегка ославбил хватку, [game.girl.name] аккуратно вынимает руки из лап колоссального монстра'
            call lb_rape_fail from _call_lb_rape_fail_9
          else:
            game.dragon 'Блажееенство!!!'
            if game.girl.willing:
              if game.rape.size == 1:
                game.girl 'И всего-то? Просто физическое упражнение, даже не особо сложное.' 
                game.girl 'Хотя я с трудом удержалась от того, чтобы не пнуть тебя... да-да, прямо туда'
              elif game.rape.size == 2:
                game.girl 'И всего-то? Сложное физическое упражнение, ничего особенного' 
                game.girl 'Хотя я с трудом удержалась от того, чтобы не пнуть тебя... да-да, прямо туда'
              elif game.rape.size == 3:
                game.girl 'Это было сложно. Ничего, я не боюсь ни испытаний, ни пыток' 
                game.girl 'Ноги оставались свободными... как же мне хотелось пнуть тебя прямо туда!'
            $ game.rape.erection += 1

# Девушка яростно отбивается и шипит  сквозь стиснутые зубы
      if ratio_proud>0.33 and ratio_proud <=0.66: # Девушка яростно отбивается и шипит  сквозь стиснутые зубы
        if game.rape.erection == 0: # Приставить член к влагалищу
          if not game.girl.willing:
            if game.rape.size == 1: # Миниатюрный дракончик
              if random.randint(1,3) == 1: # Дракону не повезло
                if game.girl.blind:
                  game.girl.third '[game.girl.name] орёт от ужаса и слепо пинается во все стороны, случайно попадая по восставшему драконьему члену!'
                else:
                  game.girl.third '[game.girl.name] орёт от ужаса и пинает ногой по восставшему драконьему члену!'
                call lb_rape_dragon_penis from _call_lb_rape_dragon_penis_10
              else:
                if game.girl.blind:
                  game.girl.third 'Услышав возбуждённое, учащённое дыхание дракона, [game.girl.name] орёт от ужаса и слепо пинается во все стороны. '
                else:                
                  game.girl.third 'Увидев драконий член, [game.girl.name] орёт от ужаса и пытается пнуть дракона ногой в промежность. Безуспешно. '
                $ game.rape.rage += random.randint(8,15)
                $ game.rape.erection += 1
            elif game.rape.size == 2: # Средний дракон 
              if random.randint(1,5) == 1: # Дракону не повезло
                if game.girl.blind:
                  game.girl.third '[game.girl.name] орёт от ужаса и слепо пинается во все стороны, случайно попадая по восставшему драконьему члену!'
                else:
                  game.girl.third '[game.girl.name] орёт от ужаса и не глядя пинает ногой по восставшему драконьему члену!'
                call lb_rape_dragon_penis from _call_lb_rape_dragon_penis_11
              else:
                if game.girl.blind:
                  game.girl.third 'Услышав возбуждённое, учащённое дыхание дракона, [game.girl.name] орёт от ужаса и начинает пинаться. К счатью, она не попадает ногой по самому сокровенному!'
                else:    
                  game.girl.third 'Увидив драконий член, [game.girl.name] орёт от ужаса и начинает пинаться. К счатью, она не попадает ногой по самому сокровенному!'
                $ game.rape.rage += random.randint(6,10)
                $ game.rape.erection += 1
            elif game.rape.size == 3: # Матёрый драконище 
              if random.randint(1,8) == 1: # Дракону не повезло
                if game.girl.blind:
                  game.girl.third '[game.girl.name] орёт от ужаса и слепо пинается во все стороны, случайно попадая по восставшему драконьему члену!'
                else:
                  game.girl.third '[game.girl.name] орёт от ужаса и не глядя начинает пинать ногами во все стороны, случайно попадая по восставшему драконьему члену!'
                call lb_rape_dragon_penis from _call_lb_rape_dragon_penis_12
              else:
                if game.girl.blind:
                  game.girl.third 'Услышав возбуждённое, учащённое дыхание дракона, [game.girl.name] орёт от ужаса и начинает пинаться. К счатью, [game.dragon.name] велик, и попасть по самому сокровенному она может разве что случайно!'
                else:    
                  game.girl.third 'Увидив драконий член, [game.girl.name] орёт от ужаса и начинает пинаться. К счатью, [game.dragon.name] велик, и попасть по самому сокровенному она может разве что случайно! '
                $ game.rape.rage += random.randint(2,6)
                $ game.rape.erection += 1
          else: # Согласна
            game.girl.third '[game.girl.name] передёргивается всем телом, закрывает глаза и начинает истово молиться.'   
            $ game.rape.erection += 1 

        elif game.rape.erection == 1: # Разорвать девственную плеву.
          if game.rape.size == 1: # Миниатюрный дракончик
            if not game.girl.willing:
              if random.randint(1,10) == 1: # Дракону не повезло
                game.girl.third 'Осознавая близость неизбежного, [game.girl.name] вырывается изо всех сил и освобождает свои руки!'
                $ game.rape.define_freedom()
                $ game.rape.rage += random.randint(10,20)
              else:
                game.girl.third 'Пленница пытается вырваться, но это не помогает.'
                call lb_rape_women from _call_lb_rape_women_4
                $ game.rape.rage += random.randint(6,10)
            else: # Согласна
              game.girl.third 'Короткий стон прерывает молитву, но [game.girl.name] быстро приходит в себя, содрогается всем телом и начинает молиться ещё истовее. '  
              call lb_rape_women from _call_lb_rape_women_26

          elif game.rape.size == 2: # Средний дракон 
            if not game.girl.willing:
              game.girl.third 'Пленница пытается вырваться, но увы - дракон слишком велик.'
              $ game.rape.rage += random.randint(4,8)
            else: # Согласна
              game.girl.third 'Молитва заканчивается громким стоном. Впрочем, [game.girl.name] всё же приходит в себя, содрагается все телом и начинает молиться ещё истовее. '  
            call lb_rape_women from _call_lb_rape_women_3
          elif game.rape.size == 3: # Матёрый драконище 
            if not game.girl.willing:
              game.girl.third 'Пленница пытается вырваться, но никому не дано вырвать свои руки из лап гиганта.'
              $ game.rape.rage += random.randint(2,6)
            else: # Согласна
              game.girl.third 'Молитва заканчивается криком боли. [game.girl.name] дрожит крупной дрожью и пытается прийти в себя. Кажется, с молитвами на сегодня всё. ' 
            call lb_rape_women from _call_lb_rape_women_2

        elif game.rape.erection == 2: # Совершить половой акт.
          if game.rape.size == 1: # Миниатюрный дракончик
            if not game.girl.willing: 
              if random.randint(1,10) == 1: # Дракону не повезло
                game.girl.third 'Осознание произошедшего придаёт жертве сил. Пользуясь тем, что дракон полностью поглощён процессом, [game.girl.name] брыкается и вырывает свои руки из лап дракона!'
                $ game.rape.define_freedom()
                $ game.rape.rage += random.randint(10,20)
              else:
                game.girl.third '[game.girl.name] продолжает сопротивляться, но уже без прежней ярости. Похоже, произошедшее сломило её, и пленница смирилась со своей участью.'
                $ game.rape.rage += random.randint(4,8)
                $ game.rape.erection += 1
            else: # Согласна
              game.girl.third '[game.girl.name] продолжает молиться, то и дело постанывая от боли. Её глаза закрыты, она пытается отрешиться от того, что происходит там, внизу.' 
              $ game.rape.erection += 1
          elif game.rape.size == 2: # Средний дракон 
            if not game.girl.willing: 
              game.girl.third '[game.girl.name] продолжает сопротивляться, но тщетно: дракон слишком велик. Похоже, произошедшее сломило её, и пленница смирилась со своей участью. '
              $ game.rape.rage += random.randint(2,4)
            else: # Согласна
              game.girl.third 'Молитва [game.girl.name_r] то и дело прерывается криками боли. Её глаза закрыты, она пытается отрешиться от того, что происходит там, внизу. Тщетно.' 
            $ game.rape.erection += 1
          elif game.rape.size == 3: # Матёрый драконище
            if not game.girl.willing:   
              game.girl.third '[game.girl.name] продолжает сопротивлятья, но никому не дано вырваться из хватки гиганта. Тщетность усилий очевидна; похоже, произошедшее сломило её, и пленница смирилась со своей участью.'
              $ game.rape.rage += random.randint(1,2)
            else: # Согласна
              game.girl.third 'Отдельные слова молитв тонут в криках боли. Глаза [game.girl.name_r] крепко зажмурены, она дёргается всем телом, пытаясь хоть как-то облегчить эту пытку.' 
            $ game.rape.erection += 1  

        elif game.rape.erection == 3: # Кончить.
          if game.rape.size == 1 and random.randint(1,3) == 1 and not game.girl.willing: # Миниатюрный дракончик
            game.girl.third 'Пользуясь тем, что дракон не обращает никакого внимание на её трепыхания, [game.girl.name] резким движением вырывает руки из его лап. Смирение было наигранным!'
            call lb_rape_fail from _call_lb_rape_fail_10 
          elif game.rape.size == 2 and random.randint(1,5) == 1 and not game.girl.willing: # Средний дракон 
            game.girl.third 'Пользуясь тем, что дракон не обращает никакого внимание на её жалкие трепыхания, [game.girl.name] резким движением вырывает руки из его лап. Смирение было наигранным!'
            call lb_rape_fail from _call_lb_rape_fail_11 
          elif game.rape.size == 3 and random.randint(1,8) == 1 and not game.girl.willing: # Матёрый драконище 
            game.girl.third 'Пользуясь тем, что дракон не обращает никакого внимание на её жалкие трепыхания и слегка ославбил хватку, [game.girl.name] аккуратно вынимает руки из лап колоссального монстра. Смирение было наигранным!'
            call lb_rape_fail from _call_lb_rape_fail_12
          else:
            game.dragon 'Блажееенство!!!'
            if game.girl.willing:
              if game.rape.size == 1:
                game.girl 'Да простит мой грех Небесный Отец. К счастью, это оказалось легче, чем я боялась.' 
              elif game.rape.size == 2:
                game.girl 'Да простит мой грех Небесный Отец. Это было ужасно' 
              elif game.rape.size == 3:
                game.girl 'Небесный Отец... наказывает меня... за грехи мои... Если бы я знала заранее, то пиналась бы изо всех сил.' 
            $ game.rape.erection += 1

# Девушка заламывает руки и молит о пощаде
      elif ratio_proud>0 and ratio_proud <=0.33:  # Заламывает руки и умоляет прекратить
        if game.rape.erection == 0: # Приставить член к влагалищу
          if game.rape.size == 1 and random.randint(1,6) == 10 and not game.girl.willing: # Миниатюрный дракончик
            game.girl.third 'Пленнице удаётся вырвать руки из лап дракона'
            'Эх, тело ей тоже надо было зафиксировать!'
            $ game.rape.define_freedom()
            $ game.rape.rage += random.randint(8,15)
          else:
            if not game.girl.willing:
              game.girl.third '[game.girl.name] вяло пинается и умоляет дракона о милосердии'
              $ game.rape.rage += random.randint(2,6)
            else: # Согласна
              game.girl.third '[game.girl.name], замирая от какого-то необъяснимого чувства, выгибается в сторону дракона.' 
            $ game.rape.erection += 1

        elif game.rape.erection == 1: # Разорвать девственную плеву.
          game.girl.third 'Пленница дёргается всем телом и коротко вскрикивает от боли.'
          call lb_rape_women from _call_lb_rape_women_1
          $ game.rape.rage += random.randint(1,4)
          $ game.rape.erection += 1
          $ game.girl.virgin = False

        elif game.rape.erection == 2: # Совершить половой акт.
          if game.rape.pussy:
            game.girl.third 'Похоже, [game.girl.name] входит во вкус. Обхватив ногами тело ящера, она задаёт ритм, активно подмахивая своими бёдрами. С её губ всё чаще и чаще срываются стоны наслаждения, смешивающиеся с порыкиваниями дракона. Происходящее нравится ящеру всё больше и больше!'
          else:
            game.girl.third 'Повреждения, нанесённые драконом при ухаживании, слишком серьёзны. Каждое движение дракона отдаётся жгучей болью в женском местечке, и [game.girl.name] потрясённо понимает, что ей... это... нравится! Страдание причудливо смешивается с наслаждением, и [game.girl.name] жаждет больше - и того, и другого.'
            game.girl 'Быстрее... глубже... сильнее... Порви меня!!!'
          $ game.rape.erection += 1 

        elif game.rape.erection == 3: # Кончить.
          game.girl.third 'Ритм ускоряется, [game.girl.name] двигается всё энергичнее, всё страстнее, и когда драконье семя заполняет её лоно, издаёт долгий крик удовольствия '
          game.dragon 'Блажееенство!!!'
          if game.rape.pussy:
            if game.girl.blind:
              game.girl.third '[game.girl.name] счастливо улыбается куда-то в пустоту. Сейчас ей кажется, что потеря зрения - крошечная плата за пережитоте блаженство. [game.girl.name] на седьмом небе от счастья и мечтает о повторном заходе!'
            else:
              if game.girl.type == 'afrodita':
                game.girl.third '[game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Лицо её расплывается в радостной, счастливой улыбке. Кажется, произошедший позор её нимало не беспокоит - да она и позором это не считает! Что бы ни задумала богиня любви - её план только что блистательно осуществился.'
              else:
                game.girl.third '[game.girl.name] смотрит на дракона со счастливой улыбкой. Сейчас неважно, кем она была раньше, что было между ними до того. [game.girl.name] на седьмом небе от счастья и мечтает о повторном заходе!'
          else:
            if game.girl.nature == 'proud':
              game.girl.third '[game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Низ живота пульсирует жгучей болью, и эта боль - самое классное, что было в её жизни. Жаль, что успокоившись, она возненавидит своего мучителя.\n Поэтому прямо сейчас ей хочется одного - умереть. Умереть счастливой.'
            elif game.girl.nature == 'innocent':
              if game.girl.type == 'danu':
                game.girl.third 'Богиня [game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Низ живота пульсирует жгучей болью, и эта боль - самое лучшее, что было в её жизни. \n Похоже, после пережитого богиня Дану решила отказаться от своего народа и стать верной игрушкой дракона'
                $ game.history = historical( name='danu_broken',end_year=game.year+1,desc=None,image=None)
                $ game.history_mod.append(game.history)
              else: 
                game.girl.third '[game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Низ живота пульсирует жгучей болью, и эта боль - самое классное, что было в её жизни. Жаль, что успокоившись, она придёт в ужас от произошедшего.\n Поэтому прямо сейчас ей хочется одного - умереть. Умереть счастливой.'
            elif game.girl.nature == 'lust':
              if game.girl.type == 'afrodita':
                game.girl.third '[game.girl.name] смотрит на дракона со счастливой улыбкой. Кажется, богиню нисколько не беспокоит та боль, что причинил ей дракон.'
              else:
                game.girl.third '[game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Низ живота пульсирует жгучей болью, и эта боль - самое классное, что было в её жизни. Даже успокоившись, она никогда не забудет первой близости со своим мучителем. Вот только такое никогда не повторится.\n Поэтому прямо сейчас ей хочется одного - умереть. Умереть счастливой.'
          $ game.rape.erection += 1
          if game.girl.type == 'afrodita':
            $ game.history = historical( name='afrodita_win',end_year=game.year+1,desc=None,image=None)
            $ game.history_mod.append(game.history)
 
# Полностью сломлена
      elif ratio_proud==0:  
        call lb_rape_broken from _call_lb_rape_broken_3


# Захвачены и руки, и тело
    elif not game.rape.body and not game.rape.arms:   
      if ratio_proud>0.66: # Честь превыше жизни
        if game.rape.erection == 0: # Приставить член к влагалищу
          $ game.rape.erection += 1  
          if not game.girl.willing:
            game.girl.third '[game.girl.name] в критической ситуации: драконий член уже приставлен к её лону, она полностью обездвижена, сопротивление ни к чему не приводит. Но вместо того, чтобы впасть в панику, она резко успокаивается и ищет выход из ситуации.'
            if game.rape.size == 1: # Миниатюрный дракончик
              $ game.rape.rage += random.randint(4,8)
            elif game.rape.size == 2: # Средний дракон 
              $ game.rape.rage += random.randint(2,6)
            elif game.rape.size == 3: # Матёрый драконище 
              $ game.rape.rage += random.randint(0,4)
            if game.girl.type == 'peasant' or game.girl.type == 'citizen' or game.girl.type == 'princess' or game.girl.type == 'jasmine':
              game.girl 'Мой дед пришёл сюда через Туманы из иного мира. Перед своей смертью он научил меня Опасному и Запретному приёму, который можно применять лишь в критической ситуации. По-моему, ситуация весьма критическая.'
            elif game.girl.type == 'elf':
              game.girl 'Мой дед пришёл сюда через Туманы из иного мира. Перед своей смертью он научил меня Тайному Колдовству, неизвестному даже старейшинам альвов. Его можно применить лишь раз в жизни, но, по-моему, ситуация весьма подходящая.'
            elif game.girl.type == 'mermaid' or game.girl.type == 'siren':
              game.girl 'Мой дед приплыл сюда через Туманы из иного мира. Перед своей смертью он научил меня Волшебному Заклинанию, заповедовав никогда не применять его, ибо оно калечет душу. Но сейчас сохранность души волнует меня в последнюю очередь.'
            elif game.girl.type == 'ice':
              game.girl 'В конце концов, я умею повелевать холодом! Неужели я не смогу проморозить червяка до самых костей?'
            elif game.girl.type == 'fire':
              game.girl 'В конце концов, я умею повелевать огнём! Неужели я не смогу прожарить червяка до самых костей?'
            elif game.girl.type == 'titan':
              game.girl 'В конце концов, я умею повелевать молниями! Неужели боги отвернуться от меня в сей скорбный час?'
          else: # Согласна
            game.girl.third 'Когда член дракона упирается во влагалище девушки, [game.girl.name] отворачивается и прикусывает губу. Больше ей ничего не остаётся делать - из хватки дракона не выбраться.'  

        elif game.rape.erection == 1: # Разорвать девственную плеву.
#          $ game.rape.erection += 1  
          if not game.girl.willing:
            game.girl.third  'Драконий член входит во влагалище на всю свою длину, и [game.girl.name] кричит от боли.'
            call lb_rape_women from _call_lb_rape_women_17
            if game.girl.type == 'ice' or game.girl.type == 'fire' or game.girl.type == 'titan':
              game.girl 'Надо сосредоточиться, у меня только одна попытка.'
            else:
              game.girl 'Как же там было-то? Не помню! Ничего не помню!!!'
          else: # Согласна
            if game.rape.size == 1: # Миниатюрный дракончик
              game.girl.third '[game.girl.name] изо всех сил стискивает зубы, и когда член дракона разрывает её девственую плеву, не издаёт ни единого стона боли.' 
            elif game.rape.size == 2: # Средний дракон 
              game.girl.third '[game.girl.name] изо всех сил стискивает зубы, но когда член дракона разрывает её девственую плеву, с её уст срывается негромкий стон боли.' 
            elif game.rape.size == 3: # Матёрый драконище 
              game.girl.third '[game.girl.name] изо всех сил стискивает зубы. Тщетно: когда член дракона разрывает её девственую плеву, [game.girl.name] истошно орёт от боли.'  
            call lb_rape_women from _call_lb_rape_women_22
 

        elif game.rape.erection == 2: # Совершить половой акт.
          $ game.rape.erection += 1  
          if not game.girl.willing:
            if random.randint(1,2)==1:  # Неудача у девушки, дракону повезло
              if game.girl.type == 'peasant' or game.girl.type == 'citizen' or game.girl.type == 'princess' or game.girl.type == 'jasmine':
                game.girl 'Крибли-крабли-бумс!'
                game.girl 'Ой, не так...'
              elif game.girl.type == 'elf':
                game.girl 'Абра-швабра-кадабра!'
                game.girl 'Ой, что-то не то...'
              elif game.girl.type == 'mermaid' or game.girl.type == 'siren':
                game.girl 'Трах-тибидох-тибидох!'
                game.girl 'Ой, ошибочка вышла...'
              elif game.girl.type == 'ice':
                game.girl 'Почувствуй истинную мощь Повелительницы льда!'
                'Поглощенный процессом, [game.dragon.name] евда обращает внимание на некоторое понижение температуры'
              elif game.girl.type == 'fire':
                game.girl 'Почувствуй истинную мощь Повелительницы огня!'
                'Поглощенный процессом, [game.dragon.name] евда обращает внимание на некоторое повышение температуры'
              elif game.girl.type == 'titan':
                game.girl 'Почувствуй истинную мощь Повелительницы молний!'
                'Поглощенный процессом, [game.dragon.name] воспринимает слабенькие разряды как часть заигрываний'
            else:
              if game.girl.type == 'peasant' or game.girl.type == 'citizen' or game.girl.type == 'princess' or game.girl.type == 'jasmine':
                game.girl 'Каге Буншин но Дзюцу!!!'
                'Пространство заполняет толпа теневых клонов'
                if random.randint(1,2)==1:
                  'Поглощённый процессом, [game.dragon.name] едва обращает внимание на теневых клонов, и они вскоре развеиваются'
                else:
                  '[game.dragon.name] полностью сбит с толку. Он отвлекается от пленницы, а потомм никак не может найти её в толпе одинаково раздетых девушек. С помощью клонов [game.girl.name] благополучно возвращается домой.'
                  call lb_rape_escape from _call_lb_rape_escape_1
                  return
              elif game.girl.type == 'elf':
                game.girl 'Бамбара, чуфара, лорики, ёрики, пикапу, трикапу, спорики, морики!'
                'Пространство заполняет огромная стая летучих обезьян'
                if random.randint(1,2)==1:
                  'Поглощённый процессом, [game.dragon.name] едва обращает внимание на летучих обезьян, и те вскоре улетают'
                else:
                  '[game.dragon.name] полностью сбит с толку. Пока он разбирается с частью летучих обезьян, остальные хватают альву и уносят её домой.'
                  call lb_rape_escape from _call_lb_rape_escape_2
                  return
              elif game.girl.type == 'mermaid' or game.girl.type == 'siren':
                game.girl 'Империо!'
                game.girl 'Немедленно отнеси меня домой!'
                if random.randint(1,2)==1:
                  game.dragon '*Неразборчивое рычание*'
                else:
                  game.dragon 'Как пожелаете, Божественная!'
                  call lb_rape_escape from _call_lb_rape_escape_3
                  return
              elif game.girl.type == 'ice':
                game.girl 'Холодку не желаешь?!'
                if 'ice_immunity' in game.dragon.modifiers():
                  'Кажется, [game.dragon.name] даже не почувствовал обжигающего холода'
                else:
                  'Холод пробирает дракона до костей. Сбитый с толку, [game.dragon.name] с трудом приходит в себя, а [game.girl.name] благополучно бежит прочь.'
                  call lb_rape_escape from _call_lb_rape_escape_4
                  return
              elif game.girl.type == 'fire':
                game.girl 'Огоньку не желаешь?!'
                if 'fire_immunity' in game.dragon.modifiers():
                  'Кажется, [game.dragon.name] даже не почувствовал опаляющего жара'
                else:
                  'Жар пробирает дракона до костей. Сбитый с толку, [game.dragon.name] с трудом приходит в себя, а [game.girl.name] благополучно бежит прочь.'
                  call lb_rape_escape from _call_lb_rape_escape_5
                  return
              elif game.girl.type == 'titan':
                game.girl 'Разнообразим нашу игру, красавчик?!'
                if 'lightning_immunity' in game.dragon.modifiers():
                  'Кажется, [game.dragon.name] даже не почувствовал сверкающей молнии'
                else:
                  'Электрический разряд пробирает дракона до костей. Сбитый с толку, [game.dragon.name] с трудом приходит в себя, а [game.girl.name] благополучно бежит прочь.'
                  call lb_rape_escape from _call_lb_rape_escape_6
                  return
            'После неудачи девушку захлёстывает паника. Второй попытки не будет.'
          else: # Согласна
            if game.rape.size == 1: # Миниатюрный дракончик
              game.girl.third '[game.girl.name] громко дышит сквозь сомкнутые зубы - и этим её участи в процессе и ограничивается. Лежит в объятиях дракона бревно-бревном. Честное слово, лучше бы брыкалась - хоть что-то интересное было бы!' 
            elif game.rape.size == 2: # Средний дракон 
              game.girl.third '[game.girl.name] негромко постанывает сквозь сомкнутые зубы - и этим её участи в процессе и ограничивается. Лежит в объятиях дракона бревно-бревном. Честное слово, лучше бы брыкалась - хоть что-то интересное было бы!' 
            elif game.rape.size == 3: # Матёрый драконище 
              game.girl.third '[game.girl.name] громко стонет от боли и пытается извиваться. Тщетно - она слишком хорошо зафиксирована. [game.dragon.name] улыбается - такой процесс явно пришёлся ему по вкусу!'

        elif game.rape.erection == 3: # Кончить.
          game.dragon 'Блажееенство!!!'
          $ game.rape.erection += 1
          if game.girl.willing:
              if game.rape.size == 1:
                game.girl 'И всего-то? Просто физическое упражнение, даже не особо сложное.' 
                game.girl 'Хотя зафиксировал ты меня очень надёжно'
              elif game.rape.size == 2:
                game.girl 'И всего-то? Сложное физическое упражнение, ничего особенного' 
                game.girl 'Хотя зафиксировал ты меня очень надёжно'
              elif game.rape.size == 3:
                game.girl 'Это было сложно. Ничего, я не боюсь ни испытаний, ни пыток' 
                game.girl 'Хотя если бы ты меня так крепко не зафиксировал бы... Хм.'

# Девушка яростно отбивается и шипит  сквозь стиснутые зубы
      if ratio_proud>0.33 and ratio_proud <=0.66: # Девушка яростно отбивается и шипит  сквозь стиснутые зубы
        if game.rape.erection == 0: # Приставить член к влагалищу
          if not game.girl.willing:
            if game.rape.size == 1: # Миниатюрный дракончик
              if game.girl.blind:
                game.girl.third 'Услышав возбуждённое, учащённое дыхание дракона, [game.girl.name] орёт от ужаса и пытается вырваться. Безуспешно: несмотря на свой маленький размер, [game.dragon.name] полностью обездвижил пленницу. '      
              else:  
                game.girl.third 'Увидив драконий член, [game.girl.name] орёт от ужаса и пытается вырваться. Безуспешно: несмотря на свой маленький размер, [game.dragon.name] полностью обездвижил пленницу. '
              $ game.rape.rage += random.randint(2,6)
            elif game.rape.size == 2: # Средний дракон 
              if game.girl.blind:
                game.girl.third 'Услышав возбуждённое, учащённое дыхание дракона, [game.girl.name] орёт от ужаса и пытается вырваться. Безуспешно: [game.dragon.name] полностью обездвижил пленницу. '
              else:
                game.girl.third 'Увидив драконий член, [game.girl.name] орёт от ужаса и пытается вырваться. Безуспешно: [game.dragon.name] полностью обездвижил пленницу. '
              $ game.rape.rage += random.randint(0,4)
            elif game.rape.size == 3: # Матёрый драконище 
              if game.girl.blind:
                game.girl.third 'Услышав возбуждённое, учащённое дыхание дракона, [game.girl.name] орёт от ужаса и пытается вырваться. Безуспешно: [game.dragon.name] полностью обездвижил пленницу. Да от такого гиганта сбежать в любом случае затруднительно.'
              else:
                game.girl.third 'Увидив драконий член, [game.girl.name] орёт от ужаса и пытается вырваться. Безуспешно: [game.dragon.name] полностью обездвижил пленницу. Да от такого гиганта сбежать в любом случае затруднительно.'
              $ game.rape.rage += random.randint(0,2)
          else: # Согласна
            game.girl.third '[game.girl.name] передёргивается всем телом, закрывает глаза и начинает истово молиться.'  
          $ game.rape.erection += 1

        elif game.rape.erection == 1: # Разорвать девственную плеву.
          if game.rape.size == 1: # Маленький дракончик 
            if not game.girl.willing:
              game.girl.third 'Несмотря на свой маленький размер, [game.dragon.name] обладает впечатляющим членом. Когда он проникает внутрь, [game.girl.name] кричит от боли, но её вопли лишь раззадоривают безжалостного ящера. '
            else: # Согласна
              game.girl.third 'Короткий стон прерывает молитву, но [game.girl.name] быстро приходит в себя, ёрзает в объятиях ящера и начинает молиться ещё истовее. '  
          elif game.rape.size == 2: # Средний дракон 
            if not game.girl.willing:
              game.girl.third '[game.dragon.name] обладает огромным членом, который с трудом входит в лоно девушки. [game.girl.name] кричит от боли, но её вопли лишь раззадоривают безжалостного ящера. '
            else: # Согласна
              game.girl.third 'Молитва заканчивается громким стоном. Впрочем, [game.girl.name] всё же приходит в себя, ёрзает в объятиях ящера и начинает молиться ещё истовее. '  
          elif game.rape.size == 3: # Матёрый драконище 
            if not game.girl.willing:
              game.girl.third '[game.dragon.name] - настоящий исполин, и член у него исполинский. Влагалище девушки с трудом растягивается, принимая в себя чужеродный орган. [game.girl.name] орёт от непереносимой боли, но её вопли лишь раззадоривают безжалостного ящера. '
            else: # Согласна
              game.girl.third 'Молитва заканчивается криком боли. [game.girl.name] кричит и беспрестанно ёрзает в объятиях ящерад. Кажется, с молитвами на сегодня всё. ' 
          call lb_rape_women from _call_lb_rape_women_16

        elif game.rape.erection == 2: # Совершить половой акт.
          $ game.rape.erection += 1
          # Удача у девушки (редкая), дракону не повезло
          if game.girl.type == 'elf' and random.randint(1,8)==1 and not game.girl.willing:
            game.girl 'Силиврен пенна мириель!'
            'Богиня Дану снизошла к мольбам своей дочери. Дракона пронзает столб света, и он, оглушённый, отпускает пленницу. Ведомая волей богини, альва сбегает от своего мучителя.'
            call lb_rape_escape from _call_lb_rape_escape_7
            return
          elif game.girl.type == 'ice' and random.randint(1,8)==1 and not game.girl.willing:
            game.girl 'Холодку не желаешь?!'
            if 'ice_immunity' in game.dragon.modifiers():
              'Кажется, [game.dragon.name] даже не почувствовал обжигающего холода'
            else:
              'Холод пробирает дракона до костей. Сбитый с толку, [game.dragon.name] с трудом приходит в себя, а [game.girl.name] благополучно бежит прочь.'
              call lb_rape_escape from _call_lb_rape_escape_8
              return
          elif game.girl.type == 'fire' and random.randint(1,8)==1 and not game.girl.willing:
            game.girl 'Огоньку не желаешь?!'
            if 'fire_immunity' in game.dragon.modifiers():
              'Кажется, [game.dragon.name] даже не почувствовал опаляющего жара'
            else:
              'Жар пробирает дракона до костей. Сбитый с толку, [game.dragon.name] с трудом приходит в себя, а [game.girl.name] благополучно бежит прочь.'
              call lb_rape_escape from _call_lb_rape_escape_9
              return
          elif game.girl.type == 'titan' and random.randint(1,8)==1 and not game.girl.willing:
            game.girl 'Разнообразим нашу игру, красавчик?!'
            if 'lightning_immunity' in game.dragon.modifiers():
              'Кажется, [game.dragon.name] даже не почувствовал сверкающей молнии'
            else:
              'Электрический разряд пробирает дракона до костей. Сбитый с толку, [game.dragon.name] с трудом приходит в себя, а [game.girl.name] благополучно бежит прочь.'
              call lb_rape_escape from _call_lb_rape_escape_10
              return
          else:
            $ game.rape.erection += 1  
            if not game.girl.willing:
              game.girl.third '[game.girl.name] прекращает сопротивляться и бессильно обвисает в объятиях дракона, лишь негромко и жалобно постанывая от боли.'
            else:  # Согласна
              if game.rape.size == 1: # Миниатюрный дракончик
                game.girl.third '[game.girl.name] продолжает молиться, то и дело постанывая от боли. Её глаза закрыты, она пытается отрешиться от того, что происходит там, внизу.' 
              elif game.rape.size == 2: # Средний дракон 
                game.girl.third 'Молитва [game.girl.name_r] то и дело прерывается криками боли. Её глаза закрыты, она пытается отрешиться от того, что происходит там, внизу. Тщетно.' 
              elif game.rape.size == 3: # Матёрый драконище
                game.girl.third 'Отдельные слова молитв тонут в криках боли. Глаза [game.girl.name_r] крепко зажмурены, но она даже не может дёрнуться, чтобы облегчить муку - дракон держит её слишком крепко.' 


        elif game.rape.erection == 3: # Кончить.
          if game.rape.size == 1 and random.randint(1,4) == 1 and not game.girl.willing: # Миниатюрный дракончик
            game.girl.third 'Пользуясь тем, что дракон не обращает на неё никакого внимания, [game.girl.name] резким движением вырывает руки из его лап и срывает крошечную тушку со своего тела. Смирение было наигранным!'
            call lb_rape_fail from _call_lb_rape_fail_13 
          elif game.rape.size == 2 and random.randint(1,5) == 1 and not game.girl.willing: # Средний дракон 
            game.girl.third 'Пользуясь тем, что дракон не обращает на неё никакого внимания, [game.girl.name] резким движением вырывает руки из его лап и отбрасывает его тушу прочь. Смирение было наигранным!'
            call lb_rape_fail from _call_lb_rape_fail_14 
          elif game.rape.size == 3 and random.randint(1,6) == 1 and not game.girl.willing: # Матёрый драконище 
            game.girl.third 'Пользуясь тем, что дракон не обращает на неё никакого внимания, [game.girl.name] аккуратным движением вынимает руки из его лап и изящно выскальзывает из объятий дракона. Смирение было наигранным!'
            call lb_rape_fail from _call_lb_rape_fail_15
          else:
            game.dragon 'Блажееенство!!!'
            $ game.rape.erection += 1
            if game.girl.willing:
              if game.rape.size == 1:
                game.girl 'Да простит мой грех Небесный Отец. К счастью, это оказалось легче, чем я боялась.' 
              elif game.rape.size == 2:
                game.girl 'Да простит мой грех Небесный Отец. Это было ужасно' 
              elif game.rape.size == 3:
                game.girl 'Небесный Отец... наказывает меня... за грехи мои... Впрочем, я бы всё равно ничего не смогла бы сделать.'

# Девушка заламывает руки и молит о пощаде
      elif ratio_proud>0 and ratio_proud <=0.33:  # Заламывает руки и умоляет прекратить
        if game.rape.erection == 0: # Приставить член к влагалищу
          if not game.girl.willing:
            if game.girl.blind:
              game.girl.third '[game.girl.name] мотает безглазой головой и молит о пощаде'
            else:
              game.girl.third 'При виде драконьего члена [game.girl.name] продожает молить о пощаде. Правда, как-то неубедительно...'
          else:
            if game.girl.type == 'afrodita':
              game.girl.third 'При виде драконьего члена глаза [game.girl.name_r] взагораются от восторга' 
            else:
              game.girl.third 'При виде драконьего члена у [game.girl.name_r] всё внутри замирает от какого-то необъяснимого чувства...' 
          $ game.rape.erection += 1

        elif game.rape.erection == 1: # Разорвать девственную плеву.
          if game.rape.size == 1: # Маленький дракончик 
            if game.girl.blind:
              game.girl.third 'Несмотря на свой маленький размер, [game.dragon.name] обладает впечатляющим членом. [game.girl.name] закусывает губу, полностью сосредоточившись на ощущениях. Дракон неспешно вводит свой орган внутрь её лона'
            else:
              game.girl.third 'Несмотря на свой маленький размер, [game.dragon.name] обладает впечатляющим членом. [game.girl.name] заворожённо смотрит, как он неспешно проникает внутрь её лона, и коротко вскрикивает от боли. '
          elif game.rape.size == 2: # Средний дракон 
            game.girl.third '[game.dragon.name] обладает огромным членом, который с трудом входит в лоно девушки. [game.girl.name] полностью сосредатачивается на своих ощущениях и коротко вскрикивает от боли. '
          elif game.rape.size == 3: # Матёрый драконище 
            game.girl.third '[game.dragon.name] - настоящий исполин, и член у него исполинский. Влагалище девушки с трудом растягивается, принимая в себя чужеродный орган. [game.girl.name] пытается всячески помочь дракону в этом нелёгком труде, и когда уд полностью погружается в лоно, с её уст срывается крик боли и торжества!'
          call lb_rape_women from _call_lb_rape_women_15

        elif game.rape.erection == 2: # Совершить половой акт.
          if game.rape.pussy:
            game.girl.third '[game.girl.name] млеет от удовольствия. Будучи полностью обездвиженной, она расслабляется и впитывает новые ощущения, в которых боль причудливо сплетается с наслаждением. С её губ всё чаще и чаще срываются страстные стоны, смешивающиеся с порыкиваниями дракона. Происходящее нравится ящеру всё больше и больше!'
          else:
            game.girl.third 'Повреждения, нанесённые драконом при ухаживании, слишком серьёзны. Каждое движение дракона отдаётся жгучей болью в женском местечке, и [game.girl.name] потрясённо понимает, что ей... это... нравится! Страдание причудливо смешивается с наслаждением, и [game.girl.name] жаждет больше - и того, и другого.'
            game.girl 'Быстрее... глубже... сильнее... Порви меня!!!'
          $ game.rape.erection += 1 

        elif game.rape.erection == 3: # Кончить.
          game.girl.third 'Ритм ускоряется. [game.girl.name], несмотря на вынужденную неподвижность, начинает извиваться в порывах страсти, и когда драконье семя заполняет её лоно, издаёт долгий крик удовольствия '
          game.dragon 'Блажееенство!!!'
          if game.rape.pussy:
            if game.girl.blind:
              game.girl.third '[game.girl.name] счастливо улыбается куда-то в пустоту. Сейчас ей кажется, что потеря зрения - крошечная плата за пережитоте блаженство. [game.girl.name] на седьмом небе от счастья и мечтает о повторном заходе!'
            else:
              if game.girl.type == 'afrodita':
                game.girl.third '[game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Лицо её расплывается в радостной, счастливой улыбке. Кажется, произошедший позор её нимало не беспокоит - да она и позором это не считает! Что бы ни задумала богиня любви - её план только что блистательно осуществился.'
              else:
                game.girl.third '[game.girl.name] смотрит на дракона со счастливой улыбкой. Сейчас неважно, кем она была раньше, что было между ними до того. [game.girl.name] на седьмом небе от счастья и мечтает о повторном заходе!'
          else:
            if game.girl.nature == 'proud':
              game.girl.third '[game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Низ живота пульсирует жгучей болью, и эта боль - самое классное, что было в её жизни. Жаль, что успокоившись, она возненавидит своего мучителя.\n Поэтому прямо сейчас ей хочется одного - умереть. Умереть счастливой.'
            elif game.girl.nature == 'innocent':
              if game.girl.type == 'danu':
                game.girl.third 'Богиня [game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Низ живота пульсирует жгучей болью, и эта боль - самое лучшее, что было в её жизни. \n Похоже, после пережитого богиня Дану решила отказаться от своего народа и стать верной игрушкой дракона'
                $ game.history = historical( name='danu_broken',end_year=game.year+1,desc=None,image=None)
                $ game.history_mod.append(game.history)
              else: 
                game.girl.third '[game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Низ живота пульсирует жгучей болью, и эта боль - самое классное, что было в её жизни. Жаль, что успокоившись, она придёт в ужас от произошедшего.\n Поэтому прямо сейчас ей хочется одного - умереть. Умереть счастливой.'
            elif game.girl.nature == 'lust':
              if game.girl.type == 'afrodita':
                game.girl.third '[game.girl.name] смотрит на дракона со счастливой улыбкой. Кажется, богиню нисколько не беспокоит та боль, что причинил ей дракон.'
              else:
                game.girl.third '[game.girl.name] лежит, откинувшись на спину, и тяжело дышит. Низ живота пульсирует жгучей болью, и эта боль - самое классное, что было в её жизни. Даже успокоившись, она никогда не забудет первой близости со своим мучителем. Вот только такое никогда не повторится.\n Поэтому прямо сейчас ей хочется одного - умереть. Умереть счастливой.'
          $ game.rape.erection += 1
          if game.girl.type == 'afrodita':
            $ game.history = historical( name='afrodita_win',end_year=game.year+1,desc=None,image=None)
            $ game.history_mod.append(game.history)
 
# Полностью сломлена
      elif ratio_proud==0:  
        call lb_rape_broken from _call_lb_rape_broken_4

    call screen penetration_sex    
    return



label lb_rape_body:    # Змей обвивается вокруг тела
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    $ ratio_proud=game.rape.actual_proud/game.rape.full_proud
    game.dragon.third '[game.dragon.name] неспешно обвивается вокруг тела пленницы'
    if game.rape.arms:  # Если руки свободны, девчонка может дать сдачи

      if ratio_proud>0.66: # Честь превыше жизни
        if game.rape.size == 1: # Миниатюрный дракончик
          if not game.girl.willing:
            if random.randint(1, game.dragon.max_energy()) > 4: # Дракону повезло
              game.dragon.third '[game.dragon.name] всё же обвивается вокруг визжащего, сопротивляющегося, брыкающегося тела. Да за такое молоко надо бесплатно давать, не меньше! Гордость за этот подвиг слегка унимает растущее раздражение дракона.'
              if 'tough_scale' in game.dragon.modifiers():
                $ game.rape.rage += random.randint(6,13)
              else:
                $ game.rape.rage += random.randint(8,15)
              $ game.rape.body=False
            else:
              game.girl.third '[game.girl.name] с силой отшвыривает насильника в сторону'
              'Эх, если бы [game.dragon.name] был побольше, или [game.girl.name] была бы поспокойней!'
              $ game.rape.rage += random.randint(6,10)
          else: # Согласна
            game.girl.third '[game.girl.name] с ненавистью смотрит, как мелкий змеёныш обвивается вокруг её тела, но, несмотря на свободные руки, даже не пытается ему помешать.'
            $ game.rape.body=False
        elif game.rape.size == 2: # Средний дракон
          if not game.girl.willing:
            if random.randint(1,game.dragon.max_energy()) <= 3: # Дракону не повезло
              game.girl.third 'С изрядным трудом [game.girl.name] отпихивает насильника в сторону'
              'Да разве можно так издеваться над бедным драконом, а?!'
              $ game.rape.rage += random.randint(16,20)
            else:  #  У дракона всё получилось
              game.girl.third '[game.girl.name] визжит, царапается, бьёт по телу дракона кулаками и кусается. Но [game.dragon.name] с изрядным трудом всё же обвивается вокруг её тела.'
              if 'tough_scale' in game.dragon.modifiers():
                $ game.rape.rage += random.randint(14,22)
              else:
                $ game.rape.rage += random.randint(16,24)
              $ game.rape.body=False
          else: # Согласна
            game.girl.third '[game.girl.name] с ненавистью смотрит, как змей обвивается вокруг её тела, но, несмотря на свободные руки, даже не пытается ему помешать.'
            $ game.rape.body=False
        elif game.rape.size == 3: # Матёрый драконище
          if not game.girl.willing:
            game.girl.third '[game.girl.name] визжит, царапается, бьёт по телу дракона кулаками и кусается. Но [game.dragon.name] слишком велик, трепыхания жертвы лишь раздражают его, но не могут ничем повредить. '
            if 'tough_scale' in game.dragon.modifiers():
              $ game.rape.rage += random.randint(12,20)
            else:
              $ game.rape.rage += random.randint(14,22)
          else: # Согласна
            game.girl.third '[game.girl.name] с ненавистью смотрит, как огромный змей обвивается вокруг её тела, но, несмотря на свободные руки, даже не пытается ему помешать. Впрочем, это у неё всё равно бы не получилось.'
          $ game.rape.body=False
      elif ratio_proud>0.33 and ratio_proud <=0.66:  # Отбивается яростно, но всё же без фанатизма
        if game.rape.size == 1: # Миниатюрный дракончик
          if not game.girl.willing:
            if random.randint(1, game.dragon.max_energy()) <= 2: # Дракону не повезло
              game.girl.third '[game.girl.name]  отпихивает насильника в сторону'
              'Эх, если бы [game.dragon.name] был побольше, или поудачливее, или [game.girl.name] сопротивлялась бы не столь яростно!'
              $ game.rape.rage += random.randint(4,6)
            else: # Дракону повезло
              game.girl.third '[game.girl.name] пытается отпихнуть насильника в сторону, но в последний момент замирает от страха, и [game.dragon.name] обвивается вокруг её тела.'
              if 'tough_scale' in game.dragon.modifiers():
                $ game.rape.rage += random.randint(8,12)
              else:
                $ game.rape.rage += random.randint(10,14)
              $ game.rape.body=False
          else: # Согласна
            game.girl.third 'Когда мелкий змеёныш обвивается вокруг тела [game.girl.name_r], девушка, даже не пытаясь сопротивляться, начинает громко и отчаянно молиться.'
            $ game.rape.body=False
        elif game.rape.size == 2: # Средний дракон
          if not game.girl.willing:
            game.girl.third '[game.girl.name] пытается отпихнуть насильника в сторону, но он чересчур велик, а пленница слишком напугана и сражается вполсилы.'
            if 'tough_scale' in game.dragon.modifiers():
              $ game.rape.rage += random.randint(6,10)
            else:
              $ game.rape.rage += random.randint(8,12)
          else: # Согласна
            game.girl.third 'Когда змей обвивается вокруг тела [game.girl.name_r], девушка, даже не пытаясь сопротивляться, начинает громко и отчаянно молиться.'
          $ game.rape.body=False
        elif game.rape.size == 3: # Матёрый драконище
          if not game.girl.willing:
            game.girl.third '[game.girl.name] пытается отпихнуть насильника в сторону, но он слишком велик и едва замечает её усилия'
            if 'tough_scale' in game.dragon.modifiers():
              $ game.rape.rage += random.randint(4,8)
            else:
              $ game.rape.rage += random.randint(6,10)
          else: # Согласна
            game.girl.third 'Когда огромный змей обвивается вокруг тела [game.girl.name_r], девушка, даже не пытаясь сопротивляться, начинает громко и отчаянно молиться. Впрочем, сопротивляйся-не сопротивляйся - исход всё равно один.'
          $ game.rape.body=False

      elif ratio_proud>0 and ratio_proud <=0.33:  # Заламывает руки и умоляет прекратить
        if game.rape.size == 1: # Миниатюрный дракончик
          if not game.girl.willing:
            if random.randint(1, game.dragon.max_energy()) <= 1: # Дракону не повезло
              game.girl.third '[game.girl.name] аккуратно берёт дракона на руки и откладывает его в сторону.'
              'Да разве можно так издеваться над бедным драконом, а?!'
              $ game.rape.rage += random.randint(4,6)
            else: # Дракону повезло
              if game.girl.blind:
                game.girl.third '[game.girl.name] пытается взять дракона на руки и отложить в сторону, но в последний момент замирает от страха и прислушивается к своим ощущениям. [game.dragon.name] неспешно обвивается вокруг её тела.'
              else:
                game.girl.third '[game.girl.name] пытается взять дракона на руки и отложить в сторону, но в последний момент замирает от страха и безвольно смотрит, как [game.dragon.name] обвивается вокруг её тела.'
              if 'tough_scale' in game.dragon.modifiers():
                $ game.rape.rage += random.randint(2,6)
              else:
                $ game.rape.rage += random.randint(4,8)
              $ game.rape.body=False
          else: # Согласна
            game.girl.third '[game.girl.name] всячески помогает мелкому дракоше поудобнее обвиться вокруг её тела.'
            $ game.rape.body=False
        elif game.rape.size == 2: # Средний дракон
          if not game.girl.willing:
            game.girl.third '[game.girl.name] вяло сопротивляется и молит дракона о пощаде, пока тот неспешно обвивается вокруг её тела.'
            if 'tough_scale' in game.dragon.modifiers():
              $ game.rape.rage += random.randint(2,14)
            else:
              $ game.rape.rage += random.randint(4,6)
          else: # Согласна
            game.girl.third '[game.girl.name] помогает дракону поудобнее обвиться вокруг её тела.'
          $ game.rape.body=False
        elif game.rape.size == 3: # Матёрый драконище
          if not game.girl.willing:
            game.girl.third '[game.girl.name] понимает, что насильник слишком велик и сопротивление бесполезно. Она пробует молить о пощаде, но после короткого шипения решает расслабиться и попытаться получить удовольствие. '
            if 'tough_scale' in game.dragon.modifiers():
              $ game.rape.rage += random.randint(0,2)
            else:
              $ game.rape.rage += random.randint(2,4)
          else: # Согласна
            game.girl.third '[game.girl.name] пытается помочь дракону поудобнее обвиться вокруг её тела, но огромный ящер успешно справляется с этим и без посторонней помощи.'
          $ game.rape.body=False
      elif ratio_proud==0:
        if game.girl.blind:
          game.girl.third ' [game.girl.name] безучастно смотрит в пустоту отсутствующими глазами и ни на что не реагирует. '
        else:
          game.girl.third ' [game.girl.name] безучастно смотрит в пустоту и ни на что не реагирует. '
        $ game.rape.body=False

    elif not game.rape.arms:  # Руки заняты

      if ratio_proud>0.66: # Честь превыше жизни
        if game.rape.size == 1: # Миниатюрный дракончик
          if not game.girl.willing:
            if random.randint(1, game.dragon.max_energy()) <= 3: # Дракону не повезло
              game.dragon.third 'Точный пинок не только отшвыривает дракона, но и заставляет его разжать лапы и отпустить девушку .'
              $ game.rape.rage += random.randint(4,8)
              $ game.rape.define_freedom()
            else:
              game.girl.third '[game.girl.name] яростно пинается, но толку от этого немного.'
              $ game.rape.rage += random.randint(6,10)
              $ game.rape.body=False
          else: # Согласна
            game.girl.third '[game.girl.name] с ненавистью смотрит, как мелкий змеёныш обвивается вокруг её тела, но даже не пытается ему помешать. Впрочем, дракон всё равно крепко держит её ладони своими лапами.'
            $ game.rape.body=False
        elif game.rape.size == 2: # Средний дракон
          if not game.girl.willing:
            if random.randint(1, game.dragon.max_energy()) <= 2: # Дракону не повезло
              game.girl.third 'Град точных пинков не только держит дракона на расстоянии, но и заставляет его разжать лапы и отпустить девушку.'
              'Да разве можно так издеваться над бедным драконом, а?!'
              $ game.rape.rage += random.randint(4,8)
              $ game.rape.define_freedom()
            else:  #  У дракона всё получилось
              game.girl.third '[game.girl.name] визжит, пинается и кусается, но благодаря зафиксированным рукам ничего не может сделать.'
              $ game.rape.rage += random.randint(4,8)
              $ game.rape.body=False
          else: # Согласна
            game.girl.third '[game.girl.name] с ненавистью смотрит, как змей обвивается вокруг её тела, но даже не пытается ему помешать. Впрочем, дракон всё равно крепко держит её ладони своими лапами.'
            $ game.rape.body=False
        elif game.rape.size == 3: # Матёрый драконище
          if not game.girl.willing:
            game.girl.third '[game.girl.name] визжит, пинается и кусается, но благодаря зафиксированным рукам ничего не может сделать. Впрочем, дракон настолько велик, что свободные руки ей не слишком помогли бы.'
            $ game.rape.rage += random.randint(2,6)
          else: # Согласна
            game.girl.third '[game.girl.name] с ненавистью смотрит, как огромный змей обвивается вокруг её тела, но даже не пытается ему помешать. Впрочем, это у неё всё равно бы не получилось.'
          $ game.rape.body=False

      elif ratio_proud>0.33 and ratio_proud <=0.66:  # Отбивается яростно, но всё же без фанатизма
        if game.rape.size == 1: # Миниатюрный дракончик
          if not game.girl.willing:
            if random.randint(1, game.dragon.max_energy()) <= 2: # Дракону не повезло
              game.girl.third 'Град точных пинков не только держит дракона на расстоянии, но и заставляет его разжать лапы и отпустить девушку.'
              'Да разве можно так издеваться над бедным драконом, а?!'
              $ game.rape.rage += random.randint(4,8)
              $ game.rape.define_freedom()
            else: # Дракону  повезло
              game.girl.third '[game.girl.name] пытается избежать драконих объятий, но с зафиксированными руками это несколько неудобно.'
              $ game.rape.rage += random.randint(4,8)
              $ game.rape.body=False
          else: # Согласна
            game.girl.third 'Когда мелкий змеёныш обвивается вокруг тела [game.girl.name_r], девушка, даже не пытаясь сопротивляться, начинает громко и отчаянно молиться.'
            $ game.rape.body=False
        elif game.rape.size == 2: # Средний дракон
          if not game.girl.willing:
            game.girl.third '[game.girl.name] пытается пинками отогнать насильника в сторону, но он чересчур велик, а пленница слишком напугана и сражается вполсилы.'
            $ game.rape.rage += random.randint(2,6)
          else: # Согласна
            game.girl.third 'Когда змей обвивается вокруг тела [game.girl.name_r], девушка, даже не пытаясь сопротивляться, начинает громко и отчаянно молиться.'
          $ game.rape.body=False
        elif game.rape.size == 3: # Матёрый драконище
          if not game.girl.willing:
            game.girl.third '[game.girl.name] пытается пинками отогнать  насильника в сторону, но он слишком велик и едва замечает её усилия'
            $ game.rape.rage += random.randint(0,4)
          else: # Согласна
            game.girl.third 'Когда огромный змей обвивается вокруг тела [game.girl.name_r], девушка, даже не пытаясь сопротивляться, начинает громко и отчаянно молиться. Впрочем, даже будь у неё свободны руки и сопротивляйся она изо все сил - исход всё равно был бы тем же самым.'
          $ game.rape.body=False

      elif ratio_proud>0 and ratio_proud <=0.33:  # Заламывает руки и умоляет прекратить
        if not game.girl.willing:
          game.girl.third '[game.girl.name] пытается сопротивляться и молит дракона о пощаде. Правда, как-то вяло. Похоже, ей и самой интересно, что будет дальше. '
          $ game.rape.rage += random.randint(0,2)
        else: # Согласна
          if game.rape.size == 1: # Миниатюрный дракончик
            game.girl.third '[game.girl.name] с улыбкой смотрит, как мелкий дракончик обвивается вокруг её тела.'
          elif game.rape.size == 2: # Средний дракон
            game.girl.third '[game.girl.name] с интересом смотрит, как дракон обвивается вокруг её тела.'
          elif game.rape.size == 3: # Средний дракон
            game.girl.third '[game.girl.name] с лёгкой опаской наблюдает за огромным драконом, обвивающимся вокруг её тела.'
        $ game.rape.body=False
      elif ratio_proud==0:
        if game.girl.blind:
          game.girl.third ' [game.girl.name] безучастно смотрит в пустоту отсутствующими глазами и ни на что не реагирует. '
        else:
          game.girl.third ' [game.girl.name] безучастно смотрит в пустоту и ни на что не реагирует. '
        $ game.rape.body=False
    call screen penetration_sex
    return


# Схватить за руки
label lb_rape_arms:
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    $ ratio_proud=game.rape.actual_proud/game.rape.full_proud
    game.dragon.third '[game.dragon.name] пытается схватить руки пленницы своими лапами '
    if game.rape.body:  # Если тело свободно, девчонка может дать сдачи

      if ratio_proud>0.66: # Честь превыше жизни
        if game.rape.size == 1: # Миниатюрный дракончик
          if not game.girl.willing: # @fdsc
            if random.randint(1, game.dragon.max_energy()) > 2: # Дракону повезло
              game.dragon.third 'Хотя [game.girl.name] пинается и отмахивается руками подобно ветряной мельнице,  [game.dragon.name] всё же выгадывает подходящий момент и хватает её за руки.'
              $ game.rape.rage += random.randint(6,10)
              $ game.rape.arms=False
            else: # Дракону не повезло
              game.girl.third '[game.girl.name] пинается и отмахивается руками подобно ветряной мельнице. [game.dragon.name] никак не может выгадать подходящий момент. '
              'Эх, если бы [game.dragon.name] был побольше, или [game.girl.name] была бы поспокойней!'
              $ game.rape.rage += random.randint(2,4)
          else: # Согласна
            game.girl.third '[game.girl.name] неохотно разжимает кулаки и позволяет маленькому дракончику взять ладони своими крошечными лапками.'
            $ game.rape.arms=False
        elif game.rape.size == 2: # Средний дракон
          if not game.girl.willing:
            if random.randint(1, game.dragon.max_energy()) <= 1: # Дракону не повезло
              game.girl.third '[game.dragon.name] хватает девушку за руки, но резкий и чувствительный пинок заставляет его отшатнуться. '
              'Да разве можно так издеваться над бедным драконом, а?!'
              $ game.rape.rage += random.randint(4,8)
            else:  #  У дракона всё получилось
              game.girl.third '[game.girl.name] визжит, пинается и бьёт по телу дракона кулаками. На последнем он её и ловит. Всё, теперь не уйдёт! '
              $ game.rape.rage += random.randint(4,8)
              $ game.rape.arms=False
          else: # Согласна
            game.girl.third '[game.girl.name] неохотно разжимает кулаки и позволяет дракону взять ладони своими лапами.'
            $ game.rape.arms=False
        elif game.rape.size == 3: # Матёрый драконище
          if not game.girl.willing:
            game.girl.third '[game.girl.name] визжит, пинается и бьёт по телу дракона кулаками. Но [game.dragon.name] слишком велик, он с лёгкостью захватывает руки девушки в свои лапы. '
            $ game.rape.rage += random.randint(2,6)
          else: # Согласна
            game.girl.third '[game.girl.name] неохотно разжимает кулаки. Её крошечные ладони практически тонут в огромных лапах дракона.'
          $ game.rape.arms=False

      elif ratio_proud>0.33 and ratio_proud <=0.66:  # Отбивается яростно, но всё же без фанатизма
        if game.rape.size == 1: # Миниатюрный дракончик
          if not game.girl.willing:
            if random.randint(1, game.dragon.max_energy()) <= 1: # Дракону не повезло
              if game.girl.blind:
                game.girl.third 'Ориентируясь на слух, [game.girl.name]  метко пинает дракона, не позволяя ему приблизиться. '
              else:
                game.girl.third '[game.girl.name]  метко пинает дракона, не позволяя ему приблизиться. '
              $ game.rape.rage += random.randint(6,10)
            else: # Дракону повезло
              game.girl.third '[game.girl.name] пинается и пытается отпихнуть насильника в сторону, но в последний момент замирает от страха, и [game.dragon.name] благополучно хватает её за руки.'
              $ game.rape.rage += random.randint(4,8)
              $ game.rape.arms=False
          else: # Согласна
            game.girl.third '[game.girl.name] отчётливо вздрагивает, когда маленький дракончик берёт её ладони своими крошечными лапками.'
            $ game.rape.arms=False
        elif game.rape.size == 2: # Средний дракон
          if not game.girl.willing:
            game.girl.third '[game.girl.name] пинается и пытается отпихнуть насильника в сторону, но он чересчур велик, а пленница слишком напугана и сражается вполсилы.'
            $ game.rape.rage += random.randint(2,6)
          else: # Согласна
            game.girl.third '[game.girl.name] отчётливо вздрагивает, когда дракон берёт её ладони своими лапами.'
          $ game.rape.arms=False
        elif game.rape.size == 3: # Матёрый драконище
          if not game.girl.willing:
            game.girl.third '[game.girl.name] пинается и пытается отпихнуть насильника в сторону, но он слишком велик и едва замечает её усилия'
            $ game.rape.rage += random.randint(1,4)
          else: # Согласна
            game.girl.third '[game.girl.name] отчётливо вздрагивает, когда её ладони тонут в огромных лапах дракона.'
          $ game.rape.arms=False

      elif ratio_proud>0 and ratio_proud <=0.33:  # Заламывает руки и умоляет прекратить
        if game.rape.size == 1: # Миниатюрный дракончик
          if not game.girl.willing:
            if random.randint(1, game.dragon.max_energy() + game.dragon.reputation.points) <= 1: # Дракону не повезло
              game.girl.third '[game.girl.name] аккуратно пинает дракона и отталкивает его в сторону.'
              'Да разве можно так издеваться над бедным драконом, а?!'
              $ game.rape.rage += random.randint(4,10)
            else: # Дракону повезло
              game.girl.third '[game.girl.name]  пытается акуратно пнуть дракона и оттолкнуть в сторону, но в последний момент замирает от страха и безвольно смотрит, как [game.dragon.name] хватает её за руки.'
              $ game.rape.rage += random.randint(2,6)
              $ game.rape.arms=False
          else: # Согласна
            game.girl.third 'Счастливо улыбаясь, [game.girl.name] берёт ладонями лапки дракона.'
            $ game.rape.arms=False
        elif game.rape.size == 2: # Средний дракон
          if not game.girl.willing:
            game.girl.third '[game.girl.name] вяло сопротивляется и молит дракона о пощаде, пока тот неспешно лапает её за руки.'
            $ game.rape.rage += random.randint(0,4)
          else: # Согласна
            game.girl.third 'Счастливо улыбаясь, [game.girl.name] вкладывает ладони в лапы дракона.'
          $ game.rape.arms=False
        elif game.rape.size == 3: # Матёрый драконище
          if not game.girl.willing:
            game.girl.third '[game.girl.name] понимает, что насильник слишком велик и сопротивление бесполезно. Она пробует молить о пощаде, но после короткого шипения решает расслабиться и попытаться получить удовольствие. '
            $ game.rape.rage += random.randint(0,2)
          else: # Согласна
            game.girl.third 'Очень аккуратно [game.girl.name] вкладывает ладони в огромные лапы дракона.'
          $ game.rape.arms=False
      elif ratio_proud==0:
        game.girl.third ' [game.girl.name] безучастно смотрит в пустоту и ни на что не реагирует. '
        $ game.rape.arms=False

    elif not game.rape.body:  # Тело захвачено

      if ratio_proud>0.66: # Честь превыше жизни
        if game.rape.size == 1: # Миниатюрный дракончик
          if not game.girl.willing:
            if random.randint(1, game.dragon.max_energy() + game.dragon.reputation.points) <= 1: # Дракону не повезло
              game.dragon.third '[game.girl.name] наносит по телу дракона такой ошеломляющий град ударов, что [game.dragon.name] вынужден отпустить её и отползти подальше.'
              $ game.rape.rage += random.randint(2,4)
              $ game.rape.define_freedom()
            else: # Дракону не повезло
              game.girl.third '[game.girl.name] со всей дури бьёт по телу дракона, но это лишь помогает зафиксировать её руки.'
              $ game.rape.rage += random.randint(4,8)
              $ game.rape.arms=False   
          else: # Согласна
            game.girl.third '[game.girl.name] неохотно разжимает кулаки и позволяет маленькому дракончику взять ладони своими крошечными лапками.'
            $ game.rape.arms=False  
        elif game.rape.size == 2: # Средний дракон
          if not game.girl.willing:
            if random.randint(1,  game.dragon.max_energy() + game.dragon.reputation.points + 2) <= 1: # Дракону не повезло
              game.girl.third '[game.dragon.name] тянется своими грязными лапами к невинному телу, но резкий удар кулаком в глаз заставляет его переменить намерения. По крайней мере, на время.'
              'Да разве можно так издеваться над бедным драконом, а?!'
              $ game.rape.rage += random.randint(4,8)
              $ game.rape.define_freedom()
            else:  #  У дракона всё получилось
              game.girl.third '[game.girl.name] визжит и бьёт по телу дракона кулаками. На последнем он её и ловит. Всё, теперь не уйдёт! '
              $ game.rape.rage += random.randint(2,6)
              $ game.rape.arms=False
          else: # Согласна
            game.girl.third '[game.girl.name] неохотно разжимает кулаки и позволяет дракону взять ладони своими лапами.'
            $ game.rape.arms=False
        elif game.rape.size == 3: # Матёрый драконище
          if not game.girl.willing:
            game.girl.third '[game.girl.name] визжит и бьёт по телу дракона кулаками. Но [game.dragon.name] слишком велик, он с лёгкостью захватывает руки девушки в свои лапы. '
            $ game.rape.rage += random.randint(0,4)
          else: # Согласна
            game.girl.third '[game.girl.name] неохотно разжимает кулаки. Её крошечные ладони практически тонут в огромных лапах дракона.'
          $ game.rape.arms=False

      elif ratio_proud>0.33 and ratio_proud <=0.66:  # Отбивается яростно, но всё же без фанатизма
        if game.rape.size == 1: # Миниатюрный дракончик
          if not game.girl.willing:
            if random.randint(1,  game.dragon.max_energy() + game.dragon.reputation.points + 2) <= 1: # Дракону не повезло
              game.girl.third '[game.girl.name]  со всей силы бьёт дракона кулаком в глаз. Кажется, она сама не ожидала такого эффекта. '
              $ game.rape.rage += random.randint(6,10)
              $ game.rape.define_freedom()
            else: # Дракону повезло
              game.girl.third '[game.girl.name] пытается сопротивляться, но обвившееся вокруг неё тело дракона внушает ей дикий ужас, и [game.dragon.name] благополучно хватает её за руки.'
              $ game.rape.rage += random.randint(2,6)
              $ game.rape.arms=False
          else: # Согласна
            game.girl.third '[game.girl.name] отчётливо сглатывает, когда маленький дракончик берёт её ладони своими крошечными лапками.'
            $ game.rape.arms=False
        elif game.rape.size == 2: # Средний дракон
          if not game.girl.willing:
            game.girl.third '[game.girl.name] в ужасе от обвившегося вокруг неё дракона. Она сражается вполсилы.'
            $ game.rape.rage += random.randint(0,4)
          else: # Согласна
            game.girl.third '[game.girl.name] отчётливо сглатывает, когда дракон берёт её ладони своими лапами.'
          $ game.rape.arms=False
        elif game.rape.size == 3: # Матёрый драконище
          if not game.girl.willing:
            game.girl.third '[game.girl.name] в ужасе от обвившегося вокруг неё дракона. Его размер настолько велик, что её воля к сопротивлению практически парализована.'
            $ game.rape.rage += random.randint(0,2)
          else: # Согласна
            game.girl.third '[game.girl.name] отчётливо сглатывает, когда её ладони тонут в огромных лапах дракона.'
          $ game.rape.arms=False

      elif ratio_proud>0 and ratio_proud <=0.33:  # Заламывает руки и умоляет прекратить
        if not game.girl.willing:
          game.girl.third '[game.girl.name] умоляет дракона её отпустить, но не слишком убедительно. Похоже, ей и самой интересно, что же будет дальше. [game.dragon.name] берёт её за руки без всякого сопротивления.'
        else: # Согласна
          if game.rape.size == 1: # Миниатюрный дракончик
            game.girl.third 'Счастливо улыбаясь, [game.girl.name] берёт своими ладонями лапки дракона.'
          elif game.rape.size == 2: # Средний дракон
            game.girl.third 'Счастливо улыбаясь, [game.girl.name] вкладывает ладони в лапы дракона.'
          elif game.rape.size == 3: # Матёрый драконище
            game.girl.third 'Очень аккуратно [game.girl.name] вкладывает ладони в огромные лапы дракона.'
        $ game.rape.arms=False
      elif ratio_proud==0:
        if game.girl.blind:
          game.girl.third ' [game.girl.name] безучастно смотрит в пустоту отсутствующими глазами и ни на что не реагирует. '
        else:
          game.girl.third ' [game.girl.name] безучастно смотрит в пустоту и ни на что не реагирует. '
        $ game.rape.arms=False
    call screen penetration_sex
    return


label lb_rape_broken:  # Пленница полностью сломлена
    if game.rape.erection == 0:
      if game.girl.blind:
        game.girl.third '[game.girl.name] безучастно стоит на месте, уставившись в пространство выколотыми глазами'
      else:
        game.girl.third '[game.girl.name] безучастно стоит на месте, уставившись в пространство невидящим взглядом'
      $ game.rape.erection += 1
    elif game.rape.erection == 1:
      if game.girl.virgin:
        game.girl.third '[game.girl.name] никак не реагирует, когда драконий уд впервые проникает в её лоно.'
      else:
        game.girl.third '[game.girl.name] никак не реагирует, когда драконий уд вновь проникает в её кровоточащее лоно.'
      call lb_rape_women from _call_lb_rape_women_14
    elif game.rape.erection == 2:
      game.girl.third 'От мощных толчков дракона [game.girl.name] механически болтается взад-вперёд'
      $ game.rape.erection += 1
    elif game.rape.erection == 3:
     if game.girl.type == 'afrodita':
       game.girl.third 'Когда горячее драконье семя заливает лоно Афродиты, богиня резко вздыхает, как будто очнувшись ото сна'
       $ game.history = historical( name='afrodita_broken',end_year=game.year+1,desc=None,image=None)
       $ game.history_mod.append(game.history)
     else:
       game.girl.third 'Когда горячее драконье семя заливает лоно девушки, на её лице не отражается ни единой эмоции'

     $ game.rape.erection += 1
    return

label lb_rape_dragon_penis:  # Дракону досталось по самому чувствительному месту
    game.dragon 'Больнооо!!!'
    game.dragon.third 'От резкой и внезапной боли [game.dragon.name] отпускает пленницу. [game.girl.name] отпрыгивает в сторону и шипит рассержанной тигрицей.'
    game.girl 'Ну, давай же, убей меня, гад!!!'
    $ game.rape.define_freedom()
    $ game.rape.rage += random.randint(20,30)
    if game.rape.rage < 50:
      game.dragon 'Да я тебе руки-ноги поотрываю, тварь!'
      $ game.rape.fail=True
    else:
      game.dragon 'Сожру!!!'
    return

label lb_rape_fail:
    game.girl 'Выкусил? Ну, давай же, убей меня, гад!!!'
    game.dragon 'Да я тебе руки-ноги поотрываю, тварь!'
    $ game.rape.define_freedom()
    $ game.rape.rage += random.randint(20,30)
    $ game.rape.fail=True
    return 

label lb_rape_end:
    $ description = game.girls_list.rape_impregnate()
    if not game.girl.type == 'afrodita' and not game.girl.type == 'danu' and not game.girl.type == 'jasmine':
      stop music fadeout 1.0
    $ current_image=sex_imgs(game.girl.sex_expression)
    show expression current_image as xxx
    if game.girl.cripple:
      $ game.girl.cripple_image=current_image
    play sound get_random_file("sound/sex")
    pause (500.0)
    stop sound fadeout 1.0
    hide xxx
    return

label lb_rape_escape: # Побег из лап дракона
    python:
        text = u'Изнасилованная, но не понёсшая отродья %s не иначе как чудом спасается прямо из лап дракона и благополучно возвращается домой.\n\n' % (game.girl.name)
        game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
        game.girl.dead = True   # Чтобы корректно выйти из программы
        game.girls_list.free_list.append(game.girl)
    return

# Потрея девственности
label lb_rape_women:
    if not girls_data.girls_info[game.girl.type]['giantess']:
      if game.girl.virgin:
        game.girl.third 'Ну вот [game.girl.name] и стала женщиной!'
      else:
        game.girl.third 'Драконий уд повторно входит в кровоточащее лоно жертвы.'
    else:
      game.girl.third 'Ну вот великанша и познала любовь дракона!'
    $ game.rape.erection += 1
    $ game.girl.virgin = False
    return

# Принуждение
label lb_bdsm_breast_clutches:   # Оторвать грудь когтями
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_2
    game.dragon.third '[game.dragon.name] с удовольствием лапает полную, упругую, приятную на ощупь грудь.'
    game.girl 'Он же там просто потрогает? Или помнёт? Или хотя бы поцарапает?! Или...'
    game.dragon.third '[game.dragon.name] неспешно вытягивает бритвенно-острые когти. Они способны вскрыть рыцаря в полной броне, что уж говорить о мягкой, податливой девичьей плоти! [game.dragon.name] отрывает грудь медленно, аккуратно, наслаждаясь каждым мгновением безумно приятного процесса.  '
    play sound get_random_file("sound/pain") 
    if game.rape.breast=='left':
        $ add_image=rape.relative_path + "/button_left_breast_done.png"
        show expression add_image as left_breast with vpunch_long
    elif game.rape.breast=='right':
        $ add_image=rape.relative_path + "/button_right_breast_done.png"
        show expression add_image as right_breast with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Грудь, которую должен был ласкать её суженый, к которой должно было припасть её дитя - скрывается в пасти дракона.'    
    $ game.rape.actual_health -= random.randint(30,40)
    $ game.rape.actual_proud -= random.randint(15,25)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_2
    else:
      game.dragon 'Кину-ка я целебное заклинание, а то ещё кровью истечёт.'
      if game.girl.blind:
        game.girl.third '[game.girl.name] поражённо щупает огромный, уродливый, дёргающий болью шрам. Похоже, она до сих пор не осознала произошедшего. '
      else:
        game.girl.third '[game.girl.name] поражённо смотрит на огромный, уродливый, дёргающий болью шрам. Похоже, она до сих пор не осознала произошедшего. '
      $ game.rape.clutches=False
      $ game.rape.clutches_used=True
      if game.rape.breast=='left':
        $ game.rape.left_breast=False
      elif game.rape.breast=='right':
        $ game.rape.right_breast=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_2
      call screen bdsm_sex
    return

# Принуждение
label lb_bdsm_breast_tongue:   # Полизать
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show
    game.dragon.third '[game.dragon.name] с удовольствием лапает полную, упругую, приятную на ощупь грудь.'
    game.girl 'Он же там просто потрогает? Или помнёт? Или хотя бы поцарапает?! Или...'
    game.dragon.third '[game.dragon.name] неспешно вытягивает сладкий шершавый язык. О касании этого языка девушка будет помнить всю оставшуюся жизнь! [game.dragon.name] ласкает грудь медленно, аккуратно, наслаждаясь каждым мгновением безумно приятного процесса.  '
    play sound get_random_file("sound/sex") 
    if game.rape.breast=='left':
        $ add_image=rape.relative_path + "/button_left_breast_done.png"
        show expression add_image as left_breast with vpunch_long
    elif game.rape.breast=='right':
        $ add_image=rape.relative_path + "/button_right_breast_done.png"
        show expression add_image as right_breast with vpunch_long
    game.girl 'Ах!!! Ах!!! Ах!!!'   
    game.girl.third '[game.girl.name] подёргивается от удовольствия. Грудь, которую должен был ласкать её суженый, к которой должно было припасть её дитя - эта грудь испытывает то, что больше не испытает никогда: особое прикосновение драконьего языка!'    

    $ [girlW, girlQ] = game.dragon.attractiveness(game.girl)

    $ game.dragon.drain_energy(girlQ+1, True)
    $ game.rape.actual_proud -= 5 + girlQ*5
    if game.rape.actual_proud <= 1:
        $ game.rape.actual_proud = 1
        $ game.girl.willing = True
    if game.dragon.lust < 3:
        $ game.dragon.lust+=1

    call lb_bdsm_hide from _call_lb_bdsm_hide_2
    call screen bdsm_sex
    return

# Принуждение
label lb_bdsm_head_tongue:   # Полизать
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show
    game.dragon.third '[game.dragon.name] с удовольствием лижет губы девушки. Неспешно, он пробирается внутрь рта и касается её языка.'

    play sound get_random_file("sound/sex") 
    game.girl 'Ах!!! Ах!!! Ах!!!'   
    
    $ [girlW, girlQ] = game.dragon.attractiveness(game.girl)

    $ game.dragon.drain_energy(girlQ+1, True)
    $ game.rape.actual_proud -= 5 + girlQ*5
    if game.rape.actual_proud <= 1:
        $ game.rape.actual_proud = 1
        $ game.girl.willing = True
        game.girl.third '[game.girl.name] на седьмом небе от счастья и уже забыла, где находится.'    
    else:
        game.girl.third '[game.girl.name] на седьмом небе от счастья.'
    if game.dragon.lust < 3:
        $ game.dragon.lust+=1

    call lb_bdsm_hide from _call_lb_bdsm_hide_2
    call screen bdsm_sex
    return

# @fdsc и выше
# Принуждение
label lb_bdsm_pussy_tongue:   # Полизать

    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show
    game.dragon.third '[game.dragon.name] с удовольствием пробирается языком между ног девушки и приоткрывает половые губы.'
    game.girl 'Он же не лишит меня девственности языком?'
    game.dragon.third '[game.dragon.name] слышыт сладкие стоны девушки '
    play sound get_random_file("sound/sex") 

    game.girl 'А-а-а!!! А-а-а!!! А-а-а!!!'   
    game.girl.third '[game.girl.name] изгибается от невыносимого удовольствия.'    

    $ [girlW, girlQ] = game.dragon.attractiveness(game.girl)
    $ game.dragon.drain_energy(girlQ+2, True)
    $ game.rape.actual_proud -= 10 + girlQ*5
    if game.rape.actual_proud <= 1:
        $ game.rape.actual_proud = 1
        $ game.girl.willing = True
    if game.dragon.lust < 3:
        $ game.dragon.lust+=1

    call lb_bdsm_hide from _call_lb_bdsm_hide_2
    call screen bdsm_sex
    return

label lb_bdsm_breast_fangs:   # Откусить грудь клыками
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_3
    game.dragon.third '[game.dragon.name] с удовольствием облизывает полную, упругую, приятную на ощупь грудь.'
    game.girl 'Он же там просто полижет? Или пососёт? Или...'
    game.dragon.third '[game.dragon.name] засовывает грудь в пасть и начинает неспешно сжимать зубы. Вкусняшка лопается в его рту, как сочная и зрелая ягода. [game.dragon.name] облизывается. Вкусно, но мало! '
    play sound get_random_file("sound/pain") 
    if game.rape.breast=='left':
        $ add_image=rape.relative_path + "/button_left_breast_done.png"
        show expression add_image as left_breast with vpunch_long
    elif game.rape.breast=='right':
        $ add_image=rape.relative_path + "/button_right_breast_done.png"
        show expression add_image as right_breast with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Грудь, которую должен был ласкать её суженый, к которой должно было припасть её дитя - скрылась в пасти дракона.'    
    $ game.rape.actual_health -= random.randint(30,40)
    $ game.rape.actual_proud -= random.randint(15,25)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_3
    else:
      game.dragon 'Кину-ка я целебное заклинание, а то ещё кровью истечёт.'
      if game.girl.blind:
        game.girl.third '[game.girl.name] поражённо щупает огромный, уродливый, дёргающий болью шрам. Похоже, она до сих пор не осознала произошедшего. '
      else:
        game.girl.third '[game.girl.name] поражённо смотрит на огромный, уродливый, дёргающий болью шрам. Похоже, она до сих пор не осознала произошедшего. '
      $ game.rape.fangs=False
      $ game.rape.fangs_used=True
      if game.rape.breast=='left':
        $ game.rape.left_breast=False
      elif game.rape.breast=='right':
        $ game.rape.right_breast=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_3
      call screen bdsm_sex
    return

label lb_bdsm_breast_fire:   # Обжечь грудь огнём
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_1
    game.dragon.third '[game.dragon.name] неспешно склоняется над полной, упругой, приятной на ощупь грудью'
    game.girl 'Он же там просто полижет? Или помнёт? Или...'
    game.dragon.third '[game.dragon.name] аккуратно выдыхает струю не самого жаркого пламени. '
    play sound get_random_file("sound/pain") 
    if game.rape.breast=='left':
        $ add_image=rape.relative_path + "/button_left_breast_done.png"
        show expression add_image as left_breast with vpunch_long
    elif game.rape.breast=='right':
        $ add_image=rape.relative_path + "/button_right_breast_done.png"
        show expression add_image as right_breast with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Мягкая нетронутая кожа стремительно краснеет и покрывается волдырями.'    
    $ game.rape.actual_health -= random.randint(10,20)
    $ game.rape.actual_proud -= random.randint(10,20)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_1
    else:
      game.dragon 'Ничего страшного. Ожог второй степени... в крайнем случае - третьей.'
      game.girl.third '[game.girl.name] плачет и скулит от боли. Заживать будет долго. '
      $ game.rape.fire=False
      $ game.rape.fire_used=True
      if game.rape.breast=='left':
        $ game.rape.left_breast=False
      elif game.rape.breast=='right':
        $ game.rape.right_breast=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_1
      call screen bdsm_sex
    return

label lb_bdsm_breast_ice:   # Обморозить грудь холодом
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_4
    game.dragon.third '[game.dragon.name] неспешно склоняется над полной, упругой, приятной на ощупь грудью'
    game.girl 'Он же там просто полижет? Или помнёт? Или...'
    game.dragon.third '[game.dragon.name] аккуратно выдыхает облако не самого морозного воздуха. '
    play sound get_random_file("sound/pain") 
    if game.rape.breast=='left':
        $ add_image=rape.relative_path + "/button_left_breast_done.png"
        show expression add_image as left_breast with vpunch_long
    elif game.rape.breast=='right':
        $ add_image=rape.relative_path + "/button_right_breast_done.png"
        show expression add_image as right_breast with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Мягкая нетронутая кожа стремительно краснеет и покрывается волдырями - строго говоря, это не обморожение, а ожог, только холодный.'    
    $ game.rape.actual_health -= random.randint(10,20)
    $ game.rape.actual_proud -= random.randint(10,20)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_4
    else:
      game.dragon 'Ничего страшного. Холодный ожог второй степени... в крайнем случае - третьей.'
      game.girl.third '[game.girl.name] плачет и скулит от боли. Заживать будет долго. '
      $ game.rape.ice=False
      $ game.rape.ice_used=True
      if game.rape.breast=='left':
        $ game.rape.left_breast=False
      elif game.rape.breast=='right':
        $ game.rape.right_breast=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_4
      call screen bdsm_sex
    return

label lb_bdsm_breast_lightning:   # Ударить в грудь электричеством
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_5
    game.dragon.third '[game.dragon.name] неспешно склоняется над полной, упругой, приятной на ощупь грудью'
    game.girl 'Он же там просто полижет? Или помнёт? Или...'
    game.dragon.third '[game.dragon.name] аккуратно выдыхает сноп электрических искр. '
    play sound get_random_file("sound/pain") 
    if game.rape.breast=='left':
        $ add_image=rape.relative_path + "/button_left_breast_done.png"
        show expression add_image as left_breast with vpunch_long
    elif game.rape.breast=='right':
        $ add_image=rape.relative_path + "/button_right_breast_done.png"
        show expression add_image as right_breast with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Визуальных эффектов от удара миниатюрной молнией нет - но девушке от этого ни капельки не легче.'    
    $ game.rape.actual_health -= random.randint(5,15)
    $ game.rape.actual_proud -= random.randint(15,25)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_5
    else:
      game.dragon 'Крайне болезненно и практически безопасно. Идеальный вариант'
      if game.girl.blind:
        game.girl.third '[game.girl.name] скулит от непереносимой боли и мотает безглазой головой. Наверное, оторви дракон грудь - и то было бы легче. '
      else:
        game.girl.third '[game.girl.name] скулит от непереносимой боли и с ужасом смотрит на своего мучителя. Наверное, оторви он грудь - и то было бы легче. '
      $ game.rape.lightning=False
      $ game.rape.lightning_used=True
      if game.rape.breast=='left':
        $ game.rape.left_breast=False
      elif game.rape.breast=='right':
        $ game.rape.right_breast=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_5
      call screen bdsm_sex
    return

label lb_bdsm_breast_poison:   # Обморозить грудь холодом
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_6
    game.dragon.third '[game.dragon.name] неспешно склоняется над полной, упругой, приятной на ощупь грудью'
    game.girl 'Он же там просто полижет? Или помнёт? Или...'
    game.dragon.third '[game.dragon.name] аккуратно выдыхает облако не самого жгучего яда. '
    play sound get_random_file("sound/pain") 
    if game.rape.breast=='left':
        $ add_image=rape.relative_path + "/button_left_breast_done.png"
        show expression add_image as left_breast with vpunch_long
    elif game.rape.breast=='right':
        $ add_image=rape.relative_path + "/button_right_breast_done.png"
        show expression add_image as right_breast with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Мягкая нетронутая кожа стремительно чернеет и покрывается струпьями.'    
    $ game.rape.actual_health -= random.randint(10,20)
    $ game.rape.actual_proud -= random.randint(10,20)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_6
    else:
      game.dragon 'Ничего страшного, небольшой токсигенный некроз. Такой строптивице он очень к лицу!'
      game.girl.third '[game.girl.name] плачет и скулит от боли. Ей очень повезёт, если грудь вообще ккогда-нибудь заживёт. '
      $ game.rape.poison=False
      $ game.rape.poison_used=True
      if game.rape.breast=='left':
        $ game.rape.left_breast=False
      elif game.rape.breast=='right':
        $ game.rape.right_breast=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_6
      call screen bdsm_sex
    return

label lb_bdsm_breast_string:   # Обморозить грудь холодом
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_7
    game.dragon.third '[game.dragon.name] ласкает полную, упругую, приятную на ощупь грудь кончиком хвоста'
    game.girl 'Он же там просто погладит? Или помнёт? Или...'
    game.dragon.third '[game.dragon.name] неспешно вводит под кожу острое жало и начинает впрыскивать жгучий яд. '
    play sound get_random_file("sound/pain") 
    if game.rape.breast=='left':
        $ add_image=rape.relative_path + "/button_left_breast_done.png"
        show expression add_image as left_breast with vpunch_long
    elif game.rape.breast=='right':
        $ add_image=rape.relative_path + "/button_right_breast_done.png"
        show expression add_image as right_breast with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке, орёт от боли и пытается выдернуть жало - безуспешно, разумеется. Грудь неторопливо и страшно раздувается.'    
    $ game.rape.actual_health -= random.randint(30,40)
    $ game.rape.actual_proud -= random.randint(15,25)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_7
    else:
      game.dragon 'Что-то я не рассчитал, как бы анафилактический шок не начался... а, ладно, пронесло'
      game.girl.third '[game.girl.name] плачет и скулит от боли. Повреждённая грудь похожа на огромную красную тыкву, причиняющую невыносимые страдания. Она умоляет ящера откусить её, но [game.dragon.name] только скалится в ответ. '
      $ game.rape.string=False
      $ game.rape.string_used=True
      if game.rape.breast=='left':
        $ game.rape.left_breast=False
      elif game.rape.breast=='right':
        $ game.rape.right_breast=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_7
      call screen bdsm_sex
    return


# Голова
label lb_bdsm_head_clutches:   # Выколоть глаза когтями
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_8
    game.dragon.third '[game.dragon.name] одной лапой прижимает голову пленницы к полу и подносит вторую лапу к её голове. Он неспешно шевелит плаьцами с длинными, бритвенно-острыми когтями.'
#    game.girl 'Ой! Текущая версия игры не поддерживает инвалидок! Давай мы только сделаем вид, что ты выколол мне глаза?'
#    game.dragon 'Ну, давай...'
    if game.girl.type=='peasant' or game.girl.type == 'citizen' or game.girl.type == 'princess':
      game.girl 'Господи, не глаза! Только не глаза!!!'
    elif game.girl.type=='elf':
      game.girl 'Дану, не глаза! Только не глаза!!!'
    elif game.girl.type=='mermaid' or game.girl.type=='siren':
      game.girl 'Дагон, не глаза! Только не глаза!!!'
    elif game.girl.type=='titan':
      game.girl 'Боги, не глаза! Только не глаза!!!'
    elif game.girl.type=='jasmine':
      game.girl 'Хочешь - выкалывай. Видеть тебя не могу!'
    else:
      game.girl 'Не глаза! Только не глаза!!!'
    game.dragon.third '[game.dragon.name] аккуратно отодвигает веки и  неспешно вонзает когти прямо в глазные яблоки жертвы.   '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_head_done.png"
    show expression add_image as head with vpunch_long
    $ game.rape.blind_avatar()
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке как сумасшедшая и орёт от боли и отчаяния. Свет мира для неё померк навсегда.'    
    $ game.rape.actual_health -= random.randint(30,40)
    $ game.rape.actual_proud -= random.randint(25,35)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_8
    else:
      game.dragon 'Отлично! И покорнее станет, и не убежит никуда. Одно слабенькое целебное заклинание, чтобы пустые глазницы зажили.'
      game.girl.third '[game.girl.name] скулит, прижимая ладони к безглазому лицу. Произошедшее стало для неё колоссальным ударом. '
      $ game.rape.clutches=False
      $ game.rape.clutches_used=True
      $ game.girl.blind = True
      $ game.rape.head=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_8
      call screen bdsm_sex
    return

label lb_bdsm_head_fear:   # Напугать пленницу своим видом
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_9
    game.dragon.third '[game.dragon.name] пристально смотрит в глаза пленницы. До этого девушка не раз видела дракона - но ни разу не присматривалась к нему по-настоящему.'
    game.girl 'Нет... Нет, нет, нет. НЕЕЕЕТ!!!'
    game.dragon.third 'Истинный облик чудовища способен внушить ужас даже самым бесстрашным существам...  '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_head_done.png"
    show expression add_image as head with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] орёт от чистого, первобытного ужаса. Её маленькое сердечко заполошно бьётся с невероятной скоростью'    
    $ game.rape.actual_health -= random.randint(0,10)
    $ game.rape.actual_proud -= random.randint(25+game.dragon.fear,35+game.dragon.fear*2)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_9
    else:
      game.dragon 'Лучше и не бывает! И напугал, и игрушку не сломал... правда, чуть сердечный приступ не случился.'
      game.girl.third '[game.girl.name] сжимается в комок и скулит от пережитого ужаса. '
      $ game.rape.fear=False
      $ game.rape.fear_used=True
      $ game.rape.head=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_9
      call screen bdsm_sex
    return

label lb_bdsm_head_horns:   # Выколоть глаза рогами
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_10
    game.dragon.third '[game.dragon.name] лапой прижимает голову пленницы к полу и склоняет над ней свою голову, украшенную мощными и острыми рогами.'
#    game.girl 'Ой! Текущая версия игры не поддерживает инвалидок! Давай мы только сделаем вид, что ты выколол мне глаза?'
#    game.dragon 'Ну, давай...'
    if game.girl.type=='peasant' or game.girl.type == 'citizen' or game.girl.type == 'princess':
      game.girl 'Господи, не глаза! Только не глаза!!!'
    elif game.girl.type=='elf':
      game.girl 'Дану, не глаза! Только не глаза!!!'
    elif game.girl.type=='mermaid' or game.girl.type=='siren':
      game.girl 'Дагон, не глаза! Только не глаза!!!'
    elif game.girl.type=='titan':
      game.girl 'Боги, не глаза! Только не глаза!!!'
    elif game.girl.type=='jasmine':
      game.girl 'Хочешь - выкалывай. Видеть тебя не могу!'
    else:
      game.girl 'Не глаза! Только не глаза!!!'
    game.dragon.third '[game.dragon.name] аккуратно отодвигает веки и неспешно вонзает кончики рогов прямо в глазные яблоки жертвы.   '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_head_done.png"
    show expression add_image as head with vpunch_long
    $ game.rape.blind_avatar()
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке как сумасшедшая и орёт от боли и отчаяния. Свет мира для неё померк навсегда.'    
    $ game.rape.actual_health -= random.randint(30,40)
    $ game.rape.actual_proud -= random.randint(25,35)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_10
    else:
      game.dragon 'Отлично! И покорнее станет, и не убежит никуда. Одно слабенькое целебное заклинание, чтобы пустые глазницы зажили.'
      game.girl.third '[game.girl.name] скулит, прижимая ладони к безглазому лицу. Произошедшее стало для неё колоссальным ударом. '
      $ game.rape.horns=False
      $ game.rape.horns_used=True
      $ game.girl.blind = True

      $ game.rape.head=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_10
      call screen bdsm_sex
    return

label lb_bdsm_head_sound:   # Выколоть глаза рогами
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_11
    game.dragon.third '[game.dragon.name] склоняется над пленницей.'
    game.girl 'Что, сожрать меня решил, зверюга?!'
    game.dragon.third '[game.dragon.name] открывает пасть и издаёт негромкий рёв. Ну, более тихий, чем в бою. '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_head_done.png"
    show expression add_image as head with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] орёт и изо всех сил зажимает уши ладонями'    
    $ game.rape.actual_health -= random.randint(5,15)
    $ game.rape.actual_proud -= random.randint(10,20)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_11
    else:
      game.dragon 'Хорошо! Правда, пленница чуть контузию не заработала, но это мелочи'
      game.girl.third '[game.girl.name] скулит, прижимая ладони к ушам. Судя по всему, слух вернётся к ней нескоро.'
      $ game.rape.sound=False
      $ game.rape.sound_used=True
      $ game.rape.head=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_11
      call screen bdsm_sex
    return

# Живот
label lb_bdsm_stomach_fire:   # Обжечь живот огнём
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_12
    game.dragon.third '[game.dragon.name] неспешно склоняется над упругим, приятным на ощупь животиком'
    game.girl 'Он же там просто полижет? Или помнёт? Или...'
    game.dragon.third '[game.dragon.name] аккуратно выдыхает струю не самого жаркого пламени. '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_stomach_done.png"
    show expression add_image as stomach with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Мягкая нетронутая кожа стремительно краснеет и покрывается волдырями.'    
    $ game.rape.actual_health -= random.randint(10,20)
    $ game.rape.actual_proud -= random.randint(10,20)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_12
    else:
      game.dragon 'Ничего страшного. Ожог второй степени... в крайнем случае - третьей.'
      game.girl.third '[game.girl.name] плачет и скулит от боли. Заживать будет долго. '
      $ game.rape.fire=False
      $ game.rape.fire_used=True
      $ game.rape.stomach=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_12
      call screen bdsm_sex
    return

label lb_bdsm_stomach_ice:   # Обморозить живот холодом
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_13
    game.dragon.third '[game.dragon.name] неспешно склоняется над упругим, приятным на ощупь животиком'
    game.girl 'Он же там просто полижет? Или помнёт? Или...'
    game.dragon.third '[game.dragon.name] аккуратно выдыхает облако не самого морозного воздуха. '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_stomach_done.png"
    show expression add_image as stomach with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Мягкая нетронутая кожа стремительно краснеет и покрывается волдырями - строго говоря, это не обморожение, а ожог, только холодный.'    
    $ game.rape.actual_health -= random.randint(10,20)
    $ game.rape.actual_proud -= random.randint(10,20)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_13
    else:
      game.dragon 'Ничего страшного. Холодный ожог второй степени... в крайнем случае - третьей.'
      game.girl.third '[game.girl.name] плачет и скулит от боли. Заживать будет долго. '
      $ game.rape.ice=False
      $ game.rape.ice_used=True
      $ game.rape.stomach=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_13
      call screen bdsm_sex
    return

label lb_bdsm_stomach_lightning:   # Ударить в грудь электричеством
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_14
    game.dragon.third '[game.dragon.name] неспешно склоняется над упругим, приятным на ощупь животиком'
    game.girl 'Он же там просто полижет? Или помнёт? Или...'
    game.dragon.third '[game.dragon.name] аккуратно выдыхает сноп электрических искр. '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_stomach_done.png"
    show expression add_image as stomach with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Визуальных эффектов от удара миниатюрной молнией нет - но девушке от этого ни капельки не легче.'    
    $ game.rape.actual_health -= random.randint(5,15)
    $ game.rape.actual_proud -= random.randint(15,25)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_14
    else:
      game.dragon 'Крайне болезненно и практически безопасно. Идеальный вариант'
      if game.girl.blind:
        game.girl.third '[game.girl.name] скулит от непереносимой боли и мотает безглазой головой.'
      else:
        game.girl.third '[game.girl.name] скулит от непереносимой боли, сжимается в комок и с ужасом смотрит на своего мучителя. '
      $ game.rape.lightning=False
      $ game.rape.lightning_used=True
      $ game.rape.stomach=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_14
      call screen bdsm_sex
    return

label lb_bdsm_stomach_poison:   # Выдохнуть на живот ядовитое облако
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_15
    game.dragon.third '[game.dragon.name] неспешно склоняется над полным и рыхловатым животиком. [game.dragon.name] всегда предпочитал пышек - там мяса больше!'
    game.girl 'Он же там просто полижет? Или помнёт? Или...'
    game.dragon.third '[game.dragon.name] аккуратно выдыхает облако не самого жгучего яда. '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_stomach_done.png"
    show expression add_image as stomach with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Мягкая нетронутая кожа стремительно чернеет и покрывается струпьями.'    
    $ game.rape.actual_health -= random.randint(15,25)
    $ game.rape.actual_proud -= random.randint(10,20)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_15
    else:
      game.dragon 'Ничего страшного, небольшой токсигенный некроз. Хорошо, что у этой пышки жира много, есть чему отмирать!'
      game.girl.third '[game.girl.name] плачет и скулит от боли. Дракон присмотрит, чтобы у неё не начался сепсис... наверное.'
      $ game.rape.poison=False
      $ game.rape.poison_used=True
      $ game.rape.stomach=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_15
      call screen bdsm_sex
    return

# Лоно
label lb_bdsm_pussy_clutches:   # Оторвать клитор когтями
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_16
    game.dragon.third '[game.dragon.name] с удовольствием лапает нежную, девственную щёлку пленницы'
    game.girl 'Соблазнять меня вздумал, зверюга?!'
    game.dragon.third '[game.dragon.name] касается бритвенно-острым когтем нежного бугорка, ещё не знавшего мужской ласки. Одно слитное движение - и клитор отправляется в рот дракона. '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_pussy_done.png"
    show expression add_image as pussy with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] орёт от боли и прижимает ладонь к паху. Кажется, в будущем она будет весьма фригидной... если доживёт до этого "будущего", конечно!'    
    $ game.rape.actual_health -= random.randint(10,20)
    $ game.rape.actual_proud -= random.randint(15,25)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_16
    else:
      game.dragon 'Кину-ка я целебное заклинание, а то заживать долго будет.'
      if game.girl.blind:
        game.girl.third '[game.girl.name] поражённо щупает своё лоно и поскуливает от боли. Кажется, она ещё точно не поняла, что произошло... но осознала, что что-то очень скверное.' 
      else:
        game.girl.third '[game.girl.name] поражённо взирает на своё лоно и поскуливает от боли. Кажется, она ещё точно не поняла, что произошло... но осознала, что что-то очень скверное.'
      $ game.rape.clutches=False
      $ game.rape.clutches_used=True
      $ game.rape.pussy=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_16
      call screen bdsm_sex
    return

label lb_bdsm_pussy_fire:
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_17
    game.dragon.third '[game.dragon.name] неспешно склоняется над девственной щёлочкой пленницы'
    game.girl 'Он же там просто полижет? Или помнёт? Или...'
    game.dragon.third '[game.dragon.name] аккуратно выдыхает крошечную струйку не самого жаркого пламени. '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_pussy_done.png"
    show expression add_image as pussy with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Волосы на лобке загораются, клитор вспучивается, половые губы стремительно краснеют и покрываются волдырями.'    
    $ game.rape.actual_health -= random.randint(10,20)
    $ game.rape.actual_proud -= random.randint(10,20)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_17
    else:
      game.dragon 'Ничего страшного. Ожог второй степени... в крайнем случае - третьей.'
      game.girl.third '[game.girl.name] плачет и скулит от боли. Заживать будет долго. '
      $ game.rape.fire=False
      $ game.rape.fire_used=True
      $ game.rape.pussy=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_17
      call screen bdsm_sex
    return

label lb_bdsm_pussy_ice:   # Обморозить лоно холодом
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_18
    game.dragon.third '[game.dragon.name] неспешно склоняется над девственной щёлочкой пленницы'
    game.girl 'Он же там просто полижет? Или помнёт? Или...'
    game.dragon.third '[game.dragon.name] аккуратно выдыхает крошечную струйку не самого морозного воздуха. '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_pussy_done.png"
    show expression add_image as pussy with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Волосы на лобке покрываются инеем, клитор сморщивается, половые губы краснеют и вспучиваются волдырями - строго говоря, это не обморожение, а ожог, только холодный.'    
    $ game.rape.actual_health -= random.randint(10,20)
    $ game.rape.actual_proud -= random.randint(10,20)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_18
    else:
      game.dragon 'Ничего страшного. Холодный ожог второй степени... в крайнем случае - третьей.'
      game.girl.third '[game.girl.name] плачет и скулит от боли. Заживать будет долго. '
      $ game.rape.ice=False
      $ game.rape.ice_used=True
      $ game.rape.pussy=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_18
      call screen bdsm_sex
    return

label lb_bdsm_pussy_lightning:   # Ударить в грудь электричеством
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_19
    game.dragon.third '[game.dragon.name] неспешно склоняется над девственной щёлочкой пленницы'
    game.girl 'Он же там просто полижет? Или помнёт? Или...'
    game.dragon.third '[game.dragon.name] аккуратно выдыхает сноп электрических искр. '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_pussy_done.png"
    show expression add_image as pussy with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Визуальных эффектов от удара миниатюрной молнией нет - но девушке от этого ни капельки не легче.'    
    $ game.rape.actual_health -= random.randint(5,15)
    $ game.rape.actual_proud -= random.randint(15,25)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_19
    else:
      game.dragon 'Крайне болезненно и практически безопасно. Идеальный вариант'
      if game.girl.blind:
        game.girl.third '[game.girl.name] скулит от непереносимой боли и мотает безглазой головой.'
      else:
        game.girl.third '[game.girl.name] скулит от непереносимой боли, сжимается в комок и с ужасом смотрит на своего мучителя. '
      $ game.rape.lightning=False
      $ game.rape.lightning_used=True
      $ game.rape.pussy=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_19
      call screen bdsm_sex
    return

label lb_bdsm_pussy_poison:   # Выдохнуть на живот ядовитое облако
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_20
    game.dragon.third '[game.dragon.name] неспешно склоняется над девственной щёлочкой пленницы'
    game.girl 'Он же там просто полижет? Или помнёт? Или...'
    game.dragon.third '[game.dragon.name] аккуратно выдыхает облако не самого жгучего яда. '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_pussy_done.png"
    show expression add_image as pussy with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке и орёт от боли. Волосы на лобке слезают, половые губы и клитор чернеют и покрываются струпьями.'    
    $ game.rape.actual_health -= random.randint(10,20)
    $ game.rape.actual_proud -= random.randint(10,20)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_20
    else:
      game.dragon 'Ничего страшного, небольшой токсигенный некроз. В крайнем случае отомрут половые губы и клитор. Сущие мелочи!'
      game.girl.third '[game.girl.name] плачет и скулит от боли. Ей очень повезёт, если её лоно вообще когда-нибудь заживёт. '
      $ game.rape.poison=False
      $ game.rape.poison_used=True
      $ game.rape.pussy=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_20
      call screen bdsm_sex
    return

label lb_bdsm_pussy_string:   # Обморозить грудь холодом
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
    call lb_bdsm_show from _call_lb_bdsm_show_21
    game.dragon.third '[game.dragon.name] теребит бугорок наслаждения кончиком хвоста'
    game.girl 'Соблазнять меня вздумал, зверюга?!'
    game.dragon.third '[game.dragon.name] неспешно возает в клитор острое жало и начинает впрыскивать жгучий яд. '
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_pussy_done.png"
    show expression add_image as pussy with vpunch_long
    game.girl 'Аааа!!!'   
    game.girl.third '[game.girl.name] бьётся в припадке, орёт от боли и пытается выдернуть жало - безуспешно, разумеется. Клитор неторопливо и страшно раздувается.'    
    $ game.rape.actual_health -= random.randint(20,30)
    $ game.rape.actual_proud -= random.randint(15,25)
    if game.rape.actual_health<0:
      call lb_rape_dead from _call_lb_rape_dead_21
    else:
      game.dragon 'Что-то я не рассчитал, как бы анафилактический шок не начался... да и если бы яд дошёл до матки, игрушка стала бы бесплодной... а, ладно, пронесло'
      game.girl.third '[game.girl.name] плачет и скулит от боли. Повреждённый клитор похож на огромный красный абрикос, причиняющий невыносимые страдания. Она умоляет ящера оторвать его, но [game.dragon.name] только скалится в ответ. '
      $ game.rape.string=False
      $ game.rape.string_used=True
      $ game.rape.pussy=False
      if game.girl.willing:
        game.dragon.third 'Что же, теперь о добровольности не может идти и речи!'
        $ game.girl.willing = False
      call lb_bdsm_hide from _call_lb_bdsm_hide_21
      call screen bdsm_sex
    return

# Оторвать руки и ноги
label lb_bdsm_cripple:   
    $ current_image = rape.relative_path + "/ground.jpg"
    hide bg
    show expression current_image as bg
    nvl clear
#    game.girl 'Ой! В текущей версии игры инвалидки не предусмотрены. Давай мы просто сделаем вид, что ты оторвал мне руки и ноги?'
#    game.dragon 'Ну, давай...'
#    $ add_image=rape.relative_path + "/button_left_breast_done.png"
#    show expression add_image as left_breast
#    $ add_image=rape.relative_path + "/button_right_breast_done.png"
#    show expression add_image as right_breast
    $ add_image=rape.relative_path + "/button_head_done.png"
    show expression add_image as head
#    $ add_image=rape.relative_path + "/button_stomach_done.png"
#    show expression add_image as stomach
    $ add_image=rape.relative_path + "/button_pussy_done.png"
    show expression add_image as pussy  
    play sound get_random_file("sound/pain") 
    $ add_image=rape.relative_path + "/button_arms_and_legs_done.png"
    show expression add_image as arms_and_legs with vpunch_long
    game.girl 'Аааа!!!' 
    if not game.girl.type == 'mermaid' and not game.girl.type == 'siren':
      game.girl.third '[game.dragon.name] жестоко отрывает непокорной пленнице руки и ноги, прокалывает уши и вырывает язык.'  
    else: 
      game.girl.third '[game.dragon.name] жестоко отрывает непокорной пленнице руки и хвост, прокалывает уши и вырывает язык.'  
    $ game.rape.actual_health -= random.randint(70,75)
    if game.rape.actual_health<0 or game.girl.blind:  # Инвалидки всегда зрячи
      game.girl.third 'Бедняжке повезло: когда [game.dragon.name] пришёл в себя, он обнаружил лишь остывающий труп.'   
      call lb_rape_dead from _call_lb_rape_dead_22
    else:
      game.girl.third 'Бедняжке не повезло: когда [game.dragon.name] пришёл в себя, она ещё дышала.'
      if game.dragon.hunger > 0:
        game.girl.third 'Подзакусив мясцом, ящер успокоился и продолжил.'
        $ description =  game.girls_list.eat_girl()
        $ game.rape.rage=0
      game.dragon.third '[game.dragon.name] с помощью магии остановил кровотечение, а потом жестоко надругался над беспомощным телом.'
      $ game.girl.cripple=True
      call lb_bdsm_hide from _call_lb_bdsm_hide_22
      call lb_rape_end  from _call_lb_rape_end
    return

label lb_bdsm_show:
    if not game.rape.left_breast:
      $ add_image=rape.relative_path + "/button_left_breast_done.png"
      show expression add_image as left_breast
    if not game.rape.right_breast:
      $ add_image=rape.relative_path + "/button_right_breast_done.png"
      show expression add_image as right_breast
    if not game.rape.head:
      $ add_image=rape.relative_path + "/button_head_done.png"
      show expression add_image as head
    if not game.rape.stomach:
      $ add_image=rape.relative_path + "/button_stomach_done.png"
      show expression add_image as stomach
    if not game.rape.pussy:
      $ add_image=rape.relative_path + "/button_pussy_done.png"
      show expression add_image as pussy
    return

label lb_bdsm_hide:
    hide head
    hide left_breast
    hide right_breast
    hide stomach
    hide pussy
    hide arms_and_legs
    return

label lb_rape_dead:
    call lb_bdsm_hide from _call_lb_bdsm_hide_666
    $ current_image = "img/scene/rape_death.jpg"
    show expression current_image
    pause (500.0)
    hide current_image
    show expression current_image as bg
    game.dragon 'Эх, жалко'
    game.dragon 'Ещё одна игрушка сломалась. А так интересно было с ней забаляться!'
    $ text = u'%s не вынесла "ухаживаний" дракона. Пытаясь сломить волю девушки, %s убил её. \n\n' % (game.girl.name,game.dragon.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('rape_death',current_image)
    $ game.girl.dead = True
    if game.dragon.hunger > 0:
      menu:
        'Подзакусить свежатинкой':
          $ description =  game.girls_list.eat_girl()
        'Да ну её':
          pass
    if not game.girl.type == 'afrodita' and not game.girl.type == 'danu' and not game.girl.type == 'jasmine':
      stop music fadeout 1.0      
    if game.girl.love is not None:
      if game.girl.love.type == 'lizardman':
        call lb_love_suicide_lizardman from _call_lb_love_suicide_lizardman_3
    return

