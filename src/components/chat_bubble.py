from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel, QSizePolicy
from PyQt6.QtCore import Qt

class ChatBubble(QFrame):
    def __init__(self, text, is_user=True):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 10, 20, 10) 
        layout.setSpacing(0)
        
        self.label = QLabel(text)
        self.label.setWordWrap(True) # 긴 문장 자동 줄바꿈
        
        self.label.setStyleSheet("background: transparent; border: none; padding: 0px;")

        self.setMaximumWidth(400)
        self.setMinimumHeight(60)
        
        self.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)

        # 타입에 따른 스타일 설정
        if is_user:
            # 사용자
            self.setStyleSheet("background-color: #DCF8C6; border-radius: 10px; padding: 5px;")
            layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignRight)
        else:
            # 챗봇
            self.setStyleSheet("background-color: #FFFFFF; border-radius: 10px; padding: 5px;")
            layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignLeft)
            
        self.setLayout(layout)