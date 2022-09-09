# coding=utf-8

label lb_enc_noting:
    $ place = 'poverty'
    $ current_image=get_place_bg(place)
    hide bg
    show expression get_place_bg(place) as bg 
    $ choices = [
        ("lb_enc_empty", 10),
        ("lb_enc_refuge", 10),
        ("lb_enc_alv", 5),
        ("lb_enc_gift", 10),
        ("lb_enc_cannibal", 10),
        ("lb_enc_plague", 10)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_enc_empty:   # Пусто
    'Здесь лишь запустение и разруха. Хотя когда-то тут можно было встретить людей или животных, сейчас их больше нету. Кругом лишь разрушенные дома да заросшие бурьяном пашни.'
    python:
        if game.dragon.bloodiness < 5: 
            game.dragon.gain_rage()
    return

label lb_enc_refuge:
    'По дороге тянется длинный караван оборванных беженцев. Один лишь слух о том, что в соседней области никто не слышал ни о каком драконе, вынудил их бросить родные места. Они ещё не знают, что слух этот оказался лишь слухом.'
    menu:
        'Перебить беженцев':
            $ game.dragon.drain_energy()
            'С диким рёвом [game.dragon.name] врывается в толпу обезумевших беженцев, убивая их направо и налево. Отчавяшиеся люди и не помышляют о сопротивлении, разбегаясь в разные стороны. Залив дорогу кровью и завалив ошмётками мяса, [game.dragon.name] сполна потешил своё самолюбие и отточил охотничьи инстинкты.'
            if game.dragon.hunger > 0:
              menu:
                  'Устроить пиршество':
                      'Дракон всласть попировал на останках жалких людишек'
                      $ game.dragon.bloodiness = 0
                      $ game.dragon.hunger -= 1
                      $ game.dragon.reputation.points += 5
                      '[game.dragon.reputation.gain_description]'
                  'Поискать кого-нибудь повкуснее':
                      'Вскоре о драконе напоминали лишь разорванные трупы'
                      $ game.dragon.reputation.points += 3
                      '[game.dragon.reputation.gain_description]'
            else:
                $ game.dragon.reputation.points += 3
                '[game.dragon.reputation.gain_description]'
        'Поискать невинную девушку': 
            'Среди этих беженцев должна была найтись невинная девушка - чисто по теории вероятности. И научный подход на сей раз оправдался!'
            $ chance = random.choice(['peasant', 'peasant', 'peasant', 'citizen'])
            $ game.dragon.drain_energy()
            $ description = game.girls_list.new_girl(chance)
            $ text = u'%s росла в тяжёлое время. Жестокий и беспощадный дракон свирептсовал в Королевстве, сея разруху и ужас. Семья девушки бежала из родных мест в поисках лучшей доли. И когда %s устало брела по бесконечной дороге, дракон приметил себе новую жертву.\n\n' % (game.girl.name, game.girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            '[game.dragon.kind] стремительно врывается в толпу беженцев. Люди разбегаются в страхе, но дракона не интересуют их жалкие жизни. Его цель - оборванная и голодная девушка, бредущая куда-то в неизвестность. Даже появление дракона не взбодрило уставшую путницу - она лишь бессильно обмякла в его объятиях, отдаваясь на волю судьбы.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_48
        'Пусть себе бредут' if game.dragon.bloodiness<5:
            $ game.dragon.gain_rage()
            'Пожав хвосстом, [game.dragon.kind] отправился по более важным делам'
    return

label lb_enc_alv:
    'На окраине бесплодного поля стоит альва и тщательно проводит какой-то сложный магический ритуал. Кажется, дети богини Дану решили помочь людям, страдающим от разразившегося голода'
    menu:
        'Схватить девицу':
            $ game.dragon.drain_energy()
            'Лесная фея настолько сконцентрировалась на своём ритуале, что не заметила дракона, пока он не сжал её в своих объятиях!'
            'Теперь альвы постерегутся помогать смертным, и голод в людских землях будет воистину страшным.'
            $ game.poverty.value += 1
            $ description = game.girls_list.new_girl('elf')
            $ text = u'%s, услышав о разразившемся в землях людей голоде, бесстрашно отпраилась им на помощь. Она решила провести древний ритуал, способный даровать обильный урожай всего через пару-тройку недель. Увы, в эти дни Королевство полно опасностей - дракон легко захватил беспечную чаровницу!\n\n' % (game.girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_49
        'Да пусть помогает, мне-то что?' if game.dragon.bloodiness<5:
            $ game.dragon.gain_rage()
            game.dragon 'Пусть помогает. Ведь если люди сдадутся раньше времени, это будет совершенно неинтересно!'
    return

label lb_enc_gift:
    '[game.dragon.name] зашёл в разорённую деревеньку'
    game.dragon 'Кажется, ничего я здесь не найду'
    'Из какой-то землянки наружу выходит древняя старуха'
    python: #делаем аватарку старухи  для диалогового окна
        crone= Talker(game_ref=game)
        crone.avatar = "img/avahuman/crone.jpg"
        crone.name = 'Старая карга' 
    crone 'Батюшки светы, спаситель пришёл!'
    game.dragon 'Спаситель?!'
    crone 'Умираем мы, милок. С голоду пухнем. Я и внученька моя, ненаглядная. Уж как я её уговаривала меня съесть и бежать прочь, а она ни в какую. Пожалуйста, спасите её, на вас вся надежда!'
    nvl clear
    'Из землянки, шатаясь от голода, выходит осунувшаяся и измождённая девушка'
    menu:
        'Идёт!':
            $ game.dragon.drain_energy()
            'Прикончив старуху одним ударом, дракон склонился над её внучкой'
            $ description = game.girls_list.new_girl('peasant')
            $ game.girl.willing=True # Добровольно согласна на секс с драконом
            $ text = u'Тяжело жить в голодную годину. %s со своей бабушкой оказались единственными жителями деревни, дожившими до прилёта дракона. Злобный ящер приккончил старуху и захватил девушку. %s спаслась от голодной смерти... но не окажется ли её участь ещё горше? \n\n' % (game.girl.name, game.girl.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_50
        'Умирайте на здоровье!' if game.dragon.bloodiness<5:
            $ game.dragon.gain_rage()
            game.dragon 'Полудохлые простолюдинки меня не возбуждают. Счастливо оставаться!'
    return

label lb_enc_cannibal:
    '[game.dragon.name] заметил в лесу подозрительное шевеление'
    'Тяжело шатаясь, навстречу дракону вышла девушка и бросилась ему на шею'
    game.dragon 'Эт-то ещё что такое? Это я должен быть охотником, а не наоборот!'
    $ description = game.girls_list.new_girl('peasant',tres=False)
    $ game.girl.willing=True # Добровольно согласна на секс с драконом
    $ text = u'Тяжело жить в голодную годину. %s сбежала от родного отца, который, обезумев от голода, решил съесть собственную дочь. У ослабевшей девушки не было ни единого шанса, но ей повезло наткнуться на дракона. Ну, или НЕ повезло, это как посмотреть.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
    game.girl 'Умоляю, спаси!'
    game.girl 'Мы умираем с голода, и мой отец решил меня съесть!'
    game.dragon.third 'Дракон прекрасно понимал этого достойного человека'
    'Из-за деревьев вышел косматый и бородатый мужик с топором'
    menu:
        'Кто смеет покушаться на МОЁ мясо?!':
            $ game.dragon.drain_energy()
            'Прикончив тестя одним ударом, дракон перешёл к более плотному знакомству с девушкой.'
            $ text = u'%s спас бедняжку, убив её родного отца.\n\n' % (game.dragon.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex from _call_lb_nature_sex_51
        'Пожалуй, стоит устроить пирушку здесь и сейчас!' if game.dragon.hunger > 0:
            $ game.dragon.drain_energy()
            game.dragon 'Добро пожаловать к столу, приятель!'
            'Обедая вкусной и здоровой пищей, дракон и человек быстро нашли общий язык. Расстались они добрыми друзьями.'
            $ game.dragon.bloodiness = 0
            $ game.dragon.hunger -= 1
            $ text = u'Однако дракон предпочёл подзакусить девушкой тут же, в лесу. Он щедро поделился мясом с её отцом. %s и его несостоявшийся тесть расстались добрыми друзьями.\n\n' %(game.dragon.name)
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            $ current_image=sex_imgs.get_eat_image()
            $ game.chronik.death('cannibal','img/bg/poverty/04.jpg')
        'Пожелать приятного аппетита и уйти' if game.dragon.bloodiness<5:
            $ game.dragon.gain_rage()
            game.dragon 'Приятного аппетита!'
            $ text = u'Однако дракон решил не вмешиваться в семейный скандал и оставил девушку наедине с её папашей.\n\n' 
            $ game.chronik.write_chronik(text,game.dragon.level,game.chronik.girl_id)
            $ game.chronik.death('cannibal','img/bg/poverty/04.jpg')
    return

label lb_enc_plague:
    game.dragon 'Эта деревня вымерла. Интересно, от чего?'
    game.dragon 'А, от чумы! Хорошо, что драконы иммунны к человеческим болезням'
    game.dragon 'Хм, а ведь можно отнести переносчиков чумы в иные области Королевства!'
    menu:
        'Тяжёлый, но благородный труд!':
            $ game.dragon.drain_energy()
            $ game.poverty.value += 1
            'Благодаря усилиям дракона новые очаги чумы появилиссь в различных областях Королевства'
        'Не, лениво' if game.dragon.bloodiness<5:
            $ game.dragon.gain_rage()
            game.dragon 'Мне, дракону, возиться с какими-то блохами?! Вот ещё!'
    return

