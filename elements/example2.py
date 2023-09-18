from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from window import factory

class Example(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        title = QLabel("Example Widget2!")
        button = QPushButton("Dare to click2?")
        button.clicked.connect(lambda: title.setText("Nothing."))

        layout.addWidget(title)
        layout.addWidget(button)

        self.setLayout(layout)

def register():
    factory.register("example2", Example)