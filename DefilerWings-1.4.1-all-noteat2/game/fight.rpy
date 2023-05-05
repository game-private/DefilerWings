# coding=utf-8
init python:
    from pythoncode import battle

label lb_fight(foe=game.foe, skip_fear=False, fast=False):
#    hide bg
    show expression foe.bg as foeimg_bg
    nvl clear
#    "[foe.name], [foe.kind]"
#    'Должно быть изображение [foe.bg]' 
    if not skip_fear:
        $ battle_status = battle.check_fear(game.dragon, foe)
    else:
        $ battle_status = ['foe_intro', 'foe_alive']

    if not fast:
        $ narrator(foe.battle_description(battle_status, game.dragon))

    while 'foe_alive' in battle_status:

        $ battle_status = battle.battle_action(game.dragon, foe)
        $ description = foe.battle_description(battle_status, game.dragon)
        if not fast:
            "[description]"

        if 'dragon_dead' in battle_status:
            if foe.kind == 'imps' or foe.kind == 'architot_proection':
              call lb_death_dragon from _call_lb_death_dragon_2
            game.dragon "Я подвёл тебя, мама..."
            if freeplay or battle.army_battle:
                jump lb_game_over
            hide foeimg_bg
            nvl clear
            if foe.kind != 'knight':
                $ renpy.pop_return()
            return "defeat"
        elif 'foe_alive' in battle_status:
            $ chances = show_chances(foe)
            if not fast:
                '[chances]'
            nvl clear
            
            if not fast:
                menu:
                    'Продолжать бой':
                        pass
                    'Отступить' if (not battle.army_battle) and not (foe.kind == 'dark_sister' or foe.kind == 'imps'):
                        if foe.kind == 'knight':
                            # Отступаем в новое логово
                            "Позорно бежав, [game.dragon.name] укрылся в первом попавшемся укромном местечке"
                            hide bg
                            show expression "img/bg/special/knight_sucsess.jpg" as bg
                            $ game.girls_list.knight_free_all_girls()
                            $ game.create_lair()
                        elif foe.kind == 'lizardman':
                            # Отступаем в новое логово
                            "Позорно бежав, [game.dragon.name] укрылся в первом попавшемся укромном местечке"
    #                        hide bg
                            call lb_love_lizardman_victory from _call_lb_love_lizardman_victory_1
                            $ game.girls_list.lizardman_free_all_girls()
                            $ game.create_lair()
                        elif foe.kind == 'gargoyle':
                            "Бой с горгульей слишком тяжёл. Пожалуй, стоит отказаться от столь амбициозных целей. Благо, награда, пусть и не  столь ценная, имеется."
                            call lb_fear_plains_retreat from _call_lb_fear_plains_retreat_2
                            $ renpy.pop_return()
                            jump lb_location_lair_main
                        elif foe.kind == 'zombie':
                            "Зомби - крайне надоедливые существа. Но, к счастью, медлительные. [game.dragon.name] с лёгкостью отрывается от противника и обходит толпу нежити по другому коридору."
                            call lb_fear_plains_murder from _call_lb_fear_plains_murder_10
    #                        $ renpy.pop_return()
                            jump lb_location_lair_main
                        elif foe.kind == 'fire_witch':
                            pass
                        elif foe.kind == 'architot_proection':
                            call lb_archimonde_retreat from _call_lb_archimonde_retreat_5
                            $ renpy.pop_return()
                            jump lb_location_lair_main
                        else:
                            "[game.dragon.name] отступает в своё логово, чтобы собраться с силами и продумать новую стратегию."
                        if foe.kind != 'knight' and foe.kind != 'fire_witch':
                            hide foeimg_bg
                            nvl clear
                            $ renpy.pop_return()
                            jump lb_location_lair_main
                        if foe.kind == 'fire_witch':   # К сожалению, сражение с огненной ведьмой требует дополнительных условий.
                            if game.dragon.health>0:
                              '[game.dragon.fullname] пытается позорно скрыться с поля боя.'
                              game.rape.kind_girl 'Куда? Я тебя не отпускала.'
                              'Пламя, как живое, окружает дракона со всех сторон, перекрывая ему пути к отступлению. Избиение продолжается!'
                            else:
                              '[game.rape.kind_girl.name] легонько пинает ногой полумёртвого дракона. Ящер, получив новый ожог, скрючивается от боли.'
                              game.rape.kind_girl 'Ползи прочь, жалкий червь, и помни о моём милосердии!'
                              'Подвывая от боли и униженно восхваляя победительницу, [game.dragon.fullname] уползает с места своего сокрушительного поражения.'
                              call lb_fear_plains_defeat from _call_lb_fear_plains_defeat
                              $ game.rape.dragon_win=False
                              hide foeimg_bg
                              return "retreat"
    #                          jump lb_location_lair_main
                        else:
                          hide foeimg_bg
                          nvl clear
                          if foe.kind == 'dark_novice':
                            $ game.summon.seal += 1
                            'Ещё одна крестьянка отдала свою жизнь на алтаре демонопоклонников. Слабеют печати. Близится победа Легиона.'
                          elif foe.kind == 'dark_apprentice':
                            $ game.summon.seal += 2
                            'Ещё одна горожанка отдала свою жизнь на алтаре демонопоклонников. Слабеют печати. Близится победа Легиона.'
                          elif foe.kind == 'dark_mage':
                            $ game.summon.seal += 4
                            'Ещё одна благородная девица отдала свою жизнь на алтаре демонопоклонников. Слабеют печати. Близится победа Легиона.'
                          elif foe.kind == 'dark_magister':
                            $ game.summon.seal += 8
                            'Ещё одна альва отдала свою жизнь на алтаре демонопоклонников. Слабеют печати. Близится победа Легиона.'
                          elif foe.kind == 'dark_archmage':
                            $ game.summon.seal += 16
                            'Ещё одна титанида отдала свою жизнь на алтаре демонопоклонников. Слабеют печати. Близится победа Легиона.'
                          return "retreat"
    hide foeimg_bg
    nvl clear
    if not battle.army_battle:
      call lb_hope_check from _call_lb_hope_check    # Надежда ещё жива?
    return "win"
