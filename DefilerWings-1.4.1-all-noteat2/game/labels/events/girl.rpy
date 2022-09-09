# coding=utf-8
init python:
    from pythoncode import girls_data
    
label lb_event_girl_escape:
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    if game.girl.blind:
      $ text = game.girls_list.description('escape_blind')  # описание чудесного спасения
    else:
      $ text = game.girls_list.description('escape')  # описание чудесного спасения
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

# Mahariel_print
label lb_try_to_go_underwater_usual(g_type,l_access):
    $ place = 'sea'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    python:
       save_girl=(girls_data.girls_info[g_type]['endurance']-0.1*l_access)
    $ choices = [
        ("lb_try_to_go_underwater_usual_save", 75 * save_girl),
        ("lb_try_to_go_underwater_usual_dead_1", 10),
        ("lb_try_to_go_underwater_usual_dead_2", 10),
        ("lb_try_to_go_underwater_usual_dead_3", 10),
        ("lb_try_to_go_underwater_usual_dead_4", 10),
        ("lb_try_to_go_underwater_usual_dead_5", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return


label lb_try_to_go_underwater_usual_save:
    $ text = u'%s благополучно доплыла до берега. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_underwater_usual_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_underwater_usual_dead_1:
    $ text = u'%s так и не добралась до своих сородичей: неподалёку от берега её ногу свело судорогой. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    $ game.chronik.death('underwater_usual_dead_1',None)
    $ game.girls_list.description('try_to_go_underwater_usual_dead_1', True)  
    return

label lb_try_to_go_underwater_usual_dead_2:
    $ text = u'%s так и не добралась до своих сородичей, ведь она просто-напросто не умела плавать. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underwater_usual_dead_2',None)
    $ game.girls_list.description('try_to_go_underwater_usual_dead_2', True)  
    return

label lb_try_to_go_underwater_usual_dead_3:
    $ text = u'%s так и не добралась до своих сородичей: мощное течение унесло её в открытый океан. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underwater_usual_dead_3',None)
    $ game.girls_list.description('try_to_go_underwater_usual_dead_3', True)  
    return

label lb_try_to_go_underwater_usual_dead_4:
    $ text = u'%s так и не добралась до своих сородичей: она оказалась в открытом море в двенадцатибалльный шторм. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underwater_usual_dead_4',None)
    $ game.girls_list.description('try_to_go_underwater_usual_dead_4', True)  
    return

label lb_try_to_go_underwater_usual_dead_5:
    $ text = u'%s так и не добралась до своих сородичей: почти у самого берега она попала в щупальца к гигантскому кальмару. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underwater_usual_dead_5',None)
    $ game.girls_list.description('try_to_go_underwater_usual_dead_5', True)  
    return

# Спасение русалки из подводного логова

label lb_try_to_go_underwater_mermaid(g_type,l_access):
    $ place = 'sea'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_underwater_mermaid_save", 75 ),
        ("lb_try_to_go_underwater_mermaid_dead", 0.5*nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_underwater_mermaid_save:
    $ text = u'Русалка благополучно доплыла до своих сородичей. \n\n' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_underwater_mermaid_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_underwater_mermaid_dead:
    $ text = u'Русалка так и не добралась до своих сородичей, погибнув в бою с гигантским кальмаром. \n\n' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underwater_mermaid_dead',None)
    $ game.girls_list.description('try_to_go_underwater_mermaid_dead', True) 
    return

# Спасение сирены из подводного логова. Спасается всегда.

label lb_try_to_go_underwater_siren(g_type,l_access):
    $ place = 'sea'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_underwater_siren_save_1", 75 ),
        ("lb_try_to_go_underwater_siren_save_2", 0.5*nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_underwater_siren_save_1:
    $ text = u'Сирена благополучно добралась до сородичей. \n\n' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_underwater_siren_save_1', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_underwater_siren_save_2:
    $ text = u'Сирена благополучно добралась до сородичей. Правда, по пути ей повстречался гигантский кальмар, но красавица легко победила глупое головоногое. \n\n' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_underwater_siren_save_2', True) 
    python:
        game.girls_list.save_girl()  
    return

# Спасение ифритки из подводного логова. Спастись очень сложно.

label lb_try_to_go_underwater_fire(g_type,l_access):
    $ place = 'sea'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_underwater_fire_save", 5 ),
        ("lb_try_to_go_underwater_fire_dead", 50)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_underwater_fire_save:
    $ text = u'Каким-то чудом ифритка умудрилась доплыть до берега. \n\n' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_underwater_fire_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_underwater_fire_dead:
    $ text = u'Ифритка так и не добралась до своих сородичей, утонув в безбрежном океане.  \n\n' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underwater_fire_dead',None)
    $ game.girls_list.description('try_to_go_underwater_fire_dead', True) 
    return

# Спасение остальных великанш из подводного логова. 

label lb_try_to_go_underwater_giant(g_type,l_access):
    $ place = 'sea'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_underwater_giant_save", 75 ),
        ("lb_try_to_go_underwater_giant_dead_1", 10),
        ("lb_try_to_go_underwater_giant_dead_2", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_underwater_giant_save:
    $ text = u'%s благополучно доплыла до берега. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_underwater_giant_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_underwater_giant_dead_1:
    $ text = u'%s так и не добралась до своих сородичей. Иногда вредно не уметь плавать. Даже великаншам. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underwater_giant_dead_1',None)
    $ game.girls_list.description('try_to_go_underwater_giant_dead_1', True) 
    return

label lb_try_to_go_underwater_giant_dead_2:
    $ text = u'%s так и не добралась до своих сородичей: во время заплыва к берегу её схватил гигантский кальмар. Великанша обладала немалой силой, но, увы, не умела дышать под водой. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underwater_giant_dead_2',None)
    $ game.girls_list.description('try_to_go_underwater_giant_dead_2', True) 
    return

# Спасение с Неприступной вершины
label lb_try_to_go_peak_usual(g_type,l_access):
    $ place = 'mountain'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    python:
        save_girl=(girls_data.girls_info[g_type]['endurance']-0.1*l_access)
        if (save_girl <= 0):
            save_girl = 1. / 75.
       
        choices = [
        ("lb_try_to_go_peak_usual_save", 75 * save_girl),
        ("lb_try_to_go_peak_usual_dead_1", 10),
        ("lb_try_to_go_peak_usual_dead_2", 10),
        ("lb_try_to_go_peak_usual_dead_3", 10),
        ("lb_try_to_go_peak_usual_dead_4", 10),
        ("lb_try_to_go_peak_usual_dead_5", nochance)]

        enc = weighted_random(choices)
        renpy.call(enc)
    return

label lb_try_to_go_peak_usual_save:
    $ text = u'%s умудрилась благополучно спуститься с гор. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_peak_usual_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_peak_usual_dead_1:
    $ text = u'%s так и не добралась до своих сородичей: пробираясь по горной местности, она случайно сломала ногу. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('peak_usual_dead_1',None)
    $ game.girls_list.description('try_to_go_peak_usual_dead_1', True)  
    return

label lb_try_to_go_peak_usual_dead_2:
    $ text = u'%s так и не добралась до своих сородичей: идя по прижиму, она поскользнулась и сорвалась в пропасть. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('peak_usual_dead_2',None)
    $ game.girls_list.description('try_to_go_peak_usual_dead_2', True)  
    return

label lb_try_to_go_peak_usual_dead_3:
    $ text = u'%s так и не добралась до своих сородичей: она сорвалась в пропасть, умудрилась зацепиться за край скалы, но не смогла подтянуться на руках. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('peak_usual_dead_3',None)
    $ game.girls_list.description('try_to_go_peak_usual_dead_3', True)  
    return

label lb_try_to_go_peak_usual_dead_4:
    $ text = u'%s так и не добралась до своих сородичей: выбрав короткий, но опасный путь, она вышла на неустойчивую осыпь и вызвала камнепад. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('peak_usual_dead_4',None)
    $ game.girls_list.description('try_to_go_peak_usual_dead_4', True)  
    return

label lb_try_to_go_peak_usual_dead_5:
    $ text = u'%s так и не добралась до своих сородичей: она угодила в лапы к гоблинам, бесчинствующим в тех местах. После пары суток унижений и пыток гоблины заживо съели свою жертву. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('peak_usual_dead_5',None)
    $ game.girls_list.description('try_to_go_peak_usual_dead_5', True)  
    return

# Спасение русалки с Неприступной вершины. Спастись сложно.

label lb_try_to_go_peak_mermaid(g_type,l_access):
    $ place = 'mountain'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_peak_mermaid_save", 15 ),
        ("lb_try_to_go_peak_mermaid_dead", 50)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_peak_mermaid_save:
    $ text = u'%s умудрилась добраться до горной реки и благополучно спуститься с гор. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_peak_mermaid_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_peak_mermaid_dead:
    $ text = u'Русалка в горах - грустное зрелище. Печальное. И мёртвое. \n\n'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('peak_mermaid_dead',None)
    $ game.girls_list.description('try_to_go_peak_mermaid_dead', True) 
    return

# Спасение великанш с Неприступной вершины. 

label lb_try_to_go_peak_giant(g_type,l_access):
    $ place = 'mountain'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_peak_giant_save_1", 75 ),
        ("lb_try_to_go_peak_giant_save_2", nochance),
        ("lb_try_to_go_peak_giant_dead", 10)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_peak_giant_save_1:
    $ text = u'%s умудрилась благополучно спуститься с гор. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_peak_giant_save_1', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_peak_giant_save_2:
    $ text = u'%s умудрилась благополучно спуститься с гор. Правда, по пути она встретила отряд гоблинов, но мелкие монстрики ничего не смогли сделать разъярённой великанше. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_peak_giant_save_2', True) 
    return

label lb_try_to_go_peak_giant_dead:
    $ text = u'%s так и не добралась до своих сородичей: идя по прижиму, она поскользнулась и сорвалась в пропасть. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('peak_giant_dead',None)
    $ game.girls_list.description('try_to_go_peak_giant_dead', True) 
    return

# Спасение с ледяных гор
label lb_try_to_go_ice_usual(g_type,l_access):
    $ place = 'mountain'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    python:
       save_girl=(girls_data.girls_info[g_type]['endurance']-0.1*l_access)
    $ choices = [
        ("lb_try_to_go_peak_usual_save", 75 * save_girl),
        ("lb_try_to_go_peak_usual_dead_1", 10),
        ("lb_try_to_go_peak_usual_dead_2", 10),
        ("lb_try_to_go_peak_usual_dead_3", 10),
        ("lb_try_to_go_peak_usual_dead_4", 10),
        ("lb_try_to_go_peak_usual_dead_5", nochance),
        ("lb_try_to_go_ice_usual_dead_1", 10),
        ("lb_try_to_go_ice_usual_dead_2", 10),
        ("lb_try_to_go_ice_usual_dead_3", 10),
        ("lb_try_to_go_ice_usual_dead_4", 10),
        ("lb_try_to_go_ice_usual_dead_5", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_ice_usual_dead_1:
    $ text = u'%s так и не добралась до своих сородичей: она прилегла на минутку отдохнуть и замёрзла насмерть. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('ice_usual_dead_1',None)
    $ game.girls_list.description('try_to_go_ice_usual_dead_1', True)  
    return

label lb_try_to_go_ice_usual_dead_2:
    $ text = u'%s так и не добралась до своих сородичей: пробираясь по ледяным полям, она упала в трещину.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('ice_usual_dead_2',None)
    $ game.girls_list.description('try_to_go_ice_usual_dead_2', True)  
    return

label lb_try_to_go_ice_usual_dead_3:
    $ text = u'%s так и не добралась до своих сородичей: она попала в снегопад, который погрёб её с головой.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('ice_usual_dead_3',None)
    $ game.girls_list.description('try_to_go_ice_usual_dead_3', True)  
    return

label lb_try_to_go_ice_usual_dead_4:
    $ text = u'%s так и не добралась до своих сородичей: пробираясь по ледяным полям, она оказалась на пути лавины.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('ice_usual_dead_4',None)
    $ game.girls_list.description('try_to_go_ice_usual_dead_4', True)  
    return

label lb_try_to_go_ice_usual_dead_5:
    $ text = u'%s так и не добралась до своих сородичей: выбравшись с ледяных полей, она наткнулась на йети. Монстр долго насиловал беззащтное женское тело, одновременно пожирая его заживо. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('ice_usual_dead_5',None)
    $ game.girls_list.description('try_to_go_ice_usual_dead_5', True)  
    return

# Спасение русалки с Ледяных гор. Спастись очень сложно.

label lb_try_to_go_ice_mermaid(g_type,l_access):
    $ place = 'mountain'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_peak_mermaid_save", 10 ),
        ("lb_try_to_go_ice_mermaid_dead", 50)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_ice_mermaid_dead:
    $ text = u'Русалка на леднике - грустное зрелище. Печальное. И мёртвое. \n\n'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('ice_mermaid_dead',None)
    $ game.girls_list.description('try_to_go_ice_mermaid_dead', True) 
    return

# Спасение ифритки c ледяных гор. Спастись практически невозможно.

label lb_try_to_go_ice_fire(g_type,l_access):
    $ place = 'mountain'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_ice_fire_save", 5 ),
        ("lb_try_to_go_ice_fire_dead", 50)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_ice_fire_save:
    $ text = u'Ифритка добралась до родных вулканов, хотя поход по ледникам дался ей нелегко. \n\n'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_ice_fire_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_ice_fire_dead:
    $ text = u'%s так и не добралась до своих сородичей: пробираясь по ледяным полям, ифритка замёрзла насмерть.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('ice_fire_dead',None)
    $ game.girls_list.description('try_to_go_ice_fire_dead', True) 
    return

# Спасение йотунши c ледяных гор. Спасается наверняка.

label lb_try_to_go_ice_ice(g_type,l_access):
    $ place = 'mountain'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_ice_ice_save_1", 75 ),
        ("lb_try_to_go_ice_ice_save_2", nochance),
        ("lb_try_to_go_peak_giant_save_2", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_ice_ice_save_1:
    $ text = u'Йотунша благополучно спустилась с ледника и добралась до своих сородичей.\n\n' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_ice_ice_save_1', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_ice_ice_save_2:
    $ text = u'Йотунша благополучно добралась до своих сородичей. Правда, она повстречала йети, но благодаря своей исполинской силе смогла победить монстра. \n\n' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_ice_ice_save_2', True) 
    python:
        game.girls_list.save_girl()  
    return

# Спасение великанш с Ледяных гор. 

label lb_try_to_go_ice_giant(g_type,l_access):
    $ place = 'mountain'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_peak_giant_save_1", 75 ),
        ("lb_try_to_go_peak_giant_save_2", nochance),
        ("lb_try_to_go_peak_giant_dead", 10),
        ("lb_try_to_go_ice_giant_dead_1", 10),
        ("lb_try_to_go_ice_giant_dead_2", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

    label lb_try_to_go_ice_giant_dead_1:
    $ text = u'%s так и не добралась до своих сородичей: пробираясь по ледника, она упала в исполинскую трещину.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('ice_giant_dead_1',None)
    $ game.girls_list.description('try_to_go_ice_giant_dead_1', True) 
    return

    label lb_try_to_go_ice_giant_dead_2:
    $ text = u'%s так и не добралась до своих сородичей: спускаясь с ледника, она повстречала йети. Великанша сражалась отчаянно и пала в бою.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('ice_giant_dead_2',None)
    $ game.girls_list.description('try_to_go_ice_giant_dead_2', True) 
    return

# Спасение с вулканических гор
label lb_try_to_go_fire_usual(g_type,l_access):
    $ place = 'mountain'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    python:
       save_girl=(girls_data.girls_info[g_type]['endurance']-0.1*l_access)
    $ choices = [
        ("lb_try_to_go_peak_usual_save", 75 * save_girl),
        ("lb_try_to_go_peak_usual_dead_1", 10),
        ("lb_try_to_go_peak_usual_dead_2", 10),
        ("lb_try_to_go_peak_usual_dead_3", 10),
        ("lb_try_to_go_peak_usual_dead_4", 10),
        ("lb_try_to_go_peak_usual_dead_5", nochance),
        ("lb_try_to_go_fire_usual_dead_1", 10),
        ("lb_try_to_go_fire_usual_dead_2", 10),
        ("lb_try_to_go_fire_usual_dead_3", 10),
        ("lb_try_to_go_fire_usual_dead_4", 10),
        ("lb_try_to_go_fire_usual_dead_5", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_fire_usual_dead_1:
    $ text = u'%s так и не добралась до своих сородичей: она умерла от жажды на вулканическом плато.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('fire_usual_dead_1',None)
    $ game.girls_list.description('try_to_go_fire_usual_dead_1', True)  
    return

label lb_try_to_go_fire_usual_dead_2:
    $ text = u'%s так и не добралась до своих сородичей: она свалилась в котловину гейзера и сварилась заживо.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('fire_usual_dead_2',None)
    $ game.girls_list.description('try_to_go_fire_usual_dead_2', True)  
    return

label lb_try_to_go_fire_usual_dead_3:
    $ text = u'%s так и не добралась до своих сородичей: она сорвалась с обрыва и упала прямо в лаву.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('fire_usual_dead_3',None)
    $ game.girls_list.description('try_to_go_fire_usual_dead_3', True)  
    return

label lb_try_to_go_fire_usual_dead_4:
    $ text = u'%s так и не добралась до своих сородичей: она оказалась прямо на пути лавого потока.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('fire_usual_dead_4',None)
    $ game.girls_list.description('try_to_go_fire_usual_dead_4', True)  
    return

label lb_try_to_go_fire_usual_dead_5:
    $ text = u'%s так и не добралась до своих сородичей: почти спустившись с гор, она попала в лапы адской гончей.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('fire_usual_dead_5',None)
    $ game.girls_list.description('try_to_go_fire_usual_dead_5', True)  
    return

# Спасение русалки с вулкана. Спастись практически невозможно.

label lb_try_to_go_fire_mermaid(g_type,l_access):
    $ place = 'mountain'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_peak_mermaid_save", 5 ),
        ("lb_try_to_go_fire_mermaid_dead", 50)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_fire_mermaid_dead:
    $ text = u'Русалка на вулкане - грустное зрелище. Печальное. И мёртвое.\n\n' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('fire_mermaid_dead',None)
    $ game.girls_list.description('try_to_go_fire_mermaid_dead', True) 
    return

# Спасение йотунши с вулкана. Спастись практически невозможно.

label lb_try_to_go_fire_ice(g_type,l_access):
    $ place = 'mountain'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_fire_ice_save", 5 ),
        ("lb_try_to_go_fire_ice_dead", 50)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_fire_ice_save:
    $ text = u'Йотунша добралась до родных ледников, хотя поход по вулканическому плато дался ей нелегко.\n\n' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_fire_ice_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_fire_ice_dead:
    $ text = u'%s так и не добралась до своих сородичей: йотунша на вулканическом плато просто-напросто сварилась заживо. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('fire_ice_dead',None)
    $ game.girls_list.description('try_to_go_fire_ice_dead', True) 
    return

# Спасение ифритки с вулкана. Спасается наверняка.

label lb_try_to_go_fire_fire(g_type,l_access):
    $ place = 'mountain'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_fire_fire_save_1", 75 ),
        ("lb_try_to_go_fire_fire_save_2", nochance),
        ("lb_try_to_go_peak_giant_save_2", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_fire_fire_save_1:
    $ text = u'Ифритка благополучно добралась до родных вулканов.\n\n'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_fire_fire_save_1', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_fire_fire_save_2:
    $ text = u'%s благополучно добралалась до родных мест. Правда, по пути ей попалась адская гончая, но ифритка пришибла чуловищную собачку. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_fire_fire_save_2', True) 
    python:
        game.girls_list.save_girl()  
    return

# Спасение великанш с вулкана. 

label lb_try_to_go_fire_giant(g_type,l_access):
    $ place = 'mountain'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_peak_giant_save_1", 75 ),
        ("lb_try_to_go_peak_giant_save_2", nochance),
        ("lb_try_to_go_peak_giant_dead", 10),
        ("lb_try_to_go_fire_giant_dead_1", 10),
        ("lb_try_to_go_fire_giant_dead_2", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_fire_giant_dead_1:
    $ text = u'%s так и не добралась до своих сородичей: великанша прозевала извержение вулкана и погибла в лаве.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('fire_giant_dead_1',None)
    $ game.girls_list.description('try_to_go_fire_giant_dead_1', True) 
    return

label lb_try_to_go_fire_giant_dead_2:
    $ text = u'%s так и не добралась до своих сородичей: спускаясь с вулкана, она повстречала адскую гончую. Великанша сражалась отчаянно и пала в бою.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('fire_giant_dead_2',None)
    $ game.girls_list.description('try_to_go_fire_giant_dead_2', True) 
    return

# Спасение из Подгорных чертогов
label lb_try_to_go_underground_usual(g_type,l_access):
    $ current_image='img/bg/special/moria.jpg'
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    python:
       save_girl=(girls_data.girls_info[g_type]['endurance']-0.1*l_access)
    $ choices = [
        ("lb_try_to_go_underground_usual_save", 20 * save_girl),
        ("lb_try_to_go_underground_usual_dead_1", 10),
        ("lb_try_to_go_underground_usual_dead_2", 10),
        ("lb_try_to_go_underground_usual_dead_3", 10),
        ("lb_try_to_go_underground_usual_dead_4", 10),
        ("lb_try_to_go_underground_usual_dead_5", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_underground_usual_save:
    $ text = u'%s благополучно выбралась из Подгорных чертогов.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_underground_usual_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_underground_usual_dead_1:
    $ text = u'%s так и не добралась до своих сородичей: она заблудилась и умперла от жажды.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underground_usual_dead_1',None)
    $ game.girls_list.description('try_to_go_underground_usual_dead_1', True)  
    return

label lb_try_to_go_underground_usual_dead_2:
    $ text = u'%s так и не добралась до своих сородичей: блуждая в темноте, она свалилась в подземное озеро и утонула.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underground_usual_dead_2',None)
    $ game.girls_list.description('try_to_go_underground_usual_dead_2', True)  
    return

label lb_try_to_go_underground_usual_dead_3:
    $ text = u'%s так и не добралась до своих сородичей: блуждая в темноте, она упала в бездонный колодец.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underground_usual_dead_3',None)
    $ game.girls_list.description('try_to_go_underground_usual_dead_3', True)  
    return

label lb_try_to_go_underground_usual_dead_4:
    $ text = u'%s так и не добралась до своих сородичей: она намертво застряла в узком лазе всего в нескольких метрах от поверхности.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underground_usual_dead_4',None)
    $ game.girls_list.description('try_to_go_underground_usual_dead_4', True)  
    return

label lb_try_to_go_underground_usual_dead_5:
    $ text = u'%s так и не добралась до своих сородичей: выйдя на поверхность, она наткнулась на лагерь гоблинов. Маленькие монстрики долго развлекались с беззащитным девичьим телом, а потом съели его заживо.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underground_usual_dead_5',None)
    $ game.girls_list.description('try_to_go_underground_usual_dead_5', True)  
    return

# Спасение русалки из Поземных чертогов. Спастись очень сложно
label lb_try_to_go_underground_mermaid(g_type,l_access):
    $ current_image='img/bg/special/moria.jpg'
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_underground_mermaid_save", 15 ),
        ("lb_try_to_go_underground_mermaid_dead", 50)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_underground_mermaid_save:
    $ text = u'%s добралась до подземной реки и выплыла из Подгорных чертогов.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_underground_mermaid_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_underground_mermaid_dead:
    $ text = u'Русалка под землёй - грустное зрелище. Печальное. И мёртвое.\n\n' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('underground_mermaid_dead',None)
    $ game.girls_list.description('try_to_go_underground_mermaid_dead', True) 
    return

# Спасение ифритки из Подгорных чертогов. Спасается наверняка.
label lb_try_to_go_underground_fire(g_type,l_access):
    $ current_image='img/bg/special/moria.jpg'
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_underground_fire_save_1", 75 ),
        ("lb_try_to_go_underground_fire_save_2", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_underground_fire_save_1:
    $ text = u'%s, освещая путь своим пламенем, благополучно выбралась из Подгорных чертогов.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_underground_fire_save_1', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_underground_fire_save_2:
    $ text = u'%s благополучно выбралась из Подгорных чертогов. Правда, при выходе на поверхность она наткнулась на лагерь гоблинов, но мелкие монстрики послужили великанше отличной закуской.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_underground_fire_save_2', True) 
    python:
        game.girls_list.save_girl()  
    return

# Спасение остальных великанш из Подгорных чертогов
label lb_try_to_go_underground_giant(g_type,l_access):
    $ current_image='img/bg/special/moria.jpg'
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3

    $ choices = [
        ("lb_try_to_go_underground_usual_save", 15),
        ("lb_try_to_go_underground_usual_dead_1", 10),
        ("lb_try_to_go_underground_usual_dead_2", 10),
        ("lb_try_to_go_underground_usual_dead_3", 10),
        ("lb_try_to_go_underground_usual_dead_4", 10),
        ("lb_try_to_go_underground_fire_save_2", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

# Спасение из осквернённого леса
label lb_try_to_go_elf_usual(g_type,l_access):
    $ place = 'forest'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    python:
       save_girl=(girls_data.girls_info[g_type]['endurance']-0.1*l_access)
    $ choices = [
        ("lb_try_to_go_elf_usual_save", 20 * save_girl),
        ("lb_try_to_go_elf_usual_dead_1", 10),
        ("lb_try_to_go_elf_usual_dead_2", 10),
        ("lb_try_to_go_elf_usual_dead_3", 10),
        ("lb_try_to_go_elf_usual_dead_4", 10),
        ("lb_try_to_go_elf_usual_dead_5", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_elf_usual_save:
    $ text = u'Каким-то чудом %s выбралась из осквернённого леса.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_elf_usual_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_elf_usual_dead_1:
    $ text = u'%s так и не добралась до своих сородичей: она легла спать на полянке с живой травой, которая проросла сквозь девичье тело.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('elf_usual_dead_1',None)
    $ game.girls_list.description('try_to_go_elf_usual_dead_1', True)  
    return

label lb_try_to_go_elf_usual_dead_2:
    $ text = u'%s так и не добралась до своих сородичей: её заживо съели хищные растения.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('elf_usual_dead_2',None)
    $ game.girls_list.description('try_to_go_elf_usual_dead_2', True)  
    return

label lb_try_to_go_elf_usual_dead_3:
    $ text = u'%s так и не добралась до своих сородичей: стая муравьёв обнаружила спящее девичье тело, парализовала его и сгрызла заживо.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('elf_usual_dead_3',None)
    $ game.girls_list.description('try_to_go_elf_usual_dead_3', True)  
    return

label lb_try_to_go_elf_usual_dead_4:
    $ text = u'%s так и не добралась до своих сородичей: в её плоть проникли ядовитые семена, и девушка сгнила заживо.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('elf_usual_dead_4',None)
    $ game.girls_list.description('try_to_go_elf_usual_dead_4', True)  
    return

label lb_try_to_go_elf_usual_dead_5:
    $ text = u'%s так и не добралась до своих сородичей: на опушке осквернённого леса она встретила драконорождённого. Впрочем, после всего увиденного она встретила смерть с облегчением.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('elf_usual_dead_5',None)
    $ game.girls_list.description('try_to_go_elf_usual_dead_5', True)  
    return

# Спасение русалки из Эльфийского леса. Спастись не так уж сложно.
label lb_try_to_go_elf_mermaid(g_type,l_access):
    $ place = 'forest'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_elf_mermaid_save", 30 ),
        ("lb_try_to_go_elf_mermaid_dead", 50)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_elf_mermaid_save:
    $ text = u'%s благополучно выплыла из осквернённого леса и добралась до своих сородичей.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_elf_mermaid_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_elf_mermaid_dead:
    $ text = u'Русалка, сидящая на ветвях - грустное зрелище. Печальное. И мёртвое. \n\n' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('elf_mermaid_dead',None)
    $ game.girls_list.description('try_to_go_elf_mermaid_dead', True) 
    return

# Спасение великанш из осквернённого леса
label lb_try_to_go_elf_giant(g_type,l_access):
    $ place = 'forest'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_elf_giant_save_1", 20 ),
        ("lb_try_to_go_elf_usual_dead_1", 10),
        ("lb_try_to_go_elf_usual_dead_2", 10),
        ("lb_try_to_go_elf_usual_dead_3", 10),
        ("lb_try_to_go_elf_usual_dead_4", 10),
        ("lb_try_to_go_elf_giant_save_2", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_elf_giant_save_1:
    $ text = u'%s благополучно добралась до своих сородичей. Правда, прогулка по осквернёённому лесу далась ей нелегко.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_elf_giant_save_1', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_elf_giant_save_2:
    $ text = u'%s благополучно добралась до своих сородичей. Правда, при выходе из леса ей повстречался драконорожденный, но добрая драка лишь восстановила её пошатнувшееся психическое здоровье.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_elf_giant_save_2', True) 
    python:
        game.girls_list.save_girl()  
    return

# Спасение титаниды из замка в облаках. Спасается наверняка.
label lb_try_to_go_cloud_titan(g_type,l_access):
    $ place = 'sky'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ text = u'%s благополучно улетела из облачного замка.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_cloud_titan_save', True) 
    python:
        game.girls_list.save_girl() 
    return

# Возможное спасение падающей девушки грифоном.
label lb_try_to_go_cloud_griffin(g_type,l_access):
    $ place = 'sky'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ choices = [
        ("lb_try_to_go_cloud_griffin_save", 20 ),
        ("lb_try_to_go_cloud_usual_dead", 50)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_cloud_griffin_save:
    $ text = u'%s упала из облачного замка и непременно разбилась бы насмерть, если бы в последний момент её не подхватил всадник на грифоне. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_cloud_usual_dead', True) 
    $ game.girls_list.description('try_to_go_cloud_griffin_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_cloud_usual_dead:
    $ text = u'%s так и не добралась до своих сородичей: она упала из облачного замка и разбилась насмерть \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('cloud_usual',None)
    $ game.girls_list.description('try_to_go_cloud_usual_dead', True)  
    return

# Падение из облачного замка. Спастись нельзя.
label lb_try_to_go_cloud_usual(g_type,l_access):
    $ place = 'sky'
    $ current_image=get_place_bg(place)
    hide bg
    show expression current_image as bg
    nvl clear
    $ text = u'%s так и не добралась до своих сородичей: она упала из облачного замка и разбилась насмерть \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('cloud_usual',current_image)
    $ game.girls_list.description('try_to_go_cloud_usual_dead', True)
    return

# Спасение из обычного логова
label lb_try_to_go_forest_usual(g_type,l_access):
    $ place = 'forest'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    python:
       save_girl=(girls_data.girls_info[g_type]['endurance']-0.1*l_access)
    $ choices = [
        ("lb_try_to_go_forest_usual_save", 150* save_girl),
        ("lb_try_to_go_forest_usual_dead_1", 10),
        ("lb_try_to_go_forest_usual_dead_2", 10),
        ("lb_try_to_go_forest_usual_dead_3", 10),
        ("lb_try_to_go_forest_usual_dead_4", 10),
        ("lb_try_to_go_forest_usual_dead_5", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_forest_usual_save:
    $ text = u'%s умудрилась благополучно выйти из леса.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('try_to_go_forest_usual_save', True) 
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_forest_usual_dead_1:
    $ text = u'%s так и не добралась до своих сородичей: она попала в руки разбойников. Попользовавшись красоткой, мужчины задушили свою жертву. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('forest_usual_dead_1',None)
    $ game.girls_list.description('try_to_go_forest_usual_dead_1', True)  
    return

label lb_try_to_go_forest_usual_dead_2:
    $ text = u'%s так и не добралась до своих сородичей: она нарвалась на стаю голодных волков.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('forest_usual_dead_2',None)
    $ game.girls_list.description('try_to_go_forest_usual_dead_2', True)  
    return

label lb_try_to_go_forest_usual_dead_3:
    $ text = u'%s так и не добралась до своих сородичей: собирая ягоды, она нечаянно отравилась беладонной\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('forest_usual_dead_3',None)
    $ game.girls_list.description('try_to_go_forest_usual_dead_3', True)  
    return

label lb_try_to_go_forest_usual_dead_4:
    $ text = u'%s так и не добралась до своих сородичей: она нечаянно зашла на болото, и её медленно засосало в трясину.\n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('forest_usual_dead_4',None)
    $ game.girls_list.description('try_to_go_forest_usual_dead_4', True)  
    return

label lb_try_to_go_forest_usual_dead_5:
    $ text = u'%s так и не добралась до своих сородичей: по пути домой её укусил аспид. Смерть, наступившую через несколько часов, она приняла как избавление.  \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    
    $ game.chronik.death('forest_usual_dead_5',None)
    $ game.girls_list.description('try_to_go_forest_usual_dead_5', True)  
    return

# Спасение великанш из обычного логова. Спасаются наверняка.
label lb_try_to_go_forest_giant(g_type,l_access):
    $ place = 'forest'
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_try_to_go_forest_giant_save_1", 10 ),
        ("lb_try_to_go_forest_giant_save_2", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_try_to_go_forest_giant_save_1:
    $ game.girls_list.description('try_to_go_forest_giant_save_1', True) 
    $ text = u'%s благополучно и без каких-либо приключений добралась до своих сородичей. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    python:
        game.girls_list.save_girl()  
    return

label lb_try_to_go_forest_giant_save_2:
    $ game.girls_list.description('try_to_go_forest_giant_save_2', True) 
    $ text = u'%s благополучно добралась до своих сородичей. Правда, по пути домой её ужалил аспид, но он не смог прокусить толстую кожу великанши. \n\n' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    python:
        game.girls_list.save_girl()  
    return
# Неужели всё?
# Нет, не всё. Принимаюсь за слепых
label lb_ttg_show(place):
    $ current_image=get_place_bg(place)
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
#    'Тест'
    return


label lb_ttg_sea_blind1_mermaid_save:
    call lb_ttg_show(place='sea') from _call_lb_ttg_show_01
    $ text = u"Но даже слепая морская дева в своей родной стихии может многое. Несмотря на все опасности морских глубин, %s добралась до родных мест." % (game.girl.name)
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.save_girl()
    return

label lb_ttg_sea_blind1_mermaid_dead:
    call lb_ttg_show(place='sea') from _call_lb_ttg_show_02
    '[game.girl.name] плывёт. Куда-то. Зрения у неё больше нет, но остались иные чувства. Увы, они не способны предупредить её об опасности: подкравшийся гигантский кальмар ломает морской деве хвост. [game.girl.name] кричит от дикой боли, пытается отбиваться - тщетно. Монстр поглощает нежданную добычу и неспешно начинает её переваривать.'
    $ text = u"Слепая морская дева попыталась добраться до родных мест, но попала в щупальца к кракену."
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('blind_mermaid_sea',None)
    return

label lb_ttg_sea_blind1_dead:
    call lb_ttg_show(place='sea') from _call_lb_ttg_show_03
    '[game.girl.name] плывёт. Куда-то. Силы постепенно тают, а берег.. где он вообще, этот берег? Может, совсем рядом, может, удаляется с каждой минутой. [game.girl.name] лишь надеется, что выбрала правильное направление. \n\n Оказалос - неправильное.'
    $ text = u"Поэтому закономерно, что %s выбрала неправильное направление и так и не доплыла до берега." % game.girl.name
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('blind_sea',None)
    return

label lb_ttg_mount_blind1_giant_save:
    call lb_ttg_show(place='mountain') from _call_lb_ttg_show_04
    $ text = u"Но даже слепая великанша способна на многое. Несмотря на все опасности горных круч, %s добралась до родных мест." 
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.save_girl()
    return

label lb_ttg_mount_blind1_giant_dead:
    call lb_ttg_show(place='mountain') from _call_lb_ttg_show_05
    '[game.girl.name] спутает медленно и аккуратно. Увы, когда не видишь, куда идти, возможны всяческие непритности! Например, после очередного шага камни под ногой [game.girl.name_r] начинают ехать, и великанша с криком устремляется к пропасти.\n\nИногда размер не имеет значения'
    $ text = u"Поэтому закономерно, что великанша, пытаясь слезть с горных круч, упала в пропасть" 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('blind_giant_mountain',None)
    return

label lb_ttg_mount_blind1_mermaid_dead:
    call lb_ttg_show(place='mountain') from _call_lb_ttg_show_06
    $ text = u'Русалка в горах - грустное зрелище. Печальное. И мёртвое. \n\n Слепая русалка - тем более.'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)\
    $ game.chronik.death('blind_mermaid_mountain',None)
    'Рождённый плавать летать не может. Русалка в горах - грустное зрелище. Печальное. И мёртвое.\n\nСлепая русалка - тем более.' 
    return

label lb_ttg_mount_blind1_dead:
    call lb_ttg_show(place='mountain') from _call_lb_ttg_show_07
    '[game.girl.name] спутает медленно и аккуратно. Увы, когда не видишь, куда идти, возможны всяческие непритности! Например, после очередного шага камни под ногой [game.girl.name_r] начинают ехать, и женщина с криком устремляется к пропасти.'
    $ text = u"Поэтому закономерно, что %s, пытаясь слезть с горных круч, упала в пропасть" % game.girl.name
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('blind_mountain',None)
    return

label lb_ttg_ice_blind1_ice_save:
    call lb_ttg_show(place='mountain') from _call_lb_ttg_show_08
    $ text = u"Но даже слепая йотунша способна выжить на леднике. Несмотря на все опасности ледяных склонов, %s добралась до родных мест." 
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.save_girl()
    return

label lb_ttg_ice_blind1_ice_dead:
    call lb_ttg_show(place='mountain') from _call_lb_ttg_show_09
    '[game.girl.name] спутает медленно и аккуратно. судя по её внутреннему ощущению, она почти добралась до родных мест! \n\nЙети атакует йотуншу абсолютно неожиданно. Кажется, сегодня у монстра будет романтический вечер, совмещённый с романтическим ужином!'
    $ text = u"Несмотря на это, йотунша почти добралась до родичей. Но справиться с устроившим засаду йети %s оказалось не под силу." % game.girl.name_d
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('blind_ice_ice',None)
    return

label lb_ttg_ice_blind1_dead:
    call lb_ttg_show(place='mountain') from _call_lb_ttg_show_10
    'Холодно. \n\nВыбраться с ледяных полей непросто, даже пребывая в добром здравии. Когда ты не видишь, куда идти - тем паче. [game.girl.name] сидит, съежившись и прижавшись к какой-то скале, и тщетно пытается согреться. Впрочем, это беспокоит её всё менше и меньше. Сознание постепенно растворяется в какой-то дымке.\n\n Холодно-холодно-холодно-холодно...'
    $ text = u"Поэтому закономерно, что %s, спускаясь с горных ледников, замёрзла насмерть." % game.girl.name
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('blind_ice',None)
    return

label lb_ttg_fire_blind1_fire_save:
    call lb_ttg_show(place='mountain') from _call_lb_ttg_show_11
    $ text = u"Но даже слепая ифритка способна выжить среди гейзеров и лавы. Несмотря на все опасности вулканического плато, %s добралась до родных мест." 
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.save_girl()
    return

label lb_ttg_fire_blind1_fire_dead:
    call lb_ttg_show(place='mountain') from _call_lb_ttg_show_12
    '[game.girl.name] спутает медленно и аккуратно. судя по её внутреннему ощущению, она почти добралась до родных мест! \n\nДэв атакует ифритку абсолютно неожиданно. Кажется, сегодня у монстра будет романтический вечер, совмещённый с романтическим ужином!'
    $ text = u"Несмотря на это, ифритка почти добралась до родичей. Но справиться с устроившим засаду дэвом %s оказалось не под силу." % game.girl.name_d
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('blind_fire_fire',None)
    return

label lb_ttg_fire_blind1_dead:
    call lb_ttg_show(place='mountain') from _call_lb_ttg_show_13
    'Жарко. \n\nВыбраться с вулканического плато непросто, даже пребывая в добром здравии. Когда ты не видишь, куда идти - тем паче. [game.girl.name] медленно пятиться от палящего жара, оступается и падает в озеро кипящей лавы.'
    $ text = u"Поэтому закономерно, что %s, спускаясь с вулканического плато, упала в лавовое озеро." % game.girl.name
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('blind_fire',None)
    return

label lb_ttg_gnome_blind1_dead:
    $ current_image='img/bg/special/moria.jpg'
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    'Тьма.\n\nВыбраться из Подгорных чертогов непросто, даже пребывая в добром здравии. Без глаз - тем паче. [game.girl.name] медленно тащится наугад сквозь тьмы коридоров. Где она? Как выбраться отсюда? Возможно, она уже несколько раз прошла мимо выхода?\n\nБездонный колодец положил конец её напрасным раздумьям.'
    $ text = u"Поэтому закономерно, что %s заблудилась в Подгорных чертогах и упала в бездонный колодец." % game.girl.name
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('blind_underground',current_image)
    return

label lb_ttg_elf_blind1_dead:
    call lb_ttg_show(place='forest') from _call_lb_ttg_show_14
    'Несть числа опасностям осквернённого леса. Плотоядные животные, плотоядные деревья, плотоядные кустарники, плотоядная трава. Большинство монстров питается не только и не столько мясом, сколько болью своих жертв.\n\nНеизвестно, что стало с ослеплённой [game.girl.name_t] в этом чудовищном месте. Но на опушку она так и не выбралась.'
    $ text = u"Поэтому закономерно, %s так и не смогла выбраться из осквернённого леса" % game.girl.name
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('blind_elf',None)
    return

label lb_ttg_cloud_blind1_titan_save:
    call lb_ttg_show(place='sky') from _call_lb_ttg_show_15
    $ text = u"Но даже слепая титанида чувствует себя в небесах, как дома. %s с лёгкостью добралась до родных мест." 
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.save_girl()
    return

label lb_ttg_cloud_blind1_dead:
    call lb_ttg_show(place='sky') from _call_lb_ttg_show_16
    'Замок величественно парит в облаках. [game.girl.name] отчаянно цепляется кончиками пальцев за край скалы. Свистит ветер, разжимаются пальцы. [game.girl.name] кричит, и воздушный океан принимает её в свои объятия. \n\nЭксперимент показал: отсутствие глаз никак не влияет на результат падения с большой высоты!'
    $ text = u"Впрочем, при падении из облачного замка наличие глаз %s никак бы не помогло!" % game.girl.name_d
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('blind_cloud',None)
    return

label lb_ttg_usual_blind1_giant_save:
    call lb_ttg_show(place='forest') from _call_lb_ttg_show_17
    $ text = u"Но даже слепая великанша способна на многое. Плутая и голодая, отбиваясь от прожорливых волков и похотливых монстров, %s всё-таки добралась до родных мест.\n\n Иногда размер имеет значение." % game.girl.name
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.save_girl()
    return

label lb_ttg_usual_blind1_mermaid_dead:
    call lb_ttg_show(place='forest') from _call_lb_ttg_show_18
    $ text = u'Русалка, сидящая на ветвях - грустное зрелище. Печальное. И мёртвое. \n\n Слепая русалка - тем более.'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('blind_mermaid_usual',None)
    'Русалка, сидящая на ветвях - прекрасный поэтический образ. Вот только выживанию сама русалка, оказавшись в подобном положении, погибает очень быстро.\n\nСлепая русалка - тем более.' 
    return

label lb_ttg_usual_blind1_save:
    call lb_ttg_show(place='forest') from _call_lb_ttg_show_19
    $ text = u"Но даже слепую не следует хоронить раньше срока. Плутая и голодая, ежечасно рискуя нарваться на прожорливых волков и похотливых монстров, %s совершила невозможно и добрела до обжитых мест. \n\nСможет ли она выжить и дальше - другой вопрос." % game.girl.name
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.save_girl()
    return

label lb_ttg_usual_blind1_dead:
    call lb_ttg_show(place='forest') from _call_lb_ttg_show_20
    $ text = u'Неудивительно, что %s так и не добралась до обжитых мест.' %game.girl.name
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('blind_usual',None)
    'Плутая и голодая, ежечасно рискуя нарваться на прожорливых волков и похотливых монстров, [game.girl.name] наугад пробиралась по лесу, пытаясь добраться до обжитых мест.\n\n Но у неё это не получилось.' 
    return

# Теперь - удачные побеги слепых, открывших "внутреннее зрение"

label lb_ttg_save(art,text):
    if art == 'undeground':
      $ current_image='img/bg/special/moria.jpg'
      $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
      hide bg
      show expression current_image as bg
      nvl clear
      $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    else:
      call lb_ttg_show(place=art) from _call_lb_ttg_show_21
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.save_girl()
    return

label lb_ttg_underwater_cripple:
    call lb_ttg_show(place='sea') from _call_lb_ttg_show_22
    if game.girl.type=='mermaid' or game.girl.type=='siren':
      '[game.girl.name] беззвучно открывает и закрывает рот - и это всё, что она может поделать. Её тело медленно погружается на глубину, запредельную даже для морского народа.'
      $ text = u'%s выкинул искалеченную %s из своего логова, и морская дева нашла вечный покой в глубоководном желобе' %(game.dragon.fullname, game.girl.name_v)
      $ game.chronik.death('cripple_underwater_mermaid',None)
    else:
      'Безрукое и безногое тело [game.girl.name_r] медленно погружается всё глубже и глубже, и вода прихотливо играет с её длинными волосами.'
      $ text = u'%s выкинул искалеченную %s из своего логова, и она нашла вечный покой на морском дне.' %(game.dragon.fullname, game.girl.name_v)
      $ game.chronik.death('cripple_underwater',None)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_ttg_peak_cripple:
    call lb_ttg_show(place='mountain') from _call_lb_ttg_show_23
    '[game.girl.name] беззвучно открывает и закрывает рот - и это всё, что она может поделать. Её тело обдувает свежий и чистый горный воздух, и где-то там, в головокружительной синеве, кружат орлы.'
    $ text = u'%s выкинул искалеченную %s из своего логова, и она нашла вечный покой среди горных пиков' %(game.dragon.fullname, game.girl.name_v)
    $ game.chronik.death('cripple_peak',None)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_ttg_ice_cripple:
    call lb_ttg_show(place='mountain') from _call_lb_ttg_show_24
    if game.girl.type=='ice':
      '[game.girl.name] не боится холода - но какой в этом толк, когда не можешь даже сдвинуться с места? \n\n Грузно ступая по снегу, к искалеченной йотунше приближается йети. Кажется, сегодня у него будет романтический вечер, совмещённый с романтическим ужином.'
      $ text = u'%s выкинул %s из своего логова, и искалеченную йотуншу изнасиловал и сожрал йети.' %(game.dragon.fullname, game.girl.name_v)
      $ game.chronik.death('cripple_ice_ice',None)
    else:
      'Безрукое и безногое тело [game.girl.name_r] дрожит мелкой дрожью и постепенно коченеет. [game.girl.name_d] безумно хочется согреться, но она может лишь бессильно хлопать глазами.'
      $ text = u'%s выкинул искалеченную %s из своего логова, и она замёрзла на горном леднике.' %(game.dragon.fullname, game.girl.name_v)
      $ game.chronik.death('cripple_ice',None)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_ttg_fire_cripple:
    call lb_ttg_show(place='mountain') from _call_lb_ttg_show_25
    if game.girl.type=='fire':
      '[game.girl.name] не боится жара - но какой в этом толк, когда не можешь даже сдвинуться с места? \n\n Грузно ступая по вулканическому пеплу, к искалеченной ифритке приближается дэв. Кажется, сегодня у него будет романтический вечер, совмещённый с романтическим ужином.'
      $ text = u'%s выкинул %s из своего логова, и искалеченную ифритку изнасиловал и сожрал дэв.' %(game.dragon.fullname, game.girl.name_v)
      $ game.chronik.death('cripple_fire_fire',None)
    else:
      'Безрукое и безногое тело [game.girl.name_r] дрожит покрыто липким потом. Кажется, ещё немного, и оно начнёт постепенно прожариваться. [game.girl.name_d] безумно хочется хоть глоточка прохладного воздуха, но она может лишь бессильно хлопать глазами.'
      $ text = u'%s выкинул искалеченную %s из своего логова, и она меленно испеклась на вулканическом плато.' %(game.dragon.fullname, game.girl.name_v)
      $ game.chronik.death('cripple_fire',None)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_ttg_underground_cripple:
    $ current_image='img/bg/special/moria.jpg'
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    'Воды. Как же хочется хоть глоточка воды. Но здесь, в бесконечном подземном лабиринте, [game.girl.name_v] обволакивает лишь сухая темнота и тишина. \n\n Сейчас мечтает [game.girl.name] о том, чтобы дотянуться до вены и испить собственной крови. Увы, этой мечте не суждено сбыться!'
    $ text = u'%s выкинул искалеченную %s из своего логова, и она медленно и мучительно скончалась от жажды' %(game.dragon.fullname, game.girl.name_v)
    $ game.chronik.death('cripple_underground',None)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_ttg_elf_cripple:
    call lb_ttg_show(place='forest') from _call_lb_ttg_show_26
    '[game.girl.name] чувствует, как сквозь её тело медленно прорастает трава. Ей хочется бежать, бежать отсюда без оглядки. Но всё, что она может - лишь бессильно хлопать глазами.\n\nЭто была самая незабываемая ночь в жизни [game.girl.name_r]. А под утро она успела увидеть, как у неё на груди распустился прекрасный цветок.'
    $ text = u'%s выкинул искалеченную %s из своего логова, и заколдованная трава с удовольствием усвоила девичье тело.' %(game.dragon.fullname, game.girl.name_v)
    $ game.chronik.death('cripple_elf',None)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_ttg_cripple:
    call lb_ttg_show(place='forest') from _call_lb_ttg_show_27
    '[game.girl.name] беззвучно открывает и закрывает рот - и это всё, что она может поделать. Её тело обдувает лесной ветерок, по коже ползают мухи, и где-то неподалёку раздаётся настырное воронье карканье.\n\nКажется, её дальнейшая жизнь будет насыщенной, но недолгой.'
    $ text = u'%s выкинул искалеченную %s из своего логова, и она нашла вечный покой в глухом лесу' %(game.dragon.fullname, game.girl.name_v)
    $ game.chronik.death('cripple_usual',None)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_ttg_cripple_save:
    call lb_ttg_show(place='forest') from _call_lb_ttg_show_28
    '[game.girl.name] беззвучно открывает и закрывает рот - и это всё, что она может поделать. Её тело обдувает лесной ветерок, по коже ползают мухи, и где-то неподалёку раздаётся старушечье причитание. Что?!\n\nСтарушка, собирающая грибы, нашла искалеченное тело [game.girl.name_r] и кликнула парней из ближайшей деревни. [game.girl.name] осталась жива. Впрочем, разве это жизнь?!'
    $ text = u'%s выкинул искалеченную %s из своего логова. Впрочем, её вовремя нашла сердобольная старушка, и крестьяне отнесли %s в деревню.' %(game.dragon.fullname, game.girl.name_v,game.girl.name_v)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.save_girl()
    return



label lb_dragon_lair:
    $ place = game.lair.type_name
    show place as bg
    return

label lb_cripple_impaled:
    hide bg
    nvl clear
    if ('servant' in game.lair.upgrades):
      show expression 'img/scene/spawn/kobold.jpg' as bg
    elif ('gremlin_servant' in game.lair.upgrades):
      show expression 'img/bg/special/gremlins.jpg' as bg
    'Радостно переговариваясь, драконьи слуги собираются вокруг искалеченного женского тела. Им ужасно надоело обихаживать этот обрубок, и теперь они спешат устроить захватывающий финальный аттракцион'
    hide bg
    nvl clear
    $ current_image = 'img/scene/cripple_impaled.jpg'
    show expression current_image as bg
    '[game.girl.name] стискивает зубы изо всех сил, так крепко, как только можно. Невозможно, мучительно тянет их разжать - но [game.girl.name] пока удерживает на весу своё искалеченное тело. А где-то там, внизу, лоно ласкает остриё кола. Стоит разжать зубы - и всё будет кончено. Так стоит ли цепляться за такую жизнь? \n\n Быть или не быть?'
    $ text = u'Драконьи слуги устроили себе роскошный аттракцион. Они дали %s в зубы деревяшку и повесили над острым колом. \n\nК их удивлению, %s целялась за жизнь очень долго.' % (game.girl.name_d,game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.death('cripple_impaled',current_image)
    return

label lb_cripple_die: # Погибает из-за ненадлежащего ухода.
    hide bg
    nvl clear
    $ current_image= game.girl.cripple_image
    show expression current_image as bg
    $ game.chronik.death('cripple_die',current_image)
    game.girl 'Ааа...'
    $ text = u'%s абсолютна беспомощна. Драконьи слуги ухаживают за ней, кормят, поят, убирают. Вот только нудное занятие надоедает им крайне быстро. Из-за их небрежания у %s начались пролежни. Потом некроз. Потом сепсис. Потом летальный исход.' %(game.girl.name, game.girl.name_v)
    '[text]'
    $ text = u"Драконьи слуги ухаживали за %s спустя рукава, и она умерла от заражения крови.\n\n" %(game.girl.name_t)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_cripple_alive: # Выживает.
    hide bg
    nvl clear
    $ current_image= game.girl.cripple_image
    show expression current_image as bg
    game.girl 'Ааа...'
    $ text = u'%s абсолютна беспомощна. Драконьи слуги ухаживают за ней, кормят, поят, убирают. Дни тянутся бесконечной унылой чередой, единственное изменение в которой - медленно растущий животик. %s ждёт рождения отродья как освобождения. Может быть,  хоть тогда от неё наконец-то избавятся?' %(game.girl.name, game.girl.name)
    '[text]'
    $ text = u"Благодаря тщательному уходу драконьих слуг %s дожила до рождения ребёнка\n\n" %(game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_blind_alive: # Выживает.
    hide bg
    nvl clear
    $ place = game.lair.type_name
    show place as bg
    game.girl 'Глаза! Мои глаза!'
    'Слепая и неприкаянная, [game.girl.name] слоняется по логову дракона'
    return

# Эвенты поедания девушек слугами дракона
label lb_girl_kitchen:
    if ('servant' in game.lair.upgrades): 
      show expression 'img/scene/spawn/kobold.jpg' as bg
    elif ('gremlin_servant' in game.lair.upgrades):
      show expression 'img/bg/special/gremlins.jpg' as bg
    $ text = u'Мелкие монстрики по достоинству оценили девичье тело. '
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('girl_kitchen', True)  
    $ choices = [
        ("lb_girl_kitchen_fry", 10),
        ("lb_girl_kitchen_boil", 10),
        ("lb_girl_kitchen_spit", 10)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

label lb_girl_kitchen_fry:
    $ text = u'Они положили его на противень, обмазали соусом, запекли и съели с огромным аппетитом. ' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('girl_kitchen_fry', True)  
    $ current_image=get_random_image("img/scene/kitchen/fry")
    $ game.chronik.death('kitchen_fry',current_image)
    show expression current_image
    pause (500.0)
    hide place  
    return

label lb_girl_kitchen_boil:
    $ text = u'Они погрузили его к огромный котёл, добавили овощей и специй по вкусу, сварили и съели с огромным аппетитом. ' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image=get_random_image("img/scene/kitchen/boil")
    $ game.chronik.death('kitchen_boil',current_image)
    $ game.girls_list.description('girl_kitchen_boil', True)
    show expression current_image
    pause (500.0)
    hide place  
    return

label lb_girl_kitchen_spit:
    $ text = u'Они насадили его на вертел, обмазали соусом, пожарили на открытом огне и съели с огромным аппетитом. ' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('girl_kitchen_spit', True)
    $ current_image=get_random_image("img/scene/kitchen/spit")
    $ game.chronik.death('kitchen_spit',current_image)
    show expression current_image
    pause (500.0)
    hide place  
    return

# Эвенты, связанные с беременностью девушек на свободе.

label lb_show_home:
    $ g_type=game.girl.type
    hide bg
    if g_type == 'peasant':
      $ current_image='img/bg/special/village.jpg'
      show expression current_image as bg
    elif g_type == 'citizen':
      $ current_image='img/bg/city/market.jpg'
      show expression current_image as bg
    elif g_type == 'princess':
      $ current_image='img/bg/special/bedroom.jpg'
      show expression current_image as bg
    elif g_type == 'elf':
      $ current_image='img/bg/special/enchanted_forest.jpg'
      show expression current_image as bg
    elif g_type == 'mermaid' or g_type == 'siren':
      $ place = 'sea'
      $ current_image=get_place_bg(place)
      show expression current_image as bg
    elif g_type == 'ice':
      $ current_image='img/bg/lair/icecastle.jpg'
      show expression current_image as bg
    elif g_type == 'fire':
      $ current_image='img/bg/lair/volcanoforge.jpg'
      show expression current_image as bg
    elif g_type == 'titan':
      $ current_image='img/bg/special/cloud_castle.jpg'
      show expression current_image as bg
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    nvl clear
    return

label lb_old_maid:   # Старая дева
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    game.girl.third '[game.girl.name] слишком стара. Она ещё может рожать людей, но не способна зачать отродье дракона'
    $ text = u'Но за долгие годы %s так и не притронулся к девушке. После тридцати лет женщины больше не способны зачать отродье дракона.\n\n' % (game.dragon.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
    $ game.girl.old=True
    return

label lb_willing_wait:   # Старая дева
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    if game.girl.nature == 'innocent':
      game.girl.third '[game.girl.name] дисциплинированно томится в темнице, замаливая свои будущие грехи'
    elif game.girl.nature == 'proud':
      game.girl.third '[game.girl.name] дисциплинированно томится в темнице, планируя свою будущую месть'  
    elif game.girl.nature == 'lust':
      game.girl.third '[game.girl.name] дисциплинированно томится в темнице, предаваясь греховным мечтаниям'    
    return

label lb_pregnant_blind:
    call lb_show_home from _call_lb_show_home_1
    if g_type is not 'ogre':
      game.girl 'Я не могу держать своё положение в тайне. Придётся признаться родичам.'
      $ text = u'Оказавшись в родных краях, ослепшая %s не могла скрывать свою чудовищную беременность и честно рассказала родственникам о произошедшем. ' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    if g_type=='peasant':
      if (random.randint(1,5) == 1):
        'Тяжела крестьянская доля, и нечем там кормить нахлебников. Конечно, в крестьянском быте найдётся, куда пристроить слепую работницу, но - беременную от дракона? К счастью, [game.girl.name] не ошиблась с выбором родственника. Её двоюродная тётя приютила ослеплённую племянницу в своём доме. Услышав, от кого [game.girl.name] понесла своё дитя, она сохранила это в секрете.\n\nХорошо жить в любящей семье!'
        game.girl 'Но рожать я буду за околицей. Мало ли.'
        $ text = u'Двоюродная тётя приютила слепую и скрыла её чудовищную беременность.\n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
      else:
        'Тяжела крестьянская доля, и нечем там кормить нахлебников. Конечно, в крестьянском быте найдётся, куда пристроить слепую работницу, но - беременную от дракона? Узнав об этом, родственники пришли в ужас и обнародовали эту чудовищную весть. '
        $ text = u'Они пришли в ярость и обнародавали этот ужасающий факт. \n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
        call lb_girl_execution from _call_lb_girl_execution_2
    elif g_type=='citizen':
      if (random.randint(1,2) == 1):
        'Участь [game.girl.name_r] стала для её родственников страшным ударом. Потерять зрение... сложно представить более печальный исход. И это не говоря уже о её неестественной беременности! В конце концов этот факт решили скрыть - что было несложно, ведь теперь [game.girl.name]  общалась только с самыми проверенными слуги.\n\nХорошо жить в любящей семье!'
        game.girl 'Но рожать я буду за городом. Мало ли.'
        $ text = u'Родственники-горожане приютили слепую и надёжно скрыли её чудовищную беременность.\n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
      else:
        'Участь [game.girl.name_r] стала для её родственников страшным ударом. Потеря зрение, неестественная беременность... есть от чего прийти в отчаяние! И скрывать такое чревато - кто знает, КОГО родит [game.girl.name]? С тяжёлым сердцем они обнародовали этот чудовищный факт'
        $ text = u'Они пришли в отчаяние и обнародавали этот ужасающий факт. \n\n'
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
        call lb_girl_execution from _call_lb_girl_execution_3
    elif g_type=='mermaid':
      if (random.randint(1,2) == 1):
        'Участь [game.girl.name_r] стала для её родственников страшным ударом. Потерять зрение... сложно представить более печальный исход. И это не говоря уже о её неестественной беременности! В конце концов этот факт решили скрыть - что было несложно, ведь теперь за [game.girl.name_t]  ухаживали только две самых преданных сестры-русалки. \n\nХорошо жить в любящей семье!'
        game.girl 'Но рожать я всё равно поплыву к Одинокому рифу. Мало ли.'
        $ text = u'Родственники-русалки стали заботиться о слепой и надёжно скрыли её чудовищную беременность.\n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
      else:
        'Участь [game.girl.name_r] стала для её родственников страшным ударом. Потеря зрение, неестественная беременность... есть от чего прийти в отчаяние! И скрывать такое чревато - кто знает, КОГО родит [game.girl.name]? Какие беды навлечёт погибельное дитя на морской народ? С тяжёлым сердцем они обнародовали этот чудовищный факт'
        $ text = u'Они пришли в отчаяние и обнародавали этот ужасающий факт. \n\n'
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
        call lb_girl_execution from _call_lb_girl_execution_5
    elif g_type=='princess':
      if not (random.randint(1,3) == 1):
        'Участь [game.girl.name_r] стала для её родственников страшным ударом. Потерять зрение... сложно представить более печальный исход. И это не говоря уже о её неестественной беременности! В конце концов этот факт решили скрыть - что было несложно, ведь теперь за [game.girl.name_t]  ухаживали только слуги, чья преданность была проверена поколениями.\n\nХорошо жить в любящей семье!'
        game.girl 'Но рожать я всё равно буду в летнем поместье... а ещё лучше - за пределами летнего поместья. Мало ли.'
        $ text = u'Родственники-аристократы окружили слепую любовью и заботой и надёжно скрыли её чудовищную беременность.\n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
      else:
        'Участь [game.girl.name_r] стала для её родственников страшным ударом. Потеря зрение, неестественная беременность... есть от чего прийти в отчаяние! И если это вскроется - ущерб чести рода будет неоценим. С тяжёлым сердцем аристократы раскрыли чудовищную беременность [game.girl.name_r].'
        $ text = u'Опасаясь за честь рода, они обнародавали этот ужасающий факт. \n\n'
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
        call lb_girl_execution from _call_lb_girl_execution_6
    elif g_type=='elf':
      if not (random.randint(1,5) == 1):
        'Участь [game.girl.name_r] стала для её родственников страшным ударом. Потерять зрение... сложно представить более печальный исход. Чары альвов могут многое, но вернуть глаза? Беременность [game.girl.name_r] только усугубляла ситуацию. Это было чудовищное, вопиющее нарушение природного равновесия. Но и убийство одной из Дочерей Дану было нарушением не меньшим! Посовешавшись, Круг Друидов решил оставить жизнь [game.girl.name_d и попытатьься исцелить её.\n\nХорошо жить в среди развитого и гуманного народа!'
        game.girl 'Но рожать я всё равно буду в Тёмном лесу. Мало ли.'
        $ text = u'Альвы стали заботиться о слепой, примирившись с фактом её чудовищной беременности.\n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
      else:
        'Участь [game.girl.name_r] стала для её родственников страшным ударом. Потерять зрение... сложно представить более печальный исход. Чары альвов могут многое, но вернуть глаза? Беременность [game.girl.name_r] только усугубляла ситуацию. Это было чудовищное, вопиющее нарушение природного равновесия. Но и убийство одной из Дочерей Дану было нарушением не меньшим! Посовешавшись, Круг Друидов прнял тяжёлое, но единственно верное решение.'
        $ text = u'Круг друидов, опасаясь нарушения природного равновесия, принял тяжёлое, но единственно верное решение.\n\n' 
        call lb_girl_execution from _call_lb_girl_execution_7
    elif g_type=='ogre':
      game.girl 'Каждого, кто полезть ко мне, я убивать и трахать!'
      'Уж кто-то, а [game.girl.name] сумеет о себе позаботиться, даже будучи слепой!'
      $ text = u'Даже ослепнув, %s сумела о себе позаботиться.\n\n' % (game.girl.name)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
    elif g_type=='siren':
      'Собравшись на вече, тритоны и сирены долго думали, чем можно помочь ослепшей сестре. Морские великаны живучи, но под силу ли им вновь стать зрячими? В конце концов старейшины решили дождаться окончания беременности, а потом уже приниматься за лечение.\n\n'
      game.girl 'Но рожать я всё равно поплыву к Одинокому рифу. Мало ли.'
      $ text = u'Тритоны и сирены решили подождать окончания беременности, а потом уже думать о помощи %s \n\n' % (game.girl.name_d)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    elif g_type=='ice':
      'Инеистые великаны, собравшись на тинге, долго обсуждали судьбу [game.girl.name_r]. Можно ли как-то помочь несчастной дочери их народа и вновь даровать ей зрение? В конце концов собрание решило дождаться окончания беременности, а потом уже приниматься за лечение.\n\n'
      game.girl 'Но рожать я всё равно буду у Эвесайлогвудчорра. Мало ли.'
      $ text = u'Инеистые великаны решили подождать окончания беременности, а потом уже думать о помощи %s \n\n' % (game.girl.name_d)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
    elif g_type=='fire':
      'Огненные великаны, собравшись на анджомане, долго обсуждали судьбу [game.girl.name_r]. Можно ли как-то помочь несчастной дочери их народа и вновь даровать ей зрение? В конце концов собрание решило дождаться окончания беременности, а потом уже приниматься за лечение.\n\n'
      game.girl 'Но рожать я всё равно буду у Эйяфльятлайокудля. Мало ли.'
      $ text = u'Огненные великаны решили подождать окончания беременности, а потом уже думать о помощи %s \n\n' % (game.girl.name_d)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
    elif g_type=='titan':
      'Титаны, собравшись на экклесии, долго обсуждали судьбу [game.girl.name_r]. Неужели Боги останутся глухи к её мольбам и так и не вернут ей зрение? В конце концов собрание решило дождаться окончания беременности, а потом уже приниматься за лечение.\n\n'
      game.girl 'Но рожать я всё равно буду не в Облачном замке. Мало ли.'
      $ text = u'Титаны решили подождать окончания беременности, а потом уже думать о помощи %s \n\n' % (game.girl.name_d)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
    return

label lb_pregnant_cripple:
    call lb_show_home from _call_lb_show_home_3
    game.girl 'Ааа...'
    $ current_image = game.girl.cripple_image
    if g_type=='peasant':
      if (random.randint(1,10) == 1):
        'Тяжела крестьянская доля, и нечем там кормить нахлебников. Но даже в столь тяжёлых находятся добрые люди. Двоюродная тётя [game.girl.name_r] приютила искалеченную племянницу в своём доме. Она быстро поняла, от кого [game.girl.name] понесла своё дитя, но сохранила это в секрете. Тётя и её родственники ухаживали за [game.girl.name_t], поддерживая жизнь в её недвижимом теле.\n\nАвось, обойдётся, а?'
        $ text = u'Двоюродная тётя приютила калеку и скрыла её чудовищную беременность.\n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
      else:
        show expression current_image as bg
        'Тяжела крестьянская доля, и нет в деревенском доме нахлебников. Родственники не обрадовались возвращению [game.girl.name_r], по крайней мере - возвращению в таком виде. После долгих уговоров и споров ей дали смертельную доозу отвара сонной травы.'
        $ text = u'Крестьяне не могли содержать калеку, и ей дали смертельную дозу отвара сонной травы.\n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
        $ game.chronik.death('cripple_pregnant_peasant',current_image)
        $ game.girl.pregnant=0  
    elif g_type=='citizen':
      if (random.randint(1,3) == 1):
        'Участь [game.girl.name_r] стала для её родственников колоссальным ударом. У купцов было достаточно средств, чтобы содержать увечную дочь, но что делать с её неестественной беременностью? В конце концов этот факт решили скрыть - что было несложно, ведь за [game.girl.name_t]  ухаживали только самые проверенные слуги.\n\nАвось, обойдётся, а?'
        $ text = u'Родственники-горожане стали заботиться об инвалидке и скрыли её чудовищную беременность.\n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
      else:
        show expression current_image as bg
        'Участь [game.girl.name_r] стала для её родственников колоссальным ударом. У купцов было достаточно средств, чтобы содержать увечную дочь, но что делать с её неестественной беременностью? После долгих уговоров и споров её близкие решили, что риск слишком велик, а подобное существование немногим лучше смерти. Родственники  дали [game.girl.name_d] смертельную дозу сонной микстуры.'
        $ text = u'Родственники-горожане, опасаясь беременности дочери и решив не обрекать её на участь хуже смерти, дали %s смертельную дозу сонной микстуры.\n\n' % (game.girl.name_d)
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
        $ game.chronik.death('cripple_pregnant_citizen',current_image)
        $ game.girl.pregnant=0  
    elif g_type=='mermaid':
      if (random.randint(1,3) == 1):
        'Участь [game.girl.name_r] стала для её родственников колоссальным ударом. У морского народа достаточно ресурсов, чтобы содержать увечную дочь, но что делать с её неестественной беременностью? В конце концов этот факт решили скрыть - что было несложно, ведь за [game.girl.name_t]  ухаживали только парочка самых преданных русалок.\n\nАвось, обойдётся, а?'
        $ text = u'Родственники-русалки стали заботиться об инвалидке  и скрыли её чудовищную беременность.\n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
      else:
        show expression current_image as bg
        'Участь [game.girl.name_r] стала для её родственников колоссальным ударом. У морского народа достаточно ресурсов, чтобы содержать увечную дочь, но что делать с её неестественной беременностью? После долгих уговоров и споров её близкие решили, что риск слишком велик, а подобное существование немногим лучше смерти. Родственники  дали [game.girl.name_d] смертельную дозу сонных водорослей.'
        $ text = u'Родственники-русалки, опасаясь беременности дочери и решив не обрекать её на участь хуже смерти, дали %s смертельную дозу сонных водорослей.\n\n' % (game.girl.name_d)
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
        $ game.chronik.death('cripple_pregnant_mermaid',current_image)
        $ game.girl.pregnant=0  
    elif g_type=='princess':
      if (random.randint(1,2) == 1):
        'Участь [game.girl.name_r] стала для её родственников колоссальным ударом. У аристократов достаточно средств, чтобы прокормить хоть десяток калек, но разве это исцелит увечья [game.girl.name_r]? И что делать с её неестественной беременностью? В конце концов этот факт решили скрыть - что было несложно, ведь за [game.girl.name_t] ухаживала только парочка слуг, чья верность была проверена поколениями.\n\nАвось, обойдётся, а?'
        $ text = u'Родственники-аристократы стали заботиться об инвалидке и скрыли её чудовищную беременность.\n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
      else:
        show expression current_image as bg
        'Участь [game.girl.name_r] стала для её родственников колоссальным ударом. У аристократов достаточно средств, чтобы прокормить хоть десяток калек, но разве это исцелит увечья [game.girl.name_r]? И что делать с её неестественной беременностью? После долгих уговоров и споров её близкие решили, что если это когда-нибудь вскроется, чести их рода будет нанесён колоссальный урон. Родственники отравили [game.girl.name_v] с помощью сонного камня.'
        $ text = u'Родственники-аристократы, опасаясь урона чести своего рода, отравили %s с помощью сонного камня.\n\n' % (game.girl.name_v)
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
        $ game.chronik.death('cripple_pregnant_princess',current_image)
        $ game.girl.pregnant=0  
    elif g_type=='elf':
      if not (random.randint(1,3) == 1):
        'Участь [game.girl.name_r] стала для её родственников колоссальным ударом. Чары альвов могут многое, но исцеление таких ран лежит на пределах возможного для Детей Дану, а скорее, даже за их пределами. Беременность [game.girl.name_r] только усугубляла ситуацию. Это было чудовищное, вопиющее нарушение природного равновесия. Но и убийство одной из Дочерей Дану было нарушением не меньшим! Посовешавшись, Круг Друидов решил оставить жизнь [game.girl.name_d] и попытатьься исцелить её.\n\nАвось, обойдётся, а? '
        $ text = u'Альвы стали заботиться об инвалидке, примирившись с фактом её чудовищной беременности.\n\n' 
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
      else:
        show expression current_image as bg
        'Участь [game.girl.name_r] стала для её родственников колоссальным ударом. Чары альвов могут многое, но исцеление таких ран лежит на пределах возможного для Детей Дану, а скорее, даже за их пределами. Беременность [game.girl.name_r] только усугубляла ситуацию. Это было чудовищное, вопиющее нарушение природного равновесия. Но и убийство одной из Дочерей Дану было нарушением не меньшим! Долго совещался Круг Друидов, спорным и тяжёлым было его решение. Но, увы. необхожимым и неизбежным. На [game.girl.name_v] наложили сонные чары, и проснуться ей было уже не суждено.'
        $ text = u'Альвы, опасаясь нарушения природного равновесия, убили %s с помощью сонных чар.\n\n' % (game.girl.name_v)
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
        $ game.chronik.death('cripple_pregnant_elf',current_image)
        $ game.girl.pregnant=0
    elif g_type=='ogre':
      show expression current_image as bg
      'Искалеченную [game.girl.name_v] съели её же сородичи. Особенности огрского менталитета, ничего не поделаешь!'
      $ text = u'Искалеченную %s съели её же сородичи.\n\n' % (game.girl.name_v)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
      $ game.chronik.death('cripple_ogre',current_image)
      $ game.girl.pregnant=0  
    elif g_type=='siren':
      'Тритоны и сирены долго думали, чем можно помочь искалеченной сестре. Морские великаны живучи, но под силу ли им отрастить потерянные конечности? В конце концов старейшины решили дождаться окончания беременности, а потом уже приниматься за лечение.\n\nГуманное решение.\n\n'
      $ text = u'Тритоны и сирены решили подождать окончания беременности, а потом уже думать о помощи %s \n\n' % (game.girl.name_d)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    elif g_type=='ice':
      'Инеистые великаны, собравшись на тинге, долго обсуждали судьбу [game.girl.name_r]. Можно ли как-то помочь несчастной дочери их народа? Ледяные великаны живучи, но под силу ли им отрастить потерянные конечности? В конце концов собрание решило дождаться окончания беременности, а потом уже приниматься за лечение.\n\nГуманное решение.\n\n'
      $ text = u'Инеистые великаны решили подождать окончания беременности, а потом уже думать о помощи %s \n\n' % (game.girl.name_d)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
    elif g_type=='fire':
      'Огненные великаны, собравшись на анджомане, долго обсуждали судьбу [game.girl.name_r]. Можно ли как-то помочь несчастной дочери их народа? Огненные великаны живучи, но под силу ли им отрастить потерянные конечности? В конце концов собрание решило дождаться окончания беременности, а потом уже приниматься за лечение.\n\nГуманное решение.\n\n'
      $ text = u'Огненные великаны решили подождать окончания беременности, а потом уже думать о помощи %s \n\n' % (game.girl.name_d)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
    elif g_type=='titan':
      'Титаны, собравшись на экклесии, долго обсуждали судьбу [game.girl.name_r]. Можно ли как-то помочь несчастной, неужели Боги останутся глухи к её мольбам? В конце концов собрание решило дождаться окончания беременности, а потом уже приниматься за лечение.\n\nГуманное решение.\n\n'
      $ text = u'Титаны решили подождать окончания беременности, а потом уже думать о помощи %s \n\n' % (game.girl.name_d)
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id) 
    return

label lb_cripple_birth_fail: # Отродье убивают при рождении
    $ spawn_type = game.girls_list.spawn_type
    $ spawn_image = 'img/scene/spawn/%s.jpg' % spawn_type
    hide bg
    show expression spawn_image as bg
    if spawn_type == 'poisonous_asp':
      'Когда тётя зашла в комнату к [game.girl.name_d], ядовитый аспид только-только вылупился из яйца. Однако эта решительная женщина не испугалась, схватила какую-то тряпку и прихлопнула аспида одним метким ударом!\n\nДа, если бы все женщины Вольных были такими, Тёмной Госпоже и её отродьям пришлось бы весьма солоно!'
    elif spawn_type == 'basilisk':
      'Когда тётя зашла в комнату к [game.girl.name_d], василиск только-только вылупился из яйца. Однако эта решительная женщина не испугалась, схватила стоящий у двери кол и воткнула его прямо в кокатрикса!\n\nВ тот день крестьянская семья ужинала наваристым куриным супом. Да, если бы все женщины Вольных были такими, Тёмной Госпоже и её отродьям пришлось бы весьма солоно!'
    elif spawn_type == 'winged_asp':
      'Когда служанка зашла в комнату к [game.girl.name_d], ядовитый аспид только-только вылупился из яйца. Однако эта решительная девушка не испугалась и схватила какую-то тряпку. Гад попался увёртливый, и за ним пришлось хорошенько погоняться по комнате, но импровизированная аспидобойка всё же нашла свою цель.\n\nДа, если бы все женщины Вольных были такими, Тёмной Госпоже и её отродьям пришлось бы весьма солоно!'
    elif spawn_type == 'kobold':
      'Когда служанка зашла в комнату к [game.girl.name_d], кобольд только-только вылупился из яйца. Однако эта решительная девушка не испугалась, схватила стоящий у двери кол и воткнула его прямо в мелкого поганца!\n\n Да, если бы все женщины Вольных были такими, Тёмной Госпоже и её отродьям пришлось бы весьма солоно!'
    elif spawn_type == 'krokk':
      'Младшая сестрёнка [game.girl.name_r], мучимая любопытством, пробралась в комнату к калеке. К сожалению, она сделала это в тот самый момент, когда из яйца уже вылупился крокк. От потрясения девочка завизжала изо всех сил. Крокк замешкался, оглушённый звуковым ударом, и прибежавшие взрослые забили мелкого поганца.\n\nДевочка выпуталась из ситуации без единой царапины. Но как эта травма скажется на её дальнейшей жизни?'
    elif spawn_type == 'lizardman':
      'Младшая сестрёнка [game.girl.name_r], мучимая любопытством, пробралась в комнату к калеке. К сожалению, она сделала это в тот самый момент, когда из яйца уже вылупился ящерик. От потрясения девочка завизжала изо всех сил. Ящерик замешкался, оглушённый звуковым ударом, и прибежавшие взрослые забили мелкого поганца.\n\nДевочка выпуталась из ситуации без единой царапины. Но как эта травма скажется на её дальнейшей жизни?'
    elif spawn_type == 'gargoyle':
      'Когда подруга зашла в комнату к [game.girl.name_d], горгуйль только-только вылупился из яйца. Однако эта решительная альва не испугалась и приложила летающего монстра заклинанием! Раненый в одно из крыльев, горгуйль потерял возможность к полёту, и альвы быстро уничтожили эту нечисть.\n\n Да, все девы альвов - решительные и боевые. Вот только для противостояния дракону решительности и храбрости зачастую недостаточно...'
    elif spawn_type == 'dragonborn':
      'Когда подруга зашла в комнату к [game.girl.name_d], драконорождённый только-только вылупился из яйца. Однако эта решительная альва не испугалась и приложила монстра заклинанием! Парализованный монстр ничего не смог противопоставить воинскому и колдовскому искусству Aein Sidhe.\n\n Да, все девы альвов - решительные и боевые. Вот только для противостояния дракону решительности и храбрости зачастую недостаточно...'
    elif spawn_type == 'octopus':
      'Когда русалка вплыла в покои [game.girl.name_r], ядовитый спрут только-только вылупился из яйца. Однако эта решительная морская дева не испугалась, схватила стоящий у входа трезубец и пронзила отвратительного монстра.  У новорождённого спрута не было ни единого шанса.\n\nДа, если бы все женщины Вольных были такими, Тёмной Госпоже и её отродьям пришлось бы весьма солоно!'
    elif spawn_type == 'sea_bastard':
      'Маленький братик [game.girl.name_r], мучимый любопытством, пробрался в запретную комнату к калеке. К сожалению, он сделала это в тот самый момент, когда из яйца уже вылупился рыбоглаз. Маленький водяной в ужасе поплыл прочь. Поднялась паника, рыбоглаза быстро нашли и убили.\n\nМаленький водяной потом много лет винил себя в трусости. Правда, его трусость помогла спасти множество жизней...'
    elif spawn_type == 'strigg' or spawn_type == 'minotaur':
      pass # Ошибка, огрши не рожают
    elif spawn_type == 'murloc':
      'Когда сирена вплыла в покои [game.girl.name_r], мурлок только-только вылупился из яйца. При виде открывшейся картины сирена ощутила приступ ярости. Она уничтожила монстра одним-единственным ударом.\n\nИногда размер имеет значение.'
    elif spawn_type == 'naga':
      'Когда русалка вплыла в покои [game.girl.name_r], ядовитый спрут только-только вылупился из яйца. При виде открывшейся картины русалка в ужасе кинулась прочь. Поднялась паника, и парочка тритонов догнала и уничтожила нага.\n\nИногда трусость - единственный выход.'
    elif spawn_type == 'ice_worm':
      'Когда йотунша вошла в покои [game.girl.name_r], ледяной червь только-только вылупился из яйца. При виде ледяной великанши он попытался забуриться под землю, но разъярённая йотунша схватила его за хвост, вытащила из земли и с силой ударила его об стену.\n\nИногда размер имеет значение.'
    elif spawn_type == 'yettie':
      'Когда йотунша вошла в покои [game.girl.name_r], йетти только-только вылупился из яйца. При виде кома белого меха ледяная великанша покрепче сжала кулаки и пошла в атаку. Йетти сопротивлялся, но силы были слишком неравны. Скоро йотунша превратила своего противника в невнятное кровавое месиво.\n\nИногда размер имеет значение.'
    elif spawn_type == 'hell_hound':
      'Когда ифритка вошла в покои [game.girl.name_r], адский щеночек только-только вылупился из яйца. При виде огненной великанши блохастый ощерился и зарычал, и ифритка с криком бросилась на монстра. Спустя пару минут от того осталось только невнятное месиво.\n\nИногда размер имеет значение.'
    elif spawn_type == 'barlog':
      'Когда ифритка вошла в покои [game.girl.name_r], дэв только-только вылупился из яйца. При виде сгустка тёмного огня великанша покрепче сжала кулаки и пошла в атаку. Новорождённый дэв сопротивлялся, но силы были слишком неравны. Скоро ифритка превратила своего противника в невнятную кучку пепла.\n\nИногда размер имеет значение.'
    elif spawn_type == 'chimera':
      'Когда титанида вошла в покои [game.girl.name_r], химера только-только вылупился из яйца. При виде великанши многоголовая тварь ощерилась и зарычала. Титанида с полнейшим равнодушием испепелила её молнией.\n\nИногда размер имеет значение.'
    elif spawn_type == 'troll':
      'Когда титанида вошла в покои [game.girl.name_r], тролль только-только вылупился из яйца. Ком шерсти и мускулов распрямился и спросил "Вы не подскажите, как пройти в библиотеку"? Титанида, не отвечая, испепелила монстра молнией.\n\nИногда размер имеет значение.'
    $ text = "Правда, новорождённое отродье удалось уничтожить.\n\n"
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_cripple_birth_success: # Отродье выживает
    $ spawn_type = game.girls_list.spawn_type
    $ spawn_image = 'img/scene/spawn/%s.jpg' % spawn_type
    hide bg
    show expression spawn_image as bg
    if spawn_type == 'poisonous_asp':
      'Когда тётя зашла в комнату к [game.girl.name_d], ядовитый аспид только-только вылупился из яйца. При виде открывшейся картины тётя замерла от потрясения, и аспид ужалил её прямо в ногу. После этого ничто не мешало новорождённому отродью проползти мимо скрючившейся от боли женщины и убраться прочь.\n\nЭто было первое злодеяние, совершённое аспидом. Но далеко не последнее...'
    elif spawn_type == 'basilisk':
      'Когда тётя зашла в комнату к [game.girl.name_d], василиск только-только вылупился из яйца. При виде открывшейся картины тётя замерла от потрясения, и василиск отравил её, посмотрев прямо в глаза. После этого ничто не мешало новорождённому отродью пролететь мимо скрючившейся от боли женщины и убраться прочь.\n\nЭто было первое злодеяние, совершённое василиском. Но далеко не последнее...'
    elif spawn_type == 'winged_asp':
      'Когда служанка зашла в комнату к [game.girl.name_d], крылатый аспид только-только вылупился из яйца. При виде открывшейся картины служанка замерла от потрясения, и крылатый аспид отравил её, укусив прямо в шею. После этого ничто не мешало новорождённому отродью улететь прочь, не обращая внимания на скорчившееся от боли женское тело.\n\nЭто было первое злодеяние, совершённое крылатым аспидом. Но далеко не последнее...'
    elif spawn_type == 'kobold':
      'Когда служанка зашла в комнату к [game.girl.name_d], кобольд только-только вылупился из яйца. При виде открывшейся картины служанка замерла от потрясения, и мелкий поганец прошмыгнул у неё между ног, больно ущипнув за бедро. Поймать его так и не удалось.\n\nВ тот раз кобольд так и не совершил никакого злодеяния. Но только в тот раз...'
    elif spawn_type == 'krokk':
      'Младшая сестрёнка [game.girl.name_r], мучимая любопытством, пробралась в комнату к калеке. К сожалению, она сделала это в тот самый момент, когда из яйца уже вылупился крокк. От потрясения девочка замерла на месте. Новорождённое отродье не растерялось, кинулось к девчушке и задушило её. После этого крокк, оставшись незамеченным, высользнул из особняка. Труп девочки обнаружили только под вечер.\n\nЭто было первое злодеяние, совершённое крокком. Но далеко не последнее...'
    elif spawn_type == 'lizardman':
      'Младшая сестрёнка [game.girl.name_r], мучимая любопытством, пробралась в комнату к калеке. К сожалению, она сделала это в тот самый момент, когда из яйца уже вылупился ящерик. От потрясения девочка замерла на месте. Ящерики с самого рождения обладают завидным интеллектом. Новорождённый объяснил девочке, что он - заколдованный принц альвов, и что ему нужно выбраться из особняка. Обрадованная и взбудораженная девочка выполнила его просьбы и вывела тёмное отродье из особняка тайком от взрослых.\n\nПри расстовании ящерик не убил девочку. Более того, он обещал встретиться с ней вновь, и собирался сдержать своё обещание. Ведь она уже фигурировала в его коварных планах...'
    elif spawn_type == 'gargoyle':
      'Когда подруга зашла в комнату к [game.girl.name_d], горгуйль только-только вылупился из яйца. Однако эта решительная альва не испугалась и приложила летающего монстра заклинанием! Увы, гаргуйли обладаают врождённой магической сопротивляемостью. Магический снаряд бессильно разбился о каменную кожу, и монстр успешно улетел прочь. Поймать его так и не смогли.\n\nВ тот раз горгуйль так и совершил никакого злодеяния. Но только в тот раз...'
    elif spawn_type == 'dragonborn':
      'Когда подруга зашла в комнату к [game.girl.name_d], драконорождённый только-только вылупился из яйца. Однако эта решительная альва не испугалась и приложила монстра заклинанием! Увы, драконорождённые обладают врождённой магической защитой, и заклинание отразилось обратно в альву. После этого оказалось, что даже у новорождённых монстров всё в порядке с потенцией, дева познала это на своём собственном опыте. Надругавшись над невинным девичьим телом, драконорождённый благополучно ускользнул из Зачарованного леса.\n\nЭто было первое злодеяние, совершённое драконорожденным. Но далеко не последнее...'
    elif spawn_type == 'octopus':
      'Когда русалка вплыла в покои [game.girl.name_r], ядовитый спрут только-только вылупился из яйца. При виде открывшейся картины русалка замерла от потрясения, и осьминог отравил её, схватившись присосками прямо за её хвост. После этого ничто не мешало новорождённому отродью уплыть прочь, не обращая внимания на скорчившееся от боли женское тело.\n\nЭто было первое злодеяние, совершённое ядовитым спрутом. Но далеко не последнее...'
    elif spawn_type == 'sea_bastard':
      'Маленький братик [game.girl.name_r], мучимый любопытством, пробрался в запретную комнату к калеке. К сожалению, он сделала это в тот самый момент, когда из яйца уже вылупился рыбоглаз. Маленький водяной отважно бросился на монстра. Увы, храбрость и кулаки - плохое оружие в бою даже с новорождённым отродьем! Рыбоглаз вырвал жабры у водяного и уплыл прочь, не обращая внимания на агонизирующее тело. Труп обнаружили только к вечеру.\n\nЭто было первое злодеяние, совершённое рыбоглазом. Но далеко не последнее...'
    elif spawn_type == 'strigg' or spawn_type == 'minotaur':
      pass # Ошибка, огрши не рожают
    elif spawn_type == 'murloc':
      'Когда сирена вплыла в покои [game.girl.name_r], мурлок только-только вылупился из яйца. При виде открывшейся картины сирена ощутила приступ умиления. Это чувство разделило множество её подруг. Они выкармливали мурлока с ложечки, заботились о нём, учили плавать и говорить.\n\nСирены долго думали о подходящем имени для своего мурлока. Назвали Мурчалем.'
    elif spawn_type == 'naga':
      'Когда русалка вплыла в покои [game.girl.name_r], наг только-только вылупился из яйца. При виде открывшейся картины русалка впала в ступор, и наг с лёгкостью обвил её тело. После этого оказалось, что даже у новорождённых монстров всё в порядке с потенцией, морская дева познала это на своём собственном опыте. Надругавшись над невинной русалочкой, наг благополучно уплыл прочь.\n\nЭто было первое злодеяние, совершённое нагом. Но далеко не последнее...'
    elif spawn_type == 'ice_worm':
      'Когда йотунша вошла в покои [game.girl.name_r], ледяной червь только-только вылупился из яйца. При виде ледяной великанши он забурился под землю. Разъярённая йотунша попыталась схватить его за хвост, но чуть-чуть не успела.\n\nВ тот раз ледяной червь так и совершил никакого злодеяния. Но только в тот раз...'
    elif spawn_type == 'yettie':
      'Когда йотунша вошла в покои [game.girl.name_r], йетти только-только вылупился из яйца. При виде кома белого меха ледяная великанша задумчиво прикусила губу. Так уж получилось, что она вот уже который век не могла найти себе мужа... заслужила же она маленький кусочекк женского счастья, в конце-то концов?! Йотунша вынесла маленького йетти из ледяного дворца и укрыла его у себя. Она кормила его, воспитывала, учила говорить...\n\nЧто же, по крайней мере, сексуально неудовлетворённой она не осталась!'
    elif spawn_type == 'hell_hound':
      'Когда ифритка вошла в покои [game.girl.name_r], адский щеночек только-только вылупился из яйца. При виде огненной великанши блохастый ощерился и зарычал, и ифритка с криком бросилась прочь - она с самого детства панически боялась собак! Пора обитатели вулканического дворца смогли унять панику, пока ифритка успокоилась и рассказала что к чему - адского пёсика уже и след остыл.\n\nВ тот раз адский пёс так и совершил никакого злодеяния. Но только в тот раз...'
    elif spawn_type == 'barlog':
      'Когда ифритка вошла в покои [game.girl.name_r], дэв только-только вылупился из яйца. При виде сгустка тёмного огня великанша задумчиво прикусила губу. Так уж получилось, что она вот уже который век не могла найти себе мужа... заслужила же она маленький кусочекк женского счастья, в конце-то концов?! Ифритка вынесла маленького дэва из вулканического дворца и укрыла его у себя. Она кормила его, воспитывала, учила говорить...\n\nЧто же, по крайней мере, сексуально неудовлетворённой она не осталась!'
    elif spawn_type == 'chimera':
      'Когда титанида вошла в покои [game.girl.name_r], химера только-только вылупился из яйца. При виде великанши многоголовая тварь ощерилась и зарычала. Титанида в гневе бросилась на монстра и оторвала одну из его голов! Увы, для химеры такая рана оказалась тяжёлой, но не смертельной. Пусть и с большим трудом. но эта тварь всё же сумела улететь прочь.\n\nВ тот раз химера так и совершила никакого злодеяния. Но только в тот раз...'
    elif spawn_type == 'troll':
      'Когда титанида вошла в покои [game.girl.name_r], тролль только-только вылупился из яйца. Ком шерсти и мускулов распрямился и спросил "Вы не подскажите, как пройти в библиотеку"? Титанида в ярости закричала "Библиотека не для монстров!!!", и это стало её главной и единственной ошибкой. Она ввязалась в диалог - и уже не могла напасть просто так. Тролль успешно затроллил оппонентку, полностью сбил её с толку и сбежал из Облачного замка.\n\nИногда значение имеет не размер, а интеллект.'
    $ text = "Новорождённое отродье сумело сбежать.\n\n"
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_pregnant_decision(g_type,g_nature):
    call lb_show_home from _call_lb_show_home_2
    if game.girl.gift  is not None:   # ПОлучила блестяшку
      call lb_pregnant_gift from _call_lb_pregnant_gift
      return
    $ text = game.girls_list.description('pregnant_decision_question')
    game.girl "[text]"
# Принимаем решение - открыться или нет?
    if g_nature == 'innocent':
        $ choices = [
            ("lb_pregnant_innocent_yes", 50),
            ("lb_pregnant_innocent_no",  10)]
    elif g_nature == 'proud':
        $ choices = [
            ("lb_pregnant_proud_yes", 10),
            ("lb_pregnant_proud_no",  10)]
    elif g_nature == 'lust':
        $ choices = [
            ("lb_pregnant_lust_yes", 10),
            ("lb_pregnant_lust_no",  50)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return  

label lb_pregnant_gift:
    show screen controls_overwrite
    $ text = u'Оказавшись в родных краях, %s решила не скрывать свою беременность и честно рассказала родственникам о произошедшем. Впрочем, имея на руках %s, ей не было нужды беспокоиться о недовольстве своей родни.\n\n%s оказалась права - родственники одобрили её выбор и решили скрывать факт чудовищной беременности до последнего. ' % (game.girl.name, game.girl.gift.description(),game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    game.girl 'В моём чреве зреет чудовище. Но если я расскажу об этом родным, меня расцелуют и будут на руках носить. Ведь я вернулась не с пустыми карманами!'
    game.girl.third '[game.girl.name] не ошиблась. Её родственники очень обрадовались {i}такому{/i} подарку и решили скрывать случившееся до последнего.'
    call lb_pregnant_stels from _call_lb_pregnant_stels_5
    return    

label lb_pregnant_innocent_yes:
    $ text = game.girls_list.description('pregnant_innocent_yes')
    game.girl "[text]"
    call lb_pregnant_relatives from _call_lb_pregnant_relatives_1
    return

label lb_pregnant_innocent_no:
    show screen controls_overwrite
    $ text = game.girls_list.description('pregnant_innocent_no')
    game.girl "[text]"
    call lb_pregnant_stels from _call_lb_pregnant_stels_1
    return

label lb_pregnant_proud_yes:
    show screen controls_overwrite
    $ text = game.girls_list.description('pregnant_proud_yes')
    game.girl "[text]"
    call lb_pregnant_relatives from _call_lb_pregnant_relatives_2
    return

label lb_pregnant_proud_no:
    show screen controls_overwrite
    $ text = game.girls_list.description('pregnant_proud_no')
    game.girl "[text]" 
    call lb_pregnant_stels from _call_lb_pregnant_stels_2
    return

label lb_pregnant_lust_yes:
    show screen controls_overwrite
    $ text = game.girls_list.description('pregnant_lust_yes')
    game.girl "[text]" 
    call lb_pregnant_relatives from _call_lb_pregnant_relatives_3    
    return

label lb_pregnant_lust_no:
    show screen controls_overwrite
    $ text = game.girls_list.description('pregnant_lust_no')
    game.girl "[text]"     
    call lb_pregnant_stels from _call_lb_pregnant_stels_3
    return

# Определяется, прикроют ли девушку родственники
label lb_pregnant_relatives:
    show screen controls_overwrite
    $ text = u'Оказавшись в родных краях, %s решила не скрывать свою беременность и честно рассказала родственникам о произошедшем. ' % (game.girl.name)
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    if (g_nature == 'innocent' and not (random.randint(1,3) == 1)) or (g_nature == 'proud' and (random.randint(1,2) == 1)) or (g_nature == 'lust' and (random.randint(1,3) == 1)):
      $ text = game.girls_list.description('pregnant_relatives_save')
      game.girl.third "[text]"
      $ text = u'Они пришли в ужас и решили скрывать случившееся до последнего. \n\n' 
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_pregnant_stels from _call_lb_pregnant_stels_4
    else:
      $ text = u'Они пришли в ярость и обнародавали этот ужасающий факт. \n\n' 
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_girl_execution from _call_lb_girl_execution_1
    return

# Девушка пытается скрыть факт беременности.
label lb_pregnant_stels:
    show screen controls_overwrite
    $ text = u'%s попыталась скрыть свою беременность. ' % game.girl.name
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ text = game.girls_list.description('pregnant_stels_' + g_type)
    game.girl.third "[text]"  
    game.girl 'Умоляю, молчи! '
    if (g_nature == 'innocent' and (random.randint(1,5) == 1)) or (g_nature == 'proud' and (random.randint(1,4) == 1)) or (g_nature == 'lust' and (random.randint(1,3) == 1)):
    
      $ text = game.girls_list.description('pregnant_stels_' + g_type + '_fail')
      game.girl.third "[text]"
      $ text = u'Безуспешно. \n\n' 
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      call lb_girl_execution from _call_lb_girl_execution_4

    else:
      $ text = game.girls_list.description('pregnant_stels_' + g_type + '_sucsess')
      game.girl.third "[text]"
      $ text = u'Успешно. \n\n' 
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return


# Беременность открылась. Выбираем способ казни.
label lb_girl_execution:
    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return

    show screen controls_overwrite
    $ mobchance = game.mobilization.level
    $ badchance = game.poverty.value
    if g_type == 'peasant':
        game.girl.third 'Узнав, что [game.girl.name] носит под сердцем ребёнка чудовища, селяне обезумили от ярости.'
        $ choices = [
            ("lb_girl_execution_peasant_1", 10+badchance),
            ("lb_girl_execution_peasant_2", 10+badchance),
            ("lb_girl_execution_peasant_3", 10+badchance),
            ("lb_girl_execution_inquisition", mobchance)]
    elif g_type == 'citizen':
        game.girl.third 'Узнав, что [game.girl.name] носит под сердцем ребёнка чудовища, горожане обезумили от ярости. Магистрат пошёл навстречу народным чаяниям.'
        $ choices = [
            ("lb_girl_execution_citizen_1", 10+badchance),
            ("lb_girl_execution_citizen_2", 10+badchance),
            ("lb_girl_execution_citizen_3", 10+badchance),
            ("lb_girl_execution_inquisition", mobchance)]
    elif g_type == 'princess':
        game.girl.third '[game.girl.name] надеялась, что знатность её рода смягчит наказание. Тщетно. Судьи сочли, что для успокоения народа казнь аристократки должна быть особенно жестокой. '
        $ choices = [
            ("lb_girl_execution_princess_1", 10+badchance),
            ("lb_girl_execution_princess_2", 10+badchance),
            ("lb_girl_execution_princess_3", 10+badchance),
            ("lb_girl_execution_inquisition", mobchance)]
    elif g_type == 'elf':
        game.girl.third 'Альвы не казнят своих сородичей. Это немыслимо. Но [game.girl.name] день за днём видела укоризненные взгляды родных, знакомых, старейшин... В конце концов она не выдержала и пошла на охоту. В Тёмный лес. В одиночку. Без оружия. С заблокированной магией. Голой. Ей никто не препятствовал. '
        $ choices = [
            ("lb_girl_execution_elf_1", 10),
            ("lb_girl_execution_elf_2", 10),
            ("lb_girl_execution_elf_3", 10)]
    elif g_type == 'mermaid':
        game.girl.third 'Узнав, что [game.girl.name] носит под сердцем отродье чудовища, морской народ пришёл в ярость. Приговор был суровым, но справедливым: смерть.  '
        $ choices = [
            ("lb_girl_execution_mermaid_1", 10),
            ("lb_girl_execution_mermaid_2", 10),
            ("lb_girl_execution_mermaid_3", 10)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)
    return

# Инквизиция. Повезло.
label lb_girl_execution_inquisition:
    show screen controls_overwrite
    $ text = "Беременная девушка попала в застенки Инквизиции. Плод тщательно изучили, а саму жертву дракона - отпустили с миром. \n\n"
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression 'img/scene/execution/inquisition.jpg' as bg
    nvl clear
    $ game.girls_list.description('girl_execution_inquisition', True)
    python:
        game.girl.pregnant=-1 
    return

# Казни крестьянок
label lb_girl_execution_peasant_1:
    show screen controls_overwrite
    $ current_image='img/scene/girl_death.jpg'
    $ game.chronik.death('execution_peasant_1',current_image) 
    $ text = "Разъярённые крестьяне растерзали жертву дракона."
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression 'img/scene/girl_death.jpg' as bg
    nvl clear
    if game.girl.blind:
      $ game.girls_list.description('girl_execution_peasant_1_blind', True)
    else:
      $ game.girls_list.description('girl_execution_peasant_1', True)  # убивают из-за беременности
    python:
        game.girl.pregnant=0
    return

label lb_girl_execution_peasant_2:
    show screen controls_overwrite
    $ current_image='img/scene/execution/peasant_2.jpg'
    $ game.chronik.death('execution_peasant_2',current_image) 
    $ text = "Разъярённые крестьяне утопили жертву дракона."
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression 'img/scene/execution/peasant_2.jpg' as bg
    nvl clear
    if game.girl.blind:
      $ game.girls_list.description('girl_execution_peasant_2_blind', True)
    else:
      $ game.girls_list.description('girl_execution_peasant_2', True)
    python:
        game.girl.pregnant=0  
    return

label lb_girl_execution_peasant_3:
    show screen controls_overwrite
    $ current_image='img/scene/execution/peasant_3.jpg'
    $ game.chronik.death('execution_peasant_3',current_image) 
    $ text = "Разъярённые крестьяне закопали жертву дракона живьём."
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression 'img/scene/execution/peasant_3.jpg' as bg
    nvl clear
    if game.girl.blind:
      $ game.girls_list.description('girl_execution_peasant_3_blind', True)
    else:
      $ game.girls_list.description('girl_execution_peasant_3', True)
    python:
        game.girl.pregnant=0
    return

# Казни горожанок
label lb_girl_execution_citizen_1:
    show screen controls_overwrite
    hide bg
    $ current_image = 'img/scene/execution/citizen_1.jpg'
    show expression current_image as bg
    nvl clear
    $ text = u'Жертву дракона прилюдно сожгли на костре. ' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    if game.girl.blind:
      $ game.girls_list.description('girl_execution_citizen_1_blind', True)
    else:
      $ game.girls_list.description('girl_execution_citizen_1', True)  # убивают из-за беременности
    $ game.chronik.death('burned',current_image)
    python:
        game.girl.pregnant=0
    return

label lb_girl_execution_citizen_2:
    show screen controls_overwrite
    hide bg
    $ current_image = 'img/scene/execution/citizen_2.jpg'
    show expression current_image as bg
    nvl clear
    $ text = u'Жертву дракона прилюдно запороли кнутом. ' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('girl_execution_citizen_2', True)
    $ game.chronik.death('whipped',current_image)
    python:
        game.girl.pregnant=0  
    return

label lb_girl_execution_citizen_3:
    show screen controls_overwrite
    hide bg
    $ current_image='img/scene/execution/citizen_3.jpg'
    show expression current_image as bg
    nvl clear
    $ text = u'Жертву дракона прилюдно повесили. ' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.girls_list.description('girl_execution_citizen_3', True)
    $ game.chronik.death('hanged',current_image)
    python:
        game.girl.pregnant=0
    return

# Казни принцесс
label lb_girl_execution_princess_1:
    show screen controls_overwrite
    $ current_image='img/scene/execution/princess_1.jpg'
    $ game.chronik.death('execution_princess_1',current_image) 
    $ text = "Жертву дракона прилюдно посадили на кол."
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression 'img/scene/execution/princess_1.jpg' as bg
    nvl clear
    if game.girl.blind:
      $ game.girls_list.description('girl_execution_princess_1_blind', True)
    else:
      $ game.girls_list.description('girl_execution_princess_1', True)  # убивают из-за беременности
    python:
        game.girl.pregnant=0
    return

label lb_girl_execution_princess_2:
    show screen controls_overwrite
    $ current_image='img/scene/execution/princess_2.jpg'
    $ game.chronik.death('execution_princess_2',current_image) 
    $ text = "Жертве дракона прилюдно вскрыли живот."
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression 'img/scene/execution/princess_2.jpg' as bg
    nvl clear
    $ game.girls_list.description('girl_execution_princess_2', True)
    python:
        game.girl.pregnant=0  
    return

label lb_girl_execution_princess_3:
    show screen controls_overwrite
    $ current_image='img/scene/execution/princess_3.jpg'
    $ game.chronik.death('execution_princess_3',current_image) 
    $ text = "Жертву дракона прилюдно разорвали на дыбе."
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression 'img/scene/execution/princess_3.jpg' as bg
    nvl clear
    $ game.girls_list.description('girl_execution_princess_3', True)
    python:
        game.girl.pregnant=0
    return

# Казни эльфиек
label lb_girl_execution_elf_1:
    show screen controls_overwrite
    $ current_image='img/scene/execution/elf_1.jpg'
    $ game.chronik.death('execution_elf_1',current_image) 
    $ text = "Жертва дракона, доведённая  остракизмом до отчаяния, отправилась в Тёмный лес и стала обедом для гигантского паука."
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression 'img/scene/execution/elf_1.jpg' as bg
    nvl clear
    $ game.girls_list.description('girl_execution_elf_1', True)  # убивают из-за беременности
    python:
        game.girl.pregnant=0
    return

label lb_girl_execution_elf_2:
    show screen controls_overwrite
    $ current_image='img/scene/execution/elf_2.jpg'
    $ game.chronik.death('execution_elf_2',current_image) 
    $ text = "Жертва дракона, доведённая  остракизмом до отчаяния, отправилась в Тёмный лес и стала обедом для альвоеда."
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression 'img/scene/execution/elf_2.jpg' as bg
    nvl clear
    $ game.girls_list.description('girl_execution_elf_2', True)
    python:
        game.girl.pregnant=0  
    return

label lb_girl_execution_elf_3:
    show screen controls_overwrite
    $ current_image='img/scene/execution/elf_3.jpg'
    $ game.chronik.death('execution_elf_3',current_image) 
    $ text = "Жертва дракона, доведённая  остракизмом до отчаяния, отправилась в Тёмный лес и стала обедом для плотоядной плесени."
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression 'img/scene/execution/elf_3.jpg' as bg
    nvl clear
    $ game.girls_list.description('girl_execution_elf_3', True)
    python:
        game.girl.pregnant=0
    return

# Казни русалок
label lb_girl_execution_mermaid_1:
    show screen controls_overwrite
    $ current_image='img/scene/execution/mermaid_1.jpg'
    $ game.chronik.death('execution_mermaid_1',current_image) 
    $ text = "Русалку, ставшую жертвой дракона, оставили на берегу, обрекая на смерть от обезвоживания. "
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression 'img/scene/execution/mermaid_1.jpg' as bg
    nvl clear
    $ game.girls_list.description('girl_execution_mermaid_1', True)  # убивают из-за беременности
    python:
        game.girl.pregnant=0
    return

label lb_girl_execution_mermaid_2:
    show screen controls_overwrite
    $ current_image='img/scene/execution/mermaid_2.jpg'
    $ game.chronik.death('execution_mermaid_2',current_image) 
    $ text = "Русалку, ставшую жертвой дракона, утопили в глубоководном жёлобе."
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    hide bg
    show expression 'img/scene/execution/mermaid_2.jpg' as bg
    nvl clear
    if game.girl.blind:
      $ game.girls_list.description('girl_execution_mermaid_2_blind', True)
    else:
      $ game.girls_list.description('girl_execution_mermaid_2', True)
    python:
        game.girl.pregnant=0  
    return

label lb_girl_execution_mermaid_3:
    show screen controls_overwrite
    hide bg
    $ current_image='img/scene/execution/mermaid_3.jpg'
    $ game.chronik.death('execution_mermaid_3',current_image) 
    $ text = "Русалку, ставшую жертвой дракона, убил родной отец."
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('girl_execution_mermaid_3', True)
    python:
        game.girl.pregnant=0
    return

# Эвенты возвращения девушек домой.
# Горожанки
label lb_return_citizen_virgin:
    show screen controls_overwrite
    hide bg
    $ current_image='img/bg/girl_return/citizen_return.jpg'
    $ game.chronik.live('citizen_married',current_image)  
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_citizen_virgin', True)
    $ text = game.girls_list.description('return_citizen_virgin')
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_return_citizen_raped:
    hide bg
    $ current_image='img/bg/special/castle3.jpg'
    $ game.chronik.live('monastery',current_image)   
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_citizen_raped', True)
    $ text = game.girls_list.description('return_citizen_raped')
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_return_citizen_death:
    hide bg
    $ current_image='img/bg/girl_return/citizen_death.jpg'
    $ game.chronik.death('hanged_self_citizen',current_image)    
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_citizen_death', True)
    $ text = game.girls_list.description('return_citizen_death')
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_return_citizen_warrior:
    hide bg
    $ current_image='img/bg/girl_return/citizen_warrior.jpg'
    $ game.chronik.live('citizen_warrior',current_image)     
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_citizen_warrior', True)
    $ text = game.girls_list.description('return_citizen_warrior')
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_return_citizen_brothel:
    hide bg
    $ current_image='img/bg/girl_return/citizen_brothel.jpg'
    $ game.chronik.live('citizen_brothel',current_image)   
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_citizen_brothel', True)
    $ text = game.girls_list.description('return_citizen_brothel')
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_return_citizen_murder:
    hide bg
    $ current_image='img/bg/girl_return/citizen_murder.jpg'
    $ game.chronik.death('maniac',current_image)  
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_citizen_murder', True)
    $ text = game.girls_list.description('return_citizen_murder')
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

# Крестьянки
label lb_return_peasant_virgin:
    $ text = game.girls_list.description('return_peasant_virgin') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/peasant_return.jpg'
    $ game.chronik.live('peasant_virgin',current_image) 
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_peasant_virgin', True)
    return

label lb_return_peasant_raped:
    $ text = game.girls_list.description('return_peasant_raped') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/special/castle3.jpg'
    $ game.chronik.write_image(current_image,game.dragon.level,game.girl.girl_id)
    $ game.chronik.live('monastery',current_image)   
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_peasant_raped', True)
    return

label lb_return_peasant_death:
    $ text = game.girls_list.description('return_peasant_death') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/peasant_death.jpg'
    $ game.chronik.death('peasant_death',current_image)         
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_peasant_death', True)
    return

label lb_return_peasant_warrior:
    $ text = game.girls_list.description('return_peasant_warrior') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/peasant_warrior.jpg'
    $ game.chronik.live('peasant_warrior',current_image)   
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_peasant_warrior', True)
    return

label lb_return_peasant_brothel:
    $ text = game.girls_list.description('return_peasant_brothel') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/peasant_brothel.jpg'
    $ game.chronik.live('peasant_brothel',current_image)     
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_peasant_brothel', True)
    return

label lb_return_peasant_murder:
    $ text = game.girls_list.description('return_peasant_murder') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/peasant_murder.jpg'
    $ game.chronik.death('peasant_murder',current_image)    
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_peasant_murder', True)
    return

# Принцессы
label lb_return_princess_virgin:
    $ text = game.girls_list.description('return_princess_virgin') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/princess_return.jpg'
    $ game.chronik.live('princess_virgin',current_image)           
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_princess_virgin', True)
    return

label lb_return_princess_raped:
    $ text = game.girls_list.description('return_princess_raped') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/special/castle3.jpg'
    $ game.chronik.live('monastery',current_image)  
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_princess_raped', True)
    return

label lb_return_princess_death:
    $ text = game.girls_list.description('return_princess_death') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/princess_death.jpg'
    $ game.chronik.death('princess_death',current_image)    
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_princess_death', True)
    return

label lb_return_princess_warrior:
    $ text = game.girls_list.description('return_princess_warrior') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/princess_warrior.jpg'
    $ game.chronik.live('princess_warrior',current_image)     
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_princess_warrior', True)
    return

label lb_return_princess_brothel:
    $ text = game.girls_list.description('return_princess_brothel') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/princess_brothel.jpg'
    $ game.chronik.live('princess_brothel',current_image)   
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_princess_brothel', True)
    return

label lb_return_princess_murder:
    $ text = game.girls_list.description('return_princess_murder') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/princess_murder.jpg'
    $ game.chronik.death('princess_murder',current_image)   
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_princess_murder', True)
    return

# Эльфийки
label lb_return_elf_virgin:
    $ text = game.girls_list.description('return_elf_virgin') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/elf_return.jpg'
    $ game.chronik.live('elf_virgin',current_image)    
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_elf_virgin', True)
    return

label lb_return_elf_raped:
    $ text = game.girls_list.description('return_elf_raped') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/elf_return.jpg'
    $ game.chronik.live('elf_raped',current_image)   
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_elf_raped', True)
    return

label lb_return_elf_death:
    $ text = game.girls_list.description('return_elf_death') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/elf_death.jpg'
    $ game.chronik.death('elf_death',current_image)  
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_elf_death', True)
    return

label lb_return_elf_warrior:
    $ text = game.girls_list.description('return_elf_warrior') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/elf_warrior.jpg'
    $ game.chronik.live('elf_warrior',current_image)    
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_elf_warrior', True)
    return

label lb_return_elf_brothel:
    $ text = game.girls_list.description('return_elf_brothel') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/elf_brothel.jpg'
    $ game.chronik.live('elf_brothel',current_image)     
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_elf_brothel', True)
    return

label lb_return_elf_murder:
    $ text = game.girls_list.description('return_elf_murder') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/elf_murder.jpg'
    $ game.chronik.death('elf_murder',current_image) 
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_elf_murder', True)
    return

# Русалки
label lb_return_mermaid_virgin:
    $ text = game.girls_list.description('return_mermaid_virgin') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/mermaid_return.jpg'
    $ game.chronik.live('return_mermaid',current_image)  
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_mermaid_virgin', True)
    return

label lb_return_mermaid_raped:
    $ text = game.girls_list.description('return_mermaid_raped') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/mermaid_raped.jpg'
    $ game.chronik.live('mermaid_raped',current_image) 
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_mermaid_raped', True)
    return

label lb_return_mermaid_death:
    $ text = game.girls_list.description('return_mermaid_death') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/mermaid_death.jpg'
    $ game.chronik.death('mermaid_death',current_image)
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_mermaid_death', True)
    return

label lb_return_mermaid_warrior:
    $ text = game.girls_list.description('return_mermaid_warrior') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/mermaid_warrior.jpg'
    $ game.chronik.live('mermaid_warrior',current_image)
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_mermaid_warrior', True)
    return

label lb_return_mermaid_brothel:
    $ text = game.girls_list.description('return_mermaid_brothel') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/mermaid_brothel.jpg'
    $ game.chronik.live('mermaid_brothel',current_image) 
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_mermaid_brothel', True)
    return

label lb_return_mermaid_murder:
    $ text = game.girls_list.description('return_mermaid_murder') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/girl_return/mermaid_murder.jpg'
    $ game.chronik.death('mermaid_murder',current_image)
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_mermaid_murder', True)
    return

# Великанши
label lb_return_ogre_virgin:
    $ place = 'forest'
    $ text = game.girls_list.description('return_ogre_virgin') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image=get_place_bg(place)
    $ game.chronik.live('return_ogre',current_image)
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_ogre_virgin', True)
    return

label lb_return_ogre_raped:
    $ place = 'forest'
    $ text = game.girls_list.description('return_ogre_raped') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image=get_place_bg(place)
    $ game.chronik.live('return_ogre',current_image) 
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_ogre_raped', True)
    return

label lb_return_siren:
    $ place = 'sea'
    $ text = game.girls_list.description('return_siren') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image=get_place_bg(place)
    $ game.chronik.live('return_siren',current_image) 
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_siren', True)
    return

label lb_return_ice:
    $ place = 'mountain'
    $ text = game.girls_list.description('return_ice') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image=get_place_bg(place)
    $ game.chronik.live('return_ice',current_image) 
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_ice', True)
    return

label lb_return_fire:
    $ text = game.girls_list.description('return_fire') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/bg/lair/volcanoforge.jpg'
    $ game.chronik.live('return_fire',current_image)  
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_fire', True)
    return

label lb_return_titan:
    $ place = 'sky'
    $ text = game.girls_list.description('return_titan') 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image=get_place_bg(place)
    $ game.chronik.live('return_titan',current_image) 
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('return_titan', True)
    return

# Возвращение слепых

label lb_return_peasant_blind:
    $ current_image=get_random_image("img/scene/blind")
    show expression current_image as bg
    nvl clear
    $ text = 'Благодаря своему дару Внутреннего зрения %s быстро стала уважаемой деревенской гадалкой. Сперва к ней ходили односельчане, потом - жители соседних хуторов, а через несколько лет к %s обращались за советом даже лорды из сопредельных провинций. Гадания %s всегда рано или поздно сбылвались, хотя зачастую и не совсем так, как понимал проситель.\n\n' %(game.girl.name,game.girl.name_d,game.girl.name_r)
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    call lb_blind_prophecy from _call_lb_blind_prophecy_1
    $ game.chronik.live('blind_peasant',current_image)  
    return

label lb_return_citizen_blind:
    $ current_image=get_random_image("img/scene/blind/")
    show expression current_image as bg
    nvl clear
    $ text = 'Благодаря своему дару Внутреннего зрения %s быстро стала известной пророчицей. Сперва её совета спрашивали родные и близкие, потом - жители всего города, а через несколько лет к %s обращались за советом даже лорды из сопредельных провинций. Пророчества %s всегда рано или поздно сбылвались, хотя зачастую и не совсем так, как понимал проситель.\n\n' %(game.girl.name,game.girl.name_d,game.girl.name_r)
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    call lb_blind_prophecy from _call_lb_blind_prophecy_2
    $ game.chronik.live('blind_citizen',current_image)  
    return

label lb_return_princess_blind:
    $ current_image=get_random_image("img/scene/blind/")
    show expression current_image as bg
    nvl clear
    $ text = 'Благодаря своему дару Внутреннего зрения %s быстро стала известным оракулом. Сперва её совета спрашивали родные и близкие, потом - влиятельнейшие лорды, а через пару лет сам король на считал зазорным попросить помощи у %s. Пророчества %s всегда рано или поздно сбылвались, хотя зачастую и не совсем так, как понимал проситель.\n\n' %(game.girl.name,game.girl.name_r,game.girl.name_r)
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    call lb_blind_prophecy from _call_lb_blind_prophecy_3
    $ game.chronik.live('blind_princess',current_image)  
    return

label lb_return_elf_blind:
    $ current_image=get_random_image("img/scene/blind/")
    show expression current_image as bg
    nvl clear
    $ text = 'Благодаря своему дару Внутреннего зрения %s стала Видящей своего народа. На протяжении многих лет она пыталась спасти альвов от порождений Тёмной Госпожи - но увы, видения бессильны, когда в будущем нет благоприятного исхода! Тем не менее, старания %s изрядно облегчили участь Детей Дану.\n\n' %(game.girl.name,game.girl.name_r)
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    call lb_blind_prophecy from _call_lb_blind_prophecy_4
    $ game.chronik.live('blind_elf',current_image)  
    return

label lb_return_mermaid_blind:
    $ current_image="img/scene/blind_mermaid.jpg"
    show expression current_image as bg
    nvl clear
    $ text = 'Благодаря своему дару Внутреннего зрения %s быстро стала известной ведуньей. За советами к ней обращались не только водяные с русалками, но даже и тритоны с сиренами. Пророчества %s всегда рано или поздно сбылвались, хотя зачастую и не совсем так, как понимал проситель.\n\n' %(game.girl.name,game.girl.name_r)
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    call lb_blind_prophecy from _call_lb_blind_prophecy_5
    $ game.chronik.live('blind_mermaid',current_image)  
    return

label lb_return_siren_blind:
    $ current_image="img/scene/blind_mermaid.jpg"
    show expression current_image as bg
    nvl clear
    $ text = 'Благодаря своему дару Внутреннего зрения %s быстро стала известной ведуньей. Её слава вышла далеко за пределы морского народа, к ней за советами обращался даже король людей с поверхности. Пророчества %s всегда рано или поздно сбылвались, хотя зачастую и не совсем так, как понимал проситель.\n\n' %(game.girl.name,game.girl.name_r)
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    call lb_blind_prophecy from _call_lb_blind_prophecy_6
    $ game.chronik.live('blind_mermaid',current_image)  
    return

label lb_return_ogre_blind:
    $ current_image="img/scene/fear/plains/ogre.jpg"
    show expression current_image as bg
    nvl clear
    $ text = 'Благодаря своему дару Внутреннего зрения %s быстро нашла себе подходящего партнёра по СНУ-СНУ. Её нередко посещали видения будущего, но, разумеется, она и не думала делиться ими даже с сородичами! \n\n' %(game.girl.name)
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ game.chronik.live('blind_ogre',current_image)  
    return

label lb_return_ice_blind:
    $ current_image=get_random_image("img/scene/blind/")
    show expression current_image as bg
    nvl clear
    $ text = 'Благодаря своему дару Внутреннего зрения %s быстро стала известной вёльвой. Йотуны почитали %s как воплощение божеста, а она по мере сил пыталась провести свой народ сквозь ужасы драконьего опустошения. Нельзя сказать, что она полностью справилась со своей задачей... но и напрасными её усилия не были.\n\n' %(game.girl.name,game.girl.name_v)
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    call lb_blind_prophecy from _call_lb_blind_prophecy_7
    $ game.chronik.live('blind_ice',current_image)  
    return

label lb_return_fire_blind:
    $ current_image=get_random_image("img/scene/blind/")
    show expression current_image as bg
    nvl clear
    $ text = 'Благодаря своему дару Внутреннего зрения %s быстро стала известным кахином. Йотуны почитали %s как воплощение божеста, а она по мере сил пыталась провести свой народ сквозь ужасы драконьего опустошения. Нельзя сказать, что она полностью справилась со своей задачей... но и напрасными её усилия не были.\n\n' %(game.girl.name,game.girl.name_v)
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    call lb_blind_prophecy from _call_lb_blind_prophecy_8
    $ game.chronik.live('blind_fire',current_image)  
    return

label lb_return_titan_blind:
    $ current_image=get_random_image("img/scene/blind/")
    show expression current_image as bg
    nvl clear
    $ text = 'Благодаря своему дару Внутреннего зрения %s быстро стала пифией. К ней обращались все: люди и великаны, альвы и цверги, простые русалки и могущественные лорды. Пророчества %s всегда рано или поздно сбылвались, хотя зачастую и не совсем так, как понимал проситель.\n\n' %(game.girl.name,game.girl.name_r)
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    call lb_blind_prophecy from _call_lb_blind_prophecy_9
    $ game.chronik.live('blind_titan',current_image)  
    return

label lb_blind_prophecy:  # Последнее пророчество
    $ text = 'Правда, в старости %s сделала ряд крайне странных пророчеств. Незадолго до смерти она настойчиво твердила, что ' % game.girl.name
    $ text += game.interpolate(random.choice(txt_prophecy))
    '[text]'
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_return_cripple:
    hide bg
    $ current_image = game.girl.cripple_image
    show expression current_image as bg
    'В дальнейшем [game.girl.name] умерла, но о подробностях ничего никому не известно.'
    $ game.chronik.death('cripple_unknown',current_image) 
    return

label lb_event_girl_spawn(spawn_type):
    $ spawn_image = "img/scene/spawn/%s.jpg" % spawn_type

    hide bg
    show expression spawn_image as bg
    nvl clear
    python:
        spawn_description = game.girls_list.description(spawn_type)  # описание родов конкретного типа
        if not spawn_description:
            if 'elite' in girls_data.spawn_info[spawn_type]['modifier']:
                spawn_description = game.girls_list.description('spawn_elite')
            else:
                spawn_description = game.girls_list.description('spawn_common')
    game.girl.third "[spawn_description]"
    if game.girl.cripple and (random.randint(1, 3) == 1): # Смерть калеки при родах 
      call lb_spawn_lair_death from _call_lb_spawn_lair_death_1
    elif (random.randint(1, 10) == 1): # Смерть при родах 
      call lb_spawn_lair_death from _call_lb_spawn_lair_death_2
    else:
      $ text = u'Роды прошли благополучно. \n\n' 
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      if game.girl.blind:
        $ text = u'После родов у %s открылось мистическое Внутреннее зрение. \n\n' % (game.girl.name_r)
        game.girl.third '[text]'
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)        
    return

label lb_spawn_lair_death: # Смерть роженицы в логове

    # @fdsc Девушки не умирают просто так, если договорились с драконом
    if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
    
    $ text = u'После этого роженица погибла. Новорождённое отродье не осталось голодным. \n\n ' 
    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    $ current_image='img/scene/parturition_death_lair.jpg'
    $ game.chronik.death('lair_birth',current_image)
    hide bg
    show expression current_image as bg
    if not game.girl.cripple:
      $ text = game.girls_list.description('birth_death')
    else:
      $ text = game.girls_list.description('birth_death_cripple')
    game.girl.third "[text]"   # событие "смерть девушки при родах"
    $ game.girl.pregnant=-1
#    $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
    return

label lb_event_girl_free_spawn(spawn_type):

    $ spawn_image = 'img/scene/spawn/%s.jpg' % spawn_type
    hide bg
    show expression spawn_image as bg
    nvl clear
    $ free_spawn_description = game.girls_list.description('free_spawn')  # описание родов на воле
    game.girl.third "[free_spawn_description]"
    if (random.randint(1, 5) == 1) and game.girls_list.whore is not True: # Смерть при родах 

      # @fdsc Девушки не умирают просто так, если договорились с драконом
      if game.girl.willing:
        $ game.dragon.drain_energy(1, True)
        $ game.chronik.live('willing_girl', None)
        call lb_willing_help
        return
  
      $  text = u'После этого роженица погибла. Новорождённое отродье не осталось голодным. ' 
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      $ current_image='img/scene/parturition_death_free.jpg'
      $ game.chronik.death('free_birth',current_image)
      hide bg
      show expression current_image as bg
      if not game.girl.cripple:
        $ text = game.girls_list.description('birth_death')
      else:
        $ text = game.girls_list.description('birth_death_cripple')
      game.girl.third "[text]"   # событие "смерть девушки при родах"
      $ game.girl.pregnant=-1
      if game.girls_list.is_love:  # Роман с ящериком
        call lb_love_die_lizardman from _call_lb_love_die_lizardman_3
    else:
      $text = u'Роды прошли благополучно. \n\n' 
      $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)
      if game.girl.blind:
        $ text = u'После родов у %s открылось мистическое Внутреннее зрение. \n\n' % (game.girl.name_r)
        game.girl.third '[text]'
        $ game.chronik.write_chronik(text,game.dragon.level,game.girl.girl_id)     
    return

label lb_event_girl_hunger_death:
    $ current_image='img/scene/hunger_death.jpg'
    $ game.chronik.death('hunger_death',current_image)
    hide bg
    show expression current_image as bg
    nvl clear
    $ game.girls_list.description('hunger_death', True)  # описание смерти девушки от голода
    return

label lb_event_girl_kill:
    hide bg
    show expression 'img/scene/girl_death.jpg' as bg
    nvl clear
    $ game.girls_list.description('kill', True)  # убивают из-за беременности
    return

label lb_spawn_devastation:
    $ spawn_type = game.active_spawn
    $ spawn_image = 'img/scene/spawn/%s.jpg' % spawn_type
    hide bg
    show expression spawn_image as bg
    nvl clear
    $ n=random.randint(1,5)
    $ txt = game.interpolate(txt_spawn_devastation[spawn_type][n][0])
    '[txt]'
    return
