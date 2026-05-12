from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class HistoryArea(QFrame):
    def __init__(self):
        super().__init__()
        
        # 기록 구역 기본 스타일 및 크기 설정
        self.setStyleSheet("background-color: #4A4A4A;")
        self.setFixedWidth(250) # 너비 고정
        
        # 레이아웃 생성
        layout = QVBoxLayout(self)
        
        # 제목 라벨
        title_label = QLabel("과거 질문 내역")
        title_label.setStyleSheet("color: white; font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(title_label)
        
        # 아래쪽을 밀어주는 빈 공간 (위에서부터 쌓임)
        layout.addStretch()