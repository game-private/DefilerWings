# coding=utf-8
init python:
    import random

    from pythoncode.characters import Dragon
    
label lb_choose_dragon:
    # Хардкод на трех драконов.
    # @fdsc Выбор дракона
    # Уже не на трёх
    python:
        if renpy.music.get_playing(channel='music') != "mus/lullaby.ogg":
            renpy.music.play("mus/lullaby.ogg")           
    $ game.mobilization.level = 0
    hide bg
    python:
        lost = False
        if game.dragon is None:
            dragons = []
            dragons_choosed = []
        elif game.dragon.is_alive and not game.is_lost:
            game.dragon_parent = game.dragon
            
            data.achieve_restart("new_dragon")# событие для ачивок
            dragons = []
            dragons_choosed = []
            # добавляем 1 гоблина в армию тьмы
            game.army.add_warrior('goblin')
            # без выполненного квеста сюда попасть нельзя
            game.complete_quest()
        child_choose = None
        child_selected = None
        togle_dragonchoose_button = None
        if game.dragon and game.dragon.is_dead and len(dragons_choosed) == len(dragons):
            lost = True
    if lost:
        jump lb_game_over


    python hide:
        # @fdsc attackVirgin и uglyVirgin это способности, которые получаются не от рождения
        used_gifts = ['uglyVirgin', 'defenseVirgin', 'attackPVirgin', 'attackIVirgin', 'attackSVirgin', 'attackFVirgin', 'attackLVirgin']
        used_avatars = []
        
        if game.dragon is not None:
            if game.dragon.avatar not in used_avatars:
                used_avatars.append(game.dragon.avatar)

        if len(dragons) == 0:
            for x in xrange(8):
                try:
                    child = Dragon(parent=game.dragon, used_gifts=used_gifts, used_avatars=used_avatars, game_ref=game)
                except StopIteration:
                    break  # TODO: действие в случае когда драконы закончились
                dragons.append(child)
                used_gifts.append(child._gift)
                used_avatars.append(child.avatar)
        
        # @fdsc
        dragC = 0
        if dragons[dragC] not in dragons_choosed:
            renpy.childimg1 = ui.image(dragons[dragC].avatar)
        else:
            renpy.childimg1 = ui.image(im.Grayscale(dragons[dragC].avatar))
            
        dragC = dragC + 1
        if dragons[dragC] not in dragons_choosed:
            renpy.childimg1 = ui.image(dragons[dragC].avatar)
        else:
            renpy.childimg1 = ui.image(im.Grayscale(dragons[dragC].avatar))
            
        dragC = dragC + 1
        if dragons[dragC] not in dragons_choosed:
            renpy.childimg2 = ui.image(dragons[dragC].avatar)
        else:
            renpy.childimg2 = ui.image(im.Grayscale(dragons[dragC].avatar))
            
        dragC = dragC + 1
        if dragons[dragC] not in dragons_choosed:
            renpy.childimg3 = ui.image(dragons[dragC].avatar)
        else:
            renpy.childimg3 = ui.image(im.Grayscale(dragons[dragC].avatar))
            
        dragC = dragC + 1
        if dragons[dragC] not in dragons_choosed:
            renpy.childimg4 = ui.image(dragons[dragC].avatar)
        else:
            renpy.childimg4 = ui.image(im.Grayscale(dragons[dragC].avatar))
            
        dragC = dragC + 1
        if dragons[dragC] not in dragons_choosed:
            renpy.childimg5 = ui.image(dragons[dragC].avatar)
        else:
            renpy.childimg5 = ui.image(im.Grayscale(dragons[dragC].avatar))

        dragC = dragC + 1
        if dragons[dragC] not in dragons_choosed:
            renpy.childimg6 = ui.image(dragons[dragC].avatar)
        else:
            renpy.childimg6 = ui.image(im.Grayscale(dragons[dragC].avatar))

        dragC = dragC + 1
        if dragons[dragC] not in dragons_choosed:
            renpy.childimg7 = ui.image(dragons[dragC].avatar)
        else:
            renpy.childimg7 = ui.image(im.Grayscale(dragons[dragC].avatar))

        def get_breedbg():                               
            # Важно проверить количество голов. color_eng берёт цвет из первой головы, но иногда её почему-то нет.
            if game.dragon_parent:
                hatches_colored = [f for f in renpy.list_files() if f.startswith("img/scene/hatch/%s" % game.dragon_parent.color_eng)]
                
                if len(hatches_colored) > 0:
                    return random.choice(hatches_colored)

            return "img/scene/hatch/base.jpg"
                            
        renpy.breedbg = ui.image(get_breedbg())

    screen ava_screen:
        add renpy.breedbg
        add renpy.childimg1 xalign 0.0 yalign 0.0
        add renpy.childimg2 xalign 0.0 yalign 0.33
        add renpy.childimg3 xalign 0.0 yalign 0.66
        add renpy.childimg4 xalign 0.0 yalign 1.0
        add renpy.childimg5 xalign 0.20 yalign 0.0
        add renpy.childimg6 xalign 0.40 yalign 0.0
        add renpy.childimg7 xalign 0.60 yalign 0.0
        imagebutton idle "img/bg/frame.png" hover "img/bg/frame_light.png" selected_idle "img/bg/frame_light.png" xalign 0.0  yalign 0.0 action SetVariable("child_choose", dragons[0]), SetVariable("togle_dragonchoose_button", True), Show("text_screen"), SelectedIf(child_choose == dragons[0]), SensitiveIf(dragons[0] not in dragons_choosed)
        imagebutton idle "img/bg/frame.png" hover "img/bg/frame_light.png" selected_idle "img/bg/frame_light.png" xalign 0.0  yalign 0.33 action SetVariable("child_choose", dragons[1]), SetVariable("togle_dragonchoose_button", True), Show("text_screen"), SelectedIf(child_choose == dragons[1]), SensitiveIf(dragons[1] not in dragons_choosed)
        imagebutton idle "img/bg/frame.png" hover "img/bg/frame_light.png" selected_idle "img/bg/frame_light.png" xalign 0.0  yalign 0.66 action SetVariable("child_choose", dragons[2]), SetVariable("togle_dragonchoose_button", True), Show("text_screen"), SelectedIf(child_choose == dragons[2]), SensitiveIf(dragons[2] not in dragons_choosed)
        imagebutton idle "img/bg/frame.png" hover "img/bg/frame_light.png" selected_idle "img/bg/frame_light.png" xalign 0.0  yalign 1.0 action SetVariable("child_choose", dragons[3]), SetVariable("togle_dragonchoose_button", True), Show("text_screen"), SelectedIf(child_choose == dragons[3]), SensitiveIf(dragons[3] not in dragons_choosed)
        imagebutton idle "img/bg/frame.png" hover "img/bg/frame_light.png" selected_idle "img/bg/frame_light.png" xalign 0.20 yalign 0.0 action SetVariable("child_choose", dragons[4]), SetVariable("togle_dragonchoose_button", True), Show("text_screen"), SelectedIf(child_choose == dragons[4]), SensitiveIf(dragons[4] not in dragons_choosed)
        imagebutton idle "img/bg/frame.png" hover "img/bg/frame_light.png" selected_idle "img/bg/frame_light.png" xalign 0.40 yalign 0.0 action SetVariable("child_choose", dragons[5]), SetVariable("togle_dragonchoose_button", True), Show("text_screen"), SelectedIf(child_choose == dragons[5]), SensitiveIf(dragons[5] not in dragons_choosed)
        imagebutton idle "img/bg/frame.png" hover "img/bg/frame_light.png" selected_idle "img/bg/frame_light.png" xalign 0.60 yalign 0.0 action SetVariable("child_choose", dragons[6]), SetVariable("togle_dragonchoose_button", True), Show("text_screen"), SelectedIf(child_choose == dragons[6]), SensitiveIf(dragons[6] not in dragons_choosed)
        use status_bar

    screen text_screen:
        $renpy.childtext = "%s %s\n\n%s" % (child_choose.name, child_choose.surname, child_choose.description)
        window:
            xsize 760
            xpos 200
            ypos 200
            align(0.0, 0.0)
            # @fdsc Уменьшил шрифт
            text renpy.childtext:
                size 18
        if togle_dragonchoose_button is True:
            fixed:
                xalign 1.0
                xmaximum 320
                textbutton "Выбрать":
                    pos(72, 649)
                    xysize(174, 36)
                    text_xalign 0.5
                    text_yalign 0.5
                    background "img/bg/logovo.png"
                    # @fdsc
                    # text_size 22
                    text_size 22
                    action SetVariable("child_selected", child_choose), SetVariable("togle_dragonchoose_button", False), Hide("ava_screen"), Hide("text_screen"), Return("return")
    while True:
        nvl clear
        call screen ava_screen
        $ game.dragon = child_selected
        $ dragons_choosed.append(game.dragon)
        show expression 'img/scene/mistress.jpg' as bg
        "[game.quest_text]"
        jump lb_location_mordor_main
