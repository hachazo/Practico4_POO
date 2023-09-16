import sys
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow,QLineEdit,QLabel,QHBoxLayout,QVBoxLayout,QPushButton

# clase usada para mostrar una ventana con el texto
class SecondWindow(QDialog):
    def __init__(self,text):
        super(SecondWindow,self).__init__()
    
        self.setWindowTitle("Resultado")
        self.setGeometry(100, 70, 220, 100)
        message_label = QLabel(text)
        
        layout = QVBoxLayout()
        layout.addWidget(message_label)
        self.setLayout(layout)
        
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        
        self.setWindowTitle("Ventana Principal")
        self.setGeometry(100, 70, 220, 100)
        
        message_label = QLabel("Ingrese el texto a mostar:")
        self.label = QLabel()
        self.input = QLineEdit()
        self.button_Accept = QPushButton("Guardar")
        self.button_Accept.clicked.connect(self.save_text)

        # Viseño vertical
        layout = QVBoxLayout()
        layout.addWidget(message_label)
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button_Accept)
        self.setLayout(layout)
        
    # Guardar el texto en una variable y llamar a otra ventana
    def save_text(self):
        self.text = self.input.text()
        self.window2 = SecondWindow(self.text)
        self.window2.show()
        self.close()
            
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
#print(window.text)