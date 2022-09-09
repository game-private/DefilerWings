# coding=utf-8
init python:
    from pythoncode import focus_mask_ext
    from pythoncode.focus_mask_ext import FocusMaskArchimonde
    from pythoncode import summon
#    from pythoncode import game
    style.rape_tooltip = Style("prompt")  # Стиль для подсказки

screen archimonde_main:
    python:
        summon.path='img/archimonde/screen'
        focus_mask_ext.load_focus_mask_archimonde(summon.path + '/coordinates.bin')
    default rape_tooltip = Tooltip("None")  # Подсказка на что сейчас наведена 
    fixed:
        fit_first True 
        add summon.path + "/ground.jpg"
# Изображение Архитота
        imagebutton:
          auto summon.path + "/button_architot_%s.png"
          focus_mask FocusMaskArchimonde('architot',summon.path)
          action [Hide('archimonde_main'),Jump('lb_dragon_att_archimonde') ]
          hovered rape_tooltip.Action('{color=#ff0000}Присмотреться к противнику{/color}')
# Изображение Ангела
        if game.summon.live['angel']:
          imagebutton:
            auto summon.path + "/button_angel_%s.png"
            focus_mask FocusMaskArchimonde('angel',summon.path)
            action [Hide('archimonde_main'),Jump('lb_angel_info') ]
            hovered rape_tooltip.Action('{color=#ff0000}Присмотреться к божественному союзнику{/color}')
# Изображение Голема
        if game.summon.live['golem']:
          imagebutton:
            auto summon.path + "/button_golem_%s.png"
            focus_mask FocusMaskArchimonde('golem',summon.path)
            action [Hide('archimonde_main'),Jump('lb_golem_info') ]
            hovered rape_tooltip.Action('{color=#ff0000}Присмотреться к механическому союзнику{/color}')
# Изображение Титана
        if game.summon.live['titan']:
          imagebutton:
            auto summon.path + "/button_titan_%s.png"
            focus_mask FocusMaskArchimonde('titan',summon.path)
            action [Hide('archimonde_main'),Jump('lb_titan_info') ]
            hovered rape_tooltip.Action('{color=#ff0000}Присмотреться к титаническому союзнику{/color}')
# Изображение Дракона
        imagebutton:
          auto summon.path + "/button_dragon_%s.png"
          focus_mask FocusMaskArchimonde('dragon',summon.path)
          action [Hide('archimonde_main'),Jump('lb_dragon_info') ]
          hovered rape_tooltip.Action('{color=#ff0000}Трезво оценить собственные силы{/color}')
# Изображение Фиалки
        imagebutton:
          auto summon.path + "/button_jasmine_%s.png"
          focus_mask FocusMaskArchimonde('jasmine',summon.path)
          action [Hide('archimonde_main'),Jump('lb_jasmine_info') ]
          hovered rape_tooltip.Action('{color=#ff0000}Посоветоваться с принцессой Фиалкой{/color}')

        # Стиль для подсказок
        if rape_tooltip.value != "None":  # Костыль-костылык. Не показываем подсказу если у нее значение по умолчанию
            frame:                      # Делаем небольшой фрейм, чтобы показать подсказку
#                style "rape_tooltip"     # Ставим ему стиль
#                background "#99F7FF"    # Голубенький
#                background "#000000"     # Чёрный
                background "#202020"
                xpadding 10
                ypadding 5
                xalign 0.95
                yalign 0.01
                text rape_tooltip.value:  # Выводим собственно текст подсказки
                    xalign 0.5
        