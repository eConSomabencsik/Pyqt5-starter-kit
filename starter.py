import sys
import json
from typing import List

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from window import factory, loader

class MainWindow(QWidget):
    def __init__(self, elements: List[QWidget]) -> None:
        super().__init__()
        self.elements = elements
        
        self.setup_ui()

    def setup_ui(self) -> None:
        layout = QVBoxLayout()

        for element in self.elements:
            layout.addWidget(element)

        self.setLayout(layout)

def main():
    """Create the GUI elements and pass them to MainWindow"""
    app = QApplication(sys.argv)

    with open("./elements.json", "r", encoding="UTF-8") as file:
        data = json.load(file)

        loader.load_plugins(data["elements"])

        gui_elements = [factory.create(item) for item in data["guis"]]

    mainWindow = MainWindow(gui_elements)
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
