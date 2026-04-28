#! env /bin/python

import sys
import random
import pandas
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QMessageBox,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
)
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)

# 命令行参数
if len(sys.argv) > 1:
    name_file = sys.argv[1]
else:
    name_file = ""


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

    def load_names(self, path="") -> list:
        # with open(path, "r", encoding="utf-8") as f:
        #     lines = f.readlines()
        if path == "":
            path = self.open_file()

        et_data = pandas.read_excel(
            path,
            header=None,
            names=["name", "number"],  # pyright: ignore[reportArgumentType]
            skiprows=1,
        )
        et_data = et_data.dropna(subset=["name"])  # 去除 nan 数据
        lines = et_data["name"].astype(str).tolist()

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
            color: #88c0d0
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

        self.choose_file_button.clicked.connect(self.choose_file_button_clicked)

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
            # print("列表为空，程序退出")
            QMessageBox.warning(
                self,
                "列表为空, 程序退出",
                "列表为空, 程序退出",
                QMessageBox.StandardButton.Ok,
            )
            exit()

    def open_file(self):
        """
        选择名单文件
        """
        file = QFileDialog()

        files, _ = file.getOpenFileNames(self, "打开文件", ".", "*.xlsx")
        while len(files) == 0:
            none_file_messageBox = QMessageBox.warning(
                self,
                "没有选择文件，请重新选择",
                "没有选择文件，请重新选择",
                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close,
            )
            if none_file_messageBox == QMessageBox.StandardButton.Ok:
                files, _ = file.getOpenFileNames(self, "打开文件", ".", "*.xlsx")
            elif none_file_messageBox == QMessageBox.StandardButton.Close:
                exit(1)

        return files[0]

    def choose_file_button_clicked(self):
        self.load_names(self.open_file())


random_draw = RandomDrawApp()
random_draw.init_UI()
random_draw.draw()
sys.exit(app.exec())
