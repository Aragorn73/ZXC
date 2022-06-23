############ Деньги ################


init python:
    # это денежки
    money = 0
    # текст сообщения после проверки кода
    message = ""
    # это переменная для вводимого в окошко текста
    temp = ""

    #$ left2 = Position(xalign=0.1, yalign=0.1) # монетка слева с верху

    # функция запоминает вводимый текст в переменной temp
    def inp(newstr):
        global temp
        temp = newstr
    # срабатывает при нажатии кнопки ОК
    def clickOK():
        global money, message, temp
        # если введенный код это «1234»,
        if temp == "1234":
            # то прибавим 100 к деньгам
            money += 100
            message = "Код правильный!"
        else:
            message = "Код неверный."
        temp = ""
        renpy.restart_interaction()
    ClickOK = renpy.curry(clickOK)
    # отключение надписи
    def messageOff():
        global message, temp
        message = ""
        temp = ""
        Hide("input_scr")()
    MessageOff = renpy.curry(messageOff)
# этот экран ждет нажатия кнопки табуляции
screen cheat:
    zorder 111
    key "K_F2" action Show("input_scr")
    # индикатор денюжек
    text "$" + str(money) align(.05, .15)
    frame:
        xalign 0.025
        background Solid("#0000")
        xmaximum 130
        ymaximum 450
        xfill True
        vbox:
            image "inventory/coin1.png"
# чтобы после нажатия показать этот экран ввода кода
screen input_scr:
    default temp = ""
    # отключаем ENTER, чтобы нажимались только кнопки на экране
    key "dismiss" action NullAction()
    modal True
    if message:
        # вывод сообщения
        text message align(.5, .5) outlines [(2, "#0008", 0, 0)] at msgAlpha()
        # убираем сообщение через 3 секунды
        timer 3.0 action MessageOff()
    else:
        frame:
            align(.5, .5)
            minimum(272, 72)
            vbox:
                xalign .5
                label "Введите код:" xalign .5
                add Input(default="", changed=inp, button=renpy.get_widget("input_scr", "")) xalign .5
                hbox:
                    xalign .5
                    # по нажатию ОК проверяем правильность кода и прибавляем денег
                    textbutton _("OK") action ClickOK()
                    textbutton _("Отмена") action Hide("input_scr")
init:
    # для красивого появления надписи
    transform msgAlpha(delay=3.0):
        alpha 0.0
        linear delay*.25 alpha 1.0
        pause delay*.5
        linear delay*.25 alpha 0.0
    #image bg = "look.com.ua-83738.jpg"
    #image neko = "neko.png"


screen map123:
    text "Карта" align(.87, .155)
    frame:

        xalign 0.90
        background Solid("#0000")
        xmaximum 130
        ymaximum 450
        xfill True
        imagemap:
            hover 'images/inventory/map_hover.png'
            idle 'images/inventory/map_idle.png'
            hotspot(0,0,100,100) action Jump("map")
