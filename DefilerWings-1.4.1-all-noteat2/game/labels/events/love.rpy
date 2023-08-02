# coding=utf-8

init python:
    from pythoncode.utils import get_random_image

label lb_new_love_smuggler:  # Девушка встречает контрабандиста
    call lb_girl_waits from _call_lb_girl_waits
    game.girl.love 'Что. Здесь. Происходит!!!'
    'При приближении контрабандиста толпа рассасывается как по волшебству.'
    $ place = game.lair.type_name
    hide bg
    show place as bg
    game.girl 'Спасибо... Иначе меня бы съели!'
    game.girl.love 'Не за что. Это просто моя работа.'
    ### nvl clear
    'Обычный разговор. Обычная ситуация. И вдруг...'
    hide bg
    show expression 'img/bg/love/love.jpg' as bg
    ### nvl clear
    'Это было подобно удару грома. Подобно молнии, соединившей два сердца. [game.girl.name] и [game.girl.love.name] смотрят друг на друга и понимают...'
    game.girl 'Я люблю тебя.'
    game.girl.love 'Я люблю тебя!'
    ### nvl clear
    'Девушку больше не волнуют ни дракон, ни бесчестье, ни весьма вероятная смерть. Любимый рядом, и это всё, что имеет значение. '
    hide bg
    show expression 'img/bg/love/romantic_couple.jpg' as bg
    ### nvl clear
    'Забившись в уголок, [game.girl.name] и [game.girl.love.name] сидят, прижавшись друг к другу. '
    game.girl.love 'Нам надо бежать. Но сейчас это невозможно. Слишком бдительная охрана, слишком сложно добраться до обжитых мест. Боюсь, придётся ждать до следующего года.'
    '[game.girl.love.name] отчётливо содрогается.'
    game.girl.love 'При одной мысли о том, что может сотворить с тобой дракон, я схожу с ума!'
    '[game.girl.name] гладит мужчину по плечу.'
    game.girl 'Не бойся. Ты со мной, и это главное.'
    $ text = u'%s влюбилась в контрабандиста по имени %s, и он ответил ей взаимностью. Они задумали бежать на следующий год. \n' % (game.girl.name, game.girl.love.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.write_image('img/bg/love/romantic_couple.jpg',game.dragon.level,game.girl.girl_id)
    ### nvl clear
    if game.girl.virgin:
      if game.girl.nature == 'innocent':
        call lb_nls_innocent_sex from _call_lb_nls_innocent_sex
      elif game.girl.nature == 'proud':
        call lb_nls_proud_sex from _call_lb_nls_proud_sex
      elif game.girl.nature == 'lust':
        call lb_nls_lust_sex from _call_lb_nls_lust_sex
    else:
        call lb_nls_pregnant from _call_lb_nls_pregnant
    return


label lb_girl_waits:  # Девушка ждёт свою истинную любовь
    $ place = game.lair.type_name
    hide bg
    show place as bg
    ### nvl clear
    if game.girl.type == 'peasant':
        '[game.girl.name] слоняется по драконьему логову. Ящер спит, стражники неусыпно бдят, наружу не выбраться: это она проверила в первую очередь. Девушка вздыхает: как же ей хочется попасть домой! Пусть опять придётся работать от рассвета до заката, прясть пряжу, ухаживать за коровами, целыми днями под жарким солнцем собирать грибы и ягоды... Только бы вырваться из этого кошмара!  В последнее время драконьи слуги смотрят на неё необычайно голодными глазами...'
    elif game.girl.type == 'citizen':
        '[game.girl.name] слоняется по драконьему логову. Ящер спит, стражники неусыпно бдят, наружу не выбраться: это она проверила в первую очередь. Девушка вздыхает: неужели ей не удастся попасть домой? Папа богат, но, похоже, всё его состояние не способно вытащить её отсюда. Интересно, если предложить дракону денег, он её отпустит? Всё что угодно, только бы вырваться из этого кошмара!  В последнее время драконьи слуги смотрят на неё необычайно голодными глазами...'
    elif game.girl.type == 'princess':
        '[game.girl.name] слоняется по драконьему логову. Ящер спит, стражники неусыпно бдят, наружу не выбраться: это она проверила в первую очередь. Девушка вздыхает: где же прекрасные принцы и могучие рыцари, когда они так нужны? Целый калейдоскоп балов и приёмов, танцы, поцелуи под луной, клятвы в вечной верности... теперь всё это и гроша ломаного не стоит. Неужели никто не вытащит её из этого кошмара?! В последнее время драконьи слуги смотрят на неё необычайно голодными глазами...'
    elif game.girl.type == 'elf':
        '[game.girl.name] слоняется по драконьему логову. Ящер спит, стражники неусыпно бдят, наружу не выбраться: это она проверила в первую очередь. Девушка вздыхает: как бы ей хотелось ещё раз пройти под кронами священных лесов, испить из хрустально-чистых источников, залезть на Великое Древо... Увы, даже вся мощь богини Дану не в силах вырвать её из этого кошмара! В последнее время драконьи слуги смотрят на неё необычайно голодными глазами...'
    elif game.girl.type == 'mermaid':
        '[game.girl.name] плескается в небольшом бассейне. Ящер спит, стражники неусыпно бдят, наружу не выбраться: это она проверила в первую очередь. Девушка вздыхает: как бы ей хотелось ещё раз окунуться в воды родного океана, поиграть со стайками рыбок, позагорать под ласковыми лучами летнего солнца... Увы, даже вся мощь Дагона не в силах вырвать её из этого кошмара! В последнее время драконьи слуги смотрят на неё необычайно голодными глазами...'
    else:
        'Ой, а мне текст-то не написали!'
    hide bg
    if ('servant' in game.lair.upgrades): 
        $ current_image ='img/scene/spawn/kobold.jpg'          
    elif ('gremlin_servant' in game.lair.upgrades):
        $ current_image ='img/bg/special/gremlins.jpg' 
    show expression current_image
    pause (500.0)
    hide expression current_image
    show expression current_image as bg
    game.girl 'Ой...'
    ### nvl clear
    'Драконьи слуги окружают девушку, плотоядно облизываясь и что-то обсуждая между собой. В их руках как по волшебству появляются различные соусы и приправы, пятеро коротышек несут огромный острый вертел.'
    game.girl 'Нееет!!!'
    return

# Новая любовь, принятие решения о сексе.
label lb_nls_innocent_sex:
    '[game.girl.name] судорожно сцепляет руки в замок.'
    game.girl 'Хотя мне всё равно страшно. За год дракон наверняка обесчестит меня, а это страшно, и больно, и...'
    '[game.girl.name] с рыданиями утыкается в грудь мужчины. [game.girl.love.name] ласково гладит её по голове.'
    game.girl.love 'Говорят, это можно пережить. Не знаю как, но можно. Только... только не накладывай на себя руки, молю тебя!'
    if  (random.randint(1,5) == 1):
      $ game.girl.virgin = False
      '[game.girl.name] смотрит в пространство отсутствующим взглядом.'
      game.girl 'Это позор. Это невыносимый позор. Но лучше уж так, чем...'
      game.girl 'Пусть моя невинность достанется тебе, а не дракону. Пожалуйста, возьми меня!'
      $ text = u'%s решила, что человек - это лучше, чем дракон, и отдала свою невинность любимому. \n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_nls_first_sex from _call_lb_nls_first_sex
    else:
      '[game.girl.name] заторможенно кивает. В её голосе сквозит обречённость.'
      game.girl 'Я переживу это, любимый. Дракон пока не приставал ко мне. Может быть, всё обойдётся?'
      $ text = u'%s испугалась позора и решила остаться невинной. \n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_nls_proud_sex:
    '[game.girl.name] гордо вскидывает голову.'
    game.girl 'Да, мне страшно. За год дракон наверняка изнасилует меня, и это будет невыносимо больно. Но я переживу. Теперь мне есть, ради чего жить.'
    '[game.girl.love.name] осторожно прижимает девушку к себе и гладит её по голове.'
    game.girl.love 'Говорят, это пережили уже многие несчастные. Ты справишься. Ты сильная. Только, умоляю, не груби дракону!'
    if  (random.randint(1,3) == 1):
      $ game.girl.virgin = False
      '[game.girl.name] смотрит в пространство, что-то прикидывая для себя, а потом добавляет с нервным смешком.'
      game.girl 'Ну надо же. Никогда на парней внимания не обращала, и о свадьбе особо не мечтала. А теперь...'
      game.girl 'Пусть моя невинность достанется тебе, а не дракону. Трахни меня!'
      $ text = u'%s решила хоть в чём-то уязвить дракона и отдала свою невинность любимому. \n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_nls_first_sex from _call_lb_nls_first_sex_1
    else:
      '[game.girl.name] смотрит в пространство, что-то прикидывая для себя, а потом добавляет с лёгким сожалением.'
      game.girl 'Я бы предложила меня трахнуть, но дракон может отнестись к этому весьма нервно. Подождём до следующего года, ладно?'
      $ text = u'%s решила не гневить дракона и осталась невинной. \n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_nls_lust_sex:
    '[game.girl.name] плотоядно облизывает губы.'
    game.girl 'А знаешь, мне ни капельки не страшно. Наоборот, я расстроилась, когда дракоша лёг спать, не посмотрев в мою сторону. Мне хочется ощутить его кол внутри себя. Теперь... ты меня презираешь, да?'
    '[game.girl.love.name] крепко прижимает девушку к себе и гладит её по голове.'
    game.girl.love 'Ничуть. Я рад. Я счастлив, что предстоящее для тебя - не трагедия, а большое и интересное приключение! Ведь... я всё равно не могу тебя защитить.'
    if  (random.randint(1,2) == 1):
      $ game.girl.virgin = False
      '[game.girl.name] смотрит в пространство, что-то прикидывая для себя, а потом добавляет томным голосом.'
      game.girl 'Не, чушь. Ты и в подмётки не годишься этой жалкой ящерице.'
      game.girl 'Пусть моя невинность достанется тебе, а не дракону. Выеби меня!'
      $ text = u'%s с превеликим энтузиазмом отдала свою невинность любимому. \n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_nls_first_sex from _call_lb_nls_first_sex_2
    else:
      '[game.girl.name] смотрит в пространство, что-то прикидывая для себя, а потом добавляет с искренним сожалением.'
      game.girl 'Я бы предложила меня трахнуть, но тогда мне не видать секса с драконом. Подождём до следующего года, ладно?'
      $ text = u'%s решила, что дракон - это круче, чем человек, и осталась невинной \n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_nls_pregnant:
    if game.girl.nature == 'innocent':
      '[game.girl.name] судорожно сцепляет руки в замок.'
      game.girl 'Всё равно худшее уже произошло. Дракон обесчестил меня, и это было страшно, и больно, и...'
      '[game.girl.name] с рыданиями утыкается в грудь мужчины. [game.girl.love.name] ласково гладит её по голове.'
      game.girl.love 'Ты это пережила. Самое страшное уже позади. Скоро дракон о тебе и забудет. Только... только не накладывай на себя руки, молю тебя!'
      if  (random.randint(1,3) == 1):
        '[game.girl.name] смотрит в пространство отсутствующим взглядом.'
        game.girl 'Я опозорена и обесчещена навеки. Моё тело осквернено и поругано. Я не имею права просить о таком, но...'
        game.girl 'Пожалуйста, возьми меня!'
        $ text = u'%s решила вытеснить неприятные воспоминания и занялась сексом с контрабандистом. \n\n' % (game.girl.name)
        call lb_nls_pregnant_sex from _call_lb_nls_pregnant_sex
      else:
        '[game.girl.name] заторможенно кивает. В её голосе сквозит обречённость.'
        game.girl 'Я переживу это, любимый. Скоро этот кошмар хоть как-то, но кончится. Просто будь рядом, ладно?'
        $ text = u'%s под впечатлением от пережитого не решилась на секс с контрабандистом. \n\n' % (game.girl.name)
    elif game.girl.nature == 'proud':
      '[game.girl.name] гордо вскидывает голову.'
      game.girl 'Ничего, дракон уже изнасиловал меня. Было больно, но я пережила. Осталось  жить дальше. Теперь мне есть, ради чего жить.'
      '[game.girl.love.name] осторожно прижимает девушку к себе и гладит её по голове.'
      game.girl.love 'Самое страшное уже позади. Ты справишься. Ты сильная. Только, умоляю, не груби дракону!'
      '[game.girl.name] смотрит в пространство, что-то прикидывая для себя, а потом добавляет с нервным смешком.'
      game.girl 'Ну надо же. Никогда на парней внимания не обращала, и о свадьбе особо не мечтала. А теперь...'
      game.girl 'Пусть дракон подавится, ящерица облезлая. Трахни меня!'
      $ text = u'%s решила хоть в чём-то уязвить дракона и занялась сексом с контрабандистом. \n\n' % (game.girl.name)
      call lb_nls_pregnant_sex from _call_lb_nls_pregnant_sex_1
    elif game.girl.nature == 'lust':
      '[game.girl.name] плотоядно облизывает губы.'
      game.girl 'Ты сочтёшь меня извращенкой, но мне безумно понравился секс с драконом. Я хотела бы повторить, вот только его интересуют только девственницы. Каждую ночь мне снится, как его кол вновь входит в меня. Теперь... ты меня презираешь, да?'
      '[game.girl.love.name] крепко прижимает девушку к себе и гладит её по голове.'
      game.girl.love 'Ничуть. Я рад. Я счастлив, что произошедшее для тебя - не трагедия, а большое и интересное приключение! Ведь... я всё равно не смог тебя защитить.'
      '[game.girl.name] смотрит в пространство, что-то прикидывая для себя, а потом добавляет томным голосом.'
      game.girl 'Не, чушь. Жалкая ящерица тебе и в подмётки не годится..'
      game.girl 'Хочу сравнить ощущения. Выеби меня!'
      $ text = u'%s решила сравнить впечатления и занялась сексом с контрабандистом. \n\n' % (game.girl.name)
      call lb_nls_pregnant_sex from _call_lb_nls_pregnant_sex_2  
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_nls_first_sex:
    ### nvl clear
    $ current_image=get_random_image("img/bg/love/sex")
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image
    pause (500.0)
    hide expression current_image
    show expression current_image as bg
    'Любовники не торопятся. После поцелуев [game.girl.love.name] переходит к прелюдии. Он разминает плечи девушки, аккуратно ласкает груди, гладит живот, постепенно спускаясь всё ниже и ниже. [game.girl.name] замирает, прислушиваясь к странным, никогда не испытанным ощущениям. В животе как будто порхает стая бабочек. Мужчина аккуратно и нежно ласкает её увлажнившееся лоно языком, вызывая волны удовольствия'
    game.girl 'О... войди в меня!'
    'В первый раз действительно было больно. Но совсем чуть-чуть.'
    return

label lb_nls_pregnant_sex:
    ### nvl clear
    $ current_image=get_random_image("img/bg/love/sex")
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image
    pause (500.0)
    hide expression current_image
    show expression current_image as bg
    'Любовники не торопятся. После поцелуев [game.girl.love.name] переходит к прелюдии. Он разминает плечи девушки, аккуратно ласкает груди, гладит растущий живот, постепенно спускаясь всё ниже и ниже. [game.girl.name] замирает, прислушиваясь к странным, никогда не испытанным ощущениям. С драконом всё было иначе: страшно, грубо, больно. А теперь в животе как будто порхает стая бабочек. Мужчина аккуратно и нежно ласкает её увлажнившееся лоно языком, вызывая волны удовольствия'
    game.girl 'О... войди в меня!'
    'В отличие от дракона, контрабандист смог доставить девушке удовольствие.'
    return

label lb_knight_kills_smuggler: # Рыцарь убивает разбойника
    game.knight 'Сударыня, подлая ящерица сбежала. Вы свободны! Для меня будет честью проводить вас до цивилизованных мест.'
    game.girl 'А что стало с контрабандистами, охранявшими логово?'
    game.knight 'Вам нет нужды переживать, сударыня! Подлые негодяи приняли смерть от моего меча.'
    $ current_image="img/bg/love/drowned.jpg"
    show expression current_image
    pause (500.0)
    hide expression current_image
    show expression current_image as bg
    $ text = u'Пленница узнала, что её возлюбленный убит доблестным рыцарем. Во время одного из привалов %s подошла к реке. И утопилась.  \n\n' % (game.girl.name)
    $ narrator(text)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('drowned',current_image)
    hide bg
    show expression "img/bg/special/knight_sucsess.jpg" as bg
    return

label lb_love_execution_smuggler_cripple:
    game.dragon.third 'Кажется, [game.girl.name] спуталась с человеком. Верность мяса дракона не интересует... но игра может быть забавной!'
    game.dragon '[game.girl.love.name]!'
    game.girl.love 'Да, мой лорд?'
    game.dragon 'Убей свою девушку. Немедленно.'
    game.girl.love 'Мой лорд, если мне будет позволено высказаться, то я поведаю о более изящном решении этого вопроса.'
    game.dragon 'Да?'
    game.girl.love 'Вам стоит продать это мясо сумасшедшему алхимику. Ему всегда требуется новый материал для исследований, и жертва при этом испытывает невыносимые страдания. И выгодно, и приятно!'   
    game.dragon 'О какой сумме идёт речь?'
    game.girl.love '2000 фартингов'     
    game.dragon 'Заткнись и бери [game.girl.name_v]!'
    $ game.lair.treasury.money += 2000
    $ text = u'По совету контрабандиста дракон продал %s сумасшедшему алхимику.\n\n' % (game.girl.name_v)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    call lb_love_alchemist_cripple from _call_love_alchemist_cripple_1
    return

label lb_love_alchemist_cripple:
    if game.girl.pregnant > 0:
      python: #делаем аватарку алхимика для диалогового окна
        alchemist= Talker(game_ref=game)
        alchemist.avatar = "img/avahuman/alchemist.jpg"
        alchemist.name = 'Безумный алхимик'  
      ### nvl clear
      $ current_image="img/bg/love/alchemist.jpg"          
      hide bg
      show expression current_image as bg
      '[game.girl.name] лежит, распластанная на каменном столе, в каком-то тёмном и мрачном подземелье. Она в панике озирается по сторонам. На полках стоят запылённые тома, колбы со булькающими жидкостями и засушенные части животных и людей. Воздух наполнен странными, едкими запахами. Сморщенный старичок с седенькой бородкой щупает её растущий животик и что-то приговаривает себе под нос. Улыбающиеся скелеты не дают усомниться в дальнейшей судьбе девушки.'
      game.girl 'Ааа...'
      'Ей хочется бежать отсюда без оглядки, но без рук и ног это сделать весьма затруднительно.'
      game.girl.love 'Ха! Наконец-то я избавился от этой пустоголовой шлюхи. Если бы вы только знали, как мне надоело заботиться об этом обрубке!'
      alchemist 'Вы правильно сделали, что донесли сюда образец. Он уникальный, уникальнейший! Заполучить плод дракона и человеческой самки - более того, искалеченной человеческой самки... о, это стоит каждого отданного фартинга!'
      game.girl.love 'Скажите, уважаемый, она будет сильно страдать?'
      alchemist 'Причинение боли - лишь средство, а не самоцель. От моих опытов ещё ни один из подопытных не умирал... в смысле, в своём уме - не умирал.'
      'Сумасшедший алхимик капает на живот девушки каплю какого-то зелья. Подземелье сотрясает безумный крик.'
      $ text = u'Заполучив %s в своё полное распоряжение, %s продал её алхимику на опыты. \n\n' % (game.girl.name_v,game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ game.chronik.death('alchemist_cripple',current_image)
      hide expression current_image
      ### nvl clear
    else:
      assert "Roman of smuggler and blind"
    return

label lb_love_execution_smuggler: #Дракон казнит девушку с помощью контрабандиста
    game.dragon.third 'Кажется, [game.girl.name] спуталась с человеком. Верность мяса дракона не интересует... но игра может быть забавной!'
    game.dragon '[game.girl.love.name]!'
    game.girl.love 'Да, мой лорд?'
    game.dragon 'Убей свою девушку. Немедленно.'
    game.girl.third '[game.girl.name] резко бледнеет. Её губы дрожат. Она шепчет дрожащим голосом.'
    if game.girl.blind:
      game.girl 'Пожалуйста, любимый... сделай так, как сказал [game.dragon.name]. Всё равно дракон ослепил меня, мне нет смысла жить дальше...'
      game.girl.love 'Разумеется, моя дорогая, я сделаю это! Неужели ты хоть на миг вообразила, что я люблю тебя? Ха! Чокнутый алхимик дал бы за тебя и твоего нерождённого ублюдка несусветную цену. Ради таких денег стоило немного покорчить из себя влюблённого придурка. Но моя жизнь мне всяко дороже.'

    else:
      game.girl 'Пожалуйста, любимый... сделай так, как сказал [game.dragon.name]. Может быть, хоть ты останешься в живых...'
      game.girl.love 'Разумеется, моя дорогая, я сделаю это! Неужели ты хоть на миг вообразила, что я люблю тебя? Ха! На рынках Султаната за девушку, побывавшую в лапах дракона, дают сумасшедшие деньги. Ради них стоило немного покорчить из себя влюблённого придурка. Но моя жизнь мне всяко дороже.'
    game.girl 'Нет... ты так не считаешь, ты вовсе не такой! Я не верю в это!'
    game.girl.love 'Верь во что хочешь. Мой лорд, как именно мне прикончить эту пустоголовую шлюшку?'
    ### nvl clear
    menu:
        'Отруби ей голову':
          game.dragon 'Да отрежь ей голову, и дело с концом.'
          game.girl.love 'Как скажите, мой лорд. Хотя, как по мне, слишком лёгкий конец для этой дуры.'
          $ current_image=get_random_image("img/bg/love/execution/beheaded")
          hide bg
          show expression current_image
          pause (500.0)
          hide expression current_image
          show expression current_image as bg
          if game.girl.blind:
            game.girl.love.third '[game.girl.love.name], улыбаясь, пододит к испуганно замершей девушке и достаёт свой клинок. [game.girl.name] слепо мотает головой и что-то шепчет - то ли умоляет, то ли молится, то ли просит прощения. Мужчина хватает её за волосы, оттягивает их назад и погружает отточеную сталь в женское горло.'
          else:
            game.girl.love.third '[game.girl.love.name], улыбаясь, пододит к испуганно замершей девушке и достаёт свой клинок. [game.girl.name] смотрит на него широко открытыми от ужаса глазами и что-то шепчет - то ли умоляет, то ли молится, то ли просит прощения. Мужчина хватает её за волосы, оттягивает их назад и погружает отточеную сталь в женское горло.'
          game.girl.love.third '[game.girl.name] хрипит и дёргается, из новосозданного рта толчками бьёт кровь, но контрабандист лишь продолжает своё дело, неторопливо, с холодной улыбкой на лице. Наконец жертва затихает, и [game.girl.love.name] одним движением отсекает ей голову.'
          $ text = u'По приказу дракона %s неспешно и с удовольствием отрезал девушке голову. \n\n' % (game.girl.love.name)
          $ game.chronik.death('beheaded',current_image)
        'Задуши её':
          game.dragon 'Задуши её. Хочу полюбоваться, как она будет бороться ещё за один глоток воздуха.'
          game.girl.love 'Это будет великолепная борьба, мой лорд!'
          $ current_image=get_random_image("img/bg/love/execution/choked")
          hide bg
          show expression current_image
          pause (500.0)
          hide expression current_image
          show expression current_image as bg
          if game.girl.blind:
            game.girl.love.third '[game.girl.love.name], улыбаясь, подходит к испуганно замершей девушке и достаёт свою удавку. [game.girl.name] слепо мотает головой и что-то шепчет - то ли умоляет, то ли молится, то ли просит прощения. Мужчина обходит её и захлёстывает тонкой верёвкой женское горло.'
          else:
            game.girl.love.third '[game.girl.love.name], улыбаясь, подходит к испуганно замершей девушке и достаёт свою удавку. [game.girl.name] смотрит на него широко открытыми от ужаса глазами и что-то шепчет - то ли умоляет, то ли молится, то ли просит прощения. Мужчина обходит её и захлёстывает тонкой верёвкой женское горло.'
          game.girl.love.third '[game.girl.name] хрипит и дёргается, беспорядочно машет руками, пытаясь оттлокнуть своего убийцу. [game.girl.love.name] не торопится, душит долго, иногда приотпуская удавку и давая жертве продлить свои мучения. Наконец он захлёстывает верёвку намертво, и скоро женское тело бьют последние судороги. Для верности подождав ещё пару минут, [game.girl.love.name] отталкивает бездыханный труп. '
          $ text = u'По приказу дракона %s неспешно и с удовольствием задушил девушку удавкой. \n\n' % (game.girl.love.name)
          $ game.chronik.death('choked',current_image)
        'Выпусти ей кишки':
          game.dragon 'Выпусти ей кишки. Медленно. Хочу насладиться её агонией.'
          game.girl.love 'Вы не представляете, как я рад это слышать, мой лорд! Именно это я хотел сделать всё время, пока сюсюкался с этой сукой.'
          $ current_image=get_random_image("img/bg/love/execution/gutted")
          hide bg
          show expression current_image
          pause (500.0)
          hide expression current_image
          show expression current_image as bg
          if game.girl.blind:
            game.girl.love.third '[game.girl.love.name], улыбаясь, подходит к испуганно замершей девушке, опрокидывает её на пол и достаёт свой клинок. [game.girl.name] дрожит крупной дрожью и что-то шепчет - то ли умоляет, то ли молится, то ли просит прощения. Мужчина неторопливо погружает отточенное лезвие в её нежный животик.'
          else:
            game.girl.love.third '[game.girl.love.name], улыбаясь, подходит к испуганно замершей девушке, опрокидывает её на пол и достаёт свой клинок. [game.girl.name] смотрит на него широко открытыми от ужаса глазами и что-то шепчет - то ли умоляет, то ли молится, то ли просит прощения. Мужчина неторопливо погружает отточенное лезвие в её нежный животик.'
          game.girl.love.third 'Логово сотрясает истошный крик. [game.girl.name] вырывается, молит о милосердии, дёргается - всё бесполезно. [game.girl.love.name] глядит в глаза своей жертвы, улыбается и начинает неспешно доставать из живота ленту кишечника. Девушка борется, пытается запихнуть "как было", но контрабандист вновь достаёт их наружу. [game.girl.name] быстро слабеет, её крики становятся более тихими и жалостливыми. [game.girl.love.name] продолжает неспешную экзекуцию. Сегодня у него ещё много работы. '
          $ text = u'По приказу дракона %s неспешно и с удовольствием выпустил девушке кишки. \n\n' % (game.girl.love.name)
          $ game.chronik.death('gutted',current_image)
    ### nvl clear
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    'После [game.dragon.name] и [game.girl.love.name] мирно поговорили за жизнь, полакомившись телом их общей любовницы. [game.girl.name] - истинный деликатес!'    
    return

label lb_love_execution_both_smuggler_cripple:
    game.dragon 'Почему бы мне не казнить обоих изменников? Не вижу ни единого довода "против"!'
    game.dragon '[game.girl.love.name]!'
    game.girl.love 'Да, мой лорд?'
    game.dragon 'Я слышал, что ты связался с моим трофеем?'
    game.girl.love 'Мой лорд, я...'
    game.dragon 'О, не беспокойся, верность мяса меня не волнует. Мне даже интересно было бы посмотреть на процесс совокупления у людей.'
    $ current_image= game.girl.cripple_image
    show expression current_image as bg
    pause (1.5)
    game.girl.love 'Эээ...'
    game.dragon 'Смелее, смелее! Ты же не хочешь нарушить мой приказ, верно?'
    ### nvl clear
    '[game.girl.love.name] раздевается и неуверенно подходит к [game.girl.name_d], растерянно хлопающей глазами. Чувствуется, что вся эта ситуация его изрядно напрягает.'
    'Тем не менее, возбуждение пересиливает. [game.girl.love.name] начинает совершать характерные движения, сначала медленно, потом всё быстрее и быстрее. Кажется, необычное состояние партнёрши пришлось ему по вкусу. Он быстро подбирается к самому пику, и в миг наибольшего белаженства...'
    game.dragon 'Паралич!'
    ### nvl clear
    '...дракон накладывает на любовников заклятье паралича.'
    game.dragon 'Так, теперь надо отрезать мужчине руки и ноги и погрузить парочку в какую-нибудь прозрачную смолу. И в моём логове будет храниться уникальное произведение искусства!'
    game.dragon 'Эта скульптура будет вечной.'
    $ text = u'Измена вскрылась. Дракон велел контрабандисту заняться сексом с %s, в самый пикантный момент парализовал обоих, отрезал мужчине руки и ноги и залил получившуюся композицию прозрачной смолой.\n\nВозможно, в далёком будущем эта скульптура приобретёт огромную художественную ценность!' %(game.girl.name_t)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('couple_sculpture',current_image)
    return

label lb_love_execution_both_smuggler: # Смерть обоих
    game.dragon 'Где же эти изменники? Как только найду - казню обоих!'
    game.girl.third 'Ой...'
    hide bg
    ### nvl clear
    show expression "img/bg/love/couple_death.jpg" as bg
    if game.girl.blind:
      'После потери зрения слух у [game.girl.name_r] чрезвычайно обострился. Она услышала слова, случайно оброненные драконом, и сумела быстро отыскать своего возлюбленного. [game.girl.love.name] сначала не согласился c её планом, но потом признал, что это единственный выход.'
    else:
      'Случайно подслушав слова дракона, [game.girl.name] прибежала к своему возлюбленному. [game.girl.love.name] сначала не согласился c её планом, но потом признал, что это единственный выход.'
    'Возлюбленные выпили яд. [game.dragon.fullname] нашёл лишь их остывшие трупы.'
    $ text = u'Осозновая, что их измена вскрылась и дракон непременно казнит обоих, возлюбленные приняли яд. \n\n' 
    ### nvl clear
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('couple_death',"img/bg/love/couple_death.jpg")
    return

label lb_love_escape_smuggler_cripple:
    if game.girl.pregnant > 0:
      game.girl.love.third '[game.girl.love.name] презрительно пинает беспомощное тело [game.girl.name_r]. Алхимик дал бы хорошую цену за инвалидку, вот только нечего и думать вынести её из логова!'
      $ text = u'Узнав о трагедии, случившейся с %s, %s бросил свою бывшую возлюбленную, пнув её напоследок.\n\n' % (game.girl.name_t, game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ game.girl.love = None
    else:
      assert "Roman of smuggler and cripple"
    return

label lb_love_smuggler_cripple:
    if game.girl.pregnant > 0:
      hide bg
      ### nvl clear
      show expression game.girl.cripple_image as bg
      game.girl.love.third '[game.girl.love.name] нежно гладит беспомощное тело [game.girl.name_r]. Инвалидка смотрит на него молящим взглядом.'
      game.girl.love 'Всё будет хорошо, моя дорогая. Я знаю, где за тебя дадут отличную цену!'
      $ text = u'%s оказалась в полном распоряжении своего возлюбленного.\n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_love_alchemist_cripple from _call_love_alchemist_cripple_3
    else:
      assert "Roman of smuggler and cripple"
    return

label lb_love_escape_smuggler_blind:
    if game.girl.pregnant > 0:
      ### nvl clear
      hide bg
      show expression "img/bg/love/escape.jpg" as bg
      game.girl.love 'Как ты?'
      game.girl 'Тьма. Вечная тьма. И чувство полной беспомощности.'
      game.girl 'И это будет длиться до конца моих дней. Как хорошо, что ты со мной!'
      game.girl.love 'Да, любимая. Я буду с тобой до конца твоих дней.'
      $ text = u'Хотя дракон ослепил %s, она и %s успешно сбежали из логова дракона. ' % (game.girl.name_r, game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      python: #делаем аватарку алхимика для диалогового окна
        alchemist= Talker(game_ref=game)
        alchemist.avatar = "img/avahuman/alchemist.jpg"
        alchemist.name = 'Безумный алхимик'  
      ### nvl clear
      $ current_image="img/bg/love/alchemist.jpg"          
      hide bg
      show expression current_image as bg
      game.girl 'Что происходит? Где мы? Мне страшно!'
      '[game.girl.name] лежит, распластанная на каменном столе, в каком-то тёмном и мрачном подземелье. Она не видит окружающей обстановки - пожалуй, что к счастью для себя. На полках стоят запылённые тома, колбы со булькающими жидкостями и засушенные части животных и людей. Воздух наполнен странными, едкими запахами. Сморщенный старичок с седенькой бородкой щупает её растущий животик и что-то приговаривает себе под нос. Улыбающиеся скелеты не дают усомниться в дальнейшей судьбе девушки.'
      game.girl.love 'Ха! Неужели ты и впрямь решила, что я действительно тебя любил? Ну-ну. Я связался с такой пустоголовой шлюхой, как ты, только чтобы поднакопить побольше деньжат.'
      game.girl.love 'Сначала хотел продать тебя в Султанат, но без глаз ты никому там не нужна! К счастью, подвернулось предложение повыгодней. За твоего ублюдка мне заплатят столько, что мне хватит до конца жизни!'
      alchemist 'Уникальный образец, уникальнейший! Заполучить плод дракона и человеческой самки - более того, слепой человеческой самки... о, это стоит каждого отданного фартинга!'
      game.girl 'Пожалуйста, [game.girl.love.name]...'
      game.girl.love 'Молчать, сука! Мне до смерти надоело сюсюкаться с тупой, беспомощной уродиной! Если бы я знал, что, заботиться о слепой - это такая морока, я бы выпустил тебе кишки на первомм же привале!'
      game.girl.love 'Скажите, уважаемый, она будет сильно страдать?'
      alchemist 'Причинение боли - лишь средство, а не самоцель. От моих опытов ещё ни один из подопытных не умирал... в смысле, в своём уме - не умирал.'
      'Сумасшедший алхимик капает на живот девушки каплю какого-то зелья. Подземелье сотрясает безумный крик.'
      $ text = u'Но их счастье было недолгим: %s продал свою возлюбленную алхимику на опыты. \n\n' % (game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ game.chronik.death('alchemist_blind',current_image)
      hide expression current_image
      ### nvl clear
    else:
      assert "Roman of smuggler and blind"
    return

label lb_love_escape_smuggler: # Побег 
    ### nvl clear
    hide bg
    show expression "img/bg/love/escape.jpg" as bg
    game.girl 'Всё готово? Мы можем идти?'
    game.girl.love 'Да. Припасы собраны, дорога разведана, охранники нас не остановят, погони можно не бояться.'
    game.girl 'Спасена...'
    'Влюблённые сливаются в долгом поцелуе.'
    game.girl.love 'Да. Ты спасена. Пойдём, я приготовил для тебя кое-что очень интересное!'
    $ text = u'%s и %s успешно сбежали от дракона. ' % (game.girl.name, game.girl.love.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    if game.girl.pregnant > 0:
      python: #делаем аватарку алхимика для диалогового окна
        alchemist= Talker(game_ref=game)
        alchemist.avatar = "img/avahuman/alchemist.jpg"
        alchemist.name = 'Безумный алхимик'  
      ### nvl clear
      $ current_image="img/bg/love/alchemist.jpg"          
      hide bg
      show expression current_image as bg
      game.girl 'За что?!'
      '[game.girl.name] лежит, распластанная на каменном столе, в каком-то тёмном и мрачном подземелье. На полках стоят запылённые тома, колбы со булькающими жидкостями и засушенные части животных и людей. Воздух наполнен странными, едкими запахами. Сморщенный старичок с седенькой бородкой щупает её растущий животик и что-то приговаривает себе под нос. Улыбающиеся скелеты не дают усомниться в дальнейшей судьбе девушки.'
      game.girl.love 'Ха! Неужели ты и впрямь решила, что я действительно тебя любил? Ну-ну. Я связался с такой пустоголовой шлюхой, как ты, только чтобы поднакопить побольше деньжат.'
      game.girl.love 'Сначала хотел продать тебя в Султанат, но потом нашёл предложение повыгодней. За твоего ублюдка мне заплатят столько, что мне хватит до конца жизни!'
      alchemist 'Уникальный образец, уникальнейший! Заполучить плод дракона и человеческой самки... о, это стоит каждого отданного фартинга!'
      game.girl 'Пожалуйста, [game.girl.love.name]...'
      game.girl.love 'Молчать, сука! Мне до смерти надоело с тобой сюсюкаться. Удивительно, как я по дороге не выпустил тебе кишки.'
      game.girl.love 'Скажите, уважаемый, она будет сильно страдать?'
      alchemist 'Причинение боли - лишь средство, а не самоцель. От моих опытов ещё ни один из подопытных не умирал... в смысле, в своём уме - не умирал.'
      'Сумасшедший алхимик капает на живот девушки каплю какого-то зелья. Подземелье сотрясает безумный крик.'
      $ text = u'Но их счастье было недолгим: %s продал свою возлюбленную алхимику на опыты. \n\n' % (game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ game.chronik.death('alchemist',current_image)
      hide expression current_image
    else:
      ### nvl clear
      $ current_image="img/bg/love/slave_market.jpg"          
      hide bg
      show expression current_image as bg
      game.girl 'За что?!'
      '[game.girl.name] стоит в ряду других голых девушек. По торговым рядам неспешно прогуливаются покупатели, щупают достоинства товара, деловито обсуждают цены. Рынок рабов, на котором Султанат обменивает человеческие жизни на звонкое золото и душистые пряности. Печальные караваны регулярно тянутся отсюда на юг, через пустыню, в таинственную и страшную страну. Король уже давно собирается запретить такую торговлю... да всё никак не соберётся.'
      game.girl.love 'Ха! Неужели ты и впрямь решила, что я действительно тебя любил? Ну-ну. Я связался с такой пустоголовой шлюхой, как ты, только чтобы поднакопить побольше деньжат. За драконью подстилку султанские вельможи мне столько денег отвалят, что до конца жизни хватит!'
      $ text = u'Но их счастье было недолгим: %s продал свою возлюбленную работорговцам. \n\n' % (game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      ### nvl clear
      $ current_image="img/bg/love/slave_caravan.jpg"          
      hide bg
      show expression current_image as bg
      '"Раскалённым солнцем сжигает кожу, ветер сушит слёзы и ранит веки..."'
      show expression current_image
      pause 500
      hide expression current_image
      game.girl.third '[game.girl.name] медленно бредёт по обжигающему песку в цепочке таких же несчастных рабынь. Зачем? Куда? Как жить после такого предательства? Для чего она вообще существует?'
      game.girl.third 'Мало сил и мало воды, но зато много солнца, песка и ярости надмотрщиков. Каждый день кто-то из девочек остаётся лежать в песках. Возможно, её ждёт та же участь.'
      if  (random.randint(1,5) == 1):
        ### nvl clear
        $ current_image="img/bg/love/bone_desert.jpg" 
        hide bg
        show expression current_image as bg
        $ text = u'%s так никогда и не дошла до Султаната, и ветер веками ласкал её выбеленные кости. \n\n' % (game.girl.name)
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
        $ game.chronik.death('bone_desert',current_image)
        $ narrator(text)
      else:
        '[game.girl.name] благополучно прошла через пустыню и добралась до Султаната.'
        $ game.girls_list.sultan_list.append(game.girl)
#        call lb_sultan from _call_lb_sultan
    return

label lb_sultan:   # Девушка при дворе султана
    ### nvl clear
    $ current_image="img/bg/sultan/sultan.jpg" 
    hide bg
    show expression current_image as bg
    $ text = u'%s благополучно прошла через пустыню, добралась до Султаната и попала в гарем богатого вельможи. Душевные раны со временем начали заживать, и женщина втянулась в местную жизнь. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ narrator(text)
    $ sultanat_trade_ultimate = game.historical_check('sultanat_trade_ultimate')
    if game.girl.nature == 'innocent':
      $ choices = [
        ("lb_sultan_normal_innocent", 60 ),
        ("lb_sultan_crucify", 5),
        ("lb_sultan_scorpion", 5),
        ("lb_sultan_tiger", 5),
        ("lb_sultan_cage", 5),
        ("lb_sultan_peril", 5),
        ("lb_sultan_poison", 5),
        ("lb_sultan_crocodile", 5),
        ("lb_sultan_sands", 5)]
    elif game.girl.nature == 'proud':
      $ choices = [
        ("lb_sultan_normal_proud", 20 ),
        ("lb_sultan_crucify", 20),
        ("lb_sultan_scorpion", 20),
        ("lb_sultan_tiger", 20),
        ("lb_sultan_cage", 20)]
    elif game.girl.nature == 'lust':
      $ choices = [
        ("lb_sultan_normal_lust", 20 ),
        ("lb_sultan_peril", 20),
        ("lb_sultan_poison", 20),
        ("lb_sultan_crocodile", 20),
        ("lb_sultan_sands", 20)]
    if sultanat_trade_ultimate:
      $ enc = weighted_random(choices)
      $ renpy.call(enc)
    else:
      if game.girl.nature == 'innocent':
        call lb_sultan_normal_innocent from _call_lb_sultan_normal_innocent
      elif game.girl.nature == 'proud':
        call lb_sultan_normal_proud from _call_lb_sultan_normal_proud
      elif game.girl.nature == 'lust':
        call lb_sultan_normal_lust from _call_lb_sultan_normal_lust
    return

label lb_sultan_normal_innocent:
    ### nvl clear
    $ current_image="img/bg/sultan/sultan_fate.jpg" 
    hide bg
    show expression current_image as bg
    game.girl.third 'Благодаря тихому и незлобливому нраву [game.girl.name] нашла своё место в гареме. Скука и бесконечная череда однообразных дней не тяготили её, а приносили мир измученной душе. Запутанные и смертоносные интриги скользили мимо неё. Редкие моменты физической близости со своим новым мужем [game.girl.name] встречала спокойно, покорно и безыскусно разыгрывая страсть. Со временем у неё даже появились дети. Одного сына  сделали евнухом, второго - забрали в армию, дочка пошла по стопам матери.'
    $ text = u'Благодаря тихому и незлобливому нраву %s нашла своё место в гареме, родила нескольких детей и скончалась в глубокой старости. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.live('sultan_normal',current_image)
    call lb_sultanat_trade from _call_lb_sultanat_trade
    return

label lb_sultan_normal_proud:
    ### nvl clear
    $ current_image="img/bg/sultan/sultan_fate.jpg" 
    hide bg
    show expression current_image as bg
    game.girl.third '[game.girl.name] смирила свой гордый и независимый нрав, не нагрубив новому мужу при первой встрече, а после - совершенно неожиданно для себя - искренне полюбила его. Хатун попыталась прикончить соперницу, но вельможа неожиданно вернулся с прогулки раньше срока, пресёк безобразие и пришёл в ярость. Мегера приняла мучительную смерть, а [game.girl.name] стала главной и любимой женой. Со временем у неё родились дети, и именно её сын стал наследником отца.'
    $ text = u'Благодаря гордому и независимому нраву %s стала главной и любимой женой, родила нескольких детей и скончалась в глубокой старости. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.live('sultan_fate',current_image)
    call lb_sultanat_trade from _call_lb_sultanat_trade_1
    return

label lb_sultan_normal_lust:
    ### nvl clear
    $ current_image="img/bg/sultan/sultan_fate.jpg" 
    hide bg
    show expression current_image as bg
    game.girl.third 'Благодаря своему распущенному и хитрому нраву [game.girl.name] быстро вписалась в новое место. Она с головой окунулаась в клубок интриг, намереваясь стать главной и любимой женой. Хатун дралась за своё положение как львица, но проиграла. [game.girl.name] жестоко и изощрённо убила свою главную соперницу и заняла её место. Со временем у неё родились дети, и именно её сын стал наследником отца.'
    $ text = u'Благодаря распущенному и хитрому нраву %s устранила всех соперниц, стала главной и любимой женой, родила нескольких детей и скончалась в глубокой старости. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.live('sultan_fate',current_image)
    call lb_sultanat_trade from _call_lb_sultanat_trade_2
    return

label lb_sultan_crucify:
    $ text = u'Но однажды %s прогневала своего мужа, и он приказал распять её. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ narrator (text)
    ### nvl clear
    $ current_image="img/bg/sultan/execution/crucify.jpg" 
    $ game.chronik.death('crucify',current_image)
    hide bg
    show expression current_image as bg
    game.girl.third 'Пить'
    game.girl.third 'Как же хочется пить. Кажется, солнце прожаривает тело насквозь. '
    game.girl.third 'Дышать. Каждый вздох даётся с трудом. Чтобы глотнуть побольше воздуха, надо напрячь мышцы рук и ног и приподняться вверх. Но с каждым часом  конечности слушаются всё хуже и хуже. Уже недалёк тот миг, когда не останется сил даже на борьбу с удушьем. И тогда нагретое, обезвоженное тело прекратит свой медленный последний танец.'
    return

label lb_sultan_scorpion:
    $ text = u'Но однажды %s прогневала своего мужа, и он приказал натравить на неё скорпиона. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ narrator (text)
    ### nvl clear
    $ current_image="img/bg/sultan/execution/scorpion.jpg" 
    $ game.chronik.death('scorpion',current_image)
    hide bg
    show expression current_image as bg
    game.girl.third 'Щекотно. Маленькие лапки перебирают по животу, спускаясь всё ниже и ниже. Вскоре они коснуться грудей. [game.girl.name] замерла, стараясь не то что не шевелится - даже не дышать. Но это бесполезно. Щекотка становится мучительной, а палач аккуратно вынимает второго скорпиона.'
    return

label lb_sultan_tiger:
    $ text = u'Но однажды %s прогневала своего мужа, и он приказал скормить её тиграм. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ narrator (text)
    ### nvl clear
    $ current_image="img/bg/sultan/execution/tiger.jpg" 
    $ game.chronik.death('tiger',current_image)
    hide bg
    show expression current_image as bg
    game.girl.third '[game.girl.name] дёргается в путах, но верёвки держат крепко. А рядом уже прогуливаются игриво настроенные кошечки. Очень большие кошечки с острыми когтями и зубами. Что же, по крайней мере это будет быстро. '
    game.girl.third 'Но больно.'
    return

label lb_sultan_cage:
    $ text = u'Но однажды %s прогневала своего мужа, и он приказал посадить её в клетку и вывесить на солнцепёк. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ narrator (text)
    ### nvl clear
    $ current_image="img/bg/sultan/execution/cage.jpg" 
    $ game.chronik.death('cage',current_image)
    hide bg
    show expression current_image as bg
    game.girl.third '[game.girl.name] до крови кусает губы, чтобы хоть как-то смочить распухший язык и потрескавшееся горло. Она здесь... второй день, да? Точно, второй день. А кажется - вечность. В худшем случае [game.girl.name] умрёт завтра. А если повезёт, то сегодня, ещё до захода солнца. Ну должно же ей хоть в чём-то повезти?!! '
    return

label lb_sultan_peril:
    $ text = u'Но однажды %s неудачно ввязалась в интригу, и хатун с помощью евнухов убила её, перетянув живот верёвкой. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ narrator (text)
    ### nvl clear
    $ current_image="img/bg/sultan/execution/peril.jpg" 
    $ game.chronik.death('peril',current_image)
    hide bg
    show expression current_image as bg
    game.girl.third 'Боль. Тонкая верёвка всё туже и туже врезается в живот.  [game.girl.name] мечется, дёргает за концы, пытается ослабить натяжение, умоляет евнухов пощадить её. Бесполезно. Хатун холодно улыбается и сообщает, что ничего непоправимого пока нет.'
    game.girl.third 'Но скоро будет.'
    return

label lb_sultan_poison:
    $ text = u'Но однажды %s неудачно ввязалась в интригу, и хатун угостила её отравленным вином. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ narrator (text)
    ### nvl clear
    $ current_image="img/bg/sultan/execution/poison.jpg" 
    $ game.chronik.death('poison',current_image)
    hide bg
    show expression current_image as bg
    game.girl.third 'Терпкий вкус вина. Одышка, потливость, головокружение. Потеря сознания. Смерть.'
    game.girl.third 'Если судить объективно, всё могло быть хуже. Гораздо, гораздо хуже.'
    return

label lb_sultan_crocodile:
    $ text = u'Но однажды %s неудачно ввязалась в интригу, и хатун с помощью евнухов убила её, скормив крокодилам. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ narrator (text)
    ### nvl clear
    $ current_image="img/bg/sultan/execution/crocodile.jpg" 
    $ game.chronik.death('crocodile',current_image)
    hide bg
    show expression current_image as bg
    game.girl.third '[game.girl.name] дёргается в путах, но верёвки держат крепко. А рядом уже щёлкают челюстями вечно голодные рептилии. Что же, по крайней мере это будет быстро. '
    game.girl.third 'Но больно.'
    return

label lb_sultan_sands:
    $ text = u'Но однажды %s неудачно ввязалась в интригу, и хатун с помощью евнухов убила её, утопив в зыбучих песках. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ narrator (text)
    ### nvl clear
    $ current_image="img/bg/sultan/execution/sands.jpg" 
    $ game.chronik.death('sands',current_image)
    hide bg
    show expression current_image as bg
    game.girl.third '[game.girl.name] постепенно погружается в зыбучий песок. Чем сильнее она пытается вырваться, тем быстрее засасывает её страшная топь. Женщина тянет руку вперёд, но хатун, стоящая в нескольких шагах, лишь негромко смеётся. Вот в песок погрузился живот... груди... вот над поверхностью осталась одна голова. Кажется, всё. '
    return

label lb_sultanat_trade:  # Установка глобальных модификаторов
    python:
      sultanat_trade_basic = game.historical_check('sultanat_trade_basic')
      sultanat_trade_advanced = game.historical_check('sultanat_trade_advanced')
      sultanat_trade_ultimate = game.historical_check('sultanat_trade_ultimate')
    ### nvl clear
    hide bg
    show expression "img/bg/sultan/sultan_glory.jpg" as bg
    if not sultanat_trade_basic:
      'Среди вельмож Султаната ходят слухи о наложницах, познавших близость дракона. Многие хотят заполучить такую жемчужину в свой гарем.'
      $ game.history = historical( name='sultanat_trade_basic',end_year=None,desc=None,image=None)
      $ game.history_mod.append(game.history)
    elif not sultanat_trade_advanced:
      'Слухи о наложницах дракона ширятся. Говорят, эти прелестницы продлевают своим мужьям здоровье, молодость и, самое важное, мужскую силу.'
      $ game.history = historical( name='sultanat_trade_advanced',end_year=None,desc=None,image=None)
      $ game.history_mod.append(game.history)
    elif not sultanat_trade_ultimate:
      'Слухами о наложницах дракона заинтересовался Султан, да живёт Он вечно. Возможно, вскоре в Королевство отправится караван самого Хакима ибн Хакима. '
      $ game.history = historical( name='sultanat_trade_ultimate',end_year=None,desc=None,image=None)
      $ game.history_mod.append(game.history)
    return

label lb_caravan_trade:
    ### nvl clear
    $ game.history = historical( name='caravan_trade',end_year=None,desc=None,image=None)
    $ game.history_mod.append(game.history)
    python: #делаем аватарку Хаким для диалогового окна
      hakim = Talker(game_ref=game)
      hakim.avatar = "img/avahuman/hakim.jpg"
      hakim.name = 'Хаким ибн Хаким'  
    game.dragon.third 'Проснувшись, [game.dragon.name] обнаружил, что до его логова добрался торговый караван из Султаната'
    hakim 'Да будет ваша казна обильной, а чресла могучими, о предобрейший и всемилостевейший...'
    game.dragon 'Э?'
    hakim '...всезлейший и безжалостнейший [game.dragon.fullname]! При одном взгляде на вас душа моя поёт от восторга, а сердце - сияет от радости. Я - Хаким, сын Хакима, сына Хакима, скромный купец из Султаната.'
    game.dragon.third '[game.dragon.name] смотрит на гостя, пытаясь представить поющую душу и сияющее сердце.' 
    hakim 'Моя радость беспредельна, а счастье безмерно. Приветствую, о [game.dragon.fullname], могущественный владетель Королевства и сопредельных стран, которого сапогами попирают из Вселенной...'
    hakim 'Кхм. Разумеется, я хотел сказать - сапоги которого попирают Вселенную!'
    game.dragon 'Где ты видишь на мне сапоги?!!'
    hakim 'Кхм-кхм. Замнём для полной ясности.'
    game.dragon 'И зачем же ты явился, Хаким ибн Хаким?.. Только без цветастости! А то съем!!!'
    hakim 'Знаете ли вы, что за девушек, чей цветок невинности сорван драконом, на рынках Султаната дают хорошие деньги? Я готов покупать у вас пленниц, которые не представляют для вас никакого интереса, кроме гастрономического. Я же обязуюсь давать за них справедливую цену. Фактически себе в убыток буду работать, мамой клянусь!'
    game.dragon.third '[game.dragon.name] задумывается. На первый взгляд, предложение выглядит выгодным: обмен бесполезного мяса на вожделенное золото.'
    game.dragon 'И какую же цену ты считаешь "справедливой"?'
    hakim '100 фартингов за крестьянку, 200 - за горожанку, 300 - за аристократку, 500 за альву.'
    game.dragon 'А за великанш?'
    hakim 'О, достоинства этих выдающихся женщин столь велики, что на их фоне достоинства моих покупателей кажутся сморщенными и жалкими. Боюсь, они не будут пользоваться спросом.'
    game.dragon 'А за русалок?'
    hakim 'Увы, русалка в пустыне - зрелище жалкое и очень скоротечное. Они не выдержат дорожных тягот, слишком суров климат в наших краях. И да, кстати - слепые и искалеченные моих клиентов тоже не интересуют.'
    game.dragon 'Хорошо. Я ничего не обещаю, но, может быть, продам тебе кого-нибудь невкусного.'
    hakim 'Мой караван готов к сотрудничеству в любой удобный для вас момент!'

    return

label lb_new_love_lizardman:  # Девушка встречает контрабандиста
    $ skip_delay = config.skip_delay
    $ config.skip_delay=75

    call lb_girl_waits from _call_lb_girl_waits_1
    game.girl.love 'Ррагх. Гхар. Гхараггх!!!'
    'Теперь [game.girl.name] точно обречена: к мелким монстрикам прибился их старший братец. Могучий. Грозный. С острыми зубами, светящимися глазами, чешуйчатой кожей, вытянутой мордой... настоящее воплощение ночного кошмара.'
    hide bg
    show expression 'img/bg/love/lizardman_run.jpg' as bg
    game.girl 'Аааа!!!'
    ### nvl clear
    '[game.girl.name] бежит не разбирая дороги, бежит во всю мочь, но вскоре спотыкается и падает... прямо на колья ловушки!'
    'Чьи-то крепкие руки хватают её за плечи, предотвращая непоправимое. За спиной раздаётся глухой голос, спрашивающий "Вы в порядке?". [game.girl.name] оборачивается...'
    game.girl 'Ты умеешь говорить?!'
    game.girl.love 'Да, умею.'
    game.girl.third 'Почему-то ничего более умного ей в этот момент в голову не пришло.'
    game.girl.love 'Понимаю. Немногие из моих сородичей изучают ваш язык.'
    ### nvl clear
    hide bg
    show expression 'img/bg/love/lizardman_couple.jpg' as bg
    '[game.girl.name] и сама не заметила, как разговорилась с ящериком. [game.girl.love.name] оказался, на удивление, умным и понимающим собеседником. Конечно, он не знал многих простых и обыденных вещей, но впитывал знания, как губка.'
    'Они встретились и на следующий день, и на последующий, и на после-после-следующий... Со временем это вошло в привычку, и [game.girl.name] больше не представляла жизни без дружеских посиделок с [game.girl.love.name]ом. Постепенно она перестала обращать внимание на игольчатые зубы своего спутника, на его вытянутую морду, чешуйчатую кожу, острый раздвоенный язык, нечеловеческие глаза. Точнее, не то что бы "перестала обращать внимание..."'
    hide bg
    show expression 'img/bg/love/love.jpg' as bg
    ### nvl clear
    if game.girl.type == 'elf':
      '[game.girl.name] поняла, что её привлекает всё вышеперечисленное. Что её привлекает [game.girl.love.name]. Не просто как хороший собеседник и надёжный друг. А как мужчина. Её. Альву, дитя богини Дану. Привлекает ящерик, порождение драконьего семени. Что с ней творится?!'
    else:
      '[game.girl.name] поняла, что её привлекает всё вышеперечисленное. Что её привлекает [game.girl.love.name]. Не просто как хороший собеседник и надёжный друг. А как мужчина. Её. Человеческую  женщину. Привлекает ящерик, порождение драконьего семени. Что с ней творится?!'
    '[game.girl.name] боролась. Она искала разумные доводы, убеждала себя в противоестественности этой связи, собственной извращённости, уродстве ящерика... Тщетно. И однажды...'
    if game.girl.type == 'elf':
      game.girl 'А мы, дети богини Дану, живём в Зачарованном лесу. Кстати, [game.girl.love.name], я люблю тебя.'
    else:
      game.girl 'А на юге лежит дремучий лес, в котором живут альвы, дети богини Дану. Кстати, [game.girl.love.name], я люблю тебя.'
    game.girl.love 'А я тебя. При самой первой встрече я поклялся, что кровь моя прольётся прежде твоей крови. Что жизнь моя будет отдана за твою жизнь.'
    ### nvl clear
    hide bg
    show expression 'img/bg/love/lizardman_couple.jpg' as bg
    ### nvl clear
    '[game.girl.name] и [game.girl.love.name] сидят в уголке, прижавшись друг к другу. '
    game.girl.love 'Нам надо бежать. Но сейчас это невозможно. Слишком бдительная охрана, слишком сложно добраться до обжитых мест. Боюсь, придётся ждать до следующего года.'
    '[game.girl.love.name] отчётливо содрогается.'
    game.girl.love 'При одной мысли о том, что может сотворить с тобой отец, я схожу с ума!'
    '[game.girl.name] осторожно гладит ящерика по плечу. Чувствуется, что этот жест для неё в новинку. По крайней мере, пока.'
    game.girl 'Не бойся. Ты со мной, и это главное.'
    $ text = u'%s, неожиданно для себя, влюбилась в ящерика по имени %s, и он ответил ей взаимностью. Они задумали бежать на следующий год. \n\n Девушка долго убеждала себя в противоестественности этой связи, но так и не смогла задавить вспыхнувшее чувство. Возможно, именно так боги ответили на её молитвы? ' % (game.girl.name, game.girl.love.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.write_image('img/bg/love/lizardman_couple.jpg',game.dragon.level,game.girl.girl_id)
    ### nvl clear
    if game.girl.virgin:
      if game.girl.nature == 'innocent':
        call lb_nll_innocent_sex from _call_lb_nll_innocent_sex
      elif game.girl.nature == 'proud':
        call lb_nll_proud_sex from _call_lb_nll_proud_sex
      elif game.girl.nature == 'lust':
        call lb_nll_lust_sex from _call_lb_nll_lust_sex
    else:
        call lb_nll_pregnant from _call_lb_nll_pregnant

    $ config.skip_delay=skip_delay

    return

# Новая любовь, принятие решения о сексе.
label lb_nll_innocent_sex:
    '[game.girl.name] судорожно сцепляет руки в замок.'
    game.girl 'Хотя мне всё равно страшно. За год дракон наверняка обесчестит меня, а это страшно, и больно, и...'
    '[game.girl.name] с рыданиями утыкается в чешуйчатую грудь монстра. [game.girl.love.name] осторожно и крайне аккуратно гладит её по голове.'
    game.girl.love 'Отец очень суров. Но если он решит тебя съесть... Кровь моя прольётся прежде твоей крови. Жизнь моя будет отдана за твою жизнь.'
    if  (random.randint(1,10) == 1):
      $ game.girl.virgin = False
      '[game.girl.name] смотрит в пространство отсутствующим взглядом.'
      game.girl 'Это позор. Это невыносимый позор. Но лучше уж так, чем...'
      game.girl 'Пусть моя невинность достанется тебе, а не дракону. Буду считать это... тренировккой. Пожалуйста, возьми меня!'
      $ text = u'%s решила, что ящерик - это хорошая тренировка перед встречей с драконом, и отдала свою невинность любимому. \n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_nll_first_sex from _call_lb_nll_first_sex
    else:
      '[game.girl.name] заторможенно кивает. В её голосе сквозит обречённость.'
      game.girl 'Я переживу это, любимый. Дракон пока не приставал ко мне. Может быть, всё обойдётся?'
      $ text = u'%s испугалась позора и решила остаться невинной. \n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_nll_proud_sex:
    '[game.girl.name] гордо вскидывает голову.'
    game.girl 'Да, мне страшно. За год дракон наверняка изнасилует меня, и это будет невыносимо больно. Но я переживу. Теперь мне есть, ради чего жить.'
    '[game.girl.love.name] осторожно прижимает девушку к себе и аккуратно гладит её по голове.'
    game.girl.love 'Говорят, это пережили уже многие, включая маму. Ты справишься. Ты сильнее её. Только, умоляю, не груби отцу!'
    if  (random.randint(1,6) == 1):
      $ game.girl.virgin = False
      '[game.girl.name] смотрит в пространство, что-то прикидывая для себя, а потом добавляет с нервным смешком.'
      game.girl 'Ну надо же. Никогда на парней внимания не обращала, и о свадьбе особо не мечтала. А теперь...'
      game.girl 'Пусть моя невинность достанется тебе, а не дракону. Буду считать это тренировкой. Трахни меня!'
      $ text = u'%s решила хоть в чём-то уязвить дракона и отдала свою невинность его сыну. \n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_nll_first_sex from _call_lb_nll_first_sex_1
    else:
      '[game.girl.name] смотрит в пространство, что-то прикидывая для себя, а потом добавляет с лёгким сожалением.'
      game.girl 'Поверь, твоя внешность меня только привлекает. Я бы предложила меня трахнуть, но дракон может отнестись к этому весьма нервно. Подождём до следующего года, ладно?'
      $ text = u'%s решила не гневить дракона и осталась невинной. \n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_nll_lust_sex:
    '[game.girl.name] плотоядно облизывает губы.'
    game.girl 'А знаешь, мне ни капельки не страшно. Наоборот, я расстроилась, когда дракоша лёг спать, не посмотрев в мою сторону. Мне хочется ощутить его кол внутри себя. Теперь... ты считаешь меня странной, да?'
    '[game.girl.love.name] аккуратно прижимает девушку к себе и гладит её по голове.'
    game.girl.love 'Немного. Кажется, для человеческих самок это нехарактерно. Скажи, я тебе сильно противен? '
    game.girl 'Противен? Ха! Да ни капельки!'
    if  (random.randint(1,2) == 1):
      $ game.girl.virgin = False
      '[game.girl.name] смотрит в пространство, что-то прикидывая для себя, а потом добавляет томным голосом.'
      game.girl 'Не, чушь. Ты и в подмётки не годишься этой жалкой ящерице.'
      game.girl 'Пусть моя невинность достанется тебе, а не твоему папаше. Выеби меня!'
      $ text = u'%s с превеликим энтузиазмом отдала свою невинность ящерику. \n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_nll_first_sex from _call_lb_nll_first_sex_2
    else:
      '[game.girl.name] смотрит в пространство, что-то прикидывая для себя, а потом добавляет с искренним сожалением.'
      game.girl 'Я бы предложила меня трахнуть, но тогда мне не видать секса с драконом. Подождём до следующего года, ладно?'
      $ text = u'После некоторых размышлений %s всё же решила, что дракон - это круче, чем ящерик, и осталась невинной \n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_nll_pregnant:
    if game.girl.nature == 'innocent':
      '[game.girl.name] судорожно сцепляет руки в замок.'
      game.girl 'Всё равно худшее уже произошло. Дракон обесчестил меня, и это было страшно, и больно, и...'
      '[game.girl.name] с рыданиями утыкается в чешуйчатую грудь ящерика. [game.girl.love.name] аккуратно гладит её по голове.'
      game.girl.love 'Ты это пережила. Самое страшное уже позади. Родишь, и папа о тебе и забудет. А если попытается съесть... Кровь моя прольётся прежде твоей крови. Жизнь моя будет отдана за твою жизнь.'
      if  (random.randint(1,3) == 1):
        '[game.girl.name] смотрит в пространство отсутствующим взглядом.'
        game.girl 'Я опозорена и обесчещена навеки. Моё тело осквернено и поругано. Я хочу хоть как-то выразить свою любовь.'
        game.girl 'Пожалуйста, возьми меня!'
        $ text = u'%s решила вышибить клин клином и занялась сексом с ящериком \n\n' % (game.girl.name)
        call lb_nll_pregnant_sex from _call_lb_nll_pregnant_sex
      else:
        '[game.girl.name] заторможенно кивает. В её голосе сквозит обречённость.'
        game.girl 'Я переживу это, любимый. Скоро кошмар хоть как-то, но закончится. Просто будь рядом, ладно?'
        $ text = u'%s под впечатлением от пережитого не решилась на секс с ящериком. \n\n' % (game.girl.name)
    elif game.girl.nature == 'proud':
      '[game.girl.name] гордо вскидывает голову.'
      game.girl 'Ничего, дракон уже изнасиловал меня. Было больно, но я пережила. Осталось жить дальше. Теперь мне есть, ради чего жить.'
      '[game.girl.love.name] осторожно прижимает девушку к себе и гладит её по голове.'
      game.girl.love 'Самое страшное уже позади. Ты справишься. Ты сильная. Только, умоляю, не груби папе!'
      '[game.girl.name] смотрит в пространство, что-то прикидывая для себя, а потом добавляет с нервным смешком.'
      game.girl 'Ну надо же. Никогда на парней внимания не обращала, и о свадьбе особо не мечтала. А теперь...'
      game.girl 'Пусть дракон подавится, ящерица облезлая. Ты гораздо лучше. Трахни меня!'
      $ text = u'%s решила хоть в чём-то уязвить дракона и занялась сексом с ящериком. \n\n' % (game.girl.name)
      call lb_nll_pregnant_sex from _call_lb_nll_pregnant_sex_1
    elif game.girl.nature == 'lust':
      '[game.girl.name] плотоядно облизывает губы.'
      game.girl 'Ты сочтёшь меня странной, но мне безумно понравился секс с драконом. Я хотела бы повторить, вот только его интересуют только девственницы. Каждую ночь мне снится, как его кол вновь входит в меня. Но после встречи с тобой у меня появились иные мечты.'
      '[game.girl.love.name] аккуратно прижимает девушку к себе и гладит её по голове.'
      game.girl.love 'Я... Я не могу поверить. Ведь обычно у человеческих самок наш внешний вид вызывает отторжение и брезгливость...'
      '[game.girl.name] смотрит в пространство, что-то прикидывая для себя, а потом добавляет томным голосом.'
      game.girl 'Не-а. Ты восхитителен, твой жалкий папаша тебе и в подмётки не годится.'
      game.girl 'Хочу сравнить ощущения. Выеби меня!'
      $ text = u'%s решила сравнить впечатления и занялась сексом с ящериком. \n\n' % (game.girl.name)
      call lb_nll_pregnant_sex from _call_lb_nll_pregnant_sex_2  
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_nll_first_sex:
    ### nvl clear
    $ current_image=get_random_image("img/bg/love/lizardman_sex")
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image
    pause (500.0)
    hide expression current_image
    show expression current_image as bg
    'Любовники медленно, осторожно привыкают друг к другу. Даже поцелуй женщины с рептилией - задача нетривиальная, но после некоторого замешательства влюблённые всё же справились. Дальше пошло легче. Оказалось, что длинный язык [game.girl.love.name]а идеально подходит для ласк. Острый язычок мнёт груди, ласкает животик и спускается всё ниже и ниже. Вот он прикасается к женскому местечку и проникает внутрь. Раздвигает половые губы, теребит клитор, обследует узкую  и влажную пещерку. [game.girl.name] стонет в голос.'
    game.girl.love 'Тебе плохо?'
    game.girl 'Мне хорошо... мне здорово... войди в меня!'
    game.girl.love 'Уверена?'
    ### nvl clear
    '[game.girl.name] видит восставший член ящерика. Он страшен. Огромный, толстый, перевитый венами, он далеко превосходит в размерах хозяйство человека. [game.girl.name] отстраняется от ящерика, а потом резко, со всего маха насаживается на его член.'
    'В первый раз было очень больно. Во второй - просто больно. Но вскоре [game.girl.name] уже не представляла жизни без регулярного секса с ящериком.'
    return

label lb_nll_pregnant_sex:
    ### nvl clear
    $ current_image=get_random_image("img/bg/love/lizardman_sex")
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image
    pause (500.0)
    hide expression current_image
    show expression current_image as bg
    'Любовники медленно, осторожно привыкают друг к другу. Даже поцелуй женщины с рептилией - задача нетривиальная, но после некоторого замешательства влюблённые всё же справились. Дальше пошло легче. Оказалось, что длинный язык [game.girl.love.name]а идеально подходит для ласк. Острый язычок мнёт груди, ласкает выросший животик и спускается всё ниже и ниже. [game.girl.name] замирает, прислушиваясь к странным, никогда не испытанным ощущениям. С драконом всё было иначе: страшно, грубо, больно. А теперь в животе как будто порхает стая бабочек. Вот язычок прикасается к женскому местечку и проникает внутрь. Раздвигает половые губы, теребит клитор, обследует узкую  и влажную пещерку. [game.girl.name] стонет в голос.'
    game.girl.love 'Тебе плохо?'
    game.girl 'Мне хорошо... мне здорово... войди в меня!'
    game.girl.love 'Уверена?'
    ### nvl clear
    '[game.girl.name] видит восставший член ящерика. Он страшен. Огромный, толстый, перевитый венами, он далеко превосходит в размерах хозяйство человека. [game.girl.name] отстраняется от ящерика, а потом резко, со всего маха насаживается на его член.'
    'В первый раз было не больнее, чем с драконом. Во второй - почти терпимо. А вскоре [game.girl.name] уже не представляла жизни без регулярного секса с ящериком.'
    return

label lb_knight_kills_lizardman: # Рыцарь убивает разбойника
    game.knight 'Сударыня, подлая ящерица сбежала. Вы свободны! Для меня будет честью проводить вас до цивилизованных мест.'
    game.girl 'А что стало с ящериками, охранявшими логово?'
    game.knight 'Вам нет нужды переживать, сударыня! Грязные монстры приняли смерть от моего меча.'
    $ current_image="img/bg/love/drowned.jpg"
    show expression current_image
    pause (500.0)
    hide expression current_image
    show expression current_image as bg
    $ text = u'Пленница узнала, что её возлюбленный убит доблестным рыцарем. Во время одного из привалов %s подошла к реке. И утопилась. \n\n' % (game.girl.name)
    $ narrator(text)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('drowned',current_image)
    hide bg
    show expression "img/bg/special/knight_sucsess.jpg" as bg
    return

label lb_love_eat_lizardman:
    game.dragon 'Ну что, моя прелесссть, не пора ли нам подзакуссить?'
    if game.girl.blind:
      game.girl.third '[game.girl.name] замирает, вслушиваясь в подкрадывающуюся смерть.'
    else:
      game.girl.third '[game.girl.name] сжалась в уголке, беззащитная перед голодным ящером.'
    game.girl.love 'Отойди от неё, отец.'
    game.dragon 'Что?!'
    game.girl.third '[game.girl.name] резко бледнеет. Её губы дрожат. Она шепчет дрожащим голосом.'
    game.girl 'Пожалуйста, любимый... не мешай своему отцу. А лучше присоединяйся. Уверена, я вкусная, я тебе понравлюсь... '
    $ text = u'%s решил сожрать девушку, но %s вышел на защиту своей возлюбленной. ' % (game.dragon.name, game.girl.love.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    call lb_love_lizardman_conflict from _call_lb_love_lizardman_conflict_1
    return

label lb_love_execution_lizardman:
    game.dragon.third 'Кажется, [game.girl.name] спуталась с ящериком. Верность мяса дракона не интересует... но игра может быть забавной!'
    game.dragon '[game.girl.love.name]!'
    game.girl.love 'Да, отец?'
    game.dragon 'Убей свою человеческую самочку. Немедленно.'
    if game.girl.cripple:
      $ text = u'%s приказал %sу убить свою возлюбленную, ' % (game.dragon.name, game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      game.girl.third '[game.girl.name] не слышит разговора отца и сына, но понимает, о чём идёт речь. Она с мольбой смотрит на своего возлюбленного.'
      game.girl.love.third '[game.girl.love.name] медлит, словно пытаясь понять, что хочет сказать ему [game.girl.name], а потом принимает решение.'
      if  (random.randint(1,2) == 1):
        game.girl.love 'Как прикажешь, отец.'
        $ text = u'и ящерик выполнил приказ своего отца, оказав калеке последнюю милость. %s обезглавил %s, быстро и безболезненно.\n' % (game.girl.love.name, game.girl.name_r )
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
        ### nvl clear
        game.girl.love 'Кажется, это действительно единственный выход.'
        $ current_image = get_random_image("img/bg/love/execution/beheaded/4.jpg")
        hide bg
        show expression current_image as bg
        game.girl.love 'Прости.'
        '[game.girl.love.name] вытащил клинок и одним движением отрубил [game.girl.name_d] голову'
        $ game.chronik.death('cripple_beheaded',current_image)
        call lb_love_die_lizardman from _call_lb_love_die_lizardman_2
      else:
        game.girl.love 'Нет. Я люблю её и буду защищать до последней капли крови.'
        $ text = u'но ящерик ослушался приказа отца. '  
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
        game.dragon 'Что? Ты понимаешь, что [game.girl.name_r] больше нет, что от неё остался искалеченный обрубок? Что я могу убить тебя одним ударом?'
        game.girl.love 'Понимаю. Но я всё равно люблю её. Даже такой.'
        menu:
            'Забирай':
                game.dragon 'Тогда забирай этот шлак и катись к ангелу!'
                game.girl.love 'Спасибо, отец.'
                game.dragon 'Ну-ну. Интересно, что ты будешь делать с {i}этим{/i}?'
                game.girl.love 'Не беспокойся, что-нибудь придумаю.'
                $ text = u'%s, поражённый такой преданностью, отдал калеку в полное распоряжение ящерика.\n\nПосле пережитого %s решил' %(game.dragon.fullname, game.girl.love.name)
                $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
                call lb_love_lizardman_cripple_choice_live from _call_lb_love_lizardman_cripple_alchemist_1_2
            'Умри':
                game.drgon 'Тогда ты умрёшь.'
                'Разъярённый дракон убил [game.girl.love.name]а одним ударом.'
                $ text = u'Выслушав ответ, %s убил %sа одним ударом.\n\n' %(game.dragon.fullname, game.girl.love.name)
                $ game.girl.love = None
    else:
      game.girl.third '[game.girl.name] резко бледнеет. Её губы дрожат. Она шепчет дрожащим голосом.'
      if game.girl.blind:
        game.girl 'Пожалуйста, любимый... сделай так, как сказал [game.dragon.name]. Всё равно он ослепил меня, мне нет смысле жить дальше...'
      else:
        game.girl 'Пожалуйста, любимый... сделай так, как сказал [game.dragon.name]. Может быть, хоть ты останешься в живых...'
      $ text = u'%s приказал %sу убить свою возлюбленную, но ящерик ослушался приказания отца. ' % (game.dragon.name, game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_love_lizardman_conflict from _call_lb_love_lizardman_conflict
    return

label lb_love_execution_both_lizardman:
    game.dragon.third 'Кажется, [game.girl.name] спуталась с ящериком. Верность мяса дракона не интересует... но игра может быть забавной!'
    game.dragon '[game.girl.love.name]!'
    game.girl.love 'Да, отец?'
    game.dragon 'Ведомо ли тебе, что измена карается смертью?'
    if game.girl.cripple:
      game.dragon 'Приготовься умереть вместе со своей искалеченной подстилкой, мой жалкий сынишка!'
      game.girl.love 'Глупый, глупый, глупый папаша.'
      game.girl.love 'Ты думаешь, ей нужна такая жизнь? Ты думаешь, {i}мне{/i} нужна такая жизнь?'
      '[game.girl.love.name] одним движением обезглавливает [game.girl.name_v], а потом вонзает клинок себе в сердце.'
      '[game.dragon.fullname] растерянно чешет хвостом в затылке.'
      game.dragon 'Не совсем то, на что я рассчитывал...'
      $ text = u'%s решил казнить обоих любовников. Услышав приговор, %s обезглавил свою возлюбленную и убил себя.' % (game.dragon.name, game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ game.chronik.death('cripple_beheaded',current_image)
    else:
      game.dragon 'Приготовься умереть вместе со своей подстилкой, мой жалкий сынишка!'
      $ text = u'%s решил казнить обоих любовников, но %s не согласился со своей участью. ' % (game.dragon.name, game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_love_lizardman_conflict from _call_lb_love_lizardman_conflict_2
    return
 
label lb_love_lizardman_conflict:  # Конфликт отцов и детей. 
    game.girl.love 'Нет. Кровь моя прольётся прежде твоей крови.'
    if game.girl.blind:
      '[game.girl.love.name] обнажает свой топорик. Услышав характерные звуки, [game.girl.name] достаёт из волос костяную заколку.'
    else:
      '[game.girl.love.name] обнажает свой топорик. Увидев это, [game.girl.name] достаёт из волос костяную заколку.'
    game.dragon 'Что?!!'
    game.girl.love 'Если я должен разъять тебя на части, папочка, я сделаю это! Лучше отпусти нас по-хорошему.'
    ### nvl clear
    menu:
        'Отпустить':
            $ text = u'Дракон не захотел марать когти и отпустил влюблённых.  \n\n'
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            game.dragon 'Больно надо когти марать. Идите к ангелу!'
            game.girl.love 'Прощай, отец'
#            call lb_love_escape_lizardman from _call_lb_love_escape_lizardman
            $ game.girls_list.love_escape_ind()
        'Уничтожить':
            $ text = u'Дракон пришёл в ярость и решил убить блудного сына и их общую жену. \n\n' 
            $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
            game.dragon 'Я тебя породил, я тебя и убью!'
            game.girl 'В борьбе обретём мы право своё!'
            game.girl.love 'Победа или смерть!!!'
            if game.girl.blind:
              $ game.foe = Enemy('lizardman_blind', game_ref=game)
            else:
              $ game.foe = Enemy('lizardman', game_ref=game)
            $ narrator(show_chances(game.foe))
            menu:
                'Сражаться':
                    call lb_fight from _call_lb_fight_71
                    $ current_image = "img/bg/love/death.jpg"
                    game.dragon.third 'Ну что за день такой неудачный? Одни трупы и никакого удовольствия!'
                    $ text = u'%s погибла в схватке с драконом. \n\n' % (game.girl.name)
                    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
                    $ game.chronik.death('defeat',current_image)
                'Бежать, поджав хвост!':
                    game.dragon 'Хм, самое время предпринять манёвр стратегического отступле... э, бегства!'
                    call lb_love_lizardman_victory from _call_lb_love_lizardman_victory_2
                    $ game.girls_list.lizardman_free_all_girls()
                    $ game.create_lair()
    return

label lb_love_lizardman_victory:
    $ place = game.lair.type_name
    hide bg
    show place as bg
    'После того, как дракон удрал, поджав хвост, парочка, сбрасывая нервное напряжение, бросилась в объятия друг друга.'
    $ current_image = get_random_image("img/bg/love/lizardman_sex")
    hide bg
    show expression current_image
    pause 500
    hide expression current_image
    show expression current_image as bg
    'Они занимались любовью больше часа. [game.girl.name] требовала ещё и ещё, словно топя в животном сексе воспоминания о встречах с драконом. К счастью, [game.girl.love.name], будучи отродьем владычицы, обладал потрясающей неутомимостью. Перепробовав множество поз и заляпавшись липкой спермой с головы до ног, женщина слегка успокоилась и смогла осмыслить произошедшее.'
    game.girl 'Победа...'
    game.girl.love 'Да. Победа. Сам не ожидал...'
    'Помолчали.'
    game.girl.love 'И что теперь?' 
    if game.girl.blind:
      game.girl 'А теперь... *женщина замолкает и склоняет голову набок* А теперь мы будем жить здесь. В нашем новом доме. Возражения?'
    else:
      game.girl 'А теперь... *женщина оглядывает логово дракона* А теперь мы будем жить здесь. В нашем новом доме. Возражения?'
    game.girl.love 'Никаких!.. Но я думал, что ты захочешь вернуться... к своим?'
    if game.girl.blind:
      '[game.girl.name] задумчиво ощупывает лицо [game.girl.love.name]а.'
    else:
      '[game.girl.name] задумчиво осматривает [game.girl.love.name]а.'
    game.girl 'Не-а. Теперь ты для меня "свой". Кстати, я хочу от тебя сына. А лучше двух. '
    game.girl 'И дочку. И точка!'
    $ text = u'К своему несказанному удивлению, %s и %s смогли одолеть дракона. Подлый насильник сбежал, поджав хвост, а любовники обустроились в его бывшем логове и стали жить-поживать да добра наживать. А детишки у них родились - заглядение! \n\n' % (game.girl.name, game.girl.love.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.live('victory',current_image)
    $ place = game.lair.type_name
    hide bg
    show place as bg
    return

label lb_love_lizardman_cripple:
    if game.girl.pregnant>0:
      hide bg
      ### nvl clear
      $ current_image = game.girl.cripple_image
      show expression current_image as bg
      game.girl.love.third '[game.girl.love.name] стоит перед искалеченной [game.girl.name_t]. Его мордочка обычно безымоциональна, но теперь на ней отчётливо проявляются гнев и горе. [game.girl.name] пристально смотрит на возлюбленного, и в её взгляде читается... кто знает, что в нём читается? Она ничего не может ни сказать, ни услышать.'
      game.girl.love 'Проклятье, проклятье, отец всё-таки сделал это! [game.girl.name], чем я... что я...'
      ### nvl clear
      'Ящерик замолкает, не в силах закончить фразу. Он неотрывно следит за зрачками [game.girl.name_r], пытаясь прочитать ответ на невысказанный вопрос.'
      $ text = u'%s хорошо подготивлся к побегу, чего нельзя сказать о %s: после встречи с драконом она стала калекой. После долгих и мучительных размышлений ящерик решил ' % (game.girl.love.name, game.girl.name_p )
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ choices = [
        ("lb_love_lizardman_cripple_kill", 10),
        ("lb_love_lizardman_cripple_alchemist", 10)]
      $ enc = weighted_random(choices)
      $ renpy.call(enc)
    else:
      assert "Roman of lizardman and cripple"
    return

label lb_love_lizardman_cripple_kill:
    $ text = u'оказать своей возлюбленной последнюю милость. %s обезглавил %s, быстро и безболезненно.\n' % (game.girl.love.name, game.girl.name_r )
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    ### nvl clear
    'Молчание висело долго, очень долго'
    game.girl.love 'Кажется, это действительно единственный выход.'
    $ current_image = get_random_image("img/bg/love/execution/beheaded/4.jpg")
    hide bg
    show expression current_image as bg
    game.girl.love 'Прости.'
    '[game.girl.love.name] вытащил клинок и одним движением отрубил [game.girl.name_d] голову'
    $ game.chronik.death('cripple_beheaded',current_image)
    call lb_love_die_lizardman from _call_lb_love_die_lizardman_1
    return

label lb_love_lizardman_cripple_alchemist:
    game.girl.love 'Нет.'
    game.girl.love 'Я не могу дать тебе умереть. Я попытаюсь спасти тебя, несмотря ни на что.'
    call lb_love_lizardman_cripple_choice_live from _call_love_lizardman_cripple_alchemist_1_1
    return

label lb_love_lizardman_cripple_choice_live: # Определяется дальнейшая судьба
    if game.summon.seal==0 or game.summon.seal>=data.max_summon: 
      call lb_love_lizardman_cripple_alchemist_1 from _call_lb_love_lizardman_cripple_alchemist_1
    else:
      $ chance = random.choice(['alchemist_1', 'demon'])
      $ enc = 'lb_love_lizardman_cripple_' + chance
      call enc from _call_enc #from _call_lb_love_lizardman_cripple
    return

label lb_love_lizardman_cripple_demon: # Логово демонопоклонников
    $ current_image = 'img/scene/summon.jpg'
    $ text = u"%s, желая спасти свою возлюбленную, обратился за помощью к культистам Архитота. Что же, это ему удалось! С помощью тёмных и запретных ритуалов демонопоклонники создали %s фантомные руки и ноги и вернули ей слух. Плата за столь щедрый дар была ничтожной - вступление в культ.\n\n" %(game.girl.love.name, game.girl.name)
    '[text]'
    $ text = u"Уже совсем скоро %s безмолвно и безэмоцианально резала на алтарях невинных жертв. В качестве очередного испытания она принесла в жертву %sа, своего бывшего возлюбленного." %(game.girl.name,game.girl.love.name)
    '[text]'
    $ game.summon.seal += 1 
    $ text = u'спасти свою возлюбленную, несмотря ни на что. Ящерик отнёс %s культистам Архитота, и они с помощью тёмных и запретных ритуалов демонопоклонники создали %s фантомные руки и ноги и вернули ей слух. Она присоединилась к культу в качестве платы за исцеление.\n\n Уже совсем скоро %s безмолвно и безэмоцианально резала на алтарях невинных жертв. В качестве очередного испытания она принесла в жертву %sа, своего бывшего возлюбленного.' % ( game.girl.name, game.girl.name_d,game.girl.name,game.girl.love.name )
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.live('cripple_demon',current_image)
    return

label lb_love_lizardman_cripple_alchemist_1:
    python: #делаем аватарку алхимика для диалогового окна
      alchemist= Talker(game_ref=game)
      alchemist.avatar = "img/avahuman/alchemist.jpg"
      alchemist.name = 'Безумный алхимик'  
    ### nvl clear
    $ current_image="img/bg/love/alchemist.jpg"          
    hide bg
    show expression current_image as bg
    alchemist 'Что вас интересует, молодой ящерик? Вы решили отдать этот экземпляр человеческой самки для опытов? Не беспокойтесь, в связи с её увечьем цена только возрастёт!'
    game.girl.love 'Не совсем. Я хочу продать только её отродье от отца. Взамен вы обеспечите [game.girl.name_d] сносные условия существования.'
    alchemist 'Не совсем по моему профилю... так, техномагические протезы, требующие глубокой интеграции в нервную систему подопытной... да, задача представляется интересной!'
    alchemist 'Но только с одним условием - я уже стар. Если у вас хватит таланта, вы станете моим ассистентом и преемником.'
    game.girl.love 'Я согласен.'
    'Через некоторое время [game.girl.name] получила протезы рук и ног. Она смогла ходить и даже писать, пусть и неуклюже. Чтобы слышать речь, ей приходилось надевать на голову специальный ааппарат. Речь к [game.girl.name_d] так и не вернулась.'
    'В общем, такой судьбе могли бы позавидовать многие другие калеки.'
    $ text = u'спасти свою возлюбленную, несмотря ни на что. Ящерик отнёс %s алхимику, и старый мастер изготовил сложные техномагические протезы. Со временем %s вновь научилась кое-как ухаживать за собой и различать звуки. Речь к ней так и не вернулась.\n\nПожалуй, другие калеки могли бы позавидовать её судьбе.' % ( game.girl.name_r, game.girl.name )
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.live('cripple_alchemist',current_image)
    return       

label lb_love_escape_lizardman:
    $ skip_delay = config.skip_delay
    $ config.skip_delay=75
    $ current_image = get_random_image("img/bg/love/lizardman_sex")
    hide bg
    show expression current_image
    pause 500
    hide expression current_image
    show expression current_image as bg
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    if game.girl.blind:
      game.girl.love 'Глядя на твоё лицо, я постоянно терзаюсь виной'
      game.girl 'Выбрось из головы. Для {i}этого{/i} глаза мне совершенно не нужны!'
    else:
      game.girl.love 'Ну хватит. Нам пора бежать.'
      game.girl 'Ещё разочек, любимый.'
    'Некоторое время раздаются только охи и стоны, изредка переходящие в крики наслаждения.'
    game.girl.love 'Теперь точно пора. Я хорошо подготовился: собрал припасы, разведал дорогу. Погони можно не бояться.'
    '[game.girl.name] ласково кусает [game.girl.love.name]а за язык.'
    game.girl 'Ты куда бежать-то собрался, дурачок?'
    game.girl.love 'Как - куда? Домой тебя отведу.'
    game.girl 'А о том, что тебя там убьют, ты не подумал?'
    game.girl.love 'Подумал. Надо будет разыграть сценку "спасение девы от монстра". Меня убьют, ты заживёшь нормальной жизнью...'
    '[game.girl.name] показывает любовнику язык.'
    game.girl 'Моя нормальная жизнь - это ты. Если тебя убьют, я покончу с собой, так и знай.'
    game.girl.love 'Но как же тогда? В глуши нам не выжить.'
    game.girl 'Вот я и говорю - дурачок. Я-то давно выход нашла.'
    $ game.girls_list.save_girl()
    $ config.skip_delay=skip_delay
    return

label lb_love_lizardman_mistress:
    $ skip_delay = config.skip_delay
    $ config.skip_delay=75
    ### nvl clear
    hide bg
    show expression 'img/scene/mistress.jpg' as bg
    mistress 'Кто беспокоит меня?'
    '[game.girl.name] и [game.girl.love.name] опускаются на колени.'
    game.girl.love 'Прими нашу службу, Тёмная Госпожа.'
    game.girl 'Мы вручаем нашу верность и наши жизни владычице этого мира.'
    mistress 'Тебе, внучок, места в армии тьмы найдётся. Но зачем мне нужна твоя человеческая подстилка?'
    '[game.girl.name] отвечает спокойно и твёрдо. Похоже, она ожидала такого вопроса и давно для себя всё решила.'
    game.girl 'Я могу рожать вашим воинам детей, Тёмная Госпожа.'
    mistress 'Хорошо. Тогда я назначу вам испытание. Ты, внучок, пойдёшь и сразишься с драконорожденным. Ты, девка, отправишься вон в тот лагерь и обслужишь гоблинов. Их там, кажется, сотня... или две.'
    mistress 'Если выживете - то добро пожаловать в Армию Тьмы.'
    '[game.girl.name] и [game.girl.love.name] поднимаются с колен, глубоко кланяются и отвечают хором "Как прикажите, Тёмная Госпожа".'
    $ text = u'Оказавшись на свободе, любовники поняли, что не знают, куда идти. %s предложил проводить пленницу домой, но там ящерика точно убили бы. %s не захотела жертвовать любимым и придумала иной выход. \n\n Парочка пришла на аудиенцию к Тёмной Госпоже и вручила ей свои жизни и свою верность. Владычица приняла этот дар и назначила испытание своим новым подданным. ' % (game.girl.love.name, game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression "img/scene/spawn/dragonborn.jpg" as bg
    if random.randint(1,5)==-1: # Проигрыш ящерика # @fdsc Ящерики никогда не проигрывают: девочек жалко
      $ text = u'%s сражался храбро и отчаянно, но доблесть и самоотверженность - плохая замена голой мощи. Драконорождённый убил ящерика и надругался над его возлюбленной. %s скончалась, не выдержав горя и издевательств. ' %(game.girl.love.name, game.girl.name)
      '[text]'
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ game.chronik.death('rape_army',"img/scene/spawn/dragonborn.jpg")
    else:
      # @fdsc Замена проигрыша ящерика на работу дракона
      if random.randint(1,5)==1:
        $ game.dragon.drain_energy(7, True)
        '{color=#FFFF00}Ящерик споткнулся от усталости, но [game.dragon.name] хорошо помнит своих слуг. Он мысленно дал ему ещё энергии, чтобы ящерик смог победить.{/color}'

      '[game.girl.love.name] сражался храбро и отчаянно, и ему удалось удивить даже драконорожденного. Не сразу, далеко не сразу исполинский монстр уступил напору человека-ящерицы, но в конце концов даже ему пришлось признать своё поражение.'
      $ text = u'%s выполнил испытание Тёмной Госпожи, победив драконорожденного. \n ' %(game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      'Назад [game.girl.love.name] возвращался, обуреваемый дурными предчувствиями. Испытание, назанченное бабушкой, очень серьёзно. Выдержит ли его возлюбленная?'
      if game.girl.nature == 'lust':
        $weight=1.5
      elif game.girl.nature == 'proud':
        $weight=1.0
      elif game.girl.nature == 'innocent':
        $weight=0.5
      if game.girl.blind:
        $weight=weight*3.0
      $ choices = [
        # @fdsc Девушки никогда не умирают у королевы
        # ("lb_love_lizardman_death", 20 ),
        ("lb_love_lizardman_live", 10*weight*girls_data.girls_info[game.girl.type]['endurance'])]
      # Умереть гор-раздо проще!
      $ enc = weighted_random(choices)
      $ renpy.call(enc)

    $ config.skip_delay=skip_delay
    $ game.pauseForSkip()
      
    return

label lb_love_die_lizardman:
    $ text = u'%s похоронил возлюбленную и покончил с собой на её могиле. \n\n' % (game.girl.love.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    game.girl.love.third "[text]"
    return

label lb_love_suicide_lizardman:
    $ text = u'Узнав о смерти своей возлюбленной, %s покончил с собой.\n\n' % (game.girl.love.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    game.girl.love.third "[text]"
    return

label lb_love_caravan_lizardman:  # Ящерик спасает возлюбленную из каравана.
    ### nvl clear
    $ current_image="img/bg/love/slave_caravan.jpg"          
    hide bg
    show expression current_image as bg
    '"Раскалённым солнцем сжигает кожу, ветер сушит слёзы и ранит веки..."'
    show expression current_image
    pause 500
    hide expression current_image
    game.girl.third '[game.girl.name] медленно бредёт по обжигающему песку в цепочке таких же несчастных рабынь. Зачем? Куда? Как жить после того, как её разлучили с любимым? Да, [game.girl.love.name] - монстр, но он для неё дороже всего на свете! А теперь [game.girl.name] его больше никогда не увидит. Для чего она вообще существует?'
    game.girl.third 'Мало сил и мало воды, но зато много солнца, песка и ярости надмотрщиков. Каждый день кто-то из девочек остаётся лежать в песках. Возможно, её ждёт та же участь.'
    ### nvl clear
    $ current_image="img/bg/love/night_desert.jpg"          
    hide bg
    show expression current_image as bg
    game.girl.third 'В одну из ночей [game.girl.name] услышала странные шорохи, и её окликнул до дрожи родной голос'
    game.girl.love 'Вставай. Идём.'
    game.girl 'Ты?'
    game.girl.love 'Да. Часового я снял, но остальные могут проснуться в любой момент. Надо торопиться.'
    $ text = u'%s спас возлюбленную из каравана работорговцев. \n\n' % (game.girl.love.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
#    call lb_love_escape_lizardman from _call_lb_love_escape_lizardman_1
    $ game.girls_list.love_escape_ind()
    return

label lb_love_lizardman_death: # Затрахали до смерти
    ### nvl clear
    hide bg
    if game.girl.type == 'elf': # Тролли
      $ current_image=get_random_image("img/bg/love/troll_sex")
      show expression current_image as bg
      'Тролль!'
      'Огромный тролль насиловал его возлюбленную. Живот девушки был страшно, противоестественно раздут.'
      'Нет, не так: тролль насиловал труп его возлюбленной. Девушка была очевидно и безнадёжно мертва.'
      ### nvl clear
      game.girl.love.third '[game.girl.love.name] в ярости кинулся на тролля. Атака была настолько яростной и неожиданной, то ящерику удалось убить тролля, но и сам он скончался от полученных ран. По крайней мере, [game.girl.name] была отомщена!'
      $ text = u'А вот альва не выдержала. Привлечённой ароматом священной плоти, к оргии присоединился тролль. %s не выдержала надругательств и скончалась от полученных травм. %s ценой своей жизни отомстил за её смерть. \n ' %(game.girl.name,game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ game.chronik.death('rape_troll',current_image)
    else: # Просто скончалась   
      show expression "img/bg/love/death_sex.jpg" as bg 
      game.girl.love 'Нееет!!!'  
      '[game.girl.name], испачканная спермой и кровью, валялась на земле. Из её разверстанного влагалища неспешно, но неотвратимо струилась кровь. В лицах собравшихся вокруг гоблинов чувствовалась некоторая... растерянность.'
      game.girl.love '[game.girl.name]!'
      game.girl 'Ты... пришёл...'
      game.girl 'Прости... не выдержала...'
      ### nvl clear
      '[game.girl.name] шепчет - тем шёпотом, что громче и страшнее крика.'
      game.girl 'Пожалуйста... возьми меня...'
      game.girl.love 'Нет!!! Ещё можно что-то поправить... как-то вылечить...'
      ### nvl clear
      '[game.girl.love.name] сам понимает, насколько фальшиво звучат его слова. Никто в армии тьмы и не почешется ради спасения человеческой самки'
      game.girl 'Пожалуйста... Будь... моим... последним мужчиной.'
      ### nvl clear
      '[game.girl.love.name] выполнил последнюю просьбу умирающей, а после её смерти - покончил с собой.'
      $ text = u'А вот его возлюбленная не выдержала оргии с гоблинами и скончалась. %s покончил жизнь самоубийством \n ' %(game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ game.chronik.death('rape_goblin',"img/bg/love/death_sex.jpg")
    return

label lb_love_lizardman_live:
    ### ### nvl clear
    hide bg 
    if game.girl.type == 'elf': # Тролли
      $ current_image=get_random_image("img/bg/love/elf_sex")
    else:
      $ current_image=get_random_image("img/bg/love/goblin_sex")  
    show expression current_image as bg 
    'Возлюбленная [game.girl.love.name]а постанывала, удовлетворяя сразу несколько отродий Тёмной Госпожи, но {color=#00ff00}в целом казалась здоровой и невредимой{/color}'
    game.girl.love 'Ты как?'
    'Идиотский вопрос, но ничего умнее ящерику в голову не пришло.'
    game.girl 'Хорошо... Было трудно, но я справилась. И дальше справлюсь.'
    game.girl 'И вообще, что ты стоишь? Не стесняйся, присоединяйся!'
    game.girl.love 'Но...' 
    game.girl 'Пожалуйста...'
    $ text = u'%s тоже с честью выдержала предложенное испытание, превратившись в аппарат по производству отродий. Практически ежедневно она становилась главной героиней массовых оргий с монстрами. Но это не тяготило законченную нимфоманку-ксенофилку, ведь иногда в тех же оргиях участвовал её любимый... \n\n' %(game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.live('dark_whore',current_image)
    $ game.army.add_warrior('lizardman', 1)
    return

label lb_love_lizardman_uncle: # Возвращается к родственникам - счастливый исход
    ### nvl clear
    call lb_show_home from _call_lb_show_home_4
    $ text = u'%s привела %sа к дяде и честно рассказала ему о проихошедшем. Дядя был, мягко говоря, поражён, но он быстро убедился, ' %(game.girl.name, game.girl.love.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    game.girl.love 'Я... боюсь.'
    game.girl 'Не бойся! Мой дядя - самых честных правил, вот увидишь!'
    python: #делаем аватарку дяди для диалогового окна
      uncle= Talker(game_ref=game)
      uncle.avatar = "img/avahuman/uncle/" + game.girl.type + ".jpg"
      uncle.name = 'Дядя самых честных правил' 
    game.girl 'Дядя, добрый день! Я вернулась.'  
    uncle 'Эээ...'
    if game.girl.blind:
      uncle 'Что с твоими глазами?!'
      game.girl 'Да ослепили немного, не обращай внимания.'
    game.girl 'Кстати, познакомься с моим мужем.'
    uncle 'Эээ...'
    game.girl 'Мы любим друг друга, и я жду от него ребёнка!'
    uncle 'Эээ...'
    game.girl.love 'Меня зовут [game.girl.love.name]. Приятно познакомиться.'
    uncle 'Я убью этого монстра!'
    game.girl.third '[game.girl.name] подносит кинжал к своей груди.'
    game.girl '[game.girl.love.name] - никакой не монстр, а очень способный и образованный молодой ящерик! А если ты убьёшь его, дядя, то я покончу с собой.'
    uncle 'Способный?!! Такие твари, как он, способны только убивать и насиловать!'  
    if game.girl.type == 'peasant':
      game.girl.love 'Ну почему же. Я физически сильный и выносливый, могу пахать, сеять, жать, молотить. Работаю как минимум за двоих.'
      uncle 'Ага, а ешь за десятерых!'
      game.girl.love 'Отнюдь, весь мой род весьма умерен в еде. Иначе как бы мы выжили на бесплодных восточных равнинах?'
      uncle 'Молодец, [game.girl.name], хорошего себе работника выбрала! Думаю, к осени вас и обвенчаем.'
      $ text = u'насколько ценным работником может быть %s в крестьянском хозяйстве. Он благословил молодожёнов, и стали они жить-поживать, да добра наживать.\n\nА уж детишки у них пошли - заглядение!' %( game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ game.chronik.live('uncle_peasant',None)
    elif game.girl.type == 'citizen':
      game.girl.love 'Ну почему же. Я довольно быстро считаю в уме и могу вести бухгателрские расчёты.'
      uncle 'Ты-то? Ахаха!!! Корень квадратный из двух!'
      game.girl.love 'Один точка четыреста четырнадцать.'
      uncle 'Э? Корни квадратного уравнения?'
      game.girl.love 'Минус бэ плюс-минус корень квадратный из дискриминанта, делённое на два а, где дискриминант - бэ квадрат минус четыре а цэ.'
      uncle 'Десятичный логарифм шестьсот шестидесяти шести!'
      game.girl.love 'Ммм... два точка восемьсот двадцать три.'
      uncle 'Так, где там мои таблицы Брагса...'
      uncle '[game.girl.name]! Племяшечка! Я так рад, что выбрала себе такого замечательного мужа, который, без сомнения, станет лучшим счетоводом на моей мануфактуре!'
      $ text = u'насколько ценным счетоводом может быть %s в купеческом деле. Он благословил молодожёнов, и стали они жить-поживать, да добра наживать.\n\nА уж детишки у них пошли - заглядение!' %( game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ game.chronik.live('uncle_citizen',None)
    elif game.girl.type == 'princess':
      game.girl.love 'Ну почему же. Я слышал, что вы с трудом отбиваетесь от порождений моей бабушки. Я хорошо знаю их поведение и их уязвимые места. С моей помощью вы сможете организовать эффективное сопротивление!'
      uncle 'Что? Рискнуть и довериться тебе? Монстру?'
      game.girl.love 'Из того, что мы увидели по пути сюда - положение практически отчаянное.'
      uncle 'Это недалеко от истины. Но как это воспримут при королевском дворе?'
      game.girl.love 'Смею надеяться, положительно. Монстр, влюбившийся в человеческую девушку и перешедший на сторону людей... Отважные рыцари найдут в этом доблесть, прекрасные дамы - романтику. А произвести при дворе фурор я, буду надеяться, сумею.'
      uncle 'Хорошо. Ты принят в мою дружину. И если ты оправдаешь свои обещания, то я поздравлю [game.girl.name_v] с выбором замечательного мужа!'
      $ text = u'насколько ценным командиром может быть %s в рыцарской дружине. Он благословил молодожёнов, и стали они жить-поживать, да добра наживать.\n\nА уж детишки у них пошли - заглядение!' %( game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ game.chronik.live('uncle_princess',None)
    elif game.girl.type == 'elf':
      game.girl.love 'Ну почему же. Я слышал, что вы с трудом отбиваетесь от порождений моей бабушки. Я хорошо знаю их поведение и их уязвимые места. С моей помощью вы сможете организовать эффективное сопротивление!'
      uncle 'Что? Рискнуть и довериться тебе? Монстру?'
      game.girl.love 'Из того, что мы увидели по пути сюда - положение недалеко от отчаянного. Чары Детей Дану истощаются, они уже с трудом удерживают и моих братьев, и, что ещё хуже, порождений Тёмного леса. Я могу быть рейнджером в этих опасных местах'
      uncle 'Ты серьёзно?'
      game.girl.love 'У вас так мало желающих?'
      uncle '[game.girl.name], природное равновесие подчас может приобретать весьма странные и причудливые формы. Я рад, что ты смогла разглядеть внутреннюю суть за обёртками внешней формы!'
      $ text = u'насколько ценным рейнджером может быть %s при охране границ от порождений Тёмного леса. Он благословил молодожёнов, и стали они жить-поживать, да добра наживать.\n\nА уж детишки у них пошли - заглядение!' %( game.girl.love.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ game.chronik.live('uncle_elf',None)
    return

