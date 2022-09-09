# coding=utf-8
init python:
    from pythoncode.utils import weighted_random
    from pythoncode.characters import Enemy
        
label lb_location_sky_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))    
    $ place = 'sky'
    hide bg
    show expression get_place_bg(place) as bg    
    nvl clear
    
    if game.dragon.energy() == 0:
        'Даже драконам надо иногда спать. Особенно драконам!'
        return
        
    if not game.dragon.can_fly: 
        '[game.dragon.name] с тоской смотрит в небо. Если бы только он умел летать...'
    else:
        call lb_encounter_sky from _call_lb_encounter_sky
    return

    if game.witch_st1==5:
      'Дракон на мгновение задумывается, какой может быть награда ведьмы.'
      game.dragon 'Надо сходить проверить!'
      return
    
label lb_encounter_sky:
    $ nochance = game.poverty.value * 3
    $ choices = [
        ("lb_titan_found", 10),
        ("lb_enc_swan", 10),
        ("lb_enc_griffin", 10),
        ("lb_enc_skyboat", 10),
        ("lb_abbey_found", 10),
        ("lb_castle_found", 10),
        ("lb_palace_found", 10),
        ("lb_enc_fair_sky", 10),
        ("lb_enc_caravan_sky", 10),
        ("lb_enc_militia_sky", 10),
        ("lb_enc_cannontower", 10),
        ("lb_jotun_found", 10),
        ("lb_ifrit_found", 10),
        ("lb_enc_fear_sky",20),
        ("lb_summon_sky", 6 * game.desperate),
        ("lb_patrool_sky", 3 * game.mobilization.level),
        ("lb_enc_noting", nochance)]
    $ enc = weighted_random(choices)
    $ renpy.call(enc)

    return

label lb_enc_fear_sky:
#    $ game.fear=11
    if game.fear<4 or game.historical_check('de_Ad'):
        jump lb_encounter_sky   # При низком страхе встречи не происходит
    else:
        'Паря в небесах, дракон углядел далеко внизу кое-что интересное...'
        call lb_fear_plains from _call_lb_fear_plains_2    # Основной эвент страха равнин (а-ля Синяя борода)
    return

label lb_summon_sky:  # Призыв в небесах
    if game.summon.seal>data.max_summon:
      jump lb_encounter_sky   # При уже вызванном демоне встречи не происходит.
    else:
      'Паря в небесах, дракон углядел далеко внизу кое-что интересное...'
      call lb_summon from _call_lb_summon_5
    return    

    
label lb_enc_swan:
    'Величественно паря в облаках, [game.dragon.fullname] видит стаю белых лебедей. Впереди летит огромный откормленный вожак - он отлично сгодиться в качестве закуски!'
    nvl clear
    menu:
        'Сожрать гуся' if game.dragon.hunger > 0:
            $ game.dragon.drain_energy()
            '[game.dragon.name] ловит и пожирает гуся.'
            python:
                if game.dragon.bloodiness > 0:
                    game.dragon.bloodiness = 0
                game.dragon.hunger -= 1
        'Разогнать стаю' if game.dragon.bloodiness >= 5 and game.dragon.hunger == 0:
            $ game.dragon.drain_energy()
            '[game.dragon.name] жестоко задирает вожака и ещё нескольких птиц, а остальная стая в панике разлетается кто куда.'    
        'Пролететь мимо' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return
    
label lb_enc_griffin:
    'Хм. Над далёкими утёсами кружится стая крупных птиц.'
    nvl clear
    jump lb_griffin

label lb_griffin:
    $ place = 'sky'
    hide bg
    show expression get_place_bg(place) as bg
    nvl clear
    if not game.dragon.can_fly: 
        '[game.dragon.name] с тоской смотрит в небо. Если бы только он умел летать...'
        return
    'В вышине парит матёрый дикий грифон. Он облетает свои владения в поисках добычи и нарушителей, причём второе, по его мнению, относится и к драконам. Может быть, стоит показать пернатому, где его место?'
    $ game.dragon.drain_energy()
    $ game.foe = Enemy('griffin', game_ref=game)
    $ narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Сразиться с грифоном':
            call lb_fight from _call_lb_fight_50
            if game.dragon.hunger > 0:
                'Голодный [game.dragon.name] съедает грифона прямо в воздухе и бросает останки вниз на поживу шакалам.'
                python:
                    if game.dragon.bloodiness > 0:
                        game.dragon.bloodiness = 0
                    game.dragon.hunger -= 1
                    game.dragon.add_effect('griffin_meat')
            else:
                '[game.dragon.fullname] сейчас не голоден, поэтому он даёт смертельно раненому грифону упасть вниз и разбиться о скалы.'
            $ game.dragon.del_special_place('grffin')
        'Избежать столкновения и улететь' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('grffin', 'enc_griffin')
            $ game.dragon.gain_rage()
    return
    
label lb_enc_skyboat:
    'Над облаками вздымается парус! Это один из воздушных кораблей цвергов, судя по всему - торговый. А значит, там может быть добыча...'
    python:
        game.foe = Enemy('airship', game_ref=game)
        narrator(show_chances(game.foe))
    menu:
        'Напасть':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_51
            '[game.dragon.name] стремительно обыскивает падающий вниз корабль и выгребает всё ценное:'
            python:
                count = random.randint(5, 15)
                alignment = 'dwarf'
                min_cost = 1
                max_cost = 10000
                obtained = "Это предмет с разграбленного воздушного судна цвергов."
                trs = treasures.gen_treas(count, data.loot['klad'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
            '[trs_descrptn]'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Пропустить' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()    
    return
    
label lb_enc_fair_sky:
    'Паря в вышине, [game.dragon.fullname] замечает внизу какие-то цветные пятна. Спустившись ниже, становится понятно, что это ярмарка, которую устроили люди.'
    call lb_enc_fair from _call_lb_enc_fair
    return
    
label lb_enc_militia_sky:
    '[game.dragon.fullname] замечает какое-то шевеление на земле далеко внизу. Так и есть - это собрались на тренировку ополченцы, наспех собранные из окрестных деревень.'
    call lb_enc_militia_true from _call_lb_enc_militia_true
    return
    
label lb_enc_caravan_sky:
    'Пролетая вдоль змеящейся по земле дороги, [game.dragon.fullname] замечает на ней несколько точек. Это крупный торговый караван.'
    call lb_enc_lcaravan from _call_lb_enc_lcaravan
    return
    
label lb_patrool_sky:
    python:
        chance = random.randint(0, game.mobilization.level)
        if chance < 4:
            patrool = 'archer'
            dtxt = 'Казалось бы, летишь, никого не трогаешь, и тут снизу в тебя начинают пускать стрелы! Это излишне ретивый стрелок решил показать свою удаль.'
        elif chance < 7:
            patrool = 'catapult'
            dtxt = 'Пытаясь защитить свои владения от летающих монстров, люди установили на возвышенностях башни с катапультами, стреляющими массивными оперёнными копьями с наконечниками из закалённой стали.'
        elif chance < 11:
            patrool = 'griffin_rider'
            dtxt = 'Небеса сейчас неспокойны, так что не удивительно, что люди отправили в патруль одного из своих летучих рыцарей - всадник на грифоне представляет реальную угрозу для любого крылатого монстра.'
        elif chance < 16:
            patrool = 'airship'
            dtxt = 'Разрывая облака, перед драконом вылетает огромный воздушный корабль. Это патрульный крейсер цвергов!'
        else:
            patrool = 'angel'
            dtxt = '%s вынужден зажмуриться от яркого света, бьющего в глаза. Громогласный оклик возвещает: "Умри, мерзкое порождение греха!!!". Это ангел-хранитель, посланный людям Небесами для защиты.' % game.dragon.fullname
    '[dtxt]'
    python:
        game.foe = Enemy(patrool, game_ref=game)
        battle_status = battle.check_fear(game.dragon, game.foe)
    if 'foe_fear' in battle_status:
        $ narrator(game.foe.battle_description(battle_status, game.dragon))
        return
    $ game.dragon.drain_energy()
    call lb_fight(skip_fear=True) from _call_lb_fight_52
    return
