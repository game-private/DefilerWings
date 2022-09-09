label lb_achievement_acquired:
    python:
        if u"Пасхальный кролик" not in persistent.achievements.keys():            
            for egg in persistent.easter_eggs:
                data.achieve_target(egg, "easter_eggs")
    $ achieved = data.store_achievements(persistent.achievements)
    $ names_list = achieved.keys()
    while len(names_list) != 0:
        $ achievement_name = names_list.pop()
        $ achievement_description = achieved[achievement_name]
        "Вы получили достижение [achievement_name]: [achievement_description]"
    nvl clear
    return
label lb_achievements_list:
    python:
        if len(persistent.achievements) > 0:
            achievements_text = "\n".join(["%s: %s"%(name, desc) for name, desc in persistent.achievements.items()])
        else:
            achievements_text = "Вы ещё не открыли достижений"
    "[achievements_text]"
    nvl clear

screen sc_achievements_choose:
    window:
        xmaximum 960
        xalign 0.0
        
            
        if len(persistent.achievements) > 0:
          textbutton _("Полученные достижения"):
              xalign 0.5
              yalign 0.4
              action [Hide('sc_achievements_choose'),Show("sc_achievements_list")]

        if len(persistent.achievements) < len(data.achievements_list):
          textbutton _("Неполученные достижения"):
            xalign 0.5
            yalign 0.6
            action [Hide('sc_achievements_choose'),Show("sc_achievements_future")]

    

screen sc_achievements_list:
    python:
        if len(persistent.achievements) > 0:
            achievements_text = "\n".join(["{b}%s{/b}: %s"%(name, desc) for name, desc in persistent.achievements.items()])
        else:
            achievements_text = "Вы ещё не открыли достижений"
    window:
        viewport id "vp":
             mousewheel  True
             xmaximum 960
             xalign 0.0
             text "[achievements_text]"
        key "K_SPACE" action Hide("sc_achievements_list")
        key 'K_RETURN' action Hide("sc_achievements_list")
        key 'K_KP_ENTER' action Hide("sc_achievements_list")
        key 'mouseup_1' action Hide("sc_achievements_list")


screen sc_achievements_future:   # Будущие достижения
    python:
        achievements_text=''
        for achievement in data.achievements_list:
          check=True
          for name,desc in persistent.achievements.items():
            if name == achievement.name:
              check=False
          if check:
            achievements_text += "{b}%s{/b}: %s\n" %(achievement.name, achievement.description)
#                 break
#        else:
#            achievements_text = "Вы ещё не открыли достижений"
    window:
        viewport id "vp":
             mousewheel  True
             xmaximum 960
             xalign 0.0
             text "[achievements_text]"
        key "K_SPACE" action Hide("sc_achievements_future")
        key 'K_RETURN' action Hide("sc_achievements_future")
        key 'K_KP_ENTER' action Hide("sc_achievements_future")
        key 'mouseup_1' action Hide("sc_achievements_future")