init:
    python:
        import random


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
    ### thief
    "[thief.title] [game.thief.name]: Чёртов [game.dragon.kind] не мог выбрать себе логово в более доступном месте? Как туда добраться-то? Вот же гадство!"
    return

label lb_event_thief_prepare(thief):
    show screen controls_overwrite
    # nvl clear    
    # thief
    "[thief.title] [game.thief.name]: Если я хочу уйти из дракньей берлоги живым и богатым, мне лучше как следует подготовиться к Делу."
    return

label lb_event_thief_prepare_usefull(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    ### thief
    "[thief.title] [game.thief.name]: Хе-хе... точно по плану!."
    return

label lb_event_thief_receive_item(thief, item):
    show screen controls_overwrite
    show expression "img/scene/quest_thief.jpg" as bg
    ### nvl clear
    if item.cursed:
      "{color=#00FF00}[game.thief.name] по дешёвке прикупает на чёрном рынке: [item.name]{/color}"
      thief "Это мне пригодится!"
    else:
      if item.name=="План ограбления":
        "{color=#FFFF00}В придорожном трактире [game.thief.name] разговорился со цвергом, везущим караван с товаром в Султанат. Угостив коротышку пивом, вор полюбопытствовал насчёт логова дракона. Благодушный цверг дал ряд дельных замечаний, на основе которых [game.thief.name] составил толковый план ограбления.{/color}"
        thief "Выгодное вложение нескольких фартингов!"
      elif item.name=="Схема тайных проходов":
        "{color=#FFFF00}[game.thief.name] пробрался в деревню гремлинов и соблазнил дочь старосты. Очарованная мострица набросала ему схему тайных проходов, ведущих к логову дракона.{/color}"      
        thief "Ради сокровищ приходится идти на {i}такие{/i} жертвы..."
      elif item.name=="Сонный порошок":
        "{color=#FFFF00}По заданию ведьмы [game.thief.name] совратил девицу благородных кровей и получил в награду сонный порошок, гарантированно усыпляющий дракона.{/color}"      
        thief "Очень приятное задание, побольше бы таких!"
      elif item.name=="Бездонный мешок":
        "{color=#FFFF00}[game.thief.name] обещал принести ведьме чешуйку дракона и в качестве задатка получил бездонный мешок.{/color}"      
        thief "Опасная задача, но и награда того стоит!"
      elif item.name=="Антидот":
        "{color=#FFFF00}[game.thief.name] попытался ограбить столичное посольство альвов, но попал в магическую ловушку. Правда, лесная дева пожалела беднягу и отпустила его с миром. На прощание альва расспросила вора о его целях, восхитилась его смелостью и подарила ему универсальное противоядие.{/color}"      
        thief "Какая милая девушка... как бы её отблагодарить?"
      elif item.name=="Зачарованный кинжал":
        "{color=#FFFF00}[game.thief.name] попытался ограбить столичное посольство цвергов. Из-за невовремя сработавшей сигналиции ему пришлось в спешке уносить ноги, но единственная захваченная им  вещь - кинжал - явно обладала какими-то волшебными свойствами.{/color}"      
        thief "Жаль, что не удалось пошурудить там как следует, тогда бы, авось, и дракона грабить бы не пришлось!"
      elif item.name=="Кольцо Невидимости":
        "{color=#FFFF00}[game.thief.name] играл в загадки с каким-то подземным монстриком и (почти честно) выиграл Кольцо Невидимости.{/color}"      
        thief "И пусть он ищет себе на здоровье этого Сумкинса... а колечко я никому не отдам! Моя прелесссть..."
      elif item.name=="Летучие сандалии":
        "{color=#FFFF00}[game.thief.name] ограбил резиденцию прелата. Увы, оказалось, что высшие церковные иерархи живут весьма скромно! Правда, один предмет гардероба явно обладал немалой ценностью.{/color}"      
        thief "С помощью крылатых сандалий я заберусь куда угодно! Ну, почти."
      elif item.name=="Охлаждающий пояс":
        "{color=#FFFF00}[game.thief.name] попытался ограбить столичное посольство Ифритистана. Далеко проникнуть не удалось (слишком горячо), но пояс, предназначенный для гостей живописной и слегка жарковатой страны, стащить получилось.{/color}"      
        thief "Вот только в бане этот пояс лучше снимать!"    
      elif item.name=="Согревающие перчатки":
        "{color=#FFFF00}[game.thief.name] попытался ограбить столичное посольство Йотунхейма. Далеко проникнуть не удалось (слишком холодно), но перчатки, предназначенные для гостей живописной и слегка прохладной страны, стащить получилось.{/color}"      
        thief "Я теперь смогу зимой на снегу спать!" 
      elif item.name=="Амулет подводного дыхания":
        "{color=#FFFF00}[game.thief.name] попытался ограбить столичное посольство морского народа. Далеко проникнуть не удалось (слишком глубоко), но амулет, предназначенный для гостей подводной бездны, стащить получилось.{/color}"      
        thief "Надо будет поближе познакомиться с какой-нибудь русалочкой!"  
    ### nvl clear
    return

label lb_event_thief_prepare_useless(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    show expression "img/scene/quest_thief.jpg" as bg
    ### thief
    "[thief.title] [game.thief.name]: Ведьма задания невыполнимые даёт, во всех посольствах замки с засовами в три ряда, на чёрном рынке цены грабительские... ну как тут честному вору в делу-то готовиться, а?"
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
    ### thief
    "[thief.title] [game.thief.name]: И высота для меня - не помеха, с моими летучими сандалиями..."
    ### thief
    "[thief.title] [game.thief.name]: O-оу. Как-то подозрительно быстро они теряют перьяааа!!!"
    'Последний крик вора ещё долго висел между небом и землёй.'
    return

label lb_event_thief_warming_death(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    $ place = game.lair.type_name
    show place as bg
    ### thief
    "[thief.title] [game.thief.name]: Как хорошо, что я прикупил согревающие перчатки! Теперь среди снега и льда мне совершенно не холодно!"
    ### thief
    "[thief.title] [game.thief.name]: И даже жарко. Даже очень жаркоооо!!!"
    'Хорошо порпечённый труп вора обитателям драконьего логова пришёлся по вкусу.'
    return

label lb_event_thief_cooling_death(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    $ place = game.lair.type_name
    show place as bg
    ### thief
    "[thief.title] [game.thief.name]: Как хорошо, что я прикупил охлаждающий пояс! Теперь среди вулканов и лавы мне совершенно не жарко!"
    ### thief
    "[thief.title] [game.thief.name]: И даже холодно. Бррр! Присяду в уголке, авось согреюсь."
    'Статуя из нетающего льда стала прекрасным украшением драконьего логова.'
    return

label lb_event_thief_swiming_death(thief):
    show screen controls_overwrite
    # @fdsc Убрал очистку, чтобы не было необходимости постоянно кликать
    # nvl clear
    $ place = game.lair.type_name
    show place as bg
    ### thief 
    "[thief.title] [game.thief.name]: Как хорошо, что я прикупил амулет подводного дыхания! А то было бы сплошное 'Буль-буль!'"
    ### thief
    "[thief.title] [game.thief.name]: Буль-буль!"
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

    python:
        magic_traps  = 0
        inaccByGirls = False

        if 'magic_traps3' in game.lair.upgrades:
            magic_traps = 1
        if 'magic_traps4' in game.lair.upgrades:
            magic_traps = 2

        if random.randint(1, game.lair.inaccessability) <= game.lair.inaccByGirls:
            inaccByGirls = True

    "[thief.title] [game.thief.name] не смог даже забраться в логово - укрепления слишком надёжные."
    ### thief 
    if inaccByGirls:
        '[thief.title] [game.thief.name]: Что это? Почему здесь ходят голые девушки? Красивая! Подойду поближе.'
        '[thief.title] [game.thief.name]: Куда я зашёл? А?'
        '[thief.title] [game.thief.name]: Что она говорит?'
        '[thief.title] [game.thief.name]: Куда она делась? Прошла сквозь стену?'
        '[thief.title] [game.thief.name]: Чёрт! В смысле - дракон! Я заблудился!'
    elif magic_traps == 0:
        '[thief.title] [game.thief.name]: Проклятый [game.dragon.kind] окопался лучше, чем король цвергов - стены, рвы, ставни, решётки и запоры... я не вижу ни единой лазейки. Видать, такое дело мне не по зубам.'
        "[thief.title] [game.thief.name] благополучно заблудился в лабиринте пещер, комнат и коридоров, окружавших логово дракона."
    elif magic_traps == 1:
        "[thief.title] [game.thief.name] благополучно заблудился в магических зеркалах, мерцаниях и открытых дверях, переносящих вора совершенно в другие места."
    elif magic_traps == 2:
        "[thief.title] [game.thief.name] был подхвачен магическими потоками и, как ни старался из них выбраться, - ничего не получалось. Да и куда выбираться, когда вместо коридора с потолком и полом тебя несёт по какой-то цветной трубе, где ты барахтаешься как муха в воде, не зная, где верх, где низ?"

    $ txt = game.interpolate(random.choice(txt_thief_lost))
    thief '[txt]'
    $ ch = random.randint(0, 1)
    if ch == 0:
        'Лишь после недели бесплодных блужданий вор выбрался из лабиринта. После такого потрясения [game.thief.name] навсегда завязал с воровским ремеслом, начал законопослушную жизнь и со временем стал знаменитым цветоводом.'
        'За его цветами приезжали даже из Султаната!'
    else:
        # @fdsc Разнообразим
        'Лишь после недели бесплодных блужданий вор выбрался из лабиринта. После такого потрясения [game.thief.name] навсегда завязал с воровским ремеслом и стал выращивать виноград'

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
    ### thief 
    "[thief.title] [game.thief.name]: Пока что тут для меня крутовато... Надо подготовиться получше. Но я не сдамся!"
    return

label lb_event_thief_total_retreat(thief):
    show screen controls_overwrite
    ### thief 
    "[thief.title] [game.thief.name]: Похоже, даже увешавшись магическими цацками с ног до головы, в сокровищницу я не проберусь. Придётся бросить это гиблое дело. Жаль, столько лет дракону под хвост!"
    return
    
label lb_event_thief_starting_to_rob_the_lair(thief):
    show screen controls_overwrite
    show expression "img/scene/loot.jpg" as bg    
    ### thief
    "[thief.title] [game.thief.name]: Ух ты! Вот она, сокровищница. И [game.dragon.kind], зараза, прямо на золоте лежит... Ничего, я аккуратненько... надо только выбрать вещи поценнее."
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
    "{color=#FF0000}[game.thief.name] аккуратно вытягивает из под брюха спящего дракона понравившийся предмет: [desc]{/color}" 
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
    "{color=#00FF00}[game.dragon.fullname] раздирает неудачливого расхитителя сокровищ в клочья и, перекусив, снова ложится спать.{/color}"

    $ game.pauseForSkip()

    return