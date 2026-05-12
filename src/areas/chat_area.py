from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from components.chat_bubble import ChatBubble

class ChatArea(QWidget):
    def __init__(self):
        super().__init__()
        # 레이아웃 설정
        self.chat_layout = QVBoxLayout(self)
        self.chat_layout.setContentsMargins(40, 60, 40, 20) 
        
        # 테스트용 메시지 바로 추가 
        self.add_message("챗봇 테스트 메시지입니다.", is_user=False)
        self.add_message("사용자 테스트 메시지입니다. 테스트 테스트 테스트 테스트 테스트 테스트 테스트 테스트 테스트 테스트 테스트", is_user=True)
        
        # 위로 붙게 만들기 위해 빈 공간 추가
        self.chat_layout.addStretch()

    def add_message(self, text, is_user):
        bubble = ChatBubble(text, is_user)
        
        # 정렬 방향 결정
        align = Qt.AlignmentFlag.AlignRight if is_user else Qt.AlignmentFlag.AlignLeft
        
        # 빈 공간이 항상 맨 밑에 있도록 위쪽에 삽입
        # 세 번째 인자로 alignment 전달하여 너비 팽창 방지
        self.chat_layout.insertWidget(self.chat_layout.count() - 1, bubble, alignment=align)