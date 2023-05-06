# coding=utf-8
init python:
    from pythoncode import battle
    from pythoncode.characters import Enemy, Talker
#    import treasures
    
    reinforcement_used = False
    refuse = False
    mistress_in_battle = False
    
label lb_location_mordor_main:
    $ reinforcement_used = False
    $ place = 'mordor' 
    hide bg
    show place as bg
    python:
        if renpy.music.get_playing(channel='music') != "mus/dark.ogg":
            renpy.music.play("mus/dark.ogg")
            renpy.music.queue(get_random_files('mus/ambient'))
    nvl clear
    python:
        mistress = Talker(game_ref=game)
        mistress.avatar = "img/avahuman/mistress.jpg"
        mistress.name = "Владычица"
    
    menu:
        'В земли Вольных Народов':
            if game.first_meet:  # Первая встреча с ведьмой
              call lb_witch_first_meet from _call_lb_witch_first_meet
            $ pass
        'Армия Тьмы':
            show expression 'img/bg/special/army.jpg' as bg
            '[game.army.army_description]'
            nvl clear
            menu:
                'Собрать армию и начать войну!' if not freeplay:
#                'Собрать армию и начать войну!':
                    python:
                      renpy.music.play(get_random_files('mus/battle'))
                    $ game.vini_vidi_vici = True
                    $ renpy.call_screen("border_map") 
                # @fdsc всегда можно сразу отдать сокровища
                # 'Отдать сокровища для оснащения армии' if freeplay and game.lair.treasury.wealth > 0:
                'Отдать сокровища для оснащения армии' if (freeplay or game.is_quest_has_been_completed) and game.lair.treasury.wealth > 0:
                    '[game.dragon.name], рыдая от невыносимого горя, отдаёт все свои сокровища для подготовки вторжения'
                    $ game.dragon.gain_rage(gain=5)
                    $ game.army.money += game.lair.treasury.wealth
                    $ game.lair.treasury = treasures.Treasury()
                'Продолжить подготовку':
                    'Армия пока не готова.'

            call lb_location_mordor_main from _call_lb_location_mordor_main
            
        'Аудиенция с владычицей' if game.mistress_alive: # if not freeplay:
            jump lb_mistress
#        'Уйти на покой':
#            menu:
#                "Это действие сбросит текущую игру и позволит начать заново!"
#                "Сдаешься?"
#                "Да":
#                    python:
#                        if not freeplay:
#                            renpy.unlink_save("1-1")
#                            renpy.full_restart()
#                        else:
#                            renpy.unlink_save("1-3")
#                            renpy.full_restart()
#                "Нет":
#                    return
    return
    
label lb_mistress:
    python:
        if not persistent.isida_done:
            renpy.movie_cutscene("mov/isida.webm")
            persistent.isida_done = True
    nvl clear
    show expression 'img/scene/mistress.jpg' as bg    
    menu:
        'Получить награду' if game.is_quest_complete:
            if game.witch_st1>1:
              mistress 'Вижу, ты уже связался с ведьмой, живущей в старых руинах? Рано или поздно мы уничтожим эту шлюху, но пока сотрудничать с ней полезно. Иди и выполни её просьбу!'
              return
            # Разбираемся с пленницами
            if game.girls_list.prisoners_count > 0:
              $ game.dragon.third(u"Направляясь к Тёмной госпоже, дракон выпускает пленниц.")
            $ game.girls_list.free_all_girls()
            call lb_event_sleep_new_year from _call_lb_event_sleep_new_year_1
            $ game.girls_list.next_year()
            $ game.remove_history()
            show expression 'img/scene/mistress.jpg' as bg 
            # Если делаем подарок - удаляем его из списка сокровищ
            if game.quest_task == 'gift' and len(game.lair.treasury.jewelry) > 0:
                $ del game.lair.treasury.jewelry[game.lair.treasury.most_expensive_jewelry_index]
            game.dragon 'Я выполнил твоё задание. Помнится, мне была обещана награда...'    
            mistress 'Иди ко мне, милый. Ты не пожалеешь, обещаю.'
            call lb_mistress_fuck from _call_lb_mistress_fuck
            call lb_choose_dragon from _call_lb_choose_dragon
            return
        'Уточнить задание' if not game.is_quest_complete and not freeplay:
            "Текущее задание:\n[game.quest_text]\n[game.quest_time_text]"
            call lb_mistress from _call_lb_mistress
        'Завести разговор':
            $ txt = game.interpolate(random.choice(txt_advice))
            mistress '[txt]'   
            nvl clear            
            call lb_mistress from _call_lb_mistress_1
        'Предательски напасть':
            game.dragon 'Независимо от того, выиграю ли я эту битву, мой род прервётся. Стоит ли убивать свою мать?'
            menu:
                'Она не смеет повелевать мной!':
                    $ game.mistress_alive=False
                    jump lb_betrayal
                'Она же всё-таки Мать...':
                    'От Госпожи не укрылось напряжение сына, но она лишь загадочно улыбнулась, не высказывая ни малейшего беспокойства.'
                    call lb_location_mordor_main from _call_lb_location_mordor_main_1
        'Лизнуть её руку и уйти':
            'Иногда просто хочется прикоснуться к ней ещё раз...'  
            call lb_location_mordor_main from _call_lb_location_mordor_main_2
    return

label lb_location_mordor_questtime_completed:
    'Квест был выполнен. Вы можете продолжать играть дальше или пойти к Владычице получить новый квест'
    menu:
        'Пока продолжить':
            return False
        'Идти к Владычице':
            return True

    return True

label lb_location_mordor_questtime:
    $ place = 'mordor' 
    show place as bg
    show screen status_bar
    if game.is_quest_complete:
        mistress '[game.dragon.name], ты слишком много времени тратишь на игры с людьми, я устала ждать. Разве ты забыл о своём задании?'
        game.dragon 'Отнюдь, Владычица, я сделал всё, о чём ты просила. Вот. Смотри.'
        mistress 'Великолепно. В таком случае, тебе полагается заслуженная награда. Иди ко мне, милый.'
        call lb_mistress_fuck from _call_lb_mistress_fuck_1
        call lb_choose_dragon from _call_lb_choose_dragon_1
    else:
        $ game.dragon.die()
        mistress 'Отпущенное тебе время истекло, [game.dragon.name]. И я спрошу лишь один раз: выполнил ли ты моё задание?'
        game.dragon 'Я не успел, Владычица. Мне нужно ещё немного времени. Прости меня.'
        mistress 'Я не обижаюсь. Но и жалость мне не ведома. Ты подвёл меня, а это можно сделать лишь однажды. Продолжателем рода станет кто-то другой, ты же доживай свои дни как пожелаешь. Изыди с глаз моих!'
        menu:
            "Дать шанс другому дракону":
                call lb_choose_dragon from _call_lb_choose_dragon_2
                return
    return
    

label lb_mistress_fuck:
    mistress 'Я могу принять любой облик, приятный тебе. Выбирай, какой ты хочешь меня видеть?'
    menu:
        'Облик прекрасной девы, мне милее всего':
            show expression sex_imgs("mistress") as xxx
            pause (500.0)
            $ txt = game.interpolate(random.choice(txt_human_mistress_fuck[game.dragon.kind]))
            '[txt]'    
            hide xxx
        'Стань драконицей, я устал от немощных смертных дев':
            show expression sex_imgs("dragon") as xxx
            pause (500.0)            
            $ txt = game.interpolate(random.choice(txt_dragon_mistress_fuck[game.dragon.kind]))
            '[txt]'
            hide xxx
    show expression 'img/scene/mistress.jpg' as bg
    mistress 'Благодарю тебя за твоё могучее семя, сын мой. Наши дети превзойдут всех рождённых ранее.'
    game.dragon 'Пусть мои сыновья продолжат моё дело, когда вырастут.'
    mistress 'Когда они вылупятся, ты должен будешь выбрать своего преемника, возлюбленный мой.'
    nvl clear
    'Прошло девять месяцев, и кладка новых яиц проклюнулась...'
    python:
        if not persistent.lada_done:
            renpy.movie_cutscene("mov/lada.webm")
            persistent.lada_done = True    
    return

label lb_betrayal:
    $ renpy.movie_cutscene("mov/kali.webm")
    $ atk_tp = 'pysical'
    $ mistress_hp = 3
    call lb_new_round from _call_lb_new_round
    return

label lb_new_round:
    nvl clear    
    if mistress_hp < 1:
        mistress 'Я ещё вернусь!'
        if not freeplay:
          $data.achieve_target("betray", "win")
          $ game.win()
          jump lb_you_win
        else:
          game.dragon 'Ура! Я убил собственную мать! Э? Ура?'
    else:
      $ aspect = 'lb_' + random.choice(['kali','garuda','shiva','agni','indra','pangea','nemesis','amphisbena','gekata','hell',])
      $ renpy.call(aspect)
    return

label lb_tactics_choice:
    menu:
        'Рвать зубами':
            $ atk_tp = 'physical'
        'Ударить заклятьем' if game.dragon.mana > 0:
            $ atk_tp = 'magic'
        'Изрыгнуть пламя' if 'fire_breath' in game.dragon.modifiers():
            $ atk_tp = 'fire'
        'Леденящее дыхание' if 'ice_breath' in game.dragon.modifiers():
            $ atk_tp = 'ice'
        'Громовой рёв' if 'sound_breath' in game.dragon.modifiers():
            $ atk_tp = 'thunder'
        'Ужалить ядом'  if 'poison_breath' in game.dragon.modifiers() or 'poisoned_sting' in game.dragon.modifiers():
            $ atk_tp = 'poison'
        'Взмыть в небеса' if game.dragon.can_fly:
            $ atk_tp = 'air'
        'Зарыться под землю' if 'can_dig' in game.dragon.modifiers(): #TODO надо понять как это правильно проверить
            $ atk_tp = 'earth'
        'Юлить и уклоняться':
            $ atk_tp = 'dodge'
        'Спрятаться и затихнуть':
            $ atk_tp = 'hide'
    return

label lb_kali:
    show expression 'img/scene/fight/mistress/kali.jpg' as bg    
    'Владычица принимает облик многорукой богини Кали, с чёрной как уголь кожей и красным словно кровь языком. Она вооружена несколькими острыми серпами и очень опасна в ближнем бою.'
    call lb_tactics_choice from _call_lb_tactics_choice
    if game.dragon.defence_power()[1] > 0:
        game.dragon 'Мою чешую невозможно разрубить, Мать. Ты родила меня неуязвимым!'
    else:
        'Одним взмахом острого серпа Кали отрубает голову дракона.'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'Вот и всё, сынок... ты зря решил встать на путь Иуды.'
            jump lb_game_over
        else:
            mistress 'Одной головой меньше, сынок. Жаль, это уже не прибавит тебе ума!'
            
    if atk_tp == 'magic':
        game.dragon 'Твои серпы не защитят тебя от магии смерти, многорукая!!!'
        $ mistress_hp -= 1
    else:
        mistress 'Так меня не одолеть, глупец!'
    call lb_new_round from _call_lb_new_round_1
    return

label lb_garuda:
    show expression 'img/scene/fight/mistress/garuda.jpg' as bg    
    'Целиком покрывшись яркими перьями и отрастив острые медные когти, Владычица принимает аспект Гаруды. Ни на земле, ни в небесах нет места, чтобы укрыться от её соколиного удара, но всё же сейчас она очень уязвима.'
    call lb_tactics_choice from _call_lb_tactics_choice_1
    if atk_tp == 'earth':
        game.dragon 'Под землёй тебе меня не достать, пернатая тварь!'
    else:
        'С невероятной силой Гаруда терзает дракона когтями и отрывает ему голову.'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'От змеи рождённый, умри как червь!'
            jump lb_game_over
        else:
            mistress 'Всё ещё жив, змеёныш?!'
        
    if atk_tp != 'dodge' and atk_tp != 'hide' and atk_tp != 'earth' and atk_tp != 'air':
        game.dragon 'Получи!'
        $ mistress_hp -= 1
    else:
        mistress 'Беги-беги! А ведь у тебя был шанс ранить меня, идиот!'   
            
    call lb_new_round from _call_lb_new_round_2
    return
    

label lb_shiva:
    show expression 'img/scene/fight/mistress/sheeva.jpg' as bg    
    'Аспект Шивы наделяет Владычицу неограниченной властью над холодом и льдом. От её поступи земля покрывается коркой инея, а чешуя холодеет.'
    call lb_tactics_choice from _call_lb_tactics_choice_2
    if 'ice_immunity' in game.dragon.modifiers():
        game.dragon 'Холод мне не страшен, Мать. Уж ты-то должна была об этом помнить!'
    else:
        'Единственного прикосновения Шивы достаточно, чтобы превратить голову дракона в хрупкую ледышку и затём расколоть её на множество осколков одним ударом.'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'Да поглотит тебя ледяное безмолвие, неверный сын!'
            jump lb_game_over
        else:
            mistress 'Вот видишь, это даже не больно. Холод милостив. Но следующей голове повезёт меньше!'

    if atk_tp == 'fire':
        game.dragon 'Пламенем Я командую! Сгори, растай, испарись!!!'
        $ mistress_hp -= 1
    else:
        mistress 'Лишь огонь мог бы тебе помочь, но тебе он неподвластен! Я знаю все твои слабости!'
            
    call lb_new_round from _call_lb_new_round_3
    return

label lb_agni:
    show expression 'img/scene/fight/mistress/agni.jpg' as bg    
    'Принимая аспект Агни, Владычица закутывается в наряд из багряного пламени и удушающего черного дыма. От неё исходит испепеляющий всё живое жар, выдержать который смог бы разве что Ифрит.'
    call lb_tactics_choice from _call_lb_tactics_choice_3
    if 'fire_immunity' in game.dragon.modifiers():
        game.dragon 'Ха! Безумная старуха, неужели ты решила сжечь повелителя пламени? Я стану лишь сильнее от твоего жара, иди же ко мне!'
    else:
        "От касания Агни, голова дракона вспыхивает и мигом превращается в почерневшую головёшку."
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'Почувствуй ярость огня моей души, жалкий предатель! УМРИ!!!'
            jump lb_game_over
        else:
            mistress 'Почувствуй ярость огня моей души! Ещё дергаешься, жалкий червяк?!'
        
    if atk_tp == 'ice':
        game.dragon 'Твой огонь умрёт, скованный хладом моего дыхания, Агни!'
        $ mistress_hp -= 1
    else:
        mistress 'Разве можно надеяться сокрушить само пламя, глупец?'
                            
    call lb_new_round from _call_lb_new_round_4
    return

label lb_indra:
    show expression 'img/scene/fight/mistress/indra.jpg' as bg    
    'В аспекте Индры Владычица получает власть над молнией и громом небесным. Она неуязвима, как сам чистый и свежий воздух, как небо, что питает её могущество. '
    call lb_tactics_choice from _call_lb_tactics_choice_4
    if 'lightning_immunity' in game.dragon.modifiers():
        game.dragon 'Титаны не могли поразить меня своими молниями. Не сможешь и ты, Индра. В штормовом облаке я как в родном доме!'
    else:
        'Удар молнии попадает точно в глову дракона, испепеляя её в одно мгновение!'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'Моё возмездие быстро, как небесный гром. Тебе стоило подумать об этом, предатель!'
            jump lb_game_over
        else:
            mistress 'Минус одна. А теперь прощайся и со следующей головой!'
        
    if atk_tp == 'poison':
        game.dragon 'Я отравлю воздух, дающий тебе силы! Никто не устоит перед токсическим смрадом, даже Небо, даже Аллах!'
        $ mistress_hp -= 1
    else:
        mistress 'Да, ты силён, но силы, что повергнет сами чистые Небеса, ты не сыщешь, предатель!'
                            
    call lb_new_round from _call_lb_new_round_5
    return
    

label lb_pangea:
    show expression 'img/scene/fight/mistress/pangea.jpg' as bg    
    'Тело владычицы превращается в один огромный живой кристалл, совершенное воплощение аспекта богини земли Пангеи. Её плоть тверда как алмаз.'
    call lb_tactics_choice from _call_lb_tactics_choice_5
    if game.dragon.defence_power()[0] + game.dragon.defence_power()[1] >= 5:
        game.dragon 'Моя чешуя не мягче твоей алмазной кожи, Пангея! Ты даже не поцарапаешь меня.'
    else:
        "Пангея сжимает глову дракона мёртвой хваткой и давит её, словно спелый арбуз."
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'Кто поднял руку на Мать, да будет сокрушён!'
            jump lb_game_over
        else:
            mistress 'Я сокрушу тебя! Каким бы живучим ты ни был, рано или поздно ты сдохнешь, поганец!'
        
    if atk_tp == 'thunder':
        game.dragon 'Попал!'
        $ mistress_hp -= 1
    else:
        mistress 'Промазал!'   
                            
    call lb_new_round from _call_lb_new_round_6
    return

label lb_nemesis:
    show expression 'img/scene/fight/mistress/nemesis.jpg' as bg    
    'Владычица принимает аспект богини Немезиды. Всё её тело покрывается острыми шипами, олицетворяя неминуемое возмездие. '
    call lb_tactics_choice from _call_lb_tactics_choice_6
    if atk_tp == 'dodge' or atk_tp == 'hide' or atk_tp == 'earth' or atk_tp == 'air':
        game.dragon 'Я знаю справедливость Немезиды. Если я не буду атаковать, ты тоже не сможешь!'
    else:
        'Нападение на Немезиду ведёт к неотвратимому воздаянию. Дракон теряет голову.'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'Такова судьба всех предателей - СМЕРТЬ!'
            jump lb_game_over
        else:
            mistress 'Моё возмездие ещё не завершено, но час твоей смерти уже близок, предатель!'
        
    if atk_tp != 'dodge' and atk_tp != 'hide' and atk_tp != 'earth' and atk_tp != 'air':
        game.dragon 'Но и тебе здоровой не уйти!'
        $ mistress_hp -= 1
    else:
        mistress 'Ты правильно делаешь, что прячешься, проживёшь лишнюю минуту, а то и две!'  
                            
    call lb_new_round from _call_lb_new_round_7
    return

label lb_amphisbena:
    show expression 'img/scene/fight/mistress/amfisbena.jpg' as bg    
    'Тело Владычицы покрывается яркой цветной чешуёй, когда она принимает аспект Амфисбены, ползучей ядовитой смерти, несущей погибель всем тварям земным.'
    call lb_tactics_choice from _call_lb_tactics_choice_7
    if atk_tp == 'air':
        game.dragon 'Рождённый ползать, летать не может. Попробуй-ка тут меня достать, тварь ползучая!'
    else:
        'От яда амфисбены голова дракона сморщивается и отсыхает.'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'Я надеялась, что ты будешь мучаться дольше, Иуда!'
            jump lb_game_over
        else:
            mistress 'Чувствуешь этот яд? Я рада, что ты ещё трепыхаешься, так моя месть будет слаще.'
        
    if game.dragon.attack_strength()[1] > 0:
        game.dragon 'Я раздавлю тебя, гадюка!'
        $ mistress_hp -= 1
    else:
        mistress 'И это всё, на что ты способен?! Слабак!'
                            
    call lb_new_round from _call_lb_new_round_8
    return
    

label lb_gekata:
    show expression 'img/scene/fight/mistress/gekata.jpg' as bg    
    'Аспект Гекаты даёт Владычице силу самой Ночи и Смерти. Сражаться с ней может лишь смельчак, не боящийся смертельных ран, но порой лучше быть трусом.'
    call lb_tactics_choice from _call_lb_tactics_choice_8
    if atk_tp == 'hide':
        game.dragon 'Я укроюсь от Тьмы во Тьме.'
    else:
        'Смертоносная Геката с лёгкостью отрывает дракону голову.'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'А твоё тело я скормлю шакалам, потому что ты падаль!'
            jump lb_game_over
        else:
            mistress 'Всё ещё дёргаешься, падаль?!'
        
    if game.dragon.attack_strength()[0] + game.dragon.attack_strength()[1] >= 5:
        game.dragon 'Вот тебе! Получай! Меня не так-то просто убить.'
        $ mistress_hp -= 1
    else:
        mistress 'А я-то надеялась, что моё чадо будет бить сильнее, чем крестьянская девчонка...' 
                            
    call lb_new_round from _call_lb_new_round_9
    return

label lb_hell:
    show expression 'img/scene/fight/mistress/hell.jpg' as bg    
    'Владычица выростает до небес, задевая макушкой облака, когда призывает на себя аспект великанши Хель - немёртвой владычицы нижнего мира. Её удары кажутся медленными, но они способны крушить даже гранитные скалы.'
    call lb_tactics_choice from _call_lb_tactics_choice_9
    if atk_tp == 'dodge':
        game.dragon 'Слишком медленно! Тебе меня не достать.'
    else:
        "Сокрушающим землю ударом огромной руки, великанша расплющивает голову дракона."
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'ХА! И мокрого места не осталось.'
            jump lb_game_over
        else:
            mistress 'Познай боль! Я сокрушу тебя как мерзкого таракана!'
        
    if atk_tp == 'magic':
        game.dragon 'Мои чары превыше твоей грубой силы, Хель!'
        $ mistress_hp -= 1
    else:
        mistress 'Хорошая попытка, малыш. Но для меня ты мелковат!'  
                            
    call lb_new_round from _call_lb_new_round_10
    return
    
label lb_mordor_mordor:
    # TODO: Дракон ведёт свою армию на вольные земли. На протяжении всех событий отступать нельзя - дракон умрёт или победит. Один раз можно попросить госпожу одолеть любого врага вместо дракона.
    # Чтобы пройти АТ нужно взять пограничную крепость. Дракон берёт на себя катапульты, армия штурмует стены.
    # Если и дракон и армия победили, засчитываем победу.
    # Если дракон победил, но армия слишком слаба даём второй энкаунтер для дракона - воздушный флот цвергов приходит
    # на помощь осаждённым, дракон должен их победить.
    python:
        battle.army_battle = True #Из боя теперь нельзя отступить
        army_decimator = 10    
    show expression 'img/scene/dark_march.jpg' as bg
    'Сражение у границ, Армия Тьмы вступает в битву. Катапульты являются ключевым звеном обороны.'
#    $ game.narrator(u"%s" %game.army.force)  
    $ game.foe = Enemy('catapult', game_ref=game)
    $ narrator(show_chances(game.foe))
            
    menu:
        'Наблюдать за битвой' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'Армия Тьмы несёт потери, но передовые отряды прорываются к катапультам и уничтожают их. Теперь победа всего в одном шаге.'
            $ game.army.power_percentage()
            
        'Сокрушить катапульты': #Дракон бережёт армию и сам уничтожает наиболее опасные очаги сопротивления
            $ battle.army_battle=True
            call lb_fight from _call_lb_fight_42

        'Молить Госпожу о помощи' if game.mistress_alive and not refuse: #Владычица вступает в бой и выигрывает его вместо дракона и армии
          call lb_mordor_mistress_help("lb_mordor_mordor") from _call_lb_mordor_mistress_help_9
          if not answer:
            return 
    if game.army.force >= 1000:
      'Вскоре [game.dragon.fullname] получает сообщение от одного из вспомогательных отрядов. Им удалось найти наземную базу воздушного флота цвергов. Всего одна искра - и гордость подземного народца превратилась в колоссальный костёр, чьи отблески были видны за многие десятки миль!\n\nДорога вглубь страны открыта.'
    else:
      call lb_war_border_continue from _call_lb_war_border_continue
    $ renpy.call_screen("main_battle_map") 
#    call lb_war_field from _call_lb_war_field
    return

label lb_war_border_continue:
    nvl clear
    show expression 'img/scene/dark_march.jpg' as bg
#    $ game.narrator(u"%s" %game.army.force)  
    'Сражение на земле практически выиграно, но дракон замечает новую опасность. Со стороны гор по воздуху приближается летучий флот цвергов. Если их не остановить, они сбросят в гущу армии монстров бочки, наполненные алхимическим огнём. Потери будут огромны.'
    $ game.foe = Enemy('airfleet', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Наблюдать за битвой' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'Тяжелые летучие крейсера демонстративно зависают над скоплением монстров и скидывают прямо на головы воинам Владычицы пузатые бочки с заженными фитилями. Земля озаряется вспышками и заливается текучим огнём. Объятые пламенем гоблины с визгоми разбегаются и катаются по земле, пытаясь погасить огонь. Когда запас бомб на кораблях подходит к концу, они мерно разворачиваются и уходят на базу невредимыми. Эта атака стоила Армии Тьмы десятой части воинов!'
            'Тем не менее, пограничные войска людей выдохнулись и вынуждены были отступить. Путь вглубь страны открыт.'
            $ game.army.power_percentage()
            
        'Перехватить летучие корабли': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            $ battle.army_battle=True
            call lb_fight from _call_lb_fight_43

        'Молить Госпожу о помощи' if game.mistress_alive and not refuse: #Владычица вступает в бой и выигрывает его вместо дракона и армии
          call lb_mordor_mistress_help("lb_war_border_continue") from _call_lb_mordor_mistress_help_8
          if not answer:
            return 
    

    return

    
label lb_mordor_road:
    # TODO: Армия продвигается вглубь страны и встречает объединённые войска Вольных Народов. Дракон должен победить титана, армия сражается с войском.
    # Если дракон и АТ победили, продвигаемся дальше. Если дракон победил а АТ проигрывает, даём дракону схватку против короля людей.

    nvl clear    
    show expression 'img/scene/great_force.jpg' as bg
#    $ game.narrator(u"%s" %game.army.force)  
    'Битва на границе была просто цветочками. Теперь Вольные Народы собрали объединённую армию, чтобы встретить тёмное воинство в чистом поле. Опаснее всех остальных врагов выглядит исполин в золотой броне - Титан решил сразиться на стороне вольных!'
    $ game.foe = Enemy('titan', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Наблюдать за битвой' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'Титан наносит тёмному воинству огромный урон, но всё же его удаётся одолеть. Вольные дрогнули, осталось лишь надавить!'
            $ game.army.power_percentage()
            
        'Атаковать': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            '[game.dragon.fullname] лично вступает в битву с Титаном, чтобы сберечь войска.'
            $ battle.army_battle=True
            call lb_fight from _call_lb_fight_44

        'Молить Госпожу о помощи' if game.mistress_alive and not refuse: #Владычица вступает в бой и выигрывает его вместо дракона и армии
          call lb_mordor_mistress_help("lb_mordor_road") from _call_lb_mordor_mistress_help_7
          if not answer:
            return 
    if game.army.force >= 1000:
      'После окончания битвы ухмыляющийся ящерик приносит дракону окровавленную человеческую голову. Оказывается, человеческий король предпринял отчаянную, самоубийственную атаку, желая уничтожить дракона и спасти армию от разгрома. Вот только атака оказалась воистину самоубийственной!\n\nТеперь Армии Тьмы открыт прямой путь на Столицу людей.'
    else:
      call lb_war_field_continue from _call_lb_war_field_continue
    $ renpy.call_screen("battle_map") 
#    call lb_war_siege from _call_lb_war_siege
    return

label lb_war_field_continue:
    # TODO: Армия продвигается вглубь страны и встречает объединённые войска Вольных Народов. Дракон должен победить титана, армия сражается с войском.
    # Если дракон и АТ победили, продвигаемся дальше. Если дракон победил а АТ проигрывает, даём дракону схватку против короля людей.
    
    nvl clear
    show expression 'img/scene/dark_march.jpg' as bg
#    $ game.narrator(u"%s" %game.army.force)  
    'Король людей воодушевляет бойцов и не даёт им отступать. Когда он будет повержен, битву можно считать выигранной.'
    $ game.foe = Enemy('king', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Наблюдать за битвой' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'Ценой огромный потерь, элитные отряды тёмных сил прорываются к королю и рассправляются с ним. Это становится переломным моментом битвы. На закате разрозненные и разбитые войска людей отступают, открывая чудовищам путь вглубь страны.'
            $ game.army.power_percentage()
            
        'Атаковать': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            'Битву можно выиграть всего одним точным ударом. [game.dragon.fullname] бросает вызов королю людей!'
            $ battle.army_battle=True
            call lb_fight from _call_lb_fight_45

        'Молить Госпожу о помощи' if game.mistress_alive and not refuse: #Владычица вступает в бой и выигрывает его вместо дракона и армии
          call lb_mordor_mistress_help("lb_war_field_continue") from _call_lb_mordor_mistress_help_6
          if not answer:
            return 

    return
    
label lb_mordor_city:
    # TODO: Армия Тьмы осаждает столицу людей. Дракон должен пробить огромные ворота чтобы армия могла ворваться в город.
    # Если дракон и АТ победили, продвигаемся дальше. Если дракон победил а АТ проигрывает, даём дракону схватку
    # против городской стражи.

    nvl clear
    show expression 'img/scene/city_fire.jpg' as bg
#    $ game.narrator(u"%s" %game.army.force)  
    'Разбив главные силы Вольных Народов, Силы Тьмы подступают к стенам столицы. В этом отлично укреплённом городе сопротивление может продолжаться годами. Пока столица не взята, говорить о подчинении Вольных Земель не приходится.'
    $ game.foe = Enemy('city', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Наблюдать за битвой' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'Войска штурмуюие главные ворота города несут страшные потери, но защитников слишком мало. Монстры сносят ворота и врываются на улицы города.'
            $ game.army.power_percentage()
            
        'Атаковать': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            'Если проломить главные ворота, обороняющиеся войска окажутся беззащитны перед монстрами Владычицы. [game.dragon.fullname] бросается на штурм. '
            $ battle.army_battle=True
            call lb_fight from _call_lb_fight_46

        'Молить Госпожу о помощи' if game.mistress_alive and not refuse: #Владычица вступает в бой и выигрывает его вместо дракона и армии
          call lb_mordor_mistress_help("lb_mordor_city") from _call_lb_mordor_mistress_help_5
          if not answer:
            return 
    if game.army.force >= 1000:
      hide bg
      show expression 'img/scene/city_raze.jpg' as bg
      'Воины армии тьмы хлынули на улицы города. Кажется, в Столице больше не осталось организованных отрядов, способных им противостоять. Война практически выиграна!'
    else:                
      call lb_war_siege_inside from _call_lb_war_siege_inside
    call lb_war_palace from _call_lb_war_palace
    return

    
label lb_war_siege_inside:
    # TODO: Армия Тьмы осаждает столицу людей. Дракон должен пробить огромные ворота чтобы армия могла ворваться в город.
    # Если дракон и АТ победили, продвигаемся дальше. Если дракон победил а АТ проигрывает, даём дракону схватку
    # против городской стражи.
    nvl clear
    show expression 'img/scene/city_raze.jpg' as bg
#    $ game.narrator(u"%s" %game.army.force)  
    'На улице города идут ожесточённые бои. Основу сопротивления составляюти элитные отряды городской стражи.'
    $ game.foe = Enemy('city_guard', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Наблюдать за битвой' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'Бой на улицах города отличается невероятной жестокостью, кровь течёт рекой и множетво раненых и убитых наблюдается с обеих сторон. Тем не менее, Силы Тьмы слишком многочисленны - защитники города обречены.'
            $ game.army.power_percentage()
            
        'Атаковать': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            '[game.dragon.fullname] лично возглавляет атаку своих войск, помогая уничтожить стражей.'
            $ battle.army_battle=True
            call lb_fight from _call_lb_fight_47

        'Молить Госпожу о помощи' if game.mistress_alive and not refuse: #Владычица вступает в бой и выигрывает его вместо дракона и армии
          call lb_mordor_mistress_help("lb_war_siege_inside") from _call_lb_mordor_mistress_help_4
          if not answer:
            return 
    'Кажется, в городе больше не осталось организованных отрядов, способных противостоять армии тьмы. Война практически выиграна!'              
#    call lb_war_citadel from _call_lb_war_citadel
    return

label lb_war_citadel:
    # TODO: Армия Тьмы захватила город, но центральная цитадель ещё держится. Дракон должен схватиться в воздухе с ангелом-хранителем, пока АТ штурмует.
    # Если дракон и АТ победили, продвигаемся дальше. Если дракон победил а АТ проигрывает, даём дракону схватку
    # против стального стража цвергов.
    # После окончательной победы переходим к сцене финальной оргии и концу игры.
    nvl clear
    show expression 'img/scene/city_raze.jpg' as bg
#    $ game.narrator(u"%s" %game.army.force)  
    'Хотя город взят и уже полыхает, в цитадели на холме всё ещё есть недобитые защитники. Учитывая, что именно там хранятся все драгоценнсти короны, взять это укрепление совершенно необходимо. К сожалению, над цитаделью парит ангел-защитник, посланный Небесами в ответ на мольбы невинных. Этот пернатый воин один стоит целой армии.'
    $ game.foe = Enemy('angel', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Наблюдать за битвой' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'Исчадия Тьмы выпускают в ангела сотни стрел, но они сгорают на подлёте. Небесный страж рубит отряды гоблинов своим мечом, словно скашивая пожухлую траву серпом. Наконец, его удаётся сбить метким выстрелом тяжёлой катапульты, но потери очень велики.'
            $ game.army.power_percentage()
            
        'Атаковать': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            'С этим противником [game.dragon.fullname] решает сразиться сам - обычным гоблинам он не по зубам.'
            $ battle.army_battle=True
            call lb_fight from _call_lb_fight_48

        'Молить Госпожу о помощи' if game.mistress_alive and not refuse: #Владычица вступает в бой и выигрывает его вместо дракона и армии
          call lb_mordor_mistress_help("lb_war_citadel") from _call_lb_mordor_mistress_help_3
          if not answer:
            return  
                
    call lb_war_final from _call_lb_war_final
    return
    
label lb_war_final:
    nvl clear
    show expression 'img/scene/city_raze.jpg' as bg
#    $ game.narrator(u"%s" %game.army.force)  
    'Воодушевлённые победой над ангелом, выродки дракона врываются внутрь цитадели, но тут же выкатываются обратно. Внутренние ворота охраняет огромный механический страж цвергов - несокрушимый железный голем.'
    $ game.foe = Enemy('golem', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Наблюдать за битвой' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'Железного голема удаётся буквально похоронить под грудой мяса и железа, в которые превращаются идущие волна за волной в самоубийственную атаку Исчадия Тьмы. Тем не менее это победа!'
            $ game.army.power_percentage()
            
        'Атаковать': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            'Как бы могуч не был железный страж, это всё, что стоит на пути к окочательной победе. [game.dragon.fullname] бросается в атаку.'
            $ battle.army_battle=True
            call lb_fight from _call_lb_fight_49

        'Молить Госпожу о помощи' if game.mistress_alive and not refuse: #Владычица вступает в бой и выигрывает его вместо дракона и армии
          call lb_mordor_mistress_help("lb_war_final") from _call_lb_mordor_mistress_help_2
          if not answer:
            return  
    jump lb_orgy

label lb_orgy:
    nvl clear
    show expression 'img/scene/city_raze.jpg' as bg
    if game.vini_vidi_vici:
      $ data.achieve_target("bliz", "battle")
      call lb_achievement_acquired from _call_lb_achievement_acquired_5      
    'Последний защитник пал, и Земли Вольных Народов отныне под властью Владычицы, Матери Драконов!'
    game.dragon 'Мы победили!'
    mistress 'Да. Благодаря тебе, твоему роду и детям твоего рода... Как давно я ждала этого. Даю тебе и армии три дня на разграбление города, а затем мы начнём строить ПЕРВУЮ | ВСЕМИРНУЮ | ИМПЕРИЮ!'
    game.dragon 'Вы слышали Владычицу, воины мои. Тащите всех девок ко мне и кидайте в кучу!'    
    show expression 'img/scene/girls.jpg' as bg
    pause (500.0)
    nvl clear
    'Отродья дракона прочесали горящий город, похватав всех красивых и молодых женщин, чтобы сорвать с них всю одежду и собрать в разгромленном тронном зале цитадели. Сотни обнаженных красавиц заполнили огромный зал до отказа, так что дракону пришлось буквально плыть в море обнаженных тел, чтобы добраться до середины.'
    game.dragon 'Сегодня вы можете насладиться победой вместе со мной, дети мои! Делайте с этими девками всё, что пожелаете.' 
    show expression 'img/scene/orgy.jpg' as bg
    pause (500.0)    
    nvl clear
    'Один из минотавров несёт отчаянно вырывающуюся, брыкающуюся и кусающуюся красавицу'
    python:
      minotaur= Talker(game_ref=game)
      minotaur.avatar = "img/avahuman/minotaur.jpg"
      minotaur.name = 'Минотавр' 
    minotaur 'Пап, это принцесса. Будешь?'
    menu:
      'Да не, развлекайся':
        pass
      'А давай!':
        $ description = game.girls_list.new_girl(girl_type='jasmine',girl_nature='proud',girl_hair='black',tres=False,name_number='01',family = u"де Джафар",avatar='img/archimonde/jasmine.jpg') 
        game.girl 'Силами, что пребывают, кровью своей и наследием, как последняя выжившая из рода - проклинаю тебя, [game.dragon.fullname]!'
        game.girl 'Чтоб было уничтожено всё, что тебе дорого, чтоб ни дна тебе, ни покрышки, чтоб ты надругался над собственной матерью и убил её...'
        '[game.dragon.name] бьёт принцессу Фиалку хвостом по губам'
        game.dragon 'Ну, последнее - это благое пожелание, а вовсе не проклятие...'
        menu:
          'Надругаться' if game.girls_list.is_mating_possible:
            call lb_sex_choice from _call_lb_sex_choice_7
#            python:
#              renpy.music.play(get_random_files('mus/battle'))
            if not game.girl.dead:
              call lb_orgy_jasmine from _call_lb_orgy_jasmine_1
        
          # @fdsc Гипноз
          'Загипнотизировать' if game.dragon.mana > game.girl.quality and not game.girl.willing:

              # @fdsc Девушки добровольно соглашаются
              $ game.girl.willing=True
              $ game.dragon.drain_mana(game.girl.quality + 1)
              pass

          'Магическое уменьшение' if not game.girls_list.is_mating_possible and game.girl.virgin and not game.girls_list.is_giant and game.dragon.lust > 0 and not game.girl.old:
            game.dragon 'Заклятье временного уменьшения!'
            $ game.dragon.gain_rage()
            call lb_sex_choice from _call_lb_sex_choice_8
#            python:
#              renpy.music.play(get_random_files('mus/battle'))
            if not game.girl.dead:
              call lb_orgy_jasmine from _call_lb_orgy_jasmine_2
          'Сожрать' if game.dragon.hunger > 0:
            game.dragon 'Интересно, а какова принцесса на вкус?'
            call lb_eat from _call_lb_eat_9
            game.dragon 'Ммм... коготки оближешь!'
          'Разорвать на части'  if game.dragon.hunger == 0:
            game.dragon 'Любопытно, из чего же сделаны наши принцессы?!'
            '[game.dragon.name] разрывает пленницу на части просто ради забавы'
            nvl clear
            hide bg
            show expression "img/scene/turn_apart.jpg" 
            game.dragon 'Ага, буду знать!'
            $ game.chronik.death('turned_apart',"img/scene/turn_apart.jpg")
    call lb_orgy_final from _call_lb_orgy_final_1
    return

label lb_orgy_jasmine:
    hide bg
    nvl clear
    show expression 'img/scene/palace.jpg' as bg
#    $ game.witch_force=100
    if game.historical_check('witch_dead'):
      mistress 'Сын, {i}немедленно{/i} отправь эту девку ко мне. Она ещё может пригодиться'
      game.dragon 'Как скажешь, мама'
    else:
      witch '[game.dragon.name], пришло время исполнить обещание, данное основателем твоего рода'
      witch 'Отдай мне принцессу Фиалку!'
      game.dragon 'Да на здоровье! Держи, мяса тут навалом.'
      mistress 'Нет'
      game.dragon 'Почему?'
      mistress 'Сын мой, ты сам не понимаешь, {i}что{/i} чуть не отдал в руки этой шлюхи'
      witch 'Ты осмелишься нарушить закон?'
      witch 'Именем договора, действие которого непреложно, я требую возвратить то, что принадлежит мне по праву!'
      show expression 'img/scene/fight/mistress/kali.jpg' as fg
      mistress '{i}{b}Я - это - Закон!!!{/b}{/i}'
      witch 'Я не хотела драться, но ты не оставила мне выбора.'
      witch 'Умри.'
      if game.witch_force<20:
        mistress 'Да неужели ты думаешь, что со своими жалкими силёнками сможешь одолеть {i}меня{/i}?'
        witch 'Посмотрим'
        $ choices = [
          ("lb_mistress_win", 60),
          ("lb_mistress_draw", game.witch_force)]
      elif game.witch_force>=20 and game.witch_force<60:
        mistress 'Что? Откуда у тебя столько сил?'
        witch 'Хорошо работала ротиком'
        mistress 'Мои дети отдали тебе так много спермы? {b}Предатели!!!{/b}'
        $ choices = [
          ("lb_mistress_win", 10),
          ("lb_mistress_draw", game.witch_force)]
      else: 
        mistress 'Что? Нет, нет, нет, не может быть!!!'
        witch 'Может, моя нахальная гостья, может. Твои дети дарили мне свою сперму на протяжении столетий!'
        $ choices = [
          ("lb_mistress_draw", 20),
          ("lb_mistress_defeate", game.witch_force)]
      $ enc = weighted_random(choices)
      $ renpy.call(enc)
    return

label lb_mistress_win:
    hide fg
    nvl clear
    show expression 'img/scene/fight/mistress/gekata.jpg' as fg
    'Тёмная Госпожа принимает аспект Гекаты и одним ударом сносит голову ведьмы'
    mistress 'Отлично. С этой шлюхой тоже покончено. Я заберу Фиалку, а ты можешь продолжать развлекаться.'
    return

label lb_mistress_defeate:
    hide fg
    nvl clear
    show expression 'img/scene/fight/mistress/nemesis.jpg' as fg
    'Тёмная Госпожа принимает аспект Немезис'
    witch 'Ты обращаешься за правосудием, нарушив закон?'
    'Удар ведьмы проходит {i}сквозь{/i} шипы и уничтожает Тёмную Госпожу'
    mistress 'Я ещё вернусь!'
    witch 'Да кто тебе даст-то.'
    hide fg
    show expression 'img/scene/palace.jpg' as bg
    witch 'До встречи, [game.dragon.fullname]. Если тебе что-то понадобится, я обращусь. Можешь продолжать развлекаться.'
    if not game.girl.cripple:
      'Принцесса Фиалка стонет от боли, явно пытаясь что-то сказать'
    else:
      'Принцесса Фиалка мотает головой, явно желая что-то сказать'
      'Ведьма одним движением руки возвращает ей слух и речь'
    witch 'Да, дитя?'
    game.girl 'Я вам... ещё... нужна?'
    witch 'У меня большие планы на твоего ребёнка'
    game.girl 'Вам нужно... моё... добровольное согласие?'
    witch 'Не помешало бы. Впрочем, ты не согласишься'
    game.girl 'Я соглашусь... на что угодно... если вы... убьёте... дракона'
    witch 'Дракон мне тоже не помешал бы...'
    witch 'Впрочем, я могу вырастить своих драконов, исправив ошибки изначальной версии. Благо, спермы мне хватит.'
    game.dragon 'Что за...'
    'Ведьма наносит магический удар небывалой силы, разрывая дракона на части.'
    $ data.achieve_target("jasmine", "battle")
    call lb_achievement_acquired from _call_lb_achievement_acquired_6
    jump lb_game_over
    return

label lb_mistress_draw:
    hide fg
    nvl clear
    show expression 'img/scene/duel.jpg' as fg
    'Ведьма и Тёмная Госпожа скользят над центральной площадью, обмениваясь магическими ударами и постоянно меняя обличья.'
    'Одержать победу в первые секунды боя не смог никто'
    mistress 'Сын! Помоги мне!'
    menu:
      'Броситься на помощь':
        game.dragon 'Сейчас, мамочка!'
        '[game.dragon.fullname] стремглав бросается вперёд и бьёт ведьму в спину. Тёмная Госпожа заканчивает дело в течение нескольких ударов сердца.'
        hide fg
        nvl clear
        show expression 'img/scene/palace.jpg' as bg
        mistress 'Спасибо, сын мой'
        game.dragon 'Мамочка, неужели я мог бы предать тебя?'
        mistress 'Я сама вложила в вас нечеловеческое коварство... Впрочем, всё обошлось. Я забираю Фиалку, а ты можешь продолжать развлекаться.'
      'Наблюдать за битвой':
        'Дракон кладёт голову на хвост и с интересом наблюдает за схваткой.'
        nvl clear
        mistress 'Сын! Почему ты медлишь?'
        mistress 'Воины! На помощь!'
        'Бесполезно - армия тьмы занята грабежами и насилием и явно не собирается отвлекаться от этого увлекательного занятия'
        'Бой продолжается с прежним ожесточением, но обе стороны, кажется, начали выдыхаться.'
        nvl clear
        game.dragon.third 'Помочь маме? Но ведь первую всемирную империю лучше всего строить в одиночку...'
        game.dragon.third 'Помочь ведьме? Нет, это точно не вариант, нечего менять одну Владычицу на другую!'
        game.dragon.third 'Подождать исхода схватки? Тогда они ослабнут, и я, возможно, смогу убить их обеих...'
        menu:
          'Помочь Тёмной Госпоже':
            '[game.dragon.fullname] тщательно выбирает подходящий момент и бьёт ведьму в спину. Тёмная Госпожа заканчивает дело в течение нескольких ударов сердца.'
            hide fg
            nvl clear
            show expression 'img/scene/palace.jpg' as bg
            mistress 'А ты не очень-то спешил, сын мой'
            game.dragon 'Я... эээ... выжидал подходящего момента, вот!'
            mistress 'Ещё одно такое предательство - и ты умрёшь. Я забираю Фиалку, а ты можешь продолжать развлекаться.'
          'Наблюдать за битвой':
            'После особенно мощного магического столкновения ведьма и Тёмная Госпожа без сил падают на землю.'
            hide fg
            nvl clear
            show expression 'img/scene/witch_death.jpg' as bg
            'Дракон вскрывает ведьме живот и добивает её ударом в голову.'
            game.dragon.third 'Так, одна есть. Осталось добить мамочку'
            game.dragon 'О-оу'
            hide bg
            nvl clear
            show expression 'img/scene/mistress_reborn.jpg' as bg
            'Кажется, Тёмная Госпожа пострадала не так сильно, как ведьма, и вот-вот придёт в себя!'
            menu:
              'Попробовать объясниться':
                game.dragon 'Мама, это не то, что ты думаешь...'
                mistress 'Нет, сыночек, именно то. Уж на то, чтобы покарать предателя, меня хватит. Умри!'
                jump lb_betrayal
              'Позвать на помощь Дану и Афродиту' if game.historical_check('danu_broken') and game.historical_check('afrodita_broken'):
                call lb_mistress_broke from _call_lb_mistress_broke
    return

label lb_mistress_broke:
    python:
     afrodita= Talker(game_ref=game)
     afrodita.avatar = "img/avahuman/afrodita.jpg"
     afrodita.name = 'Богиня Афродита'  
    game.dragon 'Дану! Афродита! Вы нужны мне! {i}Немедленно!{/i}'
    danu 'Ничтожные выполнят...'
    afrodita '...любой приказ...'
    danu '...нашего Господина...'
    afrodita '...и Повелителя!'   
    game.dragon 'Вы можете подавить силы Тёмной Госпожи, чтобы я смог подчинить её своей воле?'
    danu 'Да.'
    afrodita 'Ничтожные с радостью проведут необходимый ритуал!'
    nvl clear
    hide bg 
    show expression 'img/scene/mistress_sacriface.jpg' as bg
    'Богини сумели заблокировать силы Владычицы. Яростно сопротивляющуюся женщину отнесли во дворец и положили в центр ритуального круга'
    mistress 'Опомнитесь! Если вы проведёте этот ритуал, то погибнете!'
    danu 'Ничтожные знают.'   
    afrodita 'Ничтожные счастливы отдать свои жизни ради нашего Господина и Повелителя.'
    danu 'Как будешь счастлива и ты.'
    'От богинь к Тёмной Госпоже потянулись сияющие полосы магических энергий'
    mistress 'Если тебе так хочется власти, то почему бы просто не убить меня, предатель?!'
    game.dragon 'О, то есть смерти ты боишься меньше, чем подчинения. Интересненько.'
    nvl clear
    'Дану и Афродита рухнули на пол сломанными куклами.'
    'И тогда Тёмная Госпожа закричала.'
    nvl clear
    hide bg
    show expression sex_imgs("mistress") as bg
    '[game.dragon.fullname] насиловал свою мать неторопливо и вдумчиво, полностью погрузившись в этот бесконечно приятный процесс.'
    'С каждым часом угрозы и мольбы Владычицы звучали всё тише, всё реже.'
    'И наконец...'
    nvl clear
    hide bg
    show expression "img/intro/8.jpg" as bg
    mistress 'Ничтожная с радостью выполнит любой приказ Господина и Повелителя.'
    game.dragon 'Ха! У меня получилось! Получилось!'
    game.dragon 'Да я н{i}О{/i}гибатор!'
    $ data.achieve_target("MC", "win")
    jump lb_you_win
    return

label lb_orgy_final:
    hide bg
    show expression 'img/scene/orgy.jpg' as bg  
    nvl clear
    'Тем временем озлобленные после отчаянного боя солдаты тьмы набросились на женщин словно безумные. Глядя на творящуюся вокруг оргию, дракон и сам не терял времени. Сдавленный обнаженными телами, он не глядя вонзил в упругую женскую плоть одновременно и зубы и член, начав кровавый танец, сочетающий в себе голод и ярость, алчность и похоть. Этот танец продлится до тех пор, пока хотя бы одна женщина в зале сохранит способность визжать и дёргаться... '
    $ data.achieve_target("conquer", "win")
    jump lb_you_win

label lb_mordor_mountain:
    $ game.vini_vidi_vici = False
    hide bg
    nvl clear
    if game.historical_check('dwarf_ruined'):
      show expression 'img/scene/dwarf_ruin.jpg' as bg
      'Когда-то здесь высились неприступные врата в Подгорное царство. Но Подгорного царства больше нет, цверги рассеяны по пещерам. В данный момент они не представляют никакой опасности.'
    else:
      show expression 'img/bg/special/gates_dwarf.jpg' as bg
      'Нападение дракона не стало неожиданностью - цверги полностью готовы к отражению атаки. Мощные пушки откроют огонь по любому, кто посмеет подойти к неприступным воротам.'

      nvl clear
      menu:
        'Проломить ворота' if game.dragon.size > 3:
            'Жалкие укрепления коротышек не смогут устоять перед яростным отродьем Госпожи. [game.dragon.fullname] достаточно огромен и могуч, чтобы проломиться сквозь ворота и открыть путь неисчислимой Армии тьмы.'
            call lb_mordor_golem from _call_lb_mordor_golem_1
        'Бросить войска на штурм укреплений' if game.army.force >= 1000:
            'Пока гоблины и прочая мелочь волна за волной заваливают позиции канониров, могучие тролли подтаскивают к воротам магический таран. После тринадцати сокрушительных ударов "неприступные" укрепления покрываются сеточкой трещин и рушатся. Хотя вся площадка перед воротами завалена трупами, путь вглубь Подгорного царства открыт!'
            $ game.army.power_percentage()
            call lb_mordor_golem from _call_lb_mordor_golem_2
        'Убраться не солоно хлебавши':
            '[game.dragon.fullname] в гневе хлещет себя хвостом по бокам. Кажется, укрепления цвергов и вправду неприступны!'
    $ renpy.call_screen("battle_map") 
    return

label lb_mordor_golem:
    show expression 'img/bg/special/moria.jpg' as bg
    'Даже после того, как врата обрушились, пыль и мелкие камушки продолжают сыпаться с потолка. По центральной галерее гулко раздаются шаги стража ворот - выкованного целиком из закалённого адамантия механического гиганта. На свете немного противников, равных ему по силе...'
    $ game.foe = Enemy('golem', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Наблюдать за битвой' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'Железного голема удаётся буквально похоронить под грудой мяса и железа, в которые превращаются идущие волна за волной в самоубийственную атаку Исчадия Тьмы. Тем не менее это победа!'
            $ game.army.power_percentage()
        'Сразиться с механическим стражем':
            $ battle.army_battle=True
            call lb_fight from _call_lb_fight_99
        'Молить Госпожу о помощи' if game.mistress_alive and not refuse: #Владычица вступает в бой и выигрывает его вместо дракона и армии
          call lb_mordor_mistress_help("lb_mordor_golem") from _call_lb_mordor_mistress_help_1
          if not answer:
            return
    'Голем пал, и Подгорные чертоги отныне обречены. Отродья из Армии тьмы радостно разбегаются по коридорам, убивая цвергов, присваивая их сокровища и насилуя их женщин. Призвать разномастную орду к порядку невозможно... да, собственно, и не нужно.'
    $ game.army.power_percentage()
    $ game.history = historical( name='dwarf_ruined',end_year=game.year+15,desc='Неутомимые цверги вновь возвели Подгорные чертоги. Карликовая крепость готова к веселью! ',image='img/bg/special/dwarf_fortress.jpg')
    $ game.history_mod.append(game.history)
    return

label lb_mordor_spell:
    hide bg
    nvl clear
    show expression "img/archimonde/dragon.jpg" as bg  
    if game.choose_spell(u"Вернуться к битве"):
      python:
        game.dragon.drain_mana()
    $ renpy.call_screen("battle_map")
    return

label lb_mordor_sea:
    $ game.vini_vidi_vici = False
    $ place = 'sea'
    hide bg
    show expression get_place_bg(place) as bg
    nvl clear
    if not game.dragon.can_swim: 
        '[game.dragon.name] пробует когтем солёную морскую влагу. Если бы только он умел дышать под водой...'
        $ renpy.call_screen("battle_map")
    if game.historical_check('dagon_busy'):
      '{i}That is not dead which can eternal lie, and with strange aeons, even death may die.{/i} Дагону сейчас явно не до защиты Вольных'
    else:
      'Согласно последней информации, предводитель контрабандистов Гвидон придумал средство, способное сдержать Дагона. К сожалению, пока подступы к острову контрабандистов патрулирует флагманский галеон "Принцесса Фиалка", ни о какой поддержке со стороны Гвидона не может быть и речи.'
      $ game.foe = Enemy('battleship', game_ref=game)
      $ narrator(show_chances(game.foe))
      menu:
        'Потопить "Принцессу Фиалку"':
          $ battle.army_battle=True
          call lb_fight from _call_lb_fight_92
          hide bg
          nvl clear
          show expression 'img/bg/special/island.jpg' as bg
          python:
            gwidon = Talker(game_ref=game)
            gwidon.avatar = "img/avahuman/orc.jpg"
            gwidon.name = "Гвидон"
          if not freeplay:
            gwidon 'Ну привет, племянничек - ведь ты потомок моего отца. Или, учитывая, что ты сын моей бабушки, я должен называть тебя дядюшкой?'
            game.dragon 'Эээ... пусть этот вопрос решает мама - в хитросплетениях генов сам ангел крыло сломит!'
          else:
            gwidon 'Ну привет, папаша.'
            if not game.historical_check('witch_task_refuse'):
              game.dragon 'Привет, привет. Неплохо устроился.'
              gwidon 'А то ты не знаешь!'
            else:
              game.dragon 'Кто ты? Я тебя точно не рожал!'
              gwidon 'Ангел побери, ну просил же Хроми больше так не чудить - так нет же, опять за старое!'
          gwidon 'В любом случае, хорошо, что ты пришёл. Мои молодцы связались с Алхимиком, и он разработал специальный порошок, способный отпугнуть Дагона. Убить не убьёт - но на защиту Вольных этот божок встать не сможет.'
          game.dragon 'Отличные новости, действуй!'
          'Вскоре с острова во все стороны устремились люггеры контрабандистов, разбрасывая по морским волнам такой простой и такой коварный порошок.'
          $ game.history = historical( name='dagon_busy',end_year=game.year+1,desc=None,image=None)
          $ game.history_mod.append(game.history)
        'Спастись бегством':
          '[game.dragon.fullname] предпринимает срочный манёвр стратегического отступления.'
          game.dragon 'Ангел побери! Надеюсь, в следующей версии игры у меня будет нормальная подводная армия.'
    $ renpy.call_screen("battle_map")
    return

label lb_mordor_plains:
    $ game.vini_vidi_vici = False

    nvl clear
    if game.poverty.value > 15:
      $ game.history = historical( name='angel_busy',end_year=None,desc=None,image=None)
      $ game.history_mod.append(game.history)      
    if game.historical_check('angel_busy'):
      $ place = 'poverty'
      hide bg
      show expression get_place_bg(place) as bg
      'Земли Вольных разорены. Те, кому не повезло уцелеть, отчаянно молят Небеса о помощи. Ангелы отвечают на молитвы, вот только их мало, а дел - много. При такой занятости посланники Небес явно не успеют спасти Столицу!'
    else:
      $ place = 'plain'
      hide bg
      show expression get_place_bg(place) as bg
      'Обстановка во внутренних областях Королевства далека от критической. Чтобы разорить земли жалких людишек, необходима планомерная, рассчитанная на годы работа дракона... или приличная часть Армии тьмы. Только тогда люди взмолятся по настоящему. Только тогда ангелом придётся отвлечься от охраны Столицы.'
      menu:
        'Отправить отродий разорять земли' if game.army.force >= 1000:
          'Орда кровожадных тварей затопила людские земли. Чудовища сжигают города и сёла, травят посевы, убивают мужчин и насилуют женщин.'
          game.dragon 'Теперь ангелы обязательно вмешаются в эту заваруху!'
          $ game.army.power_percentage()
          $ game.history = historical( name='angel_busy',end_year=game.year+1,desc=None,image=None)
          $ game.history_mod.append(game.history) 
        'Оставить всё как есть':
          game.dragon 'Ладно, не так страшен ангел, как его малюют!'
    $ renpy.call_screen("battle_map")
    return

label lb_mordor_forest:
    $ game.vini_vidi_vici = False
    nvl clear
    hide bg
    if not game.historical_check('elf_ruined'):
      $ place = 'forest'
      show expression get_place_bg(place) as bg
      'Попасть в Зачарованный лес непросто. Лишь запретное колдовство способно прорвать завесу морока и сна... хотя, наводнив леса тёмными тварями, тоже можно добиться успеха. Но потери будут чудовищными.'
      menu:
        'Открыть путь колдовством' if game.dragon.mana > 0:
          $ game.dragon.drain_mana()
          nvl clear
          hide bg
          show expression 'img/bg/special/enchanted_forest.jpg' as bg
          'Чарам альвов не устоять против буйства дикой магии!'
          call lb_mordor_treant from _call_lb_mordor_treant_1
        'Отправить отродий на поиски' if game.army.force >= 1000:
          nvl clear
          hide bg
          show expression 'img/bg/special/enchanted_forest.jpg' as bg
          'Глубины леса таят в себе немало опасностей. Многие отродья отдали свои жизни, пытаясь найти незащищённый проход в Зачарованный лес среди хаоса Темнолесья. Но в конце концов и им улыбнулась удача.'
          $ game.army.power_percentage()
          call lb_mordor_treant from _call_lb_mordor_treant_2
        'Отступить в полном беспорядке':
          game.dragon 'Да ну их, этих альвов! Ну не вырастят же они своего чащобного стража прямо в центре Столицы?'
    elif game.historical_check('elf_ruined') and not game.historical_check('danu_busy'):
     show expression 'img/bg/lair/dead_grove.jpg' as bg
     'В лесу, который некогда носил название "Зачарованного" - тихо, пустынно, страшно. В нём не осталось ничего живого, ничего ценного, ничего интересного.\n\nТочно ничего?'
     menu:
       'Точно-точно, даже время терять незачем!':
         'Дракон ушёл прочь, снедаемый ощущением, что он упустил нечто важное...'
       'Прибегнуть к поисковым заклинаниям' if game.dragon.mana > 0:
          $ game.dragon.drain_mana()
          'С помощью запретного колдовства [game.dragon.fullname] разрывает завесу тонких, практически незаметных чар, и...'
          nvl clear
          hide bg
          show expression 'img/scene/danu.jpg' as bg
          $ game.history = historical( name='danu_busy',end_year=game.year+1,desc=None,image=None)
          $ game.history_mod.append(game.history) 
          $ game.history = historical( name='danu_angry',end_year=game.year+1,desc=None,image=None)
          $ game.history_mod.append(game.history) 
          '...и замечает сидящую под деревом альву.'
          'А, нет, не альву! Это же аватара самой богини Дану!'
          game.dragon 'Повеселимся, красавица?'
          'Дану равнодушно пожимает плечами'
          python: #делаем аватарку старухи  для диалогового окна
            danu= Talker(game_ref=game)
            danu.avatar = "img/avahuman/danu.jpg"
            danu.name = 'Богиня Дану'  
          danu 'Бессмысленно. Я просто-напросто сброшу эту тело, как пустую оболочку.'
          danu 'Впрочем, это доставит некоторые неудобства. Уходи прочь - и я не стану помогать Вольным, когда ты будешь штурмовать Столицу.'
          game.dragon 'С чего это ты решила заделаться предательницей?'
          danu 'Это не предательство. Даже если сейчас вы с Тёмной Госпожой сокрушите Вольных - победа будет недолговечной. На нашей стороне Пророчества.'
          game.dragon 'А на нашей - сила! А что касается пророчеств... ты их только что выдумала, да?'
          danu 'Верь во что хочешь.'
          menu:
            'Оставить богиню в покое':
              nvl clear
              game.dragon.third 'С Дану лучше не связываться... Захват Столицы важнее, чем мимолётное развлечение с богиней! '
              python:
                for i in reversed(xrange(len(game.history_mod))):
                  if game.history_mod[i].historical_name == 'danu_angry':
                     del game.history_mod[i]
            'Поразвлечься с богиней':
              'Дану сопротивляется, но [game.dragon.fullname] хватает её без особого труда.'
              $ description = game.girls_list.new_girl(girl_type='danu',girl_nature='innocent',tres=False,name_number='01',avatar='img/avahuman/danu.jpg') 
              $ game.girl.hair_color = 'blond'
              danu 'Ты об этом пожалеешь.'
              game.dragon 'Нет, это ты об этом пожалеешь!'
              menu:
                'Надругаться' if game.girls_list.is_mating_possible:
                  call lb_sex_choice from _call_lb_sex_choice_5
#                  python:
#                    renpy.music.play(get_random_files('mus/battle'))
                  if not game.girl.dead:
                    call lb_mordor_danu from _call_lb_mordor_danu_1
            
        
                # @fdsc Гипноз
                #'Загипнотизировать' if game.dragon.mana > game.girl.quality and not game.girl.willing:

                  # @fdsc Девушки добровольно соглашаются
                  #$ game.girl.willing=True
                  #$ game.dragon.drain_mana(game.girl.quality + 1)
                  #pass

                'Магическое уменьшение' if not game.girls_list.is_mating_possible and game.girl.virgin and not game.girls_list.is_giant and game.dragon.lust > 0 and not game.girl.old:
                  game.dragon 'Заклятье временного уменьшения!'
                  $ game.dragon.gain_rage()
                  call lb_sex_choice from _call_lb_sex_choice_6
#                  python:
#                    renpy.music.play(get_random_files('mus/battle'))
                  if not game.girl.dead:
                    call lb_mordor_danu from _call_lb_mordor_danu_2
                'Сожрать' if game.dragon.hunger > 0:
                  game.dragon 'Интересно, а каков богиня Дану на вкус?'
                  call lb_eat from _call_lb_eat_8
                  'К сожалению, вопрос остаётся без ответа - тело Дану во рту распадается пылью.'
                'Разорвать на части'  if game.dragon.hunger == 0:
                  game.dragon 'Любопытно, из чего же сделаны наши богини?!'
                  'К сожалению, получить ответ на вопрос не получилось - едва дракон начал раздирать тело богини, Афродита распалась белой сверкающей пылью.'
                  $ game.chronik.death('turned_apart',"img/scene/turn_apart.jpg")
    elif game.historical_check('elf_ruined') and game.historical_check('danu_busy'):
      show expression 'img/scene/dark_forest.jpg' as bg
      'Вот теперь тут точно не осталось ничего интересного'
    $ renpy.call_screen("battle_map")
    return

label lb_mordor_danu:
    hide bg
    nvl clear
    show expression 'img/scene/danu.jpg' as bg
    if not game.historical_check('danu_broken'):
      game.girl 'Так вот через что проходили дочери моего народа...'
      game.girl 'Мы ещё встретимся, и совсем скоро!'
      'Аватара богини Дану рассыпается сверкающей пылью.'
    else:
      python:
        for i in reversed(xrange(len(game.history_mod))):
          if game.history_mod[i].historical_name == 'danu_angry':
            del game.history_mod[i]
      'Кажется, изнасилование повлияло не только не аватару, но и на саму богиню - Дану смотрит на дракона с воистину безграничной преданностью.'
      game.dragon 'Кто я?'
      game.girl 'Вы - Господин и Повелитель, верховное божество для ничтожной.'
      game.dragon 'Что ты готова сделать ради меня?'
      game.girl 'По Вашей малейшей прихоти ничтожная отдаст как свою жизнь, так и жизни своего народа.'
      game.dragon 'Отлично. Я позову тебя, когда будет необходимо.'
      game.girl 'Ваше слово - закон для ничтожной.'
    return

label lb_mordor_treant:
    nvl clear
    'Великое Древо найдено, но путь к нему преграждает чащобный страж - весьма и весьма опасный противник. Увы, отступить он уже не даст...'
    $ game.foe = Enemy('treant', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Наблюдать за битвой' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'Срубить гигантское дерево, активно отмахивающееся корнями и ветками, непросто. Но, понеся огромные потери, Армия тьмы справилась и с этой нетривиальной задачей.'
            $ game.army.power_percentage()
        'Сразиться с чащобным стражем':
            $ battle.army_battle=True
            call lb_fight from _call_lb_fight_93
        'Молить Госпожу о помощи' if game.mistress_alive and not refuse: #Владычица вступает в бой и выигрывает его вместо дракона и армии
          call lb_mordor_mistress_help("lb_mordor_treant") from _call_lb_mordor_mistress_help_10
          if not answer:
            return
    if game.dragon.lust>0:
      $ game.dragon.lust-=1
    'Чащобный страж повержен, и Армия тьмы ворвалась в заповедные леса. Это была очень долгая ночь, наполненная убиствами, грабежами и насилием. Лишь на следующий день дракон, отдохнувший и телом и душой, вновь повёл свои войска на Столицу.'
    $ game.history = historical( name='elf_ruined',end_year=game.year+30,desc='Семечко, посаженное альвами, дало росток нового священного Древа. Богиня Дану благословила его ветви, и теперь народ альвов пребывает в мире и гармонии под тенью его кроны.  ',image='img/bg/special/elf_restored.jpg')
    $ game.history_mod.append(game.history)
    return

label lb_mordor_sky:
    $ game.vini_vidi_vici = False
    $ place = 'sky'
    hide bg
    show expression get_place_bg(place) as bg
    nvl clear
    if not game.dragon.can_fly: 
      '[game.dragon.name] с тоской смотрит в небо. Если бы только он умел летать...'
    elif game.historical_check('athena_busy'):
      '[game.dragon.name] долго парит в небесах, но больше не может найти ничего интересного.'
    else: 
      '[game.dragon.fullname] расправляет свою могучие крылья и взмывает ввысь. Некоторое время он видит только бескрайнюю облачную пелену, но потом...'
      hide bg
      show expression 'img/scene/olimp.jpg' as bg
      nvl clear
      '...его взору открывается величественный летающий остров.'
      nvl clear
      'Олимп'
      menu:
        'Немедленно убраться прочь!':
          game.dragon 'Я ещё не сошёл с ума, чтобы бросать вызов богам!'
        'Бросить вызов богам':
          $ game.history = historical( name='athena_busy',end_year=game.year+1,desc=None,image=None)
          $ game.history_mod.append(game.history)
          game.dragon 'Олимп? Всегда мечтал о здешних богинях...'
          hide bg
          nvl clear
          show expression 'img/scene/athena_rest.jpg' as bg    
          python: #делаем аватарку старухи  для диалогового окна
            athena= Talker(game_ref=game)
            athena.avatar = "img/avahuman/athena.jpg"
            athena.name = 'Афина'    

          'Как ни странно, дракону, похоже, удалось застать олимпийцев врасплох!'
          athena 'А? Что? Кто здесь?'
          'Похоже, они не ожидали, что [game.dragon.name] победит в решающей битве - и уж тем более что он посмеет заявиться на Олимп!'
          hide bg
          show expression 'img/scene/athena_ready.jpg' as bg 
          nvl clear
          'Впрочем, замешательство не продлилось долго - Афина быстро выдвинулась навстречу дракону'
          athena 'Как ты смеешь осквернять эти священные залы?'
          athena 'Такая дерзость заслуживает наказания.'
          $ game.foe = Enemy('athena', game_ref=game)
          $ narrator(show_chances(game.foe))
          athena 'Умри.'
          $ battle.army_battle=True
          call lb_fight from _call_lb_fight_94
          hide bg
          show expression 'img/scene/olimp.jpg' as bg
          game.dragon 'Эх, жаль, что у меня не получилось надругаться над этой вечной девственницей...'
          'Повергнув аватару Афины, дракон начал обыскивать залы и коридоры Олимпа. Они на удивление пустынны - то ли все олимпийцы отправились на защиту Столицы, то ли, что вероятнее, где-то трусливо спрятались, надеясь пережить вторжение.'
          'Похоже, поиски бесполезны... так, что это?'
          hide bg
          nvl clear
          show expression 'img/scene/afrodita.jpg' as bg
          'На одном из балконов прекрасная обнажённая женщина спокойно ожидает дракона.'
          'Афродита, богиня любви'
          $ description = game.girls_list.new_girl(girl_type='afrodita',girl_nature='lust',tres=False,name_number='01',avatar='img/avahuman/afrodita.jpg') 
          $ game.girl.hair_color = 'brown'
          game.girl 'Я так надеялась, что ты придёшь...'
          nvl clear
          'В голосе богини любви невероятным образом смешиваются надежда, страх и вожделение.'
          game.girl 'Ты... ты ведь воспользуешься правом победителя?..'
          $ game.girl.willing=True
          game.dragon 'Ну разумеется, моя похотливенькая Афродита, ну разумеется!'
          menu:
            'Надругаться' if game.girls_list.is_mating_possible:
            # Alex: Added sex images:
              call lb_sex_choice from _call_lb_sex_choice_3
#              python:
#                renpy.music.play(get_random_files('mus/battle'))
              if not game.girl.dead:
                call lb_mordor_afrodita from _call_lb_mordor_afrodita_1
            
            # @fdsc Гипноз
            'Загипнотизировать' if game.dragon.mana > game.girl.quality and not game.girl.willing:

              # @fdsc Девушки добровольно соглашаются
              $ game.girl.willing=True
              $ game.dragon.drain_mana(game.girl.quality + 1)

              # @fdsc Гипноз Афродиты
              $ game.history = historical( name='afrodita_broken',end_year=game.year+1,desc=None,image=None)
              $ game.history_mod.append(game.history)
              pass

            'Магический рост' if not game.girls_list.is_mating_possible and game.girl.virgin and game.girls_list.is_giant and game.dragon.mana > 0 and game.dragon.lust > 0:
              $ game.dragon.drain_mana()
              game.dragon 'Заклятье временного роста!'
              call lb_sex_choice from _call_lb_sex_choice_4
#              python:
#                renpy.music.play(get_random_files('mus/battle'))
              if not game.girl.dead:
                call lb_mordor_afrodita from _call_lb_mordor_afrodita_2
            'Сожрать' if game.dragon.hunger > 0:
              game.dragon 'Что-то Афродита прямо-таки прыгает в мои объятия. Подозрительно. Интересно, а каковы олимпийцы на вкус?'
              call lb_eat from _call_lb_eat_7
              'К сожалению, вопрос остаётся без ответа - тело Афродиты во рту распадается пылью.'
            'Разорвать на части'  if game.dragon.hunger == 0:
              game.dragon 'Любопытно, из чего же сделаны наши богини?!'
              game.girl 'Эй! Нет! Что ты делаешь? Ты же должен был поступить со мной по-другому, я же всё продумала!'
              'К сожалению, получить ответ на вопрос не получилось - едва дракон начал раздирать тело богини, Афродита распалась белой сверкающей пылью.'
              $ game.chronik.death('turned_apart',"img/scene/turn_apart.jpg")
    $ renpy.call_screen("battle_map")

    return

label lb_mordor_afrodita:
    hide bg
    show expression 'img/scene/afrodita.jpg' as bg
    if game.historical_check('afrodita_broken'):
      'Кажется, изнасилование повлияло не только не аватару, но и на саму богиню - Афродита смотрит на дракона с воистину безграничной преданностью.'
      game.dragon 'Кто я?'
      game.girl 'Вы - Господин и Повелитель, верховное божество для ничтожной.'
      game.dragon 'Что ты готова сделать ради меня?'
      game.girl 'Ничтожная отдаст жизнь по Вашей малейшей прихоти.'
      game.dragon 'Каким был твой план?'
      game.girl 'Ничтожная хотела поработить Вас и натравить на Тёмную Госпожу.'
      game.dragon 'Отлично. Я позову тебя, когда будет необходимо.'
      game.girl 'Ваше слово - закон для ничтожной.'
    elif game.historical_check('afrodita_win'):
      nvl clear
      'Внезапно дракон почувствовал, как его охватывает самый наастоящий ужас. Как посмел он притронуться к Величайшей? Как он мог посягнуть на святое?!!'
      game.dragon 'Богиня... Моя вина непростительна. Может ли смерть хоть немного загладить её?'
      'Богиня любви загадочно улыбнулась.'
      game.girl 'Иди и убей свою мать, а там посмотрим.'
      'Дракон почувствовал, как в его душе загорается крохотная искорка надежды. Убийство матери - ничтожная цена по сравнению с прощением Величайшей!'
      hide bg
      show expression 'img/scene/mistress.jpg' as bg  
      mistress 'Что ты здесь делаешь, [game.dragon.name]? Разве не должен ты командовать уничтожением Вольных?'  
      mistress 'Погоди... тебя околдовала Афродита?'
      mistress 'Как вообще в твою дурную башку могла прийти идея надругаться над {i}богиней {b}любви{/b}{/i}?!!'
      game.dragon 'Умри.'
      $ game.mistress_alive=False
      jump lb_betrayal
    else:
      game.dragon 'Кажется, тут какая-то ошибка. Обратитесь к разработчику.'
    return

label lb_mordor_ruin:
    $ game.vini_vidi_vici = False
    hide bg
    nvl clear
    if game.historical_check('witch_dead'):
      show expression 'img/bg/special/haunted.jpg' as bg
      game.dragon 'Ведьма мертва. Тут больше нет ничего интересного.'
    else:
      show expression 'img/scene/witch.jpg' as bg
      witch 'Зачем ты пришёл сюда?'
      menu:
        'Да так, ошибся дорогой':
          witch 'Удачи в битве. И помни про уговор!'
        'Пришла пора оплатить за все унижения, ведьма!':
          witch 'Неблагодарная скотина!'
          'Воины Армии тьмы бросились на ведьму со всех сторон. Волна тварей захлестнула её с головой...'
          $ game.army.power_percentage()
          '...и превратилась в гниющее месиво.'
          'А потом ведьма встала на ноги.'
          hide bg
          nvl clear
          show expression 'img/scene/witch_old.jpg' as bg
          'Казалось, за несколько секунд она постарела на тысячи лет. Или это спала заботливо наложенная иллюзия?'
          $ game.foe = Enemy('witch', game_ref=game)
          $ narrator(show_chances(game.foe))
          witch 'Умри.'
          $ battle.army_battle=True
          call lb_fight(skip_fear=True) from _call_lb_fight_95
          hide bg
          nvl clear
          show expression 'img/bg/special/haunted.jpg' as bg
          'После смерти тело ведьмы вспыхнуло бездымным пламенем и сгорело дотла.'
          game.dragon 'Огромные потери и никакого удовольствия.'
          game.dragon 'Ну когда я наконец усвою, что наиболее злые поступки не всегда являются самыми правильными?'
          $ game.history = historical( name='witch_dead',end_year=game.year+1,desc=None,image=None)
          $ game.history_mod.append(game.history)
    $ renpy.call_screen("battle_map")
    return

label lb_mordor_mistress_help(task):
    game.dragon '[reinforcement_ask]'
    python:
      if reinforcement_used:
        reinforcement_answer = reinforcement_refuse
      else:
        reinforcement_answer = reinforcement_agree
    mistress '[reinforcement_answer]'
    if reinforcement_used:
      $ refuse = True
      $ renpy.call(task)
      $ answer=False
      return answer
    else:
      if not game.historical_check('kali'):
        $ renpy.movie_cutscene("mov/kali.webm")               
      $ reinforcement_used = True 
      $ answer=True  
    return answer

label lb_war_palace:
    hide bg
    nvl clear
    show expression 'img/scene/palace.jpg' as bg
    'Дракон и армия тьмы триумфально вступают на площадь перед дворцом.'
    $ enemy_list = []
    if not game.historical_check('dagon_busy'):
      show expression 'img/scene/fight/dagon.jpg' as fg
      'Из морских глубин на поверхность поднимается сам Дагон'
      hide fg
      $ enemy_list.append('dagon')
    if not game.historical_check('athena_busy'):
      show expression 'img/scene/athena_ready.jpg' as fg
      'Из неясного воздушного марева выходит Афина Паллада'
      hide fg
      $ enemy_list.append('athena')
    if not game.historical_check('angel_busy') and game.poverty.value < 16:
      show expression 'img/scene/fight/angel.jpg' as fg
      'В столпе ослепительного света на землю снисходит ангел'
      hide fg
      $ enemy_list.append('angel')
    if not game.historical_check('dwarf_ruined'):
      show expression 'img/scene/fight/golem.jpg' as fg
      'Ворота дворца распахиваются, и из них неспешно выдвигается голем'
      hide fg  
      $ enemy_list.append('golem')
    if not game.historical_check('elf_ruined') or game.historical_check('danu_angry'):
      show expression 'img/scene/fight/treant.jpg' as fg
      'Из семечка, посаженного богиней Дану, за несколько секунд вырастает древесный страж'
      hide fg   
      $ enemy_list.append('treant') 
#    show expression 'img/scene/palace.jpg' as bg
    if len(enemy_list) == 0:
      'И, не встречая сопротивления, входят внутрь. Война выиграна!!!'
      $ data.achieve_target("vini_vidi_vici", "battle")
      call lb_achievement_acquired from _call_lb_achievement_acquired_4
      call lb_orgy from _call_lb_orgy_1
    else:
      if len(enemy_list) == 1:
        game.dragon 'Ещё один враг!'
      elif len(enemy_list) == 2:
        game.dragon 'Это беда...'
      elif len(enemy_list) == 3:    
        game.dragon 'Ой. Без помощи мамы нам точно не справиться!'  
      else:
        '[game.dragon.fullname] чувствует, как его внутренности скрючиваются от страха.'
        game.dragon 'Мы обречены!'
      call lb_war_last_battle from _call_lb_war_last_battle_1
    return

label lb_war_last_battle:
    nvl clear
    menu: 
      'Отправить армию в бой' if game.army.force >= 1000 and len(enemy_list) == 1:
        $ text = data.last_enemies[enemy_list[0]]['win']
        show expression data.last_enemies[enemy_list[0]]['image'] as fg
        $ game.army.power_percentage()
        '[text]'
        hide fg
      'Молить госпожу о помощи' if len(enemy_list) == 1 and not refuse and not mistress_in_battle:
        call lb_mordor_mistress_help("lb_war_last_battle") from _call_lb_mordor_mistress_help_11
        if not answer:
          return  
      'Молить госпожу о помощи' if len(enemy_list) > 1 and not refuse and not mistress_in_battle:
        $ game.history = historical( name='kali',end_year=game.year+1,desc=None,image=None)
        $ game.history_mod.append(game.history)
        call lb_mordor_mistress_help("lb_war_last_battle") from _call_lb_mordor_mistress_help_12
        if not answer:
          return 
        $ enemy_name=data.last_enemies[enemy_list[0] ]['name_r']
        if len(enemy_list) == 2:
          mistress 'Враг сильнее, чем я ожидала. Я возьму на себя [enemy_name], а ты подумай, как справиться с остальными.'
        else:
          mistress 'Что? Куда ты привёл меня, предатель?!'
          mistress 'Неужели ты не понял, что я не справлюсь со всеми чемпионами Вольных? Лучше бы ты погиб и угробил всю свою армию, чем подставил бы меня под их удар!'
          mistress 'Я возьму на себя [enemy_name], а ты сражайся, сражайся как никогда раньше, ведь если ты проиграешь - то паду и я.'
        $ del enemy_list[0]
        $ mistress_in_battle = True
        call lb_war_last_battle from _call_lb_war_last_battle_2
        return
      'Пожертвовать Афродитой' if game.historical_check('afrodita_broken'):
        game.dragon 'Афродита, мне нужна твоя помощь. Сейчас!'
        python: #делаем аватарку старухи  для диалогового окна
            afrodita= Talker(game_ref=game)
            afrodita.avatar = "img/avahuman/afrodita.jpg"
            afrodita.name = 'Афродита' 
        $ enemy_name=data.last_enemies[enemy_list[0] ]['name_r']
        afrodita 'Ничтожная с радостью выполнит волю Господина и возьмёт на себя [enemy_name]'
        $ text = data.last_enemies[enemy_list[0]]['afrodita']
        show expression data.last_enemies[enemy_list[0]]['image'] as fg
        '[text]'
        game.dragon 'Похоже, пантеону олимпийцев придётся искать новую богиню любви!'
        hide fg
        python:
          for i in reversed(xrange(len(game.history_mod))):
            if game.history_mod[i].historical_name == 'afrodita_broken':
              del game.history_mod[i]
          del enemy_list[0]
        if len(enemy_list)>0:
          call lb_war_last_battle from _call_lb_war_last_battle_3
          return
      'Пожертвовать Дану' if game.historical_check('danu_broken'):
        game.dragon 'Дану, мне нужна твоя помощь. Сейчас!'
        $ enemy_name=data.last_enemies[enemy_list[0]]['name_r']
        danu 'Ничтожная с радостью выполнит волю Господина и возьмёт на себя [enemy_name]'
        $ text = data.last_enemies[enemy_list[0]]['danu']
        show expression data.last_enemies[enemy_list[0]]['image'] as fg
        '[text]'
        game.dragon 'Похоже, альвам придётся искать нового бога. Надо бы подсуетиться и занять вакантное местечко...'
        hide fg
        python:
          for i in reversed(xrange(len(game.history_mod))):
            if game.history_mod[i].historical_name == 'danu_broken':
              del game.history_mod[i]
          del enemy_list[0]
        if len(enemy_list)>0:
          call lb_war_last_battle from _call_lb_war_last_battle_4
          return
      'Броситься в бой':
        game.dragon 'Ой, мамочки... как же не хочется умирать за  пять минут до победы...'
        game.dragon 'Кого бы выбрать-то?'
        python:
          enemy_menu = []
          for vrag in xrange(len(enemy_list)):
            enemy_menu.append((data.last_enemies[enemy_list[vrag]]['name_r'], vrag))
          enemy_menu = sorted(enemy_menu, key=lambda vrag: vrag[0])
          vrag=renpy.display_menu(enemy_menu)
          game.foe = Enemy(enemy_list[vrag], game_ref=game)
        $ narrator(show_chances(game.foe))
        $ enemy_name=data.last_enemies[enemy_list[vrag]]['name_r']
        $ del enemy_list[vrag]
        if len(enemy_list) == 0:
          if game.army.force >= 1000:
            'Армия тьмы приходит на помощь своему предводителю. С помощью своих отродий [game.dragon.name] быстро побеждает [enemy_name]'
          else:
            'Воины армии тьмы танцуют и поют, всячески выражая поддержку своему предводителю.'
            game.dragon 'Гады! Лучше бы помогли!'
            $ battle.army_battle=True
            call lb_fight(skip_fear=True) from _call_lb_fight_96
        elif len(enemy_list) == 1:
          $ enemy_name=data.last_enemies[enemy_list[0]]['name_t']
          'Армия тьмы вступает в бой с [enemy_name].'
          show expression data.last_enemies[enemy_list[0]]['image'] as fg
          if game.army.force >= 1000:
            $ text = data.last_enemies[enemy_list[0]]['win']
            $ game.army.power_percentage()
            '[text]'
            hide fg
            $ battle.army_battle=True
            call lb_fight(skip_fear=True) from _call_lb_fight_97
          else:
            $ text = data.last_enemies[enemy_list[0]]['loss']
            $ game.army.power_percentage()
            '[text]'
            hide fg            
            $ enemy_name=data.last_enemies[enemy_list[0]]['name']
            '[enemy_name] бьёт в спину сражающемуся дракону и убивает его!'
            if not mistress_in_battle:
              nvl clear
              'Так, в [game.year], бесславно завершился поход Армии Тьмы.'
              jump lb_game_over
            else:
              nvl clear
              'Оказавшись наедине с тремя чемпионами Вольных, Тёмная Госпожа попыталась сбежать.'
              'Но силы Света не упустили подвернувшуюся возможность. Тёмная Госпожа была повержена.'
              call lb_mistress_defeat from _call_lb_mistress_defeat_1
        elif len(enemy_list) == 2:    
          $ enemy_name_1=data.last_enemies[enemy_list[0]]['name_t']
          $ enemy_name_2=data.last_enemies[enemy_list[1]]['name_t']
          'Армия тьмы вступает в бой с [enemy_name_1] и [enemy_name_2].' 
          if game.army.force >= 2000: 
            'Благодаря своей численности Армия тьмы противостоит сразу двум чемпионам!' 
            show expression data.last_enemies[enemy_list[0]]['image'] as fg
            $ text = data.last_enemies[enemy_list[0]]['win']
            $ game.army.power_percentage()
            '[text]'
            hide fg
            show expression data.last_enemies[enemy_list[1]]['image'] as fg
            $ text = data.last_enemies[enemy_list[1]]['win']
            $ game.army.power_percentage()
            '[text]'
            hide fg
            $ battle.army_battle=True
            call lb_fight(skip_fear=True) from _call_lb_fight_98
          else:
            $ enemy_name_1=data.last_enemies[enemy_list[0]]['name']
            $ enemy_name_2=data.last_enemies[enemy_list[1]]['name']
            '[enemy_name_1] и [enemy_name_2], объединившись, легко разбивают Армию тьмы.'  
            game.dragon 'Эй! Трое на одного - это нечестно!'
            'Чемпионы Вольных считали иначе. После короткой, но яростной схватки дракон был уничтожен.'
            if not mistress_in_battle:
              nvl clear
              'Так, в [game.year], бесславно завершился поход Армии Тьмы.'
              jump lb_game_over
            else:
              nvl clear
              'Четверо Чемпионов Вольных - это слишком даже для Тёмной Госпожи. Владычица была повержена.'
              call lb_mistress_defeat from _call_lb_mistress_defeat_2
        else:   
          $ enemy_name_1=data.last_enemies[enemy_list[0]]['name']
          $ enemy_name_2=data.last_enemies[enemy_list[1]]['name']
          $ enemy_name_3=data.last_enemies[enemy_list[2]]['name']
          if len(enemy_list) == 3:
            '[enemy_name_1], [enemy_name_2] и [enemy_name_3] за пару минут разбили армию тьмы, а потом легко убили сражающегося дракона.'
          else:
            $ enemy_name_4=data.last_enemies[enemy_list[3]]['name']
            '[enemy_name_1], [enemy_name_2], [enemy_name_3] и [enemy_name_4] легко разбили Армию Тьмы, а потом легко убили сражающегося дракона.'
          if not mistress_in_battle:
            nvl clear
            'Так, в [game.year], бесславно завершился поход Армии Тьмы.'
            jump lb_game_over
          else:
            nvl clear
            mistress 'Что?!! Неужели годы подготовки, куча генетических экспериментов, глубины тёмного чародйства, заговоры и интриги, победы и битвы, все свершения детей моих - всё впустую?!'
            python:
              angel= Talker(game_ref=game)
              angel.avatar = "img/archimonde/angel.jpg"
              angel.name = 'Ангел'
              danu= Talker(game_ref=game)
              danu.avatar = "img/avahuman/danu.jpg"
              danu.name = 'Богиня Дану' 
              athena= Talker(game_ref=game)
              athena.avatar = "img/avahuman/athena.jpg"
              athena.name = 'Афина' 
            angel 'Именно так, ибо Свет всегда торжествует!'
            danu 'В твои годы пора бы уж и понять, что добро обязательно победит зло и поставит его на колени!'
            athena 'И на "жестоко убьёт" не рассчитывай. Жить будешь долго!'
            call lb_mistress_defeat from _call_lb_mistress_defeat_3
    'Вольные напоследок выпустили самых сильных своих бойцов, но и они оказались разбиты. Война выиграна!!!'
    call lb_orgy from _call_lb_orgy_2      
    return

label lb_mistress_defeat:
    nvl clear
    'Тёмная Госпожа предстала перед бесстрастным судом.'
    'Приговор был суров, но справедлив.'
    hide bg
    nvl clear
    show expression 'img/scene/mistress_defeat.jpg' as bg  
    'Лишённая всех своих сил, кроме бессмертия, полностью обнажённая, Тёмная Госпожа была прикована у стен королевского дворца.'
    'И вскоре, движемый могущественным заклинанием, её начал насиловать огромный металлический фаллос'
    nvl clear
    'Тёмная Госпожа лишь рассмеялась над таким "наказанием"...'
    'И смех её длился много часов.'
    nvl clear
    'К исходу первой недели с её губ сорвался первый стон боли'
    'Через пять месяцев она стала умоляла о смерти'
    nvl clear
    'Однако приговор был суров, но справедлив: {i}"Столько времени будет двигаться фаллос, сколько в Землях Вольных длилась эпоха драконов!"{/i}'
    $ data.achieve_target("mistress", "battle")
    call lb_achievement_acquired from _call_lb_achievement_acquired_6
    jump lb_game_over
    return

