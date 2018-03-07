from PyQt4.QtGui import *

class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

    # 레이블,Edit,버튼 컨트롤 
        lblName = QLabel("Name")
        self.editName = QLineEdit()
        btnOK = QPushButton("OK")

        # 레이아웃
        layout = QVBoxLayout()
        layout.addWidget(lblName)
        layout.addWidget(self.editName)
        layout.addWidget(btnOK)

         # 다이얼로그에 레이아웃 지정
        self.setLayout(layout)

        btnOK.clicked.connect(self.btnOkClicked)

    def btnOkClicked(self):
        name = self.editName.text()
        QMessageBox.information(self, "You entered", name)

# App
app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()