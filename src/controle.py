
def diminui_objeto():
    print('objeto e diminuir')

def amplia_objeto():
    print('objeto e ampliar')

def diminui_viewport():
    print('viewport e diminuir')

def amplia_viewport():
    print('viewport e ampliar')

def controle(ui):
    if ui.radioButton_objetos.isChecked():
        ui.button_diminuir.clicked.connect(diminui_objeto)
        ui.button_ampliar.clicked.connect(amplia_objeto)
    elif ui.radioButton_viewport.isChecked():
        ui.button_diminuir.clicked.connect(diminui_viewport)
        ui.button_ampliar.clicked.connect(amplia_viewport)