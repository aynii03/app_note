from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QTextEdit, QPushButton, QFileDialog, QMessageBox, QVBoxLayout)
import os

class Appnote (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 200, 500, 400)
        self.setWindowTitle('ayapp easy note')

        self.text_edit = QTextEdit(self)
        self.text_edit.setFontPointSize(18)
        
        button_save = QPushButton('simpan', self)
        button_del = QPushButton('hapus', self)
        button_open = QPushButton('buka file', self)
        button_save.clicked.connect (self.simpan)
        button_del.clicked.connect (self.hapus)
        button_open.clicked.connect (self.buka)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(button_save)
        layout.addWidget(button_del)
        layout.addWidget(button_open)
        
        kontainer = QWidget()
        kontainer.setLayout(layout)
        self.setCentralWidget(kontainer)

    def simpan(self):
        note = self.text_edit.toPlainText()
        if note:
            file_path, _ = QFileDialog.getSaveFileName(self, 'simpan catatan', filter='Text Files (*.txt);;All Files (*)')
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(note)
                self.statusBar().showMessage(f'simpan catatan di: {file_path}')  
        else:
            QMessageBox.warning(self, 'Catatan kosong', 'Tidak dapat menyimpan catatan kosong.')
    
    def hapus(self):
        self.text_edit.clear()
        self.statusBar().clearMessage()

    def buka (self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'mengambil catatan', filter='Text Files (*.txt);;All Files (*)')
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    note = file.read()
                    self.text_edit.setPlainText(note)
                self.statusBar().showMessage(f'mengambil catatan dari: {file_path}') 
            except FileNotFoundError:
                 QMessageBox.warning(self, 'File tidak ada', 'File yang dipilih tidak ada.')


app = QApplication([])
appnote = Appnote()   
appnote.show()
app.exec_()       

        

