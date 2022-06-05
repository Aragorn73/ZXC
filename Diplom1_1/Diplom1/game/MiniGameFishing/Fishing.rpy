init 15:
    $ Fish = 1 #Отечает за правильную работоспосбность мини игры.
    $ Broken = 0 #Отвечает за то что рыба сорвется
    $ BrokenFish = 0 #Так же отвечает за то что рыба сорвется
    $ Random_Time = 1
init -5 python:
    style.FishingBar = Style(style.default)
    style.FishingBar.left_bar = Frame("MiniGameFishing/BarFull.png", 0, 0)
    style.FishingBar.right_bar = Frame("MiniGameFishing/BarEmpty.png", 0, 0)
    style.FishingBar.thumb = "MiniGameFishing/thumb.png"
    style.FishingBar.thumb_offset = 26
    style.FishingBar.left_gutter = 35
    style.FishingBar.xmaximum = 364 # bar width
    style.FishingBar.ymaximum = 50 # bar height

screen MiniGameFish:
    add "MiniGameFishing/Bg.jpg"

    if BrokenFish == 0:
        add "MiniGameFishing/status1.jpg" align(0.5,0.6)#Изображения добовляються от значения BrokenFish
    if BrokenFish == 1:                                 #Те мы наблюдаем нятяженнось лески этими изображениями
        add "MiniGameFishing/status2.jpg" align(0.5,0.6)
    if BrokenFish == 2:
        add "MiniGameFishing/status3.jpg" align(0.5,0.6)
    if BrokenFish == 3:
        add "MiniGameFishing/status4.jpg" align(0.5,0.6)
    if BrokenFish == 4:
        add "MiniGameFishing/status5.jpg" align(0.5,0.6)


    if FishUp <= 0: #Условие кнопки которое отвечает за поимку рыбы.
        key "K_SPACE" action [Jump("YouWin"), Hide('Fish_Up'),Hide('Fish_Free'),Hide('MiniGameFish')]
    else:
        if BrokenFish <= 3:
            if Broken == 1:
                key "K_SPACE" action [SetVariable("FishUp", FishUp - 1), SetVariable("BrokenFish", BrokenFish + 1)]
            if Broken == 0:
                key "K_SPACE" action SetVariable("FishUp", FishUp - 1)
        if BrokenFish == 4:

            key "K_SPACE" action [Jump("BrokenFish_End"), Hide('Fish_Up'),Hide('Fish_Free'),Hide('MiniGameFish')]

    #В этом условий сказано. Если FishUp меньше или равно нулю, то мы побеждаем. (FishUp отвечает за наполение бара)
    #Иначе если BrokenFish меньше или равно трем, то кнопка будет выполнять 2 действия одно из которых это ограниечение количетво нажатий когда рыба вырываеться.
    #Если Broken равна 1, то мы ловим рыбу и при этом она может соваться.
    #Если Broken равна 0, то мы просто ловим рыбу
    #Если BrokenFish равна четырем, то рыба сорвется
    bar:
        style "FishingBar"
        range 150
        value FishUp
        align(0.5,0.7)
screen Fish_Up:
    timer 0.01 action SetVariable("Random_Time", renpy.random.randint(1,6))#Отвечает за паузу, в течений которой можно спокойно тянуть рыбу
    if BrokenFish >= 1:
        timer 0.7 repeat True action SetVariable("BrokenFish", BrokenFish - 1)#Отвечает за то что леска на удочке потеряет свою натяженность, Так же можно поменять время сбрасывания натяженности
    if BrokenFish == 0:
        timer 0.05 repeat True action NullAction()
    if FishUp <= 149:
        timer Random_Time repeat True action SetVariable("Fish", renpy.random.randint(1,5)), Hide("Fish_Up"),Show("Fish_Free")#Здесь у нас задаеться рандмоное значение переменой Fish
    if FishUp >= 150:                                                                                                         #По сути просто задает время сопротивления рыбы
        timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]

screen Fish_Free:
    if FishUp <= 149:
        if Fish == 1:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 2:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 3:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 4:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 5:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 6:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 7:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 8:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 9:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 10:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 11:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 12:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 13:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 14:
            if FishUp <= 149:
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 1)
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
        if Fish == 15:
            if FishUp <= 149:
                #Этот таймер всегда оставлять последним.
                #Если хотите проблить время сопротивления рыбы, то просто скопируйте одно из условий выше и вставте выше этой строки
                #Но и не забывайте менять значение Fish, Чем бельше времени которое рыба сопротивляеться, тем больше будет условий с Fish
                timer 0.03 repeat True action SetVariable("FishUp", FishUp + 1), SetVariable("Fish", Fish + 1), SetVariable("Broken", 0), Hide('Fish_Free'), Show('Fish_Up'), If(FishUp >= 150, [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')])
            if FishUp >= 150:
                timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]
    if FishUp >= 150:
        timer 0.01 action [Jump("YouLose"), Hide('Fish_Up'),Hide('Fish_Free')]


label YouLose:
    window show
    "YouLose"
    window hide
    return

label YouWin:
    $ TypeFish = renpy.random.choice(["Лосось", "Карп", "Сайга", "Рыба Ёж"])
    window show
    "[TypeFish]"
    window hide
    $ renpy.pause(2, hard=True)
    jump path
    return

label BrokenFish_End:
    "Рыба сорвалась"
    window hide
    return
#Мини Игру написал DarkSoulHero
#Что делать с этой информацией решать вам
