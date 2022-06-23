# Определение персонажей игры.
define e = Character('Я', color="#00BFFF", image='anton')
define q = Character("[name]")
define al = Character('Торговец', color='#FFA500')
define k = Character("Кузнец", color='#FFA500')
define pek = Character("Пекарня", color='#FFA500')

    #with moveinleft  -  персонаж появляется с левой стороны
    #with easeinleft  -  персонаж появляется с левой стороны
    #hade "имя картинки" with moveoutleft  - персонаж уходит в левую сторону
    #В диалоге {w} ".....{w}..." - продолжит идти после нажатия кнопки
    #а если добавить {w=2} - продолжит через 2 секунды
    #
    #
    #
define audio.fon_menu = "audio/fon_menu.ogg"
define audio.les = "audio/fon_menu.ogg"
# define audio.antasy. = "audio/antasy.ogg"

# мини игры разпознайка
screen t:
    timer 0.05 repeat True action If(t>0,SetVariable("t",t-0.02),Jump(labell))
    bar value t range 2 xalign 0.5 xmaximum 300
screen galaxy:
    modal True
    use t
    frame:
        xalign 0.5 yalign 0.25
        if labell == "vopros_one":
            xsize 500 ysize 500
            text"*" xpos 206 ypos 192
            text"*" xpos 262 ypos 270
            text"*" xpos 184 ypos 367
            text"*" xpos 356 ypos 188
            text"*" xpos 345 ypos 345
            text"*" xpos 90 ypos 412
            text"*" xpos 437 ypos 455
            text"*" xpos 427 ypos 82
        if labell =="vopros_two":
            xsize 500 ysize 500
            text"*" xpos 128 ypos 143
            text"*" xpos 208 ypos 160
            text"*" xpos 285 ypos 231
            text"*" xpos 274 ypos 282
            text"*" xpos 385 ypos 257
            text"*" xpos 358 ypos 312
screen map12:
    #выделение объекта
    imagemap:
        hover 'images/mapp_hover.png'
        idle 'images/mapp_idle.png'
        hotspot (450,260,100,100) action Jump('City')
        hotspot (450,495,650,100) action Jump('path1')
        #hotspot (670,77,240,240) action Jump('digging')
screen map11:
    #выделение объекта
    imagemap:
        hover 'images/mapp_hover.png'
        idle 'images/mapp_idle.png'
        hotspot (450,260,100,100) action Jump('City')
        hotspot (450,495,650,100) action Jump('path1')
        hotspot (670,77,240,240) action Jump('digging')
#### сундук
screen chest2:
    imagemap:
        hover 'images/chest21.png'
        idle 'images/chest2.png'
        hotspot (200,145,905,520) action Jump('digging3')
screen chest3:
    imagemap:
        hover 'images/chest31.png'
        idle 'images/chest3.png'
        hotspot (196,258,962,500) action Jump('digging4')
# screen chest4:
#     imagemap:
#         hover 'images/chest41.png'
#         idle 'images/chest4.png'
#         hotspot (450,260,100,100) action Jump('digging4')
#####
init:
    image home="room/home1.jpg"
    image corr="room/corridor1.jpg"
    image zal="room/zal1.jpg"

    $ centre1 = Position(xalign=0.55, yalign=0.5) # расположение персонажа по x , y
    $ left1 = Position(xalign=0.2, yalign=1.0) # персонаж с лева
    $ right = Position(xalign=0.8, yalign=1.0) # персонаж с право

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Фон главное меню
image menu_slideshow:
    "gui/main_menu4.jpg" with dissolve
    pause 3.0
    "gui/main_menu3.jpg" with dissolve
    pause 3.0
    "gui/main_menu2.jpg" with dissolve
    pause 3.0
    "gui/main_menu1.jpeg" with dissolve
    pause 3.0
    repeat
# Игра начинается здесь:



#######################################

label start:
    $qwest = 0 #квест не взят и не выполнен
    $cvetok = 0 #цветка нет
    $dang = 0 #пещера цела
    $p1 = 0 #удочка
    $p2 = 0 #лопата
    $p3 = 0 #ключ
    $cv = 0 #цветок заблокирован
    "Добро пожалоть в визуальную новеллу"
#    show screen button
    "Вступление...."
    # stop fadeout 1
    scene les with dissolve #плавный переход
    "Вашего главного героя зовут Антон, то вы можете поменять его имя"
    python:
        name = renpy.input(_("Поменять его имя, или же нажая Enter"))
        name = name.strip() or __("Антон")
        "Приятной игры, [name]"
    show anton smile at centre1
    e smile "Я ваш главный персонаж"
    $ last_item = None
    show screen inventory
    show screen cheat
    show screen map123
    show screen quast1
    "А теперь покажу вам как работает инвентарь"
    #$ items.extend([("map_idle", "Карта")])
    #$ items.extend([("key", "Ключ")])
    #$ items.extend([("fishing", "Удочка")])
    "Это очень просто, давайте начнем с простого примера. Давай я дам тебе денежку"
    $ items.extend([("coin", "Денюжка")])

label give:
    "Воспользуйся монетой в своем инвентаре, что бы пополнить баланс"
    jump give

label money:
    $ money += 100
    "Молодец, на твоем счету появилось 100$"
    "Отлично теперь вы научились использовать инвентарь"
    "Теперь перейдет к следующему этапу..."
    "Начало сюжетной линии."
    "Какое-то событие происходит..."
    "Попробуй за пару секунд распознать, что за созвездие перед тобой."
    scene frame1 with dissolve
    hide anton smile
    jump mygame
    return
##    menu:
#        e "Куда отправиться?"

#        "Алхимия":
#            jump alchemy
#        "Провинзия":
#            jump food
#        "Кузня":
#            jump smithy
#        "Отправиться в путь":
#            jump map

#    return

##игра разпознайка
label mygame:
    hide les with dissolve
    hide ploshchad
    hide medvidisa
    hide dielebed
    scene frame1
    "Попробуй за пару секунд распознать, что за созвездие перед тобой."
    $t = 3
    $ labell = "vopros_one"
    show screen galaxy
    "Время пошло!"
    return
label vopros_one:
    hide screen galaxy
    menu:
        "Что за созвездие?"
        "Лебедь":
            show dielebed:
                xalign 0.5 yalign 0.5
            "Это правильно!"
            jump two
        "Медведица":
            show dielebed:
                xalign 0.5 yalign 0.5
            "Это неправильно!"
            jump mygame
    return

label two:
    hide medvidisa
    hide dielebed
    "Попробуй за пару секунд распознать, что за созвездие перед тобой."
    $t = 2
    $ labell = "vopros_two"
    show screen galaxy
    "Время пошло!"
    return
label vopros_two:
    hide screen galaxy
    menu:
        "Что за созвездие?"
        "Лебедь":
            show medvidisa:
                xalign 0.5 yalign 0.5
            "Это неправильно!"
            jump mygame
        "Медведица":
            show medvidisa:
                xalign 0.5 yalign 0.5
            "Это правильно!"
            jump City
    return





#Алхимия
label alchemy0:
    scene alkhimiya
    with fade
    al "Приветсвую вас, дорогой покупать!"
    $p3 = 0 #ключ
    $cv = 0 #цветок заблокирован
    jump alchemy
    return

label alchemy:
    scene alkhimiya
    with fade
    $text_qwest11 = "В пещере за озером растет одно редкое растение, оно необходимо мне для изготовления тайного зелья, исцеляющего недуг моего сына. Если ты принесешь мне его, я расскажу тебе где спрятан сундук с добром одного нашего бывшего мера, и даже случайно у меня завалялся ключ от этого сундка."
    $text_qwest12 = "Но вход в эту пещеру запечатан, тебе придется найти способ попасть внутрь."
    al "Чем могу помочь?"
    # $qwest = 3
    # $cvetok = 1
    # $ items.extend([("flower", "Цветок")])
    menu:
        "Я хотел бы взглянуть на ваш товар":
            al "Да, конечно"
            jump alchemy1
        "Хотел кое-что продать":
            al "Да, конечно"
            jump alchemy2
        "Есть ли у вас какая-нибудь роботенка для меня?":
            if qwest == 0:
                al "Хмм..."
                al "Дай ка подумать"
                al "Есть одно дельце, если ты готов"
                e "Рассказывай"
                al "[text_qwest11]"
                al "[text_qwest12]"
                al "Ну что, ты согласен?"
                menu:
                    "Хорошо, я принесу тебе это растение":
                        al "Хорошо, надеюсь, ты записал все в свой журнал, чтобы не перишлось спрашивать меня по 30 раз."
                        $qwest = 1
                        #Добавление в журнал
                        jump alchemy
                    "Нет, я еще не готов":
                        al "Слабак..."
                        jump alchemy
            if qwest == 1 or qwest == 2:
                al "Ты уже сделал то, о чем я тебя просил?"
                menu:
                    "Еще нет, я в процессе":
                        al "Скорее бы уже"
                        jump alchemy
                    "Да, я принес тебе цветок. Знаешь, это было непросто":
                        if qwest == 2:
                            jump give1
                        else:
                            al "Не ври мне, сукин сын"
                            "..."
                            jump alchemy
                    "Напомни, что нужно было сделать":
                        al "[text_qwest11]"
                        al "[text_qwest12]"
                        jump alchemy
                    "Боюсь, я не смогу выполнить твою просьбу":
                        al "Очень жаль"
                        $qwest = 0
                        jump alchemy

            if qwest == 3 or qwest == 4 or qwest == 5:
                al "Пока ничего нет, заходи в следующий раз"
                jump alchemy

        "Город":
            jump City
    return
label give1:
    $cv = 1
    al "Ого! Молодец, дружище, давай его скорее"
    jump give1
label alchemy1:
    scene alkhimiya
    with fade
    menu:
        "Удочка    50$":
            menu:
                "Купить":
                    if money >= 50:
                        $ items.extend([("rod", "Удочка")])
                        $ money -= 50
                    else:
                        al "Эй, сначала деньги!"
                    jump alchemy1
                "Отказаться":
                    jump alchemy1
        "Лопата    30$":
            menu:
                "Купить":
                    if money >= 30:
                        $ items.extend([("shovel", "Лопата")])
                        $ money -= 30
                        $p3 = 0
                    else:
                        al "Эй, сначала деньги!"
                    jump alchemy1
                "Отказаться":
                    jump alchemy1
        # "Ключ    20$":
        #     menu:
        #         "Купить":
        #             if money >= 20:
        #                 $ items.extend([("key", "Ключ")])
        #                 $ money -= 20
        #             else:
        #                 al "Эй, сначала деньги!"
        #             jump alchemy1
        #         "Отказаться":
        #             jump alchemy1
        "Вернуться обратно":
            jump alchemy
    return
#Продажа
label alchemy2:
    scene alkhimiya
    with fade
    menu:
        "Лосось    10$":
            menu:
                "Продать":
                    $ money += 10
                    jump alchemy2
                "Отказаться":
                    jump alchemy2
        "Карп    15$":
            menu:
                "Продать":
                    $ money += 15
                "Отказаться":
                    jump alchemy2

        "Удочка    15$":
            menu:
                "Продать":
                    $ money += 15
                    jump alchemy2
                "Отказаться":
                    jump alchemy2
        "Лопата    15$":
            menu:
                "Продать":
                    $ money+= 15
                    jump alchemy2
                "Отказаться":
                    jump alchemy2
        # "Ключ    10$":
        #     menu:
        #         "Продать":
        #             $ money += 10
        #             jump alchemy2
        #         "Отказаться":
        #             jump alchemy2
        "Вернуться обратно":
            jump alchemy
    return

label qwest_coplete:
    al "Держи ключь от сундука, а так же я пометил место, где его искать, на твоей карте. Но для начала тебе понадобиться лопата, ты можешь приобрести ее у меня."
    $ items.extend([("key", "Ключ")])
    $p3 = 0 #ключ
    $cv = 0 #цветок заблокирован
    $qwest = 3
    jump alchemy

# алхимия выбор купить/продать
# label alchemy3:
#     scene alkhimiya
#     with fade
#     $ p3 = 0
#     menu:
#         "Я хотел бы взглянуть на ваш товар":
#             al "Да, конечно"
#             jump alchemy1
#         "Хотел кое-что продать":
#             al "Да, конечно"
#             jump alchemy2
#         "Город":
#             jump City


# #Пекарня
# label food:
#     scene pekarnya
#     with fade
#     menu:
#         pek "Приветсвую вас, дорогой покупать!"
#         "Купить":
#             jump City
#         "Город":
#             jump City
#     return
# #Кузня
# label smithy:
#     scene kuznya
#     with fade
#     menu:
#         k "Приветсвую вас, дорогой покупать!"
#         "Купить":
#             jump City
#         "Город":
#             jump City
#     return
#локация город
label City:
    hide screen map12
    hide screen map11
    scene ploshchad
    with fade
    $ p1 = 0
    menu:
        e "Куда отправиться?"
        "Лавка":
            jump alchemy0
        # "Провинзия":
        #     jump food
        # "Кузня":
        #     jump smithy
        "Выйти из города":
            jump map

    return
label map:
    $ p1 = 0
    $ p2 = 0
    $p3 = 0 #ключ
    $cv = 0 #цветок заблокирован
    # hide les1
    hide anton smile
    scene mapp_idle
    with fade
    show mapp_idle
    if qwest == 3:
        show screen map11
    else:
        show screen map12
    show screen cheat
    #show screen map123
    "Куда же пойти.."
    # jump map
    $renpy.pause(delay=None, hard=True)



#копка лопатой
label digging:
    hide screen map12
    hide screen map11
    scene chest1
    with fade
    $ p2 = 1
    menu:
        "Воспользуйтесь Лопатой"
        "Вернуться в глобольную карту":
            jump map
    return

label digging2:
    show screen chest2
    with fade
    "Нажмите на эту местность"
    jump digging2
    return

label digging3:
    hide screen chest2
    show screen chest3
    with fade
    "Интересно, что мы там найдем?"
    jump digging3
    return

label digging4:
    hide screen chest3
    show chest4
    with fade
    $ p3 = 1
    $qwest = 4
    menu:
        "Воспользуйтесь ключом"
        "Вернуться в глобольную карту":
            jump map
    return
label digging5:
    hide screen chest4
    show chest5
    with fade
    $ money += 1000
    $qwest = 5
    "Вы открыли сундук и вам прибавилось 1000$"
    menu:
        "Вернуться в глобольную карту":
            jump map
    return

#локация петешествие
# label :
#     scene les1 with dissolve
#     #with fade
#     "Вы слышите какие-то от попутчиков истории..."
#     "некоторое время вы приезжаете к месту назначения"
#     "Видите неподалеку подземелье"
#     menu:
#         e "Вот оно, как искатель приключений, это прибыльное дело"
#
#         "Зайти внутрь":
#             jump dungeon
#
#         "Пойти порыбачить":
#             jump path1
#
#     return
label dangeon:
    hide screen map12
    hide screen map11
    scene podzemelye1 with fade

    "Видите неподалеку пещеру"
    e "Должно быть, это то место, о котором говорил алхимик. Но вход завален, как же пробраться внутрь..."
    "Вы замечаете небольшую впадину, а за ней каменная дверь, на ней изображены странные символы"
    menu:
        "Подойти и попробовать открыть вход":
            if dang == 0:
                e "Ну что ж, попробуем"
                jump blink
            else:
                "Dход в пещеру разрушен, и вам нbчего не остается, как вернуться к озеру"
                jump path1
        "Вернуться к озеру":
            jump path1

    return

label dangeon1:
    scene podzemelye
    with dissolve
    "Заходите все глубже и глубже вы замечаете стаю волков."
    "Подходя еще ближе, вас замечают, и начинается битва."
    $result = renpy.random.randint(1,1)
    if result == 0:
        "Волки постепенно одолевают вас. Последнее, что вы видите, это их свирепык морды. Кажется, это конец..."
        return
    else:
        "После долгой битвы вы одолеваете их. После ненадолгой передышки вы решаетесь отправиться дальше"
        menu:

            "подземелье 2 уроня":
                jump dungeon2
        return

label dungeon2:
    scene podzemelye with dissolve

    "На середине залитой странным светом комнаты вы замечете необычный цветок"
    e "это то, что мне нужно!"
    "..."
    "Вы подходите ближе..."
    menu:
        "Сорвать цветок":
            $cvetok = 1
            $qwest = 2
            $ items.extend([("flower", "Цветок")])
            $dang = 1 #пещера разрушена
            $p3 = 0 #ключ
            $cv = 0 #цветок заблокирован
            "Свет в комнате резко гаснет, а пол и стены пещеры начинает трясти"
            "Вам ничего не остается, как бежать, сломя голову к выходу..."
            jump path1
        "Убежать в панике":
            $dang = 1 #пещера разрушена
            "Свет в комнате резко гаснет, а пол и стены пещеры начинает трясти"
            "Вам ничего не остается, как бежать, сломя голову к выходу..."
            jump path1

    return

label path1:
    hide screen map12
    hide screen map11
    scene les1 with fade
    $p3 = 0 #ключ
    $ cv = 0 #цветок заблокирован
    $ p1 = 1 #флаг, что мы находимся в локации path
    "Вы добрались до озера"
    menu:
        "Порыбачить":
            "Воспользуйтесь удочкой"
            jump path1
        "Подойти к пещере":
            jump dangeon
        "Вернуться к глобалной карте":
            jump map
    return

label StartMiniGame:
    $ FishUp = renpy.random.randint(30,50) #Отвечает за то откуда рыба начнет
    show screen Fish_Up
    call screen MiniGameFish
    if _return == "EndMiniGame":
        jump start


# label dungeon:
#     scene podzemelye
#     with dissolve
#     "Заходите все глубже и глубже вы замечаете стая волков."
#     "Подходя еще ближе, вас замечают и начинается битва."
#     "После долгой битвы вы одолеваете их. После ненадолгой передышки вы решаетесь отправиться дальше"
#     menu:
#
#         "подземелье 2 уроня":
#             jump dungeon2
#     return

# label dungeon2:
#     scene podzemelye with dissolve
#
#     "Видите босса подземелье"
#     " и пытаетесь сразиться с ним"
#     "..."
#     "Вы с чудом одолеваете босса и забираете сокривища"
#     menu:
#         "Оказалась славная битва"
#         "Вернуть в город":
#             jump City2
#     return
label City2:
    scene ploshchad
    with fade
    "Вас встречаю народ и вас подздравляют с почетом"
    "И вас сам лично король дарует титул <из князя в грязи>"
    "Завершение новеллы"
    return
