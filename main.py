import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

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
    color: #FF0000
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

layout.addWidget(button)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
