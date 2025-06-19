image Cut1 = "images/locations/Greed Cave.png"
image Cut2 = "images/locations/OldCitySki.jpg"
image SanRoom = "images/locations/San_Room.png"
image SanRoomN = "images/locations/San_RoomN.png"
image XiMall = "images/locations/XI_Mall.png"
image ZitBar = "images/locations/Ziti_Bar.png"
image LisOpen = "images/Conversation/Lisalsa/Lisalsa_Opening.png"
image LycOpen = "images/Conversation/Lyck/Lyck_Opening.png"

define audio.Cave = "audio/Music/Ambient/Cave_Ambient.mp3"
define audio.SanRoom = "audio/Music/Ambient/sanavi_theme.mp3"
define audio.GiftShop ="audio/Music/Ambient/giftshop_theme.mp3"
define audio.Zitis = "audio/Music/Ambient/zitibar_theme.mp3"


define la = Character("Lisalsa")
define lk = Character ("Lyck")
define va = Character ("Vastrial")
define sn = Character ("Sanavi")
define al = Character ("Alexia")
define za = Character ("Zavir")
define AM = Character ("Auto Miss")

default player = "2"

label Cut1:
    play music Cave loop volume 0.5 fadein 1.0

    scene Cut1 with fade

    show LisOpen at left
    with dissolve

    la "It's finally time."
    la "After all these years,"
    la "You're gonna pay, Vastrial."

    show LycOpen at right
    with dissolve

    lk "So are you just gonna stare at the Gate or are you gonna test it out?"


    la "..."
    la "Let's see what your toy can do."

    scene black with fade
    hide screen clock
    hide screen day

    $ pass_time(10)

    call screen choose

label Cut2:
    play music Xi_dungeon loop volume 0.5 fadein 1.0
    scene Cut2 with fade

    show screen clock
    show screen day

    show VasDroid at right
    with dissolve

    va "Hey Babe,"
    va "I don't think you're supposed to be out here."
    va "I don't remember The Council telling you to hunt."

    show SanBatDef at left
    with dissolve

    sn "I felt... something."
    sn "Something that shouldn't be here."

    va "Could it just be a Manifested?"

    sn "No. It's defintely from Tartarus."

    va "..."
    va "Well then, let's find the fucker."
    va "I'll deal with Azrael."

    scene black with fade

    "Move by clicking the mouse! Enter buildings and areas by clicking the arrow."

    $ Location = Local1
    $ pass_time(10)

    jump local_check

label Cut5:

    show VasDroid at right
    va "That-"
    va "That's not possible, Babe."
    va "Nothing that strong can come through unless-"

    show SanBatDef at left

    sn "The Gate is weakening again."
    sn "Good, I've missed a real fight."

    hide SanBatDef

    va "Sanavi!"

    $ Location = Local3

    hide VasDroid

    return

label Inter1:

    show image [selected_character.name] at right
    with moveinright

    va "We need to kill the leader, or they'll just keep coming."

    return

label Cut6:
    play music Xi_dungeon loop volume 0.1 fadein 1.0
    $ menu_choice = "n"
    scene Cut2 with fade

    show VasDroid at right
    with dissolve

    va "I don't like this, Babe."
    va "I'm going to have to tell Azrael what happened."

    show SanBatDef at left
    with dissolve

    menu:
        "Annoyed":
            show SanBatAnn at left with dissolve
            hide SanBatDef

            sn "Do whatever you have to."
            sn "I'm going home."

            hide SanBatAnn
            with dissolve

        "...":
            sn "I'm going home."
            hide SanBatDef
            with dissolve


    va "..."

    hide VasDroid
    with dissolve

    scene black with fade
    stop music fadeout 1.0

    jump Cut8

label Cut7:

    "HI! You've reached the End of the First Playable."

    "Consider heading back to the Discord to give your feedback,"

    "and Help development as we continue to a pre-Alpha!"

    "Thank you for your time!"

    $ renpy.quit()

label Cut8:
    $ time_in_minutes = 1800
    call daycheck from _call_daycheck
    play music SanRoom loop volume 0.2 fadein 1.0

    scene SanRoom with fade
    play sound "audio/Effects/chime1.mp3"

    AM "An Alexia is here to see you."

    show SanDefDef at left
    with dissolve

    sn "Let her in."

    show AlexDefDef at right
    with dissolve

    al "Morning!"
    al "I hope you haven't forgotten that you promised to spend time with me."

    menu:
        "Sarcastic":
            show SanDefAnn at left with dissolve
            hide SanDefDef
            sn "Even If I had, you just reminded me."
            jump badrep1

        "Friendly":
            show SanDefHap at left with dissolve
            hide SanDefDef
            sn "Of course I remember."
            jump happyrep1

        "Rude":
            show SanDefAnn at left with dissolve
            hide SanDefDef
            sn "Will you leave if I said I forgot?"
            jump badrep1


    label happyrep1:
        show AlexDefHap at right with dissolve
        hide AlexDefDef
        al "Well, Let's go!"
        al "I want to pick up plants for my place."
        al "Also your car should be fixed by now!"

        jump con1

    label badrep1:
        show AlexDefAnn at right with dissolve
        hide AlexDefDef
        al "Well, you already promised,"
        al "so you're coming whether you want to or not."
        al "I have things I want to get and you need your own car back."

        jump con1

    label con1:
        menu:
            "Friendly":
                show SanDefHap at left with dissolve
                hide SanDefAnn
                sn "Where to first?"

                scene black with fade
                stop music fadeout 1.0



            "Rude":
                show SanDefAnn at left with dissolve
                hide SanDefHap
                sn "Can't wait."

                scene black with fade
                stop music fadeout 1.0

    "Would you like to save?"

    menu:
        "Yes":
            jump Save
        "No":
            jump Cut9

label Cut9:
    $ pass_time(240)

    play music GiftShop loop volume 0.2 fadein 1.0

    scene XiMall with fade

    show AlexDefDef at right
    with dissolve

    show SanDefDef at left
    with dissolve

    al "Awesome, a new garden shop opened here last week!"
    al "I want to see what they have!"

    $ inventory.earn(400)

    hide AlexDefDef
    with dissolve

    sn "It's busy today..."
    sn "..."
    sn "A gift store?"

    hide SanDefDef
    with dissolve

    call giftstore

label Cut95:
    scene XiMall with fade

    show SanDefDef at left
    with dissolve

    show AlexDefHap at right
    with moveinright

    al "I'm back! And with a new friend!"
    al "Let's go get your car!"

    scene black with fade
    stop music fadeout 1.0

    jump Cut10

label Cut10:
    $ time_in_minutes = 2520

    play music Zitis loop volume 0.2 fadein 1.0

    scene ZitBar with fade

    show AlexWorkDef at right
    with moveinright

    show SanWorkDef at left
    with moveinleft


    al "Well now that you're mobile again,"
    al "I don't have to worry so much."

    al "I have work tonight too,"
    al "So have fun, darling!"

    menu:
        "Friendly":
            show SanWorkHap at left with dissolve
            hide SanWorkDef
            sn "You too."

        "Neutral":
            sn "Thanks."

        "Rude":
            show SanWorkAnn at left with dissolve
            hide SanWorkDef
            sn "As if."

    hide AlexWorkDef
    with moveoutright

    show SanWorkDef at left with dissolve
    hide SanWorkAnn
    hide SanWorkHap

    $ renpy.pause(0.5)

    show ZavWorkDef at right
    with moveinright

    za "So you can get to work on time!"
    za "I can't fathom why you have so much fucking trouble making it to work the few days you're expected to be here."

    menu:
        "Rude":
            show SanWorkAnn at left with dissolve
            hide SanWorkDef
            sn "I didn't ask for your evaluation, Zavir."

            jump badrep2

        "Sarcastic":
            show SanWorkAnn at left with dissolve
            hide SanWorkDef
            sn "Sorry, I didn't know you cared."

            jump badrep2

        "Neutral":
            sn "..."

            jump happyrep2

    label badrep2:
        show ZavWorkAnn at right with dissolve
        hide ZavWorkDef

        za "Well, in this case,"
        za "My feelings don't matter tonight."
        za "Boss wants me to retrain you since it's been so long."
        za "Didn't think your memory was that shit, but what do I know?"

        scene black with fade
        stop music fadeout 1.0

        jump Cut11

    label happyrep2:

        za "Ah, the silent treatment."
        za "Well you don't have to talk,"
        za "But you still have to get trained by your favorite person."
        za "Which is me, of course."

        scene black with fade
        stop music fadeout 1.0

        jump Cut11

label Cut11:
    $ pass_time(330)

    play music SanRoom loop volume 0.2 fadein 1.0

    scene SanRoomN with fade

    show SanWorkDef at left
    with moveinleft

    sn "I still haven't heard from Azrael or Vastrial..."

    menu:
        "Dismissive":
            sn "He's probably just busy."

            hide SanWorkDef
            with moveoutleft

            scene black with fade

            jump Cut7

        "Mischievous":
            show SanWorkAnn at left with dissolve
            hide SanWorkDef
            sn "I could go out anyway..."
            sn "..."
            sn "Too much trouble I guess."

            hide SanWorkAnn
            with moveoutleft

            scene black with fade

            jump Cut7

label Save:

    play music SanRoom loop volume 0.2 fadein 1.0

    scene SanRoomN with fade

    show screen save

screen choose:
    imagebutton:
        at center
        focus_mask True
        idle "f1.png"
        hover "hover.png"
        action [SetVariable("player", 0), Return()]
    imagebutton:
        at left
        focus_mask True
        idle "m1.png"
        hover "hover1.png"
        action [SetVariable("player", 1), Return()]
    imagebutton:
        at right
        focus_mask True
        idle "b1.png"
        hover "hover2.png"
        action [SetVariable("player", 2), Return()]
