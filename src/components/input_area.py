from PyQt6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton, QLabel, QProgressBar, QGraphicsOpacityEffect
from PyQt6.QtCore import Qt, pyqtSignal

class InputArea(QFrame): 
    # 메시지가 전송 신호
    clicked_send = pyqtSignal(str) 

    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("background-color: #ede5d3;")
        self.setFixedHeight(160)

        # 전체 수직 레이아웃
        main_vbox = QVBoxLayout()
        main_vbox.setContentsMargins(20, 10, 20, 20)
        main_vbox.setSpacing(5)

        # 상태 메시지
        self.loading_container = QFrame()
        loading_layout = QHBoxLayout(self.loading_container)
        loading_layout.setContentsMargins(0, 0, 0, 0)

        self.loading_label = QLabel("AI가 답변을 생성 중입니다...")
        self.loading_label.setStyleSheet("color: #4A4A4A; font-size: 12px; font-weight: bold;")
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(10)
        self.progress_bar.setRange(0, 0) 
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar { border: 1px solid #CCCCCC; border-radius: 5px; background-color: white; }
            QProgressBar::chunk { background-color: #4A4A4A; }
        """)

        loading_layout.addWidget(self.loading_label)
        loading_layout.addWidget(self.progress_bar)
        
        # 투명도 설정
        self.opacity_effect = QGraphicsOpacityEffect(self.loading_container)
        self.loading_container.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0.0) # 처음에는 투명하게

        # 가로 레이아웃 생성
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10) 
        
        # 인풋 박스
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("여기에 질문을 입력하세요")
        self.text_input.setFixedHeight(60)
        self.text_input.setStyleSheet("background-color: white; border: 1px solid #CCCCCC; border-radius: 5px; padding: 10px; font-size: 14px;")
        
        # 전송 버튼
        self.send_button = QPushButton("전송")
        self.send_button.setFixedSize(80, 60)
        self.send_button.setStyleSheet("background-color: #4A4A4A; color: white; border-radius: 5px; font-weight: bold; font-size: 14px;")
        
        # 버튼 클릭 시 내부 함수 연결
        self.send_button.clicked.connect(self.on_click_send)
        
        layout.addWidget(self.text_input)
        layout.addWidget(self.send_button)

        main_vbox.addWidget(self.loading_container)
        main_vbox.addLayout(layout)
        self.setLayout(main_vbox)

    # 버튼 누르면 텍스트 외부로 전달하는 로직
    def on_click_send(self):
        text = self.text_input.toPlainText().strip()
        if text:
            self.clicked_send.emit(text) # 신호 전송

    # 투명도 변경 로직
    def set_loading(self, is_loading):
        if is_loading:
            self.opacity_effect.setOpacity(1.0) # 불투명
            self.send_button.setEnabled(False)
            self.text_input.setEnabled(False)
        else:
            self.opacity_effect.setOpacity(0.0) # 투명
            self.send_button.setEnabled(True)
            self.text_input.setEnabled(True)
            self.text_input.clear()