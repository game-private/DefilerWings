# coding=utf-8
# локация взаимодействий
init python:

    from pythoncode import focus_mask_ext
label lb_nature_sex:
    if game.girl.jailed:
        $ place = 'prison'
        show place as bg
    nvl clear
    $ room_desc='(свободных камер: %.0f)' %(game.girls_list.free_size//game.girl.size)
    if (game.girls_list.free_size-game.girl.size)<0:
      game.girl.third 'Даже как-то жаль, что девицу с собой не заберёшь - свободные камеры в логове закончились!'
    menu:
        'Надругаться' if game.girls_list.is_mating_possible:
            # Alex: Added sex images:

            call lb_nature_rape from _call_lb_nature_rape_1
            if game.girl.dead:
              return
        'Магическое уменьшение' if not game.girls_list.is_mating_possible and game.girl.virgin and not game.girls_list.is_giant and game.dragon.lust > 0 and not game.girl.old:
#            $ focus_mask_ext.create_focus_mask_data('DefilerWings-1.4.0/game/img/sex_screen/elf/red/3/coordinates.bin')   
            game.dragon 'Заклятье временного уменьшения!'
            $ game.dragon.gain_rage()
            call lb_nature_rape from _call_lb_nature_rape_2
            if game.girl.dead:
              return
        'Магический рост' if not game.girls_list.is_mating_possible and game.girl.virgin and game.girls_list.is_giant and game.dragon.mana > 0 and game.dragon.lust > 0:
            $ game.dragon.drain_mana()
            game.dragon 'Заклятье временного роста!'
            call lb_nature_rape from _call_lb_nature_rape_4
            if game.girl.dead:
              return
        'Ограбить' if game.girl.treasure:
            $ description = game.girls_list.rob_girl()
            game.girl.third "[description]"
        'Утащить в логово [room_desc]' if game.witch_st1==0 and (game.girls_list.free_size-game.girl.size)>=0:
            if game.girl.virgin:
              $ text = u'Заполучив девицу, дракон утащил бедняжку в своё логово%s. \n\n' % game.lair.type.name_locative
            else:
              $ text = u'Надругавшись над девичьим телом, дракон утащил бедняжку в своё логово%s. \n\n' % game.lair.type.name_locative
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            $ description = game.girls_list.steal_girl()
            game.girl.third "[description]"
            $ place = game.lair.type_name
            show place
            nvl clear
            $ description = game.girls_list.jail_girl()
            game.girl.third "[description]"
            return
        'Отпустить восвояси' if not game.girl.virgin:
            if game.girl.virgin:
              $ text = u'%s уже простилось с жизнью, однако в тот день, наверное, девушку хранили сами Небеса. Хорошенько помяв и обслюнявив невинное тельце, дракон отпустил девушку восвояси. Целой и невредимой... \n\n' % game.girl.name
            else:
              $ text = u'Вдоволь потешив свою похоть и излив едкое семя в нежное лоно жертвы, %s отпустил обесчещенную девицу на все четыре стороны. \n\n' % game.dragon.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            $ description = game.girls_list.free_girl()
            game.girl.third "[description]"
            python:
                game.girls_list.save_girl()    
# По-умолчанию такая девушка благополучно попадает домой. Начинаем отслеживать.
            return 
        'Сожрать' if game.dragon.hunger > 0:
            if game.girl.virgin:
              $ text = u'%s не стал насиловать девушку. Он просто-напросто сожрал её, не опасаясь возможных свидетелей. \n\n' % game.dragon.name
            else:
              $ text = u'Утолив свою похоть, %s сожрал хрупкое тельце, наслаждаясь истошными воплями поедаемой заживо жертвы.  \n\n' % game.dragon.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            call lb_eat from _call_lb_eat_1
            return
        'Разорвать на части'  if game.dragon.hunger == 0:
            game.dragon 'Любопытно, из чего же сделаны наши девчонки?!'
            nvl clear
            hide bg
            show expression "img/scene/turn_apart.jpg" 
            '[game.dragon.name] разрывает пленницу на части просто ради забавы'
            $ text = u'%s разорвал на части пленницу просто ради забавы. \n\n' % (game.dragon.name)
            game.girl.third '[text]'
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            $ game.chronik.death('turned_apart',"img/scene/turn_apart.jpg")
            return
            
    jump lb_nature_sex


label lb_lair_sex:
    $ description = game.girls_list.girl_in_prison()
    game.girl "[description]" 
    if game.girl.cripple:
      if game.girl.pregnant>0:
        'Изнасилованная, лишённая языка, слуха и конечностей, [game.girl.name] беспомощно распласталась на полу. В её чреве медленно зреет чудовищное отродье. Жизнь в [game.girl.name_p] теплится только благодаря заботам драконьих слуг. Впрочем, разве это жизнь?! '
      else:
        'Осквернённая, лишённая языка, слуха и конечностей, родившая противоестественное отродье, [game.girl.name] беспомощно распласталась на полу. Жизнь в [game.girl.name_p] теплится только благодаря заботам драконьих слуг. Впрочем, разве это жизнь?! '
#    python:
#        if game.girl.type == 'ice' or game.girl.type == 'fire' or game.girl.type == 'ogre' or game.girl.type == 'titan' or game.girl.type == 'siren':
#            renpy.jump('lb_gigant_sex')

    if game.girl.jailed:
        $ place = 'prison'
        show place as bg
    nvl clear
    menu:
        'Надругаться' if game.girls_list.is_mating_possible:
         
            call lb_lair_rape from _call_lb_lair_rape_1
            if game.girl.dead:
              return
        'Магическое уменьшение' if not game.girls_list.is_mating_possible and game.girl.virgin and not game.girls_list.is_giant and game.dragon.lust > 0 and not game.girl.old:

            game.dragon 'Заклятье временного уменьшения!'
            $ game.dragon.gain_rage()
            call lb_lair_rape from _call_lb_lair_rape_2
            if game.girl.dead:
              return
        'Магический рост' if not game.girls_list.is_mating_possible and game.girl.virgin and game.girls_list.is_giant and game.dragon.mana > 0 and game.dragon.lust > 0:
            $ game.dragon.drain_mana()
            game.dragon 'Заклятье временного роста!'
            call lb_lair_rape from _call_lb_lair_rape_4
            if game.girl.dead:
              return
        'Ограбить' if game.girl.treasure:
            $ description = game.girls_list.rob_girl()
            game.girl.third "[description]"
        'Попробовать уговорить' if game.girls_list.is_talk_possible:
            call lb_talk from _call_lb_talk
        'Вернуть в темницу':
            $ description = game.girls_list.jail_girl()
            game.girl.third "[description]"
#            call lb_location_lair_main from _call_lb_location_lair_main_9
            call screen girls_menu
            return
        'Отнести в родные места' if (game.girl.love is None) and game.dragon.energy() > 0:
            game.dragon 'Интересно, а как эти примитивные цивилизации относятся к моим жертвам?'
            game.dragon 'Хмм... Надо бы провести социальный эксперимент и отнести [game.girl.name_v] в родные места!'
            $ game.dragon.drain_energy()
            if game.girl.virgin:
              $ text = u'Угодив в драконье логово, %s уже простилось с честью и жизнью. Однако в тот день %s был сытым и умиротворённым. Хорошенько помяв и обслюнявив невинное тельце, он отнёс девушку восвояси. Чудо, настоящее чудо, иначе не скажешь! \n\n' % (game.girl.name, game.dragon.name)
            else:
              $ text = u'%s отнёс обесчещенную девицу восвояси. Дракона весьма интересовало, как сложится её дальнейшая судьба.\n\n' % (game.dragon.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            $ game.girls_list.free_list.append(game.girl)
            return
# Выбираясь из драконьего логова, девушка может погибнуть.
        'Отпустить восвояси' if not (game.girl.cripple and game.girl.love is not None):
            if game.girl.virgin:
              $ text = u'Угодив в драконье логово, %s уже простилось с честью и жизнью. Однако в тот день %s был сытым и умиротворённым. Хорошенько помяв и обслюнявив невинное тельце, он отпустил девушку восвояси. Возможно, это просто изощрённый способ убийства? \n\n' % (game.girl.name, game.dragon.name)
            else:
              $ text = u'%s отпустил обесчещенную девицу восвояси. Дракона нимало не заботило, сможет ли %s добраться до дома.\n\n' % (game.dragon.name, game.girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            $ description = game.girls_list.free_girl()
            game.girl.third "[description]"
            python:
                if game.girl.love is not None:
                  game.girls_list.love_escape_ind()
                else:
                  game.girls_list.try_to_go()             
            return
        'Отдать бесполезное мясо возлюбленному' if (game.girl.cripple and game.girl.love is not None):
            if game.girl.love.type == 'smuggler':
              game.dragon '[game.girl.love.name], неужели ты действительно любишь этот обрубок?'
              game.girl.love 'Честно? Ни капельки!'
              game.dragon 'Тогда зачем же связался?'
              game.girl.love 'Сначала я хотел продать её в Султанат. но потом обнаружил более выгодное предложение. Сумасшедший алхимик активно скупает материал для экспериментов.'
              game.dragon 'По какой цене?'
              game.girl.love '2000 фартингов'
              game.dragon 'Заткнись и бери [game.girl.name_v]!'
              $ game.lair.treasury.money += 2000
              $ text = u'По совету контрабандиста дракон продал %s сумасшедшему алхимику.\n\n' % (game.girl.name_v)
              $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
              call lb_love_alchemist_cripple from _call_love_alchemist_cripple_2
            elif game.girl.love.type == 'lizardman':
              game.dragon '[game.girl.love.name], неужели ты действительно любишь этот обрубок?'
              game.girl.love 'Больше жизни. Меня терзает невыносимое чувство вины, ведь меня не было рядом, когда ты калечил её.'
              game.dragon 'Мне этого не понять.'
              game.girl.love 'Возможно, отец.'
              game.dragon 'Забирай её'
              game.girl.love 'Что?'
              game.dragon 'Забирай её и убирайся к ангелу!'
              '[game.girl.love.name] немедленно воспользовался неожиданным предложением.'
              $ text = u'%s отдал искалеченную %s %sу\n\n' % (game.dragon.name, game.girl.name_v, game.girl.love.name)
              $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
              $ game.girls_list.love_escape_ind()
            call screen girls_menu
            return
        'Сожрать' if game.dragon.hunger > 0:
            if game.girl.love is not None:
              if game.girl.love.type == 'lizardman' and not game.girl.cripple:  
                jump lb_love_eat_lizardman
            if not game.girls_list.is_giant:
              $ text = u'%s - это не только аппарат для производства отродий, но и 50-60 килограмм диетического, легкоусвояемого мяса. %s с удовольствием съел свою жертву, с аппетитом разжевав её тонкие косточки.\n\n' % (game.girl.name, game.dragon.name)
            else:
              $ text = u'%s - это не только аппарат для производства элитных отродий, но и 500-600 килограмм диетического, легкоусвояемого мяса. %s с удовольствием съел свою жертву, с аппетитом разжевав её массивные кости.\n\n' % (game.girl.name, game.dragon.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            call lb_eat from _call_lb_eat_2  
            call screen girls_menu              
            return
        'Казнить за измену' if game.girl.love is not None:
            if game.girl.love.type == 'smuggler':
              if game.girl.cripple:
                call lb_love_execution_smuggler_cripple from _call_lb_love_execution_smuggler_cripple
              else:
                call lb_love_execution_smuggler from _call_lb_love_execution_smuggler
            elif game.girl.love.type == 'lizardman':
              call lb_love_execution_lizardman from _call_lb_love_execution_lizardman
            return
        'Казнить обоих за измену' if game.girl.love is not None:
            if game.girl.love.type == 'smuggler':
              if game.girl.cripple:
                call lb_love_execution_both_smuggler_cripple from _call_lb_love_execution_both_smuggler_cripple
              else:
                call lb_love_execution_both_smuggler from _call_lb_love_execution_both_smuggler
            elif game.girl.love.type == 'lizardman':
              call lb_love_execution_both_lizardman from _call_lb_love_execution_both_lizardman
            return
        'Продать в Султанат' if game.love.is_trade_possible:
            if game.girl.type == 'peasant':
              $ game.lair.treasury.money += 100
              game.dragon.third '[game.girl.name] продана в Султанат за 100 фартингов. Лучше, чем ничего.'
            elif game.girl.type == 'citizen':
              $ game.lair.treasury.money += 200
              game.dragon.third '[game.girl.name] продана в Султанат за 200 фартингов. Неплохая сделка.'
            elif game.girl.type == 'princess':
              $ game.lair.treasury.money += 300
              game.dragon.third '[game.girl.name] продана в Султанат за 300 фартингов. С паршивой принцессы - хоть золота мешок!'
            elif game.girl.type == 'elf':
              $ game.lair.treasury.money += 500
              game.dragon.third '[game.girl.name] продана в Султанат за 500 фартингов. Богатство!!!'
            $ text = u'%s была продана драконом в Султанат.\n\n' % (game.girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            if game.girl.love is not None:
              if game.girl.love.type == 'smuggler':
                $ game.girls_list.sultan_list.append(game.girl)
              elif game.girl.love.type == 'lizardman':
                call lb_love_caravan_lizardman from _call_lb_love_caravan_lizardman
            else:
              $ game.girls_list.sultan_list.append(game.girl)
            return
#        'Использовать как заготовку для мясного голема' if game.girl.cripple and'shadow' in game.dragon.heads and 'elite_guards' not in game.lair.upgrades and game.dragon.mana > 0:
#            call lb_meat_golem
#            return 
    jump lb_lair_sex


label lb_knight_new:
    show expression 'img/bg/special/oath.jpg' as bg
    'Рыцарь дал клятву убить дракона.'
    return

label lb_water_sex:
    jump lb_nature_sex
    return

label lb_nature_rape():
    $ game.rape.rage=0
    if game.dragon.bloodiness > 2:
      'Девушка явно не осознаёт своего счастья.\n\n А [game.dragon.fullname] к тому же слегка раздражён. Во время соития он просто-напросто разорвёт девушку на части. \n\n Может, имеет смысл отнести бунтарку в логово и кликнуть охранников, чтобы подержали?'
    else:
      'Девушка явно не осознаёт своего счастья. Но это временно!\n\n С другой стороны - может, имеет смысл отнести бунтарку в логово и кликнуть охранников, чтобы подержали?'
    menu:
        'Да что с ней возиться?! Сожрать, и все дела!' if game.dragon.bloodiness > 2 and game.dragon.hunger > 0:
            if not girls_data.girls_info[game.girl.type]['giantess']:
              $ text = u'%s - это не только аппарат для производства отродий, но и 50-60 килограмм диетического, легкоусвояемого мяса. %s с удовольствием съел свою жертву, с аппетитом разжевав её тонкие косточки.\n\n' % (game.girl.name, game.dragon.name)
            else:
              $ text = u'%s - это не только аппарат для производства элитных отродий, но и 500-600 килограмм диетического, легкоусвояемого мяса. %s с удовольствием съел свою жертву, с аппетитом разжевав её массивные кости.\n\n' % (game.girl.name, game.dragon.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            call lb_eat from _call_lb_eat_4
            $ game.girl.dead = True
        'Из чего же сделаны наши девчонки?' if game.dragon.bloodiness > 2 and game.dragon.hunger == 0:
            $ text = u'%s разорвал на части пленницу просто ради забавы. \n\n' % (game.dragon.name)
            game.girl.third '[text]'
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            $ game.chronik.death('turned_apart',"img/scene/turn_apart.jpg")
            $ game.girl.dead = True
        'Пока оставлю. Пригодицца.' if game.dragon.bloodiness > 2:
            pass
        'Я возьму сам!' if game.dragon.bloodiness < 3:  
            call lb_sex_choice from _call_lb_sex_choice_1
            if not game.girl.dead:
              $ text = u' Девушка недолго оставалась таковой: %s обесчестил жертву, не сходя с места и не опасаясь возможных свидетелей. ' % game.dragon.name
              if game.girl.cripple:
                if game.girl.type=='mermaid' or game.girl.type=='siren':
                  $ text += u'При этом морская дева отбивалась с такой яростью, что %s в порыве гнева оторвал ей руки и хвост, вырвал язык и выколол уши. ' % (game.dragon.name)
                else:
                  $ text = u'При этом жертва отбивалась с такой яростью, что %s в порыве гнева оторвал ей руки и ноги, вырвал язык и выколол уши.  ' % (game.dragon.name)
              elif game.girl.blind:
                $ text += u'При этом в процессе ухаживаний дракон решил немного подшутить и выколол %s глаза. ' % (game.girl.name_d)
              $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
        'Не, лениво' if game.dragon.bloodiness < 3:
            pass
    return

label lb_lair_rape:
    $ game.rape.rage=0
    if game.dragon.bloodiness > 2:
      if (not girls_data.girls_info[game.girl.type]['giantess'] and (('regular_guards' in game.lair.upgrades) or ('smuggler_guards' in game.lair.upgrades))):
        'Девушка явно не осознаёт своего счастья.\n\n А [game.dragon.fullname] к тому же слегка раздражён. Во время соития он просто-напросто разорвёт девушку на части. \n\n Может, имеет смысл кликнуть охранников, чтобы подержали?'
      elif  (girls_data.girls_info[game.girl.type]['giantess'] and ('elite_guards' in game.lair.upgrades)):
        'Девушка явно не осознаёт своего счастья.\n\n А [game.dragon.fullname] к тому же слегка раздражён. Во время соития он просто-напросто разорвёт девушку на части. \n\n Может, имеет смысл кликнуть охранников, чтобы подержали? Элитных - великанша расшвыряет простых воинов, как щенят.'
      else:
        'Девушка явно не осознаёт своего счастья.\n\n А [game.dragon.fullname] к тому же слегка раздражён. Во время соития он просто-напросто разорвёт девушку на части. \n\n И к тому же в логове нету охранников! Может, развлечь пленницу позже?'
    else:
      if (not girls_data.girls_info[game.girl.type]['giantess'] and (('regular_guards' in game.lair.upgrades) or ('smuggler_guards' in game.lair.upgrades))):
        'Девушка явно не осознаёт своего счастья. Но это временно!\n\n С другой стороны - может, имеет смысл кликнуть охранников, чтобы подержали? Благо, желающие имеются.'
      elif  (girls_data.girls_info[game.girl.type]['giantess'] and ('elite_guards' in game.lair.upgrades)):
        'Девушка явно не осознаёт своего счастья. Но это временно!\n\n С другой стороны - может, имеет смысл кликнуть охранников, чтобы подержали? Благо, желающие имеются.'
      else:
        'Девушка явно не осознаёт своего счастья. Но это временно!\n\n С другой стороны - может, имеет смысл кликнуть охранников, чтобы подержали? Правда, желающих как-то не наблюдается...'
    menu:
        'Кликнуть охранников' if (not girls_data.girls_info[game.girl.type]['giantess'] and (('regular_guards' in game.lair.upgrades) or ('smuggler_guards' in game.lair.upgrades)) and not game.girl.willing):
            call lb_sex from _call_lb_sex_1
            $ text = u' %s насиловал девушку в течении нескольких часов, пока не убедился, что обезумевшая от боли %s понесла его отродье, а потом отдал её на потеху охранникам.\n\n ' % (game.dragon.name,  game.girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            'Надругавшись над невинным девичьим телом, дракон отдал её на забаву охранникам.'
            game.dragon 'Развлекайтесь, заслужили. Но без членовредительства - ей ещё рожать!'
        'Кликнуть элитных охранников' if (girls_data.girls_info[game.girl.type]['giantess'] and ('elite_guards' in game.lair.upgrades) and not game.girl.willing):
            call lb_sex from _call_lb_sex_2
            $ text = u' %s насиловал великаншу в течении нескольких часов, пока не убедился, что стонущая от боли %s понесла его отродье, а потом отдал её на потеху элитным охранникам. ' % (game.dragon.name, game.girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            'Надругавшись над телом великанши, дракон отдал её на забаву элитным охранникам.'
            game.dragon 'Развлекайтесь, заслужили. Но без членовредительства - ей ещё рожать!'
        'Да что с ней возиться?! Сожрать, и все дела!' if game.dragon.hunger > 0 and game.dragon.bloodiness > 2:
            if not girls_data.girls_info[game.girl.type]['giantess']:
              $ text = u'%s - это не только аппарат для производства отродий, но и 50-60 килограмм диетического, легкоусвояемого мяса. %s с удовольствием съел свою жертву, с аппетитом разжевав её тонкие косточки.\n\n' % (game.girl.name, game.dragon.name)
            else:
              $ text = u'%s - это не только аппарат для производства элитных отродий, но и 500-600 килограмм диетического, легкоусвояемого мяса. %s с удовольствием съел свою жертву, с аппетитом разжевав её массивные кости.\n\n' % (game.girl.name, game.dragon.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            call lb_eat from _call_lb_eat_5
            $ game.girl.dead = True
        'Из чего же сделаны наши девчонки?' if game.dragon.hunger == 0 and game.dragon.bloodiness > 2:
            $ text = u'%s разорвал на части пленницу просто ради забавы. \n\n' % (game.dragon.name)
            game.girl.third '[text]'
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            $ game.chronik.death('turned_apart',"img/scene/turn_apart.jpg")
            $ game.girl.dead = True
#            jump lb_location_lair_main
        'Потом займусь. Пригодицца.'  if game.dragon.bloodiness > 2:
            pass
        'Я возьму сам!' if game.dragon.bloodiness < 3:  
            call lb_sex_choice from _call_lb_sex_choice_2
            if not game.girl.dead and not girls_data.girls_info[game.girl.type]['giantess']:
              if game.girl.cripple:
                if game.girl.type=='mermaid':
                  $ text = u'Русалка отбивалась с такой яростью, что %s в порыве гнева оторвал ей руки и хвост, вырвал язык и выколол уши. Спустив пар, ящер насиловал беспомощный обрубок в течении нескольких часов, пока не убедился, что жертва понесла его отродье. \n\n' % (game.dragon.name)
                else:
                  $ text = u'Пленница отбивалась с такой яростью, что %s в порыве гнева оторвал ей руки и ноги, вырвал язык и выколол уши. Спустив пар, ящер насиловал беспомощный обрубок в течении нескольких часов, пока не убедился, что жертва понесла его отродье. \n\n' % (game.dragon.name)
              elif game.girl.blind:
                $ text = u'Развлекаясь с пленницей, %s решил подшутить над %s и выколол ей глаза. Потом он насиловал безглазое тело в течении нескольких часов, пока не убедился, что жертва понесла его отродье. \n\n' % (game.dragon.name, game.girl.name_t)
              else:
                $ text = u' %s насиловал девушку в течении нескольких часов, пока не убедился, что обезумевшая от боли %s понесла его отродье.\n\n ' % (game.dragon.name,  game.girl.name)
              $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            elif not game.girl.dead and girls_data.girls_info[game.girl.type]['giantess']:
              if game.girl.cripple:
                if game.girl.type=='siren':
                  $ text = u'Сирена отбивалась с такой яростью, что %s в порыве гнева оторвал ей руки и хвост, вырвал язык и выколол уши. Спустив пар, ящер насиловал беспомощный обрубок в течении нескольких часов, пока не убедился, что жертва понесла его отродье. \n\n' % (game.dragon.name)
                else:
                  $ text = u'Великанша отбивалась с такой яростью, что %s в порыве гнева оторвал ей руки и ноги, вырвал язык и выколол уши. Спустив пар, ящер насиловал беспомощный обрубок в течении нескольких часов, пока не убедился, что жертва понесла его отродье. \n\n' % (game.dragon.name)
              elif game.girl.blind:
                $ text = u'Развлекаясь с пленницей, %s решил подшутить над %s и выколол ей глаза. Потом он насиловал ослеплённую великаншу в течении нескольких часов, пока не убедился, что жертва понесла его отродье. \n\n' % (game.dragon.name, game.girl.name_t)
              else:
                $ text = u' %s насиловал великаншу в течении нескольких часов, пока не убедился, что стонущая от боли %s понесла его отродье. \n\n' % (game.dragon.name, game.girl.name)
              $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
        'Не, лениво' if game.dragon.bloodiness < 3:
            pass

    return

label lb_sex_choice:   # В этой подпрограмме производится настройка экранов
    if not game.girl.type == 'afrodita' and not game.girl.type == 'danu' and not game.girl.type == 'jasmine':
      stop music fadeout 1.0
      $ renpy.music.play(get_random_files('mus/darkness')) 
    python:
        hair_color=game.girl.hair_color
        if game.girl.type == 'afrodita':
          rape.relative_path="img/sex_screen/afrodita"
        elif game.girl.type == 'danu':
          rape.relative_path="img/sex_screen/danu"  
        elif game.girl.type == 'jasmine':
          rape.relative_path="img/sex_screen/jasmine"  
        elif game.girl.type == 'mermaid' or game.girl.type == 'siren':
          num = get_place_sex_screen('mermaid')
          rape.relative_path="img/sex_screen/mermaid/" + num
        elif game.girl.type == 'elf':
          hair_color="elf/"+hair_color
          num = get_place_sex_screen(hair_color)
          rape.relative_path="img/sex_screen/" + hair_color + "/" + num
        else:
          num = get_place_sex_screen(hair_color)
          rape.relative_path="img/sex_screen/" + hair_color + "/" + num
        game.rape.define_full_health()
        game.rape.define_full_proud()
#        game.narrator('[game.girl.nature],[game.rape.actual_proud],[game.rape.full_proud]')
        game.rape.define_rage()
        game.rape.define_freedom()
# Выбираем цвет голов
        head_color=random.choice(game.dragon.heads)
        rape.dragon_path="img/dragon_screen/" + head_color
#        game.narrator("path: %s" % rape.dragon_path)

    call screen start_sex
    $ game.rape.rage=0
    return


label lb_sex:
    $ description = game.girls_list.impregnate()
    if not game.girl.type == 'afrodita' and not game.girl.type == 'danu' and not game.girl.type == 'jasmine':
      stop music fadeout 1.0            
    game.girl "[description]"
    $ current_image=sex_imgs(game.girl.sex_expression)
    show expression current_image as xxx
    play sound get_random_file("sound/sex")
    pause (500.0)
    stop sound fadeout 1.0
    hide xxx
    return

label lb_eat:  # Пожирание девушки
    $ description =  game.girls_list.eat_girl()
    game.girl "[description]"
    play sound "sound/eat.ogg"
    $ current_image=sex_imgs.get_eat_image()
    show expression current_image as eat_image
#    $ game.chronik.chronik_image[game.dragon.level-1][game.girl.girl_id]=current_image
    $ game.chronik.death('eat',current_image)
#    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    pause (500.0)
    hide eat_image 
    if game.girls_list.is_love:
      call lb_love_suicide_lizardman from _call_lb_love_suicide_lizardman_4
    return
    