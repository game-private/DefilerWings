# coding=utf-8
init python:
    from pythoncode import summon_data

label lb_hope_check:  # Надежда ещё жива?
#    hide bg
    show expression 'img/intro/4.jpg' as fg
    if foe.kind == 'angel' and not game.historical_check('angel_fall'):
      $ game.history = historical(name='angel_fall',end_year=None,desc=None,image=None)
      $ game.history_mod.append(game.history)
      'Ангел, посланник самих Небес, пал перед мощью дракона!'
      'Какая весть может быть горше этой?!'
      call lb_hope_estimate from _call_lb_hope_estimate_1
    if foe.kind == 'golem' and not game.historical_check('golem_fall'):
      $ game.history = historical(name='golem_fall',end_year=None,desc=None,image=None)
      $ game.history_mod.append(game.history)
      'Голем, совершенное творение цвергов, повержен драконом!'
      'Вся сила железа и пара - ничто перед его мощью.'
      call lb_hope_estimate from _call_lb_hope_estimate_2
    if foe.kind == 'treant' and not game.historical_check('treant_fall'):
      $ game.history = historical(name='treant_fall',end_year=None,desc=None,image=None)
      $ game.history_mod.append(game.history)
      'Чащобный страж, любимое чадо альвов, сокрушён нечестивым ящером!'
      'Леса детей Дану никогда не станут прежними.'
      call lb_hope_estimate from _call_lb_hope_estimate_3
    if foe.kind == 'titan' and not game.historical_check('titan_fall'):
      $ game.history = historical(name='titan_fall',end_year=None,desc=None,image=None)
      $ game.history_mod.append(game.history)
      'Титан, величайший из великанов, пал в своём собственном замке!'
      'Перед яростью чудовища бессильны даже гиганты.'
      call lb_hope_estimate from _call_lb_hope_estimate_4
    if foe.kind == 'triton' and not game.historical_check('triton_fall'):
      $ game.history = historical(name='triton_fall',end_year=None,desc=None,image=None)
      $ game.history_mod.append(game.history)
      'Тритон, морской владыка, разорван кровожадным монстром!'
      'Глубины больше не принадлежат морскому народу.'
      call lb_hope_estimate from _call_lb_hope_estimate_5
    hide fg
    return

label lb_hope_estimate:
    $ game.desperate += 1
    if game.desperate == 1:
      'Неужели даже самые могущественные защитники бессильны пред этим исчадием Ада?'
    elif game.desperate == 2:
      'Какая судьба ждёт простых людей, если пало уже два чемпиона?'
    elif game.desperate == 3:
      'Да есть ли хоть кто-то, способный противостоять этому порождению Бездны?!'
    elif game.desperate == 4:
      'Неужели... мы... обречены?'
    elif game.desperate == 5:
      'Надежды нет.'
    return

label lb_summon:
    hide bg
    nvl clear
    show expression get_random_image("img/scene/sacriface") as bg
    python:
        chance = random.randint(1, game.desperate)
        if chance == 1:
            patrool = 'dark_novice'
            dtxt = 'Ученик какого-то тёмного мага пытается принести в жертву демонам крестьянку. Девица кричит и отбивается, ученик краснеет, извиняется и мямлит. Тем не менее, если ему не помешать, он доведёт ритуал до конца.'
        elif chance == 2:
            patrool = 'dark_apprentice'
            dtxt = 'Подмастерье какого-то тёмного мага приносит в жертву демонам горожанку. Парень бледен и напряжён, но преисполнен желания довести ритуал до конца. Похоже, люди принялись за вызов демонов всерьёз.'
        elif chance == 3:
            patrool = 'dark_mage'
            dtxt = 'Тёмный маг спокойно и деловито приносит в жертву демонам девицу благородных кровей. Раз культисты умудряются похищать аристократок, значит, они пользуются негласной поддержкой лордов. По крайней мере, неоторых из них.'
        elif chance == 4:
            patrool = 'dark_magister'
            dtxt = 'При большом скоплении народа тёмный магистр приносит в жертву демонам альву. Учитывая, насколько трепетно ушастые относятся к женщинам своего народа... неужели демонопоклонники завелись даже среди детей Дану? '
        elif chance == 5:
            patrool = 'dark_archmage'
            dtxt = 'Большая толпа народа с интересом наблюдает, как тёмный архимаг приносит в жертву демонам титаниду, находящуюся под заклятием временного уменьшения. Похоже, даже великаны отчаялись в край и губят своих жён и дочерей ради мифического шанса остановить дракона.'
    '[dtxt]'
    $ game.foe = Enemy(patrool, game_ref=game)
    $ narrator(show_chances(game.foe))
    menu:
        'Такая девица нужна самому!':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_87
            if chance == 1:
              $ description = game.girls_list.new_girl('peasant',tres=False)            
            elif chance == 2:
              $ description = game.girls_list.new_girl('citizen',tres=False)
            elif chance == 3:
              $ description = game.girls_list.new_girl('princess',tres=False)
            elif chance == 4:
              $ description = game.girls_list.new_girl('elf',tres=False)
            elif chance == 5:
              $ description = game.girls_list.new_girl('titan',tres=False)
            $ text = u'%s должна была принять смерть на алтаре демонопоклонников. Но в последнюю минуту её спас... нет, не рыцарь, не принц на белом коне, а кровожадный и похотливый дракон. Стала ли её судьба от этого хоть немногим лучше? Вряд ли, но это покажет только время... \n\n' % game.girl.name
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            '[game.dragon.fullname] спасает обречённую жертву.'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_47
        'Пожать хвостом и уйти'if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage() 
            if chance == 1:
              $ game.summon.seal += 1            
            elif chance == 2:
              $ game.summon.seal += 2
            elif chance == 3:
              $ game.summon.seal += 4
            elif chance == 4:
              $ game.summon.seal += 8
            elif chance == 5:
              $ game.summon.seal += 16
            'Ещё одна жертва отдала свою жизнь на алтаре демонопоклонников. Слабеют печати. Близится победа Легиона.'
    return

label lb_archimonde_arrive:  #  Прибытие Архитота
    $ game.history = historical( name='archimonde_was',end_year=None,desc=None,image=None)
    $ game.history_mod.append(game.history)
    hide bg
    nvl clear
    python:
        angel= Talker(game_ref=game)
        angel.avatar = "img/archimonde/angel.jpg"
        angel.name = 'Ангел'
        architot=  Talker(game_ref=game)
        architot.avatar = "img/archimonde/archimonde.jpg"
        architot.name = 'Князь Ада Архитот'
        jasmine= Talker(game_ref=game)
        jasmine.avatar = "img/archimonde/jasmine.jpg"
        jasmine.name = 'Принцесса Фиалка'
        witch = Talker(game_ref=game)
        witch.avatar = "img/avahuman/witch.jpg"
        witch.name = "Ведьма"
        game.summon.battle_init() 
    show expression 'img/archimonde/cuty_fire.jpg' as bg
    if not "archimonde" in persistent.easter_eggs:
      $ persistent.easter_eggs.append("archimonde")
    'Чу! Кажется, в Столице что-то не так.'
#    call lb_archimonde_batlle_st1 from lb_archimonde_batlle_st1_4 
#    call lb_archimonde_end from _call_lb_archimonde_end_1
    'Люди призвали какого-то могущественного демона для борьбы с драконом, а он взял и и атаковал своих призывателей. Какая досада.'
    $ game.poverty.value += 4
    game.dragon 'Слетать в Столицу, что ли?'
    menu:
        'Наблюдать за страданиями людей - это так приятно!':
            game.dragon 'Почему бы и нет? Одно крыло - или что там у меня есть? - там, другое... тоже там.'
            call lb_archimonde_introduce from _call_lb_archimonde_introduce
        'Не, лениво':
            game.dragon 'Да ну их. Лучше ещё немного посплю.'
            'Позже [game.dragon.fullname] узнал, что Князь Ада Архитот разорил Столицу, разметал группу из ангела, голема и титана как котят и уничтожил всю королевскую семью. Только после этого демон соизволил убраться обратно в Ад.'
            'Впрочем, люди, привыкшие к регулярным налётам драконов, отстроили Столицу довольно быстро.'
            nvl clear
            'Больше с призывами демонов они не игрались.'
    return

label lb_archimonde_introduce:
    stop music fadeout 1.0
    $ renpy.music.play(get_random_files('mus/darkness')) 
    nvl clear
    hide bg
    show expression 'img/archimonde/archimonde_intro.jpg' as bg
    $ data.achieve_target("seen", "architot")
    if not freeplay:
      call lb_achievement_acquired from _call_lb_achievement_acquired_3
    'Исполинский демон идёт вперёд, сметая любое сопротивление.'
    'Кажется, ему невозможно противостоять.'
    game.dragon 'Ого, это же Князь Ада Архитот! Он прихлопнет меня как мушку. С ним разве что мама справится, и то не уверен.'
    game.dragon 'Хорошо хоть Князья Ада не могут надолго задерживаться в материальном мире.'
    nvl clear
    hide bg
    show expression 'img/archimonde/archimonde_introduce.jpg' as bg
    pause 60.0
    'Однако Вольные не беззащитны. К Архитоту аккуратно приближаются ангел, голем и титан. Защитники идут вперёд с обречённой решимостью - даже в таком составе шансов на победу над Князем Ада нет.'
    game.dragon 'Я обожаю запах чёрного злорадства по утрам!'
    game.dragon 'Хотя можно помочь Вольным и сразиться с Архитотом... чисто в качестве утренней разминки, разумеется!'
    menu:
        'Устроиться поудобнее и наблюдать':
            game.dragon 'Чего-то не хватает... точно, обжаренных специальным образом зёрен кукурузы!'
            nvl clear
            hide bg
            show expression 'img/archimonde/archimonde_base.png' as bg
            show expression 'img/archimonde/angel.png' as img_angel
            show expression 'img/archimonde/titan.png' as img_titan
            show expression 'img/archimonde/golem.png' as img_golem
            show expression 'img/archimonde/archimonde.png' as img_archimonde
            'Архитот, не обращая внимания на удары, читает какое-то длинное и изощрённое заклятие.'
            nvl clear
            hide bg
            hide img_angel
            hide img_titan
            hide img_golem
            hide img_archimonde
            call lb_death_angel from _call_lb_death_angel
            show expression 'img/archimonde/archimonde_base.png' as bg
            show expression 'img/archimonde/titan.png' as img_titan
            show expression 'img/archimonde/golem.png' as img_golem
            show expression 'img/archimonde/archimonde.png' as img_archimonde
            'Голем и титан бросились на Князя Ада с упорством отчаявшихся.'
            'Архитот улыбнулся.'
            nvl clear
            hide bg
            hide img_titan
            hide img_golem
            hide img_archimonde
            call lb_death_titan from _call_lb_death_titan
            show expression 'img/archimonde/archimonde_base.png' as bg
            show expression 'img/archimonde/golem.png' as img_golem
            show expression 'img/archimonde/archimonde.png' as img_archimonde
            'Оставшись в одиночестве, голем продолжил стоять, как каменная глыба.'
            'Впрочем, это ему не помогло.'
            nvl clear
            hide bg
            call lb_death_golem from _call_lb_death_golem
            show expression 'img/archimonde/archimonde_base.png' as bg
            'После гибели последнего защитника уже ничто не стояло между Архитотом и горящим городом.'
            'Князь Ада легко догоняет убегающую девушку. Судя по запаху - принцессу, к тому же и девственницу.'
            nvl clear
            hide bg
            show expression 'img/archimonde/jasmine_captured.jpg' as bg
            'Пленница пинается и брыкается, но ничего, ничего не может поделать.'
            'Архитот проходит через портал, унося с собой обречённую принцессу. Можно только гадать, для чего демон утащил её живьём в Ад.'
            'Но явно не для светских бесед и торжественных раутов.'
            game.dragon 'Пожалуй, это будет для людей уроком. Теперь они вряд ли когда-нибудь станут вновь призывать демонов.'
            game.dragon 'Ну а Столица... её быстро отстроят!'
        'Аккуратно вмешаться, не рискуя собственной жизнью':
            game.dragon 'А сражусь-ка я с Архитотом... не для защиты Вольных, разумеется - а чисто из спортивного интереса! В случае чего всегда сбежать успею.'
            game.dragon 'Эй, светлые! Помощь нужна?'

            angel 'Сгинь, гнусное порождение безд...'
            'Ангел осекается, повинуясь лёгкому взмаху изящной девичьей ручки.'
            nvl clear
            hide bg
            show expression 'img/archimonde/jasmine_intro.jpg' as bg 
            jasmine 'Хм-хм.'
            game.dragon.third '[game.dragon.name] поневоле засмотрелся на девицу. Точёный стан, коса до пояса, алые губки, выразительные глазки, огненный нрав... Прелесть, просто прелесть.'
            game.dragon.third 'Так бы и вдул!'
            jasmine 'Сэр Ангел, чем закончится битва?'
            angel 'Ваше высочество, мы готовы бороться до последнего...'
            'Принцесса Фиалка спокойно прерывает посланника Небес.'
            jasmine '...и бессмысленно сдохнуть, утянув за собой всю Столицу. Я уже поняла. Сейчас вы можете лишь продержаться чуть-чуть подольше, дав горожанам шанс на спасение.'
            jasmine 'Поэтому мы примем помощь дракона.'
            angel 'Ваше Высочество, вы не понимаете! [game.dragon.fullname] - кровожадное и блудливое чудовище, наслаждающееся болью и страданием невинных жертв!'
            game.dragon 'Ага.'
            '[game.dragon.fullname] внимательно изучает принцессу Фиалку плотоядно-похотливым взглядом.'
            jasmine 'Ну и что он сделает? Потребует за помощь пол-Королевства и принцессу впридачу?!'
            jasmine 'По Королевству он и так шастает, как у себя дома, а принцесса, хвала Небесному Отцу, в наличии.'
            angel 'Но...'
            jasmine 'Именем древних клятв! Кровью своей и наследием! Как последняя выжившая из рода! Приказываю: повинуйся, слуга!'
            jasmine 'Пусть моё правление будет самым  коротким в истории, но это будет моё правление.'
            angel 'Как прикажите, Ваше Высочество.'
            if game.dragon.health < 2:
              jasmine 'Кстати, [game.dragon.name], у тебя вид какой-то нездоровый. Прими лечебное зелье.'
              'Принцесса кидает дракону маленький красный флакончик. [game.dragon.name] с настороженно нюхает его содержимое, а потом осторожно трогает жидкость языком.'
              $ game.dragon.health = 2
              nvl clear
              game.dragon.third 'Раны затянулись. Ну почему самые нужные вещи появляются только в самых опасных ситуациях, а?!'
            hide bg
            nvl clear
            show expression 'img/archimonde/archimonde_intro.jpg' as bg
            'Князь Ада Архитот, до этого снисходительно прислушивавшийся к разговору, вновь пошёл вперёд.'
            game.dragon.third 'Что же делать?!'
            call lb_archimonde_decision1 from _call_lb_archimonde_decision1_1
    return

label lb_archimonde_decision1:
    menu:
        'Можно позвать на помощь маму...' if game.summon.mistress_help:
            $ game.summon.mistress_help=False
            game.dragon 'Мама, у нас проблемы!'
            mistress 'Архитот... Старый, старый враг. И очень могущественный. Я рада, что снова сойдусь с ним лицом к лицу.'
            mistress 'Жаль только, что ты позвал меня слишком рано. Я смогу лишь слегка раздразнить его.'
            mistress 'А теперь... почувствуй ярость Тёмной Госпожи!'
#            $ renpy.movie_cutscene("mov/kali.webm")
            $ renpy.music.play(get_random_files('mus/darkness'))
            call lb_archimonde_decision2 from _call_lb_archimonde_decision2_1
        '...хотя лучше обойтись своими силами...':
            game.dragon 'Только не говорите, что у вас нет плана!'
            'Архитот временно прекращает атаки и прислушивается. Кажется, этот вопрос его тоже интересует.'
            hide bg
            nvl clear
            show expression 'img/archimonde/jasmine_discuss.jpg' as bg
            'Принцесса Фиалка обворожительно улыбается.'
            jasmine 'Есть, есть, не беспокойся. Но тут всё зависит от твоих способностей, [game.dragon.fullname]!'
            jasmine 'Если ты хорошо защищён, то можешь стать танком и принимать на себя основные удары Архитота.'
            jasmine 'Но для этого у тебя должна быть крепкая броня... эээ... чешуя, надёжный щит... хм... надёжные рога. Ну и размер побольше.'
            jasmine 'Если же ты искусно владеешь магией, то сможешь стать целителем и лечить всю группу.'
            jasmine 'Но для этого действительно нужно много маны.'
            jasmine 'Ну и во всех остальных случаях ты будешь бойцом. Постарайся бить врага как можно сильнее и выживать как можно дольше. Как-то так.'
            'Принцесса Фиалка опускает глаза.'
            jasmine 'Ну... в настольных ролевых играх это всегда срабатывало!'
            call lb_archimonde_batlle_st1 from lb_archimonde_batlle_st1_1
        '...а ещё лучше - бежать поджав хвост!':
            call lb_archimonde_retreat from _call_lb_archimonde_retreat_1
        
    return

label lb_archimonde_retreat:
    game.dragon 'Извините, мне пора! Дела не ждут. Всего наилучшего!'
    hide bg
    nvl clear
    show expression 'img/archimonde/city_burn.jpg' as bg 
    'Позже [game.dragon.fullname] узнал, что Князь Ада Архитот открыл портал для своего Легиона, и демоны опустошили Столицу. Принцессу Фиалку больше никто и никогда не видел.'
    'Впрочем, люди, привыкшие к налётам драконов, отстроились довольно быстро.'
    return

label lb_archimonde_batlle_st1:
    menu:
        'Меня не страшат удары врага!':
            python:
                game.summon.tank_list=['dragon']
                game.summon.dd_list=['titan','golem']
                game.summon.healer_list=['angel']
                game.summon.dragon='tank'
            game.dragon 'Танком буду я! Фиалка, я сделаю всё, чтобы ты не досталась Архитоту.'
            game.dragon 'А досталась мне!'
            jasmine 'Без проблем. Если тебе нужны советы по тактике - спрашивай!'
        'Нападение - вот лучшая защита!':
          if len(summon_data.fighters['dragon']['attack'])==0 and game.summon.dd_approve:
            angel 'Ты самого Архитота хоть чем-нибудь поцарапать сможешь, гер-рой?'
            game.dragon 'Эээ... нет, не думаю.'
            jasmine 'Тогда, возможно, тебе стоит выбрать иную роль?'
            $ game.summon.dd_approve=False
            call lb_archimonde_batlle_st1 from lb_archimonde_batlle_st1_3
            return
          else:
            python:
                game.summon.tank_list=['titan']
                game.summon.dd_list=['dragon','golem']
                game.summon.healer_list=['angel']
            game.dragon 'Защита - не для меня. Только атакуя, я дам волю своей ярости! '
            jasmine 'Как я и думала, в настолках этот класс очень популярен. Если тебе нужны советы по тактике - спрашивай!'
        'Никогда не был целителем. Надо попробывать!':
            python:
                game.summon.tank_list=['titan']
                game.summon.dd_list=['angel','golem']
                game.summon.healer_list=['dragon']
            game.dragon 'Лечение других - вот моё истинное призвание!'
            game.dragon 'Только скрытое. Очень хорошо скрытое.'
            angel 'Чтобы я ещё хоть раз хоть когда-нибудь связался с этим отродьем бездны...'
            'С горьким вздохом ангел подходит и возлагает руки на голову дракона.'
            angel 'Обращаю тебя к Свету. Отринь Тьму, защити Свет. Даю тебе взор отличать Добро от Зла. Даю тебе веру идти за Светом. Даю тебе отвагу сражаться с Тьмой. Свет с тобой!'
            game.dragon 'И не подумаю!'
            jasmine 'Да это чистая формальность, чтобы ты мог лечить других. Если тебе нужны советы по тактике - спрашивай!'
        'А что такое "танк"?' if not game.summon.tank_known:
            $ game.summon.tank_known=True
            game.dragon '"Боец" - понятно. "Целитель" - понятно. Но "танк" - что это вообще такое?!'
            'Принцесса Фиалка стыдливо потупила глаза.'
            jasmine 'Ну... это термин из настолок. В смысле, настольных ролевых игр. Паровый танк - это машина цвергов, мощная, практически неузвимая, способная стянуть вражеский огонь на себя и прикрыть любое количество бойцов!'
            show expression 'img/archimonde/tank.png' as tank_img
#            pause 3.0
            nvl clear
            game.dragon.third '[game.dragon.fullname] в ужасе представляет бессчётную армаду неуязвимых паровых машин.'
            game.dragon 'Настоящая?!'
            'Фиалка смотрит на дракона как на идиота.'
            jasmine 'Разумеется, выдуманная! Говорю же - термин из настолок.'
            hide tank_img
            game.dragon 'Уф.'
            call lb_archimonde_batlle_st1 from lb_archimonde_batlle_st1_2
            return
    $ game.summon.battle_st1()
    if not game.summon.live['dragon']: # Дракон повержен
      return   # Приддставление закончилось
    call lb_archimonde_decision2 from _call_lb_archimonde_decision2_2

#    'Битва выиграна'
    return

label lb_archimonde_talk:
    architot '[game.summon.talk]' 
    nvl clear
    return

label lb_death_angel:
    nvl clear
    show expression 'img/archimonde/death_angel.jpg' as fg
    'Ангела выгибает дугой, из его рта вырывается дикий крик.'
    'Почерневшая фигура в потоке неестественного света возносится на небеса.'
    nvl clear
    hide fg
    return

label lb_death_titan:
    nvl clear
    show expression 'img/archimonde/death_titan.jpg' as fg
    'Титан перешёл в ближний бой, но Архитот забил великана голыми руками.'
    'Вскоре в невнятном месиве нельзя было опознать некогда гордую и величественную фигуру.'
    nvl clear
    hide fg
    return

label lb_death_golem:
    nvl clear
    show expression 'img/archimonde/death_golem.jpg' as fg
    'Шедевр цвергов сражался до последнего. Лишившись ног и половины тела, он ещё пытался куда-то ползти и что-то делать.'
    'Бесполезно.'
    nvl clear
    hide fg
    return

label lb_death_dragon:  
    nvl clear
    '[game.dragon.fullname] без сил валится наземь.'
    nvl clear
    hide bg
    show expression "img/archimonde/black.jpg" as bg
    pause 3.0
    game.dragon 'Что?..'
    game.dragon 'Я жив?'
    hide bg
    show expression "img/archimonde/city_ruined.jpg" as bg
    game.dragon 'Кажется, Князь Ада не стал меня добивать...'
    'А вокруг - ни защитников, ни демонов, ни Архитота. Ни принцессы Фиалки.'
    game.dragon 'Жаль: девочка досталась демонам.'
    game.dragon 'Я бы оприходовал её с куда большей пользой!'
    'Вокруг - лишь безжизненные руины.'
    'Впрочем, Вольные наверняка отстроют Столицу крайне быстро!'
#    $ renpy.pop_return()
    game.dragon 'Ладно, пойду ещё чуток подремлю'
    return

label lb_clear:
    nvl clear
    return

label lb_screen_archimonde_main:
    call screen archimonde_main
    return

label lb_dragon_att_archimonde:
    hide bg
    nvl clear
    show expression "img/archimonde/archimonde_intro.jpg" as bg
    python:
      ratio=game.summon.hp['architot']/summon_data.archimonde['max_hp']
      if ratio>=1.0:
        mood='{color=#00ff00}умиротворен{/color}'
      elif ratio>=0.8 and ratio<1.0:
        mood='{color=#ccccff}спокоен{/color}'
      elif ratio>=0.6 and ratio<0.8:
        mood='{color=#0085FF}напряжен{/color}'
      elif ratio>=0.4 and ratio<0.6:
        mood='{color=#ff8100}раздражен{/color}'
      elif ratio>=0.2 and ratio<0.4:
        mood='{color=#ff00ff}разъярен{/color}'
      elif ratio>=0.0 and ratio<0.2:
        mood='{color=#ff0000}взбешен{/color}, сейчас что-то будет!!!'
    'Князь Ада Архитот [mood]'
    $text='%s, %s, %s' %(game.summon.hp['architot'],summon_data.archimonde['max_hp'],ratio)
#    '[text]'
    nvl clear
    menu:
        'Прежде чем атаковать, хорошо бы выбрать, чем именно атаковать!' if 'dragon'  in game.summon.dd_list:
            call lb_hope_dragon_choose_atk from _call_lb_hope_dragon_choose_atk
        'Вроде бы всех вылечил?..' if 'dragon' in game.summon.healer_list and game.summon.act_mana>0:
            hide bg
            pass
        'Или всё же не всех?' if 'dragon' in game.summon.healer_list and game.summon.act_mana>0:
            hide bg
            call screen archimonde_main
        'Даже если вылечил не всех - божественной энергии всё равно не осталось!' if 'dragon' in game.summon.healer_list and game.summon.act_mana==0:
            hide bg
            pass
        'Но зато ещё осталась мана для заклинаний!' if 'dragon' in game.summon.healer_list and game.summon.act_mana==0 and not game.summon.magic_used and game.dragon.mana>0:
            hide bg
            call screen archimonde_main
        'Атаковать в лоб!' if 'dragon' in game.summon.tank_list:
            hide bg
            pass
        'Атаковать со спины, вынуждая Архитота развернуться' if 'dragon' in game.summon.tank_list:
            '[game.dragon.fullname] плавно обходит Архитота'
            if (random.randint(0,1)==0): # Защита не сработала
              'Благодаря своему выдающемуся интеллекту Князь Ада разгадывает тактический замысел дракона и не поддаётся на провокацию.'
            else:
              'Князь Ада Архитот разворачивается с поистине звериной грацией. Может быть, теперь его атаки не попадут по союзникам дракона?'
              $ game.summon.change_position()
            hide bg
            pass
        'Может, сперва стоит наложить заклинание?' if ('dragon' in game.summon.tank_list or 'dragon' in game.summon.dd_list) and not game.summon.magic_used and game.dragon.mana>0:
            hide bg
            call screen archimonde_main
#        'Атаковать!' if 'dragon' not in game.summon.healer_list and game.summon.dragon_att_chosen:
#            hide bg
#            pass

            
        'Хорошо бы ещё немного подумать...' if game.summon.dragon_att_chosen:
            hide bg
            call screen archimonde_main
        'Чем там Архитот атакует, я что-то забыл?':
            "[game.summon.desc]" 
            nvl clear
            call lb_dragon_att_archimonde from _call_lb_dragon_att_archimonde
#    show expression "img/archimonde/dragon.jpg" as bg 
    return

label lb_angel_info:  # Информация об ангеле
    hide bg
    nvl clear
    show expression "img/scene/fight/angel.jpg" as bg  
    if 'angel' in game.summon.healer_list:
      $text='Ангел лечит союзников.\n\nПосланец Небес может выдержать ударов: %s \n\nБожественной энергии в запасе: %s \n\nВ настоящий момент может вылечить ран: %s\n\nАнгел полностью неуязвим для дробящего и огненного урона, при удаче может избежать колющего и рубящего урона.\n\nАнгел может нанести демону огненный, рубящий или колющий урон.' % (game.summon.hp['angel'],game.summon.mp['angel'], game.summon.act_mana)
    else:
      $text='Ангел пытается уничтожить Архитота.\n\nПосланец Небес может выдержать ударов: %s \n\nАнгел полностью неуязвим для дробящего и огненного урона, при удаче может избежать колющего и рубящего урона.\n\nАнгел может нанести демону огненный, рубящий или колющий урон.' % (game.summon.hp['angel'])
    if 'forward' in game.summon.position:
      $text+='\n\nБойцы сосредоточились перед Архитотом.'
    else:
      $text+='\n\nБойцы сосредоточились позади Архитота.'
    '[text]'
    menu:
      'Лечить посланца Небес' if 'dragon' in game.summon.healer_list and game.summon.act_mana>0 and game.summon.hp['angel']<summon_data.fighters['angel']['max_hp']:
          if game.summon.act_mana==1 and (summon_data.fighters['angel']['max_hp']-game.summon.hp['angel'])>1:
            $ game.summon.act_mana=0
            $ game.summon.hp['angel']+=1
            'Повинуясь воле дракона, божественная энергия вливается в ангела. Увы, посланец Небес излечивается лишь частично!'
            angel 'Тёмный дилетант!'
            game.dragon 'Светлый ханжа!'
            jasmine '*Устало* Ну вы ещё подеритесь, подеритесь...'
          elif (summon_data.fighters['angel']['max_hp']-game.summon.hp['angel'])==1:   # Одна единица маны, у ангела одна рана
            $ game.summon.act_mana-=1
            $ game.summon.hp['angel']+=1
            'Повинуясь воле дракона, божественная энергия вливается в ангела. Посланец Небес полностью излечивается!'
            game.dragon 'Знай наших!'
            angel 'Просто счастливое совпадение'
            jasmine 'А ты бы предпочёл, чтобы совпадение было НЕ счастливым?!'
          else:
            game.dragon 'Сколько бы ран излечить у пернатого?' 
            menu:
                '1':
                    $ game.summon.act_mana-=1
                    $ game.summon.hp['angel']+=1
                '2' if game.summon.act_mana>1 and (summon_data.fighters['angel']['max_hp']-game.summon.hp['angel'])>1:
                    $ game.summon.act_mana-=2
                    $ game.summon.hp['angel']+=2
                '3' if game.summon.act_mana==3 and (summon_data.fighters['angel']['max_hp']-game.summon.hp['angel'])==3:
                    $ game.summon.act_mana-=3
                    $ game.summon.hp['angel']+=3                    
            if summon_data.fighters['angel']['max_hp']-game.summon.hp['angel']==0:
              'С помощью божественной энергии [game.dragon.fullname] полностью излечивает ангела. Какая ирония!'
            else:
              'С помощью божественной энергии [game.dragon.fullname] излечивает ангела, но некоторые раны по-прежнему остаются на теле посланца Небес. Достойная мстя за пережитые неудобства!'
      'Ясненько...':
          pass
    call screen archimonde_main      
    return

label lb_golem_info:  # нформация о големе
    hide bg
    nvl clear
    show expression "img/scene/fight/golem.jpg" as bg 
    if 'golem' in game.summon.tank_list:
      $text='Голем принимает на себя удары Князя Ада.\n\n'
    else:
      $text='Голем пытается уничтожить Архитота.\n\n'
    $text+='Шедевр цвергов может выдержать ударов: %s \n\nГолем уязвим для любого урона и полностью невосприимчив к божественной энергии. Абсолютно бесполезная жестянка... если не учитывать очень, ОЧЕНЬ большой запас прочности!\n\nГолем может нанести демону акустический или дробящий урон.' % (game.summon.hp['golem'])
    if 'forward' in game.summon.position:
      $text+='\n\nБойцы сосредоточились перед Архитотом.'
    else:
      $text+='\n\nБойцы сосредоточились позади Архитота.'
    '[text]'
    menu:
      'Ясненько...':
          pass
    call screen archimonde_main      
    return

label lb_titan_info:  # Информация об ангеле
    hide bg
    nvl clear
    show expression "img/scene/fight/titan.jpg" as bg  
    if 'titan' in game.summon.tank_list:
      $text='Титан принимает на себя удары Князя Ада.\n\n'
    else:
      $text='Титан пытается уничтожить Архитота.\n\n'
    $text+='Обитатель Облачного замка может выдержать ударов: %s \n\nТитан полностью неуязвим для дробящего и электрического урона, при удаче может избежать колющего и рубящего урона.\n\nТитан может нанести демону электрический, рубящий или колющий урон.' % (game.summon.hp['titan'])
    if 'forward' in game.summon.position:
      $text+='\n\nБойцы сосредоточились перед Архитотом.'
    else:
      $text+='\n\nБойцы сосредоточились позади Архитота.'
    '[text]'
    menu:
      'Лечить обитателя Облачного замка' if 'dragon' in game.summon.healer_list and game.summon.act_mana>0 and game.summon.hp['titan']<summon_data.fighters['titan']['max_hp']:
          $text='%s, %s' %(game.summon.hp['titan'], summon_data.fighters['titan']['max_hp'])
#          '[text]'
          if game.summon.act_mana==1 and (summon_data.fighters['titan']['max_hp']-game.summon.hp['titan'])>1:
            $ game.summon.act_mana=0
            $ game.summon.hp['titan']+=1
            'Повинуясь воле дракона, божественная энергия вливается в титана. Увы, обитатель Облачного замка излечивается лишь частично!'
            titan 'Жалкий неумёха!'
            game.dragon 'Титанический неудачник!'
            jasmine '*Устало* Ну вы ещё подеритесь, подеритесь...'
          elif (summon_data.fighters['titan']['max_hp']-game.summon.hp['titan'])==1:   # Одна единица маны, у титана одна рана
            $ game.summon.act_mana-=1
            $ game.summon.hp['titan']+=1
            'Повинуясь воле дракона, божественная энергия вливается в титана. Обитатель Облачного замка полностью излечивается!'
            game.dragon 'Знай наших!'
            angel 'Просто счастливое совпадение'
            jasmine 'А ты бы предпочёл, чтобы совпадение было НЕ счастливым?!'
          else:
            game.dragon 'Сколько бы ран излечить у громыхающего?' 
            menu:
                '1':
                    $ game.summon.act_mana-=1
                    $ game.summon.hp['titan']+=1
                '2' if game.summon.act_mana>1 and (summon_data.fighters['titan']['max_hp']-game.summon.hp['titan'])>1:
                    $ game.summon.act_mana-=2
                    $ game.summon.hp['titan']+=2
                '3' if game.summon.act_mana==3 and (summon_data.fighters['titan']['max_hp']-game.summon.hp['titan'])==3:
                    $ game.summon.act_mana-=3
                    $ game.summon.hp['titan']+=3                    
            if summon_data.fighters['titan']['max_hp']-game.summon.hp['titan']==0:
              'С помощью божественной энергии [game.dragon.fullname] полностью излечивает титана. Похвальная забота о... собственном враге?'
            else:
              'С помощью божественной энергии [game.dragon.fullname] излечивает титана, но некоторые раны по-прежнему остаются на теле обитателя Облачного замка. Достойная мстя за прошлые схватки!'
      'Ясненько...':
          pass
    call screen archimonde_main      
    return

label lb_dragon_info:  # Информация об ангеле
    hide bg
    nvl clear
    show expression "img/archimonde/dragon.jpg" as bg  
    if 'dragon' in game.summon.healer_list:
      $text='Дракон лечит союзников.\n\n'
    elif 'dragon' in game.summon.tank_list:
      $text='Дракон принимает на себя удары Князя Ада.\n\n'
    else: 
      $text='Дракон пытается уничтожить Архитота.\n\n'
    $text+='Злобный ящер может выдержать ударов: %s' %(game.summon.hp['dragon'])
    if 'dragon' in game.summon.healer_list:
      $text+='\n\nБожественной энергии в запасе: %s \n\nВ настоящий момент может вылечить ран: %s' % (game.summon.mp['dragon'], game.summon.act_mana)
    if 'forward' in game.summon.position:
      $text+='\n\nБойцы сосредоточились перед Архитотом.'
    else:
      $text+='\n\nБойцы сосредоточились позади Архитота.'
    '[text]'
    nvl clear
    menu:
      'Вспомнить бы, какие у меня способности...':
          $ buffs=game.buff_description()
          game.dragon.third "[game.dragon.description]\n\n[buffs]"
          call screen archimonde_main
      'Лечить самого себя' if 'dragon' in game.summon.healer_list and game.summon.act_mana>0 and game.summon.hp['dragon']<summon_data.fighters['dragon']['max_hp']:
          if game.summon.act_mana==1 and (summon_data.fighters['dragon']['max_hp']-game.summon.hp['dragon'])>1:
            $ game.summon.act_mana=0
            $ game.summon.hp['dragon']+=1
            $ game.dragon.health=game.summon.hp['dragon']
            'Дракон излечивает самого себя. Увы, лишь частично!'
            game.dragon 'Упс. Ошибочка вышла.'
          elif (summon_data.fighters['dragon']['max_hp']-game.summon.hp['dragon'])==1:   # Одна единица маны, у ангела одна рана
            $ game.summon.act_mana-=1
            $ game.summon.hp['dragon']+=1
            $ game.dragon.health=game.summon.hp['dragon']
            'Дракон полностью излечивает самого себя.'
            game.dragon 'Всю жизнь о таком мечтал!'
          else:
            game.dragon 'Сколько бы ран излечить у себя? Хотелось бы, конечно, побольше...' 
            menu:
                '1':
                    $ game.summon.act_mana-=1
                    $ game.summon.hp['dragon']+=1
                    $ game.dragon.health=game.summon.hp['dragon']
                '2' if game.summon.act_mana>1 and (summon_data.fighters['dragon']['max_hp']-game.summon.hp['dragon'])>1:
                    $ game.summon.act_mana-=2
                    $ game.summon.hp['dragon']+=2
                    $ game.dragon.health=game.summon.hp['dragon']
                '3' if game.summon.act_mana==3 and (summon_data.fighters['dragon']['max_hp']-game.summon.hp['dragon'])==3:
                    $ game.summon.act_mana-=3
                    $ game.summon.hp['dragon']+=3     
            if summon_data.fighters['dragon']['max_hp']-game.summon.hp['dragon']==0:
              'С помощью божественной энергии [game.dragon.fullname] полностью излечивает самого себя. Ну почему такой полезный навык доступен лишь в столь экстремальных ситуациях?!'
            else:
              'С помощью божественной энергии [game.dragon.fullname] излечивает самого себя, но некоторые раны по-прежнему остаются на теле ящера. Ну что такое "не везёт" и как с этим бороться?!!'
          call screen archimonde_main
      'Не, лечение - это что-то не моё' if 'dragon' in game.summon.healer_list:
          game.dragon 'Эй, пернатый! Ты был прав: лечение - это определённо не моё призвание!'
          angel.third 'Ангел без слов забирает у дракона остаток божественной энергии и начинает лечить'
          python:
              game.summon.mp['angel']=game.summon.mp['dragon']
              game.summon.healer_list.remove('dragon')
              game.summon.healer_list.append('angel')
              game.summon.dd_list.remove('angel')
              game.summon.dd_list.append('dragon')
      'Не, терпеть удары - это как-то не по-драконьи!' if 'dragon' in game.summon.tank_list:
          game.dragon 'Не, защита других - это определённо не моё призвание!'
          'Ангел что-то бурчит себе под нос.'
          game.dragon 'Кем ты меня назвал? Лягушкой?!'
          angel 'Да, а ещё червяком. А ещё земляным червяком!'
          'Голем бесстрастно занимает место дракона'
          python:
              game.summon.tank_list.remove('dragon')
              game.summon.tank_list.append('golem')
              game.summon.dd_list.remove('golem')
              game.summon.dd_list.append('dragon')
      'Самое время наложить заклинание!' if not game.summon.magic_used and game.dragon.mana>0:
          if game.choose_spell(u"Вернуться к битве"):
            python:
              game.dragon.drain_mana()
              game.summon.dragon_dict()
              game.summon.magic_used=True
          call screen archimonde_main
      'Мне нужно БОЛЬШЕ магической энергии!' if game.dragon.mana==0 and not game.summon.witch1_used:
          hide bg
          nvl clear
          show expression 'img/scene/witch.jpg'
          witch 'Вызывал, красавчик?'
          game.dragon 'Да, то есть нет, то есть можно без всей этой нервотрёпки?!'
          witch 'Нет. Я повинуюсь древним договорам, действие которых непреложно.'
          game.dragon 'Если ты не заметила, у нас тут небольшой конец света!'
          witch 'Глупости. Этот малыш даже до Ктунху не дотягивает.'
          witch 'Конечно, у меня были свои планы на королевскую династию... придётся их пока отложить. Сражаться из-за них с Архитотом я не намерена.'
          game.dragon 'Ох, ничего не поделаешь...'
          jasmine 'С вашего разрешения я отвернусь.'
          jasmine 'Моя гувернантка (увы, покойная) не одобрила бы подобного зрелища.'
          hide bg
          show expression 'img/scene/witch_sex.jpg' as bg
          'Кажется, это был самый скоростной минет на памяти дракона.'
          $ game.dragon.lust = 0
          $ game.dragon._mana_used-=1
          $ game.summon.witch1_used=True
          call screen archimonde_main
      'Мне нужно ЕЩЁ больше магической энергии!' if game.dragon.mana==0 and  game.summon.witch1_used and not game.summon.witch2_used and game.dragon.hunger == 3 and game.dragon.lust==0:
          hide bg
          nvl clear
          show expression 'img/scene/witch.jpg' as bg
          witch 'Всегда к твоим услугам'
          game.dragon 'Да я полностью пустой!!!'
          hide bg
          show expression 'img/archimonde/jasmine_intro.jpg' as bg 
          jasmine 'И что, ничего нельзя сделать?'
          game.dragon 'Ну, если подзакусить нежным девичьим мясцом...'
          'Принцесса Фиалка пожимает плечами'
          jasmine 'Угощайся.'
          witch.third 'Ведьма внимательно смотрит на принцессу.'
          jasmine.third 'Фиалка разводит руками'
          jasmine 'Полагаю, лучше оказаться в желудке дракона, чем в руках демона'
          game.dragon.third '[game.dragon.name] с некоторым сожалением отвергает этот вариант.'
          nvl clear
          game.dragon 'Тебя одной всё равно мало.'
          game.dragon 'К тому же на тебе вся тактика битвы. Без твоих советов мы бы просто не знали, что нам делать!'
          'Ангел, титан и Архитот согласно кивают.'
          jasmine 'Ну, количество это не проблема, сейчас фрейлин позову.'
          'Повинуясь приказам Фиалки, из полуразрушенного дворца выбегают девицы. Изрядно замызганные, но всё ещё благородные и вполне невинные.'
          $ i=0
          while i<3:
            $ description = game.girls_list.new_girl('princess')
            game.girl.third "[description]"
            $ text = u'%s, фрейлина принцессы Фиалки, прислуживала своей госпоже в королевском дворце. Увы, она устроилась на работу в нелёгкий час: на Столицу напал Князь Ада Архитот. Город был разрушен, вся королевская семья, кроме Фиалки, погибла. Исполняя волю принцессы, %s стала обедом для дракона, позволив ящеру восстановить похоть, заполучить магическую энергию и продолжить бой с Князем Ада.\n\nМужественная фрейлина до конца исполнила свой долг.' % (game.girl.name, game.girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            if game.girl.nature == 'innocent':
              game.girl 'Ой, боже мой, умоляю, сделайте это быстро, мне так страшно!!!'
            elif game.girl.nature == 'proud':
              game.girl 'Ты получишь моё тело, но не душу!'
            elif game.girl.nature == 'lust':
              game.girl 'Жаль, что у нас нет времени для более... обстоятельного знакомства.'
            $ description =  game.girls_list.eat_girl()
            play sound "sound/eat.ogg"
            $ current_image=sex_imgs.get_eat_image()
            show expression current_image as eat_image
            $ game.chronik.death('eat_architot',current_image)
            pause (500.0)
            hide eat_image
            $ i+=1
          nvl clear
          jasmine.third 'Принцесса Фиалка, бледная и испуганная, неотрывно следила за драконьим пиршеством.'
          witch 'Ай-ай-ай, разве про такое зрелище гувернантка ничего не говорила?'
          jasmine 'Ну должна же я представлять, что меня ждёт! И нет, ничего.'
          jasmine 'Ей бы такое просто в голову не пришло.'
          'Ящер насытился и восстановил свои силы. Фиалка отвернулась - кажется, с некоторой неохотой.'
          hide bg
          show expression 'img/scene/witch_sex.jpg' as bg
          'Вот это точно был самый скоростной минет на памяти дракона.'
          $ game.dragon.lust = 0
          $ game.dragon._mana_used-=1
          $ game.summon.witch2_used=True
          call screen archimonde_main
      'Как это ни странно, мне нужно ЕЩЁ БОЛЬШЕ магической энергии!' if game.dragon.mana==0 and not game.summon.witch3_used and game.summon.third_phase and game.summon.witch1_used:
          hide bg
          nvl clear
          show expression 'img/scene/witch.jpg' as bg
          witch 'Это уже становится привычным, красавчик?'
          '[game.dragon.fullname] тяжело вздыхает.'
          show expression 'img/scene/witch_sex.jpg'
          game.dragon.third 'Поглощённый приятными ощущениями, [game.dragon.name] не сразу замечает подглядывающую принцессу Фиалку'
          game.dragon 'Эй, а как же твоя гувернантка?!'
          'Фиалка стремительно краснеет'
          jasmine 'Нуу... должна же я понять, как это вообще анатомически возможно!'
          $ game.dragon.lust = 0
          $ game.dragon._mana_used-=1
          $ game.summon.witch3_used=True
          call screen archimonde_main
      'Магической энергии НИКОГДА не бывает достаточно' if game.dragon.mana==0 and game.dragon.hunger == 3 and game.summon.witch2_used and game.dragon.lust == 0 and game.summon.third_phase and not game.summon.witch4_used:
          hide bg
          nvl clear
          show expression 'img/scene/witch.jpg' as bg
          witch 'Тебе не надоело? Мне - нет.'
          game.dragon 'Вот только я опять пустой'
          hide bg
          show expression 'img/archimonde/jasmine_intro.jpg' as bg 
          jasmine 'Угощайся.'
          game.dragon 'Не хочу. У меня на тебя колоссальные планы... и вообще, такая жена нужна самому!'
          game.dragon.third 'Дракон в ужасе захлопнул пасть. Кажется, он сам не ожидал подобной реакции'
          jasmine 'Жаль...'
          'Принцесса Фиалка тяжело вздыхает'
          jasmine 'Сдаётся мне, что битву мы проиграем, и я в итоге достанусь демонам...'
          'Фиалка встряхивает головой, отгоняя тяжёлые мысли'
          jasmine 'Ладно. Битва ещё не закончена, а впереди в любом  случае много нового и интересного. Эй, девочки!'
          'Повинуясь приказам Фиалки, из полуразрушенного дворца выбегают девицы. Изрядно замызганные, но всё ещё благородные и вполне невинные.'
          $ i=0
          while i<3:
            $ description = game.girls_list.new_girl('princess')
            game.girl.third "[description]"
            $ text = u'%s, фрейлина принцессы Фиалки, прислуживала своей госпоже в королевском дворце. Увы, она устроилась на работу в нелёгкий час: на Столицу напал Князь Ада Архитот. Город был разрушен, вся королевская семья, кроме Фиалки, погибла. Исполняя волю принцессы, %s стала обедом для дракона, позволив ящеру восстановить похоть, заполучить магическую энергию и продолжить бой с Князем Ада.\n\nМужественная фрейлина до конца исполнила свой долг.' % (game.girl.name, game.girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            if game.girl.nature == 'innocent':
              game.girl 'Ой, боже мой, умоляю, сделайте это быстро, мне так страшно!!!'
            elif game.girl.nature == 'proud':
              game.girl 'Ты получишь моё тело, но не душу!'
            elif game.girl.nature == 'lust':
              game.girl 'Жаль, что у нас нет времени для более... обстоятельного знакомства.'
            $ description =  game.girls_list.eat_girl()
            play sound "sound/eat.ogg"
            $ current_image=sex_imgs.get_eat_image()
            show expression current_image as eat_image
            $ game.chronik.death('eat_architot',current_image)
            pause (500.0)
            hide eat_image
            $ i+=1
          nvl clear
          hide bg
          show expression 'img/scene/witch_sex.jpg' as bg
          jasmine.third 'Принцесса Фиалка бегает кругами, делая карандашный набросок.'
          jasmine 'Помедленнее, пожалуйста, я зарисовываю!'
          game.dragon 'Что ты творишь-то?!!'
          jasmine 'Рисую. У меня настоящий талант, честное слово. А такое зрелище не каждый день увидишь!'
          game.dragon.third 'Ну как такая приятная процедура может быть НАСТОЛЬКО нервирующей?!'
          $ game.dragon.lust = 0
          $ game.dragon._mana_used-=1
          $ game.summon.witch4_used=True
          call screen archimonde_main
      'Ясненько...':
          call screen archimonde_main
    return

label lb_jasmine_info:
    hide bg
    nvl clear   
    show expression 'img/archimonde/jasmine_discuss.jpg' as bg 
    jasmine 'Ты хотел о чём-то спросить?'
    menu:
        'Да, что тут вообще происходит?!':
            'Ангел, титан и Архитот прекращают бой и начинают внимательно прислушиваться. Кажется, их тоже интересует этот вопрос.'
            if not game.summon.third_phase:
              jasmine 'Тактика первой фазы...'
              game.dragon 'Так это только ПЕРВАЯ фаза?!!'
              jasmine 'Конечно, а как ты думал? Так вот, первая фаза.'
              jasmine 'Архитот танкуется, и в каждом раунде он наносит по танку три удара. Кроме того, он бьёт по рейду одной AoE-способностью.'
              jasmine 'AoE можно избежать, если танк успеет развернуть демона в противоположную сторону. Но тогда защита самого танка ослабнет'
              jasmine 'В каждом ходу целитель может вылечить три раны. Увы, голема лечить нельзя, но зато он очень, ОЧЕНЬ прочный.'
              jasmine 'Также на каждом ходу Архитот получает защиту от трёх типов урона. Бойцы должны смотреть, чем именно они бьют. Танку об этом беспокоиться не надо - его атака попадёт в любом случае.'
              game.dragon 'И мы должны победить такого монстра?!'
              jasmine 'Разумеется, нет!'
              jasmine 'Мы должны  взбесить Архитота, пока он нас всех не уничтожил. '
              game.dragon 'А там?'
              jasmine 'А там видно будет.'
            else:
              jasmine 'Ну, в третьей фазе Архитот не танкуется, зато он спускает по рейду три AoE и вешает на себя иммунитет к пяти видам урона'
              jasmine 'Но! Благодаря героизму ангел теперь одновременно - и боец, и целитель, и может вылечить любое количество ран.'
              jasmine 'Цель та же - взбесить Архитота и... хм...'
              jasmine '...и посмотреть, что получится!'
            call screen archimonde_main
        'Нет, ничего, спасибо':
            call screen archimonde_main
    return


label lb_hope_dragon_choose_atk:
    nvl clear
    hide bg
    show expression "img/archimonde/dragon.jpg" as bg  
    menu:
        'Навалиться на Архитота всей своей массой ({color=#ff8100}дробящий{/color} урон)' if 'mass' in summon_data.fighters['dragon']['attack']:
            $ game.summon.dragon_att_chosen='mass'
        'Полоснуть Архитота когтями ({color=#ff8100}режущий{/color} урон)' if 'cut' in summon_data.fighters['dragon']['attack']:
            $ game.summon.dragon_att_chosen='cut'
        'Укусить Архитота ({color=#ff8100}колющий{/color} урон)' if 'prick' in summon_data.fighters['dragon']['attack']:
            $ game.summon.dragon_att_chosen='prick'
        'Выдохнуть облако {color=#ff8100}огня{/color}' if 'fire' in summon_data.fighters['dragon']['attack']:
            $ game.summon.dragon_att_chosen='fire'
        'Выдохнуть облако {color=#ff8100}ледяного{/color} воздуха' if 'ice' in summon_data.fighters['dragon']['attack']:
            $ game.summon.dragon_att_chosen='ice'
        'Ударить Архитота {color=#ff8100}молнией{/color}' if 'lightning' in summon_data.fighters['dragon']['attack']:
            $ game.summon.dragon_att_chosen='lightning'
        'Использовать {color=#ff8100}яд{/color}' if 'poison' in summon_data.fighters['dragon']['attack']:
            $ game.summon.dragon_att_chosen='poison'
        '{color=#ff8100}Закричать{/color}' if 'sound' in summon_data.fighters['dragon']['attack']:
            $ game.summon.dragon_att_chosen='sound'
        'Подумать':
            call screen archimonde_main
    return

label lb_archimonde_decision2:
    nvl clear
    hide bg
    show expression "img/archimonde/gate.jpg" as bg
    architot 'Ып! \n *(Довольно!!!)*'
    'С помощью способности демонов "демоническое спокойствие" демон Архитот становится демонически спокойным!'
    architot "Арькъ'ка маньчыщ. \n *(Мне лень марать свои копыта. Мои прислужники покончат с вами)*"
    'Князя Ада окружает поле абсолютной защиты. Он начинает готовить ритуал призыва. Через открытый адский портал в мир проникает 3872 беса.'
    jasmine 'Скорее! Если через 666 секунд в живых останется хоть один бес, Архитот призовёт легионы демонов, и мы проиграем!'
    if game.summon.mistress_help:
      game.dragon.third 'Что же делать?!'
    else:
      game.dragon.third 'Что же делать?! Жаль, что нельзя позвать на помощь маму...'
    menu:
        'Можно позвать на помощь маму...' if game.summon.mistress_help:
            $ game.summon.mistress_help=False
            game.dragon 'Мама, у нас проблемы!'
            mistress 'Архитот... Старый, старый враг. И очень могущественный. Я рада, что снова сойдусь с ним лицом к лицу.'
            mistress 'Жаль только, что ты позвал меня слишком рано. Я смогу лишь уничтожить его мелких подручных.'
            mistress 'А теперь... почувствуй ярость Тёмной Госпожи!'
            $ renpy.movie_cutscene("mov/kali.webm")
            $ renpy.music.play(get_random_files('mus/darkness'))
            call lb_archimonde_decision3 from _call_lb_archimonde_decision3_1
        '...хотя лучше обойтись своими силами...':
            game.dragon 'Орды врагов меня не пугают!'
            game.dragon 'Наверное'
            python:
                game.summon.dd_list=[]
                if game.summon.live['angel']:
                  game.summon.dd_list.append('angel')
                if game.summon.live['golem']:
                  game.summon.dd_list.append('golem')
                if game.summon.live['titan']:
                  game.summon.dd_list.append('titan')
                if game.summon.live['dragon']:
                  game.summon.dd_list.append('dragon')
            call lb_archimonde_batlle_st2 from lb_archimonde_batlle_st2_1
        '...а ещё лучше - бежать поджав хвост!':
            call lb_archimonde_retreat from _call_lb_archimonde_retreat_2

    return

label lb_archimonde_batlle_st2:   # Вторая серия
    $ game.summon.minute=11
    $ game.summon.battle_st2()
    if game.summon.imps==1:
      python:
          imp = Talker(game_ref=game)
          imp.avatar = "img/archimonde/imp.jpg"
          imp.name = "Бес-победитель"
      nvl clear
      hide bg
      show expression 'img/archimonde/imp_win.jpg' as bg 
      'Последний выживший бес умудряется досрочно открыть врата Ада!'
      imp 'Муа-ха-ха! У меня получилось! Получилось!!!'
      imp 'Легионы Архитота уничктокха-кха-кха...'
      'Бес валится наземь, захлёбываясь собственной кровью. Принцесса Фиалка аккуратно извлекает кинжал из спины адского создания.'
      jasmine 'Сдохни, ублюдочное порождение грёбанной преисподней...'
      jasmine 'Кхм-кхм. Прошу меня простить: когда началось сражение, у меня как раз был мой любимый урок изящных манер.'
      call lb_archimonde_decision3 from _call_lb_archimonde_decision3_2
    else:
      nvl clear
      hide bg
      show expression 'img/archimonde/city_burn.jpg' as bg 
      'Благодаря уцелевшим бесам ([game.summon.imps]) Архитот успешно открывает Адские врата, и из них изливается необозримый поток демонов.'
      'Легионы буквально смели защитников. [game.dragon.fullname] пытался сражаться, но силы были неравны.'
      'После пропущенного удара его сознание погружается в благословенную черноту.'
      $ game.summon.live['dragon']=False
      call lb_death_dragon from _call_lb_death_dragon_1
    return

label lb_archimonde_dragon_st2:
    menu:
        'Попытаться убить беса' if game.summon.minute==11:
            '[game.dragon.fullname] аккуратно вступает в схватку и убивает одного-единстенного беса. Что, и это всё?!!'
            $ game.summon.imps-=1
        'Рискнуть и сразиться с десятком бесов' if game.summon.minute==10:
            '[game.dragon.fullname] осторожно начинает бой и безо всякого труда уничтожает десяток бесов. Какие-то они слабые...'
            $ game.summon.imps-=10
        'Бесстрашно сразиться с полустоней бесов' if game.summon.minute<10:
            $ game.foe = Enemy('imps', game_ref=game)
            call lb_fight from _call_lb_fight_88 
            $ x_min=50
            $ x_max=59
        'Раздавить мелких паразитов всей массой колоссального тела' if game.summon.minute<9 and 'mass' in summon_data.fighters['dragon']['attack']:
            if game.summon.imp_def=='mass':
              'Дракон пытается давить этих противных маленьких монстриков, но несуразно твёрдые бесы легко выскакивают из-под его колоссального тела. На земле остаётся лишь десяток-другой тушек'
              $ x_min=10
              $ x_max=20
            elif game.summon.imp_vul=='mass':
              'Бесы лопаются как переспелые ягоды. Кажется, дракон сам не ожидал такого успеха!'
              $ x_min=130
              $ x_max=150
            else:
              'Благодаря своим колоссальным габаритам [game.dragon.name] легко давит визжащих бесов'
              $ x_min=90
              $ x_max=110
        'Продемонстрировать адским завсегдатаям НАСТОЯЩИЙ огонь' if game.summon.minute<9 and 'fire' in summon_data.fighters['dragon']['attack']:
            if game.summon.imp_def=='fire':
              'Бесы орут, кувыркаются, но гореть отчего-то не спешат. На земле остаётся лишь десяток-другой тушек'
              $ x_min=10
              $ x_max=20
            elif game.summon.imp_vul=='fire':
              'Бесы вспыхивают как соломенные чучела. Странно, разве обитатели ада не должны быть более... огнеупорными?'
              $ x_min=130
              $ x_max=150
            else:
              'Огненное дыхание дракона испепеляет десятки визжащих бесов'
              $ x_min=90
              $ x_max=110
        'Познакомить настырных поганцев с понятием "абсолютный ноль"' if game.summon.minute<9 and 'ice' in summon_data.fighters['dragon']['attack']:
            if game.summon.imp_def=='ice':
              'Бесы нахально игнорируют резкое понижение температуры. На земле остаётся лишь десяток-другой тушек'
              $ x_min=10
              $ x_max=20
            elif game.summon.imp_vul=='ice':
              'Поле боя превращается в настоящий сад ледяных скульптур. Кажется, дракон сам не ожидал такого успеха!'
              $ x_min=130
              $ x_max=150
            else:
              'После особенно мощного выдоха десятки бесов превращаются в хорошо промороженные ледышки'
              $ x_min=90
              $ x_max=110
        'Устроить в толпе чёртовых коротышек потрясающий электрический шторм!' if game.summon.minute<9 and 'lightning' in summon_data.fighters['dragon']['attack']:
            if game.summon.imp_def=='lightning':
              'Бесы истошно орут, и этим весь эффект шторма и исчерпывается. На земле остаётся лишь десяток-другой тушек'
              $ x_min=10
              $ x_max=20
            elif game.summon.imp_vul=='lightning':
              'Очевидно, что тело беса - просто идеальный проводник. Кажется, дракон сам не ожидал такого успеха!'
              $ x_min=130
              $ x_max=150
            else:
              'Бушующий шторм оставляет после себя десятки подёргивающихся трупиков.'
              $ x_min=90
              $ x_max=110
        'Разъяснить незванным гостям смысл слова "pH"' if game.summon.minute<9 and 'poison' in summon_data.fighters['dragon']['attack']:
            if game.summon.imp_def=='poison':
              'Бесы проявляют поразительную кислотостойкость. На земле остаётся лишь десяток-другой тушек'
              $ x_min=10
              $ x_max=20
            elif game.summon.imp_vul=='poison':
              'Бесы бодро расплываются невнятными лужицами. Кажется, дракон сам не ожидал такого успеха!'
              $ x_min=130
              $ x_max=150
            else:
              'Клубы концентрированной кислоты оставляют после себя десятки полуразложившихся трупиков.'
              $ x_min=90
              $ x_max=110
        'Похвастаться перед демоническими завоевателями красотой драконьего голоса' if game.summon.minute<9 and 'sound' in summon_data.fighters['dragon']['attack']:
            if game.summon.imp_def=='sound':
              'Бесы в панике зажимают уши, но этим, собственно, эффект и исчерпывается. На земле остаётся лишь десяток-другой тушек'
              $ x_min=10
              $ x_max=20
            elif game.summon.imp_vul=='sound':
              'Акустическая волна просто разрывает бесов на куски. Кажется, дракон сам не ожидал такого успеха!'
              $ x_min=130
              $ x_max=150
            else:
              'От оглушающего драконьего рёва бесы десятками падают замертво.'
              $ x_min=90
              $ x_max=110

# Выбор сделан, жребий брошен
    if game.summon.minute<10: # В двух остальных случаях объяснение приведено выше
      nvl clear
      hide bg
      show expression "img/archimonde/dragon.jpg" as bg 
      $ num=game.summon.num_imps(x_min,x_max)
      $ text='%s уничтожил бесов: %s. Слава дракону!' %(game.dragon.name, num)
      game.dragon.third '[text]'
      $ game.summon.imps-=num
    return

label lb_archimonde_decision3:  # Третья фаза
    nvl clear
    hide bg
    show expression "img/archimonde/gate.jpg" as bg
    'Князь Ада Архитот прерывает свой ритуал и идёт навстречу защитникам' 
    jasmine 'А вот и третья фаза'
    game.dragon 'Надеюсь, она проще, чем первая?'
    jasmine 'Ну... в тех настолках, что я играла, она всегда была сложнее!'
    if game.summon.live['angel']:
      angel 'Да куда ещё сложнее-то?!!'
      'Впервые в жизни дракон был согласен с ангелом'
      if game.summon.mistress_help:
        game.dragon.third 'Что же делать?!'
      else:
        game.dragon.third 'Что же делать?! Жаль, что нельзя позвать на помощь маму...'
      menu:
        'Можно позвать на помощь маму...' if game.summon.mistress_help:
            $ game.summon.mistress_help=False
            game.dragon 'Мама, у нас проблемы!'
            mistress 'Архитот... Старый, старый враг. И очень могущественный. Я рада, что снова сойдусь с ним лицом к лицу.'
            mistress 'Жаль только, что ты позвал меня слишком рано. Я смогу лишь слегка поцарапать его шкуру.'
            mistress 'А теперь... почувствуй ярость Тёмной Госпожи!'
            $ renpy.movie_cutscene("mov/kali.webm")
            $ renpy.music.play(get_random_files('mus/darkness'))
            call lb_archimonde_decision4 from _call_lb_archimonde_decision4_1
        '...хотя лучше обойтись своими силами...':
            angel 'На что способен Архитот в третьей фазе?'
            'Князь Ада останавливается и прислушивается. Похоже, ему тоже интересно.'
            nvl clear
            hide bg
            show expression "img/archimonde/jasmine_intro.jpg" as bg
            jasmine 'В третьей фазе Архитот не танкуется. Кроме того, разозлить его гораздо легче.'
            game.dragon 'Похоже, это будет несложно.'
            jasmine 'Кроме того, демон сдаёт по рейду три AoE и вешает на себя иммунитет к пяти видам урона'
            game.dragon 'Беру свои слова обратно.'
            angel 'Я не смогу вылечить такой урон. Это будет наш последний бой.'
            jasmine.third 'Принцесса Фиалка с сомнением теребит в руках платочек.'
            jasmine 'Я попробую пробудить в вас героизм'
            nvl clear
            hide bg
            show expression "img/archimonde/jasmine_discuss.jpg" as bg
            pause 3.0
            'Фиалка становится на колени, молитвенно складывает руки и широко открывает глаза'
            jasmine 'Умоляю... Спасите...'
            angel 'Я чувствую прилив сил! Я вылечу любые раны! Мы сокрушим любого врага!!!'
            game.dragon 'Что-то я ничего не чувствую.'
            jasmine 'Ах да, у тебя же злое мировоззрение. На тебя "героизм" не подействует, только "жажда крови".'
            'Принцесса избавляется от лишней одежды и принимает завораживающую позу'
            hide bg
            show expression "img/archimonde/jasmine_intro.jpg" as bg
            show expression "img/archimonde/jasmine_nude.png" as fg
            pause 5.0
            jasmine 'Тебе понравится моя награда, милашка...'
            python:
                game.dragon.lust = 3  # range 0..3, ресурс восстанавливается до 3 после каждого отдыха
                game.dragon.hunger = 3  # range 0..3, ресурс восстанавливается до 3 после каждого отдыха
                game.dragon.health = summon_data.fighters['dragon']['max_hp']  # range 0..2, ресурс восстанавливается до 2 после каждого отдыха
            game.dragon 'Ты достанешься мне и только мне!!!'
            jasmine 'Уф. Подействовало.'
            hide fg
            jasmine 'Дракоша, я всё для тебя сделаю, ты только разберись с Архитотом, ладно?'
            python:
                game.summon.dd_list=[]
                game.summon.tank_list=[]
                if game.summon.live['angel']:
                  game.summon.dd_list.append('angel')
                if game.summon.live['dragon']:
                  game.summon.dd_list.append('dragon')
                if game.summon.live['titan']:
                  game.summon.dd_list.append('titan')
                if game.summon.live['golem']:
                  game.summon.dd_list.append('golem')
                game.summon.healer_list=[]
                game.summon.healer_list.append('angel')
                game.summon.battle_st3()
            if not game.summon.live['dragon']: # Дракон повержен
              return   # Приддставление закончилось
            call lb_archimonde_decision4 from _call_lb_archimonde_decision4_2
        '...а ещё лучше - бежать поджав хвост!':
            call lb_archimonde_retreat from _call_lb_archimonde_retreat_3     
    else:
      game.dragon 'Да куда ещё сложнее-то?!!'
      nvl clear
      hide bg
      show expression "img/archimonde/city_burn.jpg" as bg
      'Архитот показал - куда, расшвыряв защитников за считанные секунды'
      $ game.summon.live['dragon']=False
      call lb_death_dragon from _call_lb_death_dragon_3
    return

label lb_archimonde_decision4:  # Четвёртая фаза
    nvl clear
    hide bg
    show expression "img/archimonde/gate.jpg" as bg
    architot 'Довольно!'
    'И это была первая фраза, сказанная Князем Ада не на языке демонов.'
    architot 'Неужели вы думаете, что способны победить меня? Да даже тени моего могущества хватит, чтобы стереть вас в пыль.'
    'От Архитота отделяется множество астральных проекций'
    jasmine 'Ой. Босс вошёл в энрейдж.'
    jasmine 'Ребята, прощайте и спасибо за всё.'
    if game.summon.live['angel']:
      'Одна из проекций связала боем ангела, а вторая в это время прочитала какое-то заковыристое заклинание.'
      call lb_death_angel from _call_lb_death_angel_2
    if game.summon.live['titan']:
      'Всё воинское мастерство титана оказалось бесполезным'
      call lb_death_titan from _call_lb_death_titan_2
    if game.summon.live['golem']:
      'Голем, как и положено идеальной боевой машине, сражался размеренно и чётко, не обращая внимания на обстоятельства'
      call lb_death_golem from _call_lb_death_golem_2

    game.dragon 'Ой.'
    if game.summon.mistress_help:
      game.dragon.third 'Что же делать?!'
    else:
      game.dragon.third 'Что же делать?! Жаль, что нельзя позвать на помощь маму...'
    menu:
        'Можно позвать на помощь маму...' if game.summon.mistress_help:
            $ game.summon.mistress_help=False
            game.dragon 'Мама, у нас проблемы!'
            mistress 'Архитот... Старый, старый враг. И очень могущественный. Я рада, что снова сойдусь с ним лицом к лицу.'
            mistress 'Жаль только, что ты позвал меня слишком рано. Я смогу лишь уничтожить его астральные проекции'
            mistress 'А теперь... почувствуй ярость Тёмной Госпожи!'
            $ renpy.movie_cutscene("mov/kali.webm")
            $ renpy.music.play(get_random_files('mus/darkness'))
            call lb_archimonde_decision5 from _call_lb_archimonde_decision5_1
        '...хотя лучше обойтись своими силами...':
            game.dragon.third 'Отпступить?.. Ну уж нет, меня ещё ждёт награда от принцессы Фиалки!'
            $ game.foe = Enemy('architot_proection', game_ref=game)
            call lb_fight(skip_fear=True) from _call_lb_fight_89 
            call lb_archimonde_decision5 from _call_lb_archimonde_decision5_1
        '...а ещё лучше - бежать поджав хвост!':
            call lb_archimonde_retreat from _call_lb_archimonde_retreat_4   
    return

label lb_archimonde_decision5:  # Последняя пятая фаза
    nvl clear
    hide bg
    show expression "img/archimonde/black.jpg" as bg
    pause 3.0
    game.dragon 'Что?..'
    game.dragon 'Я жив?'
    game.dragon 'И битва, кажется, ещё не закончена. Надо быстрее выбраться из-под обломков!'
    menu:
        'Тому, кто умеет копать со скоростью бригады цвергов, не страшны никакие обломки!' if 'can_dig' in game.dragon.modifiers():
            game.dragon 'Ха! Я способен ЖИТЬ под землёй. Что мне какие-то обломки?'
            call lb_hope_find from _call_lb_hope_find_1
        'Ха! Благодаря своим размерам я могу проскользнуть в любую щель!' if game.dragon.size==1:
            game.dragon 'Потихонечку, полегонечку... иногда полезно быть маленьким - можно проскользнуть в любую щель!'
            call lb_hope_find from _call_lb_hope_find_2
        'Это будет непросто, но, кажется, я смогу тут проскользнуть...' if game.dragon.size==2 and game.dragon.paws==0:
            game.dragon 'Проклятье, как же здесь узко!'
            game.dragon 'Упс. Застрял.'
            game.dragon 'А, нет, всё в порядке. Но с лапами бы точно застрял!'
            call lb_hope_find from _call_lb_hope_find_3
        'Иногда размер имеет значение' if game.dragon.size>=5:
            game.dragon 'Так, надо немного поднатужиться...'
            game.dragon 'Получилось!'
            call lb_hope_find from _call_lb_hope_find_4
        'Когда у тебя есть мана, любая проблема кажется лишь поводом для заклинания!' if game.dragon.mana>0:
            game.dragon 'Хорошо, что я не потратил всю ману в битве с Архитотом!'
            $ game.dragon.drain_mana()
            call lb_hope_find from _call_lb_hope_find_5
        'Положиться на сакральные знания' if 'gold_magic' in game.dragon.modifiers() or 'silver_magic' in game.dragon.modifiers() or 'shadow_magic' in game.dragon.modifiers():
            game.dragon.third 'Так, так, вспомнить бы, как это делается...'
            game.dragon.third 'Взмахнуть хвостом... проклятье, хвост почти не движется! Ну, надеюсь, этого хватит.'
            game.dragon 'Вингардиум левиоса!!!'
            game.dragon  'Ну надо же. Получилось.'
            call lb_hope_find from _call_lb_hope_find_6
        'Если я не запутаюсь в лапах, то смогу выкопаться очень быстро!' if game.dragon.paws>=3:
            game.dragon 'Так. Передняя левая... Средняя правая... Задняя левая... Или всё же задняя правая?!'
            call lb_hope_find from _call_lb_hope_find_7
        'Спешить абсолютно некуда, выкапываться буду медленно и аккуратно...':
            hide bg
            show expression "img/archimonde/city_ruined.jpg" as bg
            'Кажется, [game.dragon.fullname] выбрался на свободу слишком поздно. Вокруг нет ни демонов, ни Архитота. Ни принцессы Фиалки.'
            game.dragon 'Жаль: девочка досталась демонам.'
            game.dragon 'Под конец она мне действительно понравилась. Я бы её точно есть не стал бы.'
            game.dragon 'Нуу... по крайней мере - сразу!'
            'Вокруг - лишь безжизненные руины.'
            'Впрочем, Вольные наверняка отстроют Столицу крайне быстро!'
             
    return

label lb_hope_find:
    nvl clear
    hide bg
    show expression "img/archimonde/city_ruined.jpg" as bg
    'Столица разрушена, но демоны, видимо, уже успели убраться прочь.'
    'А вот эманации Архитота никуда не делись - кажется, он ещё не успел уйти в портал.'
    game.dragon 'Неужели Фиалку ещё можно спасти?!'
    game.dragon 'Но как искать её в этом месиве обломков?'
    menu:
        '"Так взлетай вертикально вверх!"' if game.dragon.can_fly:
            game.dragon 'Полёт - это незабываемо. Он может сравниться разве что с общением с девушками!'
            call lb_archimonde_final from _call_lb_archimonde_final_1
        'К счастью, у меня достаточно лап, чтобы оббежать все руины очень быстро!' if game.dragon.paws>=3:
            game.dragon 'Так, одна лапа здесь, другая там, остальные четыре - где придётся!'
            call lb_archimonde_final from _call_lb_archimonde_final_2
        'Достаточно встать на цыпочки и оглянуться' if game.dragon.size>=5:
            game.dragon 'Ещё бы немножечко вытянуться...'
            call lb_archimonde_final from _call_lb_archimonde_final_3
        'Магический поиск. Затратно, но быстро' if game.dragon.mana>0:
            game.dragon 'Хорошо, что я не потратил всю ману в битве с Архитотом!'
            $ game.dragon.drain_mana()
            call lb_archimonde_final from _call_lb_archimonde_final_4
        'Почему бы не прибегнуть к эхолокации?' if 'sound_breath' in game.dragon.modifiers():
            game.dragon 'Крик нужен не только для того, чтобы крушить им скалы!'
            call lb_archimonde_final from _call_lb_archimonde_final_5
        'Догадаться о месторасположении портала' if game.dragon.modifiers().count('cunning') >=3:
            game.dragon 'Так, если бы я был на месте Архитота, я бы открыл портал... О! Точно!'
            call lb_archimonde_final from _call_lb_archimonde_final_6
        'Искать буду неспешно и обстоятельно...':
            '[game.dragon.fullname] обыскал все руины бывшей Столицы, но не нашёл ни следа Архитота. Видимо, он уже успел уйти.'
            game.dragon 'Жаль: девочка досталась демонам.'
            game.dragon 'Под конец она мне действительно понравилась. Я бы её точно есть не стал бы.'
            game.dragon 'Нуу... по крайней мере - сразу!'
            game.dragon 'Ладно, надеюсь, что люди быстро отстроят свою столицу'
    return

label lb_archimonde_final:
    game.dragon 'Нашёл!!!'
    nvl clear
    hide bg
    show expression 'img/archimonde/jasmine_captured.jpg' as bg
    'Архитот несёт принцессу к порталу. Фиалка кричит, отбивается, но ничего, ничего не может поделать.'
    '[game.dragon.fullname] отважно бросается на Князя Ада'
    'Архитот делает лёгкое движение ладонью, и дракона полностью парализует'
    game.dragon 'Нет... нет! Я не могу сдвинуться с места!'
    'Принцесса Фиалка замечает порыв дракона. Она начинает шептать, и [game.dragon.name] легко читает по губам'
    jasmine 'Пожалуйста, убей меня.'
    game.dragon 'Нет...'
    jasmine 'Умоляю... Я не хочу! Не хочу!!! Прикончи меня!'
    game.dragon 'Нет, нет, нет!'
    'По лицу Фиалки катятся слёзы. Архитот практически дошёл до портала'
    game.dragon 'Нет!!!'
    'Дракон убил множество девиц. Почему же отнять одну-единственную жизнь настолько  трудно?!'
    nvl clear
    menu:
        'Выдохнуть струю огня' if 'fire_breath' in game.dragon.modifiers(): 
            'Струя опаляющего жара накрывает визжащую Фиалку. Её кожа и мясо обугливаются и чернеют, волосы и одежда сгорают, крик резко обрывается. Спустя несколько секунд на спине у Архитота лежит обугленный труп.'
            call lb_archimonde_end from _call_lb_archimonde_end_1
        'Выдохнуть облако морозного воздуха' if 'ice_breath' in game.dragon.modifiers(): 
            'Облако иссущающего мороза накрывает визжащую Фиалку. От резкого перепада температур все жидкости  в её теле замерзают. Кристаллики льда разрушают каждую клеточку, причиняя короткую, но нестерпимую боль. Спустя несколько секунд на спине у Архитота лежит качественно промороженный труп.'
            call lb_archimonde_end from _call_lb_archimonde_end_2
        'Ударить молнией' if 'lightning_breath' in game.dragon.modifiers(): 
            'Визжащее тело Фиалки бьётся в последних конвульсиях. Архитот берёт его на руке, но уже поздно - после такой мощного электрического разряда на руках у демона остаётся лишь труп.'
            call lb_archimonde_end from _call_lb_archimonde_end_3
        'Закричать' if 'sound_breath' in game.dragon.modifiers(): 
            'Мощная акустическая волна рвёт и корёжит тело Фиалки. Во все стороны летят брызги крови, ошмётки мяса и обломки костей. Несколько секунд - и на спине Архитота нет даже трупа.'
            call lb_archimonde_end from _call_lb_archimonde_end_4
        'Выдохнуть облако яда' if 'poison_breath' in game.dragon.modifiers(): 
            'Фиалка орёт, когда кислотные испарения начинают разъедать её тело. Архитот берёт на руки, но от его малейших движений плоть слезает с принцессы огромными уродливыми квусками. Спустя несколько секунд от Фиалки остаётся лишь полуразложившийся труп.'
            call lb_archimonde_end from _call_lb_archimonde_end_5
        'Наложить заклинание' if game.dragon.mana>0: 
            'Фиалка коротко вздыхает, закрывает глаза и умирает. Быстро, безболезненно и навсегда. '
            call lb_archimonde_end from _call_lb_archimonde_end_6
        'Проигнорировать просьбу {color=#00ff00}(абсолютно безопасно){/color}':
            'Зелёное сияние портала поглощает безжалостного демона и его обречённую жертву.'
            hide bg
            show expression "img/archimonde/city_ruined.jpg" as bg
            game.dragon 'Я - хладнокровный безжалостный дракон.'
            game.dragon 'Почему же тогда мне так горько?!'
            game.dragon 'Даже мне становится не по себе при мысли о том, что ожидает Фиалку в Аду.'
            $ game.dragon.bloodiness = 5
            game.dragon 'Тьфу, нервы ни к ангелу. Пойду кого-нить съем.'
    return

label lb_archimonde_end:
    nvl clear
    hide bg
    show expression 'img/archimonde/archimonde_rage.jpg' as bg
    architot 'Вы не готовы'
    'А вот теперь Архитот ДЕЙСТВИТЕЛЬНО разозлился'
    architot 'Десять тысяч лет я охотился за этой генетической линией'
    architot 'Я мог перескочить через нескончаемую цепь перерождений'
    architot 'А теперь вы смеете унитожать плод моих трудов?!!'
    nvl clear
    game.dragon.third 'Это конец'
    menu:
        'Ой' if not game.summon.mistress_help:
            architot 'Вы не готовы'
            $ game.dragon._alive=False
            if freeplay:
              jump lb_game_over
        'Мама, спаси!' if  game.summon.mistress_help:
            game.dragon 'Мама!!!'
            mistress 'Я слышу тебя, сынок'
            mistress 'Архитот... Старый, старый враг. И очень могущественный. Я рада, что снова сойдусь с ним лицом к лицу.'
            mistress 'Ты позвал меня как нельзя вовремя. Астральные щиты Архитота пробиты, его силы истощены. Мне вполне по силам одолеть его!'
            mistress 'А теперь... почувствуй ярость Тёмной Госпожи!'
            $ renpy.movie_cutscene("mov/kali.webm")
            $ renpy.music.play(get_random_files('mus/darkness'))
            call lb_archimonde_rape1 from _call_lb_archimonde_rape1
    return

label lb_archimonde_rape1:
    nvl clear
    hide bg
    show expression "img/archimonde/black.jpg" as bg
    pause 4.0
    game.dragon.third 'Сознание возвращалось медленно.'
    game.dragon.third 'Откуда-то извне доносились противные хлюпающие звуки.'
    game.dragon.third '[game.dragon.name] с трудом открыл глаза'
    nvl clear
    hide bg
    show expression game.summon.get_archimonde_pic() as bg
    pause 3.0
    game.dragon 'Нет!'
    game.dragon.third 'Архитот насиловал маму'
    nvl clear
    hide bg
    show expression game.summon.get_archimonde_pic() as bg
    game.dragon.third 'Мама сопротивлялась, вырывалась, постоянно меняла тела'
    game.dragon.third 'Но в кого бы она не превращалась, какую бы позу не принимала, одно оставалось неизменным.'
    game.dragon.third 'Архитот насиловал маму'
    menu:
        'Броситься на помощь':
            nvl clear
            'Не помня себя от бешенства, [game.dragon.fullname] бросается на Князя Ада'
            'Архитот делает небрежное движение ладонью, и непреодолимая сила рвёт и сминает тело дракона, как мягкую бумажную фигурку'
            '[game.dragon.name] умер с полным осознанием того, что своими действиями погубил себя, свою мать и весь свой род.'
            game.dragon 'Мама...'
            jump lb_game_over
        'Дождаться подходящего момента':
            call lb_archimonde_rape2 from _call_lb_archimonde_rape2
    return

label lb_archimonde_rape2:
    nvl clear
    hide bg
    show expression game.summon.get_archimonde_pic() as bg
    mistress 'Тебе не победить...'
    'Магия Архитота заперла Тёмную Госпожу в человеческом теле.'
    'Она содрагается от ритмичных толчков и постанывает - явно от боли, а не от удовольствия.'
    mistress 'Когда... ты будешь изливаться в меня... то станешь... уязвим...'
    architot 'Вот только тебе это ни капельки не поможет'
    menu:
        'Броситься на помощь':
            nvl clear
            'Не помня себя от бешенства, [game.dragon.fullname] бросается на Князя Ада'
            architot 'А, вот на кого ты надеялясь'
            'Лёгким движением ладони Архитот парализует дракона.'
            '[game.dragon.name] чувствует, что задыхается. Он дышит, тяжело и отчаянно, но его кровь просто не в силах переносить кислород. Помутившимся зрением он видит, как отчаяние и безнадёжность в глазах мамы сменяются обожанием и беспрекословной преданностью. '
            game.dragon 'Ма...'
            jump lb_game_over
        'Дождаться подходящего момента':
            call lb_archimonde_rape3 from _call_lb_archimonde_rape3
    return

label lb_archimonde_rape3:
    nvl clear
    hide bg
    show expression game.summon.get_archimonde_pic() as bg
    architot 'А знаешь, что я сделаю с тобой?'
    'Архитот, не прекращая ритмичных движений, глумится над поверженной противницей.'
    architot 'Не убью, нет. Когда моё семя укоренится в тебе, ты сломаешься, станешь моей безвольной игрушкой.'
    mistress 'Но...'
    architot 'Так и будет, моя дорогая, так и будет.'
    'В глазах Тёмной Госпожи надежда сменяется отчаянием'
    menu:
        'Броситься на помощь':
            nvl clear
            'Не помня себя от бешенства, [game.dragon.fullname] бросается на Князя Ада'
            architot 'Посмотри, как это делается'
            'Лёгким движением ладони Архитот полностью порабощает дракона.'
            game.dragon 'Что прикажите, Повелитель?'
            architot 'Мне не нужен ваш порченный род. Отправляйся в пустоши, убей всех своих братьев и предков, а затем и себя.'
            game.dragon.third 'Повелитель добр и мудр. Он отдал правильный приказ.'
            mistress 'НЕЕЕТ!!!'
            game.dragon 'Будет исполнено, Повелитель'
            jump lb_game_over
        'Дождаться подходящего момента':
            call lb_archimonde_rape4 from _call_lb_archimonde_rape4
    return

label lb_archimonde_rape4:
    nvl clear
    hide bg
    show expression game.summon.get_archimonde_pic() as bg
    'Архитот ускоряется.'
    mistress 'Нееет!!!'
    architot 'О дааа...'
    nvl clear
    'С утробным рычанием Князь Ада изливается в лоно беспомощной жертвы'
    menu:
        'Броситься на помощь':
            nvl clear
            'Не помня себя от бешенства, [game.dragon.fullname] бросается на Князя Ада'
            $ renpy.music.play('mus/forest.ogg')
            nvl clear
            hide bg
            show expression "img/archimonde/archimonde_defeat.jpg" as bg
            'Князь Ада настолько поглощён приятными ощущениями, что пропускает удар дракона!'
            
            'От полученной раны Архитот кричит и выгибается дугой'
            mistress 'Анду-фала-дор!!!' 
            'С ладоней Тёмной Госпожи бесконечным потоком срываются светящиеся огоньки. Они окружают Архитота, впиваются в него, убивают его.'
            nvl clear
            hide bg
            show expression "img/archimonde/archimonde_death.jpg" as bg
            'Князь Ада встаёт, шатается.'
            'Падает'
            architot 'Вам... не победить.'
            architot 'Моя смерть... ничего... не изменит!'
            architot 'После меня... придёт... Архи... этот...'
            'И это были последние слова могущественного Князя Ада'
            nvl clear
            hide bg
            show expression "img/intro/8.jpg" as bg
            'Тёмная Госпожа неспешно поднимается'
            mistress 'Превосходно'
            game.dragon 'Мама?'
            mistress 'Превосходно! Я горжусь тобой, сын!'
            game.dragon 'Но мама, ведь эта тварь изнасиловала тебя! И это мои, именно мои поступи привели к такому!!!'
            mistress 'Да. Воистину, мои дети не только сильны, но и умны!'
            mistress 'Ты спровоцировал Вольных, позволил им призвать Архитота, схватился с Князем Ада, уничтожив его астральные щиты, вовремя позвал меня и понял мой намёк, идеально выбрав время для атаки!'
            '[game.dragon.name], не возражая, лишь склоняет голову.'
            mistress 'А теперь мало того, что Архитот мёртв, но я ещё и обладаю его уникальной спермой, которая серьёзно увеличит мои силы. Я горжусь тобой, сын!'
            nvl clear
            hide bg
            show expression "img/archimonde/city_ruined.jpg" as bg  
            'Тёмная Госпожа ушла, оставив сына на развалинах Столицы'
            game.dragon.third 'Да, это было неожиданно. А всё-таки жаль принцессу Фиалку.'
            if freeplay:
              game.dragon 'Ну что же, буду жить дальше. Думаю, Вольные отстроят Столицу очень быстро!'
            else:
              nvl clear
              hide bg
              show expression "img/scene/mobilization/16.jpg" as bg
              'Внезапно небеса засияли огнём, и на землю сошёл ещё один ангел'
              '[game.dragon.name] тяжело ввздохнул и приготовился к бою'
              'Но посланец Небес почему-то не торопился'
              angel 'Насилие. Разрушение. Смерть.'
              angel 'И ведь это сделали люди. Сами люди. Именно они начали практиковать человеческие жертвоприношения, именно они прибегли к тёмной и запретной магии, именно они вызвали демонов. Финал закономерен. Эх. если бы мы только знали...'
              game.dragon 'А вы не знали?'
              angel 'Ты удивишься, но нет.'
              nvl clear
              'Дракон и ангел помолчали'
              game.dragon 'И что теперь?'
              angel 'Теперь нам предстоит война  с демонами. Хозяева Архитота не простят нам его смерти.'
              game.dragon 'Хозяева? То есть он не  самый сильный демон в Аду?!'
              angel 'Разумеется. У разорённого Королевства нет ни единого шанса, а вслед за нами падёт весь мир.'
              angel 'Поэтому у нас есть единственный выход. Я послан сообщить что Небеса присягают на верность Тёмной Госпоже и обязуются поддерживать её. Во всём.'
              'Пожалуй, это было самое сильное потрясение за сегодняшний день.'
              game.dragon 'Но ты же понимаешь, что...'
              angel 'Мы понимаем. Вы создадите царство боли, насилия и смертей. Но вы ещё можете измениться - проявил же ты сочувствие к принцессе Фиалке!'
              angel 'А вот если восторжествуют хозяева Архитота, вся жизнь в мире будет уничтожена.'
              'В разговор неожиданно включилась Тёмная Госпожа'
              mistress 'Разумный выбор. Я отправлю своих потомков в Королевство - ребята заслужили немного развлечений.'
              nvl clear
              hide bg
              show expression "img/scene/orgy.jpg" as bg
              pause 3.0
              mistress 'Поддерживаешь?'
              'Ангел замолчал, не в силах сказать следующую фразу. Но всё-таки он решился'
              angel 'Да, Госпожа.'
              $ data.achieve_target("architot", "win")
              jump lb_you_win
        'Дождаться подходящего момента':
            call lb_archimonde_rape5 from _call_lb_archimonde_rape5
    return

label lb_archimonde_rape5:
    nvl clear
    hide bg
    show expression "img/archimonde/after.jpg" as bg
    'Семя Архитота переполнило лоно Тёмной Госпожи, и Князь Ада спустил его на спину и волосы своей жертвы. Из взгляда Владычицы уходили отчаяние и безнадёжность, сменяясь обожанием и беззаветной преданностью'
    architot 'Кто я?'
    mistress 'Вы - мой Господин и Повелитель, самое дорогое существо во Вселенной!'
    architot 'Ты знаешь, что с тобой будет?'
    mistress 'О да. Из Вашего семени родится ребёнок, и он будет вашим новым, совершенным телом! Ну а я умру при родах, в мучениях даря жизнь Вашему воплощению!'
    architot 'Как ты к этому относишься?'
    mistress 'Я счастлива умереть за Вас, о мой Повелитель!'
    nvl clear
    '[game.dragon.fullname] слушал это с нарастающим ужасом'
    menu:
        'Броситься на помощь':
            nvl clear
            'Не помня себя от бешенства, [game.dragon.fullname] бросается на Князя Ада'
            nvl clear
            hide bg
            show expression "img/intro/8.jpg" as bg
            pause 3.0
            'Тёмная Госпожа встала на защиту Архитота'
            '[game.dragon.fullname] замешкался, не в силах атаковать собственную мать'
            game.dragon 'Мама?'
            mistress 'Сдохни, ублюдок'
            jump lb_game_over
        'Дождаться подходящего момента':
            architot 'Ты что-то хотела сказать, раба?'
            mistress 'Повелитель, мой сын ещё жив. Если будет на то Ваша милость...'
            architot 'Разумеется'
            nvl clear
            hide bg
            show expression "img/intro/8.jpg" as bg
            pause 3.0
            'Тёмная Госпожа неспешно приближается к своему сыну'
            game.dragon 'Мама?'
            mistress 'Сдохни, ублюдок'
            jump lb_game_over
    return

