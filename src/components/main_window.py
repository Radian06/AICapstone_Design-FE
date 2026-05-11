from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QFrame, QLabel
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("AI 캡스톤 디자인 - 민사 소송 AI 상담")
        self.setMinimumSize(QSize(1080, 720))
        
        # 가장 밑바탕 레이아웃 flex-row
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0) # margin 제거
        main_layout.setSpacing(0) # gap 제거
        
        # 왼쪽 사이드바 (과거 기록)
        sidebar = QFrame()
        sidebar.setStyleSheet("background-color: #4A4A4A;")
        sidebar.setFixedWidth(250) # 너비 고정
        
        sidebar_layout = QVBoxLayout()
        sidebar_label = QLabel("과거 질문 내역")
        sidebar_label.setStyleSheet("color: white; font-weight: bold;")
        sidebar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sidebar_layout.addWidget(sidebar_label)
        sidebar.setLayout(sidebar_layout)

        # 오른쪽 전체 영역
        right_widget = QWidget()
        right_layout = QVBoxLayout() # flex-col
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        # 대화창 영역
        chat_area = QFrame()
        chat_area.setStyleSheet("background-color: #F4F4F4;") # 밝은 회색 바탕
        
        chat_layout = QVBoxLayout()
        chat_label = QLabel("사용자 / 챗봇 대화가 표시되는 구역")
        chat_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        chat_layout.addWidget(chat_label)
        chat_area.setLayout(chat_layout)

        # 입력창 영역
        input_area = QFrame()
        input_area.setStyleSheet("background-color: #e4f532;")
        input_area.setFixedHeight(160) # 높이 고정
        
        input_layout = QHBoxLayout()
        input_label = QLabel("사용자 질문 입력 칸 및 전송 버튼 구역")
        input_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_layout.addWidget(input_label)
        input_area.setLayout(input_layout)

        # 조립
        # 오른쪽 영역
        right_layout.addWidget(chat_area)
        right_layout.addWidget(input_area)
        right_widget.setLayout(right_layout)

        # 메인 영역
        main_layout.addWidget(sidebar)
        main_layout.addWidget(right_widget)
        
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)