import sys
import random
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)


class RandomDrawApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("random draw app")
        self.setGeometry(100, 100, 400, 300)
        self.names = self.load_names("./list/list")
        # 初始化布局
        self.base_layout = QVBoxLayout()
        # 标签（显示结果）
        self.result_label = QLabel("请抽签")
        # 按钮， 开始随机
        self.random_button = QPushButton("抽取")

    def load_names(self, path: str) -> list:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return lines

    def init_UI(self):
        # 标签样式
        label_font = QFont()
        label_font.setPointSize(48)
        label_font.setBold(True)
        self.result_label.setFont(label_font)

        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.result_label.setStyleSheet("""
        QLabel {
            color: #0000FF
        }
        """)  # CSS 美化

        self.base_layout.addWidget(self.result_label)

        self.random_button.setStyleSheet("""
            QPushButton {
                font-size = 20px;
                padding: 15px;
            }
        """)

        self.random_button.clicked.connect(self.button_clicked)
        self.base_layout.addWidget(self.random_button)
        self.setLayout(self.base_layout)

    def draw(self):
        self.show()

    def button_clicked(self):
        select_name = random.choice(self.names)
        self.result_label.setText(select_name)


random_draw = RandomDrawApp()
random_draw.init_UI()
random_draw.draw()
sys.exit(app.exec_())
