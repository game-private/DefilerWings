﻿# coding=utf-8
# Как это работает
#
# В листе map_data содержатся названия локаций
# По маске 'img/map/button_<localtion>_%s.png' выбираются картинки для imagebutton
# TODO: добавить описание для Action
#
# Добавление локации на карте
# Для того чтобы добавить локацию на карте, нужно добавить в лист map_data название этой локации (location, name)
# где location - внутреннее название локации, а name - отображаемое название локации пользователю
# и добавить как минимум две картинки в img/map/ с названиями button_<location>_idle и button_<location>_hover
# для положений не выделенной локации и локации при наведении соотвественно.
# Изображения должны по размеру совпадать с размером задника и содержать только саму кнопку -
# все остальное прозрачный альфа-слой.
#
# TODO: Можно добавить map_data куда-нибудь в Game, для того чтобы была возможность управления налету.

# Составляем стиль для подсказки.
# TODO: выпилить, сделав нормальный стиль для prompt
init python:
    from pythoncode.focus_mask_ext import FocusMaskCallable
    
    style.map_tooltip = Style("prompt")
    style.map_tooltip.background = Frame("img/bg/logovo.png", 5, 5)

screen main_map:
    python:
        # После добавления новых кнопок или их обновления НЕОБХОДИМО сгенерировать новые координаты
        # при помощи функции focus_mask_ext.create_focus_mask_data. Получившийся в итоге файл должен
        # располагаться в focus_mask_ext.COORDINATES_FILE_PATH.
        map_data = [
            ("sea", "Море"),
            ("mordor", "Земли Владычицы"),
            ("sky", "Небеса"),
            ("forest", "Лес"),
            ("smuggler", "Приют контрабандистов"),
            ("mountain", "Горы"),
            ("road", "Торговый тракт"),
            ("ruin", "Старые руины"),
            ("gremlin", "Деревня гремлинов"),
            ("city", "Столица"),
            ("plains", "Обжитые земли")
        ]
    
    default map_tooltip = Tooltip("None")  # Подсказка на что сейчас наведена мышка
    # Тултип для статусбара, если не объявить в родительском окне, то почему-то не работает.
    default status_bar_tooltip = Tooltip("None")
    fixed:
        fit_first True  # Принимаем размер следущей картинки. Нужно для корректного отображения подсказки посередине.
        add "img/map/ground.jpg"
    
        for target, description in map_data:
            imagebutton:  # target
                auto "img/map/button_" + target + "_%s.png"
                action Return("lb_location_%s_main" % target)
                focus_mask FocusMaskCallable(target)
                hovered map_tooltip.Action(description)
    
        if map_tooltip.value != "None":  # Костыль-костылык. Не показываем подсказу если у нее значение по умолчанию
            frame:                      # Делаем небольшой фрейм, чтобы показать подсказку
                style "map_tooltip"     # Ставим ему стиль
                xpadding 10
                ypadding 5
                xalign 0.5
                yalign 0.01
                text map_tooltip.value:  # Выводим собственно текст подсказки
                    xalign 0.5
        
        if game.dragon is not None:
            text u"{font=fonts/AnticvarShadow.ttf} Год %d э.д. (Прошло %d) {/font}" % (game.year, game.dragon.age)
    
    if game.dragon is not None:
        text "{font=fonts/AnticvarShadow.ttf} %d фартингов {/font}" % game.lair.treasury.money:
            xalign 0.7
            yalign 1
            size 25


    # Выходим из под действия fixed
    use status_bar
    if game.lair is not None:
        use to_lair_button
    
    if game.dragon is not None and game.dragon.special_places_count > 0:
        use special_places 

# Составляем стиль для подсказки.
# TODO: выпилить, сделав нормальный стиль для prompt
init python:
    style.status_bar_tooltip = Style("prompt")
    style.status_bar_tooltip.background = Frame("img/bg/logovo.png", 5, 5)
    
screen status_bar:
    default status_bar_tooltip = Tooltip("None")
    fixed:
        xalign 1.0
        xmaximum 320
        
        add "img/bg/status-bar.png"
        
        if game.dragon is not None and game.dragon.is_alive:
            # @fdsc
            text "%d / %d" % (game.dragon.energy(), game.dragon.max_energy()):
                pos(65, 365)
                anchor(0.5, 0.5)
                size 30
                color "a7926d"      # Цвет взял с шаблона, но тут он почему-то выглядит по-другому.
                outlines[(2, "#0004", 0, 0), (4, "#0003", 0, 0), (6, "#0002", 0, 0), (8, "#0001", 0, 0)]
            mousearea:              # Зона при наведении на которую всплывет подсказка
                area(42, 342, 45, 45)
                hovered status_bar_tooltip.Action("Запас сил / max")

            # @fdsc
            text "%d / %d" % (game.dragon.reputation.level, game.mobilization.level):
                # pos(160, 365)
                pos(170, 365)
                anchor(0.5, 0.5)
                size 30
                color "a7926d"     
                outlines[(2, "#0004", 0, 0), (4, "#0003", 0, 0), (6, "#0002", 0, 0), (8, "#0001", 0, 0)]
            mousearea:              # Зона при наведении на которую всплывет подсказка
                area(140, 342, 45, 45)
                hovered status_bar_tooltip.Action("Дурная слава / Мобилизация")

            add '%s' % game.dragon.avatar:
                pos(160, 155)
                anchor(0.5, 0.5)

            text "{font=fonts/AnticvarShadow.ttf}%s{/font}" % game.dragon.name:
                pos(160, 315)
                anchor(0.5, 0.5)
                size 25
                color "a7926d"     
                outlines[(2, "#0004", 0, 0), (4, "#0003", 0, 0), (6, "#0002", 0, 0), (8, "#0001", 0, 0)]

            text "%d" % game.dragon.mana:
                pos(260, 365)
                anchor(0.5, 0.5)
                size 30
                color "a7926d"     
                outlines[(2, "#0004", 0, 0), (4, "#0003", 0, 0), (6, "#0002", 0, 0), (8, "#0001", 0, 0)]
            mousearea:              # Зона при наведении на которую всплывет подсказка
                area(240, 342, 45, 45)
                hovered status_bar_tooltip.Action("Коварство")

            text "%s" % hunger_texts[game.dragon.hunger]:
                pos(160, 447)
                anchor(0.5, 0.5)
                size 23

            text "%s" % lust_texts[game.dragon.lust]:
                pos(160, 477)
                anchor(0.5, 0.5)
                size 23

            text "%s" % bloodlust_texts[game.dragon.bloodiness]:
                pos(160, 503)
                anchor(0.5, 0.5)
                size 23

            text "%s" % health_texts[game.dragon.health]:
                pos(160, 530)
                anchor(0.5, 0.5)
                size 23
        
        if status_bar_tooltip.value != "None":  # см. map_tooltip на экране main_map
            frame:
                style "status_bar_tooltip"
                xpadding 10
                ypadding 5
                pos(158, 396)
                text status_bar_tooltip.value:
                    xalign 0.5

        if config.developer:
            textbutton "{font=fonts/Tchekhonin2.ttf}О{/font}{font=fonts/times.ttf}тладка{/font}":
                pos(72, 549)
                xysize(174, 36)
                text_xalign 0.5
                text_yalign 0.5
                background "img/bg/logovo.png"
                text_size 22
                action ShowMenu("lb_test_main")

screen special_places:
    fixed:
        xalign 1.0
        xmaximum 320
        textbutton "{font=fonts/Tchekhonin2.ttf}М{/font}{font=fonts/times.ttf}еста{/font}":
            pos(72, 599)
            xysize(174, 36)
            text_xalign 0.5
            text_yalign 0.5
            background "img/bg/logovo.png"
            text_size 22
            action Return("lb_special_places")
        
screen to_lair_button:
    fixed:
        xalign 1.0
        xmaximum 320
        textbutton "{font=fonts/Tchekhonin2.ttf}Л{/font}{font=fonts/times.ttf}огово{/font}":
            pos(72, 649)
            xysize(174, 36)
            text_xalign 0.5
            text_yalign 0.5
            background "img/bg/logovo.png"
            text_size 22
            action Return("lb_location_lair_main")


screen battle_map:
    python:
        # После добавления новых кнопок или их обновления НЕОБХОДИМО сгенерировать новые координаты
        # при помощи функции focus_mask_ext.create_focus_mask_data. Получившийся в итоге файл должен
        # располагаться в focus_mask_ext.COORDINATES_FILE_PATH.
        map_data = [
            ("sea", "Попробовать справиться с Дагоном"),
            ("sky", "Бросить вызов богам"),
            ("forest", "Вторгнуться в Зачарованный лес альвов"),
            ("mountain", "Парировать угрозу цвергов"),
            ("ruin", "Отомстить ведьме за унижения"),
            ("city", "Начать штурм Столицы"),
            ("plains", "Разорить обжитые земли")
        ]
    
    default map_tooltip = Tooltip("None")  # Подсказка на что сейчас наведена мышка
    # Тултип для статусбара, если не объявить в родительском окне, то почему-то не работает.
    default status_bar_tooltip = Tooltip("None")
    fixed:
        fit_first True  # Принимаем размер следущей картинки. Нужно для корректного отображения подсказки посередине.
        add "img/map/ground.jpg"
    
        for target, description in map_data:
            imagebutton:  # target
                auto "img/map/button_" + target + "_%s.png"
                action Jump("lb_mordor_%s" % target)
                focus_mask FocusMaskCallable(target)
                hovered map_tooltip.Action(description)
    
        if map_tooltip.value != "None":  # Костыль-костылык. Не показываем подсказу если у нее значение по умолчанию
            frame:                      # Делаем небольшой фрейм, чтобы показать подсказку
                style "map_tooltip"     # Ставим ему стиль
                xpadding 10
                ypadding 5
                xalign 0.5
                yalign 0.01
                text map_tooltip.value:  # Выводим собственно текст подсказки
                    xalign 0.5
        
    # Выходим из под действия fixed
    use status_bar
    if game.dragon.mana > 0:
        use to_magic_buttom
    
screen to_magic_buttom:
    fixed:
        xalign 1.0
        xmaximum 320
        textbutton "{font=fonts/Tchekhonin2.ttf}З{/font}{font=fonts/times.ttf}аклинания{/font}":
            pos(72, 649)
            xysize(174, 36)
            text_xalign 0.5
            text_yalign 0.5
            background "img/bg/logovo.png"
            text_size 22
            action Jump("lb_mordor_spell" ) 

screen border_map:
    python:
        # После добавления новых кнопок или их обновления НЕОБХОДИМО сгенерировать новые координаты
        # при помощи функции focus_mask_ext.create_focus_mask_data. Получившийся в итоге файл должен
        # располагаться в focus_mask_ext.COORDINATES_FILE_PATH.
        map_data = [
            ("mordor", "Прорвать пограничные укрепления")
        ]
    
    default map_tooltip = Tooltip("None")  # Подсказка на что сейчас наведена мышка
    # Тултип для статусбара, если не объявить в родительском окне, то почему-то не работает.
    default status_bar_tooltip = Tooltip("None")
    fixed:
        fit_first True  # Принимаем размер следущей картинки. Нужно для корректного отображения подсказки посередине.
        add "img/map/ground.jpg"
    
        for target, description in map_data:
            imagebutton:  # target
                auto "img/map/button_" + target + "_%s.png"
                action Jump("lb_mordor_%s" % target)
                focus_mask FocusMaskCallable(target)
                hovered map_tooltip.Action(description)
    
        if map_tooltip.value != "None":  # Костыль-костылык. Не показываем подсказу если у нее значение по умолчанию
            frame:                      # Делаем небольшой фрейм, чтобы показать подсказку
                style "map_tooltip"     # Ставим ему стиль
                xpadding 10
                ypadding 5
                xalign 0.5
                yalign 0.01
                text map_tooltip.value:  # Выводим собственно текст подсказки
                    xalign 0.5
        
    # Выходим из под действия fixed
    use status_bar
    
screen to_magic_buttom:
    fixed:
        xalign 1.0
        xmaximum 320
        textbutton "{font=fonts/Tchekhonin2.ttf}З{/font}{font=fonts/times.ttf}аклинания{/font}":
            pos(72, 649)
            xysize(174, 36)
            text_xalign 0.5
            text_yalign 0.5
            background "img/bg/logovo.png"
            text_size 22
            action Jump("lb_mordor_spell" ) 

screen main_battle_map:
    python:
        # После добавления новых кнопок или их обновления НЕОБХОДИМО сгенерировать новые координаты
        # при помощи функции focus_mask_ext.create_focus_mask_data. Получившийся в итоге файл должен
        # располагаться в focus_mask_ext.COORDINATES_FILE_PATH.
        map_data = [
            ("road", "Дать генеральное сражение")
        ]
    
    default map_tooltip = Tooltip("None")  # Подсказка на что сейчас наведена мышка
    # Тултип для статусбара, если не объявить в родительском окне, то почему-то не работает.
    default status_bar_tooltip = Tooltip("None")
    fixed:
        fit_first True  # Принимаем размер следущей картинки. Нужно для корректного отображения подсказки посередине.
        add "img/map/ground.jpg"
    
        for target, description in map_data:
            imagebutton:  # target
                auto "img/map/button_" + target + "_%s.png"
                action Jump("lb_mordor_%s" % target)
                focus_mask FocusMaskCallable(target)
                hovered map_tooltip.Action(description)
    
        if map_tooltip.value != "None":  # Костыль-костылык. Не показываем подсказу если у нее значение по умолчанию
            frame:                      # Делаем небольшой фрейм, чтобы показать подсказку
                style "map_tooltip"     # Ставим ему стиль
                xpadding 10
                ypadding 5
                xalign 0.5
                yalign 0.01
                text map_tooltip.value:  # Выводим собственно текст подсказки
                    xalign 0.5
        
    # Выходим из под действия fixed
    use status_bar
    
screen to_magic_buttom:
    fixed:
        xalign 1.0
        xmaximum 320
        textbutton "{font=fonts/Tchekhonin2.ttf}З{/font}{font=fonts/times.ttf}аклинания{/font}":
            pos(72, 649)
            xysize(174, 36)
            text_xalign 0.5
            text_yalign 0.5
            background "img/bg/logovo.png"
            text_size 22
            action Jump("lb_mordor_spell" ) 
