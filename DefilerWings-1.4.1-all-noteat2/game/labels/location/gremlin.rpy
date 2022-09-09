# coding=utf-8
label lb_location_gremlin_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))
    $ place = 'gremlins'
    hide bg
    nvl clear
    if game.witch_st1>0:
      show expression 'img/bg/special/village.jpg' as bg
      '[game.dragon.name] нашёл деревню гремлинов. Но не нашёл в ней никаких гремлинов!'
      game.dragon 'ЧЯДНТ?!'
      return
    show place as bg
        
    # Стоимость года работы гремлинов-слуг
    $ servant_cost = data.lair_upgrades['gremlin_servant']['cost']
    # Стоимость установки механических ловушек
    $ mechanic_traps_cost = 500
    # Стоимость строительства укреплений
    $ fortification_cost = 1000
    
    # @fdsc Украшения для логова
    $ brilliance_cost      = 25000
    $ brilliance_heat_cost = 500

    nvl clear
        
    menu:
        'Нанять слуг' if 'servant' not in game.lair.upgrades and 'gremlin_servant' not in game.lair.upgrades:
            "Гремлины будут служить в логове, приглядывать за пленницами и охранять их. Всего за [servant_cost] фартингов в год"
            menu:
                "Пообещать им заплатить" if servant_cost <= game.lair.treasury.wealth:
                    $ game.lair.add_upgrade('gremlin_servant')
                    "Гремлины идут {s}за сокровищами.{/s} заботиться о пленницах, не смыкая глаз."
                "Отказаться":
                    call lb_location_gremlin_main from _call_lb_location_gremlin_main
        'Ловушки для логова' if (not game.lair.type.provide or 'mechanic_traps' not in game.lair.type.provide) and 'mechanic_traps' not in game.lair.upgrades:
            menu:
                "Стоимость установки ловушек: [mechanic_traps_cost] фартингов"
                "Установить ловушки" if mechanic_traps_cost <= game.lair.treasury.money:
                    $ game.lair.add_upgrade('mechanic_traps')
                    $ game.lair.treasury.money -= mechanic_traps_cost
                    'Теперь вору не поздоровится... если он окажется настолько косоруким, что попадётся в эту ловушку, конечно же!'
                "Уйти":
                    call lb_location_gremlin_main from _call_lb_location_gremlin_main_1
        'Укрепления для логова' if 'gremlin_fortification' not in game.lair.upgrades:
            menu:
                "Стоимость возведения укреплений: [fortification_cost] фартингов"
                "Укрепить логово" if fortification_cost <= game.lair.treasury.money:
                    $ game.lair.add_upgrade('gremlin_fortification')
                    $ game.lair.treasury.money -= fortification_cost
                    'Гремлины устанавливают в логове дракона решётки и двери с хитрыми замками, укрепляют стены. Вор не пройдёт!'
                "Уйти":
                    call lb_location_gremlin_main from _call_lb_location_gremlin_main_2

        # @fdsc
        'Украшения для логова' if (not game.lair.type.provide or 'lair_brilliance' not in game.lair.type.provide) and 'lair_brilliance' not in game.lair.upgrades:
            menu:
                "Стоимость украшения логова: [brilliance_cost] фартингов"
                "Украсить логово" if brilliance_cost <= game.lair.treasury.money:
                    $ game.lair.add_upgrade('lair_brilliance')
                    $ game.lair.treasury.money -= brilliance_cost

                    'Девушки будут без ума от украшенного логова!'
                "Уйти":
                    call lb_location_gremlin_main
        'Золотые полы для логова' if (not game.lair.type.provide or 'lair_brilliance_gold' not in game.lair.type.provide) and 'lair_brilliance_gold' not in game.lair.upgrades:
            menu:
                "Стоимость украшения логова: [brilliance_cost] фартингов"
                "Украсить логово" if brilliance_cost <= game.lair.treasury.money:
                    $ game.lair.add_upgrade('lair_brilliance_gold')
                    $ game.lair.treasury.money -= brilliance_cost
                    'Девушки будут поражены, что ходят по золотому полу!'
                "Уйти":
                    call lb_location_gremlin_main
        'Ковровые дорожки для логова' if (not game.lair.type.provide or 'lair_brilliance_gold_heat' not in game.lair.type.provide) and 'lair_brilliance_gold_heat' not in game.lair.upgrades and 'lair_brilliance_gold' in game.lair.upgrades:
            menu:
                "Стоимость украшения логова: [brilliance_heat_cost] фартингов"
                "Украсить логово" if brilliance_heat_cost <= game.lair.treasury.money:
                    $ game.lair.add_upgrade('lair_brilliance_gold_heat')
                    $ game.lair.treasury.money -= brilliance_heat_cost
                    'Золотые полы красивы, но холодны. Теперь девушки смогут ходить по мягким и тёплым дорожкам, любуясь на золото'
                "Уйти":
                    call lb_location_gremlin_main

        'Смастерить вещь':
            $ new_item = game.lair.treasury.craft(**data.craft_options['gremlin'])
            if new_item:
                $ game.lair.treasury.receive_treasures([new_item])
                $ test_description = new_item.description()
                "Изготовлено: [test_description]."
                call lb_location_gremlin_main from _call_lb_location_gremlin_main_3
        'Уйти':
            $ pass
        
    return