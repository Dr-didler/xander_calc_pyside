"""
basic_app.py
by Xander for futher use later
A demo of the most basic input/output: labels, text inputs, and buttons.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic App")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Basic App: a simple greeting app.")

        # TODO: add a text input for user's name
        self.name_input = QLineEdit(placeholderText="llamo a mi amigo...")
        # TODO: add a push button to greet user
        submit_button = QPushButton("greet me!")
        submit_button.clicked.connect(self.get_input)
        # TODO: add a label to greet user
        self.instructions = "Enter your name and click the button to be greeted!"
        self.output_label = QLabel(self.instructions)
        
        """
        Challenges:
            * Add another text input (last name, home town, etc.)
            * Add a clear button that, when clicked will
                - clear the text in the name input
                - reset the output text to its initial value
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.name_input)
        layout.addWidget(submit_button)
        layout.addWidget(self.output_label)
        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)
    
    def get_input(self):
        output = "Hello, "
        name = self.name_input.text()
        if not name:
            output = "friend" + "Give a real name next time, you didn't this time!" 
            output += "your name is empty!"
        else:
            output = f"you entered: {name} as your name." 
        self.output_label.setText(output + name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()