from PyQt5.QtWidgets import *
import sys


class testApp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Test dialog app')
        layout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Name:',QLineEdit())
        formLayout.addRow('Age:',QLineEdit())
        formLayout.addRow('Job:',QLineEdit())
        formLayout.addRow('Hobbies:',QLineEdit())
        layout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok
        )

        btn = QPushButton('Click',self)
        btn.setGeometry(200,200,200,200)
        btn.clicked.connect(self.clickMe)
        layout.addWidget(btns)
        self.setLayout(layout)

    def clickMe(self):

        print('Clicked')


# if __name__ == 'main':
app = QApplication(sys.argv)
dlg = testApp()
dlg.show()
sys.exit(app.exec_())