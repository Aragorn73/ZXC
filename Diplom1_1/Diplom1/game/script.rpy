# Определение персонажей игры.
define e = Character('Я', color="#00BFFF", image='anton')
define q = Character("[name]")
define al = Character('Алхимик', color='#FFA500')
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
#screen room:
    #выделение объекта
#    imagemap:
#        hover 'images/room/my_room1_hover.jpg'
#        idle 'images/room/my_room1_idle.jpg'
#        hotspot (570,577,795,255) action Jump('corridor')
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
    "Добро пожалоть в визуальную новеллу"
#    show screen button
    "Вступление...."
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
    "А теперь покажу вам как работает инвентарь"
    #$ items.extend([("map_idle", "Карта")])
    #$ items.extend([("key", "Ключ")])
    #$ items.extend([("fishing", "Удочка")])
    show screen cheat
    show screen map123
    "Это очень просто, давайте начнем с простого примера "
    "Давай я дам тебе денежку"
    $ items.extend([("coin", "Денюжка")])

label give:
    "Воспользуйся монетой в своем инвентаре, что бы пополнить баланс"
    jump give

label money:
    "молодец, на твоем счету появилось 100$"
    $ money += 100
    "отлично теперь вы научились использовать инвентарь"
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
    $t = 3
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
label alchemy:
    scene alkhimiya
    with fade
    al "Приветсвую вас, дорогой покупать!"
    al "Чем могу помочь?"
    menu:
        "Я хотел бы взглянуть на ваш товар":
            al "Да, конечно"
            jump alchemy1
        "Хотел кое-что продать":
            al "Да, конечно"
            jump alchemy2
        "Город":
            jump City
    return

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
                    else:
                        al "Эй, сначала деньги!"
                    jump alchemy1
                "Отказаться":
                    jump alchemy1
        "Ключ    20$":
            menu:
                "Купить":
                    if money >= 20:
                        $ items.extend([("key", "Ключ")])
                        $ money -= 20
                    else:
                        al "Эй, сначала деньги!"
                    jump alchemy1
                "Отказаться":
                    jump alchemy1
        "Вернуться обратно":
            jump alchemy3
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
        "Ключ    10$":
            menu:
                "Продать":
                    $ money += 10
                    jump alchemy2
                "Отказаться":
                    jump alchemy2
        "Вернуться обратно":
            jump alchemy3
    return
# алхимия выбор купить/продать
label alchemy3:
    scene alkhimiya
    with fade
    menu:
        "Я хотел бы взглянуть на ваш товар":
            al "Да, конечно"
            jump alchemy1
        "Хотел кое-что продать":
            al "Да, конечно"
            jump alchemy2
        "Город":
            jump City


#Пекарня
label food:
    scene pekarnya
    with fade
    menu:
        pek "Приветсвую вас, дорогой покупать!"
        "Купить":
            jump City
        "Город":
            jump City
    return
#Кузня
label smithy:
    scene kuznya
    with fade
    menu:
        k "Приветсвую вас, дорогой покупать!"
        "Купить":
            jump City
        "Город":
            jump City
    return
#локация город
label City:
    scene ploshchad
    with fade
    $ p1 = 0
    menu:
        e "Куда отправиться?"
        "Лавка":
            jump alchemy
        # "Провинзия":
        #     jump food
        # "Кузня":
        #     jump smithy
        "Выйти из города":
            jump map

    return
label map:
    scene map1
    with fade
    "Выходя из города, Вы решаетесь пойти.."
    menu:
        "Вернуться в город":
            jump City
        "Отправиться в путь":
            jump path


#локация петешествие

#копка лопатой
label digging:
    scene map1
    with fade
    "Выходя из города, Вы решаетесь пойти.."
    menu:
        "Вернуться в город":
            jump City
        "Отправиться в путь":
            jump path


label path:
    scene les1
    with fade
    "Вы слышите какие-то от попутчиков истории..."
    "некоторое время вы приезжаете к месту назначения"
    "Видите неподалеку подземелье"
    menu:
        e "Вот оно, как искатель приключений, это прибыльное дело"

        "Зайти внутрь":
            jump dungeon

        "Пойти порыбачить":
            jump path1

    return

label path1:
    scene les1
    with fade
    $ p1 = 1 #флаг, что мы находимся в локации path
    "Воспользуйтесь удочкой"
    menu:
        "Пойти порыбачить":
            jump path1
        "Отправиться в путь":
            $ p1 = 0
            jump map
    return

label StartMiniGame:
    $ FishUp = renpy.random.randint(30,50) #Отвечает за то откуда рыба начнет
    show screen Fish_Up
    call screen MiniGameFish
    if _return == "EndMiniGame":
        jump start


label dungeon:
    scene podzemelye
    with dissolve
    "Заходите все глубже и глубже вы замечаете стая волков."
    "Подходя еще ближе, вас замечают и начинается битва."
    "После долгой битвы вы одолеваете их. После ненадолгой передышки вы решаетесь отправиться дальше"
    menu:

        "подземелье 2 уроня":
            jump dungeon2
    return

label dungeon2:
    scene podzemelye with dissolve

    "Видите босса подземелье"
    " и пытаетесь сразиться с ним"
    "..."
    "Вы с чудом одолеваете босса и забираете сокривища"
    menu:
        "Оказалась славная битва"
        "Вернуть в город":
            jump City2
    return
label City2:
    scene ploshchad
    with fade
    "Вас встречаю народ и вас подздравляют с почетом"
    "И вас сам лично король дарует титул <из князя в грязи>"
    "Завершение новеллы"
    return
