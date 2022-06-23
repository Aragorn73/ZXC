screen quast1:
    zorder 111
    text "Журнал" align(.172, .16)
    frame:

        xalign 0.4
        background Solid("#0000")
        xmaximum 800
        ymaximum 1000
        xfill True
        vbox:
            imagebutton auto "inventory/book_%s.png" action SetVariable("book12", not book12)
            if book12:

                hbox:

                    #xmaximum 0.7

                    viewport id "box":
                        image "Quest/book.png"
                        #yinitial 9999
                        #xmaximum 0.1
                        mousewheel True
                        draggable True
