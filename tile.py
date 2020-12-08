from PySide2.QtGui import QPixmap, QTransform, QImage
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide2.QtWidgets import QLabel
from PySide2.QtCore import QUrl, Qt, QVariantAnimation, QEasingCurve, QSize


class Tile(QLabel):
    def __init__(self, row, col, img_url, parent=None):
        super(Tile, self).__init__(parent=parent)
        self.row = row
        self.col = col
        self.setGeometry(0, 0, 200, 200)
        self.setMargin(10)
        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.mousePressEvent = lambda event: self.handle_mouse_pressed(event)
        self.setStyleSheet("border: 1px dotted gray;")

        # load the image
        manager = QNetworkAccessManager(self)
        manager.finished[QNetworkReply].connect(self.disp_image)
        manager.get(QNetworkRequest(QUrl("https://images.dog.ceo/breeds/groenendael/n02105056_6127.jpg")))

        # default pixmap
        self.default_pixmap = QPixmap(200, 200)
        self.default_pixmap.fill(Qt.gray)
        self.setPixmap(self.default_pixmap)

        # second pixmap
        self.dog_pixmap = QPixmap(200, 200)

        self.anim = QVariantAnimation()
        self.anim.setDuration(500)
        self.anim.setEasingCurve(QEasingCurve.Linear)
        self.anim.valueChanged.connect(self.anim_value_changed)
        self.anim.setStartValue(float(0))
        self.anim.setEndValue(float(180))

        self.anim1 = QVariantAnimation()
        self.anim1.setDuration(500)
        self.anim1.setEasingCurve(QEasingCurve.Linear)
        self.anim1.valueChanged.connect(self.anim1_value_changed)
        self.anim1.setStartValue(float(180))
        self.anim1.setEndValue(float(0))

        self.resize(200, 200)
        self.anim1.start()

    def disp_image(self, reply):
        image_data = reply.readAll()
        image = QImage()
        image.loadFromData(image_data)
        self.dog_pixmap = QPixmap.fromImage(image).scaled(QSize(200, 200), Qt.KeepAspectRatio, Qt.FastTransformation)
        self.setPixmap(self.dog_pixmap)

    def anim_value_changed(self, value):
        value = int(value)
        t = QTransform()
        t.rotate(value, Qt.YAxis)
        self.setPixmap(self.dog_pixmap.transformed(t))
        if value == 180:
            self.anim1.start()

    def anim1_value_changed(self, value):
        value = int(value)
        t = QTransform()
        t.rotate(value, Qt.YAxis)
        self.setPixmap(self.default_pixmap.transformed(t))

    def handle_mouse_pressed(self, event):
        self.anim.start()
