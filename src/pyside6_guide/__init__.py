"""
By Alexander Scott
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget, QPushButton , QLineEdit
)
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My calculator")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(1000, 850)
        
        layout = QVBoxLayout()
        title_label = QLabel("this is the label")

        #buttons for calc
        
        name_input = QLineEdit(placeholdertext = "name")

        submit_button = QPushButton("numbers")

        
        
        instructions = "do something"
        output_label = QLabel()


        #layout
        layout.addWidget(title_label)
        layout.addWidget(name_input)
        layout.addWidget(submit_button)
        layout.addWidget(output_label)

        def get_input(self):
            output = ""
            name = self.name_input.text()

            if not name:
                output = "retry, enter"
            self.output_label.setText(output)

        """
        if button clicked pring number for operation..., like the number then clicking math operations will print them aswell
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()