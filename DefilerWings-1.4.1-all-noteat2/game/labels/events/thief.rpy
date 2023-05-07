# coding=utf-8
label lb_event_thief_spawn(thief):
    show screen controls_overwrite
    show expression "img/scene/thief.jpg" as bg
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    "[thief.title] по имени [game.thief.name] хочет порыться в сокровищнице дракона"
    # nvl clear
    thief "Сокровища станут моими!"
    return

label lb_event_thief_steal_items(thief, items):
    show screen controls_overwrite
    $ descriptions = "\n".join(game.lair.treasury.treasures_description(items))
    show expression "img/scene/loot.jpg" as bg
    nvl clear
    "[game.thief.name] выкрал из сокровищницы: [descriptions]"
    thief "Вот это дело! Еле живым ушел. Зато теперь я могу жить в роскоши как король до конца дней своих!"
    nvl clear
    return

label lb_event_thief_lair_unreachable(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    thief "Чёртов [game.dragon.kind] не мог выбрать себе логово в более доступном месте? Как туда добраться-то? Вот же гадство!"
    return

label lb_event_thief_prepare(thief):
    show screen controls_overwrite
    # nvl clear    
    # thief "Если я хочу уйти из дракньей берлоги живым и богатым, мне лучше как следует подготовиться к Делу."
    return

label lb_event_thief_prepare_usefull(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    thief "Хе-хе... точно по плану!."
    return

label lb_event_thief_receive_item(thief, item):
    show screen controls_overwrite
    show expression "img/scene/quest_thief.jpg" as bg
    nvl clear
    if item.cursed:
      "[game.thief.name] по дешёвке прикупает на чёрном рынке: [item.name]"
      thief "Это мне пригодится!"
    else:
      if item.name=="План ограбления":
        "В придорожном трактире [game.thief.name] разговорился со цвергом, везущим караван с товаром в Султанат. Угостив коротышку пивом, вор полюбопытствовал насчёт логова дракона. Благодушный цверг дал ряд дельных замечаний, на основе которых [game.thief.name] составил толковый план ограбления. "
        thief "Выгодное вложение нескольких фартингов!"
      elif item.name=="Схема тайных проходов":
        "[game.thief.name] пробрался в деревню гремлинов и соблазнил дочь старосты. Очарованная мострица набросала ему схему тайных проходов, ведущих к логову дракона."      
        thief "Ради сокровищ приходится идти на {i}такие{/i} жертвы..."
      elif item.name=="Сонный порошок":
        "По заданию ведьмы [game.thief.name] совратил девицу благородных кровей и получил в награду сонный порошок, гарантированно усыпляющий дракона."      
        thief "Очень приятное задание, побольше бы таких!"
      elif item.name=="Бездонный мешок":
        "[game.thief.name] обещал принести ведьме чешуйку дракона и в качестве задатка получил бездонный мешок."      
        thief "Опасная задача, но и награда того стоит!"
      elif item.name=="Антидот":
        "[game.thief.name] попытался ограбить столичное посольство альвов, но попал в магическую ловушку. Правда, лесная дева пожалела беднягу и отпустила его с миром. На прощание альва расспросила вора о его целях, восхитилась его смелостью и подарила ему универсальное противоядие. "      
        thief "Какая милая девушка... как бы её отблагодарить?"
      elif item.name=="Зачарованный кинжал":
        "[game.thief.name] попытался ограбить столичное посольство цвергов. Из-за невовремя сработавшей сигналиции ему пришлось в спешке уносить ноги, но единственная захваченная им  вещь - кинжал - явно обладала какими-то волшебными свойствами."      
        thief "Жаль, что не удалось пошурудить там как следует, тогда бы, авось, и дракона грабить бы не пришлось!"
      elif item.name=="Кольцо Невидимости":
        "[game.thief.name] играл в загадки с каким-то подземным монстриком и (почти честно) выиграл Кольцо Невидимости."      
        thief "И пусть он ищет себе на здоровье этого Сумкинса... а колечко я никому не отдам! Моя прелесссть..."
      elif item.name=="Летучие сандалии":
        "[game.thief.name] ограбил резиденцию прелата. Увы, оказалось, что высшие церковные иерархи живут весьма скромно! Правда, один предмет гардероба явно обладал немалой ценностью."      
        thief "С помощью крылатых сандалий я заберусь куда угодно! Ну, почти."
      elif item.name=="Охлаждающий пояс":
        "[game.thief.name] попытался ограбить столичное посольство Ифритистана. Далеко проникнуть не удалось (слишком горячо), но пояс, предназначенный для гостей живописной и слегка жарковатой страны, стащить получилось."      
        thief "Вот только в бане этот пояс лучше снимать!"    
      elif item.name=="Согревающие перчатки":
        "[game.thief.name] попытался ограбить столичное посольство Йотунхейма. Далеко проникнуть не удалось (слишком холодно), но перчатки, предназначенные для гостей живописной и слегка прохладной страны, стащить получилось."      
        thief "Я теперь смогу зимой на снегу спать!" 
      elif item.name=="Амулет подводного дыхания":
        "[game.thief.name] попытался ограбить столичное посольство морского народа. Далеко проникнуть не удалось (слишком глубоко), но амулет, предназначенный для гостей подводной бездны, стащить получилось."      
        thief "Надо будет поближе познакомиться с какой-нибудь русалочкой!"  
    nvl clear
    return

label lb_event_thief_prepare_useless(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    show expression "img/scene/quest_thief.jpg" as bg
    thief "Ведьма задания невыполнимые даёт, во всех посольствах замки с засовами в три ряда, на чёрном рынке цены грабительские... ну как тут честному вору в делу-то готовиться, а?"
    return

label lb_event_thief_find_useless(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    show expression "img/scene/quest_thief.jpg" as bg
    '[game.thief.name] хочет найти логово дракона, но безуспешно.'
    thief "Да где же прячется эта змеюка... Чёрт!"
    return

label lb_event_thief_find_useless(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    show expression "img/scene/quest_thief.jpg" as bg
    '[game.thief.name] хочет найти логово дракона, но безуспешно.'
    thief "Да где же прячется эта змеюка... Чёрт!"
    return

label lb_event_thief_no_dragon(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    show expression "img/scene/quest_thief.jpg" as bg
    'Явивишись в хорошо знакомое место, [game.thief.name] видит, что больше там нет охраны. Равно как и дракона. Равно как и сокровищ. '
    thief "Так что, мне теперь заново логово искать, что ли?!"
    return

label lb_event_thief_alpinism_death(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    $ place = game.lair.type_name
    show place as bg
    thief "И высота для меня - не помеха, с моими летучими сандалиями..."
    thief "O-оу. Как-то подозрительно быстро они теряют перьяааа!!!"
    'Последний крик вора ещё долго висел между небом и землёй.'
    return

label lb_event_thief_warming_death(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    $ place = game.lair.type_name
    show place as bg
    thief "Как хорошо, что я прикупил согревающие перчатки! Теперь среди снега и льда мне совершенно не холодно!"
    thief "И даже жарко. Даже очень жаркоооо!!!"
    'Хорошо порпечённый труп вора обитателям драконьего логова пришёлся по вкусу.'
    return

label lb_event_thief_cooling_death(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    $ place = game.lair.type_name
    show place as bg
    thief "Как хорошо, что я прикупил охлаждающий пояс! Теперь среди вулканов и лавы мне совершенно не жарко!"
    thief "И даже холодно. Бррр! Присяду в уголке, авось согреюсь."
    'Статуя из нетающего льда стала прекрасным украшением драконьего логова.'
    return

label lb_event_thief_swiming_death(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    $ place = game.lair.type_name
    show place as bg
    thief "Как хорошо, что я прикупил амулет подводного дыхания! А то было бы сплошное 'Буль-буль!'"
    thief "Буль-буль!"
    'Тело незадачливого вора навсегда упокоилось в морской пучине'
    return

label lb_event_thief_lair_enter(thief):
    show screen controls_overwrite
    nvl clear
    show expression "img/scene/thief_in_lair.jpg" as bg
    thief "Ну вот и оно - логово дракона. Я войду словно тень и выскользну обратно с мешком сокровищ, тяжким как мои грехи..."
    # $ game.pauseForSkip()
    return

label lb_event_thief_die_inaccessability(thief):
    show screen controls_overwrite
#    "[thief.title] [game.thief.name] не смог даже забраться в логово - укрепления слишком надёжные."
#    thief 'Проклятый [game.dragon.kind] окопался лучше, чем король цвергов - стены, рвы, ставни, решётки и запоры... я не вижу ни единой лазейки. Видать, такое дело мне не по зубам.'
    "[thief.title] [game.thief.name] благополучно заблудился в лабиринте пещер, комнат и коридоров, окружавших логово дракона."
    $ txt = game.interpolate(random.choice(txt_thief_lost))
    thief '[txt]'
    'Лишь после недели бесплодных блужданий вор выбрался из лабиринта. После такого потрясения [game.thief.name] навсегда завязал с воровским ремеслом, начал законопослушную жизнь и со временем стал знаменитым цветоводом.'
    'За его цветами приезжали даже из Султаната!'
    return

label lb_event_thief_die_trap(thief, trap,method):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear    
    show expression "img/scene/thief_in_lair.jpg" as bg 
    $ txt = game.interpolate(data.lair_upgrades[trap].fail[method])
    '[txt]' 
    
    $ game.pauseForSkip()

    return

label lb_event_thief_pass_trap(thief, trap,method):
    show screen controls_overwrite
    show expression "img/scene/thief_in_lair.jpg" as bg
    $ txt = game.interpolate(data.lair_upgrades[trap].success[method])
    '[txt]' 
    return

label lb_event_thief_receive_no_item(thief):
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear    
    show expression "img/scene/thief_in_lair.jpg" as bg    
    "Вор ничего не получил"
    return

# @Review: Alex: Added a bunch of new events to fill in the gaps:
label lb_event_thief_checking_accessability(thief):
    # Checking if thief can get past layer defences:
    # Debug message: thief(u"Проверяю неприступность")
    return
    
label lb_event_thief_checking_accessability_success(thief):
    # Thief can gain access:
    # Debug message: thief(u"I can get into the Layer!")
    return
    
label lb_event_thief_trying_to_avoid_traps_and_guards(thief):
    # Thief is trying to avoid traps and guards:
    # Debug message: thief(u"Пробую обойти ловушки и стражей")
    return
    
label lb_event_thief_retreat_and_try_next_year(thief):
    show screen controls_overwrite
    thief "Пока что тут для меня крутовато... Надо подготовиться получше. Но я не сдамся!"
    return

label lb_event_thief_total_retreat(thief):
    show screen controls_overwrite
    thief "Похоже, даже увешавшись магическими цацками с ног до головы, в сокровищницу я не проберусь. Придётся бросить это гиблое дело. Жаль, столько лет дракону под хвост!"
    return
    
label lb_event_thief_starting_to_rob_the_lair(thief):
    show screen controls_overwrite
    show expression "img/scene/loot.jpg" as bg    
    thief "Ух ты! Вот она, сокровищница. И [game.dragon.kind], зараза, прямо на золоте лежит... Ничего, я аккуратненько... надо только выбрать вещи поценнее."
    return

label lb_event_thief_took_an_item_trickster(thief, item):
    show screen controls_overwrite
    show expression "img/scene/loot.jpg" as bg   
    thief "Повезло, что я такой ловкий. Так, ещё немного..."
    call lb_event_thief_took_an_item(thief, item) from _call_lb_event_thief_took_an_item_1
    return

label lb_event_thief_took_an_item_dust(thief, item):
    show screen controls_overwrite
    show expression "img/scene/loot.jpg" as bg   
    thief "Так, распылить ещё немного сонного порошочка - и можно безнаказанно обчищть логово."
    call lb_event_thief_took_an_item(thief, item) from _call_lb_event_thief_took_an_item_2
    return

label lb_event_thief_wrong_dust(thief, item):
    show screen controls_overwrite
    show expression "img/scene/loot.jpg" as bg   
    thief "Так, распылить ещё немного сонного порошочка - и можно безнаказанно обчищать логово."
    hide bg
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    show expression "img/scene/wokeup.jpg" as bg  
    'Едкая смесь попадает дракону прямо в ноздри, и [game.drgon.fullname] оглушительно чихает!'
    return

label lb_event_thief_took_an_item_luck(thief, item):
    show screen controls_overwrite
    show expression "img/scene/loot.jpg" as bg   
    thief "Может, хватит искушать судьбу? Нет, нет, мне повезёт, ещё вот это прихвачу..."
    call lb_event_thief_took_an_item(thief, item) from _call_lb_event_thief_took_an_item_3
    return

label lb_event_thief_took_an_item_unluck(thief, item):
    show screen controls_overwrite
    show expression "img/scene/loot.jpg" as bg   
    thief "Может, хватит искушать судьбу? Нет, нет, мне повезёт, ещё вот это прихвачу..."
    hide bg
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    show expression "img/scene/wokeup.jpg" as bg  
    "Зазевашийся вор обрушивает кучку монет, которые со звоном раскатываются по полу."

    $ game.pauseForSkip()
    
    return

label lb_event_thief_took_an_item(thief, item):
    show screen controls_overwrite
    # Got an item!
    # Debug message: thief(u"Взял шмотку %s" % stolen_items[i]) 
    $ desc = item.description()
    "[game.thief.name] аккуратно вытягивает из под брюха спящего дракона понравившийся предмет: [desc]" 
    return
    
label lb_event_thief_lair_empty(thief):
    # There were no treasures in the lair:
    # Debug message: thief(u"В сокровищнице нечего брать. Сваливаю.")
    show expression "img/scene/thief_in_lair.jpg" as bg        
    thief "Тут больше нечем поживиться... проклятье, я думал драконы куда богаче. Надо сваливать!"
    return
    
label lb_event_thief_awakened_dragon(thief, stolen_items):
    # Thief awakens the dragon and gets killed... stolen_items: items that dragon takes back from the thief.
    # Debug message: thief(u"Разбудил дракона")
    show expression "img/scene/wokeup.jpg" as bg    
    thief "Упс..."
    game.dragon "Так-так... какая встреча. А я-то думал, кто тут шебуршится."
    nvl clear
    "[game.dragon.fullname] раздирает неудачливого расхитителя сокровищ в клочья и, перекусив, снова ложится спать."

    $ game.pauseForSkip()

    return