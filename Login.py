from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('账号密码配置')
        self.resize(380, 200)

        self.account_label = QLabel('账号:', self)
        self.account_label.move(60, 20)
        self.account_input = QLineEdit(self)
        self.account_input.resize(200, 30)
        self.account_input.move(120, 20)

        self.password_label = QLabel('密码:', self)
        self.password_label.move(60, 60)
        self.password_input = QLineEdit(self)
        self.password_input.resize(200, 30)
        self.password_input.move(120, 60)
        self.password_input.setEchoMode(QLineEdit.Password)  # 隐藏密码输入

        self.confirm_button = QPushButton('确认', self)
        self.confirm_button.move(40, 120)
        self.confirm_button.clicked.connect(self.confirm)

        self.cancel_button = QPushButton('取消', self)
        self.cancel_button.move(260, 120)
        self.cancel_button.clicked.connect(self.cancel)

    def confirm(self):
        account = self.account_input.text()
        password = self.password_input.text()

        with open('account.txt', 'w') as f:
            f.write('email=' + account + '&key=' + password)
        self.close()

    def cancel(self):
        self.close()


def login():
    global window
    window = LoginWindow()
    window.show()
