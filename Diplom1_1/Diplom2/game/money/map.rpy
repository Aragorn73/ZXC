############ Деньги ################
# screen map123:
#
#     text "Карта" align(.87, .15)
#     frame:
#
#         xalign 0.90
#         background Solid("#0000")
#         xmaximum 130
#         ymaximum 450
#         xfill True
#         imagemap:
#             hover 'images/inventory/map_hover.png'
#             idle 'images/inventory/map_idle.png'
#             hotspot(0,0,100,100) action Jump("map")
