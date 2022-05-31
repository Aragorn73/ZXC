init -2 python:
    items = []
    last_item = None
    def SelectItemF(index):
        if (index >= 0) and (index < len(items)):
            last_item = items.pop(index)
            renpy.restart_interaction()
            if last_item[0] == "coin":
                renpy.jump("money")
            if last_item[0] == "flower":
                renpy.jump("flower")
            if last_item[0] == "star":
                renpy.jump("powers")
            if last_item[0] == "key":
                renpy.jump("keys")
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
