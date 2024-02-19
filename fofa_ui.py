import sys
from Login import LoginWindow
import httpx
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QTextEdit
import base64


def base64_encode():
    strings = box_input.toPlainText()
    encoded_bytes = base64.b64encode(strings.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text


def search():
    try:
        account = open('account.txt', 'r').readline()
    except:
        global login
        login = LoginWindow()
        login.show()
        return
    keyword = base64_encode()
    fields = 'ip,port,title,domain'
    url = 'https://fofa.info/api/v1/search/all?'
    request_url = url + 'fields=' + fields + '&qbase64=' + keyword + '&' + account + '&size=1000&full=true&'
    try:
        response = httpx.get(request_url).json()
    except Exception as e:
        try:
            response = httpx.get(request_url).json()
        except:
            box_output.setText('查询失败或结果为空，请检查关键词后重试！')
    m = ''
    try:
        for i in response['results']:
            m = m + i[0] + ':' + i[1] + '\t' + i[2] + '\t' + i[3] + '\n'
            with open('result.txt', 'a+') as f:
                f.write(m)
    except Exception as e:
        box_output.setText('查询失败或结果为空，请检查关键词！')
    box_output.setText(m)


app = QApplication(sys.argv)
widget = QWidget()
layout = QGridLayout(widget)
widget.resize(800, widget.height())
widget.setWindowTitle('FoFa Search- Author: Al17er')
box_input = QTextEdit()
layout.addWidget(box_input, 0, 0)
layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
box_input.setMaximumHeight(32)
button_search = QPushButton('搜索')
button_search.setMaximumSize(200, 32)
layout.addWidget(button_search, 0, 1)
box_output = QTextEdit()
layout.addWidget(box_output, 1, 0, 1, 2)
button_search.clicked.connect(search)
widget.show()
app.exec()
