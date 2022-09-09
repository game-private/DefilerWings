# coding=utf-8
python:
    import treasures


label lb_event_knight_spawn(knight):
    show screen controls_overwrite
    scene
    show expression "img/scene/oath.jpg" as bg
    nvl clear
#    "[knight.title] принимает на себя священный обет убить дракона"
#    knight "Готовься, исчадие зла, я иду за тобой!"
    "[knight.title] принимает на себя священный обет освободить пленниц дракона"
    knight "Готовься, исчадие зла, я иду за тобой!"
    return

label lb_event_knight_receive_item(knight, item):
    show screen controls_overwrite
    scene
    show expression "img/scene/quest_knight.jpg" as bg
    nvl clear
#    "Рыцарь выполняет квест и получает [item.name]"
    if item.id == "glittering_vest":
      "[game.knight.name] выиграл рыцарский турнир и получил в награду сверкающий доспех." 
    elif item.id == "gold_vest":
      "[game.knight.name] заметил богатый кортеж, атакованный бандой ящериков, и стремглав бросился на помощь. После битвы выяснилось, что в карете ехала юная и прелестная аристократка. В награду за спасение своей дочери герцог подарил рыцарю прекрасный золочёный доспех." 
    elif item.id == "magic_vest":
      "[game.knight.name] нашёл логово демонопоклонников и одолел мерзких сектантов. В самом логове он нашёл прекрасную альву, привязанную к алтарю, но целую и невредимую. [game.knight.title] проводил её до священных лесов. В награду за спасение Дочь Дану подарила рыцарю доспех, зачарованный самыми мудрыми друидами её народа." 
    elif item.id == "blued_spear":
      "[game.knight.name] выиграл рыцарский турнир и получил в награду воронёное копьё." 
    elif item.id == "spear_with_scarf":
      "[game.knight.name] заметил банду ящериков, орудующую на остатках разорённого кортежа, и стремглав бросился на помощь. После короткой и напряжённой схватки ящерики отступили. Увы, [game.knight.title] не смог помочь ни защитникам, ни юной аристократке, принявшей мученическую смерть в лапах кровожадных чудовищ. [game.knight.name] взял с её тела ажурный шарф и повязал его на своё копьё, поклявшись, что эта ужасная история никогда не повторится впредь." 
    elif item.id == "dragonslayer_spear":
      "[game.knight.name] обнаружил заброшенные руины, настолько древние, что даже самые мудрые из альвов вряд ли смогли бы что-то сказать об их создателях. Проникнув в подземелья, истребив множество монстров и преодолев бесчисленное количество ловушек, [game.knight.title] обнаружил копьё, созданное в незапамятные времена специально для охоты на гигантских ящеров."
    elif item.id == "glittering_sword":
      "[game.knight.name] выиграл рыцарский турнир и получил в награду сияющий меч."   
    elif item.id == "lake_woman_sword":
      "Путешествуя вдоль берега озера, [game.knight.name] заметил юную, прекрасную и очень грустную воительницу. После короткого разговора выяснилось, что озёрная дева пришла сюда из иного мира. [game.knight.title] рассказал ей о злодеяних дракона, и дева подарила ему один из своих клинков, после чего ускакала прочь и исчезла в сгустившемся тумане. [game.knight.name] до конца дней своих  жалел о том, что так и не расслышал имя Владычицы озера. Вроде бы, что-то на 'Ц'?"  
    elif item.id == "flameberg_sword":
      "[game.knight.name] путешествовал вдоль границы Ифритистана, там, где  воздух наполнен пеплом, а далёкие вулканы подпирают небо тёмными, клубящимися столбами. Внезапно [game.knight.title] увидел меч, воткнутый в огромный валун. Удивившись, рыцарь подошёл и попытался вытащить его. Сначала клинок сидел намертво, как и положено любому уважающуму себя мечу в камне. Но стоило только рыцарю подумать о сражении с драконом, как пылающий фламберг с лёгкостью вышел из монолитного валуна!"
    elif item.id == "icecracker_sword":
      "Как-то раз [game.knight.name] услышал об убийстве, совершённом в соседнем городе. Приехав на место преступления, рыцарь обнаружил, что убийца уже пойман. Да и убитый был известным смутьяном, долгое время подстрекавшим против королевской власти. Обычная история, вот только [game.knight.title] очень заинтересовался орудием убийства. Магистрат городка пошёл ему навстречу, и рыцарь заполучил ледоруб-жидобой." 
    elif item.id == "thunderer_sword":
      "Как-то раз [game.knight.name] услышал о птице рух, похищавшей в предгорьях скот и людей. Долго [game.knight.title] искал гнездо этой твари, выматывающей и тяжёлой была схватка с монстром. После победы рыцарь забрал металлические когти птицы рух, а столичный кузнец выковал из них замечательный меч-громобой."    
    elif item.id == "polished_shield":
      "[game.knight.name] выиграл рыцарский турнир и получил в награду полированный щит."   
    elif item.id == "mirror_shield":
      "Как-то раз, странствуя вдоль побережья, [game.knight.name] увидел героя в старинном доспехе, сражавшегося с Медузой Горгоной. [game.knight.title] с радостью помог своему коллеге. В благодарность за помощь герой подарил рыцарю свой зерцальный щит." 
    elif item.id == "white_horse":
      "[game.knight.name] выиграл рыцарский турнир и получил в награду белого коня."
    elif item.id == "pegasus":
      "Стоя не высоком утёсе, [game.knight.name] обозревал земли Вольных.  Незасеянные поля, проплешины от пожаров, новые кладбища... безрадостная картина. Внезапно [game.knight.title] услышал громкое ржание, и прямо с небес к нему опустился крылатый пегас. Необычайный конь склонил голову и посмотрел на рыцаря не по-лошадиному умным взглядом. Пегас как будто спрашивал рыцаря: 'Доколе? Доколе будет длится всё это?' 'Недолго', - ответил [game.knight.name], - 'С тобой - недолго'"
    elif item.id == "firehorse":
      "[game.knight.name] опоздал. Когда он добрался до обречённого села, патруль уже добивал остатки банды ящериков, а само село пылало жарким пламенем. Выли от отчаяния немногие выжившие, потерявшие родных и близких. Внезапно в языках огня проступил силуэт лошади. Не успели присутсвующие и глазом моргнуть, как перед рыцарем стоял огненно-рыжий конь, в нетерпении бивший копытом. Кажется, ему тоже надоели злодеяния отродий Тёмной Госпожи."
    elif item.id == "sivka":
      "Как-то раз, странствуя поздней ночью, [game.knight.name] увидел коня, топчущего поле пшеницы. Да какого коня - одна шерстинка серебряная, другая золотая, бежит — земля дрожит, из ушей дым столбом валит, из ноздрей пламя пышет. Подкрался к коню рыцарь, накинул верёвку на шею, да и оседлал. Долго пытался скинуть его конь, а когда не смог - заговорил человеческим голосом, да сказал своё имя. С тех пор [game.knight.title] всегда мог вызвать коня, стоило только свистнуть три раз, да крикнуть погромче: 'Сивка-Бурка, вещая каурка, стань передо мною, как лист перед травою!'"
    elif item.id == "kelpie":
      "Как-то раз [game.knight.name] в задумчивости сидел на берегу озера. Проклятый ящер ускользал как вода сквозь пальцы, творя злодеяния во всех уголках Земель Вольных. Внезапно спокойные воды вспенились, и из глубин поднялся прекраснейший белоснежный конь. Кельпи бил копытом по водной глади и косил на рыцаря прозрачным глазом, как будтно подбадривая: 'Не бойся. Теперь я с тобой'"
    elif item.id == "griffon":
      "[game.knight.name] долго помогал цвергам. Он охранял их корованы, патрулировал местность перед входом в пещеры, сражался с монстрами на горных склонах и в подземных глубинах. И когда [game.knight.title] прокачал репутацию с цвергами до 'Превознесения', они подарили ему прекрасного белоснежного грифона."
    elif item.id == "squire":
      "Как-то раз, готовясь спасти очередного котёнка с дерева, [game.knight.name] заметил, что его кто-то опередил. Ловкий парнишка в два счёта забрался в головокружительную высь и бесстрашно снял с тонюсенькой веточки жалобно пищащий комочек меха. 'Впечатляет', - заметил [game.knight.title], когда спасатель спустился вниз, - 'Мне такой оруженосец не помешает. Хочешь присоединиться ко мне?' Ловкий парнишка жизнерадостно улыбнулся. 'С удовольствием, сэр рыцарь!'"
    elif item.id == "veteran":
      "[game.knight.name] выиграл рыцарский турнир. Закалённый ветеран, впечатлённый его успехами, решил присоединиться к рыцарю."
    elif item.id == "pythoness":
      "[game.knight.name] медленно шёл вдоль рядов деревенской ярмарки. Внезапно к нему подошла юная девушка. 'Вы собираетесь идти на дракона', - сказала она, - 'Я должна быть с вами. Я вижу будущее.' [game.knight.title] опешил. 'Мы победим?' - неуверенно спросил он. Ясновидящая спокойно пожала плечами. 'Не знаю. Но без меня ваши шансы гораздо ниже.'"
      $ game.knight.year=game.year-18
    elif item.id == "thaumaturge":
      "[game.knight.name] ехал в чистом поле, и тут внезапно из-за угла вышел старик. Массивный посох, остроконечная шляпа с широкими полями, рассшитая звёздами мантия, белоснежная борода и усы. 'Значит, ты решил победить дракона?' - грозно спросил незнакомец. [game.knight.title] невесть с чего стушевался и пробормотал: 'Я попытаюсь.' Старик дружелюбно усмехнулся в густые усы. 'Не надо пытаться. Делай. Или не делай.'"
    knight "Теперь дракону не уйти от моего возмездия!"
    return

label lb_event_knight_prepare_useless(knight):
    show screen controls_overwrite
    scene
    show expression "img/scene/quest_knight.jpg" as bg
    nvl clear
    "Рыцарь странствует по землям Вольных, помогая нуждающимся, утешая отчаявшихся и снимая котят с деревьев."
    return

label lb_event_knight_lair_unreachable(knight):
    show screen controls_overwrite
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    knight "До дракона не так-то просто добраться. Но я справлюсь! Нет таких крепостей, которых нельзя было бы взять ради спасения прекрасной дамы!"
    return

label lb_event_knight_refuse_horse(knight,item):
    show screen controls_overwrite
    hide bg
    show expression "img/scene/quest_knight.jpg" as bg
    nvl clear
    knight "Прощай, мой верный друг. Здесь ты, увы, мне ничем не поможешь."
    if item.id == "pegasus":
      "Грустно посмотрев на рыцаря, пегас стремглав взлетает в небеса"
    elif item.id == "firehorse":
      "С заливистым ржанием конь-огонь оборачивается языками пламени и рассыпается снопом искр"
    elif item.id == "sivka":
      "Сивка-Бурка, вещая каурка, не оглядываясь, скачет прочь"
    elif item.id == "kelpie":
      "С заливистым ржанием кельпи скрывается в бурном потоке"
    elif item.id == "griffon":
      "С пронзительным кличем грифон взмывает в небеса"
    elif item.id == "white_horse":
      "Похоже, теперь белый конь снова станет главным призом на очередном рыцарском турнире"
    return

label lb_event_knight_find_useless(knight):
    show screen controls_overwrite
    show expression "img/scene/quest_knight.jpg" as bg
    nvl clear
    "Хотя [game.dragon.fullname] совершил множество злодеяний, найти его логово оказалось не так-то просто."
    knight "Ничего. Ему не уйти. Вечно прятаться невозможно!"
    return

label lb_event_knight_no_dragon(knight):
    show screen controls_overwrite
    show expression "img/scene/quest_knight.jpg" as bg
    nvl clear
    "Вернувшись в знакомые места, [game.knight.name] нашёл логово дракона. Но не нашёл дракона!"
    knight "[game.dragon.fullname] сбежал от меня, подлый трус! Ничего, ему не уйти от моего возмездия!"
    return

label lb_event_knight_no_girls(knight):
    show screen controls_overwrite
    show expression "img/scene/arrive.jpg" as bg
    nvl clear
    "[knight.title] нашёл логово, где спит [game.dragon.name] [game.dragon.surname], и обнаружил, что там нет ни одной пленницы!"
    knight "Ничего, это не повод откладовать возмездие!"
    return

label lb_event_knight_go_to_lair(knight,girl):
    show screen controls_overwrite
    show expression "img/scene/arrive.jpg" as bg
    nvl clear
    '[knight.title] нашёл логово, где спит [game.dragon.name] [game.dragon.surname]'
    $ game.girl=girl
    $ girl=game.girl
    knight "А вот и логово, где томится в заключении прекрасная дева. Не бойся, сейчас я спасу тебя!"
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    if 'regular_guards' in game.lair.upgrades or 'elite_guards' in game.lair.upgrades or 'smuggler_guards' in game.lair.upgrades:
      "[knight.title] спокойно проходит внутрь драконьего логова и заходит в комнату к [girl.name_d]. Стражники не обращают на него никакого внимания - ведь они в первую очередь выискивают крадущихся злоумышленников. А если человек заходит в логово, как к себе домой - значит, он имеет на это полное право!"
    else:
      "[knight.title] спокойно проходит внутрь драконьего логова и заходит в комнату к [girl.name_d]."
    return

label lb_event_knight_talk_proud(knight,girl):
    show screen controls_overwrite
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    knight 'Я - сэр [knight.name], и я пришёл, чтобы спасти тебя!'
    if girl.willing:
      girl 'Спасибо, доблестный рыцарь! Но я связана обещанием и не могу покинуть свою тюрьму. Впрочем, если вы убьёте эту ящерицу, я возражать совершенно не буду!'
      $ text = u'%s %s пришёл в логово дракона, чтобы освободить %s. Но пленница была связана обещанием и не могла уйти из темницы, пока ящер жив. Рыцарь вызвался исправить это недоразумение.\n\n' % (knight.title,knight.name,girl.name_v,knight.name)
    else:
      if girl.virgin:
        girl 'Спасибо, доблестный рыцарь! Но я не могу уйти, зная, что дракон продолжит свои бесчинства. [game.dragon.name] угрожал обесчестить меня, и, если бы не ваш визит, обязательно исполнил бы обещанное. Молю вас, уничтожьте это чудовище!'
      elif girl.pregnant>0:
        girl 'Спасибо, доблестный рыцарь! Но я не могу уйти, зная, дракон останется безнаказанным. Он обесчестил меня, в моём животе зреют отвратительные, противоестественные твари. Молю вас, уничтожьте это чудовище!'
      else:
        girl 'Спасибо, доблестный рыцарь! Но я не могу уйти, зная, дракон останется безнаказанным. [game.dragon.name] обесчестил меня, и я родила емe отвратительных, противоестественных тварей. Молю вас, отомстите за меня и уничтожьте это чудовище!'
      $ text = u'%s %s пришёл в логово дракона, чтобы освободить %s. Но пленница страстно ненавидела похотливого ящера, она попросила своего спасителя уничтожить это подлое чудовище. Рыцаря не пришлось долго уговаривать - %s отважно бросил вызов дракону.\n\n' % (knight.title,knight.name,girl.name_v,knight.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    knight 'Быть по сему!'
    return

label lb_event_knight_talk_cripple(knight,girl):  # Инвалидки
    show screen controls_overwrite
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    knight 'Я - сэр [knight.name], и я пришёл, чтобы спа... Господи, что это?!!'
    girl 'Ааа...'
    $ text = u'%s %s пришёл в логово дракона, чтобы освободить %s. Но рыцарь, едва взглянув на калеку, пришёл в ужас и без оглядки кинулся на дракона.\n\n' % (knight.title,knight.name,girl.name_v)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    knight 'Клянусь, я отомщу за тебя! Нет такой смерти, которой проклятый ящер не заслуживал бы за свои злодеяния!'
    return

label lb_event_knight_talk_blind(knight,girl):  # Слепые
    show screen controls_overwrite
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    knight 'Я - сэр [knight.name], и я пришёл, чтобы спа... Господи, с вами?!!'
    if girl.pregnant>0:
      '[game.girl.name] бросается на шею рцаря, захлёбываясь сухими рыданиями. Сухими - потому что глаз у неё больше нет'
      knight 'Это... это чудовищно! Сейчас я быстренько одолею дракона и помогу вам!'
      $ text = u'%s %s пришёл в логово дракона, чтобы освободить %s - и ослеплённая женщина с рыданиями кинулась к своему спасителю. Придя в ужас, рыцарь без оглядки кинулся на дракона.\n\n' % (knight.title,knight.name,girl.name_v)
    else:
      girl 'Да ничего особенного. Просто внутреннее зрение открылось, и я теперь будущее могу видеть. Так что, наверное, я должна поблагодарить дракона за эту... незначительную косметическую операцию. '
      knight 'Но это... это чудовищно! Я должен убить дракона и спасти вас!'
      girl 'Спасать меня не требуется, мне ровным счётом ничего не угрожает. Да и с "убийством" могут возникнуть проблемы'
      'Рыцарь, даже не дослушав [game.girl.name_v], убегает на битву с драконом. Провидица равнодушно пожимает плечами.'
      girl 'Дёрганный он какой-то, нервный'
      $ text = u'%s %s пришёл в логово дракона, чтобы освободить %s - и обнаружил, что слепой провидице спасение, в общем-то, не требуется. Она попыталась объяснить рыцарю, что всё в порядке и из-за бесполезных глаз переживать совершенно незачем, но он всё равно пришёл в ужас и без оглядки кинулся на дракона.\n\n' % (knight.title,knight.name,girl.name_v)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_event_knight_talk_lizardman(knight,girl):  # Влюблённые в ящерика
    show screen controls_overwrite
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    knight 'Я - сэр [knight.name], и я пришёл, чтобы спасти тебя!'
    girl 'Спасибо вам, сэр рыцарь, но мой возлюбленный уже подготовил план побега! Совсем скоро я покину это ужасное место'
    knight 'Возлюбленый? Неужели даже среди прислужников дракона есть достойные и честные люди?'
    girl 'Насчёт людей не знаю, но [game.girl.love.name] - самый достойный, честный и красивый ящерик на свете!'
    knight 'Ящерик? Ты спуталась с этим отродьем? Тварь!!!'
    nvl clear
    hide bg
    $ current_image='img/scene/escape_kill.jpg'
    show expression current_image as bg
    '[game.girl.name] дёрнулась, но куда там! [knight.name] с лёгкостью одолел её и приставил свой клинок к девичьей шее'
    knight 'По праву, дарованному мне матерью нашей, Священной Церковью Небес, я предаю эту прислужницу Тёмной Гопожи смерти чере...'
    'Рыцарь осёкся - клинок в груди обычно не способствет ясности дикции'
    nvl clear
    hide bg
    show expression 'img/bg/love/lizardman_couple.jpg' as bg
    game.girl.love 'Этот безумец не причинил тебе вреда?'
    '[game.girl.name] облегчённо рассмеялась и поцеловала своего спасителя'
    girl 'Слава богу, не успел. Ты пришёл вовремя!'
    $ text = u'%s %s пришёл в логово дракона, чтобы освободить %s. Но, выяснив, что девушка влюбилась в ящерика, рыцарь пришёл в ярость, решил казнить предательницу и погиб от руки подкравшегося %sа. Нездоровый фанатизм до добра не доводит!\n\n' % (knight.title,knight.name,girl.name_v, girl.love.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_event_knight_talk_smuggler(knight,girl):  # Влюблённые в ящерика
    show screen controls_overwrite
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    knight 'Я - сэр [knight.name], и я пришёл, чтобы спасти тебя!'
    python:
        i=game.girls_list.prisoners.index(girl)
        del game.girls_list.prisoners[i]
    girl 'Спасибо вам, сэр рыцарь! Мой возлюбленный уже подготовил план побега, но помощь нам не помешает! Совсем скоро я покину это ужасное место'
    knight 'Возлюбленый? Неужели даже среди прислужников дракона есть достойные и честные люди?'
    girl 'Да, разумеется! [game.girl.love.name] - самый достойный, честный и красивый мужчина на свете! А вот, кстати, и он!'
    girl.love 'Эээ... Сэр рыцарь, вы пришли очень удачно! Не поможете нам с побегом? У меня уже всё готово!'
    knight 'Разумеется, [game.girl.love.name]. Это очень достойное деяние'
    nvl clear
    hide bg
    show expression 'img/bg/love/escape.jpg' as bg
    'Благодаря тщательной подготовке побег прошёл без сучка и задоринки'
    game.girl 'Спасена... Спасибо вам, [knight.name], вы нам очень помогли!'
    knight 'Не за что. Я просто исполняю свой долг. Хорошо, что даже среди прислужников дракона встречаются такие честные и ответственные люди! Кстати, я вспомнил, тебя же в Ильханабаде называют "Грязный [game.girl.love.name]"?'
    game.girl.love 'Что? Я не имею никакого отношения к работорговле!'
    knight 'Странно. Когда я отбил рабынь из того каравана, Белла описала тебя весьма точно.'
    game.girl.love 'Эта рыжая сучка соврала! Она всегда врала!'
    knight '[game.girl.name], заметьте, не я первым упомянул про работорговлю и про цвет волос несчастной жертвы!'
    nvl clear
    hide bg
    show expression 'img/scene/ninja.jpg' as bg
    '[game.girl.name] аккуратно отодвигается от контрабандиста'
    girl 'Любимый? Что с тобой? О чём вообще речь?'
    game.girl.love 'Э... он врёт, да-да, врёт!'
    knight 'Я не вру, сударыня. Этот мерзавец собирался продать вас на рабский рынок Султаната. Это уже не перввое его преступление.'
    'Взревев от ярости, [game.girl.love.name] бросается на рыцаря'
    'Но где уж ему победить опытного воина!'
    nvl clear
    '[game.girl.name] потрясённо смотрит на труп человека, которого, казалось, любила ещё несколько минут назад. Осознать, что тебя предали и едва не продали на рабский рынок - непросто'
    girl 'Мне... нужно домой. Я должна осознать произошедшее'
    knight 'Разумеется, сударыня, я провожу вас!'
    $ text = u'%s %s пришёл в логово дракона, чтобы освободить %s. Выяснив, что девушка влюбилась в контрабандиста, рыцарь помог им сбежать - а уже выбравшись  из логова дракона, разоблачил преступления негодяя. %s в ярости бросился на рыцаря и погиб, девушка была потрясена до глубины души. Пережить предательствво любимого человека очень трудно... но, по крайней мере, рыцарь отвёл её домой!\n\n' % (knight.title,knight.name,girl.name_v, girl.love.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.free_list.append(game.girl)
    nvl clear
    hide bg
    show expression 'img/scene/oath.jpg' as bg
    knight 'Не понимаю, я выполнил свои обеты, или нет?'
    'Рыцарь погружается в глубокое раздумье'
    knight 'Похоже, придётся наведаться к дракону на следующий год!'
    return

label lb_event_knight_talk_ogre(knight,girl):
    show screen controls_overwrite
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    knight 'Я - сэр [knight.name], и...'
    knight 'Ой.'
    hide bg
    show expression 'img/scene/fear/plains/ogre.jpg' as bg
    pause 1.5
    girl 'Еда! Моя ЖРАТЬ!!!'
    '[girl.name] с удовольствием подзакусила рыцарем и его оруженосцем'
    $ text = u'%s %s пришёл в логово дракона, чтобы освободить %s. Увы, с объектом спасения ему как-то не повезло - огрша с удовольствием подзакусила рыцарем и его оруженосцем.\n\n' % (knight.title,knight.name,girl.name_v)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_event_knight_talk_lust(knight,girl):
    show screen controls_overwrite
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    knight 'Я - сэр [knight.name], и я пришёл, чтобы спасти тебя!'
    '[girl.name] с интересом рассматривает своего спасителя'
    girl 'Ну... кое в чём помощь мне действительно необходима!'
    '[girl.name] скидывает свои скудные одёжки, подходит к рыцарю и начинает снимать его латную юбку.'
    knight 'Что... что вы делаете?!'
    girl 'Расслабься, красавчик. Уверяю, тебе понравится!'
    nvl clear
    if girl.virgin:
      $ path="img/scene/minet/"+girl.hair_color
      $ current_image=knight.get_pic(path)
      show expression current_image as bg
      play sound "sound/milking.ogg"
      pause 4.0
      '[girl.name] со сноровкой, говорящей о немалом практическом опыте, начинает обслуживать рыцарский член своим очаровательным ротиком. На лице рыцаря появляется колоссальное изумление, он пытается отстраниться - но в таком положении особо не подёргаешься.'
      'Правда, через некоторое время рот рыцаря расплывается в блаженной улыбке. [knight.title] кладёт [girl.name_d] руку на голову и начинает сам задавать темп. Девица покорно пытается заглотить член до самого основания, несмотря на немалые размеры рыцарского хозяйства.'
      'С блаженным стоном [knight.name] спускает сперму в девичий ротик. [girl.name] захлёбывается, давится, но покорно глотает всё до капли. Тщательно облизав опавшее рыцарское хозяйство, девица неохотно отстраняется.'
      girl 'Понравилось? Увы, большего дать не могу - блюду себя для дракона, а его только девственницы интересуют. Жду не дождусь этого захватывающего момента!'
      $ text = u'%s %s пришёл в логово дракона, чтобы освободить %s. Но у пленницы были иные планы - соскучившись по мужскому обществу, %s сделала рыцарю минет. Нельзя сказать, что %s не получил удовольствия... но придя в себя, он стремглав сбежал из драконьего логова, отвергнул воинскую стезю и ушёл в монастырь.\n\n' % (knight.title,knight.name,girl.name_v,girl.name,knight.name)
    else:
      $ path="img/scene/knight_sex/"+girl.hair_color
      $ current_image=knight.get_pic(path)
      show expression current_image as bg
      pause 4.0
      '[girl.name] ловко направляет восставший член рыцаря в своё лоно и начинает энергично двигаться. Растерявшийся [knight.name] сначала тупо стоит столбом, но потом постепенно входит во вкус. Он начинает сам задавать темп и позу, не обращая внимания на состояние партнёрши.'
      '[girl.name] на мгновение отстраняется и направляет "меч" рыцаря в иную, более узкую дырочку. Распалённый [knight.name], не обращая на это внимания, начинает долбить ещё глубже и интенсивнее. С уст [girl.name_r] срываются негромкие стоны - то ли боли, то ли удовольствия. Она опускает ладонь вниз и начинает теребить свой бугорок.'
      'Наконец [knight.name] с утробным рычанием спускает сперму внутрь девичьего тела. [girl.name] тяжело дышит, но своего наслаждения она, кажется, ещё не получила.'
      girl 'Скоро будешь готов ко второму кругу, красавчик?'
      $ text = u'%s %s пришёл в логово дракона, чтобы освободить %s. Но у пленницы были иные планы - соскучившись по мужскому обществу, %s оседлала рыцаря и всласть поскакала на его роскошном "хозяйстве", уделив внимание обоим дырочкам. Нельзя сказать, что %s не получил удовольствия... но придя в себя, он стремглав сбежал из драконьего логова, отвергнул воинскую стезю и ушёл в монастырь.\n\n' % (knight.title,knight.name,girl.name_v,girl.name,knight.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    knight 'Нет, нет, господи, что я натворил, я не должен был, я обесчестил нас обоих, НЕЕЕТ!!!'
    nvl clear
    '[knight.name] стремглав убегает прочь.'
    '[girl.name] равнодушно пожимает плечами.'
    girl 'Странный он какой-то.'
    hide bg
    show expression 'img/bg/special/castle3.jpg' as bg
    nvl clear
    'Вернувшись из логова дракона, [knight.name] ушёл в монастырь и провёл остаток своей жизни в постах, покаяниях и молитвах.'
    $ game.dragon.add_event('knight_killer')
    return

label lb_event_knight_talk_innocent(knight,girl):
    show screen controls_overwrite
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    python:
        if knight.items['follower'].name == u'Юный оруженосец':
          knight.items['follower'].id='basic_follower'
        elif knight.items['follower'].name == u'Ловкий оруженосец':
          knight.items['follower'].id='squire'
        elif knight.items['follower'].name == u'Закалённый оруженосец':
          knight.items['follower'].id='veteran'
        elif knight.items['follower'].name == u'Ясновидящая спутница':
          knight.items['follower'].id='pythoness'
        elif knight.items['follower'].name == u'Мудрый наставник':
          knight.items['follower'].id='thaumaturge'
    knight 'Я - сэр [knight.name], и я пришёл, чтобы спасти тебя!'
    python:
        i=game.girls_list.prisoners.index(girl)
        del game.girls_list.prisoners[i]
    if girl.willing:
      girl 'Но... дракон любит меня!'
      knight 'Сударыня, как вы можете говорить такое? Дракон - это кровожадное похотливое чудовище!'
      girl 'Нет! Это неправда, уходите прочь!'
      knight 'Раз так, то у меня нет выбора.'
      nvl clear
      hide bg
      $ current_image='img/scene/escape_kill.jpg'
      show expression current_image as bg
      '[game.girl.name] дёрнулась, но куда там! [knight.name] с лёгкостью одолел её и приставил свой клинок к девичьей шее'
      knight 'По праву, дарованному мне матерью нашей, Священной Церковью Небес, я предаю эту прислужницу Тёмной Гопожи смерти через отсечение головы!'
      'Обезглавненная [game.girl.name] мешком валится на землю'
      $ text = u'%s %s пришёл в логово дракона, чтобы освободить %s. Но когда пленница заявила, что дракон её любит, рыцарь пришёл в ярость и обезглавил эту приспешницу Тёмной Госпожи. \n\n' % (knight.title,knight.name,girl.name_v)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ game.chronik.death('knight_beheaded_rage',current_image) 
      knight 'Клянусь, подлый ящер заплатит и за эту смерть!'  
      $ knight.challenge_begin(repeate=True)
      return  
    '[girl.name] с криком радости бросается рыцарю на шею.'
    if girl.virgin:
      girl 'Умоляю, вытащите меня из этого кошмара! Дракон держит меня в плену, а когда проснётся, он, он меня...'
      girl 'Нет, я не могу даже думать об этом!'
    elif girl.pregnant>0:
      girl 'Умоляю, вытащите меня из этого кошмара! Дракон обесчестил меня, я ношу под сердцем его проклятое дитя, скоро я рожу его...'
      girl 'Нет, я не могу даже думать об этом!'
    else:
      girl 'Умоляю, вытащите меня из этого кошмара, или лучше убейте, дракон обесчестил меня, я родила монстров, мне незачем жить!!!'
    knight 'Это... это чудовищно! Клянусь, я спасу вас!'
    $ text = u'%s %s пришёл в логово дракона, чтобы освободить %s. Пленница восприняла появление спасителя, как настоящее чудо. \n\n' % (knight.title,knight.name,girl.name_v)
#    '[game.dragon.level], [game.girl.girl_id]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    stop music fadeout 1.0
    play music "mus/chase.ogg"
    $ renpy.music.queue(get_random_files('mus/ambient'))
    if len(game.girls_list.prisoners)>0:
      nvl clear
      hide bg
      show expression 'img/scene/escape1.jpg' as bg
      '[knight.name], его оруженосец и [girl.name] решили сбежать из логово дракона, не обращая внимания на остальных пленниц. Увы, всем помочь невозможно!'
    if "elite_guards" in game.lair.upgrades: # Долгий и весёлый побег
      nvl clear
      hide bg
      show expression 'img/scene/elite_guard.jpg' as bg
      'Внезапно путь беглецам перегородил элитный охранник.'
      'Рыцарь окинул его профессиональным взглядом и встал в боевую стойку.'
      knight 'Бегите, я отвлеку его и потом догоню!'
      $ text = u'Рыцарь остался сдерживать элитных охранников, а %s и оруженосец побежали прочь. ' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      'Пленница и оруженосец побежали прочь.'
      $ alone = False  # Бежит ли пленница одна, или её кто-то сопровождает
      python: #делаем аватарку  для диалогового окна
        follower= Talker(game_ref=game)
        follower.avatar = "img/avahuman/%s.jpg" % knight.items['follower'].id
        follower.name = '%s' % knight.items['follower'].name
      if 'smuggler_guards' in game.lair.upgrades:
        nvl clear
        hide bg
        show expression 'img/scene/ninja.jpg' as bg  
        'Обеспокоенные поднявшимся шумом, контрабандисты-охранники тщательно выискивают беглецов'
        if knight.items['follower'].id == 'basic_follower':
          'При виде врагов юный оруженосец впадает в панику.'
          follower 'ААА МЫВСЕУМРЁМ!!!1111'
          'Бесполезный шалопай несётся сломя голову и напарывается прямо на клинок контрабандиста. Кажется, дальше [game.girl.name_d] предстоит бежать самостоятельно'
          $ knight.items['follower'] = None
          $ alone = True
        elif knight.items['follower'].id == 'squire':
          'При виде врагов ловкий оруженосец бросается вперёд.'
          follower 'Беги, я отвлеку их!'
          'Ловкач морочит контрабандистам голову, появляясь то тут, то там, но всё время ускользая от опасных выпадов. Кажется, дальше [game.girl.name_d] предстоит бежать самостоятельно'
          $ alone = True
        elif knight.items['follower'].id == 'veteran':
          'При виде врагов закалённый оруженосец поднимает свою секиру.'
          follower 'И это ты называешь оружием? Вот ЭТО - настоящее оружие!'
          'Контрабандисты бросаются на ветерана, но он убивает их несколькими мощными ударами.'
          follower 'Бежим'     
        elif knight.items['follower'].id == 'thaumaturge':
          'При виде врагов мудрый наставник лишь устало вздыхает.'
          follower 'Ох, я уже слишком стар для всего этого...'
          'Лёгкое движение ладонью - и толпа одурманенных контрабандистов в замешательстве бредёт прочь.'
          follower 'Поспешим, дитя, тебе и так многое довелось пережить.'
        elif knight.items['follower'].id == 'pythoness':
          'Предвидев появление врага, ясновидящая спутница проводит [game.girl.name_r] по другому коридору!' 
      elif 'regular_guards' in game.lair.upgrades:
        nvl clear
        hide bg
        show expression 'img/scene/lizardman.jpg' as bg  
        'Обеспокоенные поднявшимся шумом, ящерики тщательно выискивают беглецов'
        if knight.items['follower'].id == 'basic_follower':
          'При виде врагов юный оруженосец впадает в панику.'
          follower 'ААА МЫВСЕУМРЁМ!!!1111'
          'Бесполезный шалопай несётся сломя голову и напарывается прямо на клинок ящерика. Кажется, дальше [game.girl.name_d] предстоит бежать самостоятельно'
          $ knight.items['follower'] = None
          $ alone = True
        elif knight.items['follower'].id == 'squire':
          'При виде врагов ловкий оруженосец бросается вперёд.'
          follower 'Беги, я отвлеку их!'
          'Ловкач морочит монстрам голову, появляясь то тут, то там, но всё время ускользая от опасных выпадов. Кажется, дальше [game.girl.name_d] предстоит бежать самостоятельно'
          $ alone = True
        elif knight.items['follower'].id == 'veteran':
          'При виде врагов закалённый оруженосец поднимает свою секиру.'
          follower 'Это будет славный бой. Беги, девочка, эта битва не для тебя!'
          if 'gremlin_fortification' in game.lair.upgrades:
            'Ветеран бросается на монстров и некоторое время успешно сдерживает их, но высковчивший из-за укрепления ящерик заходит ветерану за спину и сносит его голову!'
            $ knight.items['follower'] = None
          else:
            'Ветеран бросается на монстров. Исход битвы неясен. '
          'Кажется, дальше [game.girl.name_d] предстоит бежать самостоятельно'
          $ alone = True    
        elif knight.items['follower'].id == 'thaumaturge':
          'При виде врагов мудрый наставник лишь устало вздыхает.'
          follower 'Ох, я уже слишком стар для всего этого...'
          if 'gremlin_fortification' in game.lair.upgrades:
            'Мудрый наставник делает заковыристое движение посохом, пытаясь наложить заклинание, но выскочивший из-за укрепления ящерик вонзает зазубренный клинок ему в спину!'
            $ knight.items['follower'] = None
            'Кажется, дальше [game.girl.name_d] предстоит бежать самостоятельно'
            $ alone = True    
          else:
            'Заковыристое движение посохом - и толпу монстров охватывает жадное пламя.'
            follower 'Поспешим, дитя, тебе и так многое довелось пережить.'
        elif knight.items['follower'].id == 'pythoness':
          'Предвидев появление врага, ясновидящая спутница проводит [game.girl.name_r] по другому коридору!' 
      if knight.items['follower'] is None:
        $ text = u'Вот только оруженосец пал, отвлекая на себя внимание охранников логова, и %s побежала дальше в одиночку. ' % (game.girl.name)
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      elif alone:
        $ text = u'Вот только при встрече с охранниками логова оруженосец остался позади, отвлекая их внимание, и %s побежала дальше в одиночку. ' % (game.girl.name)
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      if alone: # Бежит в одиночку, может нарваться на ловушку
      # Магические ловушки
        if 'magic_traps' in game.lair.upgrades:
          nvl clear
          hide bg
          show expression 'img/scene/magic_trap.jpg' as bg
          'Несясь сломя голову, [game.girl.name] забежала прямо на магическую ловушку...'
          $ prob=100.*girls_data.girls_info[game.girl.type]['endurance']*random.random()
          if prob>35.:   # Выжила
            '... и благополучно побежала дальше.'
          else:  # Погибла
            if game.lair.type_name == 'underwater_grot' or game.lair.type_name == 'underwater_mansion':
              call lb_event_knight_fish from _call_lb_event_knight_fish
            else:
              call lb_event_knight_toad from _call_lb_event_knight_toad
            nvl clear
            hide bg
            show expression 'img/scene/arrive.jpg' as bg
            'Когда рыцарь понял, что [game.girl.name] попала в магическое измерение и спасти её невозможно, он пришёл в ярость и вызвал дракона на бой!'
            $ knight.challenge_begin(repeate=True)
            return
      # Механические ловушки
        if 'mechanic_traps' in game.lair.upgrades:
          nvl clear
          hide bg
          show expression 'img/scene/trap.jpg' as bg
          'Пытаясь спастись, [game.girl.name] оказалась у механической ловушки...'
          $ prob=100.*girls_data.girls_info[game.girl.type]['endurance']*random.random()
          if prob>35.:   # Выжила
            '... и пробежала мимо, даже не заметив опасности.'
          else:  # Погибла
            '...и внезапно потеряла сознание'
            if game.lair.type_name == 'underwater_grot' or game.lair.type_name == 'underwater_mansion':
              call lb_event_knight_drown from _call_lb_event_knight_drown
            else:
              $ trap = 'lb_event_knight_' + random.choice(['pendulum','thorns',])
              $ renpy.call(trap)
            nvl clear
            hide bg
            show expression 'img/scene/arrive.jpg' as bg
            'Когда рыцарь понял, что [game.girl.name] из-за его нерасторопности приняла мученическую смерть в ловушке, он пришёл в ярость и вызвал дракона на бой!'
            $ knight.challenge_begin(repeate=True)
            return
      nvl clear
      hide bg
      if girl.type=='elf':
        show expression 'img/scene/escape_elf.jpg' as bg
      else:
        show expression 'img/scene/escape_not_elf.jpg' as bg
      'Пока [knight.title] сдерживал элитных охранников, [game.girl.name] благополучно пробежала сквозь все ловушки'
      knight 'Получилось!'
      $ text = u'Пока рыцарь сдерживал элитных охранников, %s благополучно пробралась через все ловушки.\n\nА потом дракон проснулся. ' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_event_knight_dragon_rise(knight,girl) from _call_lb_event_knight_dragon_rise_2
    else:
      nvl clear
      hide bg
      if girl.type=='elf':
        show expression 'img/scene/escape_elf.jpg' as bg
      else:
        show expression 'img/scene/escape_not_elf.jpg' as bg
      '[knight.title] умудрился отбиться от охранников и провести [girl.name_v] сквозь все ловушки'
      knight 'Получилось!'
      $ text = u'Благодаря отсутствию в логове дракона элитных стражников побег шёл гладко. До поры до времени...\n\nА потом дракон проснулся. '
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_event_knight_dragon_rise(knight,girl) from _call_lb_event_knight_dragon_rise_1
    return

label lb_event_knight_pendulum: # Маятник
    nvl clear
    hide bg
    $ path="img/scene/pendulum/"+game.girl.hair_color
    $ current_image=knight.get_pic(path)  
    show expression current_image as bg
    '[game.girl.name] медленно приходила в себя - и нельзя сказать, что пробуждение было приятным. Лежащая на спине, скованная по рукам и ногам, неспособная пошевелиться - не самый приятный способ пробуждения.'
    nvl clear
    'Но что самое жуткое - прямо над животом [game.girl.name_r] колебался маятник. Очень острый маятник вв виде огромной секиры.'
    'И он постепенно опускался.'
    nvl clear
    '[game.girl.name] кричала. [game.girl.name] билась в своих путах. [game.girl.name] истово молилась. Ну не может же всё закончиться так глупо, буквально в шаге от спасения! Ну рыцарь ведь должен же отыскать её в этом проклятом логове! '
    nvl clear
    'Оказалось - может. [game.girl.name] поняла это, когда остриё впервые чиркнуло по её коже, оставив неглубокую царапину. И закричала.'
    'Совсем скоро в её криках не осталось ничего человеческого.'
    $ text = u'Увы, такие пробежки весьма опасны! %s активировала механическую ловушку, и маятник-лезвие неспешно и со вкусом разрезал  беглянку на две аккуратные половинки. ' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('trap_pendulum',current_image)
    return

label lb_event_knight_thorns: # Шипы
    nvl clear
    hide bg
    $ path="img/scene/thorns/"+game.girl.hair_color
    $ current_image=knight.get_pic(path)   
    show expression current_image as bg
    '[game.girl.name] медленно приходила в себя - и нельзя сказать, что пробуждение было приятным. Лежащая на спине, скованная по рукам и ногам, неспособная пошевелиться - не самый приятный способ пробуждения.'
    nvl clear
    'Но что самое жуткое - сверху небыстро, но и не так чтобу уж очень медденно опускались шипы. Целая платформа, полная длинных и очень, очень острых шипов.'
    nvl clear
    '[game.girl.name] кричала. [game.girl.name] билась в своих путах. [game.girl.name] истово молилась. Ну не может же всё закончиться так глупо, буквально в шаге от спасения! Ну рыцарь ведь должен же отыскать её в этом проклятом логове! '
    nvl clear
    'Оказалось - может. [game.girl.name] поняла это, когда шипы начали неспешно втыкаться в её полную грудь. Смертоносные наконечники маячили у неё перед глазами. Прямо перед глазами. '
    $ text = u'Увы, такие пробежки весьма опасны! %s активировала механическую ловушку, и плита с шипами неспешно и со вкусом опустилась на её мягкое и податливое тело. ' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('trap_thorns',current_image)
    return

# Утонувшие
label lb_event_knight_drown:
    nvl clear
    hide bg
    $ path="img/scene/drown/"+game.girl.hair_color
    $ current_image=knight.get_pic(path)
    show expression current_image as bg
    if game.girl.hair_color=='black':
      'Когда [game.girl.name] пришла в себя, у неё перед глазами было зеркало воды. Она висела вниз головой, ёё руки каким-то образом оказались скованы за спиной, ноги охватывала цепь'
      'И, что самое страшное, эта цепь постепенно опускалась'
      nvl clear
      '[game.girl.name] дёргалась, извивалась, пыталась позвать на помощь - но с завязанным ртом её вряд ли услышали бы даже в соседней комнате. [game.girl.name] всячески пыталась отсрочить свидание с безжалостной водной толщей. Но неизбежное всё же произошло.'
      nvl clear
      'Холодная вода равнодушно приняла разгорячённое тело. Лёгкие начало жечь, живот крутило нарастающей паникой. Вдруг [game.girl.name] заметила ключ. Если до него удастся дотянуться, если получится осввободить хотя бы руки...'
      'Но гремлины строили на совесть - цепь остановилась в считанных дюймах от ключа. Со дна на [game.girl.name_v] скалился череп незадачливого вора. Его долгое одиночество подошло к концу.'
    elif game.girl.hair_color=='brown':
      'Пробуждение было резким - просто [game.girl.name] ухнула вниз, и со всех сторон её окружила масса воды.'
      nvl clear
      'Беглянка попыталась всплыть, но куда там! Цепи, обмотанные вокруг лодыжек, крепились к тяжёлой чугунной чушке. Всё, что оставалось [game.girl.name_d] - это безнадёжно смотреть на такую близкую поверхность и пускать пузырики. Буль-буль-буль!'
    else:
      '[game.girl.name] очнулась в тесном каменном мешке, прикованная цепями к скале. Само по себе это не было проблемой - рано или поздно рыцарь должен был прийти ей на помощь.'
      nvl clear
      'А вот быстро поднимающаяся вода проблемой была.'
      nvl clear
      '[game.girl.name] кричала. [game.girl.name] звала на помощь. Но вода не слышала ни призыов, ни мольб.'
      nvl clear
      'Вот холодная поверхность поцеловала нижние губы... приласкала соски... дотронулась до подбородка... [game.girl.name] задержала дыхание. Она сдерживала его так долго, как могла. Но потом не выдержала и сделала последний и страшный вдох.'
    $ text = u'Увы, такие пробежки весьма опасны! %s активировала механическую ловушку, которая неспешно и со вкусом утопила беглянку. ' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('trap_drown',current_image)

    return

# Переваренные
label lb_event_knight_fish:
    '...и благополучно призвала рыбку.'
    nvl clear
    hide bg
    show expression 'img/scene/fish/1.jpg' as bg
  #  pause 5.0
    'Маааленькую такую рыбёшку'
    nvl clear
    hide bg
    show expression 'img/scene/fish/2.jpg' as bg
  #  pause 5.0
    'Но очень прожорливую'
    nvl clear
    hide bg
    show expression 'img/scene/fish/3.jpg' as bg
  #  pause 5.0
    '[game.girl.name] билась, сопротивлялась, звала на помощь...'
    nvl clear
    hide bg
    show expression 'img/scene/fish/4.jpg' as bg
  #  pause 5.0
    'Бесполезно'
    nvl clear
    hide bg
    show expression 'img/scene/fish/5.jpg' as bg
  #  pause 5.0
    'Но самое пикантное заключалось в том, что рыба не съела [game.girl.name_v]. Она заглотала свою жертву целиком'
    nvl clear
    hide bg
    show expression 'img/scene/fish/6.jpg' as bg
 #   pause 5.0
    'Впереди у [game.girl.name_r] были долгие часы жизни. Часы, наполненные неспешным и обстоятельным перевариванием.'
    $ text = u'Увы, такие пробежки весьма опасны! %s активировала магическую ловушку и угодила в желудок к гигантской рыбе. После этого она жила ещё несколько часов.' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('disgust_fish',"img/scene/fish/6.jpg")
    return

label lb_event_knight_toad:
    '...и благополучно призвала лягушку.'
    nvl clear
    hide bg
    show expression 'img/scene/toad/1.jpg' as bg
    #pause 5.0
    'Прожорливое брюшко'
    nvl clear
    hide bg
    show expression 'img/scene/toad/2.jpg' as bg
  #  pause 5.0
    'Ну очень прожорливое'
    nvl clear
    hide bg
    show expression 'img/scene/toad/3.jpg' as bg
  #  pause 5.0
    'А у [game.girl.name_r], вдобавок, из-за действия ловушки оказались скованы руки и ноги! Впрочем, будь они свободны, ей это вряд ли помогло бы...'
    nvl clear
    hide bg
    show expression 'img/scene/toad/4.jpg' as bg
  #  pause 5.0
    'Но самое пикантное заключалось в том, что лягушка не съела [game.girl.name_v]. Она заглотала свою жертву целиком'
    nvl clear
    hide bg
    show expression 'img/scene/toad/5.jpg' as bg
 #   pause 5.0
    'Впереди у [game.girl.name_r] были долгие часы жизни. Часы, наполненные неспешным и обстоятельным перевариванием.'
    $ text = u'Увы, такие пробежки весьма опасны! %s активировала магическую ловушку и угодила в желудок к гигантской и прожорливой лягушке. После этого она жила ещё несколько часов.' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('disgust_toad',"img/scene/toad/5.jpg")
    return

label lb_event_knight_dragon_rise(knight,girl):
    $ dragon=game.dragon
    nvl clear
    hide bg
    show expression 'img/scene/wokeup.jpg' as bg
    'Из-за суеты, поднявшейся во время побега, дракон проснулся!'
    dragon 'Догнать и покарать их, что ли? Так ведь спааать хочется...'
    menu:
        'Никто не смеет безнаказанно бежать из моего логова!':
            $ game.dragon.drain_energy()
            $ text = u'И бросился в погоню.\n\n'
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            call lb_event_knight_chase(knight) from _call_lb_event_knight_chase_1
        'Вскакивать ни свет ни заря из-за каких-то людишек? Да пусть бегут куда хотят!':
            $ game.dragon.gain_rage()
            $ text = u'И лёг спать дальше.\n\n'
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            'Благодаря беспечности дракона [knight.name] и [girl.name] сбежали из логова.'
            call lb_event_knight_girl_save(knight,girl) from _call_lb_event_knight_girl_save_1
    return

label lb_event_knight_chase(knight):
    hide bg
    nvl clear
    show expression 'img/scene/chase.jpg' as bg
    '[game.dragon.fullname] легко нагнал беглецов.'
    knight 'Похоже, честной битвы не избежать!'
    if knight.items['follower'] is None:
      call lb_knight_chase_fall(knight) from _call_lb_knight_chase_fall_4
    else:
      python: #делаем аватарку  для диалогового окна
        follower= Talker(game_ref=game)
        follower.avatar = "img/avahuman/%s.jpg" % knight.items['follower'].id
        follower.name = '%s' % knight.items['follower'].name
      if knight.items['follower'].id == 'basic_follower':
        call lb_knight_chase_fall(knight) from _call_lb_knight_chase_fall_5
      if knight.items['follower'].id == 'squire':
        follower 'Бегите, я отлеку его!'
        knight  'Но...'
        follower 'Не бойтесь, он по мне даже не попадёт!'
        'Рыцарь и спасённая им пленница переглянулись и побежали дальше.'
        nvl clear
        hide bg
        show expression 'img/scene/squire.jpg' as bg
        'Ловкий парнишка заступает путь дракона. Он не секунды не стоит на месте, двигаясь, подобно капельке ртути. Попасть по нему будет непросто.'
        follower 'Ну давай, ты, неуклюжая облезлая ящерица!'
        '[dragon.name] на секунду задумывается.'
        menu:
          'Проскочить мимо':
            dragon 'Знаю я эти уловки...'
            'Не обращая никакого внимания на противника, [dragon.name] проскакивает мимо и легко догоняет рыцаря.'
            call lb_knight_chase_fall(knight) from _call_lb_knight_chase_fall_1
          'Прикончить наглеца одним ударом':
            dragon 'Сейчас я покажу тебе "ящерицу"!'
            'Правда, прикончить ловкача первым ударом не получилось. Как и вторым. Как и третьим. В общем, когда от наглеца осталось мокрое место, рыцарь и пленница были уже очень, очень далеко.'
            $ text = u'Ловкий оруженосец отвлёк дракона, ценой своей жизни дав время рыцарю и %s.\n\n' % (game.girl.name_d)
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            call lb_event_knight_girl_save(knight,game.girl) from _call_lb_event_knight_girl_save_2
          'Подготовиться к затяжному бою':
            dragon 'Возможно, тут что-то нечисто?'
            'Сначала [dragon.name] готовился к бою. Потом он долго пытался найти ловкого оруженосца, мелькавшего то тут, то там. В общем. когда он понял, что противника и след простыл, рыцарь и пленница были уже очень, очень далеко.'
            dragon 'Проклятье!'
            $ game.dragon.gain_rage()
            $ text = u'Ловкий оруженосец отвлёк дракона, а потом благополучно сбежал и присоединился к рыцарю и %s.\n\n' % (game.girl.name_d)
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            call lb_event_knight_girl_save(knight,game.girl) from _call_lb_event_knight_girl_save_3
      elif knight.items['follower'].id == 'veteran':
        follower 'Бегите, я задержу его!'
        knight  'Но...'
        follower 'Ничего, я уже достаточно пожил на этом свете!'
        'Рыцарь и спасённая им пленница переглянулись и побежали дальше.'
        nvl clear
        hide bg
        show expression 'img/scene/veteran.jpg' as bg
        'Немолодой, закалённый воин молча выходит навстречу дракону. Он крепко сжимает в руках щит и меч и явно готовится подороже продать свою жизнь.'
        '[dragon.name] на секунду задумывается.'
        menu:
          'Проскочить мимо':
            dragon 'Ну, с ним-то сражаться мне не надо...'
            $ game.dragon.health -= 1
            '[dragon.name] проскакивает мимо оруженосца, но опытный воин успевает вонзить меч ему в бок! Впрочем, догнать рыцаря это никак не помешало.'
            call lb_knight_chase_fall(knight) from _call_lb_knight_chase_fall_2
          'Прикончить воина одним ударом':
            dragon 'Неужели ты думаешь, что способен справиться с сыном Тёмной Госпожи?!'
            '[dragon.name] расправляется  закалённым оруженосцем одним точным ударом, а затем с лёгкостью догоняет рыцаря.'
            $ knight.items['follower']=None
            call lb_knight_chase_fall(knight) from _call_lb_knight_chase_fall_3
          'Подготовиться к затяжному бою':
            dragon 'Возможно, тут что-то нечисто?'
            '[dragon.name] аккуратно атакует закалённого оруженосца, но ветеран оказывается опытным противником. Несмотря на очевидное превосходство дракона, человек стоял до последнего. Когда он, истекая кровью из многочисленных ран, всё же рухнул наземь, рыцаря и спасённой им пленницы уже и след простыл.'
            dragon 'Проклятье!'
            $ game.dragon.gain_rage()
            $ text = u'Закалённый оруженосец дорого продал свою жизнь, позволив рыцарю и %s скрыться от разъярённого дракона.\n\n' % (game.girl.name_d)
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            call lb_event_knight_girl_save(knight,game.girl) from _call_lb_event_knight_girl_save_4
      elif knight.items['follower'].id == 'thaumaturge':
        follower 'Дракон. Проклятие, а я так устал!'
        'Мудрый наставник разворачивается и идёт наперерез дракону.'
        knight  'Но...'
        follower 'Бегите, глупцы!'
        'Рыцарь и спасённая им пленница переглянулись и побежали дальше.'
        nvl clear
        hide bg
        show expression 'img/scene/thaumaturge.jpg' as bg
        'Устало сгорбившись, опираясь одной рукой на посох, а в другой сжимая сияющий меч, мудрый наставник ввыходит навстречу дракону.'
        follower 'Ты не пройдёшь. Я - покорный служитель Небес, владеющий  магией Света. Тёмное пламя Госпожи не поможет тебе. Ты не пройдёшь!'
        '[dragon.name] на секунду задумывается. Мимо мага незамеченным не проскочить, это будет чистым самоубийством...'
        call lb_knight_gandalf(gandalf=True) from _call_lb_knight_gandalf_1
      elif knight.items['follower'].id == 'pythoness':
        follower 'Ага. Чтобы задержать его, требуется... Ага.'
        knight  'Нет! Я не позволю тебе рисковать собой!'
        'Ясновидящая спутница закрывает глаза, погружается в короткий транс и вещает потусторонним голосом.'
        follower 'Согласно формуле Байеса, вероятность моего выживания при вступлении в бой в одиночку значительно превышает вероятность моего выживания при вступлении в бой в составе группы.'
        'После этого, так и не выйдя из транса, провидица пошла навстречу дракону. Рыцарь и спасённая им пленница, впечатлённые могущественным заклинанием "формула Байеса", переглянулись и побежали дальше.'
        nvl clear
        hide bg
        show expression 'img/scene/pythoness.jpg' as bg
        'Молодая, прекрасная и невинная провидица встаёт на пути дракона.'
        follower 'Привет!'
        'От стоящей перед ним девушки веет какой-то загадочной и непостижимой силой, способной нарушать законы логики и здравого смысла. [dragon.name] на секунду задумывается.'
        menu:
          'Проскочить мимо':
            dragon 'Ничего, эта красавица никуда от меня не уйдёт, а вот та, вторая, вполне и убежать может!'
            '[dragon.name] пытается проскочить мимо ясновидящей спутницы и немыслимым образом натыкается на неё. Девушка отлетает в сторону и со стоном падает на землю.'
            dragon 'Ой! Вы сильно ушиблись?'
            follower 'Да нет, наверно...'
            'В голосе ясновидящей не слышно особой уверенности. Дракон галантно подаёт даме хвост и помогает встать на ноги.'
            follower 'Большое спасибо!'
            dragon 'Ну в самом деле, я же кабальеро, а не засранец какой-то! Вам помочь дойти до дому? А то места тут дикие, опасные...'
            follower 'Вы очень любезны, но я вполне способна дойти сама. Прощайте, очень приятно было познакомиться!'
            dragon 'Взаимно!'
            nvl clear
            ' '
            $ game.dragon.gain_rage()
            ' '
            dragon 'Что! Это! Было?!'
            'Вопрос повис в пустоте - и рыцаря, и обеих его спутниц уже и след простыл.'
            $ text = u'Ясновидящая спутница каким-то непостижимым образом околдовала дракона, и он спокойно отпустил беглецов, не помышляя ни о каком насилии.\n\n' 
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
          'Познакомиться с красавицей поближе':
            dragon 'Ха, да зачем мне эта беглянка, если передо мной стоит такая красавица?'
            $ captive = game.girl
            $ description = game.girls_list.new_girl(girl_type='peasant',girl_nature='innocent',girl_year=game.knight.year)
            $ text = u'%s рано открыла в себе дар ясновидения. С его помощью она пыталась помочь людям, но те редко внимали её советам, считая %s слегка блаженной. Она не обижалась.\n\nКогда %s выросла, то осознала, что должна помочь людям одолеть дракона. Она нашла отважного рыцаря и присоединлась к нему. %s нашёл логово дракона и освободил %s. Но %s погнался за ними, %s встала на на пути дракона и попала в его лапы. \n\n' % (game.girl.name,game.girl.name_v,game.girl.name,game.knight.name,captive.name_v,game.dragon.fullname, game.girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            '[game.dragon.fullname] с лёгкостью поймал беззащитную девицу.'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_54
            $ game.girl=captive
          'Подготовиться к затяжному бою':
            dragon 'Тут наверняка что-то нечисто!'
            '[dragon.name] аккуратно обходит прелестную девушку. Ясновидящая безмятежно улыбается.'
            follower 'А давай сыграем в загадки!'
            dragon 'На что?'
            follower 'Ну, если ты выиграешь хотя бы один раз, то я вернусь к рыцарю, отравлю его, верну беглянку в твоё логово и отдамся тебе. А за каждый проигрыш ты дашь мне немного монет - сначала один фартинг, потом два, потом четыре... И первым, разумеется, загадываешь ты!'
            '[dragon.name] задумывается. Условия выглядт вполне честными.'
            dragon 'А давай! Что лежит у меня в кармане?'
            follower 'У тебя нет карманов!'
            dragon 'Да, действительно, что-то я поспешил... Загадывай!'
            nvl clear
            ' '
            $ game.dragon.bloodiness = 5
            ' '
            $ game.lair.treasury = treasures.Treasury()
            ' '
            follower 'Так, теперь моя очередь!'
            follower.third 'Уничтожает всё кругом:\nЦветы, зверей, высокий дом,\nСжуёт железо, сталь сожрёт\nИ скалы в порошок сотрёт,\nМощь городов, власть королей\nЕго могущества слабей. '
            dragon 'Эээ...'
            dragon 'Тёмная Госпожа?'
            follower 'Не, что ты, разве она настолько разрушительна? Праильный ответ - "время".'
            dragon 'Ох, сейчас...'
            $ game.dragon.lust=0
            dragon 'Держи.'
            follower 'Отлично! Ну что, ещё один раунд?'
            if len(game.girls_list.prisoners)>0:
              dragon 'Да куда уж ещё?! Ты уже отыграла все мои деньги и драгоценности, пленниц и годовой запас спермы!'
            else:
              dragon 'Да куда уж ещё?! Ты уже отыграла все мои деньги, драгоцнности и годовой запас спермы!'
            follower 'Ну... ты можешь поклясться больше никогда-никогда не безобразничать! Давай, я думаю, тебе на этот раз обязательно повезёт!'
            dragon 'Ну уж нет. Я прекрасно умею вовремя останавливаться!'
            follower 'Ну как хочешь. Удачи!'
            $ text = u'Ясновидящая спутница предложила дракону сыграть в загадки, попросив за первую победу один фартинг, за вторую - два, за третью - четыре... Дракон явно не был знаком с термином "геометрическая прогрессия"!\n\n' 
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            $ captive=game.girl
            $ game.girls_list.pythoness_free_all_girls()
            $ game.girl=captive
        call lb_event_knight_girl_save(knight,game.girl) from _call_lb_event_knight_girl_save_5

    return

label lb_knight_gandalf(gandalf=False):
    menu:
        'Попытаться проскочить мимо {color=#ff0000}(смертельно опасно){/color}':
            dragon 'Ничего, авось проскочу!'
            'Совершив стремительный рывок, [dragon.fullname] проносится мимо мага. Мудрый наставник вкладывает свою жизнь в магическую стрелу и падает замертво'
            dragon 'Ха! Единственная профессия, даже более опасная, чем "герой" - это "наставник главного героя"!'
            dragon 'Ой...'
            'Стрела вонзается в тушу ящера, наносит чистый духовный урон и убивает дракона на месте.'
            $ game.dragon._alive=False
            if freeplay:
              jump lb_game_over
        'Прикончить мага одним ударом' if not gandalf:
            $ game.dragon.health -= 1
            '[dragon.name] пытается убить старого мага одним  ударом, но он с лёгкостью парирует атаку и наносит ответный выпад.'
            follower 'Ты не пройдёшь!'
            dragon 'Упс, ошибочка вышла!'
            call lb_knight_gandalf(gandalf=False) from _call_lb_knight_gandalf_2
        'Подготовиться к затяжному бою':
            dragon 'Тут явно что-то нечисто!'
            'Битва, разразившаяся между драконом и магом, длилась три дня и три ночи. В ход шли самые изощрённые заклинания и самые подлые приёмы. Сталь встречалсь с когтями, изящные магические заклятия - с первобытными токами маны, бесценный опыт - с всепожирающей яростью.'
            'И в конце концов, на исходе третей ночи...'
            '[dragon.fullname] победил.'
            dragon 'Ха! Только  в такие моменты и чувствуешь себя по-настоящему живым!'
            $ text = u'Ещё не один год барды Королевства пели о битве мудрого наставника со злокозненным драконом. Правда, маг в итоге погиб, но такую смерть и в песне воспеть не стыдно!\n\n'
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            call lb_event_knight_girl_save(knight,game.girl) from _call_lb_event_knight_girl_save_5
    return

label lb_knight_chase_fall(knight):
    knight 'Что же, бой так бой!'
    $ game.girls_list.prisoners.append(game.girl)
    $ text = u'Последнее, что запомнила %s перед тем. как потерять сознание - это рыцарь, бросающийся в отчаянную атаку на дракона.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ knight.challenge_begin(repeate=True)
    return

label lb_event_knight_girl_save(knight,girl):
    nvl clear
    hide bg
    show expression 'img/scene/oath.jpg' as bg
    knight 'Обеты выполнены. Ты спасена.'
    if girl.pregnant>0:  # Беременная
      girl 'Да, спасена...'
      '[girl.name] задумчиво трёт свой растущий животик'
      if random.randint(1,3)==1:  # Самоубийство
        girl '[knight.name], поклянитесь, что выполните мою просьбу.'
        knight 'Если это не пойдёт во вред Вольным Народам - всё, что угодно. Клянусь.'
        girl 'Нет, не пойдёт... Убейте меня.'
        knight 'Что?!'
        girl 'Я обесчещена. В моём чреве зреет чудовище. Мне незачем жить. Лучшее, что со мной может случится - это умереть на свободе. Умереть от вашей руки.'
        knight 'Но...'
        girl 'Вы поклялись! Неужели [knight.title] отречётся от своих клятв?!'
        nvl clear
        hide bg
        $ current_image='img/scene/escape_kill.jpg'
        show expression current_image as bg
        pause 4.0
        girl 'Давайте быстрее. Мне страшно.'
        knight 'Мир не забудет вашего мужества'
        '[knight.name] обезглавил [girl.name_v] одним ударом, быстро и безболезненно.'
        $ text = u'Всё должно было закончится хорошо. \n\nНо не закончилось. %s, обесчещенная и беременная жутким чудовищем, не захотела жить дальше. Она хитростью выудила у рыцаря клятву убить её, и %s с тяжёлым сердцем исполнил обещанное. %s обезглавил %s одним ударом, её смерть была быстрой и безболезненной.\n\n' % (girl.name, knight.name,knight.title,girl.name_v)
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
        $ game.chronik.death('knight_beheaded',current_image)
        $ knight.die()
        return
      else:
        girl 'Я обесчещена. В моём чреве зреет чудовище. Мне незачем жить. Лучшее, что со мной может случится - это умереть на свободе. Умереть от вашей руки.'
        knight 'Что?! И думать не смейте! Я не для того спасал вас от дракона, чтобы позволить умереть на следующий же день.'
        girl 'Но дракон...'
        knight 'Плевать. [girl.name], выходите за меня замуж.'
        girl 'Но моё проклятое дитя...'
        knight 'Эту проблему тоже можно решить.'
        $ game.girl=girl
        $ text = u'Всё должно было закончится хорошо. \n\nВот только %s, обесчещенная и беременная жутким чудовищем, не хотела жить дальше. Она попросила рыцаря убить её, и он отказался. Быстро и непреклонно. %s предложил %s выйти за него замуж. А драконье отродье... о нём может позаботиться и инквизиция.\n\n' % (girl.name, knight.name,girl.name_d)
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
        call lb_girl_execution_inquisition from _call_lb_girl_execution_inquisition
    elif girl.virgin:  # Нетронутая
      girl 'И это чудо!!!'
      girl '[knight.name], я уже простилась с жизнью и не чаяла спасения. Вернуться из логова дракона, живой и невредимой... это чудо!'  
      girl 'Что же, мне пора возвращаться в родные места.'  
      knight 'Подождите!'
      girl 'Да?'
      '[knight.title] краснеет, бледнеет и нервно переминается с ноги на ногу.'
      knight 'Я не знаю, как начать...'
      knight 'В общем, значит, так сказать...'
      girl '[knight.name], что с вами? Вы же абсолютно бесстрашно вошли в логово дракона. Вы заболели?'
      knight 'Нет, я люблю вас больше жизни! [girl.name], выходите за меня замуж!'
      'На поляне повисло долгое и неловкое молчание.'
      knight 'Извините, я...'
      girl 'Я согласна.'
      $ text = u'Пленница была спасена, рыцарь исполнил свои обеты. %s собиралась в родные места, но тут отважный %s робко и путанно признался ей в любви и предложил выйти за него замуж. После короткого раздумья %s согласилась.\n\n' % (girl.name, knight.name,girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    else:  # Попользованная
      girl 'Да, спасена...'
      '[girl.name] тяжело вздыхает и смотрит в пространство невидящим взором.'
      girl 'Вы совершили невозможное. Уверена, ваш подвиг воспоют в веках. Ну а мне предстоит иная дорога. Надеюсь, в монастыре найдётся место и для меня.'
      '[knight.title] резко бледнеет'
      knight 'Вам не нужно идти в монастырь. Выходите за меня замуж.'
      girl 'Что? Нет, я ведь обесчещена, я родила отродье дракона, моя жизнь кончена, мне остаётся только замаливать свои грехи...'
      'knight.name] аккуратно берёт [girl.name_v] за руки.'
      knight 'Нет. Ничего этого не нужно, вы ни в чём не виноваты. Пожалуйста, [girl.name], молю вас. Вы согласны выйти за меня замуж?'
      '[girl.name] прикусывает губу и, немного помолчав, резко кивает.'
      $ text = u'Пленница была спасена. Но случившееся покосило её, и %s решила уйти в монастырь. Но у рыцаря были иные планы. %s предложил %s выйти за него замуж, и она, после недолгих колебаний, согласилась.\n\n' % (girl.name, knight.name,girl.name_d)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
#    '[game.dragon.level], [game.girl.girl_id]'
    hide bg
    nvl clear
    $ current_image='img/scene/marrige.jpg'
    show expression current_image as bg
    $ text = '%s и %s торжественно обвенчались в столичном соборе при огромном стечении народа. Воистину, это история со счастливым концом!' % (knight.name,girl.name)
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.live('marrige_to_knight',current_image)
    $ knight.die()
    return

label lb_event_knight_challenge_start(knight,repeate=False):
    show screen controls_overwrite
    scene
    show expression "img/scene/arrive.jpg" as bg
    nvl clear
    $ game.foe = knight
#    "[knight.title] нашёл логово, где спит [game.dragon.name] [game.dragon.surname], и вызывает его на бой."
    if not repeate:
      knight "Выходи, подлый [game.dragon.kind], на честной бой, на побраночку!!!"
    $ narrator(knight.intro % game.format_data)
    $ narrator(show_chances(knight))  #TODO: уровень опасности боя
    menu:
        "Принять вызов и защитить логово":
            "Вы вступаете в бой"
            return
        'Подготовиться к бою, сотворив заклинание' if game.dragon.mana > 0:
            if game.choose_spell(u"Вернуться к битве"):
                python:
                    game.dragon.drain_mana()
            call lb_event_knight_challenge_start(knight,repeate=True) from _call_lb_event_knight_challenge_start_1
            return
        "Бежать и бросить логово":
            # Тут, неверное должна быть проверка на успех побега дракона от рыцаря, но ее нет. (Нет, не нужна. Побег всегда успешен, просто дракон теряет логово, золото и баб - OH)
            $ knight.battle_decision = False
            hide bg
            show expression "img/bg/special/knight_sucsess.jpg" as bg
            $ game.girls_list.knight_free_all_girls()
#            $ game.lair.treasury= 0
            if random.choice(range(4)) in range(3): # 75% что рыцарь останется
              knight "Я все равно тебя найду!"
            else:
              knight "Ты подлый трус, [game.dragon.kind]. Такой враг меня не достоин"
              $ knight.die()
            $ game.create_lair()
            return

label lb_event_knight_challenge_end(knight, result):
    show screen controls_overwrite
    if result in ["defeat", "retreat"]:
      "Дракон был повержен доблестным рыцарем."
    if result in ["win"]:
      "Дракон разорвал в клочья рыцаря."
# Приобретает спутницу
      if knight.items["follower"] is None:
        return
      if knight.items["follower"].name == "Ясновидящая спутница":
        $ description = game.girls_list.new_girl(girl_type='peasant',girl_nature='innocent',girl_year=game.knight.year)
        $ text = u'%s рано открыла в себе дар ясновидения. С его помощью она пыталась помочь людям, но те редко внимали её советам, считая %s слегка блаженной. Она не обижалась.\n\nКогда %s выросла, то осознала, что должна помочь людям одолеть дракона. Она нашла отважного рыцаря и присоединлась к нему. Увы, несмотря на все старания гадалки, %s проиграл дракону, и %s заполучил небольшой, но приятный бонус. \n\n' % (game.girl.name,game.girl.name_v,game.girl.name,game.knight.name,game.dragon.fullname)
        $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
        'Все силы ясновидящей спутницы рыцаря оказались бесполезны. [game.dragon.fullname] с лёгкостью поймал беззащитную девицу.'
        nvl clear
        game.girl.third "[description]"
        call lb_nature_sex from _call_lb_nature_sex_53
    return
