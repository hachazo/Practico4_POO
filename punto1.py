from PyQt5.QtWidgets import QApplication,QPushButton,QHBoxLayout,QDialog,QLabel,QVBoxLayout
import sys

class SimpleDialog(QDialog):
    
    def __init__(self):
        super(SimpleDialog, self).__init__()
        self.setGeometry(20, 20, 100, 100)
        self.setWindowTitle("Programa 1.0")
        message_label = QLabel("¿Está seguro que quieredar de baja al usuario?")
        

        button_accept = QPushButton("Aceptar")
        button_Cancel = QPushButton("cancelar")
        
        # Diseño horizontal para los botones
        button_Horizontal = QHBoxLayout()
        button_Horizontal.addWidget(button_accept)
        button_Horizontal.addWidget(button_Cancel)
        
        # diseño vertical para mostrar el mensaje y abajo los botones
        layout = QVBoxLayout()
        
        layout.addWidget(message_label)
        layout.addLayout(button_Horizontal)
        self.setLayout(layout)

app = QApplication(sys.argv)

window = SimpleDialog()
window.show()
app.exec()
