# coding=utf-8

label lb_talk:
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    if not game.girl.talk_was:
      call lb_talk_conditions from _call_lb_talk_conditions
    else:
      $ cost=data.gift_price[game.girl.type][game.girl.nature]
      game.girl 'Моё условие ты слышал - подарок за [cost] фартингов.'
    menu:
      'Выбрать украшение':
        $ game.chronik.active_gift = None
        call screen order_treasury(cost=data.gift_price[game.girl.type][game.girl.nature],gift_mod=True)
      'Хм... Лучше поговорим об этом в другой раз':
        game.girl 'Все мужики - козлы! Даже драконы.'
        return
    return

label lb_talk_conditions:
    game.dragon 'Послушай, я ж не зверь какой. Когда жертва брыкается, пинается и вырывается - в этом ничего приятного нет, одно раздражение. Может, я тебе какую-нибудь цацку подарю, и ты мне спокойно отдашься? '
    if game.girl.type=='peasant' and game.girl.nature=='lust':
      game.girl 'Да я и так не против. Хотя...'
      '[game.girl.name] осекается, а потом продолжает с плохо скрываемым трепетом'
      game.girl 'Хотя если ты подаришь мне какую-нибудь безделицу стоимостью в двести фартингов...'
    elif game.girl.type=='peasant' and game.girl.nature=='proud':
      game.girl 'Никогда.'
      '[game.girl.name] размышляет несколько секунд, а потом говорит не менее категорично.'
      game.girl 'Согласна.'
      game.dragon 'С чего такая перемена?'
      game.girl 'Ты меня всё равно обесчестишь или в лучшем случае сожрёшь. Но если я вернусь в деревню с украшением стоимостью четыреста фартингов... с таким приданым меня даже мельник в жёны возьмёт, на невинность и не взглянет.'
    elif game.girl.type=='peasant' and game.girl.nature=='innocent':
      game.girl 'Нет, я отдам свою невинность только тому, кого полюблю и кто полюбит меня!'
      'Дракон плотоядно облизыается'
      game.dragon 'Я тебя очень, очень люблю!'
      game.girl 'Не верю!'
      game.dragon 'Честное драконье! Подарок какой стоимости тебе подарить, чтобы ты в этом убедилась?'
      '[game.girl.name] надолго задумывается, а потом неуверенно отвечает'
      game.girl 'Восемьмсот фартингов...'
      'Чуствуется, девушка просто не верит, что такие украшения вообще существуют.'
    elif game.girl.type=='citizen' and game.girl.nature=='lust':
      '[game.girl.name] мило краснеет'
      game.girl 'Ой, что за неприличные вещи вы говорите!'
      game.girl 'Хотя, если речь идёт о подарке стоимостью в пятьсоот фартингов...'
    elif game.girl.type=='citizen' and game.girl.nature=='proud':
      game.girl 'Никогда.'
      '[game.girl.name] размышляет несколько секунд.'
      game.girl 'Так, мне нужны счёты.'
      'Заполучив необходимый инструмент, [game.girl.name] начинает что-то высчитывать. Дракон заинтересованно склоняется над записями.'
      game.dragon 'Что считаешь?'
      game.girl 'У моей семьи серьёзные финансовые трудности. Пытаюсь понять, предмет какой стоимости может их скомпенсировать.'
      game.girl 'Тысяча фартингов.'
      game.dragon 'И стоило столько считать, чтобы получить такую круглую сумму?'
      game.girl 'Могу увеличить'
      game.dragon 'Не-не-не!'
    elif game.girl.type=='citizen' and game.girl.nature=='innocent':
      game.girl 'Нет, я верю, что ещё найду свою истинную любовь!'
      'Дракон плотоядно облизыается'
      game.dragon 'Я - твоя истинная любовь!'
      game.girl 'Нет!'
      game.dragon 'Честное драконье! Давай я подарю тебе подарок стоимостью в две тысячи фартингов?'
      'У [game.girl.name_r] округляются глаза. Кажется, дочь торговца хорошо представляет себе, о какой ценности идёт речь'
      game.girl 'Две тысячи фартингов... Так вы и вправду меня любите?'
    elif game.girl.type=='princess' and game.girl.nature=='lust':
      '[game.girl.name] мило опускает глазки'
      game.girl 'Ну вы же дракон, а значит подарки у вас должны быть даже не королевские, а драконьи... Тысяча пятьсот фартингов!'
    elif game.girl.type=='princess' and game.girl.nature=='proud':
      game.girl 'Никогда.'
      '[game.girl.name] погружается в недолгие размышления, а затем резко меняет своё мнение'
      game.girl 'Три тысячи фартингов.'
      game.dragon 'С чего такая перемена?'
      game.girl 'Ты меня всё равно обесчестишь или в лучшем случае сожрёшь. Но если у меня будет такое сокровище, то после возвращения я смогу нанять опытных героев, чтобы они убили тебя.'
    elif game.girl.type=='princess' and game.girl.nature=='innocent':
      game.girl 'Нет. Согласно всем прочитанным балладам, вскоре меня должен спасти прекрасный рыцарь, за которого я и выйду замуж!'
      'Дракон плотоядно облизыается'
      game.dragon 'Я - твой прекрасный рыцарь!'
      '[game.girl.name] окидывает дракона крайне скептическим взглядом'
      game.girl 'Что-то не похож'
      game.dragon 'Честное драконье! Давай я, как положено прекрасному рыцарю, совершу невозможный подвиг!'
      game.girl 'Отустишь меня домой?'
      game.dragon 'Лучше! Подарю легендарное сокровище за шесть тысяч фартингов!'
      'Аристократка глядит на дракона с небывалым потрясением'
      game.girl 'Так вы и вправду заколдованный прекрасный принц? И чтобы снять злые чары, я должна вас поцеловать?'
      game.dragon 'Эту гипотезу определённо надо проверить. Но, думаю, поцелуями тут не обойдёшься...'
    $ game.girl.talk_was=True
    return

label lb_talk_gift:
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    if game.chronik.active_gift is None:
      game.girl 'Все мужики - козлы! Даже драконы.'
    else:
      if game.chronik.active_gift.treasure_type=='dish':
        game.girl 'Блюдо? Ох, было бы что с него есть...'
      elif game.chronik.active_gift.treasure_type=='goblet':
        game.girl 'Кубок? Что же, теперь будет из чего пить вино... если мне вообще удастся попробовать хоть немного вина.'
      elif game.chronik.active_gift.treasure_type=='cup':
        game.girl 'Чаша? Ох, было бы что из неё пить...'
      elif game.chronik.active_gift.treasure_type=='casket':
        game.girl 'Шкатулка? Жаль, что мне в неё нечего складывать.'
      elif game.chronik.active_gift.treasure_type=='statue':
        game.girl 'Статуэтка? Очень... мило.'
      elif game.chronik.active_gift.treasure_type=='tabernacle':
        game.girl 'Дарохранительница? И ты осквернил такую святыню? Неужели ты совсем не боишься гнева Небесного Отца?'
      elif game.chronik.active_gift.treasure_type=='icon':
        game.girl 'Икона? Её точно придётся в церковь отдать...'
      elif game.chronik.active_gift.treasure_type=='tome':
        game.girl 'Фолиант? Интересно, что в нём написано...'
      elif game.chronik.active_gift.treasure_type=='comb':
        game.girl 'Гребень? Здорово,мне его очень не хватало!'
      elif game.chronik.active_gift.treasure_type=='phallos':
        game.girl 'Хм-хм. Фаллос. Как... символично.'
      elif game.chronik.active_gift.treasure_type=='mirror':
        game.girl 'Свет мой, зеркальце, скажи... или нет, лучше не говори.'
      elif game.chronik.active_gift.treasure_type=='band':
        game.girl 'Обруч? Мне идёт, правда?'
      elif game.chronik.active_gift.treasure_type=='diadem':
        game.girl 'Диадема? Господи, это же королеве в пору...'
      elif game.chronik.active_gift.treasure_type=='tiara':
        game.girl 'Тиара? Господи, какая красота, это же королеве в пору...'
      elif game.chronik.active_gift.treasure_type=='earring':
        game.girl 'Серёжка? Как хорошо, что у меня проколоты уши!'
      elif game.chronik.active_gift.treasure_type=='necklace':
        game.girl 'Ожерелье? Какие аккуратные бусины...'
      elif game.chronik.active_gift.treasure_type=='pendant':
        game.girl 'Кулон? Нда, и ты наверняка предпочтёшь, чтобы я носила его между грудей...'
      elif game.chronik.active_gift.treasure_type=='ring':
        game.girl 'Кольцо? А оно невидимость случайно не даёт? Жаль, жаль...'
      elif game.chronik.active_gift.treasure_type=='broch':
        game.girl 'Брошь? Ох, было бы к чему её прикалывать...'
      elif game.chronik.active_gift.treasure_type=='gemring':
        game.girl 'Перстень? А он никакими магическими способностями случайно не обладает? Жаль, жаль...'
      elif game.chronik.active_gift.treasure_type=='seal':
        game.girl 'Перстень-печатка? Ну да, конечно же, мне же так много всего приходится запечатывать!'
      elif game.chronik.active_gift.treasure_type=='armbrace':
        game.girl 'Браслеты? Надеюсь, они мне придутся в пору...'
      elif game.chronik.active_gift.treasure_type=='legbrace':
        game.girl 'Ножные браслеты? Это что-то варварское, из Султаната?'
      elif game.chronik.active_gift.treasure_type=='crown':
        game.girl 'Корона? Господи, её же не примеришь, это же тяжелейшее государственное преступление!'
      elif game.chronik.active_gift.treasure_type=='scepter':
        game.girl 'Скипетр? Господи, как же я его продавать-то буду!'
      elif game.chronik.active_gift.treasure_type=='chain':
        game.girl 'Цепь? Да уж, на цепи мне сидеть придётся долго...'
      elif game.chronik.active_gift.treasure_type=='fibula':
        game.girl 'Фибула? Ох, было бы что ей закалывать...'
      game.girl 'Ну, спасибо. Кстати, а откуда у тебя это сокровище?'
      call lb_talk_obtained from _call_lb_talk_obtained_1

#    $ game.girls_list.jail_girl()
    return

label lb_talk_obtained(repeat=False):
    if game.chronik.active_gift.obtained=="":
      $ obtained="Но я и вправду не знаю!"
    else:
      $ obtained=u"%s" % game.chronik.active_gift.obtained
    menu:
      '[obtained]':
        if obtained.startswith(u"Принадлежало красавице по имени"):
          game.girl 'Интересно, что сейчас стало с этой бедняжкой?'
          call lb_talk_girl from _call_lb_talk_girl_1
          if game.chronik.active_gift is None:
            return
        elif obtained=="Это предмет принадлежал друиду - стражу зачарованого леса.":
          game.girl 'То есть ты отобрал его у язычника? Думаю, я могу взять эту вещь...'
        elif obtained=="Это предмет из королевской сокровищницы альвов зачарованного леса.":
          game.girl 'Заполучить вещь из легендарной сокровищницы альвов... Спасибо огромное! Я твоя!'
        elif obtained=="Это предмет из разграбленного рыцарского поместья.":
          game.girl 'Ага, отольются рыцарям слёзы крестьян. Грабь награбленное!'
        elif obtained=="Это предмет найден в деревянном рыцарском замке.":
          game.girl 'Ага, не только феодалам вытягивать деньги из народа. Грабь награбленное!'
        elif obtained=="Это предмет из разграбленного монастыря.":
          if game.girl.nature=='lust':
            game.girl 'Думаю, монашкам он больше не пригодится!'
          elif game.girl.nature=='proud':
            game.girl 'Да простит меня Небесный Отец...'
        elif obtained=="Это предмет из разграбленной крепости.":
          if game.girl.nature=='lust':
            game.girl 'Надеюсь, ты там хорошо поживился?'
          elif game.girl.nature=='proud':
            game.girl 'Выходит, даже крепкие стены и могучие армии не всегда могут спасти от дракона. Ты не поверишь, но это несколько... утешает.'
          elif game.girl.nature=='innocent':
            game.girl 'Я обязательно помолюсь за упокой погибших.'
        elif obtained=="Это предмет из королевской сокровищницы.":
          if game.girl.nature=='lust':
            if game.girl.type == 'peasant':
              game.girl 'Благодаря тебе даже крестьянка может поувствовать себя Королевой!'
            elif game.girl.type == 'citizen':
              game.girl 'Даже и не мечтала почувствовать себя Королевой!'
            elif game.girl.type == 'princess':
              game.girl 'Всегда мечтала почувствовать себя Королевой!'
          elif game.girl.nature=='proud':
            game.girl 'Выходит, даже королевская семья не может чувствовать себя в безопасности. Ты не поверишь, но это отчасти... примиряет меня с моей судьбой.'
          elif game.girl.nature=='innocent':
            game.girl 'И тебя не покарал Небесный Отец?'
        elif obtained=="Это предмет из сокровищницы короля-под-горой.":
          game.girl 'Заполучить вещь из легендарной сокровищницы цвергов... Спасибо огромное! Я твоя!'
        elif obtained=="Это предмет из разграбленной крепости маркиза де Ада.":
          game.girl 'Я слышала истории об этом маркизе. Я рада, что ты разорил его замок.'
        elif obtained=="Это предмет с затонувшего корабля.":
          game.girl 'И ты выловил его для меня со дна моря? Это так... романтично.'
        elif obtained=="Это предмет с разграбленного воздушного судна цвергов.":
          game.girl 'Интересно, как эти воздушные суда вообще могут летать?'
          game.dragon 'Самому интересно.'
          game.dragon 'Наверное, там замешана очень сильная физика!'
        elif obtained=="Это предмет из столичного кафедрального собора.":
          if game.girl.nature=='lust':
            game.girl 'Думаю, святошам он больше не пригодится!'
          elif game.girl.nature=='proud':
            game.girl 'Да простит меня Небесный Отец...'
        elif obtained=="Это предмет из лавки ювелира.":
          game.girl 'Думаю, этот жадюга вполне обойдётся без своих сокровищ!'
        elif obtained=="Это предмет из клада, зарытого кем-то в лесу.":
          game.girl 'Интересно, кем?'
          game.dragon 'Сам хотел бы знать...'
        elif obtained=="Это предмет из клада, спрятанного в горной расщелине.":
          game.girl 'А карта там была?!'
          game.dragon 'Не-а, искал исключительно на нюх!'
        elif obtained=="Это часть груза контрабандистов, которых дракон ограбил на тайном перевале в северных горах.":
          game.girl 'Чем меньше в Королевстве этой дряни, тем лучше!'
        elif obtained=="Часть дани, выплаченной одной из деревень.":
          if game.girl.type == 'peasant':
            game.girl 'Интересно, не моей ли?'
          else:
            game.girl 'То есть ты предлагаешь мне носить цацки деревенских "красавиц"? Ну уж нет, выбери что-нибудь другое!'
            $ game.girl.willing=False
            $ trs=[game.chronik.active_gift]
            $ game.lair.treasury.receive_treasures(trs)
            $ game.chronik.active_gift=None
            return
        elif obtained=="Это предмет из разграбленного людского поселения.":
          if game.girl.nature=='lust':
            game.girl 'Было ваше, стало наше!'
          elif game.girl.nature=='proud':
            game.girl '*С силой вырывая сокровище* Когда-нибудь ты отвветишь и за это преступление!'
          elif game.girl.nature=='innocent':
            game.girl 'Ты... ты заполучил это сокровище, принеся страдания невинным!'
            game.girl 'Ты не способен на любовь. Отпусти меня.'
            $ game.girl.willing_attemp=False
            $ game.girl.willing=False
            $ trs=[game.chronik.active_gift]
            $ game.lair.treasury.receive_treasures(trs)
            $ game.chronik.active_gift=None
          return
        elif obtained=="Этот предмет принадлежал когда-то беззвестному странствующему рыцарю.":
          game.girl 'Полагаю, что этот рыцарь так и остался беззвестным.'
        elif obtained=="Этот предмет изготовлен по заказу дракона":
          game.girl 'Ты сделал его специально для меня? Спасибо огромное!'
        else:
          game.girl 'Понятно.'
      '{i}(Соврать){/i} Да не  помню уже' if not repeat:
        if game.girl.nature=='lust':
          game.girl 'Врёшь ведь. Ладно, неважно.'
        elif game.girl.nature=='proud':
          game.girl 'Ты врёшь. Откуда у тебя этот предмет?'
          call lb_talk_obtained(repeat=True) from _call_lb_talk_obtained_2
          return
        elif game.girl.nature=='innocent':
          game.girl 'Ты... ты врёшь! Ты заполучил это сокровище, принеся страдания невинным, и теперь боишься даже в этом признаться!'
          game.girl 'Ты не способен на любовь. Отпусти меня.'
          $ game.girl.willing_attemp=False
          $ game.girl.willing=False
          $ trs=[game.chronik.active_gift]
          $ game.lair.treasury.receive_treasures(trs)
          $ game.chronik.active_gift=None
          return
    python:
      game.girl.willing=True
      game.girl.gift=game.chronik.active_gift
      game.chronik.active_gift = None
      text = u'Впрочем, пленнице повезло - если это вообще можно назвать везением. %s - прекрасный подарок, и в благодарность %s решила отдаться дракону по собственной воле. \n\n' % (treasures.capitalize_first(game.girl.gift.description()), game.girl.name)
      game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_talk_girl(repeat=False):
#    if game.chronik.active_gift.girl_id
#    '[game.chronik.active_gift.girl_id]'
#    '[game.chronik.death_reason]'
    python:
      jail=False
      free=False
      death=False
      live=False
      type_death=None
#      game.narrator(u"%s" % game.chronik.death_reason['eat'][0][1])
      for girl_i in reversed(xrange(game.girls_list.prisoners_count)):
        if game.chronik.active_gift.girl_id==game.girls_list.prisoners[girl_i].girl_id:
          jail=True
          break
      itog=jail or free or death or live
      if not itog:
        for girl_i in reversed(xrange(len(game.girls_list.free_list))):
          if game.chronik.active_gift.girl_id==game.girls_list.free_list[girl_i].girl_id:
            free=True
            break
      itog=jail or free or death or live
      if not itog:
        menu_list=sorted(game.chronik.death_reason.keys(),key=lambda i: len(game.chronik.death_reason[i]),reverse=True)
        for death_i in xrange(len(menu_list)):
          for girl_i in reversed(xrange(len(game.chronik.death_reason[menu_list[death_i]]))):
            if game.chronik.active_gift.girl_id==game.chronik.death_reason[menu_list[death_i]][girl_i][1] and game.dragon.level - 1 == game.chronik.death_reason[menu_list[death_i]][girl_i][0]:
              death=True
              type_death=menu_list[death_i]
#              game.narrator(u"%s, %s, %s" %(game.chronik.active_gift.girl_id, game.chronik.death_reason[menu_list[death_i]][girl_i][1], type_death))
              if type_death in data.death_reason_explain:
                desc_death=data.death_reason_explain[type_death][0]
              else:
                game.narrator("%s" %type_death)
                type_death=u"unknown"
                desc_death=u"Ой, а я и в самом деле не помню, отчего она погибла! Тут какая-то ошибка!"
              break
          if death:
            break
      itog=jail or free or death or live
      if not itog:
        menu_list=sorted(game.chronik.live_reason.keys(),key=lambda i: len(game.chronik.live_reason[i]),reverse=True)
        for live_i in xrange(len(menu_list)):
          for girl_i in reversed(xrange(len(game.chronik.live_reason[menu_list[live_i]]))):
            if game.chronik.active_gift.girl_id==game.chronik.live_reason[menu_list[live_i]][girl_i][1] and game.dragon.level - 1 == game.chronik.live_reason[menu_list[live_i]][girl_i][0]:
              live=True
              type_live=menu_list[live_i]
#              game.narrator(u"%s" %type_live)
              if type_live in data.live_reason_explain:
                desc_live=data.live_reason_explain[type_live][0]
              else:
                game.narrator("%s" %type_live) 
                type_live=u"unknown"
                desc_live=u"Ой, а я и в самом деле не помню, как она выжила! Тут какая-то ошибка!"
              break
          if live:
            break
    menu:
      'Да рядом с тобой в тюрьме сидит!' if jail:
        if game.girl.nature=='lust':
          game.girl 'Здорово! Надо будет перед ней покрасоваться, похвастаться...'
          game.dragon 'Очень достойное поведение!'
        elif game.girl.nature=='proud':
          game.girl 'Надо будет перед ней извиниться. Возможно, мне удастся помочь ей с побегом...'
          game.dragon 'Ну-ну!'
        elif game.girl.nature=='innocent':
          game.girl 'Но... но как же я посмотрю ей в глаза! Я же со стыда сгорю!'
          game.girl 'Пожалуйста, подари что-нибудь иное.'
          $ game.girl.willing=False
          $ trs=[game.chronik.active_gift]
          $ game.lair.treasury.receive_treasures(trs)
          $ game.chronik.active_gift=None
          return  
      'Пока на свободе, но что с ней станет - неизвестно' if free:
        if game.girl.nature=='lust':
          game.girl 'Надеюсь, ничего хорошего!'
          game.dragon 'Я тоже на это надеюсь'
        elif game.girl.nature=='proud':
          game.girl 'Надеюсь, всё у неё будет хорошо'
          game.dragon 'Ну-ну!'
        elif game.girl.nature=='innocent':
          game.girl 'Вы отпустили её на свободу? Как это благородно с вашей сстороны...'
          game.dragon 'Ага'   
      '[desc_death]' if death:
        if type_death=="unknown":
          game.girl 'Надеюсь, в следующих версиях исправят!'
          game.dragon 'Я тоже на это надеюсь.'          
        elif data.death_reason_explain[type_death][1]=='eat':  # Съел
          if game.girl.nature=='lust':  
            game.girl 'И как, вкусная была?'
            game.dragon 'Очень!'
          elif game.girl.nature=='proud':  
            game.girl '*Вырывая украшение* Когда-нибудь ты заплатишь за это преступление!'
            game.dragon 'Ага. Всенепременно.'
          elif game.girl.nature=='innocent':  
            game.girl 'Это ужасно! [game.dragon.fullname], молю вас: соблюдайте диету!'
            game.dragon '*Облизываясь* А я и соблюдаю...'
        elif data.death_reason_explain[type_death][1]=='contrabandist':  # 
          game.girl 'Какой ужас!'
          game.girl 'Мораль: никогда не связываться с контрабандистами.'
        elif data.death_reason_explain[type_death][1]=='blind_escape':  # 
          game.girl.third '[game.girl.name] испуганно ощупывает свои глаза'
          if game.girl.nature=='lust':  
            game.girl 'Ну уж нет, никуда я от тебя не уйду!'
          elif game.girl.nature=='proud':  
            game.girl 'Надеюсь, я уберусь из твоего логова до этого знаменательного момента.'
          elif game.girl.nature=='innocent':  
            game.girl 'Это ужасно! [game.dragon.fullname], пожалуйста, никогда больше так не  делайте!'
            game.dragon '*Ухмыляясь* Посмотрим, посмотрим...'
        elif data.death_reason_explain[type_death][1]=='execution':  # Съел
          if game.girl.nature=='lust':  
            game.girl 'Ужас! Варварство! Может, ты поскорее Вольных завоюешь, а?'
          elif game.girl.nature=='proud':  
            game.girl 'Сурово. Но, в какой-то степени - справедливо.'
          elif game.girl.nature=='innocent':  
            game.girl 'Ужасно... но правильно. Наверное, я не заслуживаю лучшей судьбы...'
        elif data.death_reason_explain[type_death][1]=='sultan':  # Съел
          if game.girl.nature=='lust':  
            game.girl 'Надеюсь, если я попаду в Султанат, моя судьба сложится по-иному.'
          else:  
            game.girl 'Ужас! Надеюсь, я никогда не попаду в Султанат...'
        elif data.death_reason_explain[type_death][1]=='escape':  # Съел
          if game.girl.nature=='lust':  
            game.girl 'Ужас! Ни-ку-да я от тебя не побегу, и не уговаривай!'
          elif game.girl.nature=='proud':  
            game.girl 'Значит, побег из логова надо планировать более тщательно.'
          elif game.girl.nature=='innocent':  
            game.girl 'Ужасная судьба. Значит, из логова не убежать, да?'
        elif data.death_reason_explain[type_death][1]=='lizardman':  # 
          game.girl 'Какой ужас!'
          game.girl 'И как ей только такое в голову пришло, связаться с ящериком?'
        elif data.death_reason_explain[type_death][1]=='cripple':  # 
          game.girl.third '[game.girl.name] обхватывает себя за плечи и мелко дрожит от ужаса'
          game.girl 'Как же мне повезло, что ты меня не калечишь, а подарки даришь...'
        elif data.death_reason_explain[type_death][1]=='lizardman_battle':  # 
          if game.girl.nature=='lust':  
            game.girl 'И как ей только такое в голову пришло, связаться с ящериком? Хотя...'
          elif game.girl.nature=='proud':  
            game.girl 'Достойная смерть.'
          elif game.girl.nature=='innocent':  
            game.girl 'Значит, у них была настоящая любовь, да? В таком случае и умереть не жалко...'
        elif data.death_reason_explain[type_death][1]=='knight':  # 
          if game.girl.nature=='lust':  
            game.girl 'Дурочка. Рыцари нужны совсем не для этого...'
          elif game.girl.nature=='proud':  
            game.girl 'Настоящий рыцарь должен был спасти всех пленниц!'
          elif game.girl.nature=='innocent':  
            game.girl 'Как? Ведь в балладах у рыцарей всегда всё получается!'
        elif data.death_reason_explain[type_death][1]=='love':  # 
          game.girl 'Значит, это была истинная любовь...'
        elif data.death_reason_explain[type_death][1]=='suicide':  # 
          if game.girl.nature=='lust':  
            game.girl 'Ну и дура.'
          elif game.girl.nature=='proud':  
            game.girl 'Глупо. Лучше бы она в воительницы подалась, что ли...'
          elif game.girl.nature=='innocent':  
            game.girl 'Наверное, для неё это и вправду было лучшим выходом...'
        elif data.death_reason_explain[type_death][1]=='prostitute':  # 
          if game.girl.nature=='lust':  
            game.girl 'Что же, в чём-то я её понимаю...'
          elif game.girl.nature=='proud':  
            game.girl 'Ну и дура!'
          elif game.girl.nature=='innocent':  
            game.girl 'Какой ужасный и абсурдный конец!'
        elif data.death_reason_explain[type_death][1]=='hunger':  # 
          game.girl 'Почему же она из логова не сбежала?'
          game.dragon 'Не помню уже.'
        elif data.death_reason_explain[type_death][1]=='kitchen':  # 
          game.girl.third '[game.girl.name] некоторое время молчит.'
          game.girl 'Почему-то мне кажется, что меня ждёт схожая судьба.'
        elif data.death_reason_explain[type_death][1]=='knight_beheaded':  # 
          if game.girl.nature=='innocent': 
            game.girl.third '[game.girl.name] грустнеет.'  
            game.girl 'Наверное, это и к лучшему.'
          else:  
            game.girl 'Глупо. C рыцарями нужно вести себя совершенно по другому!'
        elif data.death_reason_explain[type_death][1]=='birth':  # 
          game.girl 'Роды - это всегда опасно. Возможно, меня ждёт схожая судьба.'
        elif data.death_reason_explain[type_death][1]=='rape_death':  # 
          game.girl 'И именно пэтому ты начал дарить подарки.'
          game.girl 'Всё с тобой ясно.'
        elif data.death_reason_explain[type_death][1]=='suicide_prison':  # 
          if game.girl.nature=='lust':  
            game.girl 'Ну и дура.'
          elif game.girl.nature=='proud':  
            game.girl 'Глупо. Лучше бы попыталась сбежать!'
          elif game.girl.nature=='innocent':  
            game.girl 'Наверное, для неё это и вправду было лучшим выходом...'
        elif data.death_reason_explain[type_death][1]=='turned_apart':  # 
          if game.girl.nature=='lust':  
            game.girl 'И что же?'
            game.dragon 'Показать на ком-нибудь?'
            game.girl 'Ммм... Пока не надо.'
          elif game.girl.nature=='proud':  
            game.girl 'Да есть ли предел твоим злодеяниям?!'
          elif game.girl.nature=='innocent':  
            game.girl 'Молю тебя, не делай так больше!'
            game.dragon 'Не буду.'
            game.dragon 'По крайней мере, с той девицей...'

     # Хозяйка украшения выжила  
      '[desc_live]' if live:
        if type_live=="unknown":
          game.girl 'Надеюсь, в следующих версиях исправят!'
          game.dragon 'Я тоже на это надеюсь.' 
        elif data.live_reason_explain[type_live][1]=='marry':
          if game.girl.nature=='lust':  
            game.girl 'Какая скучная участь.'
          elif game.girl.nature=='proud':  
            game.girl 'И даже не продолжила борьбу? Что же, её право'
          elif game.girl.nature=='innocent':  
            game.girl 'Какая счастливая судьба!'
        elif data.live_reason_explain[type_live][1]=='monastery':
          if game.girl.nature=='lust':  
            game.girl 'Согласна, дура какая-то.'
          elif game.girl.nature=='proud':  
            game.girl '"С чего"?! Ещё спрашиваешь, гад?!'
          elif game.girl.nature=='innocent':  
            game.girl 'Она отмаливала свои грехи. Не знаю уж смогу ли я отмолить свои...'
        elif data.live_reason_explain[type_live][1]=='berries':
          game.girl 'Вот только не всем так повезло, да...'
        elif data.live_reason_explain[type_live][1]=='blind':
          game.girl 'Даже не знаю, завидовать или нет!'
        elif data.live_reason_explain[type_live][1]=='cripple_luck':  # 
          game.girl.third '[game.girl.name] обхватывает себя за плечи и мелко дрожит от ужаса'
          game.girl 'Конечно, ей ещё повезло, но как же хорошо, что ты меня не калечишь, а подарки даришь...'
        elif data.live_reason_explain[type_live][1]=='dark_whore':  #
          if game.girl.nature=='lust':  
            game.girl 'Так, с ящериками связываться не надо. Хотя...'
          else:  
            game.girl 'Ужасная участь! Хорошо, что мне и в мысли бы не пришло подобное извращение.'
        elif data.live_reason_explain[type_live][1]=='prostitute':  #
          if game.girl.nature=='lust':  
            game.girl 'Неплохо устроилась!'
          elif game.girl.nature=='proud':  
            game.girl 'И это вместо борьбы? Подстилка!'
          elif game.girl.nature=='innocent':  
            game.girl 'Как {i}этим{/i} можно заниматься по собственной воле?!'    
        elif data.live_reason_explain[type_live][1]=='marrige_to_knight':  #
          if game.girl.nature=='lust':  
            game.girl 'Пфф. Как в каком-то дешёвом романе!'
          elif game.girl.nature=='proud':  
            game.girl 'И рыцарь спас только одну пленницу, даже не подумав об остальных? Слабак!'
          elif game.girl.nature=='innocent':  
            game.girl 'Какая замечательная история!' 
        elif data.live_reason_explain[type_live][1]=='raped':  #
          if game.girl.nature=='lust':  
            game.girl 'И что, ей никто не посоветовал отличного лекарства от депрессии?'
          elif game.girl.nature=='proud':  
            game.girl 'Да, случившееся может подкосить самую отчаянную решимость'
          elif game.girl.nature=='innocent':  
            game.girl 'И я её очень хорошо понимаю...' 
        elif data.live_reason_explain[type_live][1]=='warrior':  #
          if game.girl.nature=='lust':  
            game.girl 'И зачем ей попусту рисковать собой?'
          elif game.girl.nature=='proud':  
            game.girl 'И это - самый достойный выход.'
          elif game.girl.nature=='innocent':  
            game.girl 'Дева-воительница? Это так романтично...' 
        elif data.live_reason_explain[type_live][1]=='giant':  #
          game.girl 'Вот уж действительно, ничего.'
        elif data.live_reason_explain[type_live][1]=='sultan':  #
          if game.girl.nature=='lust':  
            game.girl 'Что же, не самая худшая судьба.'
          else:  
            game.girl 'Понятно. Но я всё равно надеюсь, что никогда не попаду в эту далёкую и страшную страну.'
        elif data.live_reason_explain[type_live][1]=='uncle':  #
          game.girl 'Врёшь, поди? Быть такого не может!'
          game.dragon 'Честно драконье! Сам три дня в шоке был.'
        elif data.live_reason_explain[type_live][1]=='victory':  #
          game.girl 'Тебе-то? А ну-ка признавайся!'
          game.dragon 'Ни за что! Лучше я тебя съем!'
          game.girl 'Ну, как знаешь.'




      # Врунишка
      '{i}(Соврать){/i} Да не  помню уже' if not repeat:
        if game.girl.nature=='lust':
          game.girl 'Врёшь ведь. Ладно, неважно.'
        elif game.girl.nature=='proud':
          game.girl 'Ты врёшь. Что стало с той девушкой?'
          call lb_talk_girl(repeat=True) from _call_lb_talk_girl_2
          return
        elif game.girl.nature=='innocent':
          game.girl 'Ты... ты врёшь! Ты наверняка убил её, и теперь боишься даже в этом признаться!'
          game.girl 'Ты не способен на любовь. Отпусти меня.'
          $ game.girl.willing_attemp=False
          $ game.girl.willing=False
          $ trs=[game.chronik.active_gift]
          $ game.lair.treasury.receive_treasures(trs)
          $ game.chronik.active_gift=None
          return    

          
        
    return

