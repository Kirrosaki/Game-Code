image bg streets = "images/battle screen/BG/Battle-Streets1.jpg"
image semi Idle = "images/dungeon/Sanavi/Idle/SanIdle_6.png"

image Sanidle:
    "images/dungeon/Sanavi/Idle/SanIdle_1.png"
    pause 0.2
    "images/dungeon/Sanavi/Idle/SanIdle_2.png"
    pause 0.2
    "images/dungeon/Sanavi/Idle/SanIdle_3.png"
    pause 0.2
    "images/dungeon/Sanavi/Idle/SanIdle_4.png"
    pause 0.2
    "images/dungeon/Sanavi/Idle/SanIdle_5.png"
    pause 0.2
    repeat

image SanRun:
    "images/dungeon/Sanavi/run/SanRun_1.png"
    pause 0.18
    "images/dungeon/Sanavi/run/SanRun_2.png"
    pause 0.18
    "images/dungeon/Sanavi/run/SanRun_3.png"
    pause 0.18
    "images/dungeon/Sanavi/run/SanRun_4.png"
    pause 0.18
    "images/dungeon/Sanavi/run/SanRun_5.png"
    pause 0.18
    "images/dungeon/Sanavi/run/SanRun_6.png"
    pause 0.18
    repeat

image TutBossIntro:
    "images/dungeon/tutboss/intro/bossIntro_1.png"
    pause 0.1
    "images/dungeon/tutboss/intro/bossIntro_2.png"
    pause 0.1
    "images/dungeon/tutboss/intro/bossIntro_3.png"
    pause 0.1
    "images/dungeon/tutboss/intro/bossIntro_4.png"
    pause 0.1
    "images/dungeon/tutboss/intro/bossIntro_5.png"
    pause 0.1
    "images/dungeon/tutboss/intro/bossIntro_6.png"
    pause 0.1
    repeat

image TutBossIdle:
    "images/dungeon/tutboss/idle/bossIdle_1.png"
    pause 0.2
    "images/dungeon/tutboss/idle/bossIdle_2.png"
    pause 0.2
    "images/dungeon/tutboss/idle/bossIdle_3.png"
    pause 0.2
    "images/dungeon/tutboss/idle/bossIdle_4.png"
    pause 0.2
    "images/dungeon/tutboss/idle/bossIdle_5.png"
    repeat

image Sanavi Battle = Movie(play="images/battle screen/Sanavi/Sanavi_Battle.webm", mask="images/battle screen/Sanavi/Sanavi_Battle_mask.webm")

image Vastrial = Movie(play="images/battle screen/Vastrial/Vast_bat.webm", mask="images/battle screen/Vastrial/Vast_bat_alpha.webm")

image SanBatDef = ConditionSwitch(
    "player == 0", Movie(play="images/Conversation/Sanavi/fem/San_Bat_Def.webm", mask="images/Conversation/Sanavi/fem/San_Bat_Alpha.webm"),
    "player == 1", Movie(play="images/Conversation/Sanavi/masc/San_Bat_Def.webm", mask="images/Conversation/Sanavi/masc/San_Bat_Alpha.webm"),
    "player == 2", Movie(play="images/Conversation/Sanavi/nb/San_Bat_Def.webm", mask="images/Conversation/Sanavi/nb/San_Bat_Alpha.webm"),
    )

image SanBatAnn = ConditionSwitch(
    "player == 0", Movie(play="images/Conversation/Sanavi/fem/San_Bat_Annoy.webm", mask="images/Conversation/Sanavi/fem/San_Bat_Alpha.webm"),
    "player == 1", Movie(play="images/Conversation/Sanavi/masc/San_Bat_Annoy.webm", mask="images/Conversation/Sanavi/masc/San_Bat_Alpha.webm"),
    "player == 2", Movie(play="images/Conversation/Sanavi/nb/San_Bat_Annoy.webm", mask="images/Conversation/Sanavi/nb/San_Bat_Alpha.webm"),
    )

image SanDefDef = ConditionSwitch(
    "player == 0", Movie(play="images/Conversation/Sanavi/fem/San_Def_Def.webm", mask="images/Conversation/Sanavi/fem/San_Def_Alpha.webm"),
    "player == 1", Movie(play="images/Conversation/Sanavi/masc/San_Def_Def.webm", mask="images/Conversation/Sanavi/masc/San_Def_Alpha.webm"),
    "player == 2", Movie(play="images/Conversation/Sanavi/nb/San_Def_Def.webm", mask="images/Conversation/Sanavi/nb/San_Def_Alpha.webm"),
    )

image SanDefHap = ConditionSwitch(
    "player == 0", Movie(play="images/Conversation/Sanavi/fem/San_Def_Happ.webm", mask="images/Conversation/Sanavi/fem/San_Def_Alpha.webm"),
    "player == 1", Movie(play="images/Conversation/Sanavi/masc/San_Def_Happ.webm", mask="images/Conversation/Sanavi/masc/San_Def_Alpha.webm"),
    "player == 2", Movie(play="images/Conversation/Sanavi/nb/San_Def_Happ.webm", mask="images/Conversation/Sanavi/nb/San_Def_Alpha.webm"),
    )

image SanDefAnn = ConditionSwitch(
    "player == 0", Movie(play="images/Conversation/Sanavi/fem/San_Def_Annoy.webm", mask="images/Conversation/Sanavi/fem/San_Def_Alpha.webm"),
    "player == 1", Movie(play="images/Conversation/Sanavi/masc/San_Def_Annoy.webm", mask="images/Conversation/Sanavi/masc/San_Def_Alpha.webm"),
    "player == 2", Movie(play="images/Conversation/Sanavi/nb/San_Def_Annoy.webm", mask="images/Conversation/Sanavi/nb/San_Def_Alpha.webm"),
    )

image SanWorkDef = ConditionSwitch(
    "player == 0", Movie(play="images/Conversation/Sanavi/fem/San_Work_Def.webm", mask="images/Conversation/Sanavi/fem/San_Work_Alpha.webm"),
    "player == 1", Movie(play="images/Conversation/Sanavi/masc/San_Work_Def.webm", mask="images/Conversation/Sanavi/masc/San_Work_Alpha.webm"),
    "player == 2", Movie(play="images/Conversation/Sanavi/nb/San_Work_Def.webm", mask="images/Conversation/Sanavi/nb/San_Work_Alpha.webm"),
    )

image SanWorkHap = ConditionSwitch(
    "player == 0", Movie(play="images/Conversation/Sanavi/fem/San_Work_Happ.webm", mask="images/Conversation/Sanavi/fem/San_Work_Alpha.webm"),
    "player == 1", Movie(play="images/Conversation/Sanavi/masc/San_Work_Happ.webm", mask="images/Conversation/Sanavi/masc/San_Work_Alpha.webm"),
    "player == 2", Movie(play="images/Conversation/Sanavi/nb/San_Work_Happ.webm", mask="images/Conversation/Sanavi/nb/San_Work_Alpha.webm"),
    )

image SanWorkAnn = ConditionSwitch(
    "player == 0", Movie(play="images/Conversation/Sanavi/fem/San_Work_Annoy.webm", mask="images/Conversation/Sanavi/fem/San_Work_Alpha.webm"),
    "player == 1", Movie(play="images/Conversation/Sanavi/masc/San_Work_Annoy.webm", mask="images/Conversation/Sanavi/masc/San_Work_Alpha.webm"),
    "player == 2", Movie(play="images/Conversation/Sanavi/nb/San_Work_Annoy.webm", mask="images/Conversation/Sanavi/nb/San_Work_Alpha.webm"),
    )

image AlexDefDef = Movie(play="images/Conversation/Alexia/alex_def_def.webm", mask="images/Conversation/Alexia/alex_def_alpha.webm")
image AlexDefHap = Movie(play="images/Conversation/Alexia/alex_def_happ.webm", mask="images/Conversation/Alexia/alex_def_alpha.webm")
image AlexDefAnn = Movie(play="images/Conversation/Alexia/alex_def_annoy.webm", mask="images/Conversation/Alexia/alex_def_alpha.webm")
image AlexWorkDef = Movie(play="images/Conversation/Alexia/alex_work_def.webm", mask="images/Conversation/Alexia/alex_work_alpha.webm")
image AlexWorkHap = Movie(play="images/Conversation/Alexia/alex_work_happ.webm", mask="images/Conversation/Alexia/alex_work_alpha.webm")
image AlexWorkAnn = Movie(play="images/Conversation/Alexia/alex_work_annoy.webm", mask="images/Conversation/Alexia/alex_work_alpha.webm")
image ZavWorkDef = Movie(play="images/Conversation/Zavir/zav_work_def.webm", mask="images/Conversation/Zavir/zav_work_alpha.webm")
image ZavWorkHap = Movie(play="images/Conversation/Zavir/zav_work_happ.webm", mask="images/Conversation/Zavir/zav_work_alpha.webm")
image ZavWorkAnn = Movie(play="images/Conversation/Zavir/zav_work_annoy.webm", mask="images/Conversation/Zavir/zav_work_alpha.webm")
image VasDroid = Movie(play="images/Conversation/Vastrial/vast_droid.webm", mask="images/Conversation/Vastrial/vast_droid_alpha.webm")
