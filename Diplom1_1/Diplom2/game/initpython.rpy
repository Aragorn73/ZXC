init -2 python:
    items = []
    last_item = None
    def SelectItemF(index):
        if (index >= 0) and (index < len(items)):
            last_item = items.pop(index)
            renpy.restart_interaction()
            if last_item[0] == "coin":
                renpy.jump("money")
            if last_item[0] == "rod":
                items.extend([("rod", "Удочка")])
                if p1 == 1:
                    renpy.jump("StartMiniGame")
            if last_item[0] == "key":
                if p3 ==0:
                    items.extend([("key", "Ключ")])
                if p3 == 1:
                    renpy.jump("digging5")
            if last_item[0] == "map_idle":
                renpy.jump("map")
            if last_item[0] == "shovel":
                items.extend([("shovel", "Лопата")])
                if p2 ==1:
                    renpy.jump("digging2")
            #рыбы
            if last_item[0] == "fish1":
                renpy.jump("YouWin")
            if last_item[0] == "fish2":
                renpy.jump("YouWin")
            #цветок
            if last_item[0] == "flower":
                if cv ==0:
                    items.extend([("flower", "Цветок")])
                if cv == 1:
                    renpy.jump("qwest_coplete")



    SelectItem = renpy.curry(SelectItemF)
    def GetFN(index=0):
        global items
        if (index >= 0) and (index < len(items)):
            fn, hn = items[index]
            return "inventory/" + fn + ".png"
        else:
            return ""
    def GetHint(index=0):
        global items
        if (index >= 0) and (index < len(items)):
            fn, hn = items[index]
            return hn
        else:
            return ""
