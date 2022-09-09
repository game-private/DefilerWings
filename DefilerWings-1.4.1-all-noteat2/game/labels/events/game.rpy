# coding=utf-8
init python:
    from pythoncode.utils import get_random_image
    
label lb_event_mobilization_increase:
    show screen controls_overwrite
    show expression get_random_image("img/scene/mobilization") as bg
    nvl clear
    "Правители вольных народов обеспокоены бесчинством дракона. Они мобилизуют войска и усиливают охрану в своих владениях."
    return

label lb_event_poverty_increase:
    show screen controls_overwrite
    show expression get_random_image("img/scene/poverty") as bg
    nvl clear
    "Деяния дракона привели к росту бедности и разрухи в стране. Люди голодают, многие остались без крова и средств к существованию. Мобилизационный потенциал уменьшается."
    return
label lb_event_no_thief:
    show screen controls_overwrite
    $ place = game.lair.type_name
    hide bg
    show place as bg
    "Ни один вор не позарился пока на сокровища, которые собрал у себя в логове [game.dragon.fullname]."
    return

label lb_event_no_knight:
    show screen controls_overwrite
    $ place = game.lair.type_name
    hide bg
    show place as bg
    "Во всём королевстве не нашлось героя, желающего бросить вызов дракону. Видимо, [game.dragon.fullname] просто не успел ещё прославиться."
    return

label lb_event_sleep_start:
    show screen controls_overwrite
    '[game.dragon.fullname] засыпает, устав от нечестивых дел. Его сон продлится долго...'
    nvl clear
    return

label lb_event_sleep_new_year:
    show screen controls_overwrite
    if game.historical_check('rebel_daughter'):
      nvl clear
#      hide bg
      $ current_image=get_random_image("img/scene/poverty")
      show expression current_image as bg
      $ game.chronik.write_chronik(u'\n\n',game.dragon.level,game.rebel_id)
      $ text=u'Расправа, учинённая королём Сылтаном над семейством герцога де Пруа, сотрясла Королевство. Со всех концов страны дворяне стекались под стяги %s, дочери герцога Робертина, которая, по слухам, носила под сердцем ребёнка самого короля. Когда же на сторону восставших перешла  королевская племянница Марианна, стало казаться, что победа неизбежна.\n\nНо лютая жестокость "бешеных фурий" оттолкнула от повстанцев многих, очень многих. Мятежники были разбиты, остатки их войск укрылись на недавно отстроенном "острове контрабандистов". Судьба %s и Марианны так и осталась неизвестной.' %(game.rebel_girl.name, game.rebel_girl.name)
      game.rebel_girl.third '[text]'
      $ game.chronik.write_chronik(text,game.dragon.level,game.rebel_id)
      $ game.chronik.live('rebel',current_image)
      $ game.poverty.value +=3
    if game.historical_check('rebel_mother'):
      nvl clear
#      hide bg
      $ current_image=get_random_image("img/scene/poverty")
      show expression current_image as bg
      $ text=u'Казнь герцога Робертина де Пруа, героя войны с Тёмной Госпожой, возмутила очень многих. Со всех концов страны дворяне стекались под стяги Изольды, вдовы герцога де Пруа. Когда же на сторону восставших перешла королевская племянница Марианна, стало казаться, что победа неизбежна.\n\nВпрочем, именно это и привело к поражению повстанцев. Марианна обвиняла Изольду в излишней мягкости, Изольда Марианну - в неоправданной жестокости. Из-за конфликта двух лидеров мятежники потерпели поражение. Марианну захватили в плен и казнили, живьём содрав кожу. Остатки войск укрылись на недавно отстроенном "острове контрабандистов". По слухам, семейство де Пруа поселилось там же. ' 
      game.rebel_girl.third '[text]'
      $ game.poverty.value +=1
    if game.historical_check('rebel_niece'):
      nvl clear
#      hide bg
      $ current_image=get_random_image("img/scene/poverty")
      show expression current_image as bg
      $ game.chronik.write_chronik(u'\n\n',game.dragon.level,game.rebel_id)
      $ text=u'Благодаря своей популярности Марианна быстро собрала костяк армии. Со всех концов страны дворяне стекались под её стяги. Тот факт, что Марианна, по слухам, носила под сердцем ребёнка самого короля, только прибавлял ей популярности. В какой-то момент стало казаться, что победа мятежников неизбежна.\n\nНо лютая жестокость "белокурой фурии" оттолкнула от повстанцев многих, очень многих. Мятежники были разбиты, остатки их войск укрылись на недавно отстроенном "острове контрабандистов". Судьба Марианны так и осталась неизвестной.' 
      game.rebel_girl.third '[text]'
      $ game.chronik.write_chronik(text,game.dragon.level,game.rebel_id)
      $ game.chronik.live('rebel',current_image)
      $ game.poverty.value +=2
    return

label lb_event_sleep_end:
    show screen controls_overwrite
    nvl clear
    $ place = game.lair.type_name
    hide bg
    show place as bg
    'Полный сил и коварной злобы, [game.dragon.fullname] просыпается в своём логове. Время для грабежа и насилия!'
    if game.witch_st1 == 1:
      game.dragon 'Интересно, что за задание имела в виду ведьма с болот? Надо бы проверить!'
    return

label lb_historical_image:    # Показ изображения
    hide bg
    show expression game.historical_image as bg
    nvl clear
    '[game.historical_desc]'
    return

label lb_death_list:
    nvl clear
    $ pair=random.choice(game.chronik.death_reason[game.chronik.active_death])
#    '[pair]'
#    $ text= u"%s" % game.chronik.chronik_image[pair[0]][pair[1]] 
#    '[text]'
    hide bg
    show expression game.chronik.chronik_image[pair[0]][pair[1]] as bg
    $ desc='{font=fonts/AnticvarShadow.ttf}{size=+10}%s \n\n{/size}{/font}' % data.death_reason_desc[game.chronik.active_death]
    python:
        for i in xrange(len(game.chronik.death_reason[game.chronik.active_death])):
          d=game.chronik.death_reason[game.chronik.active_death][i][0]
#          game.narrator("%s" %d) 
          g=game.chronik.death_reason[game.chronik.active_death][i][1]
          desc+='%s, %s, %s (%s - %s) \n' %(game.chronik.chronik_girl_name[d][g], game.chronik.chronik_girl_desc[d][g], game.chronik.chronik_girl_nature[d][g], game.chronik.birth_date[d][g], game.chronik.death_date[d][g])
    '[desc]'
    call screen death_menu
    return

label lb_live_list:
    nvl clear
    $ pair=random.choice(game.chronik.live_reason[game.chronik.active_live])
#    '[pair]'
    hide bg
    show expression game.chronik.chronik_image[pair[0]][pair[1]] as bg
    $ desc='{font=fonts/AnticvarShadow.ttf}{size=+10}%s \n\n{/size}{/font}' % data.live_reason_desc[game.chronik.active_live]
    python:
        for i in xrange(len(game.chronik.live_reason[game.chronik.active_live])):
          d=game.chronik.live_reason[game.chronik.active_live][i][0]
#          game.narrator("%s" %d) 
          g=game.chronik.live_reason[game.chronik.active_live][i][1]
          desc+='%s, %s, %s (%s - %s) \n' %(game.chronik.chronik_girl_name[d][g], game.chronik.chronik_girl_desc[d][g], game.chronik.chronik_girl_nature[d][g], game.chronik.birth_date[d][g], game.chronik.death_date[d][g])
    '[desc]'
    call screen live_menu
    return

label lb_meat_golem:
    hide bg
    game.dragon 'Хм. Элитных охранников со стороны брать не будем, воспитаем в своём коллективе.'
    return

label lb_lair_without_guards:
    show screen controls_overwrite
    game.dragon.third 'Не располагая надёжными охранниками, способными провести пленниц в новое логово, [game.dragon.name] вынужден выпустить их на свободу!'    
    return

label lb_lair_guards_disappear:
    show screen controls_overwrite
    nvl clear
    if "gremlin_servant" in game.lair.upgrades:
      'Гремлины считают контракт выполненным и уходят'
    if "servant" in game.lair.upgrades:
      'Испугавшись тягот долгого пути, драконьи слуги разбегаются кто куда!' 
      $ game.poverty.value += 1  
    if "smuggler_guards" in game.lair.upgrades:
      'Контрабандисты считают контракт выполненным и уходят'
    if "regular_guards" in game.lair.upgrades:
      if len(game.girls_list.prisoners)>0:
        'Выслушав приказ дракона, стражи конвоируют пленниц в новое логово, а потом дисциплинированно отправляются чинить разбой и насилие.'
      else:
        'Выслушав приказ дракона, стражи дисциплинированно отправляются чинить разбой и насилие.'
      $ game.poverty.value += 1  
    if "poison_guards" in game.lair.upgrades:
      'Получив свободу, ядовитые стражи радостно расползаются по землям Вольных'
      $ game.poverty.value += 1  
    if "elite_guards" in game.lair.upgrades:
      if len(game.girls_list.prisoners)>0:
        'Выслушав приказ дракона, элитный страж конвоирует пленниц в новое логово, а потом дисциплинированно отправляется чинить разбой и насилие.'
      else:
        'Выслушав приказ дракона, элитный страж дисциплинированно отправляется чинить разбой и насилие.'
      $ game.poverty.value += 1  
    return


