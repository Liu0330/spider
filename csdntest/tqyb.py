from PyQt5.QtWidgets import QApplication, QMainWindow
from WeatherWin import Ui_Form
import sys
from PyQt5.QtCore import *
import requests
import time
from bs4 import BeautifulSoup


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def queryWeather(self):
        global cityCode
        cityName = self.ui.weatherComboBox.currentText()
        cityCode = self.transCityName(cityName)
        self.thread = WorkThread()
        self.thread.trigger.connect(self.writeText)
        self.thread.start()

    def writeText(self, text):
        self.ui.resultText.setText(text)

    def transCityName(self, cityName):
        cityCode = ''
        if cityName == '北京':
            cityCode = '101010100'
        elif cityName == '石家庄':
            cityCode = '101090101'
        elif cityName == '上海':
            cityCode = '101020100'
        elif cityName == '天津':
            cityCode = '101030100'
        elif cityName == '长沙':
            cityCode = '101250101'
        elif cityName == '乌鲁木齐':
            cityCode = '101130101'
        elif cityName == '重庆':
            cityCode = '101040100'
        elif cityName == '郑州':
            cityCode = '101180101'
        return cityCode

    def clearResult(self):
        self.ui.resultText.clear()


class WorkThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self):
        super(WorkThread, self).__init__()

    def run(self):
        global cityCode
        times = str(time.time()).split('.')
        times = ''.join(times[0] + times[1][0:3])
        headers = {
            "Connection": 'keep-alive',
            'Host': 'd1.weather.com.cn',
            'Referer': 'http://www.weather.com.cn/weather1d/%s.shtml' % cityCode,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        url = 'http://d1.weather.com.cn/sk_2d/%s.html?_=%s' % (cityCode, times)
        rep = requests.get(url, headers=headers)
        rep = rep.content
        page = BeautifulSoup(rep, 'lxml')
        page = page.text.split('=')
        page = eval(page[1])
        oxgan = ['优', '良', '轻度污染', '中度污染', '重度污染', '极度污染']
        live = int(page['aqi'])
        if 0 <= live <= 50:
            oxgan = oxgan[0]
        elif 50 < live <= 100:
            oxgan = oxgan[1]
        elif 100 < live <= 150:
            oxgan = oxgan[2]
        elif 150 < live <= 200:
            oxgan = oxgan[3]
        elif 200 < live <= 300:
            oxgan = oxgan[3]
        elif 300 < live <= 500:
            oxgan = oxgan[3]
        msg1 = '城市： %s\n' % page['cityname']
        msg2 = '温度： %s' % page['temp'] + '℃\n'
        msg3 = '风向： %s\n' % page['WD']
        msg4 = '风力： %s\n' % page['WS']
        msg5 = '湿度： %s\n' % page['SD']
        msg6 = '空气质量： %s ' % page['aqi'] + oxgan + '\n'
        msg7 = '时间： %s %s\n' % (page['date'], page['time'])
        msg8 = '\n\n\n\n\t by:DaddyHu_CN'
        result = msg1 + msg2 + msg3 + msg4 + msg5 + msg6 + msg7 + msg8
        self.trigger.emit(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
sys.exit(app.exec_())