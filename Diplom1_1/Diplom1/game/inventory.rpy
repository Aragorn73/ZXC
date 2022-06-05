screen inventory:
    zorder 111
    default tt = Tooltip(" ")
    frame:
        xalign 1.0
        background Solid("#0000")
        xmaximum 130
        ymaximum 450
        xfill True
        vbox:
            imagebutton auto "inventory/bag_%s.png" action SetVariable("invent", not invent)
            if invent:
                text tt.value
                hbox:
                    viewport id "box":
                        yinitial 9999
                        xmaximum 0.9
                        mousewheel True
                        draggable True
                        vbox:
                            for i in range(0, len(items)):
                                imagebutton:
                                    idle Image(GetFN(i))
                                    hover Image(GetFN(i))
                                    hovered tt.Action(GetHint(i))
                                    action SelectItem(i)
