import sys, json, pyperclip, textwrap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtGui import QIcon
import urllib.request
from Coder import *


class Text_Coder_Window1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('coder.ui', self)
        self.setWindowIcon(QIcon('RM_icon.jpg'))
        self.encode = 'Не выбрано'
        self.info_text = ''  # информация по выбранному шифрованию
        self.final_text = 'None'  # скопированный текст
        with open('import_info.json', 'r', encoding='utf-8') as f_obj:
            self.key_dict = json.load(f_obj)['info']  # считываем инфу по шифровкам и ключи
        self.pushButton.clicked.connect(self.Dialog_run)
        self.pushButton_2.clicked.connect(self.crypt_run)
        self.pushButton_3.clicked.connect(self.decrypt_run)
        self.pushButton_4.clicked.connect(self.copy_crypt)

    def Dialog_run(self):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "Выбор кодировки",
            "Выберите кодировку?",
            ("Шифр Цезаря", "Шифр Виженера", "Азбука Морзе", "Шифр замены", "Омофонический шифр",
             "Шифрование Гронсвельда", "Псевдосимвольное шифрование", "Бинарный код"),
            1,
            False
        )
        if okBtnPressed:
            self.encode = i
            self.label_2.setText(i)  # вставляем название кодировке
            if self.encode == "Не выбрано":
                self.label_8.setText("Кодировка не выбрана")  # вставляем инфу о шифре
            elif self.encode == 'Шифр Цезаря':
                print(1)
                self.info_text = '\n'.join(textwrap.wrap(self.key_dict['Шифр Цезаря'], 26))
                self.label_8.setText(self.info_text)
            elif self.encode == 'Шифр Виженера':
                self.info_text = '\n'.join(textwrap.wrap(self.key_dict['Шифр Виженера'], 26))
                self.label_8.setText(self.info_text)
            elif self.encode == 'Азбука Морзе':
                self.info_text = '\n'.join(textwrap.wrap(self.key_dict['Азбука Морзе'], 26))
                self.label_8.setText(self.info_text)
            elif self.encode == 'Шифр замены':
                self.info_text = '\n'.join(textwrap.wrap(self.key_dict['Шифр замены'], 26))
                self.label_8.setText(self.info_text)
            elif self.encode == "Омофонический шифр":
                self.info_text = '\n'.join(textwrap.wrap(self.key_dict["Омофонический шифр"], 26))
                self.label_8.setText(self.info_text)
            elif self.encode == "Бинарный код":
                self.info_text = '\n'.join(textwrap.wrap(self.key_dict["Бинарный код"], 26))
                self.label_8.setText(self.info_text)
            elif self.encode == "Шифрование Гронсвельда":
                self.info_text = '\n'.join(textwrap.wrap(self.key_dict["Шифрование Гронсвельда"], 26))
                self.label_8.setText(self.info_text)
            elif self.encode == "Псевдосимвольное шифрование":
                self.info_text = '\n'.join(textwrap.wrap(self.key_dict["Псевдосимвольное шифрование"], 26))
                self.label_8.setText(self.info_text)

    def crypt_run(self):
        try:
            if self.encode == "Не выбрано":
                pass
            elif self.encode == "Шифр Цезаря":
                self.final_text = Crypt_Caesar(self.textEdit.toPlainText(), int(self.lineEdit.text()))
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Шифр Виженера":
                self.final_text = Crypt_Vigenere(self.textEdit.toPlainText(), self.lineEdit.text())
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Азбука Морзе":
                self.final_text = Crypt_Morze(self.textEdit.toPlainText())
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Шифр замены":
                self.final_text = Crypt_replace(self.textEdit.toPlainText())
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Омофонический шифр":
                self.final_text = Crypt_omofon(self.textEdit.toPlainText())
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Шифрование Гронсвельда":
                self.final_text = Crypt_Gronsfeld(self.textEdit.toPlainText(), self.lineEdit.text())
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Псевдосимвольное шифрование":
                self.final_text = Crypt_pseudosim(self.textEdit.toPlainText())
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Бинарный код":
                self.final_text = Crypt_Binary_code(self.textEdit.toPlainText())
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
        except Exception:
            self.label_6.setText('Что-то не так... Проверьте правильность введённых данных')

    def decrypt_run(self):
        try:
            if self.encode == "Не выбрано":
                pass
            elif self.encode == "Шифр Цезаря":
                self.final_text = Decrypt_Caesar(self.textEdit.toPlainText(), int(self.lineEdit.text()))
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Шифр Виженера":
                self.final_text = Decrypt_Vegenere(self.textEdit.toPlainText(), self.lineEdit.text())
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Азбука Морзе":
                self.final_text = Decrypt_Morze(self.textEdit.toPlainText())
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Шифр замены":
                self.final_text = Decrypt_replace(self.textEdit.toPlainText())
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Омофонический шифр":
                self.final_text = Decrypt_omofon(self.textEdit.toPlainText())
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Шифрование Гронсвельда":
                self.final_text = Decrypt_Gronsfeld(self.textEdit.toPlainText(), self.lineEdit.text())
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Псевдосимвольное шифрование":
                self.final_text = Decrypt_pseudosim(self.textEdit.toPlainText())
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
            elif self.encode == "Бинарный код":
                self.final_text = Derypt_Binary_code((self.textEdit.toPlainText()))
                self.label_6.setText('\n'.join(textwrap.wrap(self.final_text)))
        except Exception:
            self.label_6.setText('Что-то не так... Проверьте правильность введённых данных')

    def copy_crypt(self):
        pyperclip.copy(self.final_text)  # копирует в буфер обмена


class Ip_Finder_Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ip.ui', self)
        self.setWindowIcon(QIcon('RM_icon.jpg'))
        self.pushButton.clicked.connect(self.run)

    def run(self):

        self.label_2.setText('')
        getIP = self.lineEdit.text()

        try:
            url = "https://ipinfo.io/" + getIP + "/json"  # создаём ссылочку
            getInfo = urllib.request.urlopen(url)  # забираем json
            infoList = json.load(getInfo)  # читаем его
            self.label_2.setText(
                "IP: {}\nCity: {}\nRegion: {}\nCountry: {}\nHostname: {}".format(infoList["ip"], infoList["city"],
                                                                                 infoList["region"],
                                                                                 infoList["country"], infoList["loc"]))
        except:
            self.label_2.setText("Что-то пошло не так :( Проверьте введённые данные")


class Number_Finder_Window3(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('number.ui', self)
        self.setWindowIcon(QIcon('RM_icon.jpg'))
        self.pushButton.clicked.connect(self.run)

    def run(self):

        self.label_2.setText('')
        phone = self.lineEdit.text()
        try:
            getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone  # создаём ссылочку
            infoPhone = urllib.request.urlopen(getInfo)  # забираем json
            infoPhone = json.load(infoPhone)  # читаем его
            self.label_2.setText("Number: +{}\nCountry: {}\nOkrug: {}\nOperator: {}\nWorld: {}".format(phone, infoPhone[
                "country"]["name"], infoPhone["region"]["name"], infoPhone["region"]["okrug"], infoPhone["0"]["oper"],
                                                                                                       infoPhone[
                                                                                                           "country"][
                                                                                                           "location"]))
        except Exception:
            self.label_2.setText("Что-то пошло не так :( Проверьте введённые данные")


class File_Coder_Window4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.file_name = 'Не выбран путь'
        uic.loadUi('file.ui', self)
        self.setWindowIcon(QIcon('RM_icon.jpg'))
        self.label.setText(self.file_name)
        self.pushButton.clicked.connect(self.crypt_run)
        self.pushButton_2.clicked.connect(self.decrypt_run)
        self.pushButton_3.clicked.connect(self.check_name)
        with open('import_info.json', 'r', encoding='utf-8') as f_obj:
            self.label_2.setText(json.load(f_obj)['info']["Шифровка файла"])

    def check_name(self):
        options = QtWidgets.QFileDialog.Options()
        name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", "C:\\",
                                                        "All Files (*);;Python Files (*.py)", options=options)
        if name:
            self.file_name = name
            self.label.setText(self.file_name)

    def crypt_run(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Ввод пароля", "Введите пароль"
        )
        if self.file_name != 'Не выбран путь':
            if okBtnPressed:
                try:
                    Crypt_file(self.file_name, i)  # шифруем файл
                    self.label_3.setText('Готово')
                except Exception:
                    self.label_3.setText('Ошибка\nПроверьте введённые данные')
            else:
                self.label_3.setText('Вы не ввели пароль')
        else:
            self.label_3.setText('Вы не ввели путь')

    def decrypt_run(self):
        i, okBtnPressed = QInputDialog.getText(
            self, "Ввод пароля", "Введите пароль"
        )
        if self.file_name != 'Не выбран путь':
            if okBtnPressed:
                try:
                    Decrypt_file(self.file_name, i)  # дешифруем файл
                    self.label_3.setText('Готово')
                except Exception:
                    self.label_3.setText('Ошибка\nПроверьте введённые данные')
            else:
                self.label_3.setText('Вы не ввели пароль')
        else:
            self.label_3.setText('Вы не ввели путь')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 300, 400, 350)
        self.setWindowTitle('CIN')
        self.setWindowIcon(QIcon('RM_icon.jpg'))
        self.pushButton = QPushButton('Шифровать сообщение', self)
        self.pushButton.setGeometry(QtCore.QRect(40, 80, 145, 81))
        self.pushButton_2 = QtWidgets.QPushButton('Пробить по ip', self)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 200, 145, 81))
        self.pushButton_3 = QtWidgets.QPushButton("Пробить по номеру", self)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 200, 145, 81))
        self.pushButton_4 = QPushButton('Зашифровать файл', self)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 80, 145, 81))
        self.pushButton.clicked.connect(self.show_window_1)
        self.pushButton_2.clicked.connect(self.show_window_2)
        self.pushButton_3.clicked.connect(self.show_window_3)
        self.pushButton_4.clicked.connect(self.show_window_4)

    def show_window_1(self):
        self.w1 = Text_Coder_Window1()
        self.w1.show()

    def show_window_2(self):
        self.w2 = Ip_Finder_Window2()
        self.w2.show()

    def show_window_3(self):
        self.w3 = Number_Finder_Window3()
        self.w3.show()

    def show_window_4(self):
        self.w4 = File_Coder_Window4()
        self.w4.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
