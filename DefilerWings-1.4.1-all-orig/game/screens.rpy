# coding=utf-8
# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    use sc_dialog(who, game.currentCharacter.avatar, what)
    use status_bar
    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.3
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:
                if action:
                    button:
                        action action
                        style "menu_choice_button"
                        text caption style "menu_choice"
                else:
                    text caption style "menu_caption"

    use status_bar

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)

    python:
        style.menu_choice_button.background = Frame("img/bg/button-idle.png", 5, 5)
        style.menu_choice_button.hover_background = Frame("img/bg/button-hovered.png", 5, 5)
        style.menu_choice_button.ypadding = 4


##############################################################################
# DF_Choice
#
# Custom screen that's used to display in-game menus.
#
# На вход экрану подается список из опций выбора, со следущем синтаксисом.
# (caption, value, visible=True, condition=True)
# где:
#   caption - текст опции
#   value - возвращаемое значение при выборе этой опции
#   visible - условие при котором опция видна, по-умолчанию True
#   condition - условие при котором опция доступна для выбора, по-умолчанию True
# Пример листа:
#  [("Пункт 1", 1, True, False), - Видимый, но недоступный для выбора пункт
#   ("Пункт 2", 2, persistent.punkt2_visible) - пункт показываестя только если ранее
#       переменная persistent.punkt2_visible была выставлена в True
#   ("Пункт 3", 3, persistent.punkt3_visible, energy > 10)] - тоже самое что пункт2 + можно выбрать только
#       при значении energy > 10
screen dw_choice(items):
    window:
        style "menu_window"
        xalign 0.3
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, value, visible, condition in items:
                if visible and condition:
                    button:
                        action Return(value)
                        style "menu_choice_button"
                        text caption style "menu_choice"
                if visible and not condition:
                    button:
                        action NullAction()
                        style "menu_choice_button"
                        text caption style "menu_choice_inactive"
    use status_bar

init python:
    # Наследуем дефолтный стиль для текста
    style.menu_choice_inactive = Style("menu_choice")
    # И делаем текст серым, чтобы показать его недоступность
    style.menu_choice_inactive.color = "#C0C0C0"

##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"
        xpos 200
        xsize 760
        align(0.0, 0.0)

        viewport:
            mousewheel True
            scrollbars "vertical"
            yinitial 1.0

            has vbox:
                style "nvl_vbox"

            # Display dialogue.
            for who, what, who_id, what_id, window_id in dialogue:
                window:
                    id window_id
                    has hbox:
                        spacing 10
                    if who is not None:
                        text who id who_id
                    text what id what_id

            # Display a menu, if given.
            if items:
                vbox:
                    id "menu"
                    for caption, action, chosen in items:
                        if action:
                            button:
                                style "nvl_menu_choice_button"
                                action action
                                text caption style "nvl_menu_choice"
                        else:
                            text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use status_bar
    use quick_menu
    use sc_avatar

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .966
        yalign .89
        xmaximum 200

        # has vbox
        if not renpy.can_load("1-1"):
            textbutton _("Начать сюжет") action Start():
                xalign .966
                yalign .465
        else:
            textbutton _("Продолжить сюжет") action FileLoad("1", confirm=False, page="1"):
                xalign .966
                yalign .465
        if not persistent.allow_freeplay and not config.developer:
            textbutton _("Достижения") action Show("sc_achievements_choose"):
                xalign .966
                yalign .580
        elif not renpy.can_load("1-3"):
            textbutton _("Свободная игра") action SetVariable("freeplay", True), Start():
                    xalign .966
                    yalign .580
        else:
            textbutton _("Продолжить свободную")action FileLoad("3", confirm=False, page="1"):
                xalign .966
                yalign .580
        textbutton _("Настройки") action ShowMenu("preferences"):
            xalign .966
            yalign .695
        if not persistent.allow_freeplay and not config.developer:
            textbutton _("Помощь") action Help():
                xalign .966
                yalign .81
        if persistent.allow_freeplay:
#            textbutton _("Достижения") action Show("sc_achievements_list"):
            textbutton _("Достижения") action Show("sc_achievements_choose"):
                xalign .966
                yalign .81
        textbutton _("Выход") action Quit(confirm=False):
            xalign .966
            yalign .925
    frame:
        style_group "mm"
        xalign .03
        yalign .95
#        imagebutton auto "img/menu/paypal_%s.png" xalign .03 yalign .95 xsize 60 ysize 40 action Help("page.html")
#        imagebutton auto "img/menu/yandex_%s.png" xalign .03 yalign .88 xsize 60 ysize 40 action OpenURL("https://money.yandex.ru/embed/donate.xml?account=41001501798872&quickpay=donate&default-sum=&targets=%D0%9A%D1%80%D1%8B%D0%BB%D1%8C%D1%8F+%D0%9E%D1%81%D0%BA%D0%B2%D0%B5%D1%80%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8F&project-name=%D0%9A%D1%80%D1%8B%D0%BB%D1%8C%D1%8F+%D0%9E%D1%81%D0%BA%D0%B2%D0%B5%D1%80%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8F&project-site=http%3A%2F%2Foldhuntergames.blogspot.ru%2F&button-text=01&successURL=")

    # text "{font=fonts/Lombardina.ttf}Крылья":
        # xalign 0.94
        # yalign 0.11
        # text_align 1
        # size 90
        # bold False
        # color "#607080"
    # text "{font=fonts/Lombardina.ttf}Осквернителя":
        # xalign 0.95
        # yalign 0.22
        # text_align 1
        # size 60
        # bold False
        # color "#607080"
    text "{font=fonts/PFMonumentaPro-Regular.ttf}Версия: %s" % config.version:
        xalign 0.96
        yalign 0.29
        text_align 0.5
        size 14
        bold False
        color "#241511"

init -2 python:
    style.mm_button.size_group = "mm"

init python:
    style.mm_button.background = Frame("img/menu/button/idle.png", 10, 10)
    style.mm_button.hover_background = Frame("img/menu/button/hover.png", 10, 10)
    style.mm_button.selected_background = Frame("img/menu/button/selected.png", 10, 10)
    style.mm_button.selected_hover_background = Frame("img/menu/button/selected.png", 10, 10)
    style.mm_frame.background = None

    style.mm_button_text.size = 22
    style.mm_button_text.font = "fonts/PFMonumentaPro-Regular.ttf"

    style.mm_button.ysize = 70
    style.mm_button.xsize = 280

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:
    # The various buttons.
    frame:
        style_group "gmnav"
        xpos 855

        has vbox

        textbutton _("Обратно") ypos 275 action Return()
#        textbutton _("Настройки") ypos 285 action ShowMenu("preferences")
        textbutton _("Сохранить игру") ypos 285 action SensitiveIf('game' in globals() and not save_blocked), Hide("preferences"),Jump('lb_save_game')  #ShowMenu("save")
        textbutton _("Загрузить игру") ypos 295 action SensitiveIf(not save_blocked), ShowMenu("load")
        textbutton _("Главное меню") ypos 305 action MainMenu()
#        textbutton _("От автора") ypos 315 action Help()
        textbutton _("Выйти из игры") ypos 315 action Quit()

init -2 python:
    style.gmnav_frame.background = None
    style.gmnav_button.background = Frame("img/menu/button/idle.png",10,10)
    style.gmnav_button.hover_background = Frame("img/menu/button/hover.png",10,10)
    style.gmnav_button.selected_background = Frame("img/menu/button/selected.png",10,10)
    style.gmnav_button.xsize = 300
    style.gmnav_button.ysize = 60
    style.gmnav_button_text.size = 20
    style.gmnav_button_text.font = "fonts/PFMonumentaPro-Regular.ttf"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker:
    #add "img/menu/gmenu2.jpg"
    use navigation
    frame:
        style "file_picker_frame"

        has vbox

        $ columns = 2
        $ rows = 2

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu
    add "img/menu/gmenu.jpg"
    # Include the navigation.
    use navigation
    
    frame:
        style_group "pref"
        has vbox
        textbutton _("Полный экран") xpos 120 ypos 140 action Preference('display', 'fullscreen')
        textbutton _("В окне") xpos 280 ypos 80 action Preference('display', 'window')
    frame:
        style_group "pref"
        has vbox
        textbutton _("Увиденное") xpos 490 ypos 140 action Preference('skip', 'seen')
        textbutton _("Все") xpos 650 ypos 80 action Preference('skip', 'all')
        textbutton _("Начать пропуск") xpos 490 ypos 140 xsize 300 ysize 40 action Preference('begin skipping')
    frame:
        style_group "pref"
        has vbox
        textbutton _("Все") xpos 120 ypos 300 action Preference("transitions", "all")
        textbutton _("Ничего") xpos 280 ypos 240 action Preference("transitions", "none")
    frame:
        style_group "pref"
        has vbox
        textbutton _("Продолжить пропуск") xpos 490 ypos 400 action Preference('after choices', 'skip')
        textbutton _("Закончить пропуск") xpos 650 ypos 340 action Preference('after choices', 'stop')
    frame:
        style_group "pref"
        has vbox
        textbutton _("Сюжет") xpos 120 ypos 540 action SensitiveIf(renpy.can_load("1-1")), Show("yesno_prompt",
                                                                                      yes_action=FileDelete("1", confirm=False, page="1"), no_action=NullAction(),
                                                                                      message="Вы уверены что хотите удалить Сюжетную Игру?")
        textbutton _("Свобод") xpos 280 ypos 480 action SensitiveIf(renpy.can_load("1-3")), Show("yesno_prompt",
                                                                                      yes_action=FileDelete("3", confirm=False, page="1"), no_action=NullAction(),
                                                                                      message="Вы уверены что хотите удалить Свободную Игру?")
    
    frame xpos 858 ypos 132:
        style_group "pref"
        has vbox
        bar value Preference("music volume")
    frame xpos 858 ypos 220:
        style_group "pref"
        has vbox
        bar value Preference("sound volume")
    frame xpos 123 ypos 455:
        style_group "pref"
        has vbox
        bar value Preference("text speed")
    frame xpos 488 ypos 540:
        style_group "pref"
        has vbox
        bar value Preference("auto-forward time")
        
    # Put the navigation columns in a three-wide grid.

init -2 python:
    style.pref_frame.background = None
    style.pref_slider.left_bar = "img/menu/bar_hover.png"
    style.pref_slider.right_bar = "img/menu/bar_empty.png"
    #style.pref_slider.hover_left_bar = "img/menu/bar_hover.png"
    style.pref_slider.thumb = "img/menu/tumb.png"
    style.pref_slider.xmaximum = 300
    style.pref_slider.ymaximum = 14
    
    style.pref_button.background = Frame("img/menu/button/idle.png",10,10)
    style.pref_button.hover_background = Frame("img/menu/button/hover.png",10,10)
    style.pref_button.selected_background = Frame("img/menu/button/selected.png",10,10)
    style.pref_button.xsize = 140
    style.pref_button.ysize = 60
    style.pref_button_text.size = 14
    style.pref_button_text.font = "fonts/PFMonumentaPro-Regular.ttf"


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    # modal True
    
    tag menu
    
    add "img/menu/quit.jpeg"
    
    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            if message == layout.QUIT and not main_menu and not save_blocked:
                if not freeplay:
                    textbutton _("Да") action yes_action #FileSave("1", confirm=False, page="1"), yes_action
                    textbutton _("Нет") action no_action, Hide("yesno_prompt")
                else:
                    textbutton _("Да") action yes_action #FileSave("3", confirm=False, page="1"), yes_action
                    textbutton _("Нет") action no_action, Hide("yesno_prompt")
            elif message == layout.MAIN_MENU and not save_blocked:
                if not freeplay:
                    textbutton _("Да") action yes_action #FileSave("1", confirm=False, page="1"), yes_action
                    textbutton _("Нет") action no_action, Hide("yesno_prompt"), ShowMenu("navigation")
                else:
                    textbutton _("Да") action yes_action #FileSave("3", confirm=False, page="1"), yes_action
                    textbutton _("Нет") action no_action, Hide("yesno_prompt"), ShowMenu("navigation")
            elif message == "Вы уверены что хотите удалить Сюжетную Игру?":
                textbutton _("Да") action yes_action, Hide("yesno_prompt"), ShowMenu("preferences")
                textbutton _("Нет") action no_action, Hide("yesno_prompt"), ShowMenu("preferences")
            elif message == "Вы уверены что хотите удалить Свободную Игру?":
                textbutton _("Да") action yes_action, Hide("yesno_prompt"), ShowMenu("preferences")
                textbutton _("Нет") action no_action, Hide("yesno_prompt"), ShowMenu("preferences")
            elif message == layout.LOADING:
                textbutton _("Загрузить") action yes_action
                textbutton _("Нет") action no_action, ShowMenu("preferences")
            else:
                textbutton _("Наверное") action yes_action
                textbutton _("Нет") action no_action, ShowMenu("preferences")

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2 python:
    style.yesno_frame.background = None
    style.yesno_button.background = Frame("img/menu/button/idle.png",10,10)
    style.yesno_button.hover_background = Frame("img/menu/button/hover.png",10,10)
    style.yesno_button.selected_background = Frame("img/menu/button/selected.png",10,10)
    style.yesno_button.xsize = 140
    style.yesno_button.ysize = 60
    style.yesno_button_text.size = 20
    style.yesno_button_text.font = "fonts/PFMonumentaPro-Regular.ttf"

init -2:
    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Назад") action Rollback()
        # textbutton _("Сохранить") action ShowMenu('save')
        # textbutton _("Б.сохранение") action QuickSave()
        textbutton _("Б.загрузка") action QuickLoad()
        textbutton _("пропуск") action Skip()
        textbutton _("Б.пропуск") action Skip(fast=True, confirm=True)
        textbutton _("Авто") action Preference("auto-forward", "toggle")
        textbutton _("Настройки") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

##############################################################################
# Menu for girls in prison
init python:
        girls_rows = 3
        girls_cols = 4
        girls_cells = girls_rows * girls_cols
        girl_page = 0
        dragon_page=0
        treasury_page=0
        death_page=0
        live_page=0
        girl_position_priority = (
            6, 7, 8, 9,
            5, 0, 1, 10,
            4, 3, 2, 11
        )
screen girls_menu:

    # This ensures that any other menu screen is replaced.
    tag menu
    default girl_tooltip = Tooltip("None")  # Подсказка на что сейчас наведена мышка
    frame background "img/scene/prison.jpg":
        if girl_page * girls_cells > game.girls_list.prisoners_count:
            $ girl_page = 0
        $ next_girl_page = girl_page + 1
        $ prev_girl_page = girl_page - 1
        $ position_i = -1

        for row_i in xrange(girls_rows):
            grid girls_cols 1:
                spacing 50
                ypos row_i * 230
                xsize 200
                for col_i in xrange(girls_cols):
                    $ position_i += 1
                    $ girl_i = girl_page * girls_cells + girl_position_priority[position_i]
                    if girl_i < game.girls_list.prisoners_count:
                      imagebutton:
                          idle Image(im.Grayscale(game.girls_list.prisoners[girl_i].avatar)) 
                          hover game.girls_list.prisoners[girl_i].avatar 
                          hovered girl_tooltip.Action(game.girls_list.girl_in_lair(girl_i))
                          action[Function(game.girls_list.set_active, girl_i), Jump('lb_lair_sex')]
                    else:
                        null

        hbox:
            ypos 680
            xpos 60
            spacing 50
            if girl_page > 0:
                textbutton _("Предыдущая страница") action[SetVariable('girl_page', prev_girl_page), Show("girls_menu")]
            else:
                textbutton _("Предыдущая страница") action None
            textbutton _("Вернуться") action Jump('lb_location_lair_main')
            if next_girl_page * girls_cells < game.girls_list.prisoners_count:
                textbutton _("Следующая страница") action[SetVariable('girl_page', next_girl_page), Show("girls_menu")]
            else:
                textbutton _("Следующая страница") action None
        # Стиль для подсказок
        if girl_tooltip.value != "None":  # Костыль-костылык. Не показываем подсказу если у нее значение по умолчанию
            frame:                      # Делаем небольшой фрейм, чтобы показать подсказку
                background "#202020"
                xpadding 10
                ypadding 5
                xalign 0.5
                yalign 0.01
                text girl_tooltip.value:  # Выводим собственно текст подсказки
                  xalign 0.5



screen girl_chronik_menu:
    python:
        girls_rows = 8
        girls_cols = 1
        girls_cells = girls_rows * girls_cols

    tag menu

    frame background "img/scene/memory_of_girl.jpg":
        if girl_page * girls_cells > game.chronik.chronik_girl_count:
            $ girl_page = 0

        $ next_girl_page = girl_page + 1
        $ prev_girl_page = girl_page - 1
#        $ position_i = -1
#        has vbox
        for col_i in xrange(girls_cols):
          grid 1 girls_rows:
            spacing 30
            ypos 20
            xpos 30

            for row_i in xrange(girls_rows):
              if not game.chronik.chronik_girl_name[game.chronik.active_dragon] == []:   
                $ girl_i= row_i+col_i*girls_rows+girls_cells*girl_page
                if girl_i<game.chronik.chronik_girl_count:
                  $ game.chronik.set_active_girl_botton(girl_i)
                  $ bot_desc = game.chronik.botton_description()
                  textbutton (bot_desc) xsize (600) action[Function(game.chronik.set_active_girl, girl_i), Jump('lb_chronical_description')]
#                  textbutton (bot_desc) action[ Jump('lb_chronical_description')]
                else:
                  null
              else:
                null 
            
        hbox: 
            ypos 680
            xpos 60
            spacing 50
            if girl_page > 0:
                textbutton _("Предыдущая страница") action[SetVariable('girl_page', prev_girl_page), Show("girl_chronik_menu")]
            else:
                textbutton _("Предыдущая страница") action None
#            textbutton _("Вернуться") action Return()
            textbutton _("Вернуться") action [Show("dragon_chronik_menu")]
            if next_girl_page * girls_cells < game.chronik.chronik_girl_count:
                textbutton _("Следующая страница") action[SetVariable('girl_page', next_girl_page), Show("girl_chronik_menu")]
            else:
                textbutton _("Следующая страница") action None
#        return()

screen dragon_chronik_menu:
    python:
        dragon_rows = 8
        dragon_cols = 1
        dragon_cells = dragon_rows * dragon_cols
#        
    tag menu

    frame background "img/scene/memory_of_dragon.jpg":
        if dragon_page * dragon_cells > game.chronik.chronik_dragon_count:
            $ dragon_page = 0

        $ next_dragon_page = dragon_page + 1
        $ prev_dragon_page = dragon_page - 1
        grid 1 dragon_rows:
            spacing 10
            ypos 10
            xpos 0
            for row_i in xrange(dragon_rows):
              $ dragon_i= row_i+dragon_cells*dragon_page
              if dragon_i<game.dragon.level:
#        for grid_i in xrange(len(game.chronik.chronik_dragon)):
#            $ dragon_i=grid_i
                $ game.chronik.set_active_dragon_botton(dragon_i)
                $ bot_desc = game.chronik.botton_dragon_description()
                textbutton (bot_desc) xsize (675) action[Function(game.chronik.set_active_dragon, dragon_i), Show("girl_chronik_menu")]
              else:
                null
#            textbutton (bot_desc) action[SetVariable('dragon_lev', dragon_i), Show("girl_chronik_menu")]
        hbox: 
            ypos 680
            xpos 60
            spacing 50
            if dragon_page > 0:
                textbutton _("Предыдущая страница") action[SetVariable('dragon_page', prev_dragon_page), Show("dragon_chronik_menu")]
            else:
                textbutton _("Предыдущая страница") action None
            if game.chronik.tot_live>0:
              textbutton _("{color=#ff0000}Живые{/color}") action Show("live_menu")
            else:
              textbutton _("{color=#ff0000}Живые{/color}") action None
            textbutton _("Вернуться") action [Jump('lb_location_lair_main') ]
            if game.chronik.tot_dead>0:
              textbutton _("{color=#173B0B}Мёртвые{/color}") action Show("death_menu")
            else:
              textbutton _("{color=#173B0B}Мёртвые{/color}") action None
            if next_dragon_page * dragon_cells < game.chronik.chronik_dragon_count:
                textbutton _("Следующая страница") action[SetVariable('dragon_page', next_dragon_page), Show("dragon_chronik_menu")]
            else:
                textbutton _("Следующая страница") action None
#        return()

screen order_treasury_item(cost=0,gift_mod=False):
    python:
        treasury_rows = 8
        treasury_cols = 1
        treasury_cells = treasury_rows * treasury_cols
#        
    tag menu

    frame background "img/bg/hoard/Smaug.jpg":
        if treasury_page * treasury_cells > len(game.chronik.list_of_treasures[game.chronik.active_treasure_type]):
            $ treasury_page = 0

        $ next_treasury_page = treasury_page + 1
        $ prev_treasury_page = treasury_page - 1
        grid 1 treasury_rows:
            spacing 10
            ypos 10
            xpos 300
            for row_i in xrange(treasury_rows):
              $ treasury_i= row_i+treasury_cells*treasury_page
              if treasury_i<len(game.chronik.list_of_treasures[game.chronik.active_treasure_type]):
                $ bot_desc = treasures.capitalize_first(game.chronik.list_of_treasures[game.chronik.active_treasure_type][treasury_i].description())
                textbutton (bot_desc) xsize (675) action[Function(game.chronik.set_active_treasure, treasury_i, cost,gift_mod), Jump('lb_treasure_description')]
              else:
                null
        hbox: 
            ypos 680
            xpos 60
            spacing 50
            if treasury_page > 0:
                textbutton _("Предыдущая страница") action[SetVariable('treasury_page', prev_treasury_page), Show("order_treasury_item",cost=cost,gift_mod=gift_mod)]
            else:
                textbutton _("Предыдущая страница") action None
            textbutton _("Вернуться") action [Show('order_treasury',cost=cost,gift_mod=gift_mod) ]
            if next_treasury_page * treasury_cells < len(game.chronik.list_of_treasures[game.chronik.active_treasure_type]):
                textbutton _("Следующая страница") action[SetVariable('treasury_page', next_treasury_page), Show("order_treasury_item",cost=cost,gift_mod=gift_mod)]
            else:
                textbutton _("Следующая страница") action None

screen order_treasury(cost=0,gift_mod=False):
    python:
        treasury_rows = 15
        treasury_cols = 1
        treasury_cells = treasury_rows * treasury_cols
#        
    tag menu

    frame background "img/bg/hoard/Smaug.jpg":
        $ game.chronik.list_of_types(cost=cost)
        if treasury_page * treasury_cells > len(game.chronik.list_of_types_of_treasures):
            $ treasury_page = 0

        $ next_treasury_page = treasury_page + 1
        $ prev_treasury_page = treasury_page - 1
        grid 1 treasury_rows:
            spacing 10
            ypos 10
            xpos 300
            for row_i in xrange(treasury_rows):
              $ type_i= row_i+treasury_cells*treasury_page
              if type_i<len(game.chronik.list_of_types_of_treasures):
                $ bot_desc = game.chronik.list_of_types_of_treasures[type_i]
                textbutton (bot_desc) xsize (675) action[Function(game.chronik.set_active_treasure_type, type_i), Show("order_treasury_item",cost=cost,gift_mod=gift_mod)]
              else:
                null
        hbox: 
            ypos 680
            xpos 60
            spacing 50
            if treasury_page > 0:
                textbutton _("Предыдущая страница") action[SetVariable('treasury_page', prev_treasury_page), Show("order_treasury",cost=cost,gift_mod=gift_mod)]
            else:
                textbutton _("Предыдущая страница") action None
            if not gift_mod:
              textbutton _("Вернуться") action [Jump('lb_location_lair_main') ]
            else:
              textbutton _("Обойдётся без подарка") action [Jump('lb_talk_gift') ]
            if next_treasury_page * treasury_cells < len(game.chronik.list_of_treasures):
                textbutton _("Следующая страница") action[SetVariable('treasury_page', next_treasury_page), Show("order_treasury",cost=cost,gift_mod=gift_mod)]
            else:
                textbutton _("Следующая страница") action None

screen scroll_chronik_menu:
    python:
        scroll_rows = 10
        scroll_cols = 10
        scroll_cells = scroll_rows * scroll_cols
        scroll_page=0
    tag menu
    frame background "img/bg/special/scroll.jpg":
        for row_i in xrange(scroll_rows):
            grid scroll_cols 1:
              spacing 50
              ypos row_i * 100
              xsize 200
              for col_i in xrange(scroll_cols):
                $ scroll_i= row_i+col_i*scroll_rows  #+girls_cells*girl_page
                if scroll_i<=game.chronik.chronik_centuary_number:
                  $ bot_desc = game.chronik.chronik_century[scroll_i]
                  textbutton (bot_desc) xsize (200) action[Function(game.chronik.set_active_centure, scroll_i),Jump('lb_chronical_scroll_description')]
                else:
                  null
                  
        hbox: 
            ypos 680
            xpos 60
            spacing 50
            textbutton _("Вернуться") action [Jump('lb_location_lair_main') ]
 #           textbutton _("Вернуться") action Return()
 
screen death_menu:
    python:
        death_rows = 8
        death_cols = 1
        death_cells = death_rows * death_cols
        menu_list=sorted(game.chronik.death_reason.keys(),key=lambda i: len(game.chronik.death_reason[i]),reverse=True)
#        
    tag menu

    frame background "img/scene/memory_of_death.jpg":
        if death_page * death_cells > len(menu_list):
            $ death_page = 0

        $ next_death_page = death_page + 1
        $ prev_death_page = death_page - 1
        
        grid 1 death_rows:
            spacing 15
            ypos 15
            xalign 0.5
            for row_i in xrange(death_rows):
              $ death_i= row_i+death_cells*death_page
              if death_i<len(menu_list):
    #            $ game.chronik.set_active_death_botton(death_i)
#                $ a=menu_list[death_i]
                $ bot_desc = "{color=#000000}%s %.2f%%{/color}" % (data.death_reason_desc[menu_list[death_i]], 100.*len(game.chronik.death_reason[menu_list[death_i]])/game.chronik.tot_dead)
                textbutton (bot_desc) xsize (675) action [Function(game.chronik.set_active_death, menu_list[death_i]), Jump("lb_death_list")]#[Function(game.chronik.set_active_dragon, death_i), Show("girl_chronik_menu")]
              else:
                null
#            textbutton (bot_desc) action[SetVariable('death_lev', death_i), Show("girl_chronik_menu")]
        hbox: 
            ypos 680
            xpos 60
            spacing 50
            if death_page > 0:
                textbutton _("Предыдущая страница") action[SetVariable('death_page', prev_death_page), Show("death_menu")]
            else:
                textbutton _("Предыдущая страница") action None
            textbutton _("Вернуться") action [Show("dragon_chronik_menu")]
            if next_death_page * death_cells < len(menu_list):
                textbutton _("Следующая страница") action[SetVariable('death_page', next_death_page), Show("death_menu")]
            else:
                textbutton _("Следующая страница") action None

screen live_menu:
    python:
        live_rows = 8
        live_cols = 1
        live_cells = live_rows * live_cols
        menu_list=sorted(game.chronik.live_reason.keys(),key=lambda i: len(game.chronik.live_reason[i]),reverse=True)
#        
    tag menu

    frame background "img/scene/memory_of_life.jpg":
        if live_page * live_cells > len(menu_list):
            $ live_page = 0

        $ next_live_page = live_page + 1
        $ prev_live_page = live_page - 1
        
        grid 1 live_rows:
            spacing 15
            ypos 15
            xalign 0.5
            for row_i in xrange(live_rows):
              $ live_i= row_i+live_cells*live_page
              if live_i<len(menu_list):
    #            $ game.chronik.set_active_death_botton(death_i)
#                $ a=menu_list[death_i]
                $ bot_desc = "{color=#000000}%s %.2f%%{/color}" % (data.live_reason_desc[menu_list[live_i]], 100.*len(game.chronik.live_reason[menu_list[live_i]])/game.chronik.tot_live)
                textbutton (bot_desc) xsize (675) action [Function(game.chronik.set_active_live, menu_list[live_i]), Jump("lb_live_list")]#[Function(game.chronik.set_active_dragon, death_i), Show("girl_chronik_menu")]
              else:
                null
#            textbutton (bot_desc) action[SetVariable('death_lev', death_i), Show("girl_chronik_menu")]
        hbox: 
            ypos 680
            xpos 60
            spacing 50
            if live_page > 0:
                textbutton _("Предыдущая страница") action[SetVariable('live_page', prev_live_page), Show("live_menu")]
            else:
                textbutton _("Предыдущая страница") action None
            textbutton _("Вернуться") action [Show("dragon_chronik_menu")]
            if next_live_page * live_cells < len(menu_list):
                textbutton _("Следующая страница") action[SetVariable('live_page', next_live_page), Show("live_menu")]
            else:
                textbutton _("Следующая страница") action None







