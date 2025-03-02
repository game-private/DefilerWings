# coding=utf-8
init python:
      from pythoncode.characters import Dragon
      
label lb_dragon_creator:
    python:
        if renpy.music.get_playing(channel='music') != "mus/lullaby.ogg":
            renpy.music.play("mus/lullaby.ogg")     
    show expression 'img/scene/hatch/green/3.jpg' as bg    
    python:
        save_blocked = True
        child = Dragon(parent=game.dragon, game_ref=game)
        game.dragon = child
        mods_left = len(persistent.achievements) if not config.developer else 12
        game.dragon.heads = ['green']
        game.dragon.anatomy = ['size']
        special_features_rus = {
            "tough_scale": "Крепкая чешуя",
            "gold_scale":  "Золотая чешуя",
            "poisoned_sting": "Ядовитое жало",
            "clutches": "Когти",
            "horns": "Рога",
            "fangs": "Клыки",
            "ugly": "Уродство",
            "cunning": "Коварство",
            "tongue": "Сладкий язык",
            "spermtoxicos": "Спермотоксикоз",
            "energy": "Энергичный дракон",
            "strong_heart": "Мощное сердце",
            "astral_projection": "Астральная проекция",
            "art_dragon": "Творческий дракон"
        }
        colored_heads = ["red", "white", "blue", "black", "iron", "bronze", "silver", "gold", "shadow"]
    init python:
        class AddModifier(object):
            def __init__(self, mod, dragon):
                self.mod = mod
                self.dragon = dragon

            def __call__(self):
                if self.mod in data.dragon_heads.keys():
                    if self.mod == "green":
                        self.dragon.heads.append(self.mod)
                    else:
                        self.dragon.heads[self.dragon.heads.index("green")] = self.mod
                        colored_heads.pop(colored_heads.index(self.mod))
                else:
                    self.dragon.anatomy.append(self.mod)
                    if self.mod in special_features_rus.keys():
                        if self.mod != "cunning":
                            special_features_rus.pop(self.mod)
                        elif self.dragon.modifiers().count("cunning") >= 3:
                            special_features_rus.pop(self.mod)

                self.dragon.correct_for_manual_creation()
                renpy.restart_interaction()
    screen creator:
        window:
            text "Осталось модификаций [mods_left]" xalign 0.45 yalign 0.9
            hbox:
                vbox:
                    text "Добавить..."
                    if len(game.dragon.heads) < 10:
                        textbutton "Голова" action SetVariable("mods_left", mods_left - 1), AddModifier("green", game.dragon), If(mods_left == 1, (Hide("creator"), Return("return")))
                    if game.dragon.paws < 3:
                        textbutton "Лапы" action SetVariable("mods_left", mods_left - 1), AddModifier("paws", game.dragon), If(mods_left == 1, (Hide("creator"), Return("return")))
                    if game.dragon.wings < 3:
                        textbutton "Крылья" action SetVariable("mods_left", mods_left - 1), AddModifier("wings", game.dragon), If(mods_left == 1, (Hide("creator"), Return("return")))
                    if game.dragon.size < 6:
                        textbutton "Размер" action SetVariable("mods_left", mods_left - 1), AddModifier("size", game.dragon), If(mods_left == 1, (Hide("creator"), Return("return")))
                    for i in special_features_rus.keys():
                        textbutton special_features_rus[i] action SetVariable("mods_left", mods_left - 1), AddModifier(i, game.dragon), If(mods_left == 1, (Hide("creator"), Return("return")))
                if game.dragon.heads.count("green") > 0: 
                    vbox:
                        text "Покрасить голову"
                        for i in colored_heads:
                            textbutton data.heads_name_rus[i].capitalize() action SetVariable("mods_left", mods_left - 1), AddModifier(i, game.dragon), If(mods_left == 1, (Hide("creator"), Return("return")))
            use status_bar
            fixed:
                xalign 1.0
                xmaximum 320
                textbutton "{font=fonts/Tchekhonin2.ttf}В{/font}{font=fonts/times.ttf}ыпустить{/font}":
                    pos(72, 649)
                    xysize(174, 36)
                    text_xalign 0.5
                    text_yalign 0.5
                    background "img/bg/logovo.png"
                    text_size 22
                    action Hide("creator"), Return("return")
            fixed:
                xalign 1.0
                xmaximum 320
                textbutton "{font=fonts/Tchekhonin2.ttf}О{/font}{font=fonts/times.ttf}писание{/font}":
                    pos(72, 600)
                    xysize(174, 36)
                    text_xalign 0.5
                    text_yalign 0.5
                    background "img/bg/logovo.png"
                    text_size 22
                    action Show("sc_dragon_description")
                if not config.developer:
                    textbutton "{font=fonts/Tchekhonin2.ttf}Д{/font}{font=fonts/times.ttf}остижения{/font}":
                        pos(72, 549)
                        xysize(174, 36)
                        text_xalign 0.5
                        text_yalign 0.5
                        background "img/bg/logovo.png"
                        text_size 22
                        action Show("sc_achievements_list")

    screen sc_dragon_description:
        window:
            xmaximum 960
            xalign 0.0
            text "[game.dragon.description]"

        key "K_SPACE" action Hide("sc_dragon_description")
        key 'K_RETURN' action Hide("sc_dragon_description")
        key 'K_KP_ENTER' action Hide("sc_dragon_description")
        key 'mouseup_1' action Hide("sc_dragon_description")
    nvl clear
    call screen creator
    $ game.dragon.avatar=get_random_image("img/avadragon/" + game.dragon.color_eng)
    $ save_blocked = False
    $ game.create_lair()
    jump lb_location_mordor_main