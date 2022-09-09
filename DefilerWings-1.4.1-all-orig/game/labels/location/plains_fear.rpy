# coding=utf-8
init python:
    from pythoncode.characters import Enemy, Talker
    from pythoncode.utils import weighted_random

label lb_fear_plains:
    nvl clear
    "Чуткий слух дракона доносит до него странные звуки. Кажется, у стен ближайшего городка творится что-то занятное. Опять ополченцы тренируются, что ли?"


    
    hide bg
    show expression 'img/scene/fear/plains/prepare.jpg' as bg
    nvl clear
    stop music fadeout 1.0
    $ renpy.music.play(get_random_files('mus/darkness')) 
    "А, нет, это какую-то девушку сжигать собрались. [game.dragon.name] принюхивается: невинная! Растрата ценного материала, однако!"
    "Толпа с интересом наблюдает за представлением. Со всех сторон доносятся крики: 'Ведьма!', 'Сжечь тварь!' 'Поджарить гадину!', 'Это она дракона на нас навлекла!!!'"
    "Обвинять жертву во злодеяних злодея? Нет, [game.dragon.name] никогда не поймёт людей!"
    menu:
        'Наблюдать издалека':
            $ game.dragon.drain_energy()
            game.dragon 'А, это всего лишь крестьянка. Невелика потеря. Лучше понаблюдаю за процессом!'
            nvl clear
            hide bg
            show expression 'img/scene/fear/plains/burning.jpg' as bg
            'Палач подносит факел к связке дров, и костёр охватывает весёлое пламя.'
            'Огонь начинает требовательно ласкать тело девушки. Он - очень суровый любовник. Жертва корчится от боли и отчаянно кричит, кричит, пытаясь выплеснуть переполняющую её муку. Но ей не дано разжать объятия пламени.'
            'Зрители взбудоражены, они с колоссальным интересом наблюдают за казнью. Дракон возбуждённо принюхивается: славный вышел шашлычок!'
            'Живой факел издаёт последний, отчаянный вопль, в котором уже не осталось ничего человеческого. '
            'Когда зрители разошлись, [game.dragon.name] подошёл поближе и попробовал экзотическое блюдо. Славный деликатес, надо будет иногда так лакомиться!'
            stop music fadeout 3.0
        'Кто смеет жарить МОЁ мясо?!!':
            $ game.dragon.drain_energy()
            game.dragon 'Ну кто так жарит, а, кто так жарит?! Они же весь вкус испортят!!!'
            'Одержимый праведным гневом, [game.dragon.name] врывается в толпу зевак.'
            $ game.foe = Enemy('mob', game_ref=game)
            call lb_fight from _call_lb_fight_76
            hide bg
            nvl clear
            show expression 'img/scene/fear/plains/talk.jpg' as bg
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            'А теперь пора заняться законной добычей!'
            $ description = game.girls_list.new_girl(girl_type='peasant',girl_nature='innocent',girl_hair='red',tres=False)
            $ text = u'%s, простая крестьянка, с детства стремилась помогать людям и отличалась тихим и кротким нравом. %s стала местной  знахаркой и лечила своих земляков, но те редко платили ей благодарностью. Когда её сестра попала в замок маркиза де Ада, а бесчинства дракона грозили уничтожить привычный уклад жизни, жители городка назвали девушку ведьмой, обвинили во всех грехах и решили сжечь живьём. Вот только у дракона были иные планы! \n\n' % (game.girl.name,game.girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            'Очаровательная рыжая девица, с едва ощутимым магическим даром. Не весть что, но с такой приятно и помиловаться, и позавтракать.'    
            $ game.history = historical(name='de_Ad',end_year=game.year+2,desc='По Королевству опять ползут зловещие слухи о замке маркиза де Ада.',image='img/scene/fear/plains/castle_dark.jpg')
            $ game.history_mod.append(game.history)
            if game.fear<7:
              '[game.girl.name] попыталась что-то сказать, но [game.dragon.name] не стал слушать пустую болтоню.'
              stop music fadeout 5.0
              call lb_nature_sex from _call_lb_nature_sex_36
            else:
              game.girl 'Спасибо за спасение, вы очень доброе и благородное существо. Молю вас, спасите мою сестру!'
              
              menu:
                'Продемонстрировать своё "благородство"':
                    game.dragon 'Ещё никогда и никто меня так не оскорблял!!! Сейчас я покажу тебе "благородство", лгунья!'
                    stop music fadeout 5.0
                    call lb_nature_sex from _call_lb_nature_sex_37
                'Чего-чего?!':
                    call lb_fear_plains_talk from _call_lb_fear_plains_talk
        'Пусть сжигают, тут только время потеряю' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            stop music fadeout 5.0
            return
    return

label lb_fear_plains_talk: # Разговор с ведьмой
    '[game.dragon.name] недоумённо оглядывает себя. Нет, с утра ничего не изменилось: всё то же кровожадное похотливое безжалостное чудовище. Где она благородство-то нашла?'
    game.girl 'Пару месяцев назад её взял в жёны маркиз де Ад, а после началось ужасное! Маркиз практически открыто забирает девственниц со всех окрестных поселений, пытает их и убивает!'
    game.dragon.third 'Может, стоит посетить столь достойного человека, обменяться опытом? Не, лениво.'
    game.girl 'Когда жители города узнали о судьбе моей сестры, они обезумили от ярости и решили сжечь меня. Молю, помогите мне!!!'
    'В общем, обычные женские глупости. Пора прекращать этот балаган.'
    game.girl 'Говорят, совсем недавно маркиз зашёл настолько далеко, что привёз в замок альву!'
    'Альву?! Это же полностью меняет дело!!!'
    game.dragon 'Альву, говоришь? Девственницу?'
    game.girl 'Да-да! Я была уверена, что в глубине души вы добры и благородны, и не пройдёте мимо страданий  невинных.'
    if game.dragon.health < 2:
      game.girl 'Ты ранен. Я простая знахарка и не владею магией, но кое-что могу. Выпей это зелье.'
      '[game.dragon.name] с недоумением разглядывает маленький красный флакончик. На первый взгляд, неядовито. Стоит попробовать!'
      $ game.dragon.health = 2
      game.dragon.third 'Раны затянулись. Ну надо же!'
    game.dragon 'И маркизу де Аду всё это сходит с рук? А то знаю: стоит немного побезобразничать, как герои мигом слетаются к твоему логову!'
    '[game.girl.name] тяжело вздыхает.'
    game.girl 'Маркиз оправдывает свои поступки защитой от дракона'
    game.dragon.third 'Действительно, в окрестных землях деткам приходится туго.'
    game.dragon 'А откуда ты знаешь, что твоя сестра жива?'
    game.girl 'Я... чувствую. Но не знаю, что с ней. Мне страшно это представить. Обычно после недели пребывания в замке прекрасные и здоровые девушки превращаются в истерзанные, обезображенные трупы. '
    game.girl 'Охрана замка очень сильна, но я знаю тайный проход, ведущий в подземемные темницы. Правда, его сторожит горгулья, и мне никак не удавалось проскользнуть мимо неё.'
    game.dragon 'Ясно. Выбор прост.'
    $ text = u'Впрочем, планы дракона оказались нарушены, когда %s упомянула про альву, томящуюся в соседнем замке. Вообще-то, девица жаждала спасти свою сестру, но кого интересуют деревенские простушки? Подумав, %s решил, что ' % (game.girl.name, game.dragon.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    menu:
        'Лучше крестьянка в руках, чем альва в замке.':
            game.dragon 'Искать мифическую альву? Рисковать жизнью? Зачем, если я уже нашёл сегодняшнюю жертву!'
            $ text = u'лучше крестьянка в лапах, чем альва в замке.\n\n'
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            stop music fadeout 5.0
            call lb_nature_sex from _call_lb_nature_sex_38
        'Спрячь за высокой стеною альвийку - выкраду вместе с стеною!':
            game.dragon 'Никакие стены меня не остановят!'
            game.girl 'Нет! Это слишком опасно! Во время штурма маркиз может успеть убить пленниц, и...'
            game.dragon 'Молчи, женщина! А лучше покажи, где тут замок.'
            $ text = u'штурм замка в лоб - именно то, что нужно в этой ситуации!\n\n %s исчезла во время штурма. Её дальнейшая судьба неизвестна.' % (game.girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            $ game.chronik.live('deAd_talk','img/scene/fear/plains/talk.jpg')
            $ game.foe = Enemy('castle_guard', game_ref=game)
            call lb_fight from _call_lb_fight_77
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            'Замок маркиза де Ада теперь беззащитен'
            $ game.dragon.reputation.points += 10
            '[game.dragon.reputation.gain_description]'                
            nvl clear
            python:
                count = random.randint(3, 8)
                alignment = 'knight'
                min_cost = 100
                max_cost = 1000
                obtained = "Это предмет из разграбленной крепости маркиза де Ада."
                trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
            
            $ txt = game.interpolate(random.choice(txt_place_castle[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            hide bg
            show expression 'img/scene/fear/plains/dungeon.jpg' as bg
            '[game.dragon.fullname] с огромным интересом исследовал подземелья замка. Жаль, что маркиз де Ад погиб при штурме - выдающийся был человек, многому мог научить!'
            'Правда, большинство пленниц было "не первой свежести", попользованные, изувеченные, они только в пищу и годились. Но острый нюх вёл дракона вглубь подземелий...'
            nvl clear
            hide bg
            show expression 'img/scene/fear/plains/elf_captured.jpg' as bg
            '... и вскоре он обнаружил главный приз!'
            'Альва была измождённой, плотно зафиксированной и всё равно прекрасной. Она явно провела в этой позе много часов, вися на вывернутых руках, едва касаясь носочками пола и упираясь животом и бёдрами в деревяшку с острыми шипами. Из насильно приоткрытого рта тянулась ниточка слюны, некогда белоснежная кожа была украшена синяками, царапинами и кровоподтёками.'
            'Но самое главное - она всё ещё оставалась невинной.'
            game.dragon 'Моя прелесссть...'
            call lb_fear_plains_elf from _call_lb_fear_plains_elf_1
        'Тайный проход? Что же, это, по крайней мере, интересно!':
            game.dragon 'Тайный проход в мрачное подземелье? Ни разу не бывал в таких местах! Тут далеко?'
            game.girl 'Нет, не очень. Идём.'
            $ text = u'скрытность - именно то, что нужно в этой ситуации.\n\n '
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            hide bg
            show expression 'img/scene/fear/plains/castle.jpg' as bg
            game.dragon.third 'Укреплённое местечко. Штурмовать такое - замучаешься.'
            game.dragon 'Так, а эта горгулья - из моих отпрысков? Не из моих? Жаль, жаль...'
            $ game.foe = Enemy('gargoyle', game_ref=game)
            $ chances = show_chances(game.foe)
            '[chances]'
            menu:
                'Сейчас я этот камень пообломаю!':
                    call lb_fight from _call_lb_fight_78
                    call lb_fear_plains_pass from _call_lb_fear_plains_pass
                'Да ну её! Довольствуюсь меньшей наградой.':
                    call lb_fear_plains_retreat from _call_lb_fear_plains_retreat_1
            
    return

label lb_fear_plains_retreat:    # Дракон отступает от горгульи
    hide bg
    show expression 'img/scene/fear/plains/talk.jpg' as bg
    game.dragon 'А знаешь что? Я передумал. Ты, конечно, не альва, но кое на что тоже сгодишься!'
    $ text = u'Правда, горгулья, охранявшая этот проход, вынудила дракона отказаться от столь заманчивой идеи, и %s оказалась в плену у ящера.\n\n ' %(game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    stop music fadeout 5.0
    call lb_nature_sex from _call_lb_nature_sex_40
    return

label lb_fear_plains_pass:
    hide bg
    show expression 'img/scene/fear/plains/pass.jpg' as bg
    if game.dragon.health < 2:
      game.girl 'Твоя смелость восхищает, но сражаться с такими врагами непросто. Возьми  целебное зелье.'
      '[game.dragon.name] откупоривает  маленький красный флакончик.'
      $ game.dragon.health = 2
      game.dragon.third 'Раны затянулись. Как она это делает?'
    'Горгулья повержена, и теперь ничто не преграждает путь сквозь заброшенное подземелье.'
    if game.dragon.mana>0:
      game.dragon 'Как же я туда пролезу? Магия есть, но её же тратить жалко!'
    else:
      game.dragon 'Как же я туда пролезу? Ведь я же не  владею магией!'
    game.girl 'Ничего страшного. Выпей это зелье, и превратишься в человека!'
    'Пройдя сквозь извилистый подземный ход, дракон и девица проникли в темницы замка маркиза де Ада'
    game.dragon 'Иди ищи свою сестру, а я пока займусь альвой'
    game.girl 'Хорошо, [game.dragon.name]'
    if game.fear<11:
      call lb_fear_plains_memory from _call_lb_fear_plains_memory_1
    else:
      $ game.rape.kind_girl=game.girl 
#      $ game.rape.game.rape.kind_girl=game.girl 
    'Пробираясь по тёмным коридорам, [game.dragon.fullname] больше полагается на обоняние, чем на зрение. Усилия приносят плоды: в душном смраде вони дракон ощущает сладкую нотку невинной плоти.'
    'Альва, дитя богини Дану: этот аромат ни с чем не перепутать.'
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/elf_bdsm.jpg' as bg
    '[game.dragon.name] восхитился при виде открывшегося зрелища'
    'Специальная конструкция вынуждала альву стоять на кончиках пальцев, мучительно выгибая спину. Затычка, вставленная в задний проход, не давала ей сделать ни единого движения. Хм, может, подкрутить ворот ещё немного?'
    if game.fear<11:
      '[game.dragon.name] принимает своё истинное обличье и, не обращая внимания на мольбы альвы, уносит её в своё логово.'
      call lb_fear_plains_elf from _call_lb_fear_plains_elf_2
    else:
      'Едва дракон заходит в комнату, как пленница истошно кричит: "[game.dragon.fullname], в этом замке разрабатывают биологическое оружие специально против драконов!" '
      menu:
          'Чушь. Этого не может быть, потому что не может быть никогда!':
              game.dragon.third 'Биологическое оружие? Против драконов? Это противоречит основам нашей физиологии! Не буду обрашать внимания на эту чушь.'
              call lb_fear_plains_memory from _call_lb_fear_plains_memory_2
              '[game.dragon.name] принимает своё истинное обличье и, не обращая внимания на мольбы альвы, уносит её в своё логово.'
              call lb_fear_plains_elf from _call_lb_fear_plains_elf_3
          'Откуда она знает моё имя?!':
              python:
                text = u'%s и %s пробрались в подземелья замка маркиза де Ада и расстались. Девушка отправилась искать сестру.\n\n ' %(game.girl.name, game.dragon.fullname)
                game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
              game.dragon.third 'Биологическое оружие? Против драконов? Это противоречит основам нашей физиологии! Стоп, откуда она знает моё имя? И что я вообще - дракон, ведь я же сейчас в облике человека!'
              $ description = game.girls_list.new_girl(girl_type='elf',girl_nature='lust',girl_hair='blond',tres=False)
              $ text = u'%s была найдена драконом в подземельях замка маркиза де Ада. Пленница предупредила ящера о разработке биологического оружия, способного смести с лица земли всё живое: и людей, и драконов. %s отнёсся к этому скептически, но решил всё же разобраться в происходящем. ' % (game.girl.name,game.dragon.name)
              $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
              call lb_fear_plains_alliance from _call_lb_fear_plains_alliance
    return

label lb_fear_plains_elf:
    $ description = game.girls_list.new_girl(girl_type='elf',girl_nature='lust',tres=False)
    $ text = u'%s была найдена драконом в подземельях замка маркиза де Ада. Пленница оказалась измученной, но живой и даже невинной. %s быстро нашёл ей лучшее применение. Каким образом сия девица попала в беду - так и осталось неизвестным.\n\n' % (game.girl.name,game.dragon.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    stop music fadeout 5.0
    game.girl.third "[description]"
    call lb_nature_sex from _call_lb_nature_sex_39
    return

label lb_fear_plains_memory:  # Запоминаем крестьянку
    python:
      text = u'%s и %s пробрались в подземелья замка маркиза де Ада и расстались. Девушка отправилась искать сестру. Её дальнейшая судьба неизвестна, но, вероятно, печальна.\n\n ' %(game.girl.name, game.dragon.fullname)
      game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
      game.chronik.live('deAd_pass','img/scene/fear/plains/pass.jpg')   
    return

label lb_fear_plains_alliance:  # Альянс с эльфийкой
    game.dragon 'Откуда ты знаешь моё имя?'
    game.girl 'Маркиз де Ад многому меня научил. Некоторе время я работала в его команде, но потом наши пути разошлись, и я попала в подземелье.'
    game.dragon 'А он откуда знает?'
    game.girl 'Де Ад отлично разбирается в биологии драконов. Он и его подручные с помощью тёмного колдовства и человеческих жертвоприношений создают боевой вирус PAX-12, способный убивать порождений Тёмной Госпожи. '
    game.dragon 'Ерунда. На нас не действуют боевые вирусы.'
    game.girl 'Это так, но де Ад с подручными зашли слишком далеко! Созданный ими штамм мутировал и вышел из-под контроля. Теперь он косит людей, как траву, и грозит всей человеческой популяции. [game.dragon.fullname], я понимаю, тебе нет дела до этих жалких обезьянок. Но если в мире не останется людей, тебе некого будет пытать и мучить!'
    game.dragon 'Созданный да Адом вирус действительно настолько опасен? Он и в самом деле может уничтожить всю человеческую цивилизацию?'
    game.girl 'Да. Действительно.'
    $game.rape.elf_lie=True   # Врёт, как сивый мерин
    game.dragon.third 'На миг у дракона мелькнула мысль плюнуть на всё и покинуть этот нелепый замок с его мутными историями. Но нет, со здешними невнятными загадками требовалось разобраться - если не из страха, то из банального любопытства!'
    $game.rape.elf_girl=game.girl
    menu:
        '[game.rape.elf_girl.name] подозрительно много знает...':
            $game.rape.Alliance=False
            $ text = u'Правда, с альвой случилась нехорошая история - не доверяя возможной союзнице, дракон '
            $game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            game.dragon 'А знаешь... я тебе ну ни капельки не верю.'
            game.rape.elf_girl 'Нет! Послушай, я искренне на твоей стороне и мечтаю о победе Тёмной Госпожи...'
            menu:
                'Избавиться от подозрительной альвы':
                    game.dragon 'Надоела.'
                    $game.rape.elf_alive=False
                    $ text = u'рассёк ей живот и оставил подыхать в одиночестве.\n\n'
                    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
                    $ game.chronik.write_image('img/scene/fear/plains/elf_death.jpg',game.dragon.level,game.girl.girl_id)
                    $ game.chronik.death('deAd_elf_lie','img/scene/fear/plains/elf_death.jpg')
#                    hide bg
                    nvl clear
                    play sound get_random_file("sound/pain") 
                    show expression 'img/scene/fear/plains/elf_death.jpg' as fg with dissolve
                    '[game.dragon.fullname] одним движением рассекает внутренности альвы, оставляя её медленно подыхать в одиночестве.'
                    call lb_fear_plains_zombie from _call_lb_fear_plains_zombie_1
                'Оставить альву в покое':
                    $game.rape.elf_alive=True
                    $ text = u'оставил её в темнице.\n\n'
                    $game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
                    hide bg
                    nvl clear
                    show expression 'img/scene/fear/plains/pass.jpg' as bg
                    '[game.dragon.fullname] покидает комнату, не прислушиваясь к женским крикам.'
                    call lb_fear_plains_zombie from _call_lb_fear_plains_zombie_2
                'Выслушать альву ещё раз':
                    nvl clear
                    $game.rape.elf_alive=True
                    $ text = u'потребовал полностью правдивого рассказа - и получил его.\n\n'
                    $game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
                    $game.rape.elf_lie=False
                    game.dragon 'На сей раз - на капли лжи.'
                    game.rape.elf_girl 'На самом деле маркиз де Ад разрабатывает вирус против драконов. Я же ненавижу людей. Не-на-ви-жу!!!'
                    game.rape.elf_girl 'Именно я разработала штамм, убивающий людей и превращающий их в уродливых, бездушных монстров. Я придумала оригинальное название для этого бедствия: "зомби-апокалипсис".'
                    game.rape.elf_girl 'Весь мир он не затронет, но пару-тройку провинций - вполне. И тебе станет гораздо легче убивать и насиловать!'
                    game.dragon 'Поддерживаю и одобряю. Но что же ты сразу-то врать начала?'
                    game.rape.elf_girl.third 'Альва краснеет от стыда. Кажется, произошедшее смущает её гораздо сильнее, чем собственная нагота и та поза, в которой она находится.'
                    game.rape.elf_girl 'По привычке...'
                    game.rape.elf_girl 'Я настолько привыкла лгать де Аду, что не сразу сообразила, что тут нужна предельная честность!'
                    call lb_fear_plains_alchemist from _call_lb_fear_plains_alchemist_1
        '[game.rape.elf_girl.name] рассуждает весьма здраво...':
            call lb_fear_plains_alchemist from _call_lb_fear_plains_alchemist_2
        'Чем хуже для человечества, тем лучше для драконов!':
            game.dragon 'Или ты говоришь правду, и тогда распространение болезни можно только приветствовать, или врёшь. В любом, разговаривать нужно не с тобой, а с создателем этого вируса.'
            $game.rape.elf_alive=True
            $game.rape.Alliance=False
            $ text = u'Правда, без альвы - дракон счёл возможную союзницу бесполезной и оставил её в темнице.\n\n'
            $game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            hide bg
            nvl clear
            show expression 'img/scene/fear/plains/pass.jpg' as bg
            '[game.dragon.fullname] покидает комнату, не прислушиваясь к женским крикам.'
            call lb_fear_plains_zombie from _call_lb_fear_plains_zombie_4
    return

label lb_fear_plains_alchemist:   # Алхимия
    $game.rape.Alliance=True
    $game.rape.elf_alive=True
    if game.rape.elf_lie:
      game.dragon 'Да, если мне некого будет убивать и мучить, жизнь станет гораздо сукчнее!'
      $ text = u'Дракон освободил альву, и девушка предложила дракону создать лекарство против смертельной болезни. Но для этого требовались некоторые реагенты, которые де Ад держал при себе. Оставив альву в алхимической лаборатории, %s отправился разбираться с маркизом.\n\n' % game.dragon.fullname
    else:
      game.dragon 'Да, если Вольные отвлекутся на борьбу с зомби, жизнь станет гораздо легче!'
      $ text = u'Дракон освободил альву, и девушка предложила дракону усовершенствовать смертоносную болезнь. Но для этого требовались некоторые реагенты, которые де Ад держал при себе. Оставив альву в алхимической лаборатории, %s отправился разбираться с маркизом.\n\n' % game.dragon.fullname
    $game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/elf_alliance.jpg' as bg
    '[game.dragon.name] освобождает альву... по крайней мере, частично.'
    game.dragon 'Есть ли у тебя план, [game.rape.elf_girl.name]?'
    game.rape.elf_girl 'Разумеется, у меня есть план, [game.dragon.name]!'
    game.rape.elf_girl 'Где-то здесь должна быть алхимическая лаборатория...'
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/laboratory.jpg' as bg
    'За углом и вправду оказалась лаборатория, оборудованная по последнему слову магии.'
    if game.rape.elf_lie:
      game.rape.elf_girl 'Лекарство от этого вируса можно создать! Я знаю!'
    else:
      game.rape.elf_girl 'Вирус можно усовершенстовать! Я знаю!'
    nvl clear
    show expression 'img/scene/fear/plains/alchemist.png' as fg with Dissolve(2.0)
    pause 2.0
    '[game.rape.elf_girl.name] начинает возиться с колбами и реторами, иногда шепча какие-то заклинания.'
    'Дракон с интересом следит за её манипуляциями, контроллируя каждый шаг.'
    'Видимо, у альвы что-то не получается: с каждой минутой она нервничает всё больше и больше.'
    game.rape.elf_girl 'Проклятье! У меня нет самого важного реагента!'
    '[game.dragon.fullname] фыркает. Ему с самого начала казалось, что всё закончится именно так.'
    if game.rape.elf_lie:
      game.rape.elf_girl 'Пожалуйста, [game.dragon.name]! Ради спасения человечества... Принеси мне лектинополимер маннозы для активации системы комплемента!'
    else:
      game.rape.elf_girl 'Пожалуйста, [game.dragon.name]! Ради мести человечеству... ради спасения своего собственного вида... Принеси мне лектинополимер маннозы для активации системы комплемента!'
    game.dragon 'Лектинополимер маннозы для активации системы комплемента? Ну да, очевидное решение.'
    game.rape.elf_girl 'Он должен быть у маркиза де Ада... или, скорее, у его ассистентки!'
    'Тяжело вздохнув, [game.dragon.name] отправляется на поиски'
    call lb_fear_plains_zombie from _call_lb_fear_plains_zombie_3
    return

label lb_fear_plains_zombie:   # Встреча с зомби
    $game.rape.kind_ill=False # Больна ли девочка
    $game.rape.kind_alive=True # Жива ли девочка
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/pass.jpg' as bg
    'Из-за угла доносится подозрительный шум...'
    if not game.rape.Alliance:
      call lb_fear_plains_light_st1 from _call_lb_fear_plains_light_st1
    else:
      $game.rape.kind_ill=True
      'А, это та самая рыжая ведьмочка, [game.rape.kind_girl.name], попала в руки зомби и вот-вот погибнет!'
      'Кстати, к рождению отродий она больше не способна. Впрочем, невелика потеря.'
      call lb_fear_plains_hard_st1 from _call_lb_fear_plains_hard_st1_1
    return

label lb_fear_plains_light_st1:
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/zombie_light/light_st1.jpg' as bg
    pause 500
    'А, это та самая рыжая ведьмочка, [game.rape.kind_girl.name], вот-вот попадёт в руки зомби.'
    'В общем, ничего особенного.'
    menu:
        'Как жалкие зомби смеют стоять на МОЁМ пути?!!':
            call lb_fear_plains_zombie_fight from _call_lb_fear_plains_zombie_fight_1
        'Обойти по другому коридору':
            call lb_fear_plains_murder from _call_lb_fear_plains_murder_1
        'Интересно, что будет дальше?':
            call lb_fear_plains_light_st2 from _call_lb_fear_plains_light_st2
    return

label lb_fear_plains_light_st2:
    hide bg
    nvl clear
    play sound get_random_file("sound/pain") 
    show expression 'img/scene/fear/plains/zombie_light/light_st2.jpg' as bg
    pause 500
    'Зомби хватают [game.rape.kind_girl.name], лапают её груди, раздвигают бёдра.'
    menu:
        'Как жалкие зомби смеют стоять на МОЁМ пути?!!':
            call lb_fear_plains_zombie_fight from _call_lb_fear_plains_zombie_fight_2
        'Обойти по другому коридору':
            call lb_fear_plains_murder from _call_lb_fear_plains_murder_2
        'Интересно, что будет дальше?':
            call lb_fear_plains_light_st3 from _call_lb_fear_plains_light_st3
    return

label lb_fear_plains_light_st3:
    hide bg
    nvl clear
    play sound get_random_file("sound/pain") 
    show expression 'img/scene/fear/plains/zombie_light/light_st3.jpg' as bg
    pause 500
    '[game.rape.kind_girl.name] пытается вырваться, но тщетно. Зомби заламывают её руки и продолжают подготовку "мяса".'
    menu:
        'Как жалкие зомби смеют стоять на МОЁМ пути?!!':
            call lb_fear_plains_zombie_fight from _call_lb_fear_plains_zombie_fight_3
        'Обойти по другому коридору':
            call lb_fear_plains_murder from _call_lb_fear_plains_murder_3
        'Интересно, что будет дальше?':
            call lb_fear_plains_light_st4 from _call_lb_fear_plains_light_st4
    return

label lb_fear_plains_light_st4:
    hide bg
    nvl clear
    play sound get_random_file("sound/pain") 
    show expression 'img/scene/fear/plains/zombie_light/light_st4.jpg' as bg
    pause 500
    'Гниющие туши зомби наваливаются на нагое тело [game.rape.kind_girl.name], лапают чистую кожу, мнут груди.'
    '[game.dragon.name] негромко присвистывает: [game.rape.kind_girl.name] стала женщиной и больше не сможет выносить отродье дракона. Впрочем, невелика потеря!'
    $game.rape.kind_ill=True
    $game.rape.kind_girl.virgin=False
    menu:
        'Как жалкие зомби смеют стоять на МОЁМ пути?!!':
            call lb_fear_plains_zombie_fight from _call_lb_fear_plains_zombie_fight_4
        'Обойти по другому коридору':
            call lb_fear_plains_murder from _call_lb_fear_plains_murder_4
        'Интересно, что будет дальше?':
            call lb_fear_plains_light_st5 from _call_lb_fear_plains_light_st5
    return

label lb_fear_plains_light_st5:
    hide bg
    nvl clear
    play sound get_random_file("sound/pain") 
    show expression 'img/scene/fear/plains/zombie_light/light_st5.jpg' as bg
    pause 500
    '[game.rape.kind_girl.name] обмякла в лапах зомби. Насильники продолжают наслаждаться юным телом и мнут склизкими пальцами женское лоно.'
    menu:
        'Как жалкие зомби смеют стоять на МОЁМ пути?!!':
            call lb_fear_plains_zombie_fight from _call_lb_fear_plains_zombie_fight_5
        'Обойти по другому коридору':
            call lb_fear_plains_murder from _call_lb_fear_plains_murder_5
        'Интересно, что будет дальше?':
            'Внезапно стайка мелких зомби прыскает в сторону. Но это вряд ли принесёт [game.rape.kind_girl.name] облегчение - к обессиленной женщине неторопливо приближается зомби-мама.'
            call lb_fear_plains_hard_st1 from _call_lb_fear_plains_hard_st1_2
    return

# Теперь начинается жесть
label lb_fear_plains_hard_st1:
    hide bg
    nvl clear
#    play sound get_random_file("sound/pain") 
    show expression 'img/scene/fear/plains/zombie_hard/hard_st1.jpg' as bg
    pause 500
    'Над обессиленной женщиной неторопливо склоняется огромная и уродливая зомби-мама. Чудовищный монстр мнёт нежный животик, не обращая внимания на жалкие трепыхания жертвы.'
    menu:
        'Как жалкие зомби смеют стоять на МОЁМ пути?!!':
            call lb_fear_plains_zombie_fight from _call_lb_fear_plains_zombie_fight_6
        'Обойти по другому коридору':
            call lb_fear_plains_murder from _call_lb_fear_plains_murder_6
        'Интересно, что будет дальше?':
            call lb_fear_plains_hard_st2 from _call_lb_fear_plains_hard_st2
    return

label lb_fear_plains_hard_st2:
    hide bg
    nvl clear
    play sound get_random_file("sound/pain") 
    show expression 'img/scene/fear/plains/zombie_hard/hard_st2.jpg' as bg
    pause 500
    'Белоглазый монстр с силой щупает живот ведьмочки. Длинные, острые и грязные ногти оставляют на нежной коже кровоточащие царапины.'
    menu:
        'Как жалкие зомби смеют стоять на МОЁМ пути?!!':
            call lb_fear_plains_zombie_fight from _call_lb_fear_plains_zombie_fight_7
        'Обойти по другому коридору':
            call lb_fear_plains_murder from _call_lb_fear_plains_murder_7
        'Интересно, что будет дальше?':
            call lb_fear_plains_hard_st3 from _call_lb_fear_plains_hard_st3
    return

label lb_fear_plains_hard_st3:
    hide bg
    nvl clear
    play sound get_random_file("sound/pain") 
    show expression 'img/scene/fear/plains/zombie_hard/hard_st3.jpg' as bg
    pause 500
    'Зомби медленно, но верно разрывает живот женщины. [game.rape.kind_girl.name] истошно орёт и отбивается, но ничего, ничего не может поделать.'
    menu:
        'Как жалкие зомби смеют стоять на МОЁМ пути?!!':
            call lb_fear_plains_zombie_fight from _call_lb_fear_plains_zombie_fight_8
        'Обойти по другому коридору':
            call lb_fear_plains_murder from _call_lb_fear_plains_murder_8
        'Интересно, что будет дальше?':
            call lb_fear_plains_hard_st4 from _call_lb_fear_plains_hard_st4
    return

label lb_fear_plains_hard_st4:
    hide bg
    nvl clear
    play sound get_random_file("sound/pain") 
    show expression 'img/scene/fear/plains/zombie_hard/hard_st4.jpg' as bg
    pause 500
    'Уродливый монстр наконец-то разорвал живот пленницы и почти добрался до тёплых, аппетитных женских кишок. [game.rape.kind_girl.name] пытается сопротивляться, но тщетно: её ждёт лютая, неминуемая смерть.'
    game.dragon 'Всё, [game.rape.kind_girl.name] больше не жилица!'
    $ game.rape.kind_alive = False
    menu:
        'Как жалкие зомби смеют стоять на МОЁМ пути?!!':
            call lb_fear_plains_zombie_fight from _call_lb_fear_plains_zombie_fight_8
        'Обойти по другому коридору':
            call lb_fear_plains_murder from _call_lb_fear_plains_murder_8
        'Интересно, что будет дальше?':
            call lb_fear_plains_hard_st5 from _call_lb_fear_plains_hard_st5
    return

label lb_fear_plains_hard_st5:
    hide bg
    nvl clear
    play sound get_random_file("sound/pain") 
    show expression 'img/scene/fear/plains/zombie_hard/hard_st5.jpg' as bg
    pause 500
    'Зомби-мама начинает пожирать тёплые кишки умирающей ведьмы. Всё, больше тут не будет ничего интересного.'
    menu:
        'Как жалкие зомби смеют стоять на МОЁМ пути?!!':
            call lb_fear_plains_zombie_fight from _call_lb_fear_plains_zombie_fight_9
        'Обойти по другому коридору':
            call lb_fear_plains_murder from _call_lb_fear_plains_murder_9

    return

label lb_fear_plains_murder:  # девушка убита
    $ game.rape.kind_alive = False
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/zombie.jpg' as bg
    '[game.dragon.name] уходит, оставив за спиной бездыханное женское тело в окружении толпы зомби. Конечно, через несколько часов [game.rape.kind_girl.name] восстанет в виде нежити, но ему-то что с того?'
    $ text = u'%s родилась под несчастливой звездой. Она нарвалась на толпу зомби, которые сперва вдоволь надругались над её невинным телом, а затем всласть полакомились её внутренностями. Через пару часов %s восстала в виде ходячего трупа, обречённая на вечное не-мёртвое существование.\n\n' %(game.rape.kind_girl.name, game.rape.kind_girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
    $ game.chronik.death('deAd_zombie','img/scene/fear/plains/zombie.jpg')
    game.dragon.third 'Дальше может быть опасно. Приму-ка я свой истинный облик!'
    call lb_fear_plains_culmination from _call_lb_fear_plains_culmination_1
    return

 
label lb_fear_plains_zombie_fight:
    '[game.dragon.name] принимает свой истинный облик и бросается на орды нежити!'
    $ game.foe = Enemy('zombie', game_ref=game)
    call lb_fight from _call_lb_fight_79
    hide bg
    nvl clear
    if not game.rape.kind_alive:   # Слишком долго ждали, девушка мертва
      show expression 'img/scene/fear/plains/after_murder.jpg' as bg
      '[game.dragon.name] идёт дальше, оставив за спиной бездыханное женское тело. Конечно, через несколько часов [game.rape.kind_girl.name] восстанет в виде нежити, но ему-то что с того?'
      $ text = u'%s родилась под несчастливой звездой. Она нарвалась на толпу зомби, которые сперва вдоволь надругались над её невинным телом, а затем всласть полакомились её внутренностями. Через пару часов %s восстала в виде ходячего трупа, обречённая на вечное не-мёртвое существование.\n\n' %(game.rape.kind_girl.name, game.rape.kind_girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
      $ game.chronik.death('deAd_zombie','img/scene/fear/plains/after_murder.jpg')
    elif game.rape.kind_ill:
      show expression 'img/scene/fear/plains/after_rape.jpg' as bg
      game.rape.kind_girl.third 'Женщина, отдаввшая свою невинность ходячему трупу, обессиленно лежит на полу.'
      game.rape.kind_girl 'Ты пришёл. Слава Небесному Отцу, ты пришёл. Я верила. Я верила...'
      game.dragon.third '[game.dragon.name] коварно улыбается.'
      game.dragon 'И абсолютно правильно делала!'
      $ text = u'На долю бедняжки выпали тяжёлые испытания: ей не повезло нарваться на толпу зомби. Ходячие мертвецы изнасиловали её невинное тело. Правда, %s выручил бедняжку - то ли из жалости, то ли из-за простой случайности. \n\n Но теперь %s больна. В её крови зреет страшный яд, и через несколько часов она неминуемо пополнит ряды мёртового воинства. \n\n' %(game.dragon.name, game.rape.kind_girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
      game.rape.kind_girl 'Я обречена. Зомби осквернили моё тело, и через пару часов я сама стану нежитью.'
      game.dragon '*С фальшивым участием* Какая трагедия!'
      game.rape.kind_girl 'Пожалуйста... перед тем, как это случится... убей меня!!!'
      game.dragon 'Да запросто!'
      if game.rape.Alliance:
        '[game.rape.kind_girl.name] нервно облизывает губы. Она хочет что-то сказать, и это пугает её даже больше, чем скорая и неминуемая смерть.'
        game.rape.kind_girl 'Но даже это - не самое страшное. Этих жутких зомби... натравила на меня моя собственная сестра! Именно она, а не маркиз де Ад, стоит за мучениями и гибелью множества невинных жизней!'
        '[game.dragon.name] удивлённо шипит.'
        game.rape.kind_girl 'Ради спасения невинных... ради тех несчастных, что в муках умерли в этих жутких лабораториях... мы должны остановить мою сестру!'
        game.dragon 'Надо - остановим. Пошли.'
      else:
        game.rape.kind_girl 'Мы должны покончить с этим ужасом и остановить маркиза де Ада. '
        '[game.dragon.name] согласно кивает.'
        game.rape.kind_girl 'И моя сестра... Я понимаю, что это глупо, но я всё ещё надеюсь.'
        '[game.dragon.name] усмехается.'
        game.dragon 'Идём, узнаем, что случилось с твоей сестрой и кто автор этого очаровательного зомби-вируса!'
      if game.dragon.health < 2:
        game.rape.kind_girl 'Идём. Только выпей это лечебное зелье. Мне оно, увы, не поможет.'
        '[game.dragon.name] откупоривает  маленький красный флакончик.'
        $ game.dragon.health = 2
        game.dragon.third 'Раны затянулись. Как она это делает?'
    elif not game.rape.kind_ill:
      show expression 'img/scene/fear/plains/after_save.jpg' as bg
      game.rape.kind_girl.third 'Девушка, спасённая в последний момент, смотрит на дракона счастливыми и чуть ли не влюблёнными глазами.'
      game.rape.kind_girl 'Ты пришёл. Я знала. Я знала, что ты придёшь. Спасибо!'
      game.dragon.third '[game.dragon.name] коварно улыбается.'
      game.dragon 'Ну как я мог поступить иначе!'
      $ text = u'%s родилась под счастливой звездой. Она попала в руки зомби, но %s выручил бедняжку как нельзя вовремя - то ли из жалости, то ли из-за простой случайности.\n\n' %(game.rape.kind_girl.name, game.dragon.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
      game.rape.kind_girl 'Мы должны покончить с этим ужасом и остановить маркиза де Ада. '
      '[game.dragon.name] согласно кивает.'
      game.rape.kind_girl 'И моя сестра... Я понимаю, что это глупо, но я всё ещё надеюсь.'
      '[game.dragon.name] усмехается.'
      game.dragon 'Идём, узнаем, что случилось с твоей сестрой и кто автор этого очаровательного зомби-вируса!'
      if game.dragon.health < 2:
        game.rape.kind_girl 'Идём. Но, спасая меня, ты рисковал жизнью и серьёзно пострадал. Выпей это лечебное зелье!'
        '[game.dragon.name] откупоривает  маленький красный флакончик.'
        $ game.dragon.health = 2
        game.dragon.third 'Раны затянулись. Как она это делает?'
    call lb_fear_plains_culmination from _call_lb_fear_plains_culmination_2
    return


# Кульминация событий
label lb_fear_plains_culmination:
    $game.rape.kind_prison=False  # Добрая ведьма пока не захвачена в плен. Конечно, к этому моменту она могла и погибнуть...
    $game.rape.kind_chocked=False  # Задушила ли добрую ведьму альва
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/culmination.jpg' as bg
    'В главном зале развалилась на подушках красивая и опасная женщина.'
    'Рядом с ней примостился дёрганный мужчина в чёрном балахоне - очевидно, маркиз да Ад.'
    'С одного взгляда ясно, кто тут главный и кто кем управляет. Нет, никакой магии, никакого влияния на разум. Просто де Ад - абсолютный и законченный подкаблучник, полностью покорившийся чужой воле.'
    python: #делаем аватарку сестры для диалогового окна
        dark_sister= Talker(game_ref=game)
        dark_sister.avatar = "img/scene/fear/plains/dark_sister.jpg"
        dark_sister.name = 'Тёмная сестра' 
        de_Ad= Talker(game_ref=game)
        de_Ad.avatar = "img/scene/fear/plains/deAd.jpg"
        de_Ad.name = 'Маркиз де Ад' 
# Первый блок - приветствие
    if not game.rape.kind_alive:   
      dark_sister 'Ты пришёл. Как же невовремя!'
      game.dragon 'А, так ты и есть та самая жена маркиза де Ада, про которую рассказывала [game.rape.kind_girl.name]? Кстати, там твою сестру сожрали твои же питомцы.'
      dark_sister.third '[dark_sister.name] холодно улыбается.'
      dark_sister 'Жаль.'
      dark_sister 'Очень жаль, что она отделалась так легко. За то, что она привела в мой... в наш замок дракона, она заслужила куда худшей участи.'
    elif game.rape.kind_alive and not game.rape.Alliance:
      game.rape.kind_girl  'Сестра... что с тобой произошло? Что с тобой сделал маркиз де Ад?'
      'При упоминании своего имени мужчина отчётливо ёжится.'
      dark_sister 'Маркиз? Ничего. Он очень вежливый и послушный мальчик. А вот что сделала ты?! Как ты смела привести в мой... в наш замок дракона?!'
      game.rape.kind_girl 'Я должна прекратить ужасы, творящиеся в этом замке!'
      dark_sister.third 'Женщина приходит в ярость.'
      dark_sister 'Ужасы? Это рутинный рабочий процесс по созданию вируса, призванного уничтожить драконий род! Процесс, сорванный по твоей вине!!!'
      game.rape.kind_girl.third '[game.rape.kind_girl.name] выглядит потрясённой.'
      game.rape.kind_girl 'Так это ты... так это по твоему приказу... Сестра, хоть мне больно даже говорить об этом, я должна остановить тебя!'
      dark_sister 'А я убью тебя, и сделаю это с превеликим удовольствием'
      if game.rape.kind_ill:
        dark_sister 'Вижу, ты уже заразилась. Хорошо. Если мне повезёт, то я проверю пару теорий.'
      elif not game.rape.kind_ill:
        dark_sister 'Жаль, что общение с зомби никак не сказалось на твоём самочувствии. Ничего, если мне повезёт, я с удовольствием дам тебе поучавствовать в парочке экспериментов.'
    elif game.rape.kind_alive and game.rape.Alliance:
      game.rape.kind_girl.third '[game.rape.kind_girl.name] смотрит спокойно и сурово.'
      game.rape.kind_girl 'Сестра. Ты сама превратилась в чудовище. Ты сама есть чудовище. '
      dark_sister 'И это смеешь говорить ты? Ты, помогающая дракону?!'
      game.rape.kind_girl 'Дракон - не человек. Ты же убиваешь и мучаешь своих собственных сородичей. И ради чего? Ради мифического "вируса", что бы ни значило это слово? '
      dark_sister 'Принцип меньшего зла в чистом виде.'
      game.rape.kind_girl 'Или чьи-то больные амбиции. Сестра, хоть мне тяжело даже говорить об этом, я должна остановить тебя!'
      dark_sister 'А я убью тебя, и сделаю это с превеликим удовольствием'
      dark_sister 'Вижу, ты уже заразилась. Хорошо. Если мне повезёт, то я проверю пару теорий.'

    # Второй блок - обсуждение вируса
    dark_sister '[game.dragon.name], ты пришёл очень невовремя. До окончания разработки вируса PAX-12 оставалось совсем немного...'
    game.dragon 'Всё равно на меня он бы не подействовал.' 
    dark_sister 'Чушь.'
    game.dragon 'Не чушь, и я могу с лёгкостью это доказать!'
    dark_sister.third 'Кажется, слова дракона задевают мучительницу за живое.'
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/fury.jpg' as bg
    pause 3.0
    dark_sister 'Доказывай.'
    game.dragon 'Судя по наблюдаемым симптомам, вирус PAX-12 в первую очередь атакует протеолитический фермент C3, препятствуя системе комплемента формировать гуморальную защиту для реализации иммунного ответа. Так? '
    dark_sister 'Так.'
    game.dragon 'Однако в глобулиновой фракции плазмы драконьей крови присутствует XX-конвертаза, гидролизущая любой компонент системы кмплемента. ' 
    game.dragon 'Таким образом, драконы обладают абсолютным врождённым иммунитетом.'
    'Чувствуется, что Тёмная сестра растеряна и сбита с толку.'
    dark_sister 'Но... как...'
    'Правда - это самое сильное оружие. Пора нанести завершающий удар!'
    game.dragon 'Вместе с тем при малейших изменениях генома PAX-12 становится опасным для людей, вызывая стремительно распространяющуюся зомби-пандемию.'
    dark_sister 'Нееет!!!'
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/culmination.jpg' as bg
    'Тёмная сестра в шоке. Узнать, что твой труд - бесполезен, твои мечты - пусты, жертвы - напрасны, а твои усилия по спасению человечества принесли обратный результат... Есть от чего впасть в отчаяние. '
    if game.rape.kind_alive:
      '[game.rape.kind_girl.name] смотрит на сестру с печальной улыбкой.'
      game.rape.kind_girl 'Я же говорила... Из всех решений выбирай самое этичное - и не ошибёшься.'
    'Тёмная сестра дерзко поднимает голову.'
    dark_sister 'Нет. Если мне суждено сегодня выжить, то я не остановлюсь. пока отродья Тёмной Госпожи не будут стёрты с лица земли. Не получилось с первого раза - получится со второго.'
    game.dragon.third 'Дракон отчётливо фыркает. Видно, что в это он ну ни капельки не верит.'

    # Третий блок - обсуждение вируса. Именно здесь происходят основные развилки.
    dark_sister 'Кстати, [game.dragon.name], а ты не встречал альву по имени [game.rape.elf_girl.name]?'
    if game.rape.Alliance:  # Альянс заключён
      if game.rape.elf_lie:
        game.dragon 'Встречал. Она сейчас пытается сделать PAX-12 безопасным для людей.'
        dark_sister 'Лооожь! [game.rape.elf_girl.name] истово, фанатично ненавидит людей. Всех людей без исключения. Она - сторонница исключительности расы альвов. Именно из-за неё PAX-12 теперь опасен для людей, а не для драконов!'
        dark_sister 'Увы, я поняла это слишком поздно... она была невероятно талантливой исследовательницей. И увы, я не убила её сразу же!!!'
        $ text = u'Правда, из разговора с Тёмной сестрой выяснилось, что %s соврала дракону. На самом деле она фанатично ненавидела человечество и жаждала создать зомби-вирус, способный нанести колоссальный урон человеческой цивилизации. \n\n' %(game.rape.elf_girl.name)
        $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
      elif not game.rape.elf_lie:
        game.dragon 'Встречал. Она сейчас повышает заразность PAX-12.'
        dark_sister 'Проклятье! Ну почему я сразу же не казнила эту предательницу?!!'
        if game.rape.kind_alive:
          game.rape.kind_girl 'Потому что ты умная, образованная, гениальная дура.'
      dark_sister '[game.dragon.name], даже ты должен понимать, что подрыв кормовой базы отрицательно скажется на развитии вида. Если зомби-вирус снесёт с лица земли человеческую цивилизацию, ты и твои отродья вымрут.'
      game.dragon.third 'Дракон игриво  шевелит хвостом. Похоже, обсуждение подобных перпектив доставляет ему истинное удовольствие.'
      game.dragon 'Или вирус опустошит всего-навсего пару-тройку провинций...'
      game.dragon 'Это всё? Или ещё что-то хочешь добавить?'
      if not game.rape.kind_alive:   # Добрая ведьма мертва
        dark_sister.third 'Голос Тёмной сестры звучит твёрдо и решительно.'
        dark_sister 'Всё. Мы временно объединяемся с тобой ради того, чтобы остановить безумную альву, и выясняем наши отношения позднее.'
        nvl clear
        menu:
            'Пообещать - не значит сделать...':
                game.dragon.third 'Это обещает быть забавным... а в случае чего я ещё успею передумать.'
                game.dragon 'Хорошо. Альву и впрямь следует остановить.'
                call lb_fear_plains_elf_battle from _call_lb_fear_plains_elf_battle_1
                # Противостояние с эльфийкой
            'Этот маразм закончится здесь и сейчас!!!':
                game.dragon.third 'Интересно, на что она вообще рассчитывала, делая это предложение?'
                game.dragon 'Ты признала, что хочешь уничтожить весь мой род, а теперь просишь меня защитить человечество?'
                game.dragon 'Просишь - МЕНЯ?!!'
                dark_sister 'Что же. Разговоры окончены.'
                dark_sister 'Умри.'
                $ game.foe = Enemy('dark_sister', game_ref=game)
                call lb_fight from _call_lb_fight_80
                hide bg
                show expression 'img/scene/fear/plains/death.jpg' as bg
                game.dragon 'Ты проиграла, женщина'
                'Тёмная сестра что-то хрипит, но дракон давит ей на грудь, расплющивая грудную клетку. Через десяток долгих секунд она превращается в безжизненную кучку плоти.'
                'Захватив лектинополимер маннозы, [game.dragon.name] возвращается к альве.'
                call lb_fear_plains_elf_help from _call_lb_fear_plains_elf_help_1
      elif game.rape.kind_alive:  # Добрая ведьма жива
        $ text = u'Встреча сестёр прошла тяжело - и это ещё мягко сказано! Оказалось, что за всеми злодеяниями маркиза де Ада стояла его жена. Сёстры решили, что им двоим не жить на этом свете. Поскольку приближалась битва с фанатичной альвой, мечтающей об уничтожении человечества, вопрос встал ребром - какую из сестёр поддержит дракон? \n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
        dark_sister.third 'Похоже, Тёмная сестра чётко осознаёт, что на её предложение дракон ответит отказом, поэтому решает наглеть по полной.'
        dark_sister 'Есть. Если мы будем сотрудничать, [game.rape.kind_girl.name] отправится прямо на лабораторный стол. Я займусь ею после.'
        game.rape.kind_girl 'Я понимаю, что альву требуется останосить. Но я отказываюсь сотрудничать со своей сестрой даже в такой малости! Эта... женщина оскверняет всё, за что берётся! Сперва нам надо остановить её!'
        game.dragon.third '[game.dragon.name] задумчиво чешет хвостом затылок...' 
        nvl clear
        menu:
            'В принципе, [game.rape.kind_girl.name] права...':
                game.dragon.third 'Помогать своему врагу? Нет уж, до таких глубин высот коварства мне ещё далеко!'
                game.dragon '[game.rape.kind_girl.name] права. Будем решать проблемы в порядке очереди.'
                dark_sister 'Что же. Разговоры окончены.'
                dark_sister 'Умри.'
                $ game.foe = Enemy('dark_sister', game_ref=game)
                call lb_fight from _call_lb_fight_81
                $ text = u'%s встал на сторону доброй ведьмы. %s перезала гороло своей сестры, быстро и милосердно. \n\n' %(game.dragon.name,game.rape.kind_girl.name)
                $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
                hide bg
                show expression 'img/scene/fear/plains/death.jpg' as bg
                pause 500
                game.dragon 'Ты проиграла, женщина'
                'Тёмная сестра хрипит что-то неразборчивое - дракон крепко прижимает её к полу.'
                game.dragon '[game.rape.kind_girl.name], убей свою сестру.'
                game.rape.kind_girl.third '[game.rape.kind_girl.name] со скорбным видом подходит к распластанному женскому телу.'
                game.rape.kind_girl 'Мне жаль, что так вышло. Но это необходимо.'
                game.rape.kind_girl.third 'Одним движением [game.rape.kind_girl.name] перезает горло своей сестры. Та погибает быстро и без мучений. '
                if game.dragon.health < 2:
                  game.rape.kind_girl 'Ты ранен. Выпей  это лечебное зелье. '
                  '[game.dragon.name] откупоривает  маленький красный флакончик.'
                  $ game.dragon.health = 2
                  game.dragon.third 'Раны затянулись. Как она это делает?'
                game.rape.kind_girl 'А теперь нам надо остановить альву!'
                game.dragon 'Ага.'
                '[game.dragon.name] и [game.rape.kind_girl.name] возвращаются к альве. Дракон не забывает захватить лектинополимер маннозы - так, на всякий случай.'
                call lb_fear_plains_elf_help from _call_lb_fear_plains_elf_help_2
            'Отправить кого-то на лабораторный стол - это так по-драконьи!':
                $ text = u'%s встал на сторону тёмной сестры. %s оказалась на лабораторном столе с перспективой послужить материалом для безумных экспериментов. \n\n' %(game.dragon.name,game.rape.kind_girl.name)
                $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
                game.dragon.third '[game.rape.kind_girl.name] надоела мне хуже пережаренного мяса!'
                game.dragon 'Сестрица, думаю, я согласен с твоими условиями.'
                game.rape.kind_girl.third '[game.rape.kind_girl.name] смотрит на дракона широко открытыми глазами, словно не веря в происходящее.'
                game.rape.kind_girl.third 'С её губ срывается шёпот:'
                game.rape.kind_girl 'Это же какой-то трюк, да? Военная хитрость?'
                game.dragon 'Никаких хитростей.'
                hide bg
                nvl clear
                show expression 'img/scene/fear/plains/bdsm.jpg' as bg
                '[game.rape.kind_girl.name] настолько потрясена, что не сопротивляется, когда сестра кладёт её на лабораторный - крайне смахивающий на пыточный - стол. Впрочем, её сопротивление всё равно было бы бесполезным.'
                $game.rape.kind_prison=True
                dark_sister 'Времени мало, [game.rape.elf_girl.name] крайне талантлива. Займёмся подопытной позже.'
                game.dragon 'Ты права, сладкое подождёт.'
                call lb_fear_plains_elf_battle from _call_lb_fear_plains_elf_battle_2
    elif not game.rape.Alliance:  # Альянс не заключён
      if game.rape.elf_alive:
        game.dragon 'Встречал, но она показалась мне подозрительной, и я оставил её в темнице.'
        dark_sister 'Это хорошо.'
      elif not game.rape.elf_alive:
        game.dragon 'Встречал, но она показалась мне подозрительной, и я убил её.'
        dark_sister 'Это просто отлично!'
      # Развилка - жива ведьма или нет.
      if not game.rape.kind_alive:   # Добрая ведьма мертва
        dark_sister 'Что же. Шансов у меня немного, но я буду сражаться с тобой до последнего вздоха!'
        menu:
            'Кажется, из-за предыдущих выборов у меня не осталось выбора!':
                game.dragon 'С радостью тебе этот самый "последний вздох" обеспечу.'
                $ game.foe = Enemy('dark_sister', game_ref=game)
                call lb_fight from _call_lb_fight_82
                hide bg
                show expression 'img/scene/fear/plains/death.jpg' as bg
                pause 500
                game.dragon 'Ты проиграла, женщина'
                'Тёмная сестра что-то хрипит, но дракон давит ей на грудь, расплющивая грудную клетку. Через десяток долгих секунд она превращается в безжизненную кучку плоти.'
                if game.rape.elf_alive:
                  game.dragon 'А теперь - время для грабежа и насилия!'
                  'Слуги уже растащили множество ценных вещиц, но кое-что досталось и дракону:'
                  call lb_fear_plains_rob from _call_lb_fear_plains_rob_5
                  hide bg 
                  show expression 'img/scene/fear/plains/elf_help.jpg' as bg
                  'Покидая замок, [game.dragon.name] не забыл прихватить с собой альву.'
                  $ game.girl=game.rape.elf_girl
                  $ text = u'Убив жену маркиза де Ада, дракон забрал себе альву в качестве законного трофея.\n\n'
                  $game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
                  call lb_nature_sex from _call_lb_nature_sex_41
                  call lb_fear_plains_deAd from _call_lb_fear_plains_deAd_1
                elif not game.rape.elf_alive:
                  call lb_fear_plains_unfortune from _call_lb_fear_plains_unfortune_1 


      elif game.rape.kind_alive:   # Добрая ведьма жива
        game.rape.kind_girl 'Как это ни горько, тебя нужно остановить.'
        dark_sister 'Что же. Если я должна разъять вас на части, [game.dragon.name] и [game.rape.kind_girl.name], я сделаю это!'
        $ text = u'Встреча сестёр прошла тяжело - и это ещё мягко сказано! Оказалось, что за всеми злодеяниями маркиза де Ада стояла его жена. Сёстры решили, что им двоим не жить на этом свете. \n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
        menu:
            'Если она хочет боя, она его получит':
                game.dragon.third 'Кажется, это цитата какого-то демона?'
                game.dragon 'Какая незадача. Я намерен сделать с тобой то же самое.'
                $ game.foe = Enemy('dark_sister', game_ref=game)
                call lb_fight from _call_lb_fight_83
                $ text = u'%s встал на сторону доброй ведьмы. %s перезала гороло своей сестры, быстро и милосердно. \n\n' %(game.dragon.name,game.rape.kind_girl.name)
                $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
                hide bg
                show expression 'img/scene/fear/plains/death.jpg' as bg
                pause 500
                game.dragon 'Ты проиграла, женщина'
                'Тёмная сестра хрипит что-то неразборчивое - дракон крепко прижимает её к полу.'
                game.dragon '[game.rape.kind_girl.name], убей свою сестру.'
                game.rape.kind_girl.third '[game.rape.kind_girl.name] со скорбным видом подходит к распластанному женскому телу.'
                game.rape.kind_girl 'Мне жаль, что так вышло. Но это необходимо.'
                game.rape.kind_girl.third 'Одним движением [game.rape.kind_girl.name] перезает горло своей сестры. Та погибает быстро и без мучений. '
                hide bg
                show expression 'img/bg/lair/ruins_inside.jpg' as bg
                game.dragon.third 'После победы дракон занялся грабежом. А здесь было что пограбить:'
                call lb_fear_plains_rob from _call_lb_fear_plains_rob_2
                if game.rape.elf_alive:
                  game.dragon.third 'Отвлёкшись от этого увлекательного процесса, дракон осознал, что его спутницы нигде не видно.'
                  game.dragon 'Куда это она? А, точно, она пошла альву освобождать!'
                  game.dragon 'Надо посмотреть, а то ещё освободит ненароком...'
                  hide bg
                  nvl clear
                  show expression 'img/scene/fear/plains/murder.jpg' as bg
                  'Всё ещё хуже. чем боялся дракон.'
                  '[game.rape.kind_girl.name] и вправду освободила альву, но [game.rape.elf_girl.name] ответила ей неблагодарностью. Обжав локтём тонкую шейку, альва душила свою спасительницу. [game.rape.kind_girl.name] вяло трепыхалось, но было понятно, что у неё ничего не выйдет.'
                  game.rape.elf_girl '[game.dragon.fullname], я хочу доработать вирус PAX-12 и устроить зомби-эпидемию в землях людей! Если ты не дашь мне этого сделать, я задушу её!'
                  nvl clear
                  'Дракон ложится на пол, пристально наблюдает за схваткой и молчит.'
                  game.rape.elf_girl.third '[game.rape.elf_girl.name] слегка разжимает хватку.'
                  game.rape.elf_girl 'Ну, давай же, скажи, что ты молишь о пощаде!!!'
                  game.rape.kind_girl '[game.dragon.name], не слушай её! Моя смерть ниче...'
                  game.rape.elf_girl.third '[game.rape.elf_girl.name] напрягает локоть, полностью перекрываю доступ кислорода.'
                  nvl clear
                  'Дракон молчит.'
                  game.rape.elf_girl 'Я не шучу!'
                  '[game.rape.kind_girl.name] хрипит, скребёт руками и дрыгает ногами, тщетно пытаясь освободиться.'
                  nvl clear
                  'Дракон молчит.'
                  game.rape.elf_girl 'Я серьёзно! Ещё чуть-чуть, и ты её потеряешь!!!'
                  '[game.rape.kind_girl.name] бьётся в агонии'
                  nvl clear
                  'Дракон молчит.'
                  'Подождав некоторое время, [game.rape.elf_girl.name] отбрасывает в сторону бездыханное тело своей спасительницы.'
                  $ text = u'А потом %s совершила коллосальную ошибку, освободив пленную альву. %s немедленно взяла её в заложницы, требуя от дракона продолжения работы над вирусом! Увы, %s лишь бесстрастно наблюдал за разыгравшейся трагедией. Доказывая серьёзность  намерений, альва задушила свою жертву.  \n\n' %(game.rape.kind_girl.name,game.rape.elf_girl.name,game.dragon.name )
                  $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
                  $ game.chronik.death('deAd_murder','img/scene/fear/plains/murder.jpg')
                  $ text = u'После победы над своей сестрой %s освободила пленную альву. Но %s, требуя от дракона продолжения работы над зомби-вирусом, взяла её в заложницы и задушила. \n\n' %(game.rape.kind_girl.name,game.rape.elf_girl.name )
                  $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
                  hide bg
                  show expression 'img/scene/fear/plains/murder.jpg' as bg with dissolve
                  pause 500
                  game.dragon 'Отчего ты решила, что эта падаль хоть что-то для меня значит?'
                  game.rape.elf_girl 'А она не значит?'
                  game.dragon 'Нет.'
                  $game.rape.kind_chocked=True
                  $game.rape.kind_alive=False
                  call lb_fear_plains_elf_help from _call_lb_fear_plains_elf_help_3
                elif not game.rape.elf_alive:
                  call lb_fear_plains_final from _call_lb_fear_plains_final_1
            'Интересно, а у меня хватит коварства, чтобы помирить сестёр?':
                game.dragon.third 'Они так трогательно ненавидят друг друга... Попытка их примирения - настоящий вызов моему коварству!' 
                game.dragon 'Тёмная сестра, ты же не хочешь сражаться!'
                dark_sister 'Я осознаю свои силы и понимаю, что мало что могу противопоставить дракону. Но вы же не оставите мне выбора!'
                game.dragon '[game.rape.kind_girl.name], на самом деле ты же не хочешь убивать свою сестру.'
                game.rape.kind_girl 'Сама мысль об этом причиняет мне муку. Но у меня же нет выбора!'
                game.dragon 'Я считаю, что Тёмная сестра должна продолжить работу над вирусом против меня, но без человеческих жертвоприношений.'
                dark_sister 'Но...'
                game.dragon 'Я думаю, что у тебя ничего не получится. Ты веришь в иное. Прекрасно, пробуй, только обойдись без всей этой грязи и крови! [game.rape.kind_girl.name] проследит за твоим благоразумием.'
                game.rape.kind_girl 'Я бы с радостью, но сестрёнка не согласится...'
                game.dragon 'Твоя первая попытка привела к тому, что на свободу чуть не вырвался вирус, способный уничтожить пару-тройку провинций. Что дальше, а, "защитница человечества"?'
                dark_sister 'Ты... ты...'
                dark_sister 'Ты прав.'
                dark_sister 'Исходя из принципа меньшего зла, я чуть было не превратилась во зло большее.'
                hide bg
                nvl clear
                show expression 'img/scene/fear/plains/sisters.jpg' as bg
                'Сёстры бросаются в объятия друг друга.'
                game.rape.kind_girl 'Спасибо! Спасибо!'
                '[game.rape.kind_girl.name] покрывает поцелуями лицо своей сестры.'
                dark_sister 'Теперь и я вижу, что ты можешь быть и не злым. Я даже сомневаюсь в необходимости дальнейших разработок...'
                $ text = u'Дракон отличался немалым коварством. После его речей %s помирилась со своей сестрой. ' %(game.rape.kind_girl.name )
                $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
                $ game.chronik.write_image('img/scene/fear/plains/sisters.jpg',game.dragon.level,game.girl.girl_id-1)
                $ game.chronik.live('deAd_sisters','img/scene/fear/plains/sisters.jpg')                
                if game.rape.kind_ill:
                  $ text = u'Заражение зомби-вирусом не стало проблемой: у жестокой и талантливой исследовательницы давным-давно было готово лекарство. %s выздоровела в мгновение ока. ' %(game.rape.kind_girl.name )
                  $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
                  '[game.rape.kind_girl.name] резко грустнеет'
                  game.rape.kind_girl 'Я счастлива... жаль только, что счастье будет недолгим.'
                  game.rape.kind_girl 'Через пару часов я неизбежно превращусь в зомби.'
                  dark_sister 'Глупости не говори. Вакцина давно изобретена и даже апробирована. Держи.'
                  '[game.rape.kind_girl.name] залпом выпивает мутноватую жидкость, и лицо её стремительно светлеет.'
                  game.rape.kind_girl 'Здорова!'
                $ text = u'Дальнейшая судьба сестёр неизвестна. Но, вероятно, всё закончилось хорошо. \n\n Хоть у кого-то - хорошо... ' 
                $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
                game.rape.kind_girl 'Что мы будем делать дальше?'
                dark_sister 'Мои действия изрядно подмочили репутацию моего... нашего замка. Необходимо сменить операционную базу.'
                dark_sister 'Дорогой, ты же согласишься передать титул какому-нибудь дальнему родственнику и уехать с нами в деревню, в глушь, в Са...'
                de_Ad 'Конечно, любимая, куда угодно!'
                dark_sister 'Вот и ладненько.'
                dark_sister 'Я благодарна тебе, [game.dragon.fullname]'
                dark_sister 'Можешь тащить в логово всё, что найдёшь, не жалко.'
                call lb_fear_plains_rob from _call_lb_fear_plains_rob_3
                dark_sister 'Что же касается более приятного бонуса...'               
                if game.rape.elf_alive:
                  dark_sister 'Думаю, та самая альва, [game.rape.elf_girl.name], послужит достойной наградой.'
                  game.dragon 'Да, вполне.'
                  game.rape.kind_girl 'Но...'
                  dark_sister 'Сестрёнка, [game.rape.elf_girl.name] хотела выпустить на свободу вирус, убивающий людей и превращающий их в уродливых, бездушных монстров. Ты и вправду считаешь, что её стоит жалеть?'
                  game.rape.kind_girl 'Нет... Нет, не стоит, она заслужила это. Прощай, [game.dragon.name]!'
                  dark_sister 'Прощай, дракоша!'
                  game.dragon 'Прощайте!'
                  hide bg
                  show expression 'img/scene/fear/plains/elf_help.jpg' as bg
                  'Покидая замок, [game.dragon.name] с разрешения хозяев прихватил с собой альву.'
                  $ game.girl=game.rape.elf_girl
                  $ text = u'Помирив жену маркиза де Ада с сестрой, дракон забрал себе альву в качестве законного трофея.\n\n'
                  $game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
                  call lb_nature_sex from _call_lb_nature_sex_42
                elif not game.rape.elf_alive:
                  dark_sister 'В своих экспериментах я планировала использовать огршу. Думаю, она послежит тебе достойной наградой.'
                  game.rape.kind_girl 'Но...'
                  dark_sister 'Сестрёнка, на совести этой людоедки - не менее десятка человеческих жизней. Ты и вправду считаешь, что её стоит жалеть?'
                  game.rape.kind_girl 'Нет... Нет, наверное, не стоит. Прощай, [game.dragon.name]!'
                  dark_sister 'Прощай, дракоша! Забирай огршу, если осмелишься!'
                  game.dragon 'Прощайте! Конечно, осмелюсь!'
                  call lb_fear_plains_ogre from _call_lb_fear_plains_ogre_1 
    return

label lb_fear_plains_rob:
    python:
        count = random.randint(3, 8)
        alignment = 'knight'
        min_cost = 100
        max_cost = 700
        obtained = "Это предмет из разграбленной крепости маркиза де Ада."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    '[trs_descrptn]'
    $ game.lair.treasury.receive_treasures(trs)
    return

label lb_fear_plains_unfortune:
    nvl clear
    hide bg
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    game.dragon.third '[game.dragon.name] подчищает сокровища, которые не успели украсть слуги:'
    call lb_fear_plains_rob from _call_lb_fear_plains_rob_1
    game.dragon.third 'Девиц в замке нет, трофеев мало, вирус PAX-12 до ума доводить некому...'
    game.dragon.third 'И почему мне кажется, что что-то пошло не так?'
    game.dragon.third 'Ладно, попаду в следующий раз в подобную ситуацию - поступлю по-другому!'
    call lb_fear_plains_deAd from _call_lb_fear_plains_deAd_2
    return

label lb_fear_plains_deAd:
    hide bg                
    show expression 'img/scene/fear/plains/pass.jpg' as bg
    de_Ad 'Слава Небесному Отцу, я свободен! Свободен!!!'
    de_Ad 'Всё, передаю титул первому попавшемуся дальнему родственнику, а сам - в деревню, в глушь, на край света!'
    de_Ad 'Как же я устал от этого бесконечного ужаса...'
    stop music fadeout 5.0  
    return

label lb_fear_plains_elf_battle:      # Битва Тёмной сестры с эльфийкой
    hide bg
    hide fg
    nvl clear
    show expression 'img/scene/fear/plains/laboratory.jpg' as bg
    show expression 'img/scene/fear/plains/alchemist.png' as fg   
    game.rape.elf_girl 'Что происходит?'
    dark_sister 'Пришло время умереть, тварь!'
    game.rape.elf_girl  '[game.dragon.name], неужели ты встанешь на сторону своего врага и поможешь этим жалким людишкам?'
    dark_sister '[game.dragon.name], неужели ты согласишься с этой альвой и поставишь под угрозу свою кормовую базу?'
    game.dragon 'Эээ...'
    'Похоже, пришла пора делать выбор'
    menu:
        'С одной стороны, [game.rape.elf_girl.name] права...':  # Помочь эльфийке
            game.dragon 'Пожалуй, я заинтересован в дальнейшей разработке вируса.'
            dark_sister 'Что?!! Ты же обещал, что встанешь на мою сторону!!!'
            '[game.dragon.name] пожимает хвостом.'
            game.dragon 'Что поделаешь, у меня хроническое спиннокинжальное расстройство!'
            'Тёмная сестра приходит в ярость. Одним заклинанием она парализует вскинувшуюся альву, а потом атакует дракона.'
            dark_sister 'Умри!'
            hide fg
            $ game.foe = Enemy('dark_sister', game_ref=game)
            call lb_fight from _call_lb_fight_84
            $ text = u'В решающей битве %s встал на сторону обозлённой альвы. %s жестоко и изощрённо вскрыла живот своей бывшей начальнице. \n\n' %(game.dragon.name,game.rape.elf_girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            hide bg
            show expression 'img/scene/fear/plains/death.jpg' as bg
            pause 500
            game.dragon 'Ты проиграла, женщина'
            'Тёмная сестра хрипит что-то неразборчивое - дракон крепко прижимает её к полу.'
            'Похоже, [game.rape.elf_girl.name] оклемалась от последствий заклинания.'
            game.rape.elf_girl 'Разрешите, я прикончу эту тварь'
            game.dragon 'Да на здоровье.'
            nvl clear
            'Прекрасная лесная дева вонзает короткий клинок в половую щель поверженной противницы, а потом вскрывает ей живот до самой грудины.'
            game.rape.elf_girl 'Умри, умри, УМРИ!!!'
            'Смерть Тёмной сестры была грязной и болезненной.'
            'Но всё-таки не такой болезненной, как у многиих её жертв.'
            nvl clear
            'Теперь надо решить, что бы такое эдакое сделать с альвой...'
            call lb_fear_plains_elf_help from _call_lb_fear_plains_elf_help_4
        '...с другой стороны, в словах Тёмной сестры тоже есть смысл...':  # Помочь Тёмной сестре
            game.dragon 'Пожалуй, дальнейшую разработку вируса следует прекратить.'
            game.rape.elf_girl 'Что?!! Ты же обещал, что встанешь на мою сторону!!!'
            '[game.dragon.name] пожимает хвостом.'
            game.dragon 'Что поделаешь, у меня хроническое спиннокинжальное расстройство!'
            'Прекрасная лесная дева приходит в ярость. Одним заклинанием она парализует вскинувшуюся Тёмную сестру, а потом атакует дракона.' 
            game.rape.elf_girl 'Умри.'
            hide fg
            $ game.foe = Enemy('elf_madness', game_ref=game)
            call lb_fight from _call_lb_fight_85
            $ text = u'В решающей битве %s встал на сторону Тёмной сестры. %s схватилась с драконом и погибла в жарком и жестоком бою.\n\n' %(game.dragon.name,game.rape.elf_girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            $ game.chronik.write_image('img/scene/fight/elf_dead.jpg',game.dragon.level,game.girl.girl_id)
            $ game.chronik.death('deAd_elf_fail','img/scene/fear/plains/elf_dead.jpg')
            hide bg
            nvl clear
            show expression 'img/scene/fear/plains/choice.jpg' as bg
            '[game.dragon.name] склоняется над поверженной Тёмной сестрой.'
            'Женщина уже пришла в сознание, но ещё не восстановилась от последствий заклинания. Сейчас она беспомощней младенца.'
            game.dragon 'Хм, что бы решить?'
            menu:
                'У меня нет ни единой причины оставлять её в живых.':
                    nvl clear
                    dark_sister.third 'Тёмная сестра стискивает зубы, с ненавистью смотря на дракона.'
                    dark_sister.third 'Она понимает, что не получит пощады, и не просит её.'
                    '[game.dragon.fullname] жестоко убивает Тёмную сестру, раздирая её на части.'
                    if game.rape.kind_alive:
                      call lb_fear_plains_free from _call_lb_fear_plains_free_1
                    elif not game.rape.kind_alive:
                      call lb_fear_plains_unfortune from _call_lb_fear_plains_unfortune_2
                'Там же ещё [game.rape.kind_girl.name] осталась недорезанная!' if game.rape.kind_alive:
                    nvl clear
                    dark_sister.third 'Тёмная сестра стискивает зубы, с ненавистью смотря на дракона. Она понимает, что не получит пощады, и не просит её.'
                    game.dragon 'Вставай.'
                    dark_sister 'Что?'
                    dark_sister.third 'Тёмная сестра ошарашена. Хотя нет, "ошарашена" - слишком мягкое определение.'
                    game.dragon 'Вставай. Мне интересно, что ты со своей сеструхой будешь делать.'
                    dark_sister.third 'Глаза Тёмной сестры вспыхивают лихорадочным блеском.'
                    dark_sister 'У меня как раз была идея одного смелого научного эксперимента. Проассестируешь?'
                    game.dragon 'Угу.'
                    hide bg
                    nvl clear
                    show expression 'img/scene/fear/plains/bdsm.jpg' as bg
                    dark_sister 'Ну что, ты рада меня видеть, сестрёнка?'
                    game.rape.kind_girl 'Если и я пойду долиной смертной тени, не убоюсь я зла, потому что Ты со мной...'
                    dark_sister '[game.dragon.fullname], для удобства ассистирования предлагаю тебе перейти в форму человека.'
                    dark_sister 'А ещё необходим кляп. Образцы во время работы производят абсолютно неприемлимый уровень шумового загрязнения.'
                    hide bg 
                    show expression 'img/scene/fear/plains/bdsm_death.jpg' as bg
                    $ text = u'Пленнице не повезло - %s убил альву и полность встал на сторону Тёмной сестры. %s послужила материалом для жестоких и бесчеловечных экспериментов. \n\n' %(game.dragon.name,game.rape.kind_girl.name)
                    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
                    $ game.chronik.death('deAd_bdsm_death','img/scene/fear/plains/bdsm_death.jpg')
                    'В лаборатории идёт спокойная и кропотливая работа.'
                    nvl clear
                    dark_sister.third 'Иглы в точки 7, 13 и 17.'
                    play sound get_random_file("sound/pain")
                    nvl clear 
                    game.dragon.third 'Сделано. Поверни пятый ворот на три деления.'
                    nvl clear
                    play sound get_random_file("sound/pain")
                    dark_sister.third 'Да, ты прав. По кубику раствора алмазной пыли в молочные железы и два кубика в мочевой пузырь.'
                    nvl clear 
                    play sound get_random_file("sound/pain")
                    game.dragon.third 'Это же сколько добра на неё переводим!'
                    nvl clear
                    dark_sister.third 'Всё ради науки!!! Толчёное стекло не подходит для наложения заклинаний.'
                    play sound get_random_file("sound/pain")
                    hide bg
                    nvl clear
                    show expression 'img/scene/fear/plains/culmination.jpg' as bg
                    dark_sister 'Спасибо! Это был потрясающий эксперимент, который продвинул разработку боевого вируса далеко...'
                    dark_sister 'Хм, далеко в сторону.'
                    game.dragon 'Да, это был очень интересный и познавательный опыт. Кстати, ты соврала.'
                    game.dragon 'Ты не ради спасения человечества всё это затеяла. Ты лишь тешишь своё научное любопытство.'
                    'Тёмная сестра долго молчит.'
                    dark_sister 'Предположим, так. И что это меняет?'
                    game.dragon 'Всё. Занимайся дальше тем же самым. А если вдруг преуспеешь, во что я ни капельки не верю... сперва поставь в известность меня и Тёмную Госпожу.'
                    dark_sister 'Хорошо, договорились.'
                    'Тёмная сестра приободряется, у неё как будто открывается второе дыхание.'
                    dark_sister 'Мой... наш замок надо покинуть и переехать на новую операционную базу: у этого места слишком дурная репутация. Титул следует передать первому попавшемуся дальнему родственнику. Не возражаешь?'
                    de_Ad 'Разумеется, нет, любимая, какой разговор!'
                    dark_sister 'Думаю, эти безделушки послужат хорошим залогом нашего сотрудничества.'
                    call lb_fear_plains_rob from _call_lb_fear_plains_rob_4
                    dark_sister 'Что касается более приятного трофея... Я хотела провести пару экспериментов над огршей, но тебе она нужнее.'
                    dark_sister 'Забирай великаншу, если осмелишься!'
                    game.dragon 'Конечно, осмелюсь!'
                    call lb_fear_plains_ogre from _call_lb_fear_plains_ogre_2
        '...да пусть они сами между собой разбираются!':  # Воздержаться от схватки
            game.dragon 'Пожалуй, вам стоит самим решить возникшие разногласия.'
            dark_sister 'Что?!! Ты же...'
            game.rape.elf_girl '...обещал, что встанешь на...'
            dark_sister '...мою сторону!!!'
            nvl clear
            game.dragon.third 'На миг дракону захотелось подшутить.'
            game.dragon.third 'Но он понимал, что это будет {color=#ff0000}смертельно опасно{/color}.'
            menu:
                'Промолчать {color=#00ff00}(абсолютно безопасно){/color}':
                    game.dragon 'Эээ...'
                    dark_sister 'Впрочем...'
                    game.rape.elf_girl '...неважно! Я...'
                    dark_sister '...разберусь с тобой...'
                    game.rape.elf_girl '...после неё!!!'
                    hide bg
                    hide fg
                    show expression 'img/scene/fear/plains/fight.jpg' as bg
                    nvl clear
                    'Противницы сошлись в жестокой схватке.'
                    'Звенят мечи, сверкают магические вспышки, и никто не может взять верх.'
                    '[game.dragon.fullname], усевшись в сторонке, с интересом наблюдает за боем. Ему кажется, что чего-то отпределённо не хватает... точно! Вздувшихся от жара зёрен кукурузы!'
                    de_Ad 'И вот так всё время...'
                    nvl clear
                    'У зрелища появляется ещё один зритель - невероятно усталый и грустный маркиз де Ад.'
                    game.dragon 'Что, тяжело с ней?'
                    de_Ad 'Не то слово! Когда-то я её любил без памяти, а теперь ежечасно мечтаю избавиться.'
                    $ text = u'В решающей битве %s не встал ни на чью сторону, взяв на себя роль зрителя. В ходе напряжённой и жестокой дуэли %s и Тёмная сестра убили друг друга.\n\n' %(game.dragon.name,game.rape.kind_girl.name)
                    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
                    $ game.chronik.write_image('img/scene/fear/plains/elf_dead.jpg',game.dragon.level,game.girl.girl_id)
                    $ game.chronik.death('deAd_elf_loose','img/scene/fear/plains/after_fight.jpg')
                    hide bg
                    nvl clear
                    show expression 'img/scene/fear/plains/after_fight.jpg' as bg
                    'Силы оказались равны - на каменные плиты пола упало два бездыханных тела.'
                    game.dragon 'Хорошо представление! Самому, что ли, такие соревнования в логове устраивать?'
                    de_Ad 'Ну вот и всё. Она мерта. Она наконец-то мертва...'
                    'В голосе маркиза облегчение переплетается с грустью. Видимо, он всё-таки любил свою беспутную жёнушку.'
                    if game.rape.kind_alive:
                      call lb_fear_plains_free from _call_lb_fear_plains_free_2
                    elif not game.rape.kind_alive:
                      call lb_fear_plains_unfortune from _call_lb_fear_plains_unfortune_3
                'Пошутить {color=#ff0000}(смертельно опасно){/color}': # Дракон погибает
                    if game.rape.kind_alive:
                      $ text = u'Альва и Тёмная сестра объединились и убили дракона. Судьба их пленницы неизвестна, но, вероятно, печальна. \n\n' 
                      $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
                      $ game.chronik.write_image('img/scene/fear/plains/bdsm.jpg',game.dragon.level,game.girl.girl_id-1)
                      $ game.chronik.live('deAd_bdsm','img/scene/fear/plains/bdsm.jpg')
                    $ text = u'%s объединилась с Тёмной сестрой и убила дракона. Её дальнейшая судьба неизвестна.\n\n' 
                    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
                    $ game.chronik.live('deAd_elf_madness','img/scene/fear/plains/elf_madness.jpg')
                    '[game.dragon.name] пожимает хвостом.'
                    game.dragon 'Что поделаешь, у меня хроническое спиннокинжальное расстройство!'
                    '[game.rape.elf_girl.name] и Тёмная сестра многозначительно переглядываются...'
                    game.rape.elf_girl 'В таком случае...'
                    dark_sister 'Мы сперва покончим с тобой!'
                    hide fg
                    hide bg
                    nvl clear
                    show expression 'img/scene/fight/dark_sister.jpg' as bg
                    'Тёмная сестра обнажает меч.'
                    game.dragon 'Эй, эй! Так нечестно!'
                    '[game.dragon.fullname] пытается совершить манёвр бег... тактического отступления, но [game.rape.elf_girl.name] преграждает ему путь.'
                    show expression 'img/scene/fear/plains/elf.png' as elf
                    game.rape.elf_girl 'Сражайся и умри, как мужчина!'
                    game.dragon 'Двое на одного? Я так не играю!'
                    'Тёмная сестра искренне и самозабвенно хохочет.'
                    show expression 'img/scene/fear/plains/zombie.png' as zombie
                    dark_sister 'Двое?! Неужели ты забыл про моих маленьких зомбяшек?'
                    'В зал влетает целая толпа зомби. Положение дракона становится отчаянным: Тёмная сестра, альва, нежить... он просто не справляется с таким количеством противников.'
                    game.dragon 'Ничего... Когда я... победю... моя мстя... будет... страшна!!!'
                    dark_sister 'Неужели ты думаешь, что это всё? Жалкий глупец!'
                    show expression 'img/scene/fear/plains/guard.png' as guard
                    pause 5.0
                    nvl clear
                    'В зал влетает замковая стража и добивает обессилевшего ящера.'
                    'В последний миг перед смертью в его голове всплывает абсурдная мысль.'
                    game.dragon.third 'Кажется, это плохой конец...'
                    $ game.dragon._alive=False
                    if freeplay:
                      jump lb_game_over
    return

label lb_fear_plains_ogre:   # Дракон получает огршу
    hide bg
    show expression 'img/scene/fear/plains/ogre.jpg' as bg
    pause 5.0
    game.dragon 'Ой...'
    game.dragon 'Ну не отступать же! Великанши на дороге не валяются.'
    $ description = game.girls_list.new_girl('ogre',tres=False)
    $ text = u' %s попала в замок маркиза де Ада и была обречена на жестокие и смертельные эксперименты. Но когда замок  посетил %s, её судьба круто изменилась. Кажется, теперь у неё будет больше СНУ-СНУ! \n\n' % (game.girl.name, game.dragon.fullname)
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    nvl clear
    game.girl.third "[description]"
    call lb_nature_sex from _call_lb_gigant_sex_5 
    return

label lb_fear_plains_elf_help:         # Окончательный выбор судьбы альвы
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/elf_dragon.jpg' as bg
    '[game.rape.elf_girl.name] испуганно наблюдает за приближающимся драконом. [game.dragon.fullname] ненадолго задумывается.'
    menu:
        'Казнить за ложь' if game.rape.elf_lie:
            game.dragon 'Тебе не следовала лгать мне.'
            game.rape.elf_girl 'Но я...'
            hide bg
            nvl clear
            show expression 'img/scene/fear/plains/elf_dead.jpg' as bg
            'Не слушая никаких оправданий, [game.dragon.name] одним движением убивает лживую гадину.'
            $ text = u'Врать дракону - не самая лучшая идея. %s убил лживую гадину, не слушая никаких оправданий.\n\n' %(game.dragon.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            $ game.chronik.death('deAd_elf_dead','img/scene/fear/plains/elf_dead.jpg')
            if game.rape.kind_alive and not game.rape.kind_prison: # Ведьма жива и свободна
              game.rape.kind_girl.third '[game.rape.kind_girl.name] грустно вздыхает.'
              game.rape.kind_girl 'Это было сурово, но необходимо'
              call lb_fear_plains_final from _call_lb_fear_plains_final_2
            elif game.rape.kind_alive and game.rape.kind_prison:  # Ведьма жива и в темнице
              call lb_fear_plains_free from _call_lb_fear_plains_free_3
            elif not game.rape.kind_alive:  # Ведьма мертва
              call lb_fear_plains_unfortune from _call_lb_fear_plains_unfortune_4
        'Казнить за сломанную игрушку' if game.rape.kind_chocked:
            game.dragon 'Тебе не следовала ломать мою игрушку.'
            game.rape.elf_girl 'Но я...'
            hide bg
            nvl clear
            show expression 'img/scene/fear/plains/elf_dead.jpg' as bg
            'Не слушая никаких оправданий, [game.dragon.name] одним движением убивает наглую душительницу.'
            $ text = u'Уничтожать что-то, что дракон считает своим - не самая лучшая идея. %s убил наглую душительницу, не слушая никаких оправданий.\n\n' %(game.dragon.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            $ game.chronik.write_image('img/scene/fight/elf_dead.jpg',game.dragon.level,game.girl.girl_id)
            $ game.chronik.death('deAd_elf_dead','img/scene/fear/plains/elf_dead.jpg')
            call lb_fear_plains_unfortune from _call_lb_fear_plains_unfortune_5
        'Ещё одна пленница мне не помешает...':
            $ text = u'%s забрал альву в качестве законного трофея.\n\n' %(game.dragon.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            game.dragon.third '[game.dragon.name] смотрит на совершенное тело альвы и похотливо облизывается.'
            if game.rape.kind_alive and not game.rape.kind_prison: # Ведьма жива и свободна
              game.rape.kind_girl.third '[game.rape.kind_girl.name] стыдливо опускает глаза.'
              game.rape.kind_girl 'Я... я понимаю. Это отвратительно, но [game.rape.kind_girl.name] заслужила этого. Я подожду в коридоре, ладно?'
            call lb_nature_sex from _call_lb_nature_sex_43 
            python:
                if not renpy.music.is_playing():
                  renpy.music.play(get_random_files('mus/darkness'))
            if game.rape.kind_alive and not game.rape.kind_prison: # Ведьма жива и свободна
              call lb_fear_plains_final from _call_lb_fear_plains_final_3
            elif game.rape.kind_alive and game.rape.kind_prison:  # Ведьма жива и в темнице
              call lb_fear_plains_free from _call_lb_fear_plains_free_4
            elif not game.rape.kind_alive:  # Ведьма мертва
              'Слуги уже растащили множество ценных вещиц, но кое-что досталось и дракону:'
              call lb_fear_plains_rob from _call_lb_fear_plains_rob_6
              call lb_fear_plains_deAd from _call_lb_fear_plains_deAd_3 
        'Почему бы не продолжить разработку зомби-вируса?':
            game.dragon 'Я принёс тебе лектинополимер маннозы для активации системы комплемента.'
            if game.rape.kind_alive and not game.rape.kind_prison: # Это была ошибка...
              stop music fadeout 2.0
              game.rape.kind_girl 'Нет.'
              $ text = u'Узнав о том, что %s намерен продолжить работу над зомби-вирусом, %s испытала такое потрясение, что умудрилась пробудить свои скрытые силы. Простая деревенская знахарка ценой собственной жизни стала воплощением огня, смертоносным и неостановимым, способным испепелить голема и оттаскать за шкирку ангела. %s сожгла замок и уничтожила все результаты работы над зомби-вирусом. \n\n' %( game.dragon.name, game.rape.kind_girl.name, game.rape.kind_girl.name)
              $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
              $ game.chronik.death('deAd_fire_witch','img/scene/fear/plains/fire_witch.jpg')
              play music "mus/fire.ogg"
              hide bg
              nvl clear
              show expression 'img/scene/fear/plains/fire_rising.jpg' as bg
              pause 3.0
              '[game.rape.kind_girl.name] отшатывается, на её ладонях вспыхивают два слабых огонька'
              game.rape.kind_girl 'Эпидемия убьёт тысячи людей, десятки тысяч! Я не позволю! Не позволю.'
              game.dragon 'И как же ты намерена помешать мне, жалкая букашка? Этот безвредный огонёк даже не нагреет моей чешуи!'
              hide bg
              nvl clear
              show expression 'img/scene/fear/plains/fire_witch.jpg' as bg
              pause 3.0
              'Фигура слабой и беспомощной девушки вспыхивает пламенем. Отчего-то она уже не кажется ни слабой, ни беспомощной.'
              game.rape.kind_girl 'Огнём.'
              game.dragon 'Ой...'
              $ game.foe = Enemy('fire_witch', game_ref=game)
              $ narrator(show_chances(game.foe))
              game.dragon.third 'Это уже не огонь, это плазма какая-то. А чем можно нарушить стабильность плазменных сгустков? Электромагнитными полями, акустическими волнами, антиэнтропийной магией... кажется, всё.'
              $ game.rape.dragon_win=True
              menu:
                  'Ничего, прорвусь! ...наверное...':
                      'Терзаемый дурными предчувствиями, [game.dragon.fullname] вступает в бой.'
                  'Пожалуй, следует проявить благоразумие':
                      '[game.dragon.fullname] пытается позорно скрыться с поля боя.'
                      game.rape.kind_girl 'Я тебя не отпускала.'
                      'Пламя, как живое, окружает дракона со всех сторон, перекрывая ему пути к отступлению. Бой неизбежен!'
              call lb_fight(skip_fear=True) from _call_lb_fight_86
              if not game.rape.dragon_win:
                return
              nvl clear
              '[game.dragon.name] и [game.rape.elf_girl.name] вырвались из ловушки огненной ведьмы и сбежали из обречённого замка.'
              if not freeplay:
                call lb_achievement_acquired from _call_lb_achievement_acquired_2
              hide bg
              nvl clear
              show expression 'img/scene/fear/plains/castle/castle_st1.jpg' as bg
              'Без сил упав на землю, они с замиранием сердца следили за происходящим. '
              call lb_fear_plains_fire from _call_lb_fear_plains_fire_1
              hide bg
              nvl clear
              show expression 'img/scene/fear/plains/elf_dragon.jpg' as bg
              'Дрожа от пережитого ужаса, [game.rape.elf_girl.name] всё теснее и теснее вжималась в чешую дракона.'
              'Альва обнимала чудовищного ящера с такой страстью, как будто он был её единственным защитником, единственной опорой в рухнувшем мире. '
              game.rape.elf_girl 'Пожалуйста... возьми меня... сожри меня... только избавь от этого ужаса!!!'
              $ text = u'Когда %s пробудила свои скрытые силы, альве повезло - %s умудрился не только спастись от практически неодолимого врага, но и прихватить с собой ценный трофей.\n\n' %(game.rape.kind_girl.name, game.dragon.name)
              $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
              $ game.rape.elf_girl.willing=True # Добровольно согласна на секс с драконом
              call lb_nature_sex from _call_lb_nature_sex_44
              hide bg
              nvl clear
              show expression 'img/scene/fear/plains/castle/castle_st4.jpg' as bg
              game.dragon.third 'Кажется, в этих руинах меня больше ничего не держит. Хотя место оживлённое, новый замок быстро отстроят.'
              stop music fadeout 5.0
            else:
              call lb_fear_plains_virus from _call_lb_fear_plains_virus              
    return

label lb_fear_plains_defeat:
    $ text = u'Когда %s пробудила свои скрытые силы, альве не повезло - %s уполз прочь, унижаясь и моля о пощаде, только благодаря милости победительницы. К той, что планировала обратить в нежить тысячи человек, %s была не столь милосердна. \n\n' %(game.rape.kind_girl.name, game.dragon.name, game.rape.kind_girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    $ game.chronik.death('deAd_elf_burned','img/scene/fear/plains/elf_burned.jpg')
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/elf_burned.jpg' as bg
    'Когда [game.dragon.name]  убежал, [game.rape.elf_girl.name] осталась один на один с огненной ведьмой.'
    'Вот только [game.rape.kind_girl.name] не стала проявлять милосердие к той, что собиралась обратить в нежить тысячи человек. Перед смертью альва познала огненную муку.'
    'А вот дракону повезло - он вырвался из ловушки огненного замка.'
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/castle/castle_st1.jpg' as bg
    'Упав на землю, полумёртвый ящер потрясённо следил за происходящим.'
    call lb_fear_plains_fire from _call_lb_fear_plains_fire_2
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/castle/castle_st4.jpg' as bg
    game.dragon.third 'Как-то неудачно всё вышло. Пленниц нет, сокровищ нет, вируса нет, населена големами... Тьфу! При чём тут големы? Уже мысли путаться стали!'
    game.dragon.third 'Надеюсь, в следующий раз мне повезёт больше. Место оживлённое, новый замок быстро отстроят.'
    stop music fadeout 5.0
    return

label lb_fear_plains_fire:
    '[game.rape.kind_girl.name] явно вошла во вкус и решила не останавливаться, пока гнездо порока не будет стёрто с лица земли.'
    'Во многих местах замка начали разгораться пожары. Тушить их явно было бесполезно.'
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/castle/castle_st2.jpg' as bg
    'Люди в панике ринулись наружу, крича и топча друг друга.'
    'Чувствовалось, что огненная ведьма не хочет лишних жертв. Огонь практически не трогал людей, но они с успехом истребляли друг друга сами. Паника - страшная вещь. '
    'А вот зомби везло меньше - огонь, казалось, специально охотился за не-мёртвыми.'
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/castle/castle_st3.jpg' as bg
    'А когда люди наконец-то покинули замок, он вспыхнул весь, внезапно, как восковая свеча. И в низком гудении огня растворялась жизнь простой человеческой женщины, отдавшей самоё себя ради спасения других.'
    game.dragon 'Мдя... Если в землях Вольных найдётся хоть пяток таких монстров, Армия Тьмы испарится как прошлогодний снег.'
    game.dragon 'В прямом смысле слова испарится.'
    return

label lb_fear_plains_virus:   # Начата разработка вируса
    game.rape.elf_girl 'Отлично! Теперь хотелось бы ещё найти ценную живую подопытную...'
    if game.rape.kind_alive and game.rape.kind_prison:   # Ведьма жива и в цепях.
      game.dragon 'Сестра главной исследовательницы - подойдёт?'
      game.rape.elf_girl 'Как нельзя лучше. Веди!'
      hide bg
      nvl clear
      show expression 'img/scene/fear/plains/bdsm.jpg' as bg
      '[game.rape.kind_girl.name] истово молится.'
      game.rape.kind_girl 'Если и я пойду долиной смертной тени, не убоюсь я зла, потому что Ты со мной...'
      game.rape.elf_girl 'Ну что, милочка, готова поучавствовать в одном научном эксперименте? '
      '[game.rape.kind_girl.name] осекается и с ужасом смотрит на приближающихся дракона и альву.'
      game.rape.kind_girl 'Нет, нет, только не это, нет...'
      game.rape.elf_girl 'Не беспокойся, больно не будет. Будет невыносимо больно. Но зато твоя жизнь усилит грядущую эпидемию!'
      game.rape.kind_girl 'НЕЕЕЕТ!!!'
      'В крике пленницы не осталось ничего человеческого. Но не из-за грядущих мук - а от того, что совсем скоро тысячам невинных предстоит обратится в нежить. И она никак, никак не может этого изменить.'
      hide bg 
      show expression 'img/scene/fear/plains/bdsm_death.jpg' as bg
      $ text = u'Пленнице не повезло - %s убил Тёмную сестру и полность встал на сторону альвы. %s послужила материалом для жестоких и бесчеловечных экспериментов, в результате которых зомби-эпидемия обрела внушительную мощь. \n\n' %(game.dragon.name,game.rape.kind_girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
      $ game.chronik.death('deAd_bdsm_death','img/scene/fear/plains/bdsm_death.jpg')
      'В лаборатории идёт спокойная и кропотливая работа.'
      nvl clear
      game.rape.elf_girl.third 'Иглы в точки 7, 13 и 17.'
      play sound get_random_file("sound/pain")
      nvl clear 
      game.dragon.third 'Сделано. Поверни пятый ворот на три деления.'
      nvl clear
      play sound get_random_file("sound/pain")
      game.rape.elf_girl.third 'Да, ты прав. По кубику раствора алмазной пыли в молочные железы и два кубика в мочевой пузырь.'
      nvl clear 
      play sound get_random_file("sound/pain")
      game.dragon.third 'Это же сколько добра на неё переводим!'
      nvl clear
      game.rape.elf_girl.third 'Всё ради мести человечеству!!! Толчёное стекло не подходит для наложения заклинаний.'
      play sound get_random_file("sound/pain")
    elif not game.rape.kind_alive:
      game.dragon 'Хотелось бы, да где же её взять?!'
      game.rape.elf_girl 'Жаль, жаль... Ничего, обойдёмся с тем, что есть!'
    hide bg
    hide fg
    nvl clear
    show expression 'img/scene/fear/plains/laboratory.jpg' as bg
    show expression 'img/scene/fear/plains/alchemist.png' as fg  
    game.rape.elf_girl 'Так, так, ещё пара минут...'
    'Пока альва занята работой, [game.dragon.name] подчищает сокровища, которые не успели растащить слуги:'
    call lb_fear_plains_rob from _call_lb_fear_plains_rob_7
    game.rape.elf_girl 'Всё!'
    if game.rape.kind_alive and game.rape.kind_prison:   # Ведьма жива и в цепях.
      game.rape.elf_girl 'У нас получился очаровательный зомби-вирус, распространяющийся воздушно-капельным, трансмиссивным, алиментарным и половым путём, с инкубационным периодом от получаса до двух недель и с девяностопроцентной летальностью!'
      game.rape.elf_girl 'Обещаю: не пройдёт и года, как разруха в стране серьёзно возрастёт!'
      $ game.poverty.value += 3
    elif not game.rape.kind_alive:
      game.rape.elf_girl 'У нас получился очаровательный зомби-вирус, распространяющийся воздушно-капельным, трансмиссивным и половым путём, с инкубационным периодом от двух часов до одной недели и с шестидесятипроцентной летальностью!'
      game.rape.elf_girl 'От такого удара разруха скоро возрастёт!'
      $ game.poverty.value += 2
    'Дракон довольно урчит'
    game.dragon 'А я посмотрррю...'
    game.rape.elf_girl 'Боюсь - не получится. Пик эпидемии придётся на время твоего сна. А к следующему году Вольные уже найдут лекарство.'
    '[game.dragon.fullname] серьёзно ошарашен.'
    game.dragon 'Как - лекарство?'
    game.rape.elf_girl 'Да очень просто. Люди воззовут к ангелом, те даруют смертным какой-нибудь "Ангедол"... Чтобы создать по-настоящему неизлечимую болезнь, необходимы сосвсем иные усилия!'
    $ text = u'%s приняла помощь дракона и создала зомби-вирус, который опустошил несколько провинций и поднял разруху в стране. Завершив дело своей жизни, альва добровольно отдалась дракону.\n\n' %(game.rape.elf_girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    hide bg
    hide fg
    nvl clear
    show expression 'img/scene/fear/plains/some_love.jpg' as bg
    'Тон альвы изменяется, вместо восторженного-делового он становится тягучим и томным. Девушка интимно прижимается к дракону.'
    game.rape.elf_girl 'А пока я хотела бы получить достойную награду за свои труды.'
    game.dragon 'И что же ты считаешь достойной наградой?'
    'Голос ящера становится откровенно похотливым.'
    game.rape.elf_girl 'Немного любви...'
    $ game.rape.elf_girl.willing=True # Добровольно согласна на секс с драконом
    stop music fadeout 5.0
    call lb_nature_sex from _call_lb_nature_sex_45
    return

label lb_fear_plains_free:   # Освобождение ведьмы
    game.dragon 'Вроде, всё... А, нет, не всё!'
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/bdsm.jpg' as bg
    '[game.dragon.fullname] возвращается к пленнице.'
    '[game.rape.kind_girl.name] истово молится.'
    game.rape.kind_girl 'Если и я пойду долиной смертной тени, не убоюсь я зла, потому что Ты со мной...'
    game.dragon 'Скучаешь?'
    game.rape.kind_girl 'Ты... вернулся? Сестра мертва? [game.rape.elf_girl.name] обезврежена?'
    game.dragon 'Ну, да.'
    game.rape.kind_girl 'Я знала! Я знала, что это всего лишь трюк, уловка, военная хитрость!'
    'Сбитый с толку женской логикой, [game.dragon.name] освобождает пленницу.'
    $ text = u'Пленнице повезло - убив Тёмную сестру и разобравшись с альвой, %s освободил ведьму. \n\n' %(game.dragon.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
    call lb_fear_plains_final from _call_lb_fear_plains_final_4
    return

label lb_fear_plains_final:   # Разбираемся с ведьмой
    $ game.girl=game.rape.kind_girl
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/final.jpg' as bg
    '[game.rape.kind_girl.name] счастливо и облегчённо вздыхает.'
    game.rape.kind_girl 'Всё... Теперь всё позади...'
    '[game.dragon.fullname] склоняется над ведьмой.'
    menu:
        'Избавлюсь, а то надоела хуже пережареного мяса!':
            game.dragon 'Для тебя теперь точно всё позади!'
            hide bg
            nvl clear
            show expression 'img/scene/fear/plains/kind_eat.jpg' as bg
            $ text = u'Однако история закончилась трагически: %s страшно надоела дракону, и он убил её при первой же попавшейся возможности. \n\n' %(game.rape.kind_girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
            $ game.chronik.death('deAd_kind_eat','img/scene/fear/plains/kind_eat.jpg')
            if game.dragon.hunger > 0:
              $ description =  game.girls_list.eat_girl()
              '[game.dragon.name] с удовольствием подзакусил рыжей ведьмой.'
            else:
              '[game.dragon.name] разодрал рыжую ведьму на части просто ради забавы.'
            call lb_fear_plains_unfortune from _call_lb_fear_plains_unfortune_6
        'Хоть и невелика добыча, но лучше, чем ничего!' if game.rape.kind_girl.virgin:
            game.dragon 'Ну не совсем позади... ты-то ещё пригодна к вынашиванию отродий!'
            $ text = u'Однако история закончилась не очень хорошо: %s досталась дракону в качествве законного трофея.\n\n' %(game.rape.kind_girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
            call lb_nature_sex from _call_lb_nature_sex_46
            'Закончив с первоочередными делами, [game.dragon.name] дограбил сокровища, которые не успели растащить слуги:'
            call lb_fear_plains_rob from _call_lb_fear_plains_rob_8
            call lb_fear_plains_deAd from _call_lb_fear_plains_deAd_4
        'Пусть катится на все четыре стороны!':
            game.dragon 'Действительно, всё позади. И это приключение было весьма интересным!'
            if game.rape.kind_ill:
              '[game.rape.kind_girl.name] мрачнеет.'
              game.rape.kind_girl 'Жаль только, что для меня всё кончено. Я больна неизлечимой болезнью и скоро превращусь в зомби.'
              game.rape.kind_girl 'Пожалуйста, выполни мою просьбу. Убей меня!'
              menu:
                  'Эдакая малость!':
                      game.dragon 'Да запросто!' 
                      hide bg
                      nvl clear
                      show expression 'img/scene/fear/plains/kind_eat.jpg' as bg
                      $ text = u'Однако история закончилась трагически: болезнь ведьмы никуда не делась. %s попросила ящера убить её, и %sс удовольствием выполнил её просьбу. \n\n' %(game.rape.kind_girl.name, game.dragon.name)
                      $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
                      $ game.chronik.death('deAd_kind_eat','img/scene/fear/plains/kind_eat.jpg')
                      if game.dragon.hunger > 0:
                        $ description =  game.girls_list.eat_girl()
                        '[game.dragon.name] с удовольствием выполнил просьбу рыжей ведьмы и подзакусил её аппетитным тельцем.'
                      else:
                        '[game.dragon.name]  удовольствием выполнил просьбу рыжей ведьмы и разодрал на части её нежное тельце.'
                      call lb_fear_plains_unfortune from _call_lb_fear_plains_unfortune_7
                  'Может быть, магия поможет?' if game.dragon.mana>0:
                      game.dragon 'Так уж и неизлечимой?'
                      game.dragon 'Великое исцеление Эгеледи!'
                      $ game.dragon.drain_mana()
                      hide bg
                      nvl clear
                      show expression 'img/scene/fear/plains/magic.jpg' as bg
                      'От дракона к ведьме хлынула волна целебной магии.'
                      'Кажется, [game.rape.kind_girl.name] не верит своему счастью.'
                      game.rape.kind_girl 'Я снова здорова! Здорова!!!'
                      $ text = u'Однако история должна  была закончится трагически: болезнь ведьмы никуда не делась, и %s попросила ящера убить её. Однако %s почему-то (наверное, по велению левой передней пятки)  решил сделать доброе дело и излечил женщину с помощью магии.\n\n' %(game.rape.kind_girl.name, game.dragon.fullname)
                      $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
                      call lb_fear_plains_end from _call_lb_fear_plains_end_1
            elif not game.rape.kind_ill:
              call lb_fear_plains_end from _call_lb_fear_plains_end_2
    return

label lb_fear_plains_end:  # Счастливый финал.
    $ text = u'У этой истории оказался счастливый финал: %s отпустил ведьму, а она поддержала  маркиза де Ада в эту трудную для него минуту. Влюблённые отказались от замка и титула и уехали прочь из этих мест. Хочется верить, что у них всё было хорошо. Хоть у них - хорошо... \n\n' %( game.dragon.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id-1)
    $ game.chronik.write_image('img/scene/fear/plains/couple.jpg',game.dragon.level,game.girl.girl_id-1)
    $ game.chronik.live('deAd_couple','img/scene/fear/plains/couple.jpg') 
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/couple.jpg' as bg
    'Кивнув дракону, [game.rape.kind_girl.name] подходит к маркизу де Аду, скромно стоящему в сторонке.'
    game.rape.kind_girl 'Бедненький... Ты натерпелся от моей сестры, да?'
    'Её голос пронизан печалью и сочуввствием.'
    de_Ad 'Да. В самом начале я любил её без памяти, а она не заходила далеко. Но потом всё становилось хуже и хуже.'
    de_Ad 'Я... я не могу понять, что чувствую. Одновременно и сожалею о её смерти, и радуюсь как ребёнок.'
    '[game.rape.kind_girl.name] обнимает мужчину.'
    game.rape.kind_girl 'Ничего. Всё позади. Теперь всё позади.'
    game.rape.kind_girl 'Мы уедем из этого проклятого замка куда-нибудь в глушь, титул...'
    de_Ad 'Я передам его какому-нибудь дальнему родственнику. Кандидатов предостаточно.'
    'За время этой семейной сценки дракон успевает натаскать достаточно сокровищ.'
    call lb_fear_plains_rob from _call_lb_fear_plains_rob_9
    hide bg
    nvl clear
    show expression 'img/scene/fear/plains/end.jpg' as bg
    '[game.rape.kind_girl.name] подходит к дракону и благодарно прижимается к его морде.'
    game.rape.kind_girl 'Спасибо тебе.'
    game.rape.kind_girl 'Вот видишь - добрым и благородным может быть даже кровожадное похотливое безжалостное чудовище.'
    'Сказать, что [game.dragon.name] ошарашен - значит, сильно погрешить против истины.'
    game.dragon 'Так ты знала, что я...'
    game.rape.kind_girl 'Конечно.'
    game.dragon 'Тогда почему...'
    game.rape.kind_girl 'Иногда приходится творить добро из зла, потому что больше его не из чего делать.'
    game.rape.kind_girl 'Я сочла, что единственный способ предотвратить бесчинства - это притвориться. что я верю в твою доброту и благородство. И это сработало.'
    game.rape.kind_girl 'Как видишь, иногда бывает приятно творить добро!'
    '[game.dragon.name] понимает, что ему надо разорвать наглячку на части... и чувствует, что ему совершенно не хочется этого делать.'
    game.dragon 'Пожалуй, ты права. Прощай.'
    game.rape.kind_girl 'Прощай!'
    stop music fadeout 5.0
    return

