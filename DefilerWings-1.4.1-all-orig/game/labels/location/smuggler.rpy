# coding=utf-8
init python:
    import random
    from pythoncode import treasures
    
label lb_location_smuggler_main:
    nvl clear
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))   
    if game.witch_st1>0:
      show expression 'img/bg/special/island.jpg' as bg
      'Какой замечательный укромный островок! Прямо-таки хочется, чтобы на нём расположилось что-нибудь эдакое. Например, логово контрабандистов.'
      'К сожалению, никакого логова контрабандистов на нём пока нет.'
      return
    $ place = 'smugglers'
    show expression 'img/bg/special/smugglers.jpg' as bg
    
#    if game.dragon.energy() == 0:
#        'Даже драконам надо иногда спать. Особенно драконам!'
#        return

    # Стоимость года работы охранников
    $ guards_cost = data.lair_upgrades['smuggler_guards']['cost']
    
    menu:
        'Нанять охрану' if 'smuggler_guards' not in game.lair.upgrades and 'regular_guards' not in game.lair.upgrades:
            "Наёмные головорезы не дадут наглым ворам растащить драконье достояние. Всего за [guards_cost] фартингов в год."
            menu:
                "Заключить контракт" if guards_cost <= game.lair.treasury.wealth:
                    $ game.lair.upgrades.add('smuggler_guards', deepcopy(data.lair_upgrades['smuggler_guards']))
                    "Наёмные головорезы будут сторожить логово, пока дракон спит."
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_2 
                "Отказаться":
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_3 
        'Продать драгоценности' if len(game.lair.treasury.jewelry) > 0:
            nvl clear
            menu:
                'Самую дорогую':
                    $ item_index = game.lair.treasury.most_expensive_jewelry_index
                'Самую дешёвую' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = game.lair.treasury.cheapest_jewelry_index
                'Случайную' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = random.randint(0, len(game.lair.treasury.jewelry) - 1)
                'Продать все украшения' if len(game.lair.treasury.jewelry) > 0:
                    $ item_index = None
                'Отмена':
                    jump lb_location_smuggler_main 
            python:
                if (item_index is None):
                    description = u"Продать все украшения за %s?" % (
                        treasures.number_conjugation_rus(game.lair.treasury.all_jewelries * 75 // 100, u"фартинг"))
                else:
                    description = u"%s.\nПродать украшение за %s?" % (
                        game.lair.treasury.jewelry[item_index].description().capitalize(),
                        treasures.number_conjugation_rus(game.lair.treasury.jewelry[item_index].cost * 75 // 100, u"фартинг"))
            menu:
                "[description]"
                'Продать':
                    python:
                        if (item_index is None):
                            description = u"Все украшения проданы за %s?" % (
                                treasures.number_conjugation_rus(game.lair.treasury.all_jewelries  * 75 // 100, u"фартинг"))
                            game.lair.treasury.money += game.lair.treasury.all_jewelries  * 75 // 100
                            game.lair.treasury.jewelry = []
                        else:
                            description = u"%s.\nПродано за %s" % (
                                game.lair.treasury.jewelry[item_index].description().capitalize(),
                                treasures.number_conjugation_rus(game.lair.treasury.jewelry[item_index].cost * 75 // 100, u"фартинг"))
                            game.lair.treasury.money += game.lair.treasury.jewelry[item_index].cost * 75 // 100
                            game.lair.treasury.jewelry.pop(item_index)
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_5 
                'Оставить':
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_6 
        'Финансировать террор' if game.mobilization.level > 1:
            show expression 'img/scene/thief.jpg' as bg
            $ terror_cost = game.mobilization.level * 100
            'Войска королевства мобилизуются, и безнаказанно творить зло становится всё сложнее. Но если обеспечить местных бандитов деньгами на оружие, снаряжение и снабжение, они могут стать угрозой, которая отвлечёт солдат от патрулирования. [terror_cost] фартингов будет достаточно, чтобы обстановка в тылах накалилась, и армейские конвои снабжения начали пропадать в пути.'
            menu:
                'Отдать [terror_cost] фартингов разбойникам' if terror_cost <= game.lair.treasury.money:
                    $ game.lair.treasury.money -= terror_cost
                    $ game.mobilization.level -= 1
                    'По приказанию дракона разбойники будут поджигать продовольственные склады, отравлять колодцы и перехватывать армейские обозы. Мобилизационный потенциал королевства снижается.'
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main
                'Это того не стоит':
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_1
        'Разузнать о воре' if game.thief is not None:
            "Тут много знающих людей, и слухи ходят разные. Только наливай, и языки сами развяжутся, никто не посмотрит, что болтает с ящерицей."
            nvl clear
            menu:
                "Уготить всех пивом (10 фартингов)" if game.lair.treasury.money >= 10:
                    python:
                        game.lair.treasury.money -= 10
                        if game.thief is not None:
                            game.thief.third('[game.thief.name] \n\n' + game.thief.description())
                        else:
                            narrator("Не появился пока вор на твое злато.")
                "Слишком дорого" if game.lair.treasury.money < 10:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_7 
                "Уйти." if game.lair.treasury.money >= 10:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_8 
        'Откупиться от вора' if (game.thief is not None) and (not game.thief.is_dead) :
            $ price = game.dragon.reputation.level * 50
            $ game.thief.third("За %d фартингов мы с ребятами объясним этому корешу, что он не с той ящерицей связался, босс!" % price)
            menu:
                "Заплатить [price] фартингов" if game.lair.treasury.money >= price:
                    $ game.lair.treasury.money -= price
                    $ game.thief.retire()
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_9 
                "Слишком дорого" if game.lair.treasury.money < price:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_10 
                "Уйти." if game.lair.treasury.money >= price:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_11 
        'Разузнать о рыцаре' if game.knight is not None:
            "Тут много знающих людей, и слухи ходят разные. Только наливай, и языки сами развяжутся, никто не посмотрит, что болтает с ящерицей."
            nvl clear
            menu:
                "Уготить всех пивом (10 фартингов)" if game.lair.treasury.money >= 10:
                    python:
                        game.lair.treasury.money -= 10
                        if game.knight is not None:
                            game.knight.third('[game.knight.name] \n\n' + game.knight.description())
                        else:
                            narrator("Не появился пока рыцарь, желающий убить тебя.")
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_12 
                "Слишком дорого" if game.lair.treasury.money < 10:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_13 
                "Уйти." if game.lair.treasury.money >= 10:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_14 
        'Ограбить рыцаря' if (game.knight is not None) and (not game.knight.is_dead):
            $ price = game.knight.enchanted_equip_count * 100
            $ narrator("Ограбить славного рыцаря дело не простое, даже опасное. А если ещё и спутников его надо порешить... Всё стоит денег. %d фартингов на бочку, и он будет гол как сокол!" % price)
            nvl clear
            menu:
                "Заплатить [price] фартингов" if game.lair.treasury.money >= price:
                    $ game.lair.treasury.money -= price
                    $ game.knight.equip_basic()
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_15 
                "Слишком дорого" if game.lair.treasury.money < price:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_16 
                "Уйти." if game.lair.treasury.money >= price:
                    call lb_location_smuggler_main from _call_lb_location_smuggler_main_17 
        'Разузнать об обстановке в королевстве':
            "Тут много знающих людей, и слухи ходят разные. Даже пива никому наливать не требуется, надо только держать глаза и уши открытыми."
#            python:
#              narrator("%s" %(game.desperate) )
#            nvl clear
#            python:
#                for i in xrange(len(data.achievements_list)):
#                  narrator( data.achievements_list[i].goal)
#                  if data.achievements_list[i].goal == 'kill':
#                    for j in data.achievements_list[i].targets:
#                      narrator( j)
#                    narrator('Проверка связи')
#                    for k in data.achievements_list[i].targets_completed:
#                      narrator( k)
            if game.desperate==0:  # Отчаяние на нуле
              call lb_smuggler_bard from _call_lb_smuggler_bard_1
            else:
              menu:
                  'Послушать сказания барда':
                      call lb_smuggler_bard from _call_lb_smuggler_bard_2
                  'Пошушукаться с контрабандистом':
                      call lb_smuggler_whisper from _call_lb_smuggler_whisper  
            call lb_location_smuggler_main from _call_lb_location_smuggler_main_18
        
#        'Вызвать демона': #if game.summon.seal<=data.max_summon:
#            python:
#                game.summon.seal=data.max_summon+1
#                for i in reversed(xrange(len(game.history_mod))):
#                  if game.history_mod[i].historical_name == 'archimonde_was':
#                    del game.history_mod[i]
# Квест Хроми
        'Оглядеться вокруг' if freeplay and "archimonde" in persistent.easter_eggs and not game.historical_check('chromi_refuse') and game.girls_list.prisoners_count >=5:
            call lb_smuggler_chromi from _call_lb_smuggler_chromi
            $ game.history = historical( name='chromi_refuse',end_year=game.year+1,desc=None,image=None)
            $ game.history_mod.append(game.history)
            call lb_location_smuggler_main from _call_lb_location_smuggler_main_19
        'Уйти':
            return
            
    return

label lb_smuggler_bard: # Поёт бард
    nvl clear
    $ narrator (game.mobilization_description() + '\n\n' + game.poverty_description()+ '\n\n' + game.fear_description()+ '\n\n' + game.desperate_description())
    nvl clear
    $ narrator (game.history_description() )
    return

label lb_smuggler_whisper:   # Рассказывает контрабандист
    python: #делаем аватарку Контрабандиста для диалогового окна
        smuggler_whisper= Talker(game_ref=game)
        smuggler_whisper.avatar = get_random_image(u"img/avahuman/thief")
        smuggler_whisper.name = 'Старый контрабандист' 
    nvl clear
    "{font=fonts/PFMonumentaPro-Regular.ttf}Старый, циничный контрабандист рассказывает об обстановке в землях Вольных:{/font} \n\n"
    $ text=game.summon_description()
    smuggler_whisper.third "[text]" 
    if game.summon.seal>0:  # Если уже начали призывать демона.
      nvl clear
      $ text=game.seal_description()
      smuggler_whisper.third "[text]" 
    return

label lb_smuggler_chromi:
    '[game.dragon.name] осматривается по сторонам. Всё как обычно, ничего интересного... а это ещё кто такая?!'
    nvl clear
    hide bg 
    show expression 'img/archimonde/chromi_meet.jpg' as bg
    'В углу сидела какая-то коротышка. Она не выказывала ни малейших признаков страха и с любопытсвом рассматривала присутствующих.'
    python:
        chromi= Talker(game_ref=game)
        chromi.avatar = "img/archimonde/chromi.jpg"
        chromi.name = 'Хроми'
    game.dragon.third 'О, новое девичье мясцо! Подойду, познакомлюсь.'
    chromi 'Привет! Ты ведь дракон? Тебя же [game.dragon.name] зовут, да? А меня Хроми. Я самая простая обыкновенная гномка!'
    nvl clear
    game.dragon.third '[game.dragon.name] почувствовал, что полностью сбит с толку.'
    game.dragon.third 'К тому же - "гномка"?! Людей он знает, альвов знает, цвергов знает, но "гномы" - это вообще кто такие?!!'
    chromi 'Кстати, ты что-нибудь слышал о Князе Ада Архитоте?'
    game.dragon  'Эээ...'
    chromi 'А, неважно! Всё равно оригинал события произошёл в другой области пространственно-временного континиума.'
    chromi 'Слушай, если хочешь, я организую тебе путешествие во времени и битву с Архитотом! Тебе понравится, я уверена!'
    game.dragon 'Эээ...'
    chromi 'Ты хочешь спросить про плату? У тебя там пленницы сидят. Выпусти их, и мы в расчёте.'
    game.dragon 'Что?!!'
    chromi 'Только нормально выпусти, с доставкой до дома, а не как всегда!'
    menu:
        'Эээ...':
            game.dragon 'Эээ...'
            chromi 'Я так и знала, что ты согласишься!'
            $ game.girls_list.chromi_free_all_girls()
            python:
                game.summon.seal=data.max_summon+1
                for i in reversed(xrange(len(game.history_mod))):
                  if game.history_mod[i].historical_name == 'archimonde_was':
                    del game.history_mod[i]
            game.dragon 'А...'
            chromi 'Ты встретишь Архитота, когда проснёшься. Пока-пока, время не ждёт!'
            hide bg
            nvl clear
            show expression 'img/bg/special/smugglers.jpg' as bg
            game.dragon 'Что? Это? Было?!!'
            game.dragon 'Кажется, мне придётся собирать пленниц заново...'
        'Да я тебя саму в темницу посажу!':
            game.dragon 'Сейчас ты к ним присоединишься!'
            'Хроми вздыхает'
            if 'black' in game.dragon.heads:
              chromi 'Ну а чего ещё ждать от чёрного дракона?'
            elif 'bronze' in game.dragon.heads:
              chromi 'Казалось  бы, бронзовый дракон, а ведёт себя хуже чёрного!'
            elif 'blue' in game.dragon.heads:
              chromi 'Это слишком даже для синих драконов!'  
            elif 'red' in game.dragon.heads:
              chromi 'Уж от кого-кого, а от красного я такого не ожидала!'
            elif 'green' in game.dragon.heads:
              chromi 'Видимо, не всё зелёные сонливы и мечтательны'
            else:
              chromi 'В худших традициях чёрных драконов.'
            hide bg
            nvl clear
            show expression 'img/bg/special/smugglers.jpg' as bg
            game.dragon 'А? Где? Что? С кем это я сейчас говорил?'
            game.dragon 'Показалось, наверное'
    return

    