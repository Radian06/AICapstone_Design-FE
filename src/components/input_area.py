from PyQt6.QtWidgets import QWidget, QHBoxLayout, QTextEdit, QPushButton
from PyQt6.QtCore import Qt

class InputArea(QWidget):
    def __init__(self):
        super().__init__()
        
        # 가로 레이아웃 생성
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20) # padding 설정
        layout.setSpacing(10) # gap 설정
        
        # 인풋 박스
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("여기에 질문을 입력하세요...") # placeholder
        self.text_input.setFixedHeight(60) # 높이 고정
        self.text_input.setStyleSheet("""
            background-color: white;
            border: 1px solid #CCCCCC;
            border-radius: 5px;
            padding: 10px;
            font-size: 14px;
        """)
        
        # 전송 버튼
        self.send_button = QPushButton("전송")
        self.send_button.setFixedSize(80, 60)
        self.send_button.setStyleSheet("""
            background-color: #4A4A4A;
            color: white;
            border-radius: 5px;
            font-weight: bold;
            font-size: 14px;
        """)
        
        # 조합
        layout.addWidget(self.text_input)
        layout.addWidget(self.send_button)
        
        self.setLayout(layout)