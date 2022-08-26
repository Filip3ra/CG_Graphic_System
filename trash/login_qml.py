from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtGui import QGuiApplication

app = QGuiApplication()

engine = QQmlApplicationEngine()

engine.load('login_qml.qml')

app.exec()