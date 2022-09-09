# coding=utf-8

init python:
    from pythoncode.utils import weighted_random
    from pythoncode.characters import Enemy
    
label lb_special_places:
    nvl clear
    hide bg
    show expression 'img/bg/special/map.jpg' as bg
    if game.dragon.energy() == 0:
        'Даже драконам надо иногда спать. Особенно драконам!'
        return   
    python:
        special_places_menu = []
        for special_place in game.dragon.special_places.keys():
            # добавляем в список исследованные достопримечательности
            special_stage = game.dragon.special_places[special_place]
            special_places_menu.append((data.special_places[special_stage][0], special_stage))
        special_places_menu.append(('Вернуться', 'back'))
        special_stage = renpy.display_menu(special_places_menu)
        
        if special_stage == 'back':
            pass
        else:
            renpy.call(data.special_places[special_stage][1])
    return
    
label lb_enchanted_forest:
    show expression 'img/bg/special/enchanted_forest.jpg' as bg
    if game.dragon.mana <= 0:
        'Даже зная путь в зачарованный лес, пройти через завесу магии альвов непросто. Нужно применить могучие чары.'

    menu:
        'Открыть путь колдовством' if game.dragon.mana > 0:
            $ game.dragon.drain_mana()
            '[game.dragon.fullname] применяет чёрную магию, чтобы разорвать завесу иллюзий, морока и сна, которыми скрыты владения альвов. Незамеченный и смертоносный, [game.dragon.kind] входит под сень чародейских древ.'
            nvl clear
            call lb_enchanted_forest_enter from _call_lb_enchanted_forest_enter
        'Открыть путь колдовством и рыскать кругом' if game.dragon.mana > 0:
            $ game.dragon.drain_mana()
            nvl clear
            $ choices = [
                ("lb_enchanted_forest_elfgirl", 10),
                ("lb_enchanted_forest_druid", 10),
                ]
            $ enc = weighted_random(choices)
            $ renpy.call(enc)

        'Уйти прочь':
            return
        
    return
            

label lb_enchanted_forest_enter:        
    stop music fadeout 1.0
    play music "mus/forest.ogg"  
    $ renpy.music.queue(get_random_files('mus/ambient')) 
    menu:
        'Рыскать кругом':
            $ choices = [
                ("lb_enchanted_forest_elfgirl", 10),
                ("lb_enchanted_forest_druid", 10),
                ]
            $ enc = weighted_random(choices)
            $ renpy.call(enc)
    
        'Напасть на Древо Жизни':
            call lb_enchanted_forest_grove from _call_lb_enchanted_forest_grove
            
    return

label lb_enchanted_forest_elfgirl:
    '[game.dragon.name] слышит непередаваемый аромат, сотканный из ноток невинности, красоты и колдовских чар. Это лесная ведьма, альва из народа богини Дану. Нет плоти более сладкой и желанной, но взять её будет непросто, ведь на её стороне колдовство.'
    $ game.foe = Enemy('elf_witch', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Напасть на фею':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_25
            'Несмотря на жестокое сопротивление, чародейка не получила особых повреждений. Она теперь безащитна, но цела... пока что.'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            $ description = game.girls_list.new_girl('elf')
            $ text = u' %s спокойно гуляла по родному лесу и внезапно встретила дракона. Короткая схватка окончилась унизительным и страшным поражением. \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_14      
        
        'Тихонько уйти прочь' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()        
    return

label lb_enchanted_forest_druid:
    '[game.dragon.name] недолго остаётся незамеченным. На пути дракона, словно материализовавшись из листьев, возникает вооруженный корявым посохом друид. Он не выглядит особенно внушительным, однако это впечатление обманичво. На стороне жреца Дану сама сила леса.'
    $ game.foe = Enemy('druid', game_ref=game)
    $ narrator(show_chances(game.foe))
    menu:
        'Вступить в бой':
            $ game.dragon.drain_energy()
            $ game.foe = Enemy('druid', game_ref=game)
            call lb_fight from _call_lb_fight_26
            $ game.dragon.reputation.points += 3
            python:
                count = random.randint(1, 2)
                alignment = 'elf'
                min_cost = 25
                max_cost = 500
                obtained = "Это предмет принадлежал друиду - стражу зачарованого леса."
                trs = treasures.gen_treas(count, data.loot['knight'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
            'Друид повержен. [game.dragon.reputation.gain_description]\n[game.dragon.name] находит на трупе кое-что ценное:\n[trs_descrptn]'
        'Отступить и покинуть лес' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()   
    return

label lb_enchanted_forest_grove:
    show expression 'img/bg/special/enchanted_forest.jpg' as bg
    nvl clear
    $ txt = game.interpolate(random.choice(txt_place_enfr[1]))
    '[txt]'    
    $ game.foe = Enemy('treant', game_ref=game)
    $ chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Атаковать священное древо':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_27
            $ txt = game.interpolate(random.choice(txt_place_enfr[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 25
            '[game.dragon.reputation.gain_description]' 
            nvl clear
            call lb_enchanted_forest_grove_rob from _call_lb_enchanted_forest_grove_rob
        'Покинуть зачарованный лес' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            
    return
    
label lb_enchanted_forest_grove_rob:
    $ game.dragon.add_event('ravage_sacred_grove')
    $ game.history = historical( name='elf_ruined',end_year=game.year+30,desc='Семечко, посаженное альвами, дало росток нового священного Древа. Богиня Дану благословила его ветви, и теперь народ альвов пребывает в мире и гармонии под тенью его кроны.  ',image='img/bg/special/elf_restored.jpg')
    $ game.history_mod.append(game.history)
    python:
        count = random.randint(5, 10)
        alignment = 'elf'
        min_cost = 500
        max_cost = 3000
        obtained = "Это предмет из королевской сокровищницы альвов зачарованного леса."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Осквернить священное древо':
            show expression 'img/bg/lair/elfruin.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_enfr[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            call lb_enchanted_forest_queen from _call_lb_enchanted_forest_queen
  
            $ game.dragon.add_special_place('enchanted_forest', 'dead_grove')
                                        
        'Запомнить место и уйти':
            $ game.dragon.add_special_place('enchanted_forest', 'dead_grove')
            
    return

label lb_enchanted_forest_queen: # Ивент с Королевой
    nvl clear
    show expression 'img/bg/special/elf_queen.jpg' as bg
    '[game.dragon.fullname] вальяжно входит в зал, в котором спряталась королева альвов'
    game.dragon 'Ты моя!'
    $ description = game.girls_list.new_girl('elf')
    $ text = u'%s, королева народа альвов, мудро вела свой народ к гармонии и процветанию. Но в один ужасный день её народ оказался истреблён, священное древо - осквернено, а ей самой грозила участь игрушки дракона. \n\n' % game.girl.name
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    if game.girl.nature == 'innocent':  # Невинная
      $ text = u'И тогда %s решила покончить с собой, вонзив кинжал в грудь. ' % game.girl.name
      $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
      game.girl 'Не думаю.'
      '[game.girl.name] уже поднесла кинжал к собственной груди!'
      menu:
          'Заклятье!' if ('gold_magic' in game.dragon.modifiers() or 'silver_magic' in game.dragon.modifiers() or 'shadow_magic' in game.dragon.modifiers()) and game.dragon.mana > 0:
              $ game.dragon.drain_mana()
              'Благодаря тайным знаниям дракон применяет мгновенное заклятье парализации!'
          'Прыгнуть!' if game.dragon.paws>=3:
              'Благодаря обилию ног дракон совершает молниеносный прыжо и предотвращает самоубийство!'
          'Помешать!':
              if random.randint(1,3)==1:
                'Дракон успевает предотвратить самоубийство!'
              else:
                'Увы, предотвратить самоубийство в этой ситуации было абсолютно невозможно! Дракону достался лишь хладный труп'
                game.dragon 'Тьфу ты!'
                $ game.dragon.gain_rage()
                $ text = u'Дракон ничем не смог помешать отчаянной альве. '
                $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
                $ game.chronik.death('forest_queen_innocent','img/bg/special/elf_queen.jpg')
                return
      game.girl 'Нет!'
      game.dragon 'Вздумала у смерти от меня спрятаться? Ну-ну.'
      call lb_nature_sex from _call_lb_nature_sex_15 
    elif game.girl.nature == 'proud':  # Гордая
      $ text = u'И тогда %s отравила себя темнейшим колдовством, обрекая себя на быструю, но мучительную смерть. Альва надеясь, что перед смертью она сумеет отравить драона. ' % game.girl.name
      $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
      game.girl 'Попробуй, возьми!'
      '[game.girl.name] сжимает в руках кинжал и готовится задорого продать свою свободу.'
      '[game.dragon.name] отнимает кинжал и обезвреживает противницу с издевательской лёгкостью.'
      menu:
          'Надругаться' if game.dragon.lust>0:
              $ text = u'План удался лишь частично. Надругавшись над альвой, [game.dragon.fullname] получил серьёзные проблемы со здоровьем... ничего, что не должно было пройти через пару-тройку лет.'
              $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
              $ game.chronik.death('forest_queen_proud','img/bg/special/elf_queen.jpg')
              'Желая сломить непокорную королеву, дракон взял её прямо в тронном зале'
              if not game.girls_list.is_mating_possible:
                $ game.dragon.gain_rage()
              call lb_sex from _call_lb_sex_3
              nvl clear
              '[game.dragon.fullname] издаёт блаженный стон.'
              'На лице обесчещенной альвы появляется подозрительно довольная улыбка.'
              'Через несколько секунд [game.girl.name] начинает биться в предсмертных конвульсиях.' 
              game.dragon 'Кажется, она отравила себя темнейшим колдовством'
              game.dragon 'Ой...'
              python:
                  game.dragon.health = 0
                  game.dragon.hunger = 0
                  game.dragon.lust = 0
                  game.dragon.bloodiness = 5
                  game.dragon.spells=[]
                  game.dragon.drain_mana(game.dragon.mana)
                  energy=game.dragon.energy()
                  game.dragon.drain_energy(energy)
              'Дракона скручивает мучительный приступ боли'
              game.dragon 'Вот это точно нельзя назвать безопасным сексом!'
              game.dragon 'Впрочем, всё ещё обошлось. Вот если бы я её съел...'
            
          # @fdsc Гипноз
          'Загипнотизировать' if game.dragon.mana > game.girl.quality and not game.girl.willing:

            # @fdsc Девушки добровольно соглашаются
            $ game.girl.willing=True
            $ game.dragon.drain_mana(game.girl.quality + 1)
            pass

          'Сожрать' if game.dragon.hunger > 0:
              $ text = u'План полностью удался. Неосторожный дракон съел королеву и умер от отравления. Дети Богини Дану были отомщены. '
              $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
              $ game.chronik.death('forest_queen_proud','img/bg/special/elf_queen.jpg')
              game.dragon.third 'Интересно, королева чем-нибудь отличается на вкус от обычной альвы?'
              $ description =  game.girls_list.eat_girl()
              play sound "sound/eat.ogg"
              $ current_image=sex_imgs.get_eat_image()
              show expression current_image as eat_image
              pause (500.0)
              hide eat_image
              game.dragon 'Ммм... коготки оближешь. Что?!..'
              nvl clear
              'Тяжесть. Вздутие. Боль в животе.'
              game.dragon 'Она отравила себя темнейшим колдовством! И я... я её съел!'
              'Дракон скрючивается в приступе непереносимой боли.'
              game.dragon 'Ма...'
              $ game.dragon._alive=False
              if freeplay:
                jump lb_game_over
          'Что-то тут не так!':
              $ text = u'План провалился. Осторожный дракон почуял подвох и не тронул королеву. %s скончалась после мучительной, но быстрой агонии. ' % game.girl.name
              $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
              $ game.chronik.death('forest_queen_proud','img/bg/special/elf_queen.jpg')
              nvl clear
              game.dragon.third 'Странно, что могущественная королева сдалась настолько легко! Надо бы приглядеться поподробнее...'
              game.dragon.third 'Ой. Кажется, [game.girl.name] отравила себя темнейшим колдовством.'
              'Обнаружив, что раскрыта, королева хотела броситься на ненавистного дракона, но скорчилась от внезапных судорог.'
              'Альва умерла после короткой, но мучительной агонии, и её тело распалось чёрной жижей.'
              game.dragon 'Ой. Если бы я над ЭТИМ надругался, а тем более - сожрал...'
              game.dragon 'Кажется, некоторые жертвы отличаются просто ангельской изобретательностью!'
              $ game.dragon.gain_rage()
    elif game.girl.nature == 'lust':  # Гордая
      $ game.girl.willing=True # Добровольно согласна на секс с драконом
      $ text = u'И %s приняла её с радостью - ведь это была её заветная мечта! \n\n' % game.girl.name
      $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
      game.girl 'Разумеется!'
      nvl clear
      'Королева альвов кидается к опешившему дракону и покрывает его морду поцелуями.'
      game.dragon 'Ммм... Не ожидал такого от верной последовательницы Природы!'
      game.girl 'А я - неортодоксальная последовательница! Размножение драконов является неотъемлимой частью природного цикла, и я жажду поучаствовать в этом процессе!'
      call lb_nature_sex from _call_lb_nature_sex_52 
    return
    
label lb_dead_grove:
    show expression 'img/bg/lair/dead_grove.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_enfr[4]))
    '[txt]'   
    nvl clear
    menu:
        'Обустроить тут новое логово':
            $ game.create_lair('forest_heart')
            $ game.dragon.del_special_place('enchanted_forest')
        
        'Уйти прочь':
            $ game.dragon.add_special_place('enchanted_forest', 'dead_grove')
    
    return

# Рыцарская усадьба
label lb_manor_found:
    show expression 'img/bg/special/castle1.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_manor[0]))
    '[txt]'
    jump lb_manor
    
label lb_manor:
    show expression 'img/bg/special/castle1.jpg' as bg
    nvl clear
    $ txt = game.interpolate(random.choice(txt_place_manor[1]))
    '[txt]'    
    $ game.foe = Enemy('old_knight', game_ref=game)
    $ chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Вызвать рыцаря на бой':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_28
            $ txt = game.interpolate(random.choice(txt_place_manor[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            nvl clear
            call lb_manor_rob from _call_lb_manor_rob
        'Запомнить место и уйти' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('manor', 'manor_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_manor_rob:
    python:
        count = random.randint(1, 5)
        alignment = 'knight'
        min_cost = 10
        max_cost = 250
        obtained = "Это предмет из разграбленного рыцарского поместья."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Разграбить поместье':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_manor[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_manor[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            $ text = u'%s, дочь небогатого рыцаря, мечтала о выгодной партии. Мечты сбываются: теперь у неё красивый и богатый кавалер. Вот только бедняжке от этого ни капельки не легче.  \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_16     
            $ game.dragon.add_special_place('manor', 'manor_empty')
                                        
        'Запомнить место и уйти':
            $ game.dragon.add_special_place('manor', 'manor_empty')
            
    return
            
label lb_manor_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_manor[4]))
    '[txt]'   
    nvl clear
    menu:
        'Обустроить тут новое логово':
            $ game.create_lair('dragon_castle')
            $ game.dragon.del_special_place('manor')
        
        'Покинуть заброшенную усадьбу':
            $ game.dragon.add_special_place('manor', 'manor_empty')
            
    return

# Деревянный замок
label lb_wooden_fort_found:
    show expression 'img/bg/special/castle2.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_wooden_fort[0]))
    '[txt]'
    jump lb_wooden_fort
    
label lb_wooden_fort:
    show expression 'img/bg/special/castle2.jpg' as bg
    nvl clear
    $ txt = game.interpolate(random.choice(txt_place_wooden_fort[1]))
    '[txt]'    
    $ game.foe = Enemy('footman', game_ref=game)
    $ chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Атаковать замок':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_29
            $ txt = game.interpolate(random.choice(txt_place_wooden_fort[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'            
            nvl clear
            call lb_wooden_fort_rob from _call_lb_wooden_fort_rob
        'Запомнить место и уйти' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('wooden_fort', 'wooden_fort_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_wooden_fort_rob:
    python:
        count = random.randint(2, 6)
        alignment = 'knight'
        min_cost = 25
        max_cost = 500
        obtained = "Это предмет найден в деревянном рыцарском замке."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Разграбить центральную башню':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_wooden_fort[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_wooden_fort[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            $ text = u'%s, дочь зажиточного барона, мечтала о выгодной партии. Мечты сбываются: теперь у неё красивый и богатый кавалер. Вот только бедняжке от этого ни капельки не легче.  \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_17 
            $ game.dragon.add_special_place('wooden_fort', 'wooden_fort_empty')
                                        
        'Запомнить место и уйти':
            $ game.dragon.add_special_place('wooden_fort', 'wooden_fort_empty')
            
    return
            
label lb_wooden_fort_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_wooden_fort[4]))
    '[txt]'   
    nvl clear
    menu:
        'Обустроить тут новое логово':
            $ game.create_lair('castle')
            $ game.dragon.del_special_place('wooden_fort')
        
        'Покинуть деревянный форт':
            $ game.dragon.add_special_place('wooden_fort', 'wooden_fort_empty')
            
    return

# Укреплённый монастырь
label lb_abbey_found:
    show expression 'img/bg/special/castle3.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_abbey[0]))
    '[txt]'
    jump lb_abbey
    
label lb_abbey:
    show expression 'img/bg/special/castle3.jpg' as bg
    nvl clear
    $ txt = game.interpolate(random.choice(txt_place_abbey[1]))
    '[txt]'    
    $ game.foe = Enemy('templars', game_ref=game)
    $ chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Атаковать монастырь':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_30
            $ txt = game.interpolate(random.choice(txt_place_abbey[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 10
            '[game.dragon.reputation.gain_description]'  
            nvl clear
            call lb_abbey_rob from _call_lb_abbey_rob
        'Запомнить место и уйти' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('abbey', 'abbey_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_abbey_rob:
    python:
        count = random.randint(4, 10)
        alignment = 'cleric'
        min_cost = 10
        max_cost = 500
        obtained = "Это предмет из разграбленного монастыря."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Разграбить обитель':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_abbey[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_abbey[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            $ text = u'Устав от мирской суеты, %s приняла постриг и отправилась в монастырь. Однако в один из дней тихая и размеренная жизнь разбилась вдребезги: драконы просто обожают чистых, невинных и аппетитных монашек. \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_18 
            $ game.dragon.add_special_place('abbey', 'abbey_empty')
                                        
        'Запомнить место и уйти':
            $ game.dragon.add_special_place('abbey', 'abbey_empty')
            
    return
            
label lb_abbey_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_abbey[4]))
    '[txt]'   
    nvl clear
    menu:
        'Обустроить тут новое логово':
            $ game.create_lair('monastery_ruin')
            $ game.dragon.del_special_place('abbey')
        
        'Покинуть осквернённый монастырь':
            $ game.dragon.add_special_place('abbey', 'abbey_empty')
            
    return

# Каменная крепость
label lb_castle_found:
    show expression 'img/bg/special/castle4.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_castle[0]))
    '[txt]'
    jump lb_castle
    
label lb_castle:
    show expression 'img/bg/special/castle4.jpg' as bg
    nvl clear
    $ txt = game.interpolate(random.choice(txt_place_castle[1]))
    '[txt]'    
    $ game.foe = Enemy('castle_guard', game_ref=game)
    $ chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Атаковать крепость':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_31
            $ txt = game.interpolate(random.choice(txt_place_castle[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 10
            '[game.dragon.reputation.gain_description]'                
            nvl clear
            call lb_castle_rob from _call_lb_castle_rob
        'Запомнить место и уйти' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('castle', 'castle_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_castle_rob:
    python:
        count = random.randint(3, 8)
        alignment = 'knight'
        min_cost = 100
        max_cost = 1000
        obtained = "Это предмет из разграбленной крепости."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Разграбить цитадель':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_castle[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_castle[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            $ text = u'%s принадлежала к одному из знатных родов королевства. Живя в неприступном замке, юная аристократка чувствовала себя в полной безопасности. А зря: драконам неведомо понятие "неприступный". \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_19     
            $ game.dragon.add_special_place('castle', 'castle_empty')
                                        
        'Запомнить место и уйти':
            $ game.dragon.add_special_place('castle', 'castle_empty')
            
    return
            
label lb_castle_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_castle[4]))
    '[txt]'   
    nvl clear
    menu:
        'Обустроить тут новое логово':
            $ game.create_lair('fortress_ruin')
            $ game.dragon.del_special_place('castle')
        
        'Покинуть пустой замок':
            $ game.dragon.add_special_place('castle', 'castle_empty')
            
    return

# Королевский замок
    
label lb_palace_found:
    show expression 'img/bg/special/castle5.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_palace[0]))
    '[txt]'
    jump lb_palace
    
label lb_palace:
    show expression 'img/bg/special/castle5.jpg' as bg
    nvl clear
    $ txt = game.interpolate(random.choice(txt_place_palace[1]))
    '[txt]'    
    $ game.foe = Enemy('palace_guards', game_ref=game)
    $ chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Атаковать замок':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_32
            $ txt = game.interpolate(random.choice(txt_place_palace[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 25
            '[game.dragon.reputation.gain_description]'                 
            nvl clear
            call lb_palace_rob from _call_lb_palace_rob
        'Запомнить место и уйти' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('palace', 'palace_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_palace_rob:
    python:
        count = random.randint(5, 10)
        alignment = 'knight'
        min_cost = 250
        max_cost = 2500
        obtained = "Это предмет из королевской сокровищницы."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Разграбить королевский дворец':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_palace[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_palace[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            $ text = u'%s принадлежала к одному из самых знатных родов королевства. Живя в роскошном дворце, юная аристократка чувствовала себя в полной безопасности. А зря: как известно, роскошь лишь раззадоривает драконов. \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_20     
            $ game.dragon.add_special_place('palace', 'palace_empty')
                                        
        'Запомнить место и уйти':
            $ game.dragon.add_special_place('palace', 'palace_empty')
            
    return
            
label lb_palace_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_palace[4]))
    '[txt]'   
    nvl clear
    menu:
        'Обустроить тут новое логово':
            $ game.create_lair('castle_ruin')
            $ game.dragon.del_special_place('palace')
        
        'Покинуть разграбленный замок':
            $ game.dragon.add_special_place('palace', 'palace_empty')
            
    return

# Жильё людоеда
    
label lb_enc_ogre:
    'Дракон некоторое время бродит по лесу...'
    show expression 'img/bg/special/cave_enter.jpg' as bg
    'И натыкается на вход в лесную пещеру, достаточно просторную, чтобы устроить внутри логово. Судя по запаху, логово себе там уже успел устроить великан-людоед.'
    jump lb_enc_fight_ogre
    
label lb_enc_fight_ogre:
    show expression 'img/bg/special/cave_enter.jpg' as bg   
    $ game.foe = Enemy('ogre', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Вызвать великана на бой':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_33
            '[game.dragon.name] победил.'
            jump lb_enc_explore_ogre_den
        'Запомнить место и уйти' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('ogre', 'enc_ogre')
            $ game.dragon.gain_rage()
    return
    
label lb_enc_explore_ogre_den:
    menu:
        'Обследовать пещеру':
            'В пещере прячется испуганная великанша. То ли дочь, то ли жена того огра, труп которого валяется снаружи.'
            $ description = game.girls_list.new_girl('ogre')
            $ text = u' Увидев дракона, %s лишь довольно оскалилась. Кажется, теперь у неё будет больше СНУ-СНУ! \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_gigant_sex     
            $ game.dragon.add_special_place('ogre', 'create_ogre_lair')
                                        
        'Запомнить место и уйти':
            $ game.dragon.add_special_place('ogre', 'create_ogre_lair')
            return
 
label lb_enc_create_ogre_lair:
    menu:
        'Пещера, в которой жил огр, теперь пуста. Но тут можно устроить своё логово, не слишком роскошное, однако всё же получше, чем открытый овраг в буреломной чащобе.'
        'Переместить логово':
            $ game.create_lair('ogre_den')
            $ game.dragon.del_special_place('ogre')
            return
        'Покинуть пещеру':
            $ game.dragon.add_special_place('ogre', 'create_ogre_lair')
            return
            

# Жльё морозного великана    

label lb_jotun_found:
    'Высоко в горах, где всё покрыто льдом и снегом стоит гигантский ледяной дворец. Интересно...'
    nvl clear
    jump lb_jotun
    
label lb_jotun:   
    show expression 'img/bg/lair/icecastle.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_jotun[0]))
    '[txt]'
    $ game.foe = Enemy('jotun', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Вызвать йотуна на бой':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_34
            jump lb_jotun_rob
        'Запомнить место и уйти' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('jotun', 'jotun_full')
            $ game.dragon.gain_rage()
    return
    
label lb_jotun_rob:
    menu:
        'Обследовать ледяную цитадель':
            $ txt = game.interpolate(random.choice(txt_place_jotun[1]))
            '[txt]'
            $ description = game.girls_list.new_girl('ice')
            $ text = u' Увидев гибель мужа, %s попыталась скрыться в глубине ледяного дворца, но дракон с лёгкостью отыскал свою жертву. \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_gigant_sex_1     
            $ game.dragon.add_special_place('jotun', 'jotun_empty')
                                        
        'Запомнить место и уйти':
            $ game.dragon.add_special_place('jotun', 'jotun_empty')
            return
 
label lb_jotun_empty:
    show expression 'img/bg/lair/icecastle.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_jotun[2]))
    '[txt]'
    menu:
        'Переместить логово'  if 'white' in game.dragon.heads:
            $ game.create_lair('ice_citadel')
            $ game.dragon.del_special_place('jotun')
        'Покинуть ледяную цитадель':
            $ game.dragon.add_special_place('jotun', 'jotun_empty')
    return 
    
# Жильё огненного великана
    
label lb_ifrit_found:
    'Над жерлом вулкана возвышается башня из чёрного обсидиана. Интересно, кто там живёт?'
    nvl clear
    jump lb_ifrit
    
label lb_ifrit:   
    show expression 'img/bg/lair/volcanoforge.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_ifrit[0]))
    '[txt]'
    $ game.foe = Enemy('ifrit', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Вызвать ифрита на бой':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_35
            jump lb_ifrit_rob
        'Запомнить место и уйти' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('ifrit', 'ifrit_full')
            $ game.dragon.gain_rage()
    return
    
label lb_ifrit_rob:
    menu:
        'Обследовать вулканическую кузню':
            $ txt = game.interpolate(random.choice(txt_place_ifrit[1]))
            '[txt]'
            $ description = game.girls_list.new_girl('fire')
            $ text = u' Увидев труп мужа, %s попыталась дать отпор дракону, но жар её тела лишь распалял похоть  ящера. \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_gigant_sex_2     
            $ game.dragon.add_special_place('ifrit', 'ifrit_empty')
                                        
        'Запомнить место и уйти':
            $ game.dragon.add_special_place('ifrit', 'ifrit_empty')
            return
 
label lb_ifrit_empty:
    show expression 'img/bg/lair/volcanoforge.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_ifrit[2]))
    '[txt]'
    menu:
        'Переместить логово'  if 'red' in game.dragon.heads:
            $ game.create_lair('vulcanic_forge')
            $ game.dragon.del_special_place('ifrit')
        'Покинуть вулканическую кузню':
            $ game.dragon.add_special_place('ifrit', 'ifrit_empty')
    return 

    
# Жильё тритона
    
label lb_triton_found:
    'Дракон проплывает вдоль прибрежной зоны...'
    show expression 'img/bg/lair/underwater.jpg' as bg
    'И обнаруживает подводную арку, украшенную кораллами и ракушками. Проём достаточно велик, чтобы внутрь мог заплыть даже кашалот.'
    nvl clear
    jump lb_triton
    
label lb_triton:  
    if not game.dragon.can_swim: 
      $ place = 'sea'
      hide bg
      show expression get_place_bg(place) as bg
      nvl clear
      '[game.dragon.name] пробует когтем солёную морскую влагу. Если бы только он умел дышать под водой...' 
      return
    show expression 'img/bg/lair/underwater.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_triton[0]))
    '[txt]'
    $ game.foe = Enemy('triton', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Вызвать тритона на бой':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_36
            jump lb_triton_rob
        'Запомнить место и уйти' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('triton', 'triton_full')
            $ game.dragon.gain_rage()
    return
    
label lb_triton_rob:
    menu:
        'Обследовать подводные хоромы':
            $ txt = game.interpolate(random.choice(txt_place_triton[1]))
            '[txt]'
            $ description = game.girls_list.new_girl('siren')
            $ text = u' %s слишком поздно услышала подозрительный шум. Приплыв на место битвы, она обнаружила труп мужа и ящера, похотливо разглядывающего её тело. \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_gigant_sex_3    
            $ game.dragon.add_special_place('triton', 'triton_empty')
                                        
        'Запомнить место и уйти':
            $ game.dragon.add_special_place('triton', 'triton_empty')
            return
 
label lb_triton_empty:
    show expression 'img/bg/lair/underwater.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_triton[2]))
    '[txt]'
    menu:
        'Переместить логово' if 'blue' in game.dragon.heads:
            $ game.create_lair('underwater_mansion')
            $ game.dragon.del_special_place('triton')
        'Покинуть подводные хоромы':
            $ game.dragon.add_special_place('triton', 'triton_empty')
    return 
    
# Жильё титана
    
label lb_titan_found:
    'Дракон поднимается над облаками...'
    show expression 'img/bg/special/cloud_castle.jpg' as bg
    'И обнаруживает летающий остров с прекрасным замком. Интересно, кто его построил?'
    nvl clear
    jump lb_titan
    
label lb_titan:   
    if not game.dragon.can_fly: 
      $ place = 'sky'
      hide bg
      show expression get_place_bg(place) as bg    
      nvl clear
      '[game.dragon.name] с тоской смотрит в небо. Если бы только он умел летать...'
      return
    show expression 'img/bg/special/cloud_castle.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_titan[0]))
    '[txt]'
    $ game.foe = Enemy('titan', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Вызвать титана на бой':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_37
            $ game.dragon.reputation.points += 10
            '[game.dragon.reputation.gain_description]'   
            jump lb_titan_rob
        'Запомнить место и уйти' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('titan', 'titan_full')
            $ game.dragon.gain_rage()
    return
    
label lb_titan_rob:
    menu:
        'Обследовать облачный замок':
            $ txt = game.interpolate(random.choice(txt_place_titan[1]))
            '[txt]'
            $ description = game.girls_list.new_girl('titan')
            $ text = u' %s расчёсывалась перед зеркалом, сидя в своей комнате на вершине самой высокой башни. Она даже не подозревала, что замок - захвачен, её муж - убит, а сама титанида уже сталаа добычей мерзкого ящера. \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_gigant_sex_4  
            $ game.dragon.add_special_place('titan', 'titan_empty')
                                        
        'Запомнить место и уйти':
            $ game.dragon.add_special_place('titan', 'titan_empty')
            return
 
label lb_titan_empty:
    show expression 'img/bg/lair/cloud_castle.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_titan[2]))
    '[txt]'
    menu:
        'Переместить логово' if game.dragon.wings>0:
            $ game.create_lair('cloud_castle')
            $ game.dragon.del_special_place('titan')
        'Покинуть облачный замок':
            $ game.dragon.add_special_place('titan', 'titan_empty')
    return 
    
# Подгорное царство цвергов

label lb_backdor:
    show expression 'img/bg/special/backdor.jpg' as bg
    'Эта потайная дверь в царство цвергов обозначена на найденных в бастионе чертежах как "задний проход". В отличие от главных ворот, тут нет своей линии обороны, и любой, кто знает секрет, сможет пробраться внутрь. Конечно, внутри всё равно придётся столкнуться с армией цвергов, но пробраться тут всё же проще, чем через центральные укрепления.'
    nvl clear
    menu:
        'Пора вороватъ и убиватъ!':
            $ game.dragon.drain_energy()
            stop music fadeout 1.0
            play music "mus/moria.ogg"
            $ renpy.music.queue(get_random_files('mus/ambient'))           
            show expression 'img/bg/special/moria.jpg' as bg
            'Нажав на неприметный камушек в правильном месте, [game.dragon.name] открыл потайной проход в подгорное царство. Теперь отступать не стоит, если цвергов не добить, то они запечатают задний проход и укрепятся ещё основательнее.'
            $ game.dragon.add_special_place('backdor', 'backdor_sealed')
            jump lb_dwarf_army    
        'Для такого дела нужна подготовка...':
            return
            
    return


label lb_backdor_sealed:
    show expression 'img/bg/special/backdor.jpg' as bg
    'Когда-то тут был тайный проход в подгорное царство, но во время нападения цверги обрушили тоннель, завалив его камнями. Ох и любят же коротышки эти взрывы...'
    nvl clear
    return
    
label lb_frontgates:
    'Укреплённые неприступыми бастионами, эти внушительные металлические врата надёжно закрывают единственный(?) вход в подгорное царство. Там, в глубине, таятся невероятные сокровища, равных которым нету ни у кого из наземных королей, но пробраться внутрь под силу только кому то очень-очень могучему.'
    show expression 'img/bg/special/gates_dwarf.jpg' as bg
    nvl clear
    menu:
        'Проломить ворота' if game.dragon.size > 3:
            'Жалкие укрепления коротышек не смогут устоять перед яростным отродьем Госпожи. [game.dragon.fullname] достаточно огромен и могуч, чтобы проломиться сквозь ворота и ворваться в подгорное царство. Однако теперь отступать нельзя - если цвергов не прогнать, они укрепятся заново.'
            $ game.dragon.add_special_place('backdor', 'backdor_sealed')
            $ game.dragon.drain_energy()
            call lb_golem_guard from _call_lb_golem_guard
        'Убраться, пока они не зарядили пушки...':
            'Шататься перед главными воротами цвергов без дела будет не лучшей идеей, они ведь могут и пальнуть чем нибудь...'
            $ game.dragon.gain_rage()
        
    return
    
label lb_golem_guard:
    stop music fadeout 1.0
    play music "mus/moria.ogg"
    $ renpy.music.queue(get_random_files('mus/ambient')) 
    show expression 'img/bg/special/moria.jpg' as bg
    'Даже после того, как врата обрушились, пыль и мелкие камушки продолжают сыпаться с потолка. По центральной галерее гулко раздаются шаги стража ворот - выкованного целиком из закалённого адамантия механического гиганта. На свете немного противников, равных ему по силе...'
    $ game.foe = Enemy('golem', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Сразиться с механическим стражем':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_38
            jump lb_dwarf_army
        'Бежать поджав хвост' if game.dragon.bloodiness < 5:
            'Сегодня коротышкам повезло, но даже если они восстановят ворота, недолго им осталось пребывать в покое...'
            $ game.dragon.gain_rage()
    
    return
    
label lb_dwarf_army:
    'Подобно несущему смерть урагану [game.dragon.fullname] ворвался во внутренние палаты подгорного царства. Однако цверги всё ещё не беззащитны, дорогу дракону заступает в спешке собранный ударный отряд...'
    $ game.foe = Enemy('dwarf_guards', game_ref=game)
    $ narrator(show_chances(game.foe))
    menu:
        'Атаковать без жалости':
            call lb_fight from _call_lb_fight_39
            'Теперь, когда основные силы цвергов разбиты и деморализованы, надо выбрать направление финального удара. Ремесленные кварталы почти беззащиты, и там цвергов можно будет перебить во множестве, пока они не успели сбежать. С другой стороны, самые главные ценности должны храниться ниже, в главной сокровищнице. Если не наведаться туда прямо сейчас, хитрые цверги вынесут всё до последней монетки.'
            menu:
                'Вниз - за сокровищами!':
                    call lb_dwarf_treashury from _call_lb_dwarf_treashury
                    
                'Разорить ремесленные цеха':
                    call lb_dwarf_houses from _call_lb_dwarf_houses
                    
                'Отступить':
                    'Обидно отступать, когда победа была так близка, но загнанные в угол цверги могут быть крайне опасными противниками. Иногда лучше не рисковать!'
                    $ game.dragon.gain_rage()
                    
        'Бежать поджав хвост':
            'Сегодня коротышкам повезло, но даже если они восстановят ворота, недолго им осталось пребывать в покое...'
            $ game.dragon.gain_rage()
    return
    
label lb_dwarf_houses:
    'Хотя большинство цвергов бегают в панике и пытаются спасти себя и свои пожитки, при виде дракона многие хватаются за ломы, кирки и топоры, чтобы дать отпор супостату...'
    $ game.foe = Enemy('dwarf_citizen', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Наброситься на цвергов':
            call lb_fight from _call_lb_fight_40
            $ game.history = historical( name='dwarf_ruined',end_year=game.year+15,desc='Неутомимые цверги вновь возвели Подгорные чертоги. Карликовая крепость готова к веселью! ',image='img/bg/special/dwarf_fortress.jpg')
            $ game.history_mod.append(game.history)
            call lb_dwarf_ruins from _call_lb_dwarf_ruins
        'Отступить':
            'Обидно отутпать, когда победа была так близка, но загнанные в угол цверги могут быть крайне опасными противниками. Иногда лучше не рисковать!'
            $ game.dragon.gain_rage()        
    return
    
label lb_dwarf_treashury:
    'Понимая, что их королевство стоит на грани катастрофы, цверги пытаются спасти две самые большие ценности - короля и сокровища. Бойцов у них осталось немного, однако среди них есть один равный по силе целой армии - закованный в доспехи до самых глаз чемпион цвергов выступает вперёд, потрясая массивным, но острым топором.'
    $ game.foe = Enemy('dwarf_champion', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Сразиться с чемпионом':
            call lb_fight from _call_lb_fight_41
            $ game.dragon.reputation.points += 25
            '[game.dragon.reputation.gain_description]'     
            call lb_dwarf_rob from _call_lb_dwarf_rob
        'Бежать поджав хвост':
            'Обидно отутпать, когда победа была так близка, но загнанные в угол цверги могут быть крайне опасными противниками. Иногда лучше не рисковать!'
            $ game.dragon.gain_rage()      
    return

label lb_dwarf_rob:
    python:
        count = random.randint(12,15)
        alignment = 'dwarf'
        min_cost = 500
        max_cost = 5000
        obtained = "Это предмет из сокровищницы короля-под-горой."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Разграбить сокровищницу цвергов':
            show expression 'img/bg/hoard/base.jpg' as bg
            'Подлые цверги многое успели растащить, но даже от того, что осталось, разбегаются глаза. Нигде больше не найти столь богатой добычи!'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            $ game.history = historical( name='dwarf_ruined',end_year=game.year+15,desc='Неутомимые цверги вновь возвели Подгорные чертоги. Карликовая крепость готова к веселью! ',image='img/bg/special/dwarf_fortress.jpg')
            $ game.history_mod.append(game.history)
            call lb_dwarf_ruins from _call_lb_dwarf_ruins_1
                                        
        'Запомнить место и уйти':
            $ game.dragon.add_special_place('palace', 'palace_empty')
    return
            
label lb_dwarf_ruins:
    show expression 'img/bg/special/moria.jpg' as bg
    'Когда-то тут жили цверги, но теперь это место опустошено и заброшено. Внутри можно устроить просторное и отлично защищённое логово.'
    menu:
        'Переместить сюда логово':
            $ game.create_lair('underground_palaces')
            $ game.dragon.del_special_place('frontgates')
            $ game.dragon.del_special_place('backdor')
        'Покинуть подгорные чертоги':
            $ game.dragon.add_special_place('frontgates', 'frontgates_open')
    return 
