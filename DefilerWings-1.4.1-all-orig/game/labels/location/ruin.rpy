# coding=utf-8
init python:
    from pythoncode.characters import Talker
    
label lb_location_ruin_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))    
    hide bg
    show expression 'img/bg/special/haunted.jpg' as bg

    python:
        witch = Talker(game_ref=game)
        witch.avatar = "img/avahuman/witch.jpg"
        witch.name = "Ведьма"
    
    if game.dragon.energy() == 0:
        'Даже драконам надо иногда спать. Особенно драконам!'
        return
        
    menu:
        'Посетить ведьму':
            show expression 'img/scene/witch.jpg' as bg
            if game.witch_st1==1:
              witch 'Тебе не терпится получить первое задание? Или ты пришёл сюда по более мелкому, но приятному делу?'
              menu:
                  'Давай сюда своё задание!':
                      call lb_witch_first_task from _call_lb_witch_first_task
                  'Не-а, задания пока подождут':
                      call lb_witch_eval from _call_lb_witch_eval_1
            elif game.witch_st2==1:
              witch 'Тебе понравилось первое задание, и ты хочешь приступить ко второму? Или ты пришёл сюда по более мелкому, но приятному делу?'
              menu:
                  'Очень понравилось!':
                      witch 'К сожалению, мне пока что нечего тебе поручить. Подойди в следующей версии игры'
                      game.dragon 'Жаль, жаль...'
                      $ game.spell_list_rus = deepcopy(data.spell_book)
                      $ game.spell_list = deepcopy(data.spell_unknown)
                      $ game.witch_st2=0
                  'Не-а, задания пока подождут':
                      call lb_witch_eval from _call_lb_witch_eval_5
            elif game.witch_st1==3:
              witch 'Да? Разве ты не должен был соблазнять королеву?'
              menu:
                  'Эээ... а ещё одно зелье можно?':
                      witch 'Что? Ты бездарно потратил ценнейший реагент?!'
                      $ game.witch_st1=2
                      witch 'Держи уж, горе хвостатое'
                  'Не, я по другому вопросу':
                      call lb_witch_eval from _call_lb_witch_eval_3
            elif game.witch_st1==4:
              witch 'Вижу, ты уже разделил ложе с Королевой. Это хорошо. На следующеий год тебе нужно будет проведать ребёночка и направить его на путь истинный.'
              call lb_witch_eval from _call_lb_witch_eval_4
            elif game.witch_st1==5:
              witch 'Великолепно. Великолепно! Мои планы, внезапно оказавшиеся на грани провала, всё ещё могут осуществиться.'
              witch 'Прими же заслуженную награду. Прежде всего - горсть презренного злата. Думаю, оно тебе не помешает.'
              $ gain = random.randint(5,10)
              $ game.lair.treasury.dublon += gain
              witch 'Также я научу тебя парочке заклинаний.'
              witch 'Первое - {i}"Магические ловушки в логово"{/i}. Оно поможет тебе в борьбе с ворами. Но помни, одних магических ловушек недостаточно, необходим целый комплекс мер! Помни - эти настырные заразы везде пролезут'
              witch 'Думаю, я буду даже помогать некоторым из них - чтобы драконий род не терял бдительности.'
              $ game.spell_list_rus['spellbound_trap'] = u"Волшебные ловушки в логово"
              $ game.spell_list['spellbound_trap'] = ['spellbound_trap']
              witch 'Второе позволяет отрастить фантомную голову. Когда битва почти проиграна, и ты находишься при смерти, фантомная голова отвлечёт врага. Он снесёт её, дав тебе ещё один шанс на победу или бегство.'
              $ game.spell_list_rus['unbreakable_scale'] = u"Отрастить фантомную голову"
              $ game.spell_list['unbreakable_scale'] = ['virtual_head']
              witch 'Ну и напоследок - чуток магической силы, чтобы ты мог распробовать эти заклинания'
              $ game.dragon.spells.append('witch_spell')
              witch 'А теперь иди. Следующее задание я дам через пять лет, тебе или твоему потомку.'
              $ game.witch_st1=0
              $ game.history = historical( name='witch_st1',end_year=game.year+5,desc='Говорят, ведьме из старых руин вновь требуется помощь дракона  ',image='img/bg/special/haunted.jpg')
              $ game.history_mod.append(game.history)
              call lb_witch_1_aftermath from _call_lb_witch_1_aftermath
            else:
              call lb_witch_eval from _call_lb_witch_eval_2
            
        'Уйти прочь':
            return
        
    return

label lb_witch_first_task:
    if game.quest_time <= 1 and not freeplay:
      witch 'Нет. Ты явно не успеешь с ним справиться. Пусть ко мне приходит твой потомок.'
      return
    $ game.witch_st1=2
    witch 'Король Сылтан, да преумножится его мужская сила, женился по любви! Не помогли ни протесты его придворных, ни вооружённые выступления военачальников, ни все слои моих интриг. Почти тысячелетня работа над королевской генетической линией поставлена под угрозу. '
    game.dragon 'А, и ты хочешь, чтобы я убил королеву.'
    witch 'Нет. Согласно моим прогнозам, тогда Сылтан примет обет безбрачия и будет блюсти целибат до конца своих дней.'
    game.dragon 'А, ты хочешь, чтобы я обесчестил Королеву!'
    witch 'Поздно. Королева уже беременна, хотя об этом пока неизвестно даже ей самой.'
    game.dragon 'Тогда что же ты хочешь?'
    witch 'Сейчас король осматривает восточные рубежи Королевства. Держи это зелье. Оно на время превратит тебя в Сылтана. Мне нужно, чтобы ты вошёл во дворец и возляг с Королевой.'
    game.dragon 'Но зачем? Тем более, в человеческом облике я бесплоден...'
    witch 'Зелье повлияет на твою сперму таким образом, что она вызовет необратимые мутации у плода.'
    witch 'И поспеши! Иди в Столицу, выпей зелье и отправляйся прямо в королевский дворец. Это задание нужно будет выполнить в текущем году, иначе станет поздно.'
    return

label lb_witch_eval:
    if game.dragon.lust == 3: 
      call lb_witch_agree from _call_lb_witch_agree
    else:
      call lb_witch_refuse from _call_lb_witch_refuse
    return
    
label lb_witch_agree:
    nvl clear
    witch 'Услуга за услугу. Я помогу тебе, если ты поделишься со мной своей уникальной спермой. Она нужна мне для алхимических нужд. Не бойся, процесс приятный, тебе понравится. Только учти - я высосу из тебя всё до капли!'
    menu:
        'Дать себя подоить':
            $ game.witch_force+=1
            $ game.dragon.drain_energy()            
            stop music fadeout 1.0            
            show expression "img/scene/witch_sex.jpg" as xxx
            play sound "sound/milking.ogg"
            pause (500.0)
            'Ведьма достаёт ведро и приступает к долгому, но приятному процессу. Чтобы выдоить дракона досуха, ей приходится без устали работать ротиком и руками в течение нескольких часов, но, похоже, она ОЧЕНЬ хочет драконье семя. Всё, что только можно добыть.'
            hide xxx  
            $ game.dragon.lust = 0
            stop sound fadeout 1.0
            call lb_witch_reward from _call_lb_witch_reward
            
        'Уйти':
            return
    
    return

label lb_witch_refuse:
    nvl clear    
    witch 'Я бы рада тебе помочь, но всё на свете требует оплаты. А ты уже потратил слишком много семени на деревенских потаскушек. Мне не нужны жалкие остатки. Возвращайся, когда отдохнёшь.'
    
    return

label lb_witch_reward:
    nvl clear    
    witch 'Мммм... Какая густота, какие объёмы. На год-другой мне этого хватит. Удружил, чешуйчатый. Проси чего хочешь!'
    menu:
        'Исцели меня' if game.dragon.health < 2:
            $ game.dragon.health = 2
            'Раны затянулись'
        'Дай мне золота':
            python:
                gain = game.dragon.level + 1
                game.lair.treasury.dublon += gain
            witch 'Дракон клянчит золото? Ну и дела! Ладно, вот все дублоны, что у меня есть: [gain]. Это того стоило.'
        'Научи меня колдовству':
            witch 'Я передам тебе часть своей силы, но это не навсегда. Ты сможешь сотворить одно заклятье по своему выбору, когда тебе потребуется...'
            $ game.dragon.spells.append('witch_spell')
            # старый вариант "поколдуй для меня"
            # $ game.choose_spell(u"Отказаться от заклинания")   
        'У меня всё есть':
            witch 'Оооо... да уж не влюбился ли ты? Ха-ха. Шучу. Спасибо за семя - приходи в любой момент, если нужно будет ещё... ммм... разрядиться. Мой ротик всегда к твоим услугам, здоровяк.'
            return
            
    
    return

label lb_witch_first_meet:   # Первая встреча с ведьмой
    $ game.first_meet = False
    $ game.witch_st2=0
    $ game.spell_list_rus = { 
    }
    $ game.spell_list = {
    }
    stop music fadeout 1.0
    python:
        witch = Talker(game_ref=game)
        witch.avatar = "img/avahuman/witch.jpg"
        witch.name = "Ведьма"
        renpy.music.play(get_random_files('mus/ambient')) 
    'На дороге, ведущей в Земли Вольных, дракон повстречал женщину'
    hide bg
    nvl clear
    show expression 'img/scene/witch_first_meet.jpg' as bg
    'Очень необычную женщину'
    nvl clear
    'От этой блондинки в нелепой широкополой шляпе прямо-таки веяло силой и могуществом.'
    witch 'Добрый день, [game.dragon.fullname].'
    game.dragon 'Кто ты?'
    'Конечно, [game.dragon.name] был агрессивным и похотливым чудовищем, не склонным к разговорам со встреченными девушками - но инстинкт самосохранения у него имелся!'
    witch 'Моё имя тебе ничего не скажет. Ты можешь зать меня ведьмой'
    game.dragon 'Что тебе нужно, ведьма? Ты друг или враг?'
    witch 'Скажем, так: у нас с Тёмной Госпожой несколько разные взгляды на будущее этого мира. Но деятельность драконов - твою и твоего рода - я в целом одобряю. И предлагаю помощь.'
    game.dragon 'Какую же?'
    witch  'Если тебя ранят, тебе потребуется золото или мана - ты всегда можешь прийти в руины на болоте и поделиться со мной своей спермой. А кроме того... тебе же хочется научиться заклинаниям, верно? '
    menu:
        'Конечно!':
            'Дракон невольно дёрнул хвостом. Заклинаний он действительно не знал'
            game.dragon 'Конечно, хочу!'
            witch 'Тогда приходи ко мне на руины, и я дам тебе несколько несложных заданий'
            game.dragon 'Каких именно?'
            witch 'Нужно соблазнить некоторых дев'
            'Дракон плотоядно облизнулся. Кажется, эти задания ему понравятся!'
            witch 'Но я потребую ещё одной платы. Когда - и если - придёт время, ты отдашь мне одну-единственную изнасилованную пленницу'
            game.dragon 'Кусок попользованного мяса - за возможность научиться колдовству? Идёт!'
            'Ведьма улыбнулась и растаяла в воздухе'
            $ game.witch_st1=1
        'Да я уже знаю все возможные заклинания!' if freeplay:
#            $ game.spell_list_rus['fire_protection'] = u"Защита от огня"
#            $ game.spell_list['fire_protection'] = ['fire_immunity']
            $ game.spell_list_rus = deepcopy(data.spell_book)
            $ game.spell_list = deepcopy(data.spell_unknown)
            game.dragon 'Да я уже все заклинания знаю!'
            witch 'Тогда это предложение снимается'
            $ game.witch_st1=0
            $ game.history = historical( name='witch_task_refuse',end_year=None,desc=None,image=None)
            $ game.history_mod.append(game.history)
    return

label lb_gwidon:
    hide bg
    nvl clear
    show expression 'img/scene/gwidon/1.jpg' as bg
    'Спустя девять месяцев король Сылтан получает известие о рождении наследника.'
    nvl clear
    hide bg
    show expression 'img/scene/gwidon/2.jpg' as bg
    'Родила блудница в ночь'
    hide bg
    show expression 'img/scene/gwidon/3.jpg' as bg
    'Не то сына, не то дочь;'
    hide bg
    show expression 'img/scene/gwidon/4.jpg' as bg
    'Не мышонка, не лягушку,'
    hide bg
    show expression 'img/scene/gwidon/5.jpg' as bg
    'А неведому зверюшку.' 
    nvl clear
    hide bg
    show expression 'img/scene/orc.jpg' as bg   
    pause 3.0
    show expression 'img/scene/gwidon/6.jpg' as bg
    'В гневе стал Сылтан чудесить' 
    hide bg
    show expression 'img/scene/gwidon/7.jpg' as bg
    'И гонца велел повесить.' 
    hide bg
    show expression 'img/scene/gwidon/8.jpg' as bg
    nvl clear
    'И велит своим придворным,\nСплетен избежав позорных,\nИ блудницу, и приплод\nТайно бросить в бездну вод.' 
    hide bg
    show expression 'img/scene/gwidon/9.jpg' as bg
    nvl clear
    'Королеву в тот же час\nВ бочку с сыном посадили,\nЗасмолили, покатили\nИ пустили в океан -\nКак велел король Сылтан' 
    hide bg
    show expression 'img/scene/gwidon/10.jpg' as bg
    nvl clear
    'В синем небе звёзды блещут,\nВ синем море волны плещут;\nТуча по небу идёт,\nБочка по морю плывёт.\nИ растёт орчонок там\nНе по дням, а по часам.' 
    nvl clear
    'Благодаря своим природным шаманским способностям принц Гвидон воззвал к духам воды, и бочку вынесло на берег отдалённого острова.'
    hide bg
    show expression 'img/scene/gwidon/11.jpg' as bg
    nvl clear
    'После чего он слегка поднатужился и с лёгкостью вышиб дно у прочнейшей бочки.'
    hide bg
    show expression 'img/bg/special/island.jpg' as bg
    nvl clear
    python:
        gwidon = Talker(game_ref=game)
        gwidon.avatar = "img/avahuman/orc.jpg"
        gwidon.name = "Гвидон"
    gwidon 'Хороший остров, даже странно, что на нём до сих пор нет поселений пиратов или контрабандистов. Послужит отличной базой для подготовки мести отцу.'
    queen 'Гвидон, ты...'
    gwidon 'Что - "я"? Ты собираешься простить человека, приговорившего нас к смерти?'
    queen 'Я понимаю твои чуства, сынок. Но принимать такие решения спонтанно - плохо. Месть может завести тебя очень далеко.'
    gwidon 'Ты права, прежде чем думать о мести, надо хотя бы прокормиться.'
    $ game.dragon.drain_energy() 
    gwidon 'Кто это?'
    'К матери и сыну неторопливо, совершенно не скрываясь, приближался [game.dragon.name]'
    game.dragon 'Здравствуй, Гвидон. Ты знаешь, кто я?'
    hide bg
    show expression 'img/scene/orc_fight.jpg' as bg
    nvl clear
    'В руках Гвидона как по волшебству материализуется топор.' 
    gwidon 'Чудовище, которое прислал Сылтан, чтобы расправиться с нами'
    gwidon 'Но отец просчитался. Прежде чем ты притронешься к маме, тебе придётся иметь дело со мной!'
    game.dragon 'Нет, король Сылтан не посылал меня.'
    menu:
      'Я пришёл сюда по своей воле':
        '[game.dragon.fullname] внезапно чувствует, что не может сказать ни слова. Очевидно, Гвидон неосознанно применил какое-то могучее шаманство.'
        gwidon 'Отлично. А теперь умри.'
        'Могучий орк с лёгкостью убивает парализованного дракона'
        jump lb_game_over
      'Гвидон, я твой отец!':
        hide bg
        nvl clear
        show expression 'img/scene/orc_no.jpg' as bg
        pause 3
        gwidon '{b}НЕЕЕЕЕТ!!!{/b}'
        hide bg
        show expression 'img/scene/orc_fight.jpg' as bg
        gwidon 'Мама, мама, ну скажи ему...'
        game.dragon 'Да-да, скажи ему, как я принял облик короля и взошёл на твоё ложе. Ты же наверняка почувствовала неладное, но никому в этом не призналась...'
        queen 'Я... я...'
        queen 'Я почувствовала, что случилось что-то ужасное. Что король был каким-то не таким. Но я и предположить не могла, что...'
        'Сын успокаивающе приобнимает свою мать.'
        gwidon 'Не переживай, мамочка. Всё уже случилось.'
        gwidon 'К тому же... лучше иметь отца-дракона, чем отца-человека, приказавшего убить собственного сына.'
        hide bg
        show expression 'img/bg/special/island.jpg' as bg
        gwidon 'Кстати, папочка, не подскажешь, как лучше отомстить Сылтану?'
        game.dragon 'Месть Вольным -  дело не одного десятилетия и даже не одного века.'
        game.dragon 'Но и твоя помощь будет неоценима, Гвидон. Вижу, что ты уже осваиваешься со своим шаманством. Построй на острове убежище для пиратов, контрабандистов и прочих лихих людей.'
        gwidon 'Ага, и они смогут подрывать экономику Королевства и помогать тебе в войне с Вольными.'
        gwidon 'Спасибо, отец! Я сделаю так, чтобы ты всегда был желанным гостем в нашем убежище!'
        menu:
          'Удачи тебе, сынок!':
            gwidon 'И тебе удачи, папаша!'
          'Ах да, и последнее: возьми свою мать, как мужчина - женщину':
            hide bg
            show expression 'img/scene/orc_fight.jpg' as bg 
            gwidon 'Что? Нет! Никогда!!!'
            game.dragon 'Ты мой сын, Гвидон. Я прекрасно знаю, что хочется тебе больше всего на свете'
            gwidon 'Я - разумный! Я могу сдерживать свои желания!'
            game.dragon 'А, ты воображаешь, что твоя мама - нежный, стеснительный и ранимый цветочек. Королева, ты рассказывала Гвидону, как зачла его?'
            queen 'Я...'
            if game.historical_check('queen_bound'):
              game.dragon 'Твоя мамаша обожает грубый и жестокий секс. Во время нашей встречи Королева попросила связать себя, а потом умоляла надругаться над ней всеми возможными способами.'
            elif game.historical_check('queen_group'):
              game.dragon 'А твоя мамаша расказывала, что пригласила на наше свидание служаночку? И что пока бедная девица стонала подо мной, она весело смеялась, целовала меня и ласкала себя?'
            elif game.historical_check('queen_double'):
              game.dragon 'А твоя мамаша расказывала, что во время встречи со мной её имели в оба отверстия двое стражников? А она смеялась, спрашивала, как мне это нравится, и предлагала присоединиться?'   
            else:
              game.dragon 'Эээ... у нас не было свидания? Тут какая-то ошибка...'
            gwidon 'Мама, это правда?'
            queen 'Гвидон, у моего мужа были проблемы с потенцией. Мне приходилось идти на унижения, чтобы...'
            game.dragon 'Она всем говорила о том, что это были унижения. Возможно, она убедила в этом даже саму себя.'
            game.dragon 'Но  я видел Королеву в моменты страсти. Ей и в самом деле это нравилось. Она и впрямь обожала отвергать табу и вгрызаться в запретный плод.'
            game.dragon 'Уверен, кровосмесительная связь ей тоже придётся по вкусу.'
            gwidon 'Мама, скажи мне только одно. Ты любила короля?'
            queen 'Сын, я...'
            gwidon 'Да или нет?'
            queen 'Да.'
            gwidon 'Хотя знала, что он за человек? Любила, несмотря на все его извращения?'
            'Королева судорожно кивает'
            'Гвидон широко усмехается'
            gwidon 'Значит, и меня тоже полюбишь!'
            hide bg
            show expression 'img/scene/orc_sex/1.jpg' as bg 
            pause 4
            queen 'Гвидон! Нет, не надо, прошу тебя!'
            gwidon 'Мам, расслабься и получай удовольствие. '
            queen 'Сыночек, но это же извращение, нельзя же так... Ох...'
            gwidon 'Вижу, ты уже втягиваешься. Если это пойдёт к обоюдному удовольствию, то можно. Полижи пока.'
            hide bg
            show expression 'img/scene/orc_sex/2.jpg' as bg 
            pause 4
            queen 'Сынок, но он такой большой... он же не войдёт!'
            game.dragon 'Войдёт, войдёт...'
            gwidon 'Ничего, мы аккуратненько. Иди сюда, мамочка.'
            hide bg
            show expression 'img/scene/orc_sex/3.jpg' as bg 
            pause 4
            queen 'Сыночек, может, не надо?'
            gwidon 'Надо, мама, надо.'
            gwidon 'Начинай потихонечку'
            hide bg
            show expression 'img/scene/orc_sex/4.jpg' as bg 
            pause 4
            queen 'Ох, Гвидончик, это так, так... Ооох...'
            gwidon 'Вот видишь, тебе уже нравится!'
            hide bg
            show expression 'img/scene/orc_sex/5.jpg' as bg 
            pause 4
            gwidon 'И ты, мам... поосторожней, у меня и вправду большой...'
            queen 'Молчи уж, я знаю, что делаю!'
            game.dragon 'Обожаю переманивать сыновей на Тёмную сторону!'
            gwidon 'Пап, а ты что стоишь как неродной? Присоединияйся!'
            queen 'Да... присоединяйся... И спасибо - так бы Гвидон никогда бы не решился... И я бы не решилась...'
            game.dragon 'С удовольствием!'
            $ game.dragon.lust-=1
    return

label lb_witch_1_aftermath:
    $ place = 'plain'
    hide bg
    show expression get_place_bg(place) as bg
    nvl clear
    if game.historical_check('marshal_hard'):  
      'Выйдя из руин, дракон оказался в землях герцога де Пруа'
      game.dragon 'Хм, а чего это гарью пахнет? Надо сходить проверить.'
      $ game.dragon.drain_energy()
      hide bg
      show expression 'img/scene/fear/plains/castle/castle_st3.jpg' as bg
      nvl clear
      game.dragon 'А, это королевские войска жгут замок герцогов де Пруа! Ничего интересного.'
      'Дракон, немного понаблюдав с безопасного расстояния, почувствовал едва уловимый, но неимоверно притягательный аромат'
      game.dragon 'О, одна из дочерей герцога всё-таки выжила! Надо бы подойти, познакомиться...'
      'Девица сидит, прислонившись к стволу дерева. Она явно обессилила от долгого бега и не может даже встать на ноги.'
      $ description = game.girls_list.new_girl(girl_type='princess',girl_nature='proud',tres=False, family = u"де Пруа")  # Вызываем девушку с характером
      game.girl "[description]"
      $ text = u'%s выпала злая судьба. Королевские войска взяли и разграбили замок герцога Робертина де Пруа. %s видела гибель своей стааршей сестры и брата. Им ещё повезло - судьба осстальных родичей была гораздо более страшной. Сама %s сбежала фактически чудом - только для того, чтобы наткнуться в лесу на дракона.\n\n' % (game.girl.name_d, game.girl.name, game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
      game.girl 'А, меня сейчас будут насиловать. Причём дракон.'
      'Голос [game.girl.name_r] полон усталого безразличия'
      game.dragon 'И тебя это не пугает?'
      game.girl 'После того, что я сегодня видела? Нисколько.'
      game.girl 'Слушай, дракон. Давай я тебе отдамся, а ты мне денег дашь, отнесёшь подальше и отпустишь?'
      game.dragon 'С какой это стати?'
      game.girl 'А я восстание подниму. После сегодняшнего нам с королём Сылтаном на одном свете не жить...'
      game.dragon.third '[game.dragon.fullname] задумывается. С одной стороны, чем больше неурядиц у Вольных, тем лучше для Тёмной Госпожи. С другой стороны, денег-то тоже жалко!'
      menu:
        'Дать 500 фартингов':
          $ game.lair.treasury.money -= 500
          $ game.girl.willing=True # Добровольно согласна на секс с драконом
          $ text = u'Впрочем, %s сумела найти плюсы даже в этой ситуации. Она добровольно отдалась дракону за 500 фартингов, надеясь на эти деньги заложить основу повстанческой армии.\n\n' % game.girl.name
          $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
          game.dragon 'Держи, вымогательница!'
          '[game.girl.name] устало пожимает плечами.'
          game.girl 'Я твоя.'
          nvl clear
          menu:
           'Надругаться' if game.girls_list.is_mating_possible:
            # Alex: Added sex images:
              call lb_nature_rape from _call_lb_nature_rape_5
              if game.girl.dead:
                return
           'Магическое уменьшение' if not game.girls_list.is_mating_possible and game.girl.virgin and not game.girls_list.is_giant and game.dragon.lust > 0 and not game.girl.old:
             game.dragon 'Заклятье временного уменьшения!'
             $ game.dragon.gain_rage()
             call lb_nature_rape from _call_lb_nature_rape_6
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
          $ game.history = historical( name='rebel_daughter',end_year=game.year+1,desc=None,image=None)
          $ game.history_mod.append(game.history)
        'Чтобы я давал деньги мясу?!':
          call lb_nature_sex from _call_lb_nature_sex_57 
    elif game.historical_check('marshal_soft'): 
      'Выйдя на большую дорогу, дракон заметил одиноко бредущую женщину. Она дракона тоже заметила.'
      game.dragon 'Попользованный материал, не интересно.'
      python:
        beggar = Talker(game_ref=game)
        beggar.avatar = "img/avahuman/beggar.jpg"
        beggar.name = "Изольда де Пруа"
      beggar 'Подождите, не уходите! У меня есть дочь, и я могу вам её продать!'
      game.dragon 'Крестьянка?'
      'Впрочем, [game.dragon.name] быстро понял свою ошибку: крестьянками тут и не пахло.'
      beggar 'Аристократка. Я - Изольда де Пруа. Моего мужа, Робертина, казнили по обвинению в измене, земли и имущество  отобрали. Мы с семьёй голодаем. Думаю, для девочки будет лучше, если она отправится с вами. По сравнению с тем, что случилось с её старшей сестрой, это будет хотя бы... быстро.'
      game.dragon 'И сколько она стоит?'
      beggar 'Я хочу поднять восстание против тирании Сылтана. Мне нужны соратники, наёмники... 500 фартингов.'
      menu:
        'Дать 500 фартингов':
          $ game.dragon.drain_energy()
          $ game.lair.treasury.money -= 500
          game.dragon 'Согласен, вымогательница!'
          $ place = 'plain'
          hide bg
          show expression get_place_bg(place) as bg
          nvl clear
          'Спустя некоторое время дракон обменял мешочек с золотом на аппарат по производству отродий'
          beggar 'Девочка почему-то думает, что вы влюблены в неё. Хотите - рушьте её иллюзию, хотите - нет...'
          $ description = game.girls_list.new_girl(girl_type='princess',girl_nature='innocent',tres=False, family = u"де Пруа")  # Вызываем девушку с характером
          game.girl "[description]"
          $ text = u'%s выпала нелёгкая судьба. Король казнил герцога Робертина де Пруа и отобрал все земли, имущество и титулы. %s влачила полуголодное существование, пока её мать Изольда не продала девушку дракону. Бывшая герцогиня хотела поднять восстание, а %s... Она с чего-то решила, что дракон влюбился в неё! \n\n' % (game.girl.name_d, game.girl.name, game.girl.name)
          $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
          game.girl 'Спасибо вам. Я впервые за несколько месяцев поела досыта.'
          game.girl 'Я знаю, что вы намерены... что я согрешу, и согрешу страшно. Я постараюсь отмолить этот грех.'
          $ game.girl.willing=True # Добровольно согласна на секс с драконом
          call lb_nature_sex from _call_lb_nature_sex_58
          $ game.rebel_girl=beggar
          $ game.history = historical( name='rebel_mother',end_year=game.year+1,desc=None,image=None)
          $ game.history_mod.append(game.history)
        'Прибить попрошайку':
          'Одним движением хвоста дракон убивает наглую попрошайку и идёт дальше по своим делам.'
    elif game.historical_check('marshal_none'): 
      'Выйдя из руин, дракон оказался в землях герцога де Пруа'
      game.dragon 'Хм, а что это за шум такой? Герцог турнир устраивает, что ли? Надо сходить проверить.'
      call lb_enc_tornament from _call_lb_enc_tornament_1
    elif game.historical_check('treasurer_hard'): 
      'Выйдя на большую дорогу, дракон с удивлением замечает караван работорговцев.'
      game.dragon 'Неужели в королевстве наконец-то легализовали этот достойный и почётный бизнес?'
      call lb_enc_slavers from _call_lb_enc_slavers_1
    elif game.historical_check('treasurer_soft'): 
      'Странствуя по Королевству, дракон услышал какой-то подозрительный шум.'
      game.dragon 'Так, надо бы проверить!'
      hide bg
      show expression 'img/scene/dwarf_fortress.jpg' as bg
      nvl clear
      'Группа из семи цвергов с ожесточением копает кирками землю'
      game.dragon 'А, это цверги свою карлиовую крепость строят!'
      game.dragon 'Грабить их сейчас - идиотизм, всё равно у них ничего, кроме кирок, нет. Вот когда поднакопят богатств, тогда можно будет и повеселиться!'
      game.dragon 'Правда, вряд ли они построят свою крепость раньше следующей версии игры.'
    elif game.historical_check('treasurer_none'): 
      'Выйдя на большую дорогу, дракон с удовольствием замечает фургон торговца.'
      game.dragon 'Видимо, ревизия в сокровищнице пошла Королевству на пользу!'
      call lb_enc_trader from _call_lb_enc_trader_1
    elif game.historical_check('spy_hard'): 
      hide bg
      show expression 'img/scene/mire/1.jpg' as bg
      'Выйдя из руин, [game.dragon.fullname] заметил прекрасную белокурую девственницу, по неосмотрительности зашедшую в самую топь. О, да судя по запаху, это аристократка!'
      game.dragon 'Разве ей неизвестно, что если вам дороги жизнь и рассудок, держитесь подальше от торфяных болот?'
      hide bg
      show expression 'img/scene/mire/2.jpg' as bg
      nvl clear
      'Тем временем девушка, погрузившаяся уже по живот, в панике звала на помощь.'
      menu:
        'Выловить девицу из трясины':
          call lb_ruin_mire from _call_lb_ruin_mire_1
        'Интересно, что будет дальше?':
          hide bg
          show expression 'img/scene/mire/3.jpg' as bg
          nvl clear
          'Болотная жижа ласково  обняла девичью шейку. Крики стали приглушённее - утопающая сильно запрокинула голову.'
          menu:
            'Выловить девицу из трясины':
              call lb_ruin_mire from _call_lb_ruin_mire_2
            'Интересно, что будет дальше?':
              hide bg
              show expression 'img/scene/mire/4.jpg' as bg
              nvl clear
              'Жижа дошла до уровня рта. Кажется, сейчас самое время сделать глубокий вдох!'
              menu:
                'Выловить девицу из трясины':
                  call lb_ruin_mire from _call_lb_ruin_mire_3
                'Интересно, что будет дальше?':
                  hide bg
                  show expression 'img/scene/mire/5.jpg' as bg
                  nvl clear
                  'Вскоре на поверхности остались лишь две белокурые косички'
                  game.dragon 'Всё, дальше уже не будет ничего интересного!'
    elif game.historical_check('spy_soft'): 
      game.dragon 'Может быть, мне стоит исповедоваться в грехах?'
      game.dragon 'Хм, почему бы и нет!'
      $ game.witch_st1=6
      call lb_location_city_main from _call_lb_location_city_main_1
    elif game.historical_check('spy_none'): 
      $ place = game.lair.type_name
      hide bg
      show place as bg
      nvl clear
      'На пороге своего логова [game.dragon.fullname] обнаружил записку. Кажется, её принёс какой-то мелкий воздушный дух по просьбе Гвидона'
      nvl clear
      gwidon.third 'Папаш, мама хочет, чтобы ты встретился с её подругой Марианной, племянницей короля. Она будет ждать тебя завтра, в столичном трактире "Подвязки королевы". '
      game.dragon 'Звучит возбуждающе!'
      $ game.witch_st1=7
      call lb_location_city_main from _call_lb_location_city_main_2
    return

label lb_ruin_mire:
    $ game.dragon.drain_energy()
    hide bg
    show expression 'img/scene/mire.jpg' as bg
    nvl clear
    'Дракон с лёгкостью вытаскиает девицу из болота'
    $ description = game.girls_list.new_girl(girl_type='princess',girl_nature='proud',girl_hair='blond',tres=False,name_number='28',avatar='img/avahuman/marianna.jpg') 
    game.girl "[description]"
    $ text = u'%s родилась племянницей короля - и в этом не было ничего хорошего. Сылтан решил избавиться от потенциальной претендентки на престол. Когда %s поняла, что нападение "разбойников" неизбежно, она бежала. Увы, неудачно - аристократка забрела в болота, и её неминуемо ждала бы страшная смерть, если бы не проходящий поблизости дракон. Вот только у него на девушку были вполне определённые планы...\n\n' % (game.girl.name, game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    game.girl 'Сказать по правде, я бы предпочла, чтобы из болота меня спас НЕ дракон'
    game.dragon 'Могу кинуть обратно!'
    game.girl 'Нет уж, спасибо. А если я скажу, что буду сопротивляться твоим домогательствам?'
    game.dragon 'Тогда я скажу, что сожру тебя'
    game.girl 'Тогда давай так: я отдамся тебе добровольно, а ты заплатишь мне 500 фартингов, доставишь в безопасное место и отпустишь?'
    game.dragon 'С какой стати?'
    game.girl 'Я племянница короля, чтоб ему на сковородке корчиться. Он давно хотел меня убить. Когда я поняла, что до летнего поместья не доеду - непременно наткнусь на "неопознанных" разбойников - я бежала прочь. К сожалению, не очень удачно - оказалась в болоте.'
    game.girl 'Если ты дашь мне денег, то я подниму восстание против короля Сылтана. Тебе же сплошная выгода, так ведь?'
    game.dragon.third '[game.dragon.fullname] задумывается. С одной стороны, чем больше неурядиц у Вольных, тем лучше для Тёмной Госпожи. С другой стороны, денег-то тоже жалко!'
    menu:
      'Дать 500 фартингов':
        $ game.lair.treasury.money -= 500
        $ game.girl.willing=True # Добровольно согласна на секс с драконом
        $ text = u'Впрочем, %s удачно обменяла свою невинность на 500 фартингов, надеясь на эти деньги заложить основу повстанческой армии.\n\n' % (game.girl.name)
        $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
        game.dragon 'Держи, вымогательница!'
        '[game.girl.name] смотрит на дракона безо всякой приязни и цедит сквозь сомкнутые зубы'
        game.girl 'Я твоя.'
        nvl clear
        menu:
         'Надругаться' if game.girls_list.is_mating_possible:
            # Alex: Added sex images:
            call lb_nature_rape from _call_lb_nature_rape_7
            if game.girl.dead:
              return
         'Магическое уменьшение' if not game.girls_list.is_mating_possible and game.girl.virgin and not game.girls_list.is_giant and game.dragon.lust > 0 and not game.girl.old:
           game.dragon 'Заклятье временного уменьшения!'
           $ game.dragon.gain_rage()
           call lb_nature_rape from _call_lb_nature_rape_8
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
        call lb_nature_sex from _call_lb_nature_sex_59 
    return

