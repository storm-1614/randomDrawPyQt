import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

app = QApplication(sys.argv)

# 创建窗口
window = QWidget()
window.setWindowTitle("random draw app")

layout = QVBoxLayout()

label = QLabel("请抽签")
layout.addWidget(label)

button = QPushButton("抽取")
layout.addWidget(button)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
