# coding=utf-8
init python:
    from pythoncode import treasures
    from pythoncode.characters import Enemy
    from pythoncode.historical import historical
        
label lb_location_city_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))        
    $ place = "city_gates"
    hide bg
    show place as bg
    nvl clear
    
    if game.dragon.energy() == 0:
        'Даже драконам надо иногда спать. Особенно драконам!'
        return      

    if game.witch_st1==5:
      'Дракон на мгновение задумывается, какой может быть награда ведьмы.'
      game.dragon 'Надо сходить проверить!'
      return

    # @fdsc Просто убрал лишнюю надпись
    # 'Столица королевства людей.'
    menu:
        'Ограбить королевский дворец'  if game.dragon.can_fly and game.dragon.energy() > 0 and game.dragon.injuries <= 0:
            call lb_city_palace_atk(True)
        'Грабить королевский дворец целый день' if game.dragon.can_fly and game.dragon.energy() > 0 and game.dragon.injuries <= 0:
            while game.dragon.energy() > 0 and game.dragon.injuries <= 0:
                call lb_city_palace_atk(True, True)

        'Украсть девушку с рынка' if game.dragon.can_fly and  not (game.witch_st1==6 or game.witch_st1==7) and game.dragon.energy() > 0 and game.girls_list.free_size-game.girl.size >= 0:
            # @fdsc
            # 'Легко перемахнув через городскую стену, [game.dragon.kind] оказывается в самом центре города. От летучего врага укрепления не спасут...'
            call lb_city_market_atk(True)

            # @fdsc Девушки добровольно соглашаются
            # $ game.girl.willing=True
            # $ game.dragon.drain_mana(game.girl.quality + 1)
            
            $ text = u'Заполучив девицу, дракон утащил бедняжку в своё логово%s. \n\n' % game.lair.type.name_locative

            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            $ description = game.girls_list.steal_girl()
            $ place = game.lair.type_name
            show place
            nvl clear
            $ description = game.girls_list.jail_girl()

            pass

        'Устроить резню на рынке' if game.dragon.can_fly and game.dragon.energy() > 0 and game.dragon.injuries <= 0:
            # while game.dragon.energy() > 0 and game.dragon.injuries <= 0:
            call lb_city_market_atk(False, True)

        ''

        'Тайный визит' if game.dragon.mana > 0:
            'Дракон превращается в человека и проходит в город. На это пришлось потратить драгоценную волшебную силу...'
            $ game.dragon.drain_mana()
            nvl clear
            call lb_city_walk from _call_lb_city_walk
        'Штурмовать ворота' if not game.dragon.can_fly and not (game.witch_st1==6 or game.witch_st1==7):
            'Заметив приближение опасности, бдительные стражники закрывают ворота. Придётся порываться с боем...'
            call lb_city_gates from _call_lb_city_gates
        'Влететь внутрь' if game.dragon.can_fly and  not (game.witch_st1==6 or game.witch_st1==7):
            # @fdsc
            # 'Легко перемахнув через городскую стену, [game.dragon.kind] оказывается в самом центре города. От летучего врага укрепления не спасут...'
            call lb_city_raze from _call_lb_city_raze
        'Выпить зелье ведьмы и принять облик короля' if game.witch_st1==2:
            $ game.witch_st1=3
            # @fdsc
            # 'Дракон принимает человеческий облик и легко проходит в город. '
            nvl clear
            call lb_city_walk from _call_lb_city_walk_11          
        'Уйти прочь'  if not (game.witch_st1==6 or game.witch_st1==7):
            return
            
    return

label lb_city_gates:
#    $ game.dragon.drain_energy()
    $ game.foe = Enemy('city', game_ref=game)
    call lb_fight from _call_lb_fight_68
    call lb_city_raze from _call_lb_city_raze_1
    return

label lb_city_raze:
    show expression 'img/bg/city/inside.jpg' as bg
    # @fdsc
    # 'Беззащитный город готов познать ярость отродья Госпожи.'
    nvl clear
    python:
        cathedral_ruined = game.historical_check('cathedral_ruined')
        
    menu:
        'Королевский дворец':
            call lb_city_palace_atk from _call_lb_city_palace_atk

        'Рыночная площадь':
            call lb_city_market_atk from _call_lb_city_market_atk

        'Кафедральный собор' if not cathedral_ruined and game.witch_st1==0:
            call lb_city_cathedral_atk from _call_lb_city_cathedral_atk

        'Руины кафедрального собора' if cathedral_ruined:
            call lb_city_cathedral_ruined from _lb_city_cathedral_ruined
            jump lb_city_raze
            
        'Богатые кварталы':
            call lb_city_jew_atk from _call_lb_city_jew_atk
            
        'Покинуть город':
            return
            
    return

label lb_city_walk:
    show expression 'img/bg/city/inside.jpg' as bg
    if game.witch_st1==3:
      'Король изящным движением руки прерывает доклад начальника караула и идёт дальше'
    else:
      'Загадочный путник проходит мимо бдительной стражи и входит в бурлящий жизнью город.'
    nvl clear
    python:
        cathedral_ruined = game.historical_check('cathedral_ruined')
    menu:
        'Королевский дворец'  if not (game.witch_st1==6 or game.witch_st1==7):
            call lb_city_palace from _call_lb_city_palace

        'Рыночная площадь'  if not (game.witch_st1==6 or game.witch_st1==7):
            call lb_city_market from _call_lb_city_market

        'Кафедральный собор' if not cathedral_ruined and not  game.witch_st1==7:
            call lb_city_cathedral from _call_lb_city_cathedral

        'Руины кафедрального собора' if cathedral_ruined:
            call lb_city_cathedral_ruined from _lb_city_cathedral_ruined_1
            jump lb_city_walk
            
        'Мастерская ювелира'  if not (game.witch_st1==6 or game.witch_st1==7):
            call lb_city_jewler from _call_lb_city_jewler
            
        'Таверна "Подвязки королевы"' if game.witch_st1==7:
            call lb_city_tavern from _call_lb_city_tavern

        'Покинуть город' if not (game.witch_st1==6 or game.witch_st1==7):
            return
            
    return

label lb_city_tavern:
    nvl clear
    hide bg
    show expression 'img/bg/city/night_watch.jpg' as bg
    $ game.witch_st1 =0
    'Дракон с удовольсвием вошёл в это развесёлое местечко. Даже как-то жаль, что с девственницами тут негусто... только одна Марианна и есть!'
    game.dragon 'Как ты только прийти рискнула?'
    marianna 'Пришлось рискнуть'
    marianna 'Я знаю, что не сегодня-завтра король отдаст приказ о моей ликвидации. Чтобы выжить, я должна пойти на экстренные меры.'
    marianna 'Я предлагаю тебе собственное тело. Взамен ты дашь мне пятьсот фартингов, отнесёшь в безопасное место и отпустишь.'
    game.dragon 'А ты не обнаглела?'
    marianna 'Я начну восстание против короля Сылтана. Тебе это тоже будет выгодно.'
    game.dragon 'А почему ты обратилась именно ко мне?'
    marianna 'Для придворных я сейчас всё равно что прокажённая. У Королевы и Гвидона денег пока что нет. Она посоветовала обратиться к тебе. Что же, раз Королева выдержала... неужели я не справлюсь?'
    game.dragon.third '[game.dragon.fullname] задумывается. С одной стороны, чем больше неурядиц у Вольных, тем лучше для Тёмной Госпожи. С другой стороны, денег-то тоже жалко!'
    menu:
      'Дать 500 фартингов':
        $ game.dragon.drain_energy()
        game.dragon.third 'Дракон галантно берёт Марианну под руку и ведёт её прочь из города'
        $ place = 'plain'
        hide bg
        show expression get_place_bg(place) as bg
        nvl clear
        $ description = game.girls_list.new_girl(girl_type='princess',girl_nature='proud',girl_hair='blond',tres=False,name_number='28',avatar='img/avahuman/marianna.jpg') 
        $ text = u'%s родилась племянницей короля - и в этом не было ничего хорошего. Когда она узнала, что Сылтан решил избавиться от потенциальной претендентки на престол, она в отчаянии, пытаясь раздобыть хоть немного денег, обратилась за помощью к дракону. Что же, дракон с удовольствием купил её невинность за 500 фартингов, позволив %s заложить основу повстанческой армии!\n\n' % (game.girl.name, game.girl.name_d)
        $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
        game.girl.third "[description]"
        game.dragon 'Держи, вымогательница!'
        $ game.lair.treasury.money -= 500
        $ game.girl.willing=True # Добровольно согласна на секс с драконом
        '[game.girl.name] скупо кивает'
        game.girl 'Я твоя.'
        nvl clear
        menu:
         'Надругаться' if game.girls_list.is_mating_possible:
            # Alex: Added sex images:
            call lb_nature_rape from _call_lb_nature_rape_11
            if game.girl.dead:
              return
        
         # @fdsc Гипноз
         'Загипнотизировать' if game.dragon.mana > game.girl.quality and not game.girl.willing:

            # @fdsc Девушки добровольно соглашаются
            $ game.girl.willing=True
            $ game.dragon.drain_mana(game.girl.quality + 1)
            pass

         'Магическое уменьшение' if not game.girls_list.is_mating_possible and game.girl.virgin and not game.girls_list.is_giant and game.dragon.lust > 0 and not game.girl.old:
           game.dragon 'Заклятье временного уменьшения!'
           $ game.dragon.gain_rage()
           call lb_nature_rape from _call_lb_nature_rape_12
           if game.girl.dead:
             return
        game.girl 'Всё, я пошла'
        game.dragon 'Скатерью дорога!'
        $ game.rebel_girl=game.girl
        $ game.rebel_id=game.girl.girl_id
        $ game.history = historical( name='rebel_niece',end_year=game.year+1,desc=None,image=None)
        $ game.history_mod.append(game.history)
      'Чтобы я давал деньги мясу?!':
        $ game.dragon.drain_energy()
        'Дракон принимает истинный облик'
        'Городской дозор отважно выступает на защиту родной таверны.'
        $ game.foe = Enemy('city_watch', game_ref=game)
        call lb_fight from _call_lb_fight_91
        'Дракон хатает королевскую племянницу и уносит её за город, где ничто не помешает их тесному общению.'  
        $ place = 'plain'
        hide bg
        show expression get_place_bg(place) as bg
        nvl clear
        $ description = game.girls_list.new_girl(girl_type='princess',girl_nature='proud',girl_hair='blond',tres=False,name_number='28',avatar='img/avahuman/marianna.jpg') 
        $ text = u'%s родилась племянницей короля - и в этом не было ничего хорошего. Когда она узнала, что Сылтан решил избавиться от потенциальной претендентки на престол, она в отчаянии, пытаясь раздобыть хоть немного денег, обратилась за помощью к дракону. Увы, %s предпочёл взять своё силой!\n\n' % (game.girl.name, game.dragon.fullname)
        $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
        $ game.dragon.reputation.points += 3
        '[game.dragon.reputation.gain_description]'
        nvl clear
        game.girl.third "[description]"
        call lb_nature_sex from _call_lb_nature_sex_61    
      'Не интересует, счастливо оставаться!':
        $ game.dragon.gain_rage()
        marianna 'Но...'
        game.dragon.third 'Когда дракон выходил из таверны, к столику Марианны как раз подсаживались какие-то мутные личности. Надо тщательнее выбирать место для встреч!'
    return

label lb_city_palace:
    nvl clear
    hide bg
    show expression 'img/bg/city/palace.jpg' as bg
    'Гордая цитадель возвышается на холме в центре города. Здесь находится зимняя резиденция короля. Изнутри доносятся соблазнительные ароматы драгоценностей и благородных дев. На воротах стоят бдительные гвардейцы.'
    $ game.foe = Enemy('palace_guards', game_ref=game)
    $ chances = show_chances(game.foe)
    nvl clear
    menu:
        'Напасть':
            call lb_city_palace_atk from _call_lb_city_palace_atk_1
        'Пройти как к себе домой' if game.witch_st1==3:
            if game.dragon.lust == 0:
              game.dragon 'С удовольствием пообщался бы с Королевой... увы, сейчас она представляет для меня лишь гастрономический интерес!'
              return
            'Гвардецы дисциплинированно берут оружие "на изготовку", когда мимо них проходит монарх'
            call lb_city_palace_seduction from _call_lb_city_palace_seduction
        'Уйти':
            call lb_city_walk from _call_lb_city_walk_1
    
    return

label lb_city_palace_seduction:
    $ game.dragon.drain_energy()
    hide bg
    nvl clear
    show expression 'img/scene/palace_reception.jpg' as bg
    python: #делаем аватарку старухи  для диалогового окна
        butler= Talker(game_ref=game)
        butler.avatar = "img/avahuman/butler.jpg"
        butler.name = 'Старик-дворецкий'  
    'К дракону семенящим шагом  спешит старик-дворецкий'
    butler 'Здравствуйте-здравствуйте, Ваше Величество! Как хорошо, что вы вернулись раньше срока! С вами очень хотят поговорить маршал, казначей и мастер над шептунами.'
    game.dragon 'Я очень устал, и собираюсь пройти в покои к своей королеве'
    butler 'Понимаю-понимаю, дело молодое. Но всё-таки, Ваше Величество, хорошо было бы поговорить хоть с кем-то из них. А то если делами Кролевства не заниматься, то так и до беды недалеко, уж поверьте старику, который Вас на руках носил. '
    menu:
        'Я поговорю с маршалом':
            game.dragon 'Ладно, война - дело важное. Где там наш маршал?'
            call lb_city_marshal from _call_lb_city_marshal
        'Я поговорю с казначеем':
            game.dragon 'Денежки, как известно, счёт любят. С удовольствием встречусь с казначеем!'
            call lb_city_treasurer from _call_lb_city_treasurer
        'Я поговорю с мастером над шептунами':
            game.dragon 'От яда в спине и кинжала в бокале никто не застрахован. Надо бы повидать мастера над шептунами!'
            call lb_city_spy_master from _call_lb_city_spy_master
    return

label lb_city_marshal:
    hide bg
    nvl clear
    show expression 'img/scene/armory.jpg' as bg
    python: 
        marshal= Talker(game_ref=game)
        marshal.avatar = "img/avahuman/marshal.jpg"
        marshal.name = 'Маршал'  
    'В дворцовой оружейной замаскированного дракона ждёт старый, но ещё крепкий маршал'
    marshal 'Ваше Величество, в прошлый раз мы с Вами обсуждали поход против герцога Робертина де Пруа.'
    nvl clear
    game.dragon.third 'Ой'
    game.dragon 'Напомни, в чём там дело было'
    marshal 'Герцог прославился во время войны с Тёмной Госпожой. Он любим и популярен в народе, его почитают как героя. Надо побыстрее от него избавиться, пока он не задумал восстание.'
    game.dragon 'А он задумывает восстание?'
    marshal 'А это совершенно не важно. Важно, что он {i}может{/i} задумать восстание. Отборные войска уже стоят на границах герцогства. Мы ждём Вашего приказа, Ваше Величество!'
    nvl clear
    game.dragon.third 'Междусобная война у Вольных не просто выгодна, она очень выгодна! Но неужели король и впрямь воюет со своими подданными по столь надуманным предлогам?'
    menu:
      'Пройтись по герцогству огнём и мечом. Не щадить никого!':
        marshal 'Суровый, но необходимый приказ, Ваше Величество. Их владения запылают. Думаю, способ казни для семьи мятеников мы обдумаем позднее.'
        game.dragon 'Обязательно, у меня уже есть несколько интересных идей. Но прошу меня простить - меня ждёт моя королева.'
        $ game.poverty.value += 2
        $ game.history = historical( name='marshal_hard',end_year=None,desc=None,image=None)
        $ game.history_mod.append(game.history)
        call lb_city_queen from _call_lb_city_queen_1
      'Война должна быть быстрой, как удар молнии!':
        marshal 'Спорное утверждение... хотя, думаю, это можно устроить. Правда, в этом случае мы разберёмся только с самим герцогом, его семья, вероятно, уцелеет...'
        game.dragon 'Ну и демон с ними, всё равно герцогство де Пруа отойдёт трону.'
        marshal 'Вы как всегда правы, Ваше Величество'
        game.dragon 'А как же иначе? Впрочем, прошу меня простить - меня ждёт моя королева.'        
        $ game.poverty.value += 1
        $ game.history = historical( name='marshal_soft',end_year=None,desc=None,image=None)
        $ game.history_mod.append(game.history)
        call lb_city_queen from _call_lb_city_queen_2
      'Я не собираюсь идти войной на моего верного герцога!':
        marshal 'Что? Кто ты такой и куда дел этого идиота, тьфу ты, короля?!'  
        marshal 'Стража!!!'
        'В оружейную врывается отряд гвардейцев. К ужасу дракона, позади них маячит фигура Верховного мага.'
        python: 
            archmage= Talker(game_ref=game)
            archmage.avatar = "img/avahuman/archmage.jpg"
            archmage.name = 'Верховный маг'  
        archmage 'Так, так, что у нас здесь творится?'
        nvl clear
        game.dragon.third 'Кажется, неправильный ответ будет смертельным'
        menu:
          'Этот человек планировал уничтожить семейство де Пруа по совершенно надуманному поводу...':
            call lb_city_archmage from _call_lb_city_archmage_1
          'Палач!':
            'Из задних рядов гвардецев выходит королевский палач'
            python: 
              executioner= Talker(game_ref=game)
              executioner.avatar = "img/avahuman/executioner.jpg"
              executioner.name = 'Королевский палач'  
            executioner 'Да?'
            game.dragon 'Этот человек предлагал начать гражданскую войну и уничтожить моего верного вассала, герцога Робертина де Пруа. Казнить изменника.'
            marshal 'Нет! Вы всё неправильно поняли, это вовсе не король...'
            game.dragon 'Думаю, повешения, потрошения и четвертования будет достаточно. В любом порядке.'
            archmage 'А, просто очередные шалости'
            executioner 'А по мне, король ведёт себя вполне по-королевски!'
            'Визжащего маршала утаскивают в застенки, а [game.dragon.fullname], вежливо кивнув присутствующим, идёт в покои к королеве'  
            $ game.history = historical( name='marshal_none',end_year=None,desc=None,image=None)
            $ game.history_mod.append(game.history)
            call lb_city_queen from _call_lb_city_queen_3
    return

label lb_city_treasurer:
    hide bg
    nvl clear
    show expression 'img/scene/treasury.jpg' as bg
    python: 
        treasurer= Talker(game_ref=game)
        treasurer.avatar = "img/avahuman/treasurer.jpg"
        treasurer.name = 'Казначей'  
    'Дракон входит в сокровищницу и восхищённо оглядывается. Сколько же здесь всего! Как притягательно пахнут все эти богатства!'
    '[game.dragon.name] не может удержаться и прихватизирует горсть монет.'
    $ gain = random.randint(5,10)
    $ game.lair.treasury.dublon += gain
    'Навстречу мнимому монарху спешит толстячок-казначей.'
    treasurer 'Ваше Величество, Ваше Величество, безумно, безумно рад Вас видеть! Как хорошо, что Вы прибыли раньше срока. У меня накопился ряд вопросов...'
    game.dragon 'Покороче'
    treasurer 'Что с турниром?'
    game.dragon 'А что не так с турниром?'
    treasurer 'О, в честь победы над Тёмной Госпожой Вы приказли устроить великий турнир! На него соберутся рыцари и воины со всего Королевства, и награда для победитля тоже будет соответстующей.'
    nvl clear
    game.dragon.third 'Какая глупая трата средств'
    game.dragon 'Всё ещё не могу понять, что не так с турниром?'
    treasurer 'О, Ваше Величество, сущая малость! Круглосуточно, не смыкая глаз, мы работали, занимались королевскими нуждами и заботами. '
    treasurer 'И я рад сообщить вам итоги работы последних лет: результаты есть.'
    treasurer 'Просто денег нет.'
    nvl clear
    'Лжемонарх потрясённо обводит рукой помещение'
    game.dragon 'И это называется - нет?!'
    treasurer 'Ваше Величество, во время войны с Тёмной Госпожой мы изрядно поиздержались. Почти все сокровища заложены, скоро в Столицу за ними приедет караван цвергов'
    treasurer 'Чтобы найти деньги на турнир, их придётся у кого-нибудь занять!'
    menu:
      'Почему бы не занять у Султаната?':
        treasurer 'Прекрасная идея, Ваше Величество! Правда, они наверняка попросят каких-либо мелких уступок - например, выпустить на свободу нескольких работорговцев...'
        game.dragon 'Не вижу ничего плохого в работорговле'
        treasurer 'Разумеется, Ваше Величество! Но как учит великий мудрец Овертон, подобные идеи следует вводить постепенно. Это дело не одного года и даже не одного десятилетия...'
        game.dragon 'Ничего, я никуда не спешу. Займись переговорами с Султанатом. Я пойду - меня ждёт моя Королева.'        
        $ game.poverty.value += 1
        $ game.history = historical( name='treasurer_hard',end_year=None,desc=None,image=None)
        $ game.history_mod.append(game.history)
        call lb_city_queen from _call_lb_city_queen_4
      'Вот у цвергов сокровища и перезаложим!':  
        treasurer 'Неплохая идея, Ваше Величество. Правда, они наверняка попросят каких-либо уступок - например, решат основать на поверхности карликовую крепость...'  
        game.dragon 'Не вижу ничего плохого в карликовой крепости. Займись этим. Мне же пора идти - меня ждёт моя Королева.'
        $ game.history = historical( name='treasurer_soft',end_year=None,desc=None,image=None)
        $ game.history_mod.append(game.history)
        call lb_city_queen from _call_lb_city_queen_5
      'Мне кажется, пора провести тщательную ревизию...': 
        treasurer 'Что? Кто ты такой и куда дел этого идиота, тьфу ты, короля?!'  
        treasurer 'Стража!!!'
        'В сокровищницу осторожно входит небольшой отряд гвардейцев. Вряд ли они поверят обвинениям какого-то казначея... но, к ужасу дракона, позади них маячит фигура Верховного мага.'
        python: 
            archmage= Talker(game_ref=game)
            archmage.avatar = "img/avahuman/archmage.jpg"
            archmage.name = 'Верховный маг'  
        archmage 'Так, так, что у нас здесь творится?'
        nvl clear
        game.dragon.third 'Кажется, неправильный ответ будет смертельным'
        menu:
          'Этот мошенник явно мухлюет с королевской казной!':
            call lb_city_archmage from _call_lb_city_archmage_2
          'Палач!':
            'Из задних рядов гвардецев выходит королевский палач'
            python: 
              executioner= Talker(game_ref=game)
              executioner.avatar = "img/avahuman/executioner.jpg"
              executioner.name = 'Королевский палач'  
            executioner 'Да?'
            game.dragon 'Этому человеку очень не понравилась идея ревизии сокровищницы. Уверен, он виноват в хищениях в особо крупных размерах. Думаю, перед началом расследования его стоит немного попытать.'
            treasurer 'Нет! Вы всё неправильно поняли, это вовсе не король...'
            game.dragon 'Думаю, для начала стоит снять кожу с его ладоней.'
            archmage 'А, просто очередные шалости. К тому же, полгода работы казначеем - и можно казнить без всяких разбирательств.'
            executioner 'А по мне, король ведёт себя вполне по-королевски!'
            'Визжащего казначея утаскивают в застенки, а [game.dragon.fullname], вежливо кивнув присутствующим, идёт в покои к королеве'  
            $ game.history = historical( name='treasurer_none',end_year=None,desc=None,image=None)
            $ game.history_mod.append(game.history)
            call lb_city_queen from _call_lb_city_queen_6
    return

label lb_city_spy_master:
    hide bg
    nvl clear
    show expression 'img/scene/spy_room.jpg' as bg
    python: 
        spy_master= Talker(game_ref=game)
        spy_master.avatar = "img/avahuman/spy_master.jpg"
        spy_master.name = 'Мастер над шептунами'  
    'Поддельный король осторожно входит в логово мастера над шептунами. Ему уже не кажется, что прийти сюда было хорошей идеей.'
    spy_master 'Вы уже вернулись? Признаться, не ожидал вас так рано. В любом случае, мне нужны указания по поводу Марианны.'
    nvl clear
    game.dragon.third 'Ой'
    game.dragon 'Какого рода указания?'
    spy_master 'Ваше Величество...'
    'В голосе мастера над шепутнами слышится сомнение - он явно пытается понять, в самом ли деле это "величество" и насколько оно "его"'
    spy_master 'Ваша племянница юна, чиста и невинна. Но её потомство потенциально может представлять угрозу для трона. Ради безопасности Королевства требуется предпринять... определённые меры.'
    menu:
      'Думаю, несчастный случай в дороге - это то, что нужно в данной ситуации':
        spy_master 'Печально, но необходимо. Жаль, что даже после победы на дорогах так небезопасно.'
        game.dragon 'Да, жаль. Прошу меня простить - меня ждёт моя Королева.'
        $ game.history = historical( name='spy_hard',end_year=None,desc=None,image=None)
        $ game.history_mod.append(game.history)
        call lb_city_queen from _call_lb_city_queen_7
      'Сослать в монастырь, и всего делов':
        'Мастер над шептунами отчётливо морщится'
        spy_master 'Не очень надёжно, но, в принципе, приемлимо.'
        '[game.dragon.name] кивает и спешно покидает комнату. И почему у него такое ощущение, что его раскусили, но не стали ничего предпринимать?'
        $ game.history = historical( name='spy_soft',end_year=None,desc=None,image=None)
        $ game.history_mod.append(game.history)
        call lb_city_queen from _call_lb_city_queen_8
      'Эта "угроза" совершенно надуманна!':
        spy_master 'А, вот как'
        'Мастер над шептунами спокойно подходит к двери'
        spy_master 'Стража!'
        'В сокровищницу входит небольшой отряд гвардейцев. Неизвестно, поверят ли они обвинениям какого-то казначея... но, к ужасу дракона, позади них маячит фигура Верховного мага.'
        python: 
            archmage= Talker(game_ref=game)
            archmage.avatar = "img/avahuman/archmage.jpg"
            archmage.name = 'Верховный маг'  
        archmage 'Так, так, что у нас здесь творится?'
        nvl clear
        game.dragon.third 'Кажется, неправильный ответ будет смертельным'
        menu:
          'Этот негодяй замышлял убийство моей племянницы!':
            call lb_city_archmage from _call_lb_city_archmage_3
          'Палач!':
            'Из задних рядов гвардецев выходит королевский палач'
            python: 
              executioner= Talker(game_ref=game)
              executioner.avatar = "img/avahuman/executioner.jpg"
              executioner.name = 'Королевский палач'  
            executioner 'Да?'
            game.dragon 'Этот человек замыслил убить мою племянницу. Никто не смеет поднимать руку на королевскую кровь. Взять его!'
            spy_master 'Нет! Вы всё неправильно поняли, это вовсе не король...'
            game.dragon 'Думаю, для начала стоит вырвать его язык.'
            archmage 'А, просто очередные шалости. '
            executioner 'А по мне, король ведёт себя вполне по-королевски!'
            'Визжащего казначея утаскивают в застенки, а [game.dragon.fullname], вежливо кивнув присутствующим, идёт в покои к королеве'  
            $ game.history = historical( name='spy_none',end_year=None,desc=None,image=None)
            $ game.history_mod.append(game.history)
            call lb_city_queen from _call_lb_city_queen_9
    return

label lb_city_archmage:
    nvl clear
    'Верховный маг что-то задумчиво бормочет себе под нос'
    nvl clear
    archmage.third 'Странно, король сегодня ведёт себя как-то слишком мягко и деликатно...'
    archmage 'Крибли-крабли-бумс!'
    'С дракона слетает магическая маскировка.'
    archmage 'А, вот в чём дело...'
    'Лёгким движением руки Верховный маг убивает дракона и идёт дальше по своим делам.'
    jump lb_game_over
    return

label lb_city_queen:
    hide bg
    nvl clear
    show expression 'img/scene/bedroom.jpg' as bg
    python: 
        queen= Talker(game_ref=game)
        queen.avatar = "img/avahuman/queen.jpg"
        queen.name = 'Королева'
    'Королева ждёт короля Сылтана прямо в спальне. Странно, похоже, она не слишком-то рада его визиту'
    queen 'Здравствуйте, Ваше Величество.'
    game.dragon 'Ну здравствуй, любимая. Я пришёл исполнить свой супружеский  долг!'
    'Королева грустнеет ещё больше'
    queen 'Понимаю. Я должна родить наследника, но до сих пор праздна. Хотя задержка... неважно.'
    queen 'Как это будет на этот раз?'
    nvl clear
    game.dragon.third 'Что-то в постановке вопроса сильно насторожило дракона.'
    game.dragon 'Полагаю, как обычно. В чём-то проблема?'
    nvl clear
    queen.third 'Королева тяжело вздохнула'
    queen 'В твоей потенции, муж мой. Неужели ты забыл? Когда ты возлягал со мной, нам приходилоь идти на различные ухищрения. Ты связывал меня, связывал служанок, приглашал ко мне стражников...'
    nvl clear
    queen.third 'Королева осекается и некоторое время молчит'    
    queen 'Я знаю, что ты любишь меня. Я знаю, что тебе не хочется подвергать меня таким унижениям. Увы, династии действительно нужен наследник.'
    queen 'Что ты выберешь на этот раз?'
    menu:
      'Как насчёт связывания?':
        $ game.history = historical( name='queen_bound',end_year=None,desc=None,image=None)
        $ game.history_mod.append(game.history)
        queen 'Как скажешь, муж мой!'
        hide bg
        nvl clear
        show expression 'img/scene/bound.jpg' as bg
        'Королева стоит у постамента, её руки и ноги крепко, но аккуратно растянуты какими-то верёвками.'
        '[game.dragon.fullname] задумчиво рассматривает женское тело. Судя по всему, с его потенцией всё в порядке!'
        queen 'Как вы накажете свою смиренную пленницу, Ваше Величество?'
        game.dragon 'Думаю, надругаюсь над ней самым противоестественным образом!'
        queen 'Ваша смиренная пленница полностью одобряет и поддерживает это наказание!'
      'Думаю, стоит пригласить служаночку...':
        $ game.history = historical( name='queen_group',end_year=None,desc=None,image=None)
        $ game.history_mod.append(game.history)
        queen 'Прекрасная идея!'
        hide bg
        nvl clear
        show expression 'img/scene/group.jpg' as bg
        'Псевдокороль совершал мерные движения, под ним покорно постанывала какая-то служанка.'
        'Королева, смеясь, ласкала себя и периодически крепко целовала Сылтана.'
        game.dragon 'Ревнуешь?'
        queen 'Что ты! Ты же король, ты можешь себе это позволить!'
        queen 'Но всё же, тебе пора бы прекратить изменять мне на моих же глазах и заняться своей законной супругой!'
        game.dragon 'С удовольствием!'
      'Пригласим-ка сюда парочку стражников, с удовольствием посмотрю на процесс со стороны!':
        $ game.history = historical( name='queen_double',end_year=None,desc=None,image=None)
        $ game.history_mod.append(game.history)
        queen 'Это же не будет считаться изменой?'
        game.dragon 'На глазах у супруга и с его разрешения? Разумеется, нет!'
        queen 'Как скажешь, супруг мой!'
        hide bg
        nvl clear
        show expression 'img/scene/double/1.jpg' as bg
        'Королева грациозно снимает одежды. В комнату заходят двое стражников и по-хозяйски начинают её лапать.'
        queen 'Тебе нравится зрелище, супруг мой?'
        hide bg
        nvl clear
        show expression 'img/scene/double/3.jpg' as bg
        'Королева обнимает одного из стражников и сквозь тканевую повязку начинает щупать "хозяйство" другого.'     
        game.dragon 'Не очень. Пока что всё излишне благопристойно.'
        hide bg
        nvl clear
        show expression 'img/scene/double/4.jpg' as bg
        'Стражники снимают остатки одежды, Королева смеётся и тесно прижимается к одному из них.'
        queen 'Ничего, сейчас это исправим!'
        hide bg
        nvl clear
        show expression 'img/scene/double/5.jpg' as bg
        'Один из стражников властно входит в отверстие, предназначенное, вообще-то, совсем не для этого. Второй с силой мнёт груди Королевы.'
        queen 'А теперь, муж мой?'
        hide bg
        nvl clear
        show expression 'img/scene/double/6.jpg' as bg     
        'Второй стражник входит в Королеву спереди. Она стонет - не понятно, от боли или от удовольствия.'
        game.dragon 'А теперь я желаю присоединиться!'
      'Зачем всё это? Я и сам по себе - парень хоть куда!':
        'Лицо Королевы озаряется улыбкой'
        queen 'Правда? Я так рада это слышать! Тебя же вылечил Верховный маг, да?'
        python: 
            archmage= Talker(game_ref=game)
            archmage.avatar = "img/avahuman/archmage.jpg"
            archmage.name = 'Верховный маг'  
        archmage 'Кто упоминает моё имя?'
        nvl clear
        'Голос исходит, кажется, с самого потолка'   
        queen 'Вы же излечили моего супруга от... известной болезни?'
        archmage 'Что? Нет. Сейчас.'
        'В внезапной вспышке телепорта в спальне появляется Верховный маг.'
        archmage 'Крибли-крабли-бумс!'
        'С дракона слетает магическая маскировка.'
        archmage 'А, вот в чём дело...'
        'Лёгким движением руки Верховный маг убивает дракона и начинает успокаивать зарыдаввшую Королеву'
        jump lb_game_over
    $ game.dragon.lust-=1
    $ game.witch_st1=4
    hide bg
    nvl clear
    show expression 'img/scene/queen_talk.jpg' as bg 
    python: 
        marianna= Talker(game_ref=game)
        marianna.avatar = "img/avahuman/marianna.jpg"
        marianna.name = 'Марианна'
    'Вечером следующего дня, когда Сылтан покинул дворец, супруга короля разговаривала с его племянницей.'
    queen 'Не знаю почему, но мне тревожно. Вчера Сылтан был каким-то не таким. Боюсь, что случилось что-то ужасное.'
    marianna 'Я удивляюсь, как ты вообще можешь жить с этим скотом?'
    queen 'Я люблю его. И как ни странно, он тоже. Иначе бы не женился, наплевав на мнение окружающих, а просто взял бы силой.'
    queen 'Я люблю его таким, какой он есть - злым, жестоким, импульсивным, распутным и при этом бессильным... Надеюсь лишь, что скоро забеременею, и все эти ужасы наконец-то закончатся. Да, он не самый лучший король...'
    marianna 'Мягко сказано! Решительно непонятно, почему ты не хочешь забеременеть от кого-нибудь другого. Мне кажется, что с нашей династией что-то не то, что она вырождается... И иногда становится жаль, что Тёмная Госпожа проиграла...'
    queen 'Как ты можешь такое говорить?!'
    marianna 'Я понимаю, что тогда настало бы царство зла, жестокости и распутства. Но всё это - пусть и замаскированное - есть и сейчас. Так было бы хотя бы честнее'
    queen 'Я не согласна, но спорить не буду. И всё равно мне кажется, что вчера случилось что-то не то. Что-то ужасное.'
    nvl clear
    'Две женщины ещё долго смотрели на море'
    return

label lb_city_palace_atk(grab=False, fast=False):
    $ game.dragon.drain_energy()
    $ game.foe = Enemy('palace_guards', game_ref=game)
    if not fast:
        $ chances = show_chances(game.foe)

    call lb_fight(game.foe, False, fast) from _call_lb_fight
    nvl clear
    hide bg
    show expression 'img/bg/city/palace.jpg' as bg
    
    $ game.dragon.reputation.points += 3
    if not fast:
        'Пока остальные защитники цитадели находятся в замешательстве, у дракона появился отличный шанс для грабежа и разбоя.\n\n[game.dragon.reputation.gain_description]'

    if grab:
        call lb_city_palace_atk_grab
        return
    
    menu:
        'Обесчестить благородную девицу':
#            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl('princess')
            $ text = u'%s, фрейлина прекрасной принцессы, прислуживала своей госпоже в королевском дворце. Что плохого могло с ней случиться в самом защищённом месте королества?! Вот только дракона не остановили ни высокие стены столицы, ни отменная выуска гвардейцев. Когда фрейлина попала в лапы дракона, в её голове билась одна-единственная мысль: "Как хорошо, что моя госпожа в безопасности!!!" \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            $ game.dragon.reputation.points += 1
            '[game.dragon.fullname] ловит благородную девицу\n[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex     
        'Вороватъ @ убиватъ':
            call lb_city_palace_atk_grab
        'Убежать':
            'Решив не искушать судьбу и использовать поднявшуюся суматоху для безопасного отхода, [game.dragon.kind] уходит прочь из города.'
    return
    
label lb_city_palace_atk_grab:
#    $ game.dragon.drain_energy()
    python:
        count = random.randint(4, 6 + game.dragon.max_energy())
        alignment = 'knight'
        min_cost = 200
        max_cost = 2000
        obtained = "Это предмет из королевской сокровищницы."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)

    $ game.lair.treasury.receive_treasures(trs)
    $ game.dragon.reputation.points += 5

    'С кровожадным рёвом [game.dragon.fullname] проносится по коридорам дворца, убивая всех на своём пути и присваивая каждую понравившуся ему вещь:\n[trs_descrptn]\n[game.dragon.reputation.gain_description]'

    return

label lb_city_market:
    show expression 'img/bg/city/market.jpg' as bg
    'Рыночная площадь полна народу. Люди покупают и продают всевозможные ненужные вещи, вроде картошки и одежды. Глупые смертные даже не догадываются, что прямо здесь стоит их самый жуткий ночной кошмар. Они беззащитны перед внезапной атакой.'
    nvl clear
    $ brothel_known = game.historical_check('brothel_known')
    $ brothel_ruined = game.historical_check('brothel_ruined')
    menu:
        'Принять истинный облик':
            'Дракон возвращает себе истинную форму. Люди в ужасе разбегаются.'
            call lb_city_market_atk from _call_lb_city_market_atk_1
        'Порасспрашивать о борделе' if not brothel_known:
            call lb_city_brothel_question from _call_lb_city_brothel_question
        'Посетить бордель' if not brothel_ruined and brothel_known:
            call lb_city_brothel from _call_lb_city_brothel
        'Посетить бордель' if brothel_ruined and brothel_known:
            call lb_city_brothel_ruined from _call_lb_city_brothel_ruined
        'Уйти':
            call lb_city_walk from _call_lb_city_walk_2

    return

label lb_city_massKilling(fast=False):
    $ game.dragon.drain_energy()
    play sound "sound/eat.ogg"
    show expression 'img/scene/fire.jpg' as bg

    $ game.dragon.reputation.points += 10

    'Зря эти обыватели думали, что за стенами столицы они в безопсности. [game.dragon.fullname] отрывается по полной, чтобы люди уж точно его не забыли. Кровь, кишки, распидорасило...\n[game.dragon.reputation.gain_description]'

    if (random.randint(1,2) == 1):
      $ game.history = historical( name='night_watch',end_year=game.year+1,desc='Доблестный городской дозор счёл, что на рынке теперь безопасно, и в поте лица патрулирует ближайшую таверну.',image='img/bg/city/night_watch.jpg')
      $ game.history_mod.append(game.history)
        
    return


label lb_city_market_atk(girl=False, massKilling=False):
    show expression 'img/bg/city/market.jpg' as bg    
    $ night_watch = game.historical_check('night_watch')
    if night_watch:
      'Городской дозор неохотно выступает на защиту родного города.'
      $ game.foe = Enemy('city_watch', game_ref=game)
      call lb_fight from _call_lb_fight_73
      'Теперь люди беззащитны перед яростью дракона!'
    nvl clear

    if girl:
        call lb_girl_citizen_market_kidnapped(True)
        return
    if massKilling:
        call lb_city_massKilling(True)
        return

    'На рыночной площади люди продают всяческие бесполезные вещи вроде молока, овощей и домашней утвари. Впрочем, тут легко можно прихватить симпатичную красотку... или, на худой конец, попросту повеселиться от души!'
    menu:
        'Устроить резню':
            call lb_city_massKilling
        'Схватить девицу':
            call lb_girl_citizen_market_kidnapped
        'Покинуть город':
            return

    return
    
label lb_girl_citizen_market_kidnapped(fast=False):
    $ game.dragon.drain_energy() 
#            $ narrator("[game.chronik.girl_id],[girls_data.index_info]")
    $ description = game.girls_list.new_girl('citizen')
    $ night_watch = game.historical_check('night_watch')

    if night_watch:
      $ text = u' %s опасалась идти на рынок за продуктами:  в последнее время дракон повадился средь бела дня таскать оттуда девиц. Но она понадеялась на доблестный городской дозор. А зря. \n\n' % game.girl.name
    else:
      $ text = u' %s даже предположить не могла, что, выйдя на рынок за продуктами, попадёт прямо в лапы дракона. \n\n' % game.girl.name    
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    if not fast:
      '[game.dragon.fullname] ловит девицу покрасивее да побогаче. Благородных дам на рынке, конечно, не найти, но вот дочери богатеев тут иногда появляются.'
      '[game.dragon.reputation.gain_description]'
    $ game.dragon.reputation.points += 3

    nvl clear
    if not fast:
      game.girl.third "[description]"

    if (random.randint(1,2) == 1):
      $ game.history = historical( name='night_watch',end_year=game.year+1,desc='Доблестный городской дозор счёл, что на рынке теперь безопасно, и в поте лица патрулирует ближайшую таверну.',image='img/bg/city/night_watch.jpg')
      $ game.history_mod.append(game.history)

    if not fast:
        call lb_nature_sex from _call_lb_nature_sex_1

    return

label lb_city_cathedral:
    hide bg
    show expression 'img/bg/city/cathedral.jpg' as bg    
    'Огромный готический собор высится над городом. Кругом нет ни одного здания, которое могло бы по вышине сравниться со шпилем соборной колокольни.'
    nvl clear
    hide bg
    show expression 'img/bg/city/cathedral_inside.jpg' as bg
    menu:
        'Разграбить собор' if game.witch_st1==0:   
            'Загадочный незнакомец входит под своды храма и прямо на глазах у молящихся преображается в чудовище.'
            call lb_city_cathedral_atk from _call_lb_city_cathedral_atk_1
        'Исповедоваться в грехах':
            call lb_city_confession from _call_lb_city_confession
        'Уйти' if not game.witch_st1==6:
            call lb_city_walk from _call_lb_city_walk_4
    return

label lb_city_confession:
    python: #делаем аватарку старухи  для диалогового окна
        nun= Talker(game_ref=game)
        nun.avatar = "img/avahuman/nun.jpg"
        nun.name = 'Святая сестра'  
    nvl clear
    'Загадочный незнакомец заходит в одну из кабинок для исповеди. Открывается крошечное окошко.'
    if game.witch_st1==6:
      call lb_city_nun_marianna from _call_lb_city_nun_marianna
      return
    if game.witch_st1==3:
      nun 'Слушаю Вас, Ваше Величество. Вы пришли снять грех с души?'
    else:
      nun 'Слушаю тебя, брат мой. Во имя Небесного Отца, сними грех с души.'
    '[game.dragon.name] принюхивается. Девственница, да ещё и благородных кровей!'
    game.dragon 'Порочен я, ибо впал в грех стяжательства.'
    if game.witch_st1==3:
      nun 'Для короля это не грех, а добродетель, Ваше Величество.'
    else:
      nun 'Отпускаются грехи твои, ибо земное - прах и тщета пред ликом Небесного Отца. Людского гнева бойся.'
    game.dragon 'Виновен я, ибо в бою отнимал жизнь людскую.'
    if game.witch_st1==3:
      'В голосе монахини слышится экстаз.'
      nun 'Отпускается Вам, Ваше Величество, ибо делали Вы это ради блага Королевства!'
    else:
      'В голосе монахини сквозит опаска.'
      nun 'Тяжек твой грех. Но чья жизнь важнее - лишь Небесному Отцу ведомо. Отпускается тебе, брат.'
    '[game.dragon.name] масляно понижает голос.'
    game.dragon 'А ещё я обожаю прелюбодействовать и совращать невинных.'
    if game.witch_st1==3:
      
      nun 'Я рада предоставить вам такую возможность, Ваше Величество!'
      game.dragon 'Эээ...'
      'Монашка входит в кабинку, хватает дракона за руку и ведёт его куда-то вниз, в подвал.'
      hide bg
      nvl clear
      show expression 'img/scene/nun.jpg' as bg
      nun 'Располагайте мной, Ваше Величество!'
      menu: 
          'Принять истинный облик':
              $ game.dragon.drain_energy()
              game.dragon 'А ты знаешь, что я, как король, обладаю особыми способностями, и могу превращаться в...'
              '[game.dragon.fullname] принимает истинный облик' 
              nun 'Ваше Величество, Вы воистину неотразимы!'  
              $ description = game.girls_list.new_girl(girl_type='princess',girl_nature='lust')
              $ game.girl.willing=True # Добровольно согласна на секс с драконом
              $ text = u'%s, девица благородных кровей, с детства страдала от странных и запретных желаний. Чтобы укротить свою греховную суть, она пошла в монастырь. Но, увидев на исповеди короля, дала волю своему похотливому нраву. Кто же знал, что под личиной короля Сылтана скрыается дракон! \n\n' % game.girl.name
#            $ narrator('[game.girl.nature]')
              $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
              game.girl.third "[description]"
              call lb_nature_sex from _call_lb_nature_sex_55  
          'Воспользоваться ситуацией' if game.dragon.lust > 0:
              $ game.dragon.drain_energy()
              'Фальшивый король неторопливо снимает штаны'
              game.dragon 'Прилоскай моё достоинство ротиком'
              nun 'Как прикажите, Ваше Величество!' 
              'Святая сестра делает неумелый, но очень старательный минет. Придя в боевую готовность, дракон начинает пользоваться ситуацией по полной.'
              nun 'Ещё, Ваше Величествооо!'
              $ game.dragon.lust -=1
              nvl clear
              game.dragon 'Ну что, теперь ты точно не попадёшь на Небеса?'
              'Обессиленная, удовлетворённая и уже не вполне невинная монашка мотает головой.'
              nun 'Почему же? Не согрешишь - не покаешься, а не поккаешься - не получишь Цаствия Небесного!'
              'Дракон покинул собор в глубоких раздумьях. Нет, ему никогда не понять логику людей!'
          'Извиниться и уйти' if game.dragon.bloodiness < 5: 
              $ game.dragon.gain_rage()  
              game.dragon 'Вы обознались. К королю я не имею никакого отношения!'
              'Монашка испуганно вскрикивает и пытается прикрыться руками. Дракон пожимает плечами и покидает собор.'
              call lb_city_walk from _call_lb_city_walk_12  
      return  
    else:
      menu:
        'Схватить монахиню':
            $ game.dragon.drain_energy()
            $ cathedral_guard = game.historical_check('cathedral_guard')
            if not cathedral_guard:
                nun 'Во имя Небесного Отцааа!!!'
                'Договорить монахиня не успевает - [game.dragon.fullname] принимает истинный облик, хватает девушку и уносит её за город, где никто не помешает их тесному общению.'
                $ game.history = historical( name='cathedral_guard',end_year=game.year+2,desc='Храмовники сочли, что кафедральный Собор в относительной безопасности, а вот простым людям необходима защита. Они патрулируют сельскую местность.',image='img/bg/city/templars.jpg')
                $ game.history_mod.append(game.history)
            else:
                'Судя по голосу, теперь монахиня полностью спокойна.'
                nun 'Во имя Небесного Отца отпускаю тебе грехи, брат мой. Иди с миром и не греши.'
                'Получив сигнал, в кабинку для исповеди врываются храмовники. [game.dragon.name] принимает истинный облик.'
                $ game.foe = Enemy('templar_guard', game_ref=game)
                call lb_fight from _call_lb_fight_74
                'Победив храмовников, [game.dragon.fullname] хватает монахиню и уносит её за город, где никто не помешает их тесному общению.'
            $ place = 'plain'
            hide bg
            show expression get_place_bg(place) as bg
            nvl clear
            $ description = game.girls_list.new_girl(girl_type='princess',girl_nature='innocent')
            $ text = u'%s, девица благородных кровей, с детства отличалась тихим и кротким нравом. Она отказалась от мирских удовольствий и посвятила свою жизнь Небесному Отцу. Увы, у дракона были иные планы! \n\n' % game.girl.name
#            $ narrator('[game.girl.nature]')
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_35    
        'Закончить исповедь и уйти' if game.dragon.bloodiness < 5:
            'Судя по голосу, монахиня в панике.'
            nun 'Во имя Небесного Отца отпускаю тебе грехи, брат мой. Иди с миром и не греши.'
            'Степенно кивнув, [game.dragon.fullname] покидает своды собора.'
            $ game.dragon.gain_rage()
    return

label lb_city_nun_marianna:
    $ game.dragon.drain_energy()
    $ game.witch_st1=0
    marianna 'Пожалуйста, заберите меня отсюда!'
    marianna 'Я знаю, у меня нечем вам заплатить...'
    marianna.third 'Монахиня с силой прикусывает губу'
    marianna 'Если хотите, можете взять плату моим телом!'
    '[game.dragon.fullname] принимает истинный облик'
    game.dragon 'Предложение в силе?'
    marianna.third 'Странная монахиня колеблется в течение нескольких секунд.'
    marianna 'Да!'
    $ place = 'plain'
    hide bg
    show expression get_place_bg(place) as bg
    nvl clear
    '[game.dragon.name] хватает монашку и уносит её за город.'
    $ game.dragon.reputation.points += 3
    '[game.dragon.reputation.gain_description]'
    $ description = game.girls_list.new_girl(girl_type='princess',girl_nature='proud',girl_hair='blond',tres=False,name_number='28',avatar='img/avahuman/marianna.jpg')
    game.girl "[description]"
    $ text = u'%s родилась племянницей короля - и в этом не было ничего хорошего. Сылтан решил избавиться от потенциальной претендентки на престол, заточив её в монастырь. Однако %s бежала при первой же возможности. Её не остановило даже то, что спаситель оказался драконом: бесчестие и смерть были для неё предпочтительнее прозябания в монастырской келье.\n\n' % (game.girl.name, game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    $ game.girl.willing=True # Добровольно согласна на секс с драконом
    game.dragon.third 'Дракон масляно понижает голос'
    game.dragon 'С нетерпением жду обещанной награды'
    game.girl 'Подождите, ещё одно предложение. Я племянница короля. Сылтан, это чудовище, заточил меня в монастырь. Если, получив свою награду, вы дадите мне 500 фаартингов и отпустите, я попытаюсь поднять восстание. Вам и самим это выгодно!'
    game.dragon.third '[game.dragon.fullname] задумывается. С одной стороны, чем больше неурядиц у Вольных, тем лучше для Тёмной Госпожи. С другой стороны, денег-то тоже жалко!'
    menu:
      'Дать 500 фартингов':
        $ game.lair.treasury.money -= 500
        $ text = u'Впрочем, %s удачно обменяла свою невинность на 500 фартингов, надеясь на эти деньги заложить основу повстанческой армии.\n\n' % (game.girl.name)
        $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
        game.dragon 'Держи, вымогательница!'
        '[game.girl.name] тяжело вздыхает и цедит сквозь сомкнутые зубы'
        game.girl 'Я твоя.'
        nvl clear
        menu:
         'Надругаться' if game.girls_list.is_mating_possible:
            # Alex: Added sex images:
            call lb_nature_rape from _call_lb_nature_rape_9
            if game.girl.dead:
              return
        
         # @fdsc Гипноз
         'Загипнотизировать' if game.dragon.mana > game.girl.quality and not game.girl.willing:

            # @fdsc Девушки добровольно соглашаются
            $ game.girl.willing=True
            $ game.dragon.drain_mana(game.girl.quality + 1)
            pass

         'Магическое уменьшение' if not game.girls_list.is_mating_possible and game.girl.virgin and not game.girls_list.is_giant and game.dragon.lust > 0 and not game.girl.old:
           game.dragon 'Заклятье временного уменьшения!'
           $ game.dragon.gain_rage()
           call lb_nature_rape from _call_lb_nature_rape_10
           if game.girl.dead:
             return
        $ place = 'plain'
        hide bg
        show expression get_place_bg(place) as bg
        nvl clear
        game.girl 'Всё, я пошла'
        game.dragon 'Скатерью дорога!'
        $ game.rebel_girl=game.girl
        $ game.rebel_id=game.girl.girl_id
        $ game.history = historical( name='rebel_niece',end_year=game.year+1,desc=None,image=None)
        $ game.history_mod.append(game.history)
      'Чтобы я давал деньги мясу?!':
        call lb_nature_sex from _call_lb_nature_sex_60 
    return

label lb_city_cathedral_atk:
    hide bg
    show expression 'img/bg/city/cathedral_atk.jpg' as bg  
    $ game.dragon.drain_energy()
    $ cathedral_guard = game.historical_check('cathedral_guard')
    if cathedral_guard:
        'Завидев ящера, храмовники бросаются ему навстречу, позволяя прихожанам вырваться из смертельной ловушки.'
        $ game.foe = Enemy('templar_guard', game_ref=game)
        call lb_fight from _call_lb_fight_75
        python:
          for i in xrange(len(game.history_mod)):
            if game.history_mod[i].historical_name == 'cathedral_guard':
              del game.history_mod[i]
              break
        'После победы над храмовниками [game.dragon.fullname] с демоническим хохотом врывается в святилище, убивая всех на своём пути и присваивая каждую понравившуся ему вещь:'
    else:
        'Немногочисленные храмовники организуют эвакуацию прихожан. Но дракону нет дела до их жалких жизней. [game.dragon.fullname] с демоническим хохотом врывается в святилище, присваивая каждую понравившуся ему вещь:'
    python:
        count = random.randint(4, 10)
        alignment = 'cleric'
        min_cost = 10
        max_cost = 500
        obtained = "Это предмет из столичного кафедрального собора."
        trs = treasures.gen_treas(count, data.loot['church'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    '[trs_descrptn]'
    $ game.history = historical( name='cathedral_ruined',end_year=game.year+5,desc='Собор в Столице Королевства  отстроен вновь. Теперь его убранство стало ещё красивей и богаче.',image='img/bg/city/cathedral_restored.jpg')

    $ game.history_mod.append(game.history)
    $ game.lair.treasury.receive_treasures(trs)
    $ game.dragon.reputation.points += 5
    '[game.dragon.reputation.gain_description]'    
    return

label lb_city_cathedral_ruined:
    hide bg
    show expression 'img/bg/city/cathedral_ruined.jpg' as bg
    'Жалкие людишки ещё не отстроили место своего примитивного культа. Тут лишь пыль и запустение. Ничего интересного.'
#    python:
#        for i in xrange(len(game.history_mod)):          
#          narrator(game.history_mod[i].historical_name)
    return


label lb_city_jewler:
    'В этом богатом квартале работают самые искустные ремесленники - оружейники, ювелиры и краснодеревщики. Кругом стоит одуряющий запах сокровищ и благородных женщин, вышедших за покупками. К сожалению, стражи тут тоже много - стоят на каждом углу.'
    $ game.foe = Enemy('city_guard', game_ref=game)
    $ chances = show_chances(game.foe)
    nvl clear
    menu:
        'Купить драгоценности':
            $ new_item = game.lair.treasury.craft(**data.craft_options['jeweler_buy'])
            if new_item:
                $ game.lair.treasury.receive_treasures([new_item])
                $ test_description = new_item.description()
                "Куплено: [test_description]."
            call lb_city_jewler from _call_lb_city_jewler_1
        'Продать драгоценности':
            menu:
                'Самую дорогую' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = game.lair.treasury.most_expensive_jewelry_index
                'Самую дешёвую' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = game.lair.treasury.cheapest_jewelry_index
                'Случайную' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = random.randint(0, len(game.lair.treasury.jewelry) - 1)
                'Продать все украшения' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = None
                'Отмена':
                    call lb_city_jewler from _call_lb_city_jewler_2
            python:
                if (item_index is None):
                    description = u"Продать все украшения за %s?" % (
                        treasures.number_conjugation_rus(game.lair.treasury.all_jewelries, u"фартинг"))
                else:
                    description = u"%s.\nПродать украшение за %s?" % (
                        game.lair.treasury.jewelry[item_index].description().capitalize(),
                        treasures.number_conjugation_rus(game.lair.treasury.jewelry[item_index].cost, u"фартинг"))
            menu:
                "[description]"
                'Продать':
                    python:
                        if (item_index is None):
                            description = u"Все украшения проданы за %s?" % (
                                treasures.number_conjugation_rus(game.lair.treasury.all_jewelries, u"фартинг"))
                            game.lair.treasury.money += game.lair.treasury.all_jewelries
                            game.lair.treasury.jewelry = []
                        else:
                            description = u"%s.\nПродано за %s" % (
                                game.lair.treasury.jewelry[item_index].description().capitalize(),
                                treasures.number_conjugation_rus(game.lair.treasury.jewelry[item_index].cost, u"фартинг"))
                            game.lair.treasury.money += game.lair.treasury.jewelry[item_index].cost
                            game.lair.treasury.jewelry.pop(item_index)

                    call lb_city_jewler from _call_lb_city_jewler_3
                'Оставить':
                    call lb_city_jewler from _call_lb_city_jewler_4
        'Драгоценности на заказ':
            $ new_item = game.lair.treasury.craft(**data.craft_options['jeweler_craft'])
            if new_item:
                $ game.lair.treasury.receive_treasures([new_item])
                $ test_description = new_item.description()
                "Изготовлено: [test_description]."
            call lb_city_jewler from _call_lb_city_jewler_5
        'Принять истинный облик':
            call lb_city_jew_atk from _call_lb_city_jew_atk_1
        'Вернуться на площадь':
            call lb_city_walk from _call_lb_city_walk_5
    return


label lb_city_jew_atk:
    $ game.dragon.drain_energy()
    $ game.foe = Enemy('city_guard', game_ref=game)
    call lb_fight from _call_lb_fight_1
    'В ближайшей округе не осталось ни одного живого стражника. Кругом царит паника, люди бегут прочь от дракона, спасая самое ценное. [game.dragon.name] оглядывает сцену разрушения и хаоса. Толстый ювелир тащит тяжелую деревянную шкатулку с драгоценностями. Благородная девица с визгом убегает прочь. В подвале горящего дома, который вот-вот обрушится, лежат без присмотра драгоценные слитки и камни.'
    $ game.dragon.reputation.points += 3
    '[game.dragon.reputation.gain_description]'
    menu:
        'Схватить ювелира':
            python:
                count = random.randint(3, 10)
                alignment = 'human'
                min_cost = 10
                max_cost = 500
                obtained = "Это предмет из лавки ювелира."
                trs = treasures.gen_treas(count, data.loot['jeweler'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
            'Ограбить неуклюжего ювелира - всё равно что отнять конфетку у ребёнка. В шкатулке много интересного:'
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]' 
    
        'Догнать благородную девицу':
#            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl('princess')
            $ text = u'%s, девица благородных кровей, решила прикупить украшений в ювелирной лавке. А попала аккурат в лапы дракона. \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            'Дракон ловит благородную девицу'
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_2     
            return
            
        'Спасти сокровища из горящего дома':
            python:
                count = random.randint(3, 10)
                alignment = 'human'
                min_cost = 10
                max_cost = 1000
                obtained = "Это предмет из лавки ювелира."
                trs = treasures.gen_treas(count, data.loot['raw_material'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
            'Действовать надо быстро, пока горящий дом не обрушился и не похоронил под своими обломками ценности:'
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]' 
    
    return

label lb_city_brothel_question:
    python: #делаем аватарку старухи  для диалогового окна
        crone= Talker(game_ref=game)
        crone.avatar = "img/avahuman/crone.jpg"
        crone.name = 'Старая карга'   
    nvl clear
    '[game.dragon.name] припоминает, что у людей есть такие специальные дома, в которых можно получить порцию секса. У людей вообще всё как-то не по-драконьи: если тебе хочется разрядки, зачем куда-то идти? Почему бы не завалить первую попавшуюся самочку прямо на улице? \n Но всё же... Вряд ли удастся найти там девственницу, ну а вдруг? '
    '[game.dragon.name] подходит к первому попавшемуся собеседнику: бабушке, которая ковыляет, с трудом опираясь на клюку.'
    game.dragon "Вы не подскажите, как пройти в бордель?"
    crone "В три часа дня?!!"
    if game.witch_st1==3:
      crone "Ну что за короли нынче пошли, теперь и по борделям шастают! Вот в моё время... кхм, кхм..."
    else:
      crone "Ну что за молодёжь нынче пошла! Вот в моё время... кхм, кхм..."
    'Старуха осекается и на несколько секунд погружается в воспоминания.'
    crone "В общем, так. Пройди по Абрикосовой, сверни на Виноградную, потом пятый поворот налево, третий поворот направо."
    game.dragon "Ага."
    crone "Потом опять седьмой поврот налево, четвёртый поворот направо."
    game.dragon "Ага..."
    'Теперь, когда [game.dragon.name] знает точное местонахождение борделя, ничто не мешает ему посетить это заведение!'
    $ game.history = historical( name='brothel_known',end_year=None,desc=None,image=None)
    $ game.history_mod.append(game.history)
    call lb_city_walk from _call_lb_city_walk_6
    return

label lb_city_brothel:
    python:
        brothel_robbed = game.historical_check('brothel_robbed')
    hide bg
    show expression 'img/bg/city/brothel_outside.jpg' as bg
    'Дракону повезло: судя по запаху, в этом красном здании есть как минимум одна девственница'
    menu:
        'Войти в бордель' if not brothel_robbed:
            call lb_city_brothel_inside from _call_lb_city_brothel_inside
        'Войти в бордель' if brothel_robbed:
            call lb_city_brothel_robbed from _call_lb_city_brothel_robbed
        'Принять истинный облик и атаковать':
            call lb_city_brothel_atk from _call_lb_city_brothel_atk        
        'Уйти':
            call lb_city_walk from _call_lb_city_walk_7
    return

label lb_city_brothel_ruined:
    hide bg
    show expression 'img/bg/city/brothel_ruined.jpg' as bg
    'Когда-то здесь стоял бордель, но теперь о его существовании напоминает лишь обгорелый остов.'
    call lb_city_walk from _call_lb_city_walk_8
    return

label lb_city_brothel_inside:
    python: #делаем аватарку хозяйки борделя для диалогового окна
        maman= Talker(game_ref=game)
        maman.avatar = "img/avahuman/maman.jpg"
        maman.name = 'Бордель-маман' 
    hide bg
    show expression 'img/bg/city/brothel_inside.jpg' as bg
    'По уютному залу туда-сюда снуют красивые полуголые девицы. Правда, попользованный материал не представляет для дракона ни малейшего интереса. Наконец, навстречу замаскированному ящеру выходит невероятно толстая женщина.'
    if game.witch_st1==3:
      maman "О, Ваше Величество, какая честь, какая честь!"
      maman 'Только сегодня и только для вас - прекрасная дева альвов, невинная, как бутон персика и распутная, как мартовская кошка!'
      game.dragon 'Эээ...'
      maman 'Ну что вы, что вы, о деньгах и речи быть не может! Просто подпишите здесь, здесь и ещё вот здесь.'
      menu:
          'Давайте перо!':
              nvl clear
              hide bg
              show expression 'img/scene/elf.jpg' as bg
              'Бордель-маман провела замаскированного дракона во внутренний дворик'
              'Там и в самом деле лежала альва. Невинная, прекрасная, обнажённая'
              'И темнокожая'
              python: #делаем аватарку хозяйки борделя для диалогового окна
                  elf= Talker(game_ref=game)
                  elf.avatar = "img/avahuman/elf.jpg"
                  elf.name = 'Темнокожая альва' 
              elf 'Король? Фи, как пошло! Я надеялась подарить свою первую любовь кому-то... особенному.'
              menu:
                  'Придётся обходиться тем, кто есть!' if game.dragon.lust > 0:
                      $ game.dragon.drain_energy()
                      '[game.dragon.fullname] старался изо всех сил, но его похоть в человеческом теле была весьма ограничена. Кажется, ему не удалось произвести впечатления на ледяную красавицу'
                      $ game.dragon.lust -=1
                      elf 'Фи. Слабак'
                      elf 'Жаль, что Тёмную Госпожу разгромили - с удовольствием отдала бы девственность кому-то из её отродий.'
                      '[game.dragon.name] стремглав вылетел из борделя. Кажется, никогда впредь драконий род больше так не унижали.'
                      $ game.dragon.bloodiness = 5
                  'Принять истинный облик':
                      game.dragon 'Тогда ты его нашла!'
                      elf 'О да...'
                      maman 'О нет!'
                      maman 'Все мои преференции... Все договоры... Всё впустую!'
                      'Бодель-маман приходит в ярость и без оглядки бросается на дракона!'
                      $ game.dragon.drain_energy()
                      $ game.history = historical( name='brothel_robbed',end_year=game.year+2,desc='Говорят, что хозяйка столичного борделя наконец-то успокоилась и больше не кидается со Скалкой Возмездия на каждого встречного',image='img/bg/city/brothel_robbed.jpg')
                      $ game.history_mod.append(game.history)
                      $ game.foe = Enemy('brothel_maman', game_ref=game)
                      call lb_fight from _call_lb_fight_90
                      python:
                          for i in xrange(len(game.history_mod)):
                            if game.history_mod[i].historical_name == 'brothel_robbed':
                               del game.history_mod[i]
                            break
                      $ game.history = historical( name='brothel_ruined',end_year=game.year+3,desc='Бордель в Столице Королевства   вновь открывает свои двери для всех желающих.',image='img/bg/city/brothel_restored.jpg')
                      $ game.history_mod.append(game.history)
                      'После победы над бордель-маман темнокожая альва прыгает от радости.'
                      elf 'Мой рыцарь... Мой дракон... Возьми меня скорее!'
                      $ description = game.girls_list.new_girl(girl_type='elf',girl_nature='lust',girl_hair='blond')
                      $ game.girl.willing=True # Добровольно согласна на секс с драконом
                      $ text = u'%s, прекрасная альва из народа Дану, выросла большой оригиналкой. Она хотела отдать свою невинность кому-нибудь особенному и устроилась на работу в столичный бордель. Что же, ей повезло - её первым мужчиной стал настоящий дракон! \n\n' % game.girl.name
                      $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
                      game.girl.third "[description]"
                      call lb_nature_sex from _call_lb_nature_sex_56  
          'Прошу прощения, вы обознались' if game.dragon.bloodiness < 5:
              maman 'Конечно-конечно, как скажете, Ваше Величество!'
              $ game.dragon.gain_rage()
              call lb_city_walk from _call_lb_city_walk_13
    else:
      maman "Чем могу служить столь представительному господину?"
      'При виде столь могучего тела дракону почему-то становится неуютно.'
      game.dragon "Эээ... Мне нужна девственница. Да. Девушка. Невинная. Вот."  
      maman "О, мсье знает толк в красивой жизни! К счастью, мы можем удовлетворить даже столь взыскательный вкус. Пятьдесят фартингов - и ваш вечер будет незабываемым."
      game.dragon "А если я захочу купить её навсегда?"
      'Похоже, вопрос приводит толстуху в экстаз. Она вот-вот забьётся в оргазме.'
      maman "О, тогда вы пришли туда, куда нужно! Двести фартингов - и никаких вопросов. Она ваша до самого нутра! Можете, хо-хо, хоть дракону её отдать!"
      menu:
        'Залатить 50 фартингов за ночь с девственницей' if 50 <= game.lair.treasury.money and game.dragon.lust>0:
            $ game.lair.treasury.money -= 50
            call lb_city_brothel_girl_night from _call_lb_city_brothel_girl_night
        'Залатить 200 фартингов и унести девственницу в своё логово' if 200 <= game.lair.treasury.money:
            $ game.lair.treasury.money -= 200
            call lb_city_brothel_girl_eternity from _call_lb_city_brothel_girl_eternity
        'Платить?!! Я возьму сам!':
            call lb_city_brothel_atk from _call_lb_city_brothel_atk_1
        'Попрощаться и уйти':
            call lb_city_walk from _call_lb_city_walk_9
    return

label lb_city_brothel_robbed:
    python: #делаем аватарку хозяйки борделя для диалогового окна
        maman= Talker(game_ref=game)
        maman.avatar = "img/avahuman/maman.jpg"
        maman.name = 'Бордель-маман' 
    hide bg
    show expression 'img/bg/city/brothel_inside.jpg' as bg
    'Навстречу дракону спешит знакомая бодель-маман.'
    maman "Нет."
    game.dragon "Что нет?"  
    maman "Девственниц нет. Никого нет. И вообще: драконов мы не обслуживаем."
    menu:
        'Атаковать наглую тётку':
            call lb_city_brothel_atk from _call_lb_city_brothel_atk_2
        'Уйти с проклятиями' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            call lb_city_walk from _call_lb_city_walk_10
    return

label lb_city_brothel_atk:
    $ game.dragon.drain_energy()
    $ game.foe = Enemy('brothel_maman', game_ref=game)
    call lb_fight from _call_lb_fight_70
    python:
        for i in xrange(len(game.history_mod)):
          if game.history_mod[i].historical_name == 'brothel_robbed':
            del game.history_mod[i]
            break
    'Бордель-маман повержена, и теперь некому встать на пути разъярённого дракона. [game.dragon.name] с наслаждением крушит здание и поднимается на верхний этаж, по дороге убивая визжащих девиц. Но дракона интересует одна-единственная самка - девственница, способная выносить отродье чудовища.'
    $ game.dragon.reputation.points += 3
    '[game.dragon.reputation.gain_description]'
    $ game.history = historical( name='brothel_ruined',end_year=game.year+3,desc='Бордель в Столице Королевства вновь открывает свои двери для всех желающих.',image='img/bg/city/brothel_restored.jpg')
    $ game.history_mod.append(game.history)
    hide bg
    show expression 'img/bg/city/brothel_girl.jpg' as bg
    nvl clear
    $ chance = random.choice(['peasant', 'peasant', 'peasant', 'peasant','citizen'])
    $ description = game.girls_list.new_girl(chance)
    $ text = u'%s не понаслышке знает, что такое превратности судьбы. Её отец, разорившись, поправил своё материальное благополучие, продав дочь в бордель: девственность нынче стоит дорого. Девушка, замирая от ужаса, ждала своего первого клиента. А дождалась дракона. \n\n' % game.girl.name
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    '[game.dragon.name] находит нетронутый бутон в этом царстве порока.'
    nvl clear
    game.girl.third "[description]"
    call lb_nature_sex from _call_lb_nature_sex_25  

    return   

label lb_city_brothel_girl_night:
    $ game.dragon.drain_energy()
    hide bg
    show expression 'img/bg/city/brothel_girl.jpg' as bg
    nvl clear
    'Девушка, лежащая на кровати, внимательно смотрит на вас'
    $ chance = random.choice(['peasant', 'peasant', 'peasant', 'peasant','citizen','citizen','princess'])
    $ description = game.girls_list.new_girl(chance,tres=False)
    python:
        if game.girl.nature == 'innocent':
          cry = u'Пожалуйста, заберите меня отсюда! Я... я не могу заниматься ЭТИМ, мне стыдно!!!'
        elif game.girl.nature == 'proud':
          cry = u'Ты получишь моё тело, но не душу!'
        elif game.girl.nature == 'lust':
          cry = u'Ну наконец-то! Позабавимся?'
    game.girl.third "[cry]"  
    menu:
        'Принять истинный облик, чтобы оплодотворить девушку':
            '[game.dragon.name] принимает истинный облик'
            $ text = u'%s не понаслышке знает, что такое превратности судьбы. Её отец, разорившись, поправил своё материальное благополучие, продав дочь в бордель: девственность нынче стоит дорого. Девушка, замирая от ужаса, ждала своего первого клиента. Ну кто мог предположить, что вошедший в комнату мужчина обернётся драконом, а хозяйка борделя не станет возражать против такого рода соития?! \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            game.girl "ААА!!!"
            maman "Что происходит?"
            game.girl "Д-д-дракон!!!"
            maman "Ну дракон, ну и что? Разве это повод отлынивать от своих профессиональных обязанностей?"
            game.girl "Но это же дракон!"
            maman "Милочка, чтобы больше я этих глупостей не слышала! Кроме того, подумай о будущем. Потеря невинности с драконом - это коронный пункт в твоём будущем резюме!"
            game.dragon "Я могу продолжать?"
            maman "Конечно-конечно, не смею вам больше мешать!"
            # Сам секс. 
            $ text = u' Начинающую проститутку ждало тяжёлое испытание: %s грубо сношал её всю ночь, пока не убедился, что она понесла его отродье. \n С другой стороны, она хотя бы не попала в драконье логово! \n\n' % game.dragon.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            $ description = game.girls_list.impregnate()
            stop music fadeout 1.0            
            game.girl "[description]"
            show expression sex_imgs(game.girl.sex_expression) as xxx
            play sound get_random_file("sound/sex")
            pause (500.0)
            stop sound fadeout 1.0
            hide xxx
            python:
                game.girls_list.save_whore() 
        'Принять истинный облик и унести девушку с собой':
            '[game.dragon.name] решил сэкономить деньги и унести девушку с собой.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            $ text = u'%s не понаслышке знает, что такое превратности судьбы. Её отец, разорившись, поправил своё материальное благополучие, продав дочь в бордель: девственность нынче стоит дорого. Девушка, замирая от ужаса, ждала своего первого клиента. Ну кто мог предположить, что вошедший в комнату мужчина обернётся драконом?! \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            $ game.history = historical( name='brothel_robbed',end_year=game.year+2,desc='Говорят, что хозяйка столичного борделя наконец-то успокоилась и больше не кидается со Скалкой Возмездия на каждого встречного',image='img/bg/city/brothel_robbed.jpg')
            $ game.history_mod.append(game.history)
            call lb_nature_sex from _call_lb_nature_sex_26
    return

label lb_city_brothel_girl_eternity:
    $ game.dragon.drain_energy()
    hide bg
    show expression 'img/bg/city/brothel_girl.jpg' as bg
    nvl clear
    'Девушка, лежащая на кровати, внимательно смотрит на вас'
    $ chance = random.choice(['peasant', 'peasant', 'peasant', 'peasant','peasant', 'peasant', 'peasant', 'peasant','citizen','citizen','citizen','citizen','princess','princess','elf'])
    $ description = game.girls_list.new_girl(girl_type=chance,girl_nature='lust',tres=False)  # Вызываем девушку с характером
    $ game.girl.willing=True # Добровольно согласна на секс с драконом
    $ text = u'%s считала, что её жизнь проходит пресно и скучно. Мечтая об умопомрачительных сексуальных приключениях, она решила устроиться в бордель. Возмущение родственников было погашено звоном момент. Ожидая своего первого клиента, девушка мечтала о чём-то необычном, грубом, страшном. Что же, её мечта сбылась! \n\n' % game.girl.name
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    game.girl "Ну наконец-то! Жду не дождусь того момента, когда я потеряю свою девственность! Надеюсь, ты достаточно выносливый любовник, ммм?"
    '[game.dragon.name] принимает свой истинный облик'
    game.dragon "Кстати, я тебя купил и теперь могу делать с тобой всё, что захочу."
    '[game.girl.name] со счастливым визгом бросается на шею ящера.'
    game.girl "Я согласна-согласна-согласна!!! Давай же, покажи мне истинный драконий размер!"
    nvl clear
    game.girl "[description]"
    call lb_nature_sex from _call_lb_nature_sex_27
    return

label lb_pregnant_whore:
    nvl clear
#    hide bg
    show expression 'img/bg/city/brothel_inside.jpg' as bg
    game.girl "Что мне делать? Я беременна! От дракона!!!"
    maman "Милочка, ну что ты переживаешь? Родишь монстрика, мы его на свободу отпустим, и всё закончится в лучшем виде! Никто ничего и не узнает."
    game.girl "Но я же не смогу родить ЭТО! Я погибну!!!"
    maman "Глупости. Каких только родов я в своей жизни не принимала! Уверяю: яйцо выскочит из тебя, как пробка из бутылки."
    $ text = u'Скрыть беременность в борделе едва ли возможно. Но маман отнеслась к произошедшему как к мелкой неприятности и полностью прикрыла свою работницу. \n\n ' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_willing_help:
    nvl clear
#    hide bg
    $ place = 'plain'
    show expression get_place_bg(place) as bg
    $ text = "Своей магией дракон спас девушку, которая отдалась ему добровольно (-1 энергии)\n"
    game.girl "[text]"
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_willing_help_prison:
    nvl clear
#    hide bg
    $ place = 'prison'
    show expression get_place_bg(place) as bg
    game.girl "Своей магией дракон спас девушку, которая отдалась ему добровольно (-1 энергии)\n"
    return    

    