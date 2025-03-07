# coding=utf-8

init python:
    import random
    
    from pythoncode import utils
    
label lb_location_lair_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))
        if game.chronik.tot_dead==0:
          ratio_desc=''
        else:
          ratio=100.*game.chronik.tot_dead/game.chronik.tot_girl_id
          if ratio>99.:
            ratio_desc='(умерло: {color=#00ff00}%.1f %%{/color})' %ratio
          elif ratio>90. and ratio<=99.:
            ratio_desc='(умерло: {color=#ccccff}%.1f %%{/color})' %ratio
          elif ratio>60. and ratio<=90.:
            ratio_desc='(умерло: {color=#0085FF}%.1f %%{/color})' %ratio
          elif ratio>30. and ratio<=60.:
            ratio_desc='(умерло: {color=#ff8100}%.1f %%{/color})' %ratio
          elif ratio>1. and ratio<=30.:
            ratio_desc='(умерло: {color=#ff00ff}%.1f %%{/color})' %ratio
          elif ratio>=0. and ratio<=1.:
            ratio_desc='(умерло: {color=#ff0000}%.1f %%{/color})' %ratio
        room_desc='Проведать пленниц (свободных камер: %.0f)' %(game.girls_list.free_size)
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    
    menu:
        'Осмотреть дракона':
            # чтобы вывести сообщение от имени дракона можно использовать "game.dragon"
            $ buffs=game.buff_description()
            game.dragon.third "{font=fonts/AnticvarShadow.ttf}{size=+5} [game.dragon.fullname] {/size}{/font} \n\n[game.dragon.description]\n\n[buffs]"
            jump lb_location_lair_main
        'Проинспектировать логово':
            python hide:
                lair_description = u"Логово: %s.\n" % game.lair.type.name
                if len(game.lair.upgrades) > 0: 
                    lair_description += u"Улучшения:\n"
                    for upgrade in game.lair.upgrades.values():   
                        lair_description += u" %s\n" % upgrade.name
                else:
                    lair_description += u"Улучшений нет"
                narrator(lair_description)
            call lb_location_lair_main from _call_lb_location_lair_main
        'Сотворить заклинание' if game.dragon.mana > 0:
            if game.choose_spell(u"Вернуться в логово"):
                python:
                    game.dragon.drain_mana()
#                    game.dragon.gain_rage()
            call lb_location_lair_main from _call_lb_location_lair_main_1
        'Чахнуть над златом' if game.lair.treasury.wealth > 0:
            python:
                files = [f for f in renpy.list_files() if f.startswith("img/bg/hoard/%s" % game.dragon.color_eng)]    
                if len(files) > 0:
                    treasurybg = random.choice(files)
                else:
                    treasurybg = "img/bg/hoard/base.jpg"
                renpy.treasurybg = ui.image(treasurybg)
                    
            show image renpy.treasurybg as bg
            nvl clear
            menu:
                '[game.lair.treasury.wealth_description]'
                '[game.lair.treasury.gems_mass_description]' if game.lair.treasury.gem_mass > 0:
                    "[game.lair.treasury.gems_list]"
                    nvl clear
                '[game.lair.treasury.materials_mass_description]' if game.lair.treasury.metal_mass + game.lair.treasury.material_mass > 0:
                    "[game.lair.treasury.materials_list]"
                    nvl clear
                '[game.lair.treasury.coin_mass_description]' if game.lair.treasury.coin_mass > 0:
                    $ description = u"В сокровищнице:\n"
                    $ description += u"%s\n" % treasures.number_conjugation_rus(game.lair.treasury.farting, u"фартинг")
                    $ description += u"%s\n" % treasures.number_conjugation_rus(game.lair.treasury.taller, u"талер")
                    $ description += u"%s" % treasures.number_conjugation_rus(game.lair.treasury.dublon, u"дублон")
                    "[description]"
                    nvl clear
                '[game.lair.treasury.jewelry_mass_description]' if len(game.lair.treasury.jewelry) > 0:
                    menu:
                        'Самая дорогая в сокровищнице':
                            "[game.lair.treasury.most_expensive_jewelry]"
                            nvl clear
                        'Самая дешёвая в сокровищнице':
                            "[game.lair.treasury.cheapest_jewelry]"
                            nvl clear
                        'Случайная':
                            "[game.lair.treasury.random_jewelry]"
                            nvl clear
                        'Навести порядок в сокровищнице':
                            call screen order_treasury
                            nvl clear
                        'Вернуться в логово':
                            jump lb_location_lair_main   
                'Вернуться в логово':
                    jump lb_location_lair_main        
            call lb_location_lair_main from _call_lb_location_lair_main_2
        '[room_desc]' if game.girls_list.prisoners_count > 0:
            call screen girls_menu
            call lb_location_lair_main from _call_lb_location_lair_main_3            
        'Смастерить вещь' if ('servant' in game.lair.upgrades) or ('gremlin_servant' in game.lair.upgrades):
            $ new_item = game.lair.treasury.craft(**data.craft_options['servant'])
            if new_item:
                $ game.lair.treasury.receive_treasures([new_item])
                $ test_description = new_item.description()
                "Изготовлено: [test_description]."
            call lb_location_lair_main from _call_lb_location_lair_main_4                
        'Уволить слуг-гремлинов' if 'gremlin_servant' in game.lair.upgrades:
            $ del game.lair.upgrades['gremlin_servant']
            "Гремлины уходят"
            call lb_location_lair_main from _call_lb_location_lair_main_5            
        'Уволить охрану' if 'smuggler_guards' in game.lair.upgrades:
            $ del game.lair.upgrades['smuggler_guards']
            "Охрана покидает посты"
            $ game.girls_list.romeo_check()
            call lb_location_lair_main from _call_lb_location_lair_main_6
        'Вспомнить былое [ratio_desc]':
#          menu:
#            'Вспомнить приятные моменты':
#                $ menu_list=sorted(game.chronik.death_reason.keys(),key=lambda i: len(game.chronik.death_reason[i]),reverse=True)
#                $ bot_desc = "{color=#ffffff}%s %.1f{/color}" % (data.death_reason_desc[menu_list[0]], 100.*len(game.chronik.death_reason[menu_list[0]])/game.chronik.tot_dead)
#                '[menu_list[0]]\n[menu_list[1]]\n[menu_list[2]]]'
                call screen dragon_chronik_menu
                call lb_location_lair_main from _call_lb_location_lair_main_7
#            'Вспомнить славные деяния':
#                call screen scroll_chronik_menu
#                call lb_location_lair_main from _call_lb_location_lair_main_8
        'Лечь спать':
            nvl clear
            if game.witch_st1==5:
              'Дракон на мгновение задумывается, какой может быть награда ведьмы.'
              game.dragon 'Надо сходить проверить!'
              return
            if game.witch_st1==4 and game.dragon.health<2:
              $ game.dragon.health=2
              witch 'На следующий год тебе понадобятся все силы. На этот раз я исцелю тебя бесплатно.'
            python:
                # Делаем хитрую штуку.
                # Используем переменную game_loaded чтобы определить была ли игра загружена.
                # Но ставим ее перед самым сохранинием, используя renpy.retain_after_load() для того
                # чтобы она попала в сохранение.
                if 'game_loaded' in locals() and game_loaded:
                    del game_loaded
                    game.narrator("game loaded")
                    renpy.restart_interaction()
                else:
                    game_loaded = True
                    renpy.retain_after_load()
                    
                    if not freeplay:
                        utils.call ("lb_achievement_acquired")
                        game.save()
                    else:
                        game.save_freegame()
                     
                    save_blocked = True

                    game.sleep()
                    save_blocked = False
                    del game_loaded
# Проверка на визит Архимонда
            if game.summon.seal>data.max_summon and not game.historical_check('archimonde_was'):
              call lb_archimonde_arrive from _call_lb_archimonde_arrive
            if game.witch_st1==2 or game.witch_st1==3:
              witch 'Я же человеческим языком тебя просила: выполнить задание в прошлом году...'
              witch 'Больше не рассчитывай ни на помощь гремлинов, ни на логово контрабандистов, ни на какие магические заклинания' 
              game.dragon 'Ой! Кажется, я проиграл...'
              jump lb_game_over
            if game.witch_st1==5:
              call lb_gwidon from _call_lb_gwidon
                    
            $this_turn_achievements = []
        'Покинуть логово':
            $ pass
            
    return
    
label lb_save_game:
#    hide screen navigation
    pause 0.01
    python:
        if not freeplay:
          game.save()
        else:
          game.save_freegame() 
    return
   

label lb_chronical_description:
    nvl clear
    python:  # Задаём аватарку
        Current_girl = Talker(game_ref=game)
        Current_girl.avatar = game.chronik.chronik_girl_avatar[game.chronik.active_dragon][game.chronik.active_girl]
        Current_girl.name = game.chronik.chronik_girl_name[game.chronik.active_dragon][game.chronik.active_girl]
    if game.chronik.chronik_image[game.chronik.active_dragon][game.chronik.active_girl] is not None:
      hide bg
      show expression game.chronik.chronik_image[game.chronik.active_dragon][game.chronik.active_girl] 
      pause (500.0)
      hide expression game.chronik.chronik_image[game.chronik.active_dragon][game.chronik.active_girl]
      show expression game.chronik.chronik_image[game.chronik.active_dragon][game.chronik.active_girl] as bg
    else:
      $ place = game.lair.type_name
      hide bg
      show place as bg
    $ description = game.chronik.description()
    Current_girl.third "[description]"
    call screen dragon_chronik_menu
#    call lb_location_lair_main from _call_lb_location_lair_main_8
    return

label lb_chronical_scroll_description: # Описание произошедших событий
    nvl clear
    hide bg
    show expression "img/bg/special/scroll_2.jpg" as bg
#    $ description = game.chronik.chronik_history[game.chronik.active_centure]
    $ narrator (game.chronik.chronik_history[game.chronik.active_centure])
    call screen scroll_chronik_menu
    return

label lb_treasure_description:
    hide bg
    show expression "img/bg/hoard/Smaug.jpg" as bg
    nvl clear
    $ description = game.lair.treasury.definitly_jewelry(game.chronik.list_of_treasures[game.chronik.active_treasure_type][game.chronik.active_treasure])
    "[description]"
#    $ description = game.chronik.list_of_treasures[game.chronik.active_treasure_type][game.chronik.active_treasure][0]
#    "[description]"

    if not game.chronik.active_gift_mod:
      call screen order_treasury_item(cost=game.chronik.active_cost)
    else:
      $ name=treasures.capitalize_first(game.chronik.list_of_treasures[game.chronik.active_treasure_type][game.chronik.active_treasure].description())
      menu:
        '[name] - прекрасный подарок!':
          python:
            for tres_i in xrange(len(game.lair.treasury.jewelry)):
              if game.lair.treasury.jewelry[tres_i].description()==game.chronik.list_of_treasures[game.chronik.active_treasure_type][game.chronik.active_treasure].description():            
                game.chronik.active_gift=game.lair.treasury.jewelry[tres_i]
                del game.lair.treasury.jewelry[tres_i]
                break
          call lb_talk_gift from _call_lb_talk_gift_1
        'Лучше выберу что-нибудь другое':
          call screen order_treasury_item(cost=game.chronik.active_cost,gift_mod=game.chronik.active_gift_mod)
    return

label lb_controls_overwrite:
    show screen controls_overwrite
    return






