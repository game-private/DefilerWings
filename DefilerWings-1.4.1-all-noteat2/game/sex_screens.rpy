# coding=utf-8
init python:
    from pythoncode import focus_mask_ext
    from pythoncode.focus_mask_ext import FocusMaskGirls, FocusMaskDragons
    from pythoncode import rape
#    from pythoncode import game
    style.rape_tooltip = Style("prompt")  # Стиль для подсказки
    
    
    
screen start_sex:   # Начальный сексуальный экран
    python:
#        focus_mask_ext.load_focus_mask_girls('img/sex_screen/' + hair_color + '/' + num + '/coordinates.bin')
        focus_mask_ext.load_focus_mask_girls(rape.relative_path + '/coordinates.bin')
        name = False  
# Проверка ярости
        if game.rape.rage >= 10 and game.dragon.bloodiness < 1:
          game.rape.game.dragon.gain_rage()
        if game.rape.rage >= 20 and game.dragon.bloodiness < 2:
          game.rape.game.dragon.gain_rage()
        if game.rape.rage >= 30 and game.dragon.bloodiness < 3:
          game.rape.game.dragon.gain_rage()
        if game.rape.rage >= 40 and game.dragon.bloodiness < 4:
          game.rape.game.dragon.gain_rage()
        if game.rape.rage >= 50 and game.dragon.bloodiness < 5:
          game.rape.game.dragon.gain_rage()
# Построение отношений
        ratio=game.rape.actual_health/game.rape.full_health
        if ratio==1:
          game.rape.health_text=u'{color=#00ff00}Цела и невредима{/color}'
        elif ratio<1 and ratio>0.66:
          game.rape.health_text=u'{color=#ccccff}Изрядно потрёпана, но непобеждена{/color}'
        elif ratio<=0.66 and ratio>0.33:
          game.rape.health_text=u'{color=#ff00ff}Может, стоит обратиться к врачу?!{/color}'
        elif ratio<=0.33 and ratio>0:
          game.rape.health_text=u'{color=#ff0000}Срочно в реанимацию!!!{/color}'
# Поправка на отрицательную гордость
        if game.rape.actual_proud<0:
          game.rape.actual_proud=0
        ratio=game.rape.actual_proud/game.rape.full_proud
        if ratio>0.66:
          game.rape.proud_text=u'{color=#ff0000}Умрёт, но не покорится{/color}'
        elif ratio>0.33 and ratio <=0.66:
          game.rape.proud_text=u'{color=#ff00ff}Яростно отбивается и шипит сквозь стиснутые зубы{/color}'
        elif ratio>0 and ratio <=0.33:
          game.rape.proud_text=u'{color=#ccccff}Заламывает руки и молит о пощаде{/color}'
        elif ratio==0:
          game.rape.proud_text=u'{color=#00ff00}Полностью сломлена и готова на всё{/color}'
#        Jump('lb_sex_ratio') 
#        Function(game.rape.check_rage)
#        Function(game.rape.define_ratio)

# Начало экранов
    default rape_tooltip = Tooltip("None")  # Подсказка на что сейчас наведена мышка
    fixed:
        fit_first True 
        add rape.relative_path + "/ground.jpg"
        if game.dragon.bloodiness < 5:
          imagebutton:
            auto rape.relative_path + "/button_pussy_%s.png"
            focus_mask FocusMaskGirls('pussy',rape.relative_path)
            action [Hide('start_sex'),Show('penetration_sex') ]
            hovered rape_tooltip.Action('{color=#ff0000}Попытаться взять силой {/color}')
        if game.dragon.bloodiness < 5 and game.rape.is_bdsm_possible:
          imagebutton:
            auto rape.relative_path +  "/button_head_%s.png"
            focus_mask FocusMaskGirls('head',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Попытаться сломить волю {/color}' )
            action [Hide('start_sex'),Show('bdsm_sex') ]
        if game.dragon.bloodiness < 5 and not game.rape.is_bdsm_possible:
          imagebutton:
            idle rape.relative_path +  "/button_head_idle.png"
            hover rape.relative_path +  "/button_head_idle.png"
            focus_mask FocusMaskGirls('head',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] с удовольствием сломил бы волю пленницы - вот только нечем!{/color}' )
            action [Hide('start_sex'),Show('start_sex') ]
        if game.rape.fail:   # Попытка провалилась...
          imagebutton:
            auto rape.relative_path +  "/button_arms_and_legs_%s.png"
            focus_mask FocusMaskGirls('arms_and_legs',rape.relative_path)
            if not game.girl.type == 'mermaid' and not game.girl.type == 'siren':
              hovered rape_tooltip.Action('{color=#ff0000}Оторвать руки и ноги{/color}' )
            else:
              hovered rape_tooltip.Action('{color=#ff0000}Оторвать руки и хвост{/color}' )
            action [Hide('start_sex'),Jump('lb_bdsm_cripple') ]
        imagebutton:
          auto rape.relative_path + "/button_stomach_%s.png"
          focus_mask FocusMaskGirls('stomach',rape.relative_path)
          if game.dragon.hunger > 0:
            hovered rape_tooltip.Action('{color=#ff0000}Подзакусить девушкой{/color}')
            action [Hide('start_sex'),Jump('lb_rape_eat_girl') ]
          else:
            hovered rape_tooltip.Action('{color=#ff0000}Разодрать девушку на части{/color}')
            action [Hide('start_sex'),Jump('lb_rape_kill_girl') ]


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
                
# Второй фрейм, с постоянными подсказками.
            frame:
              background "#202020"
              xpadding 10
              ypadding 5
              xalign 0.03
              yalign 0.01
              xsize  250
              xfill True
#              hbox:
              text '{font=fonts/AnticvarShadow.ttf}{size=+20}Дракон{/size}{/font}\n{size=+10}%s{/size}' % (bloodlust_texts[game.dragon.bloodiness]):  # Выводим собственно текст подсказки
                    xalign 0.5

# Третий  фрейм, с подсказками о девушках.
            frame:
              background "#202020"
              xpadding 10
              ypadding 5
              xalign 0.03
              yalign 0.3
              xsize  250
              xfill True
              text '{font=fonts/AnticvarShadow.ttf}{size=+20}Девушка{/size}{/font}\n%s\n%s' % (game.rape.health_text,game.rape.proud_text):  # Выводим собственно текст подсказки
                xalign 0.5
                

#        hbox: # Кнопки "вернуться" не приддусмотрено
#            ypos 680
#            xpos 1120
#            spacing 50
#            textbutton _("Вернуться") action [Jump('lb_lair_sex') ]


screen penetration_sex:
    python:
        focus_mask_ext.load_focus_mask_girls(rape.relative_path + '/coordinates.bin')
        if game.rape.rage >= 10 and game.dragon.bloodiness < 1:
          game.rape.game.dragon.gain_rage()
        if game.rape.rage >= 20 and game.dragon.bloodiness < 2:
          game.rape.game.dragon.gain_rage()
        if game.rape.rage >= 30 and game.dragon.bloodiness < 3:
          game.rape.game.dragon.gain_rage()
        if game.rape.rage >= 40 and game.dragon.bloodiness < 4:
          game.rape.game.dragon.gain_rage()
        if game.rape.rage >= 50 and game.dragon.bloodiness < 5:
          game.rape.game.dragon.gain_rage()
# Построение отношений
        ratio=game.rape.actual_health/game.rape.full_health
        if ratio==1:
          game.rape.health_text=u'{color=#00ff00}Цела и невредима{/color}'
        elif ratio<1 and ratio>0.66:
          game.rape.health_text=u'{color=#ccccff}Изрядно потрёпана, но непобеждена{/color}'
        elif ratio<=0.66 and ratio>0.33:
          game.rape.health_text=u'{color=#ff00ff}Может, стоит обратится к врачу?!{/color}'
        elif ratio<=0.33 and ratio>0:
          game.rape.health_text=u'{color=#ff0000}Срочно в реанимацию!!!{/color}'
        ratio=game.rape.actual_proud/game.rape.full_proud
        if ratio>0.66:
          game.rape.proud_text=u'{color=#ff0000}Умрёт, но не покорится{/color}'
        elif ratio>0.33 and ratio <=0.66:
          game.rape.proud_text=u'{color=#ff00ff}Яростно отбивается и шипит сквозь стиснутые зубы{/color}'
        elif ratio>0 and ratio <=0.33:
          game.rape.proud_text=u'{color=#ccccff}Заламывает руки и молит о пощаде{/color}'
        elif ratio==0:
          game.rape.proud_text=u'{color=#00ff00}Полностью сломлена и готова на всё{/color}'
    default rape_tooltip = Tooltip("None")  # Подсказка на что сейчас наведена мышка
    fixed:
        fit_first True 
        add rape.relative_path + "/ground.jpg"
        if game.dragon.bloodiness < 5 and game.rape.erection <4: # Если не пришёл в ярость и не кончил, можно продолжать
          imagebutton:   # Изнасилование
            auto rape.relative_path + "/button_pussy_%s.png"
            focus_mask FocusMaskGirls('pussy',rape.relative_path)
            if game.rape.erection == 0:
              hovered rape_tooltip.Action('{color=#ff0000}Выпустить член из складок плоти{/color}')
            elif game.rape.erection == 1:
              hovered rape_tooltip.Action('{color=#ff0000}Проникнуть в лоно{/color}')
            elif game.rape.erection == 2:
              hovered rape_tooltip.Action('{color=#ff0000}Совершать фрикции{/color}')
            elif game.rape.erection == 3:
              hovered rape_tooltip.Action('{color=#ff0000}Кончить!{/color}')
            action [Hide('penetration_sex'),Jump('lb_rape_erection') ]

        # Завершить приятный процесс
        if game.dragon.bloodiness < 5 and game.rape.erection == 4: # Всё, кончил
          imagebutton:
            idle rape.relative_path + "/button_pussy_done.png"
            hover rape.relative_path + "/button_pussy_done.png"
            focus_mask FocusMaskGirls('pussy',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Всё...{/color}')
            action  [Hide('penetration_sex'),Jump('lb_rape_end') ]

        # Обвиться вокруг тела
        if game.rape.body and game.dragon.bloodiness < 5 and game.rape.erection <4:
          imagebutton:
            auto rape.relative_path + "/button_stomach_%s.png"
            focus_mask FocusMaskGirls('stomach',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Обвиться вокруг пленницы{/color}')
            action [Hide('penetration_sex'),Jump('lb_rape_body') ]
        if not game.rape.body:  # Обвился вокруг тела
          imagebutton:
            idle rape.relative_path + "/button_stomach_done.png"
            hover rape.relative_path + "/button_stomach_done.png"
            focus_mask FocusMaskGirls('stomach',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] уже обвился вокруг пленницы{/color}')
            action  [Hide('penetration_sex'),Show('penetration_sex') ]

        # Схватить за руки
        if game.rape.arms and game.dragon.paws > 0 and game.dragon.bloodiness < 5 and game.rape.erection <4:
          imagebutton:
            auto rape.relative_path + "/button_arms_%s.png"
            focus_mask FocusMaskGirls('arms',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Схватить за руки{/color}')
            action [Hide('penetration_sex'),Jump('lb_rape_arms') ]
        if not game.rape.arms:  # Схватил за руки
          imagebutton:
            idle rape.relative_path + "/button_arms_done.png"
            hover rape.relative_path + "/button_arms_done.png"
            focus_mask FocusMaskGirls('arms',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] уже крепко держит руки пленницы в своих лапах{/color}')
            action  [Hide('penetration_sex'),Show('penetration_sex') ]
        

        # Стиль для подсказок
        if rape_tooltip.value != "None":  # Костыль-костылык. Не показываем подсказу если у нее значение по умолчанию
            frame:                      # Делаем небольшой фрейм, чтобы показать подсказку
                background "#202020"
                xpadding 10
                ypadding 5
                xalign 0.95
                yalign 0.01
                text rape_tooltip.value:  # Выводим собственно текст подсказки
                  xalign 0.5
# Второй фрейм, с постоянными подсказками.
            frame:
              background "#202020"
              xpadding 10
              ypadding 5
              xalign 0.03
              yalign 0.01
              xsize  250
              xfill True
#              hbox:
#              text '{font=fonts/AnticvarShadow.ttf}{size=+20}Дракон{/size}{/font}\n{size=+10}%s %s{/size}' % (bloodlust_texts[game.dragon.bloodiness],game.rape.rage):  # Выводим собственно текст подсказки
              text '{font=fonts/AnticvarShadow.ttf}{size=+20}Дракон{/size}{/font}\n{size=+10}%s{/size}' % (bloodlust_texts[game.dragon.bloodiness]):  # Выводим собственно текст подсказки
                xalign 0.5

# Третий  фрейм, с подсказками о девушках.
            frame:
              background "#202020"
              xpadding 10
              ypadding 5
              xalign 0.03
              yalign 0.3
              xsize  250
              xfill True
              text '{font=fonts/AnticvarShadow.ttf}{size=+20}Девушка{/size}{/font}\n%s\n%s' % (game.rape.health_text,game.rape.proud_text):  # Выводим собственно текст подсказки
                xalign 0.5
        if game.rape.erection <4: # сли ещё не кончил, можно вернуться
          hbox: 
            ypos 680
            xpos 1020
            spacing 50
            textbutton _("Попробовать иначе") hovered rape_tooltip.Action('{color=#ff0000}Потом придётся начинать заново...{/color}') action [Function(game.rape.define_freedom),Hide('penetration_sex'),Show('start_sex') ]

# Принуждение
screen bdsm_sex:
    python:
        focus_mask_ext.load_focus_mask_girls(rape.relative_path + '/coordinates.bin')
        if game.rape.rage >= 10 and game.dragon.bloodiness < 1:
          game.rape.game.dragon.gain_rage()
        if game.rape.rage >= 20 and game.dragon.bloodiness < 2:
          game.rape.game.dragon.gain_rage()
        if game.rape.rage >= 30 and game.dragon.bloodiness < 3:
          game.rape.game.dragon.gain_rage()
        if game.rape.rage >= 40 and game.dragon.bloodiness < 4:
          game.rape.game.dragon.gain_rage()
        if game.rape.rage >= 50 and game.dragon.bloodiness < 5:
          game.rape.game.dragon.gain_rage()
# Построение отношений
        ratio_health=game.rape.actual_health/game.rape.full_health
        if ratio_health==1:
          game.rape.health_text=u'{color=#00ff00}Цела и невредима{/color}'
        elif ratio_health<1 and ratio_health>0.66:
          game.rape.health_text=u'{color=#ccccff}Изрядно потрёпана, но непобеждена{/color}'
        elif ratio_health<=0.66 and ratio_health>0.33:
          game.rape.health_text=u'{color=#ff00ff}Может, стоит обратиться к врачу?!{/color}'
        elif ratio_health<=0.33 and ratio_health>0:
          game.rape.health_text=u'{color=#ff0000}Срочно в реанимацию!!!{/color}'
# Поправка на отрицательную гордость
        if game.rape.actual_proud<0:
          game.rape.actual_proud=0
        ratio=game.rape.actual_proud/game.rape.full_proud
        if ratio>0.66:
          game.rape.proud_text=u'{color=#ff0000}Умрёт, но не покорится{/color}'
        elif ratio>0.33 and ratio <=0.66:
          game.rape.proud_text=u'{color=#ff00ff}Яростно отбивается и шипит сквозь стиснутые зубы{/color}'
        elif ratio>0 and ratio <=0.33:
          game.rape.proud_text=u'{color=#ccccff}Заламывает руки и молит о пощаде{/color}'
        elif ratio==0:
          game.rape.proud_text=u'{color=#00ff00}Полностью сломлена и готова на всё{/color}'
    default rape_tooltip = Tooltip("None")  # Подсказка на что сейчас наведена мышка
    fixed:
        fit_first True 
        add rape.relative_path + "/ground.jpg"
        if game.rape.left_breast_possible: # Если левая грудь цела и с ней можно что-то сделать:
          imagebutton:   # Правая грудь
            auto rape.relative_path + "/button_left_breast_%s.png"
            focus_mask FocusMaskGirls('left_breast',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Воздействовать на правую грудь{/color}')
            action [Function(game.rape.set_breast,'left'),Hide('bdsm_sex'),Show('bdsm_breast') ]
        elif not game.rape.left_breast:
          imagebutton:   # Правая грудь
            idle rape.relative_path + "/button_left_breast_done.png"
            hover rape.relative_path + "/button_left_breast_done.png"
            focus_mask FocusMaskGirls('left_breast',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Воздействовать на правую грудь больше нельзя!{/color}')
            action [Hide('bdsm_sex'),Show('bdsm_sex') ]
        else:
          imagebutton:   # Правая грудь
            idle rape.relative_path + "/button_left_breast_idle.png"
            hover rape.relative_path + "/button_left_breast_idle.png"
            focus_mask FocusMaskGirls('left_breast',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] с удовольствием сделал бы что-нибудь с правой грудью пленницы. Вот только нечем...{/color}')
            action [Hide('bdsm_sex'),Show('bdsm_sex') ]

       # Правая грудь
        if game.rape.right_breast_possible: # Если левая грудь цела и с ней можно что-то сделать:
          imagebutton:   # Левая грудь
            auto rape.relative_path + "/button_right_breast_%s.png"
            focus_mask FocusMaskGirls('right_breast',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Воздействовать на левую грудь{/color}')
            action [Function(game.rape.set_breast,'right'),Hide('bdsm_sex'),Show('bdsm_breast') ]
        elif not game.rape.right_breast:
          imagebutton:   # Левая грудь
            idle rape.relative_path + "/button_right_breast_done.png"
            hover rape.relative_path + "/button_right_breast_done.png"
            focus_mask FocusMaskGirls('right_breast',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Воздействовать на левую грудь больше нельзя!{/color}')
            action [Hide('bdsm_sex'),Show('bdsm_sex') ]
        else:
          imagebutton:   # Левая грудь
            idle rape.relative_path + "/button_right_breast_idle.png"
            hover rape.relative_path + "/button_right_breast_idle.png"
            focus_mask FocusMaskGirls('right_breast',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] с удовольствием сделал бы что-нибудь с левой грудью пленницы. Вот только нечем...{/color}')
            action [Hide('bdsm_sex'),Show('bdsm_sex') ]

       # Голова
        if game.rape.head_possible: # Если голова цела и с ней можно что-то сделать:
          imagebutton:   
            auto rape.relative_path + "/button_head_%s.png"
            focus_mask FocusMaskGirls('head',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Воздействовать на голову{/color}')
            action [Hide('bdsm_sex'),Show('bdsm_head') ]
        elif not game.rape.head:
          imagebutton:   
            idle rape.relative_path + "/button_head_done.png"
            hover rape.relative_path + "/button_head_done.png"
            focus_mask FocusMaskGirls('head',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Воздействовать на голову больше нельзя!{/color}')
            action [Hide('bdsm_sex'),Show('bdsm_sex') ]
        else:
          imagebutton:  
            idle rape.relative_path + "/button_head_idle.png"
            hover rape.relative_path + "/button_head_idle.png"
            focus_mask FocusMaskGirls('head',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] с удовольствием сделал бы что-нибудь с головой пленницы. Вот только нечем...{/color}')
            action [Hide('bdsm_sex'),Show('bdsm_sex') ]

       # Живот
        if game.rape.stomach_possible: # Если живот цел и с ним можно что-то сделать:
          imagebutton:   
            auto rape.relative_path + "/button_stomach_%s.png"
            focus_mask FocusMaskGirls('stomach',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Воздействовать на живот{/color}')
            action [Hide('bdsm_sex'),Show('bdsm_stomach') ]
        elif not game.rape.stomach:
          imagebutton:   
            idle rape.relative_path + "/button_stomach_done.png"
            hover rape.relative_path + "/button_stomach_done.png"
            focus_mask FocusMaskGirls('stomach',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Воздействовать на живот больше нельзя!{/color}')
            action [Hide('bdsm_sex'),Show('bdsm_sex') ]
        else:
          imagebutton:  
            idle rape.relative_path + "/button_stomach_idle.png"
            hover rape.relative_path + "/button_stomach_idle.png"
            focus_mask FocusMaskGirls('stomach',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] с удовольствием причинил бы боль животу пленницы. Вот только нечем...{/color}')
            action [Hide('bdsm_sex'),Show('bdsm_sex') ]

       # Лоно
        if game.rape.pussy_possible: # Если лоно цело и с ним можно что-то сделать:
          imagebutton:   
            auto rape.relative_path + "/button_pussy_%s.png"
            focus_mask FocusMaskGirls('pussy',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Причинить боль лону{/color}')
            action [Hide('bdsm_sex'),Show('bdsm_pussy') ]
        elif not game.rape.pussy:
          imagebutton:   
            idle rape.relative_path + "/button_pussy_done.png"
            hover rape.relative_path + "/button_pussy_done.png"
            focus_mask FocusMaskGirls('pussy',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}Причинить боль лону больше нельзя!{/color}')
            action [Hide('bdsm_sex'),Show('bdsm_sex') ]
        else:
          imagebutton:  
            idle rape.relative_path + "/button_pussy_idle.png"
            hover rape.relative_path + "/button_pussy_idle.png"
            focus_mask FocusMaskGirls('pussy',rape.relative_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] с удовольствием причинил бы боль лону пленницы. Вот только нечем...{/color}')
            action [Hide('bdsm_sex'),Show('bdsm_sex') ]        

        # Стиль для подсказок
        if rape_tooltip.value != "None":  # Костыль-костылык. Не показываем подсказу если у нее значение по умолчанию
            frame:                      # Делаем небольшой фрейм, чтобы показать подсказку
                background "#202020"
                xpadding 10
                ypadding 5
                xalign 0.95
                yalign 0.01
                xsize  700
                text rape_tooltip.value:  # Выводим собственно текст подсказки
                  xalign 0.5
# Второй фрейм, с постоянными подсказками.
            frame:
              background "#202020"
              xpadding 10
              ypadding 5
              xalign 0.03
              yalign 0.01
              xsize  250
              xfill True
#              hbox:
              text '{font=fonts/AnticvarShadow.ttf}{size=+20}Дракон{/size}{/font}\n{size=+10}%s{/size}' % (bloodlust_texts[game.dragon.bloodiness]):  # Выводим собственно текст подсказки
                xalign 0.5

# Третий  фрейм, с подсказками о девушках.
            frame:
              background "#202020"
              xpadding 10
              ypadding 5
              xalign 0.03
              yalign 0.3
              xsize  250
              xfill True
#              text '{font=fonts/AnticvarShadow.ttf}{size=+20}Девушка{/size}{/font}\n%s %s %s, %s\n%s' % (game.rape.health_text,game.rape.full_health,game.rape.actual_health,ratio_health,game.rape.proud_text):  # Выводим собственно текст подсказки
              text '{font=fonts/AnticvarShadow.ttf}{size=+20}Девушка{/size}{/font}\n%s\n%s' % (game.rape.health_text,game.rape.proud_text):  # Выводим собственно текст подсказки
                xalign 0.5
#        if game.rape.erection <4: # сли ещё не кончил, можно вернуться
        hbox: 
            ypos 680
            xpos 1020
            spacing 50
            textbutton _("Хватит, пожалуй") hovered rape_tooltip.Action('{color=#ff0000}Прервать сеанс принуждения?{/color}') action [Hide('bdsm_sex'),Show('start_sex') ]

# Левая грудь
# Принуждение
screen bdsm_breast:   # Когти, клыки, огонь, лёд, молнии, яд, жало
    python:
        focus_mask_ext.load_focus_mask_dragons(rape.dragon_path + '/coordinates.bin')
    default rape_tooltip = Tooltip("None")  # Подсказка на что сейчас наведена мышка
    fixed:
        fit_first True 
        add rape.relative_path + "/ground.jpg"
        add rape.dragon_path + "/ground.png" #
        if game.rape.clutches: # Оторвать грудь когтями:
          imagebutton:   
            auto rape.dragon_path + "/button_clutches_%s.png"
            focus_mask FocusMaskDragons('clutches',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Оторвать грудь когтями{/color} (ущерб здоровью - {color=#ff0000}сильный{/color}, влияние на решимость - {color=#0085ff}выше среднего{/color})')
            action [Hide('bdsm_breast'),Jump('lb_bdsm_breast_clutches') ]
        elif game.rape.clutches_used:
          imagebutton:   
            idle rape.dragon_path + "/button_clutches_done.png"
            hover rape.dragon_path + "/button_clutches_done.png"
            focus_mask FocusMaskDragons('clutches',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]
        elif not game.rape.clutches_used and not game.rape.clutches:
          imagebutton:   
            idle rape.dragon_path + "/button_clutches_idle.png"
            hover rape.dragon_path + "/button_clutches_idle.png"
            focus_mask FocusMaskDragons('clutches',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] оторвал бы пленнице грудь - будь у него когти...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]

# Откусить грудь зубами
        if game.rape.fangs: # Откусить грудь клыками:
          imagebutton:   
            auto rape.dragon_path + "/button_fangs_%s.png"
            focus_mask FocusMaskDragons('fangs',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Откусить грудь клыками{/color} (ущерб здоровью - {color=#ff0000}сильный{/color}, влияние на решимость - {color=#0085ff}выше среднего{/color})')
            action [Hide('bdsm_breast'),Jump('lb_bdsm_breast_fangs') ]
        elif game.rape.fangs_used:
          imagebutton:   
            idle rape.dragon_path + "/button_fangs_done.png"
            hover rape.dragon_path + "/button_fangs_done.png"
            focus_mask FocusMaskDragons('fangs',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]
        elif not game.rape.fangs_used and not game.rape.fangs:
          imagebutton:   
            idle rape.dragon_path + "/button_fangs_idle.png"
            hover rape.dragon_path + "/button_fangs_idle.png"
            focus_mask FocusMaskDragons('fangs',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] откусил бы пленнице грудь - будь у него клыки...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]

# Пугать лучше в лицо!
        if game.rape.fear or game.rape.fear_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_fear_idle.png"
            hover rape.dragon_path + "/button_fear_idle.png"
            focus_mask FocusMaskDragons('fear',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] настолько чудовищен, что способен довести пленницу до нервного срыва одним внешним видом. Но пугать лучше, глядя в глаза...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]
        if not game.rape.fear and not game.rape.fear_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_fear_idle.png"
            hover rape.dragon_path + "/button_fear_idle.png"
            focus_mask FocusMaskDragons('fear',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] не настолько настолько чудовищен, чтобы доводить пленниц до нервного срыва одним внешним видом. К тому же пугать лучше, глядя в глаза...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]

# Обжечь грудь огнём
        if game.rape.fire: # Обжечь грудь огнём:
          imagebutton:   
            auto rape.dragon_path + "/button_fire_%s.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Обжечь грудь огнём{/color} (ущерб здоровью - {color=#ff8100}средний{/color}, влияние на решимость - {color=#ff8100}среднее{/color})')
            action [Hide('bdsm_breast'),Jump('lb_bdsm_breast_fire') ]
        elif game.rape.fire_used:
          imagebutton:   
            idle rape.dragon_path + "/button_fire_done.png"
            hover rape.dragon_path + "/button_fire_done.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]
        elif not game.rape.fire_used and not game.rape.fire and not game.girl.type == 'fire':
          imagebutton:   
            idle rape.dragon_path + "/button_fire_idle.png"
            hover rape.dragon_path + "/button_fire_idle.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] обжёг бы пленнице грудь - владей он огнём...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]
        elif game.girl.type == 'fire':
          imagebutton:   
            idle rape.dragon_path + "/button_fire_idle.png"
            hover rape.dragon_path + "/button_fire_idle.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Обжигать грудь ифритши малость бесполезно...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]

# Выкалывать лучше глаза!
        if game.rape.horns or game.rape.horns_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_horns_idle.png"
            hover rape.dragon_path + "/button_horns_idle.png"
            focus_mask FocusMaskDragons('horns',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] заслуженно гордится своими чудовищнымми рогами. Вот только сейчас они бесполезны.{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]
        if not game.rape.horns and not game.rape.horns_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_horns_idle.png"
            hover rape.dragon_path + "/button_horns_idle.png"
            focus_mask FocusMaskDragons('horns',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}У дракона нет рогов. Да они сейчас и не пригодились бы...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]

# Обморозить грудь холодом
        if game.rape.ice: 
          imagebutton:   
            auto rape.dragon_path + "/button_ice_%s.png"
            focus_mask FocusMaskDragons('ice',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Обморозить грудь холодом{/color} (ущерб здоровью - {color=#ff8100}средний{/color}, влияние на решимость - {color=#ff8100}среднее{/color})')
            action [Hide('bdsm_breast'),Jump('lb_bdsm_breast_ice') ]
        elif game.rape.ice_used:
          imagebutton:   
            idle rape.dragon_path + "/button_ice_done.png"
            hover rape.dragon_path + "/button_ice_done.png"
            focus_mask FocusMaskDragons('ice',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]
        elif not game.rape.ice_used and not game.rape.ice and not game.girl.type == 'ice':
          imagebutton:   
            idle rape.dragon_path + "/button_ice_idle.png"
            hover rape.dragon_path + "/button_ice_idle.png"
            focus_mask FocusMaskDragons('ice',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] обморозил бы пленнице грудь - владей он холодом...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]
        elif game.girl.type == 'ice':
          imagebutton:   
            idle rape.dragon_path + "/button_ice_idle.png"
            hover rape.dragon_path + "/button_ice_idle.png"
            focus_mask FocusMaskDragons('ice',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Обмораживать грудь йотунши малость бесполезно...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]

# Дёрнуть грудь электричеством
        if game.rape.lightning: 
          imagebutton:   
            auto rape.dragon_path + "/button_lightning_%s.png"
            focus_mask FocusMaskDragons('lightning',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Ударить грудь молнией{/color} (ущерб здоровью - {color=#0085ff}ниже среднего{/color}, влияние на решимость - {color=#0085ff}выше среднего{/color})')
            action [Hide('bdsm_breast'),Jump('lb_bdsm_breast_lightning') ]
        elif game.rape.lightning_used:
          imagebutton:   
            idle rape.dragon_path + "/button_lightning_done.png"
            hover rape.dragon_path + "/button_lightning_done.png"
            focus_mask FocusMaskDragons('lightning',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]
        elif not game.rape.lightning_used and not game.rape.lightning and not game.girl.type == 'titan':
          imagebutton:   
            idle rape.dragon_path + "/button_lightning_idle.png"
            hover rape.dragon_path + "/button_lightning_idle.png"
            focus_mask FocusMaskDragons('lightning',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] ударил бы пленнице грудь молнией - владей он электричеством...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]
        elif game.girl.type == 'titan':
          imagebutton:   
            idle rape.dragon_path + "/button_lightning_idle.png"
            hover rape.dragon_path + "/button_lightning_idle.png"
            focus_mask FocusMaskDragons('lightning',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Бить молнией в грудь титанши малость бесполезно...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]

# Выдохнуть на грудь облако яда
        if game.rape.poison: 
          imagebutton:   
            auto rape.dragon_path + "/button_poison_%s.png"
            focus_mask FocusMaskDragons('poison',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Выдохнуть облако яда{/color} (ущерб здоровью - {color=#ff8100}средний{/color}, влияние на решимость - {color=#ff8100}среднее{/color})')
            action [Hide('bdsm_breast'),Jump('lb_bdsm_breast_poison') ]
        elif game.rape.poison_used:
          imagebutton:   
            idle rape.dragon_path + "/button_poison_done.png"
            hover rape.dragon_path + "/button_poison_done.png"
            focus_mask FocusMaskDragons('poison',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]
        elif not game.rape.poison_used and not game.rape.poison:
          imagebutton:   
            idle rape.dragon_path + "/button_poison_idle.png"
            hover rape.dragon_path + "/button_poison_idle.png"
            focus_mask FocusMaskDragons('poison',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] выдохнул бы облако яда - обладай он ядовитым дыханием...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]

# Шуметь лучше в уши!
        if game.rape.sound or game.rape.sound_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_sound_idle.png"
            hover rape.dragon_path + "/button_sound_idle.png"
            focus_mask FocusMaskDragons('sound',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Громовой рёв дракона способен раскалывать камни. Вот только рычать лучше в уши..{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]
        if not game.rape.sound and not game.rape.sound_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_sound_idle.png"
            hover rape.dragon_path + "/button_sound_idle.png"
            focus_mask FocusMaskDragons('sound',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}У дракона сравнительно тихий голос. Да громовой рёв сейчас и не пригодился бы...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]

# Вонзить отравленное жало
        if game.rape.string: 
          imagebutton:   
            auto rape.dragon_path + "/button_string_%s.png"
            focus_mask FocusMaskDragons('string',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Вонзить отравленное жало{/color} (ущерб здоровью - {color=#ff0000}сильный{/color}, влияние на решимость - {color=#0085ff}выше среднего{/color})')
            action [Hide('bdsm_breast'),Jump('lb_bdsm_breast_string') ]
        elif game.rape.string_used:
          imagebutton:   
            idle rape.dragon_path + "/button_string_done.png"
            hover rape.dragon_path + "/button_string_done.png"
            focus_mask FocusMaskDragons('string',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]
        elif not game.rape.string_used and not game.rape.string:
          imagebutton:   
            idle rape.dragon_path + "/button_string_idle.png"
            hover rape.dragon_path + "/button_string_idle.png"
            focus_mask FocusMaskDragons('string',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] вонзил бы в грудь отравленное жало - вот только кончик хвоста у него гибкий и мягкий...{/color}')
            action [Hide('bdsm_breast'),Show('bdsm_breast') ]

        # Стиль для подсказок
        if rape_tooltip.value != "None":  # Костыль-костылык. Не показываем подсказу если у нее значение по умолчанию
            frame:                      # Делаем небольшой фрейм, чтобы показать подсказку
                background "#202020"
                xpadding 10
                ypadding 5
                xalign 0.95
                yalign 0.01
                text rape_tooltip.value:  # Выводим собственно текст подсказки
                  xalign 0.5

        hbox: 
            ypos 680
            xpos 1120
            spacing 50
            textbutton _("Не, не так") hovered rape_tooltip.Action('{color=#ff0000}Попробовать что-нибудь иное{/color}') action [Hide('bdsm_breast'),Show('bdsm_sex') ]


# Голова
screen bdsm_head:   # Когти, страх, рога, звук
    python:
        focus_mask_ext.load_focus_mask_dragons(rape.dragon_path + '/coordinates.bin')
    default rape_tooltip = Tooltip("None")  # Подсказка на что сейчас наведена мышка
    fixed:
        fit_first True 
        add rape.relative_path + "/ground.jpg"
        add rape.dragon_path + "/ground.png" #
        if game.rape.clutches and not (game.girl.type == 'afrodita' or game.girl.type == 'danu'): # Выколоть глаза когтями:
          imagebutton:   
            auto rape.dragon_path + "/button_clutches_%s.png"
            focus_mask FocusMaskDragons('clutches',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Выколоть глаза когтями{/color} (ущерб здоровью - {color=#ff0000}сильный{/color}, влияние на решимость - {color=#00ff00}сильное{/color})')
            action [Hide('bdsm_head'),Jump('lb_bdsm_head_clutches') ]
        elif game.rape.clutches_used:
          imagebutton:   
            idle rape.dragon_path + "/button_clutches_done.png"
            hover rape.dragon_path + "/button_clutches_done.png"
            focus_mask FocusMaskDragons('clutches',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]
        elif not game.rape.clutches_used and not game.rape.clutches:
          imagebutton:   
            idle rape.dragon_path + "/button_clutches_idle.png"
            hover rape.dragon_path + "/button_clutches_idle.png"
            focus_mask FocusMaskDragons('clutches',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] выколол бы пленнице глаза - будь у него когти...{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]

# Зубы тут бесполезны
        if game.rape.fangs or game.rape.fangs_used: # Откусить грудь клыками:
          imagebutton:   
            idle rape.dragon_path + "/button_fangs_idle.png"
            hover rape.dragon_path + "/button_fangs_idle.png"
            focus_mask FocusMaskDragons('fangs',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] резко щёлкает зубами перед лицом пленницы. К сожалению, как ещё можно использовать свои роскошные клыки - он не знает.{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]
        elif not game.rape.fangs_used and not game.rape.fangs:
          imagebutton:   
            idle rape.dragon_path + "/button_fangs_idle.png"
            hover rape.dragon_path + "/button_fangs_idle.png"
            focus_mask FocusMaskDragons('fangs',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Зубки у дракона весьма невпечатляющие. Да если бы и было наоборот - как их использовать на голове?!{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]

# Напугать!
        if game.rape.fear: 
          imagebutton:   
            auto rape.dragon_path + "/button_fear_%s.png"
            focus_mask FocusMaskDragons('fear',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Напугать пленницу{/color} (ущерб здоровью - {color=#00ff00}слабый{/color}, влияние на решимость - {color=#00ff00}сильное{/color})')
            action [Hide('bdsm_head'),Jump('lb_bdsm_head_fear')]
        elif game.rape.fear_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_fear_done.png"
            hover rape.dragon_path + "/button_fear_done.png"
            focus_mask FocusMaskDragons('fear',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] несколько в замешаетльстве. Ему кажется, что происходит что-то не то...{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]
        elif not game.rape.fear_used and not game.rape.fear:
          imagebutton:   
            idle rape.dragon_path + "/button_fear_idle.png"
            hover rape.dragon_path + "/button_fear_idle.png"
            focus_mask FocusMaskDragons('fear',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Дракон с удовольствием напугал бы пленницу - но, увы, он не настолько чудовищен...{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]

# Обжигать лицо огнём - небезопасно!
        if game.rape.fire or game.rape.fire_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_fire_idle.png"
            hover rape.dragon_path + "/button_fire_idle.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Лучше не обжигать огнём лицо, а то игрушка и сломаться может!{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]
        elif not game.rape.fire_used and not game.rape.fire and not game.girl.type == 'fire':
          imagebutton:   
            idle rape.dragon_path + "/button_fire_idle.png"
            hover rape.dragon_path + "/button_fire_idle.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] не владеет огнём. Да даже если бы владел, то не стал бы обжигать лицо пленницы - слишком рискованно... {/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]
        elif game.girl.type == 'fire':
          imagebutton:   
            idle rape.dragon_path + "/button_fire_idle.png"
            hover rape.dragon_path + "/button_fire_idle.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Обжигать лицо ифритки малость бесполезно... {/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]

# Выколоть глаза!
        if game.rape.horns and not (game.girl.type == 'afrodita' or game.girl.type == 'danu'): 
          imagebutton:   
            auto rape.dragon_path + "/button_horns_%s.png"
            focus_mask FocusMaskDragons('horns',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Выколоть глаза рогами{/color} (ущерб здоровью - {color=#ff0000}сильный{/color}, влияние на решимость - {color=#00ff00}сильное{/color})')
            action [Hide('bdsm_head'),Jump('lb_bdsm_head_horns') ]
        elif game.rape.horns_used:
          imagebutton:   
            idle rape.dragon_path + "/button_horns_done.png"
            hover rape.dragon_path + "/button_horns_done.png"
            focus_mask FocusMaskDragons('horns',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]
        elif not game.rape.horns_used and not game.rape.horns:
          imagebutton:   
            idle rape.dragon_path + "/button_horns_idle.png"
            hover rape.dragon_path + "/button_horns_idle.png"
            focus_mask FocusMaskDragons('horns',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] выколол бы пленнице глаза - будь у него рога...{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]

# Обморозить лицо холодом - небезопасно!
        if game.rape.ice or game.rape.ice_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_ice_idle.png"
            hover rape.dragon_path + "/button_ice_idle.png"
            focus_mask FocusMaskDragons('ice',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Лучше не обмораживать холодом лицо, а то игрушка и сломаться может!{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]
        elif not game.rape.ice_used and not game.rape.ice:
          imagebutton:   
            idle rape.dragon_path + "/button_ice_idle.png"
            hover rape.dragon_path + "/button_ice_idle.png"
            focus_mask FocusMaskDragons('ice',rape.dragon_path)
            if not game.girl.type == 'ice':
              hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] не владеет холодом. Да даже если бы владел, то не стал бы обмораживать лицо пленницы - слишком рискованно... {/color}')
            else:
              hovered rape_tooltip.Action('{color=#ff0000}Обмораживать лицо йотунши малость бесполезно... {/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]

# Дёргать лицо электричеством - небезопасно!
        if game.rape.lightning or game.rape.lightning_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_lightning_idle.png"
            hover rape.dragon_path + "/button_lightning_idle.png"
            focus_mask FocusMaskDragons('lightning',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Лучше не бить молнией в лицо, а то игрушка и сломаться может!{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]
        elif not game.rape.lightning_used and not game.rape.lightning:
          imagebutton:   
            idle rape.dragon_path + "/button_lightning_idle.png"
            hover rape.dragon_path + "/button_lightning_idle.png"
            focus_mask FocusMaskDragons('lightning',rape.dragon_path)
            if not game.girl.type == 'titan':
              hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] не владеет молнией. Да даже если бы владел, то не стал бы бить ей в лицо пленницы - слишком рискованно... {/color}')
            else:
              hovered rape_tooltip.Action('{color=#ff0000}Бить молнией в лицо титанши малость бесполезно... {/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]

# Выдыхать в лицо облако яда - небезопасно!
        if game.rape.poison or game.rape.poison_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_poison_idle.png"
            hover rape.dragon_path + "/button_poison_idle.png"
            focus_mask FocusMaskDragons('poison',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Лучше не выдыхать облако яда в лицо, а то игрушка и сломаться может!{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]
        elif not game.rape.poison_used and not game.rape.poison:
          imagebutton:   
            idle rape.dragon_path + "/button_poison_idle.png"
            hover rape.dragon_path + "/button_poison_idle.png"
            focus_mask FocusMaskDragons('poison',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] не владеет ядовитым дыханием. Да даже если бы владел, то не стал бы выдыхать яд в лицо пленницы - слишком рискованно... {/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]

# Шуметь в уши!
        if game.rape.sound: 
          imagebutton:   
            auto rape.dragon_path + "/button_sound_%s.png"
            focus_mask FocusMaskDragons('sound',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Напугать пленницу рёвом{/color} (ущерб здоровью - {color=#0085ff}ниже среднего{/color}, влияние на решимость - {color=#ff8100}среднее{/color})')
            action [Hide('bdsm_head'),Jump('lb_bdsm_head_sound') ]
        elif game.rape.sound_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_sound_done.png"
            hover rape.dragon_path + "/button_sound_done.png"
            focus_mask FocusMaskDragons('sound',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]
        if not game.rape.sound and not game.rape.sound_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_sound_idle.png"
            hover rape.dragon_path + "/button_sound_idle.png"
            focus_mask FocusMaskDragons('sound',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}У дракона сравнительно тихий голос. А жаль: напугать пленницу рёвом сейчас не помешало бы!{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]

# Вонзать отравленное жало в глаза - небезопасно
        if game.rape.string or game.rape.string_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_string_idle.png"
            hover rape.dragon_path + "/button_string_idle.png"
            focus_mask FocusMaskDragons('string',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] на секунду задумывается, стоит ли выкалывать жалом глаза. Не, яд мгновенно дойдёт до мозга - и всё, очередная игрушка сломана!{/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]
        elif not game.rape.string_used and not game.rape.string:
          imagebutton:   
            idle rape.dragon_path + "/button_string_idle.png"
            hover rape.dragon_path + "/button_string_idle.png"
            focus_mask FocusMaskDragons('string',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}У дракона очень мягкий и гибкий кончик хвоста. Да даже если бы там было ядовитое жало, [game.dragon.name] дважды подумал бы, прежде чем выкалывать глаза пленнице. {/color}')
            action [Hide('bdsm_head'),Show('bdsm_head') ]

        # Стиль для подсказок
        if rape_tooltip.value != "None":  # Костыль-костылык. Не показываем подсказу если у нее значение по умолчанию
            frame:                      # Делаем небольшой фрейм, чтобы показать подсказку
                background "#202020"
                xpadding 10
                ypadding 5
                xalign 0.95
                yalign 0.01
                text rape_tooltip.value:  # Выводим собственно текст подсказки
                  xalign 0.5

        hbox: 
            ypos 680
            xpos 1120
            spacing 50
            textbutton _("Не, не так") hovered rape_tooltip.Action('{color=#ff0000}Попробовать что-нибудь иное{/color}') action [Hide('bdsm_head'),Show('bdsm_sex') ]



# Живот
screen bdsm_stomach:   # Огонь, лёд, молнии, яд
    python:
        focus_mask_ext.load_focus_mask_dragons(rape.dragon_path + '/coordinates.bin')
    default rape_tooltip = Tooltip("None")  # Подсказка на что сейчас наведена мышка
    fixed:
        fit_first True 
        add rape.relative_path + "/ground.jpg"
        add rape.dragon_path + "/ground.png" #
        if game.rape.clutches or game.rape.clutches_used: # Разодрать живот когтями нельзя:
          imagebutton:   
            idle rape.dragon_path + "/button_clutches_idle.png"
            hover rape.dragon_path + "/button_clutches_idle.png"
            focus_mask FocusMaskDragons('clutches',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] с удовльствием разодрал бы живот пленницы когтями и подзакусил бы её внутренностями - но , увы, пока рано...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]
        elif not game.rape.clutches_used and not game.rape.clutches:
          imagebutton:   
            idle rape.dragon_path + "/button_clutches_idle.png"
            hover rape.dragon_path + "/button_clutches_idle.png"
            focus_mask FocusMaskDragons('clutches',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] с удовльствием разодрал бы живот пленницы когтями и подзакусил бы её внутренностями - но , увы, пока рано... Да и когтей у него нет!{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]

# Укусить живот зубами нельзя!
        if game.rape.fangs or game.rape.fangs_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_fangs_idle.png"
            hover rape.dragon_path + "/button_fangs_idle.png"
            focus_mask FocusMaskDragons('fangs',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] с удовльствием разодрал бы живот пленницы и подзакусил бы её внутренностями - но, увы, пока рано...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]
        elif not game.rape.fangs_used and not game.rape.fangs:
          imagebutton:   
            idle rape.dragon_path + "/button_fangs_idle.png"
            hover rape.dragon_path + "/button_fangs_idle.png"
            focus_mask FocusMaskDragons('fangs',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] с удовльствием разодрал бы живот пленницы и подзакусил бы её внутренностями - но, увы, пока рано... Да и клыки у него невпечатляющие!{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]

# Пугать лучше в лицо!
        if game.rape.fear or game.rape.fear_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_fear_idle.png"
            hover rape.dragon_path + "/button_fear_idle.png"
            focus_mask FocusMaskDragons('fear',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] настолько чудовищен, что способен довести пленницу до нервного срыва одним внешним видом. Но пугать лучше, глядя в глаза...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]
        if not game.rape.fear and not game.rape.fear_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_fear_idle.png"
            hover rape.dragon_path + "/button_fear_idle.png"
            focus_mask FocusMaskDragons('fear',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] не настолько настолько чудовищен, чтобы доводить пленниц до нервного срыва одним внешним видом. К тому же пугать лучше, глядя в глаза...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]

# Обжечь живот огнём
        if game.rape.fire: 
          imagebutton:   
            auto rape.dragon_path + "/button_fire_%s.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Обжечь живот огнём{/color} (ущерб здоровью - {color=#ff8100}средний{/color}, влияние на решимость - {color=#ff8100}среднее{/color})')
            action [Hide('bdsm_stomach'),Jump('lb_bdsm_stomach_fire') ]
        elif game.rape.fire_used:
          imagebutton:   
            idle rape.dragon_path + "/button_fire_done.png"
            hover rape.dragon_path + "/button_fire_done.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]
        elif not game.rape.fire_used and not game.rape.fire and not game.girl.type == 'fire':
          imagebutton:   
            idle rape.dragon_path + "/button_fire_idle.png"
            hover rape.dragon_path + "/button_fire_idle.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] обжёг бы пленнице живот - владей он огнём...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]
        elif game.girl.type == 'fire':
          imagebutton:   
            idle rape.dragon_path + "/button_fire_idle.png"
            hover rape.dragon_path + "/button_fire_idle.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Обжигать живот ифритки малость бесполезно...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]

# Выкалывать лучше глаза!
        if game.rape.horns or game.rape.horns_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_horns_idle.png"
            hover rape.dragon_path + "/button_horns_idle.png"
            focus_mask FocusMaskDragons('horns',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] заслуженно гордится своими чудовищнымми рогами. Вот только сейчас они бесполезны.{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]
        if not game.rape.horns and not game.rape.horns_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_horns_idle.png"
            hover rape.dragon_path + "/button_horns_idle.png"
            focus_mask FocusMaskDragons('horns',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}У дракона нет рогов. Да они сейчас и не пригодились бы...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]

# Обморозить живот холодом
        if game.rape.ice: 
          imagebutton:   
            auto rape.dragon_path + "/button_ice_%s.png"
            focus_mask FocusMaskDragons('ice',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Обморозить живот холодом{/color} (ущерб здоровью - {color=#ff8100}средний{/color}, влияние на решимость - {color=#ff8100}среднее{/color})')
            action [Hide('bdsm_stomach'),Jump('lb_bdsm_stomach_ice') ]
        elif game.rape.ice_used:
          imagebutton:   
            idle rape.dragon_path + "/button_ice_done.png"
            hover rape.dragon_path + "/button_ice_done.png"
            focus_mask FocusMaskDragons('ice',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]
        elif not game.rape.ice_used and not game.rape.ice and not game.girl.type == 'ice':
          imagebutton:   
            idle rape.dragon_path + "/button_ice_idle.png"
            hover rape.dragon_path + "/button_ice_idle.png"
            focus_mask FocusMaskDragons('ice',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] обморозил бы пленнице живот - владей он холодом...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]
        elif game.girl.type == 'ice':
          imagebutton:   
            idle rape.dragon_path + "/button_ice_idle.png"
            hover rape.dragon_path + "/button_ice_idle.png"
            focus_mask FocusMaskDragons('ice',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Обмораживать живот йотунши малость бесполезно...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]

# Дёрнуть живот электричеством
        if game.rape.lightning: 
          imagebutton:   
            auto rape.dragon_path + "/button_lightning_%s.png"
            focus_mask FocusMaskDragons('lightning',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Ударить живот молнией{/color} (ущерб здоровью - {color=#0085ff}ниже среднего{/color}, влияние на решимость - {color=#0085ff}выше среднего{/color})')
            action [Hide('bdsm_stomach'),Jump('lb_bdsm_stomach_lightning') ]
        elif game.rape.lightning_used:
          imagebutton:   
            idle rape.dragon_path + "/button_lightning_done.png"
            hover rape.dragon_path + "/button_lightning_done.png"
            focus_mask FocusMaskDragons('lightning',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]
        elif not game.rape.lightning_used and not game.rape.lightning and not game.girl.type == 'titan':
          imagebutton:   
            idle rape.dragon_path + "/button_lightning_idle.png"
            hover rape.dragon_path + "/button_lightning_idle.png"
            focus_mask FocusMaskDragons('lightning',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] ударил бы пленнице живот молнией - владей он электричеством...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]
        elif game.girl.type == 'titan':
          imagebutton:   
            idle rape.dragon_path + "/button_lightning_idle.png"
            hover rape.dragon_path + "/button_lightning_idle.png"
            focus_mask FocusMaskDragons('lightning',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Бить молнией в живот титанше малость бесполезно...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]

# Выдохнуть на живот облако яда
        if game.rape.poison: 
          imagebutton:   
            auto rape.dragon_path + "/button_poison_%s.png"
            focus_mask FocusMaskDragons('poison',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Выдохнуть облако яда{/color} (ущерб здоровью - {color=#ff00ff}выше среднего{/color}, влияние на решимость - {color=#ff8100}среднее{/color})')
            action [Hide('bdsm_stomach'),Jump('lb_bdsm_stomach_poison') ]
        elif game.rape.poison_used:
          imagebutton:   
            idle rape.dragon_path + "/button_poison_done.png"
            hover rape.dragon_path + "/button_poison_done.png"
            focus_mask FocusMaskDragons('poison',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]
        elif not game.rape.poison_used and not game.rape.poison:
          imagebutton:   
            idle rape.dragon_path + "/button_poison_idle.png"
            hover rape.dragon_path + "/button_poison_idle.png"
            focus_mask FocusMaskDragons('poison',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] выдохнул бы облако яда - обладай он ядовитым дыханием...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]

# Шуметь лучше в уши!
        if game.rape.sound or game.rape.sound_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_sound_idle.png"
            hover rape.dragon_path + "/button_sound_idle.png"
            focus_mask FocusMaskDragons('sound',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Громовой рёв дракона способен раскалывать камни. Вот только рычать лучше в уши..{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]
        if not game.rape.sound and not game.rape.sound_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_sound_idle.png"
            hover rape.dragon_path + "/button_sound_idle.png"
            focus_mask FocusMaskDragons('sound',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}У дракона сравнительно тихий голос. Да громовой рёв сейчас и не пригодился бы...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]

# Вонзать отравленное жало небезопасно!
        if game.rape.string or game.rape.string_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_string_idle.png"
            hover rape.dragon_path + "/button_string_idle.png"
            focus_mask FocusMaskDragons('string',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Вонзать отравленное жало в живот - опасно. Игрушка наверняка сломается!{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach')  ]
        elif not game.rape.string_used and not game.rape.string:
          imagebutton:   
            idle rape.dragon_path + "/button_string_idle.png"
            hover rape.dragon_path + "/button_string_idle.png"
            focus_mask FocusMaskDragons('string',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Вонзать отравленное жало в живот - опасно! Да к тому же у дракона никакого жала и нет...{/color}')
            action [Hide('bdsm_stomach'),Show('bdsm_stomach') ]

        # Стиль для подсказок
        if rape_tooltip.value != "None":  # Костыль-костылык. Не показываем подсказу если у нее значение по умолчанию
            frame:                      # Делаем небольшой фрейм, чтобы показать подсказку
                background "#202020"
                xpadding 10
                ypadding 5
                xalign 0.95
                yalign 0.01
                text rape_tooltip.value:  # Выводим собственно текст подсказки
                  xalign 0.5

        hbox: 
            ypos 680
            xpos 1120
            spacing 50
            textbutton _("Не, не так") hovered rape_tooltip.Action('{color=#ff0000}Попробовать что-нибудь иное{/color}') action [Hide('bdsm_stomach'),Show('bdsm_sex') ]

# Лоно
screen bdsm_pussy:   # Когти, огонь, лёд, молнии, яд, жало
    python:
        focus_mask_ext.load_focus_mask_dragons(rape.dragon_path + '/coordinates.bin')
    default rape_tooltip = Tooltip("None")  # Подсказка на что сейчас наведена мышка
    fixed:
        fit_first True 
        add rape.relative_path + "/ground.jpg"
        add rape.dragon_path + "/ground.png" #
        if game.rape.clutches: # Оторвать клитор когтями:
          imagebutton:   
            auto rape.dragon_path + "/button_clutches_%s.png"
            focus_mask FocusMaskDragons('clutches',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Оторвать клитор когтями{/color} (ущерб здоровью - {color=#ff8100}средний{/color}, влияние на решимость - {color=#0085ff}выше среднего{/color})')
            action [Hide('bdsm_pussy'),Jump('lb_bdsm_pussy_clutches') ]
        elif game.rape.clutches_used:
          imagebutton:   
            idle rape.dragon_path + "/button_clutches_done.png"
            hover rape.dragon_path + "/button_clutches_done.png"
            focus_mask FocusMaskDragons('clutches',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]
        elif not game.rape.clutches_used and not game.rape.clutches:
          imagebutton:   
            idle rape.dragon_path + "/button_clutches_idle.png"
            hover rape.dragon_path + "/button_clutches_idle.png"
            focus_mask FocusMaskDragons('clutches',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] оторвал бы пленнице клитор когтями - будь у него когти...{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]

# Откусывать зубами нечего!
        if game.rape.fangs: 
          imagebutton:   
            idle rape.dragon_path + "/button_fangs_idle.png"
            hover rape.dragon_path + "/button_fangs_idle.png"
            focus_mask FocusMaskDragons('fangs',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] прищёлкивает клыками и озадаченно смотрит на лоно пленницы. Нет, откусывать там явно нечего. {/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]
        elif not game.rape.fangs_used and not game.rape.fangs:
          imagebutton:   
            idle rape.dragon_path + "/button_fangs_idle.png"
            hover rape.dragon_path + "/button_fangs_idle.png"
            focus_mask FocusMaskDragons('fangs',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] озадаченно смотрит на лоно пленницы. Нет, откусывать там явно нечего. Да и клыки у него невпечатляющие!{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]

# Пугать лучше в лицо!
        if game.rape.fear or game.rape.fear_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_fear_idle.png"
            hover rape.dragon_path + "/button_fear_idle.png"
            focus_mask FocusMaskDragons('fear',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] настолько чудовищен, что способен довести пленницу до нервного срыва одним внешним видом. Но пугать лучше, глядя в глаза...{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]
        if not game.rape.fear and not game.rape.fear_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_fear_idle.png"
            hover rape.dragon_path + "/button_fear_idle.png"
            focus_mask FocusMaskDragons('fear',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] не настолько настолько чудовищен, чтобы доводить пленниц до нервного срыва одним внешним видом. К тому же пугать лучше, глядя в глаза...{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]

# Обжечь лоно огнём
        if game.rape.fire: 
          imagebutton:   
            auto rape.dragon_path + "/button_fire_%s.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Обжечь лоно огнём{/color} (ущерб здоровью - {color=#ff8100}средний{/color}, влияние на решимость - {color=#ff8100}среднее{/color})')
            action [Hide('bdsm_pussy'),Jump('lb_bdsm_pussy_fire') ]
        elif game.rape.fire_used:
          imagebutton:   
            idle rape.dragon_path + "/button_fire_done.png"
            hover rape.dragon_path + "/button_fire_done.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]
        elif not game.rape.fire_used and not game.rape.fire:
          imagebutton:   
            idle rape.dragon_path + "/button_fire_idle.png"
            hover rape.dragon_path + "/button_fire_idle.png"
            focus_mask FocusMaskDragons('fire',rape.dragon_path)
            if not game.girl.type == 'fire':
              hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] обжёг бы пленнице грудь - владей он огнём...{/color}')
            else:
              hovered rape_tooltip.Action('{color=#ff0000}Обжигать лоно ифритши малость бесполезно...{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]

# Выкалывать лучше глаза!
        if game.rape.horns or game.rape.horns_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_horns_idle.png"
            hover rape.dragon_path + "/button_horns_idle.png"
            focus_mask FocusMaskDragons('horns',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] заслуженно гордится своими чудовищнымми рогами. Вот только сейчас они бесполезны.{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]
        if not game.rape.horns and not game.rape.horns_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_horns_idle.png"
            hover rape.dragon_path + "/button_horns_idle.png"
            focus_mask FocusMaskDragons('horns',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}У дракона нет рогов. Да они сейчас и не пригодились бы...{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]

# Обморозить лоно холодом
        if game.rape.ice: 
          imagebutton:   
            auto rape.dragon_path + "/button_ice_%s.png"
            focus_mask FocusMaskDragons('ice',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Обморозить лоно холодом{/color} (ущерб здоровью - {color=#ff8100}средний{/color}, влияние на решимость - {color=#ff8100}среднее{/color})')
            action [Hide('bdsm_pussy'),Jump('lb_bdsm_pussy_ice') ]
        elif game.rape.ice_used:
          imagebutton:   
            idle rape.dragon_path + "/button_ice_done.png"
            hover rape.dragon_path + "/button_ice_done.png"
            focus_mask FocusMaskDragons('ice',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]
        elif not game.rape.ice_used and not game.rape.ice:
          imagebutton:   
            idle rape.dragon_path + "/button_ice_idle.png"
            hover rape.dragon_path + "/button_ice_idle.png"
            focus_mask FocusMaskDragons('ice',rape.dragon_path)
            if not game.girl.type == 'ice':
              hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] обморозил бы пленнице лоно - владей он холодом...{/color}')
            else:
              hovered rape_tooltip.Action('{color=#ff0000}Обмораживать лоно йотунши малость бесполезно...{/color}')              
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]

# Дёрнуть грудь электричеством
        if game.rape.lightning: 
          imagebutton:   
            auto rape.dragon_path + "/button_lightning_%s.png"
            focus_mask FocusMaskDragons('lightning',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Ударить лоно молнией{/color} (ущерб здоровью - {color=#0085ff}ниже среднего{/color}, влияние на решимость - {color=#0085ff}выше среднего{/color})')
            action [Hide('bdsm_pussy'),Jump('lb_bdsm_pussy_lightning') ]
        elif game.rape.lightning_used:
          imagebutton:   
            idle rape.dragon_path + "/button_lightning_done.png"
            hover rape.dragon_path + "/button_lightning_done.png"
            focus_mask FocusMaskDragons('lightning',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]
        elif not game.rape.lightning_used and not game.rape.lightning:
          imagebutton:   
            idle rape.dragon_path + "/button_lightning_idle.png"
            hover rape.dragon_path + "/button_lightning_idle.png"
            focus_mask FocusMaskDragons('lightning',rape.dragon_path)
            if not game.girl.type == 'titan':
              hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] ударил бы пленнице лоно молнией - владей он электричеством...{/color}')
            else:
              hovered rape_tooltip.Action('{color=#ff0000}Бить молнией в лоно титанши малость бесполезно...{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]

# Выдохнуть на грудь облако яда
        if game.rape.poison: 
          imagebutton:   
            auto rape.dragon_path + "/button_poison_%s.png"
            focus_mask FocusMaskDragons('poison',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Выдохнуть облако яда{/color} (ущерб здоровью - {color=#ff8100}средний{/color}, влияние на решимость - {color=#ff8100}среднее{/color})')
            action [Hide('bdsm_pussy'),Jump('lb_bdsm_pussy_poison') ]
        elif game.rape.poison_used:
          imagebutton:   
            idle rape.dragon_path + "/button_poison_done.png"
            hover rape.dragon_path + "/button_poison_done.png"
            focus_mask FocusMaskDragons('poison',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]
        elif not game.rape.poison_used and not game.rape.poison:
          imagebutton:   
            idle rape.dragon_path + "/button_poison_idle.png"
            hover rape.dragon_path + "/button_poison_idle.png"
            focus_mask FocusMaskDragons('poison',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] выдохнул бы облако яда - обладай он ядовитым дыханием...{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]

# Шуметь лучше в уши!
        if game.rape.sound or game.rape.sound_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_sound_idle.png"
            hover rape.dragon_path + "/button_sound_idle.png"
            focus_mask FocusMaskDragons('sound',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Громовой рёв дракона способен раскалывать камни. Вот только рычать лучше в уши..{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]
        if not game.rape.sound and not game.rape.sound_used: 
          imagebutton:   
            idle rape.dragon_path + "/button_sound_idle.png"
            hover rape.dragon_path + "/button_sound_idle.png"
            focus_mask FocusMaskDragons('sound',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}У дракона сравнительно тихий голос. Да громовой рёв сейчас и не пригодился бы...{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]

# Вонзить отравленное жало
        if game.rape.string: 
          imagebutton:   
            auto rape.dragon_path + "/button_string_%s.png"
            focus_mask FocusMaskDragons('string',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Вонзить в клитор отравленное жало{/color} (ущерб здоровью - {color=#ff00ff}выше среднего{/color}, влияние на решимость - {color=#0085ff}выше среднего{/color})')
            action [Hide('bdsm_pussy'),Jump('lb_bdsm_pussy_string') ]
        elif game.rape.string_used:
          imagebutton:   
            idle rape.dragon_path + "/button_string_done.png"
            hover rape.dragon_path + "/button_string_done.png"
            focus_mask FocusMaskDragons('string',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}Использовать один и тот же приём дважды - неспортивно!{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]
        elif not game.rape.string_used and not game.rape.string:
          imagebutton:   
            idle rape.dragon_path + "/button_string_idle.png"
            hover rape.dragon_path + "/button_string_idle.png"
            focus_mask FocusMaskDragons('string',rape.dragon_path)
            hovered rape_tooltip.Action('{color=#ff0000}[game.dragon.name] вонзил бы в клитор отравленное жало - вот только кончик хвоста у него гибкий и мягкий...{/color}')
            action [Hide('bdsm_pussy'),Show('bdsm_pussy') ]

        # Стиль для подсказок
        if rape_tooltip.value != "None":  # Костыль-костылык. Не показываем подсказу если у нее значение по умолчанию
            frame:                      # Делаем небольшой фрейм, чтобы показать подсказку
                background "#202020"
                xpadding 10
                ypadding 5
                xalign 0.95
                yalign 0.01
                text rape_tooltip.value:  # Выводим собственно текст подсказки
                  xalign 0.5

        hbox: 
            ypos 680
            xpos 1120
            spacing 50
            textbutton _("Не, не так") hovered rape_tooltip.Action('{color=#ff0000}Попробовать что-нибудь иное{/color}') action [Hide('bdsm_pussy'),Show('bdsm_sex') ]

