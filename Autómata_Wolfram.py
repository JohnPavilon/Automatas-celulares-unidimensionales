# importing various libraries
from GUI import *
from Cellular import *
from View import *

rule_number = 0
pos = 'impulse'
cond = 'center'
size = 600
steps = 400

"Clase ventana principla"
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        "Agrega un icono"
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
        
        "Conectamos los eventos con sus acciones"
        
        "Seleccional la función single"
        self.button_single.clicked.connect(self.single)
        
        "Seleccional la función random"
        self.random_button.clicked.connect(self.random)
        
        "Ejecuta Cellular"
        self.Ejecute_button.clicked.connect(self.ejecute)
        
        "Obtiene el número de la regla"
        self.rule_spinBox.valueChanged.connect(self.rule)
        
        "Obtiene el número de generaciones (ancho)"
        self.height_spinBox.valueChanged.connect(self.height)
        
        "Obtiene el número de casillas (largo)"
        self.large_spinBox.valueChanged.connect(self.height)
        
        "Obtiene la posición inicial (center, left, right)"
        self.horizontalSlider.valueChanged.connect(self.pose)
        
        "Devuelve el valor dado en el slider de posición"
    def pose(self):
        global cond
        comp = self.horizontalSlider.value()
        cond = self.point(comp)
    
        "Diccionario que devuelve una cadena para un entero dado"
    def point(self, comp):
        switcher = {
            0: 'left',
            1: 'center',
            2: 'right',
            }
        return switcher.get(comp, 'center')
        
        "Devuelve el valor impulse para pos"
    def single(self):
        global pos
        pos = 'impulse'
        
        "Devuelve el valor random para pos"
    def random(self):
        global pos
        pos = 'random'
    
        "Regresa el valor seleccionado en la spinBox (rule)"
    def rule(self):
        global rule_number
        rule_number = self.rule_spinBox.value()
        
        "Obtiene el número de casillas iniciales"
    def height(self):
        global size
        size = self.height_spinBox.value()
        
        "Obtiene el número de generaciones"
    def large(self):
        global steps
        steps = self.large_spinBox.value()

        "Procesa el aútomata y devuelve una imagen"
    def ejecute(self):
        print_image(rule_number, size, steps, pos, cond)
        
"Ejecuta la ventana"
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()