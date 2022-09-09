﻿# coding=utf-8
init python:
    from pythoncode.utils import weighted_random
    from pythoncode.characters import Enemy
        
label lb_location_forest_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))    
    $ place = 'forest'
    hide bg
    show expression get_place_bg(place) as bg
    nvl clear
    
    if game.dragon.energy() == 0:
        'Даже драконам надо иногда спать. Особенно драконам!'
        return
    if game.witch_st1==5:
      'Дракон на мгновение задумывается, какой может быть награда ведьмы.'
      game.dragon 'Надо сходить проверить!'
      return        
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_enc_lumberjack", 10),
        ("lb_enc_onegirl", 10),
        ("lb_enc_wandergirl", 10),
        ("lb_enc_ogre", 10),
        ("lb_enc_deer", 10),
        ("lb_enc_boar", 10),
        ("lb_enc_berries", 10),
        ("lb_enc_shrooms", 10),
        ("lb_enc_guardian", 10),
        ("lb_enc_lumbermill", 10),
        ("lb_forest_elfgirl",15),
        ("lb_enc_klad", 5),
        ("lb_enc_domiki", 3),
        ("lb_summon_forest", 5 * game.desperate),
        ("lb_patrool_forest", 3 * game.mobilization.level),
        ("lb_enc_noting", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    
    return
    
label lb_summon_forest:  # Призыв на равнинах
    if game.summon.seal>data.max_summon:
      jump lb_location_forest_main   # При уже вызванном демоне встречи не происходит.
    else:
      'Выйдя на глухую лесную поляну, дракон обнаружил кое-что любопытное...'
      call lb_summon from _call_lb_summon_2
    return

label lb_enc_domiki:
    if "domiki_done" in persistent.easter_eggs:
        jump lb_location_forest_main
    $ persistent.easter_eggs.append("domiki_done")
    "ВНЕЗАПНО! Из лесной чащи на дракона набигает..."
    show expression 'img/scene/fight/domik.jpg' as bg    
    'ДЕРЕВЯННЫЙ ДОМИК?!!!! Видимо, это легендарное творение древнего безумного странствующего Архимага Кирилла "Коровануса"  - боевой деревянный голем. Он явно агрессивен...'
    $ game.foe = Enemy('domik', game_ref=game)    
    $ chances = show_chances(game.foe)   
    call lb_fight from _call_lb_fight_69    
    'Среди обломков домика находится табличка: "Изготовлено по заказу Злого (имя я пока не придумал)". Что за безумное и гениальное творение...'
    return

label lb_enc_lumberjack:
    'Неподалёку слышны ритмичные удары, гулко разносящиеся по всему лесу. Похоже на топор дровосека. Сам по себе дровосек добыча совершенно безынтересная, но время сейчас как раз обеденное, а по человеческой традиции еду работающим вдали от дома приносит старшая из незамужих дочерей. Стоит подкрасться и поглядеть...'
    nvl clear
    python:
        if game.dragon.size < 3: 
            succes = True
        else:
            succes = False
    if succes: 
        '[game.dragon.name] припадает к земле и медленно, стараясь не шуметь, пробирается в сторону шума. К счастью, дровосек слишком занят своей интересной и творческой работой, чтобы заметить, что в соседних кустах пристраивается гигантский ящер. Теперь остаётся только подождать...'
        nvl clear
        menu:
            'Наблюдать из засады':
                $ game.dragon.drain_energy()
                $ description = game.girls_list.new_girl('peasant')
                $ text = u'%s несла обед своему отцу-дровосеку - и наткнулась на затаившегося дракона. Увы, крадущегося тигра поблизости не оказалось! \n\n' % game.girl.name
                $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
                'Не прошло и часа, как на тропинке появляется ещё одна фигура, женская. У неё в руках тяжелая корзинка, накрытая белой тряпицей. [game.dragon.name] втягивает нозрями воздух и определяет с точностью - девица! Хотя и низкородная...'
                game.girl 'Папааааш! Я тебе покушать принесла. У меня тут в корзинке сладкий хлеб.'
                nvl clear
                'Девушка бежит к отцу, чтобы обнять его, но тот замирает в ужасе, глядя за спину дочери, где в полный рост встаёт [game.dragon.name]. Не давая людям опомниться, [game.dragon.name] убивает дровосека и сбивает с ног его дочь.'
                $ game.dragon.reputation.points += 1
                '[game.dragon.reputation.gain_description]'
                nvl clear
                game.girl.third "[description]"
                call lb_nature_sex from _call_lb_nature_sex_21      
                return        
            'Оставить его в покое' if game.dragon.bloodiness < 5:
                $ game.dragon.gain_rage()
    else: 
        'Припадает к земле и медленно, стараясь не шуметь, пробирается в сторону шума. Но он слишком велик для таких фокуов, конечно же, дровосек слышит пыхтение и треск ломающихся молодых деревьев и, бросив в ужасе топор, убегает прочь. Какая досада...' 
        $ if game.dragon.bloodiness < 5: game.dragon.gain_rage()
            
    return
    
    
label lb_enc_onegirl:
    'Если затаиться у лесной тропинки, то рано или поздно по ней пройдёт кто-нибудь. Вот, например, на этот раз на тропинке показывается молодая крестьянка с корзинкой. Видимо, несёт обед работающему в лесу отцу или брату.'
    nvl clear
    menu:
        'Поймать девицу':
            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl('peasant')
            $ text = u'%s несла обед своему отцу-дровосеку - и на узкой лесной тропинке наткнулась на дракона. \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            '[game.dragon.name] вываливается на дорогу, проламываясь сквозь кусты. Крестьянка в ужасе бросает корзинку и замирает от ужаса. Похоже она даже бежать не собирается... впрочем, это было бы бессмысленно.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_22      
        'Отпустить её' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return

label lb_enc_wandergirl:
    'Из лесной чащи доносятся крики "Ау!", голос женский, молодой. Видимо, девушка отбилась от группы в лесу и заблудилась. Надеется, что её кто-нибудь услышит. Ну, вот её услышал дракон. Интересно, станет ли ей от этого легче?'
    nvl clear
    menu:
        'Позвать девицу':
            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl('peasant')
            $ text = u'Заблудиться в лесу - незавидная участь. %s пыталась найти дорогу обратно. Кто же знал, что на её крик "Ау!" откликнется дракон? \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            'Драконы очень коварны и талантливы. Одно из многих их замечательных умений - это умение подделывать голоса. Стоит откликнуться на зов девушки по человечески, и вот она уже сама бежит к тебе в лапы!'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_23      
        'Отпустить её' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return

label lb_enc_deer:
    'В чаще леса пасётся матёрый откормленный олень. Неплохая закуска, но ничего особенного. Сойдёт, если в животе урчит.'
    nvl clear
    menu:
        'Сожрать оленя' if game.dragon.hunger > 0:
            $ game.dragon.drain_energy()
            '[game.dragon.name] ловит и пожирает оленя.'
            python:
                if game.dragon.bloodiness > 0:
                    game.dragon.bloodiness = 0
                game.dragon.hunger -= 1
        'Разорвать оленя' if game.dragon.bloodiness >= 5 and game.dragon.hunger == 0:
            $ game.dragon.drain_energy()
            '[game.dragon.name] жестоко задирает оленя просто ради забавы.'    
        'Просто шугануть' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return

label lb_enc_boar:
    'Хм. На тропинке, ведущей к водопою, чётко отпечатались чьи-то следы. Похоже, эту полянку обжило какое-то парнокопытное. '
    nvl clear
    jump lb_boar

label lb_boar:
    $ place = 'forest'
    hide bg
    show expression get_place_bg(place) as bg
    nvl clear
    'Ветер доносит запах крупного зверя. В подлеске шуршит гигантский вепрь. Более метра в холке, толстокожий и массивный зверь вооружён огромными загнутыми клыками. Он не боится никого в лесу - непростая добыча, но она позволит набраться сил перед более серьёзными сражениями.'
    $ game.foe = Enemy('boar', game_ref=game)
    $ chances = show_chances(game.foe)
    nvl clear
    menu:
        'Сразиться с вепрем':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_53
            if game.dragon.hunger > 0:
                '[game.dragon.name] съедает поверженного вепря. Сила, заключённая в мясе старого кабана, придаст ударам дракона убийственную мощь.'
                python:
                    if game.dragon.bloodiness > 0:
                        game.dragon.bloodiness = 0
                    game.dragon.hunger -= 1
                    game.dragon.add_effect('boar_meat')
            else:
                'Дракон торжествует победу.'
            $ game.dragon.del_special_place('boar')
        'Запомнить место и уйти' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('boar', 'enc_boar')
            $ game.dragon.gain_rage()
    
    return
    
label lb_enc_guardian:
    $ elf_ruined = game.historical_check('elf_ruined')
    if elf_ruined:
        jump lb_location_forest_main
    $ txt = game.interpolate(random.choice(txt_enc_forest_guardian[0]))
    '[txt]'
    show expression 'img/scene/fight/elf_ranger.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_enc_forest_guardian[1]))
    $ game.foe = Enemy('elf_ranger', game_ref=game)
    '[txt]'
    $ chances = show_chances(game.foe)
    nvl clear
    menu:
        'Атаковать стража':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_54
            python:
                txt = game.interpolate(random.choice(txt_enc_forest_guardian[2]))
                if game.dragon.magic > 0:
                    txt = game.interpolate(random.choice(txt_enc_forest_guardian[3]))
                    game.dragon.add_special_place('enchanted_forest', 'enter_ef')
            '[txt]'
        'Отступить' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            return            
    return

label lb_forest_elfgirl:
    $ elf_ruined = game.historical_check('elf_ruined')
    if not elf_ruined:
        jump lb_location_forest_main
    '[game.dragon.name] слышит непередаваемый аромат, сотканный из ноток невинности, красоты и колдовских чар. Это лесная ведьма из народа богини Дану. Альвы, лишённые священного Древа, вынуждены скитаться по простым лесам, в которых их может отыскать кто угодно. Например, дракон.'
    $ game.foe = Enemy('elf_witch', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Напасть на фею':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_72
            'Несмотря на жестокое сопротивление, чародейка не получила особых повреждений. Она теперь безащитна, но цела... пока что.'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            $ description = game.girls_list.new_girl('elf')
            $ text = u' %s настороженно пробиралась по густому и враждебному лесу. Но вся её осторожность не помогла альве: внезапная встреча с драконом привела к унизительному и страшному поражению. \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_34      
        
        'Тихонько уйти прочь' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()        
    return

label lb_enc_lumbermill:
    show expression 'img/bg/special/lumbermill.jpg' as bg
    'На берегу лесной реки стоит деревянное здание, заключающее в себе какой-то огромный механизм, приводимый в движение водяным колесом. Скорее всего, люди тут обрабатывают древесину.'
    nvl clear
    python:
        doit = False
        if 'fire_breath' in game.dragon.modifiers(): 
            doit = True
    menu:
        'Дыхнуть огнём' if doit:
            $ game.dragon.drain_energy()
            "[game.dragon.name] изрыгает на здание поток всепожирающего пламени. Сухое дерево тут же занимается, и вскоре лесопилка сгорает. Теперь у людей будет меньше строительных материалов для их домов и замков."
            $ game.poverty.value += 1
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Наколдовать синее пламя' if game.dragon.mana > 0:
            $ game.dragon.drain_energy()
            $ game.dragon.drain_mana()
            "[game.dragon.name] произносит заклинание, призывающее магический огонь. Сухое дерево тут же занимается, и вскоре лесопилка сгорает. Теперь у людей будет меньше строительных материалов для их домов и замков."
            $ game.poverty.value += 1
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Обследовать здание' if game.dragon.size <= 3 and game.dragon.magic == 0:
            $ game.dragon.drain_energy()
            "[game.dragon.name] тщательно обследует необычное строение на предмет важности и уязвимых мест. Вращаемое потоком воды колесо приводит в движение скрытые внутри здания пилы, при помощи которых люди изготавливают из брёвен доски. Огромный штабель готовой продукции сложен неподалёку. Если бы только было чем это всё поджечь..."
            'Только время зря потерял. Придётся уйти несолоно хлебавши.'
        'Пройти мимо' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    
    return
    
label lb_enc_klad:
    'Дракон учуял зарытые сокровища.'
    nvl clear
    python:
        tr_lvl = random.randint(1, 100)
        count = random.randint(1, 10)
        alignment = 'human'
        min_cost = 1 * tr_lvl
        max_cost = 10 * tr_lvl
        obtained = "Это предмет из клада, зарытого кем-то в лесу."
        trs = treasures.gen_treas(count, data.loot['klad'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Отыскать и раскопать':
            $ game.dragon.drain_energy()
            'Под корнями старого дуба закопан древний, уже слегка подгнивший сундук. Внутри лежит:'
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            
        'Пусть пока лежат' if game.dragon.bloodiness < 5:
            'Конечно, сокровища полезны, но то, что тут могли закопать жалкие людишки, вряд ли стоит драгоценного времени благородного змея.'
    return

label lb_patrool_forest:
    python:
        chance = random.randint(0, game.mobilization.level)
        if chance < 4:
            patrool = 'jagger'
            dtxt = 'Леса патрулирует королевский егерь - следопыт, вооруженный длинным тисовым луком и острым кинжалом.'
        elif chance < 7:
            patrool = 'footman'
            dtxt = 'По лесной дороге марширует отряд солдат. Похоже, они патрулируют местность в поисках разбойников и чудовищ. Ну, одно они нашли...'
        elif chance < 11:
            patrool = 'heavy_infantry'
            dtxt = 'Лесные дороги патрулируются отрядами тяжелой пехоты. Если люди так сильно пекутся о безопасности лесов, что решили послать туда элитных бойцов, значит, они действительно напуганы.'
        elif chance < 16:
            patrool = 'griffin_rider'
            dtxt = 'Пронзительный клич раздаётся с небес - это всадник на грифоне пикирует с высоты, завидев между деревьями блеск драконьей чешуи.'
        else:
            patrool = 'angel'
            dtxt = '%s вынужден зажмуриться от яркого света, бьющего в глаза. Громогласный оклик возвещает: "Умри, мерзкое порождение греха!!!". Это ангел-хранитель, посланный людям Небесами для защиты.' % game.dragon.name
    '[dtxt]'
    python:
        game.foe = Enemy(patrool, game_ref=game)
        battle_status = battle.check_fear(game.dragon, game.foe)
    if 'foe_fear' in battle_status:
        $ narrator(game.foe.battle_description(battle_status, game.dragon))
        return
    $ game.dragon.drain_energy()
    call lb_fight(skip_fear=True) from _call_lb_fight_55
    return
