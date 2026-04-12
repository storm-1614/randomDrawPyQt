import sys
import random
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

name_list = ["A", "B", "C", "D"]

app = QApplication(sys.argv)

# 创建窗口
window = QWidget()
window.setWindowTitle("random draw app")
window.setGeometry(100, 100, 400, 300)

# 创建布局
layout = QVBoxLayout()

# 标签（显示结果）
label = QLabel("请抽签")

# 字体
font = QFont()
font.setPointSize(48)
font.setBold(True)
label.setFont(font)

# 设置居中对齐
label.setAlignment(Qt.AlignmentFlag.AlignCenter)

# 设置字体样式：CSS
label.setStyleSheet("""
QLabel {
    color: #0000FF
}
""")

layout.addWidget(label)

button = QPushButton("抽取")

button.setStyleSheet("""
    QPushButton {
        font-size: 20px;
        padding: 15px;
    }
""")


# 按钮点击事件
def button_clicked():
    select_name = random.choice(name_list)
    label.setText(select_name)

# 连接 clicked 信号到 button_clicked 函数
button.clicked.connect(button_clicked)

layout.addWidget(button)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
