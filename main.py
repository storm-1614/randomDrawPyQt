#! env /bin/python

import sys
import random
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
)
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

# 命令行参数
if len(sys.argv) > 1:
    name_file = sys.argv[1]
else:
    name_file = "./list/test"


class RandomDrawApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("random draw app")
        self.setGeometry(100, 100, 400, 300)
        self.names = self.load_names(name_file)
        # 初始化布局
        self.base_layout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        # 标签（显示结果）
        self.result_label = QLabel("请抽签")
        # 按钮， 开始随机
        self.random_button = QPushButton("抽取")
        # 选择文件
        self.choose_file_button = QPushButton("选取文件")

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

        self.random_button.clicked.connect(self.button_clicked)  # 绑定点击事件

        self.choose_file_button.setStyleSheet("""
            QPushButton {
                font-size = 20px;
                padding: 15px;
            }
        """)

        self.choose_file_button.clicked.connect(self.open_file)

        self.button_layout.addWidget(self.choose_file_button)
        self.button_layout.addWidget(self.random_button)
        self.base_layout.addLayout(self.button_layout)
        self.setLayout(self.base_layout)

    # 绘制
    def draw(self):
        self.show()

    # 按钮点击事件
    def button_clicked(self):
        if self.names:
            select_name = random.choice(self.names)
            self.result_label.setText(select_name)
            self.names.remove(select_name)
        else:
            print("列表为空，程序退出")
            exit()

    def open_file(self):
        """
        选择名单文件
        """
        file = QFileDialog()

        files, _ = file.getOpenFileNames(self, "打开文件", ".", "")
        self.names = self.load_names(files[0])
        self.result_label.setText("请抽签")


random_draw = RandomDrawApp()
random_draw.init_UI()
random_draw.draw()
sys.exit(app.exec_())
