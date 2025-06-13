import sys
import os
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsView, QGraphicsScene, QPushButton, QLabel, QVBoxLayout, QWidget, QListWidget, QHBoxLayout, QSpinBox, QGraphicsItem, QGraphicsLineItem, QGraphicsItemGroup, QInputDialog, QGraphicsRectItem, QGraphicsEllipseItem, QMenuBar
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor, QPolygonF, QAction
from PyQt6.QtCore import Qt, QPointF, QRectF, QSizeF

class ResizableRectItem(QGraphicsRectItem):
    def __init__(self, *args):
        super().__init__(*args)
        self.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable |
                      QGraphicsItem.GraphicsItemFlag.ItemIsSelectable |
                      QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.setAcceptHoverEvents(True)
        self.handle_size = 8
        self.handles = []

    def hoverMoveEvent(self, event):
        cursor = Qt.CursorShape.ArrowCursor
        for handle in self.handles:
            if handle.contains(event.pos()):
                cursor = Qt.CursorShape.SizeFDiagCursor
                break
        self.setCursor(cursor)
        super().hoverMoveEvent(event)

    def mousePressEvent(self, event):
        for handle in self.handles:
            if handle.contains(event.pos()):
                self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
                break
        else:
            self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        super().mouseReleaseEvent(event)

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        if self.isSelected():
            pen = QPen(Qt.GlobalColor.blue, 1, Qt.PenStyle.DashLine)
            painter.setPen(pen)
            painter.drawRect(self.rect())
            self.handles = [QRectF(self.rect().topLeft(), QSizeF(self.handle_size, self.handle_size)),
                            QRectF(self.rect().topRight() - QPointF(self.handle_size, 0), QSizeF(self.handle_size, self.handle_size)),
                            QRectF(self.rect().bottomLeft() - QPointF(0, self.handle_size), QSizeF(self.handle_size, self.handle_size)),
                            QRectF(self.rect().bottomRight() - QPointF(self.handle_size, self.handle_size), QSizeF(self.handle_size, self.handle_size))]
            for handle in self.handles:
                painter.fillRect(handle, Qt.GlobalColor.blue)

class ResizableEllipseItem(QGraphicsEllipseItem):
    def __init__(self, *args):
        super().__init__(*args)
        self.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable |
                      QGraphicsItem.GraphicsItemFlag.ItemIsSelectable |
                      QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.setAcceptHoverEvents(True)
        self.handle_size = 8
        self.handles = []

    def hoverMoveEvent(self, event):
        cursor = Qt.CursorShape.ArrowCursor
        for handle in self.handles:
            if handle.contains(event.pos()):
                cursor = Qt.CursorShape.SizeFDiagCursor
                break
        self.setCursor(cursor)
        super().hoverMoveEvent(event)

    def mousePressEvent(self, event):
        for handle in self.handles:
            if handle.contains(event.pos()):
                self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
                break
        else:
            self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        super().mouseReleaseEvent(event)

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        if self.isSelected():
            pen = QPen(Qt.GlobalColor.blue, 1, Qt.PenStyle.DashLine)
            painter.setPen(pen)
            painter.drawEllipse(self.rect())
            self.handles = [QRectF(self.rect().topLeft(), QSizeF(self.handle_size, self.handle_size)),
                            QRectF(self.rect().topRight() - QPointF(self.handle_size, 0), QSizeF(self.handle_size, self.handle_size)),
                            QRectF(self.rect().bottomLeft() - QPointF(0, self.handle_size), QSizeF(self.handle_size, self.handle_size)),
                            QRectF(self.rect().bottomRight() - QPointF(self.handle_size, self.handle_size), QSizeF(self.handle_size, self.handle_size))]
            for handle in self.handles:
                painter.fillRect(handle, Qt.GlobalColor.blue)

class ResizableCrossItem(QGraphicsItemGroup):
    def __init__(self, *args):
        super().__init__(*args)
        self.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsMovable |
                      QGraphicsItem.GraphicsItemFlag.ItemIsSelectable |
                      QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges)
        self.setAcceptHoverEvents(True)
        self.handle_size = 8
        self.handles = []

    def hoverMoveEvent(self, event):
        cursor = Qt.CursorShape.ArrowCursor
        for handle in self.handles:
            if handle.contains(event.pos()):
                cursor = Qt.CursorShape.SizeFDiagCursor
                break
        self.setCursor(cursor)
        super().hoverMoveEvent(event)

    def mousePressEvent(self, event):
        for handle in self.handles:
            if handle.contains(event.pos()):
                self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
                break
        else:
            self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
        super().mouseReleaseEvent(event)

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        if self.isSelected():
            pen = QPen(Qt.GlobalColor.blue, 1, Qt.PenStyle.DashLine)
            painter.setPen(pen)
            self.handles = [QRectF(self.boundingRect().topLeft(), QSizeF(self.handle_size, self.handle_size)),
                            QRectF(self.boundingRect().topRight() - QPointF(self.handle_size, 0), QSizeF(self.handle_size, self.handle_size)),
                            QRectF(self.boundingRect().bottomLeft() - QPointF(0, self.handle_size), QSizeF(self.handle_size, self.handle_size)),
                            QRectF(self.boundingRect().bottomRight() - QPointF(self.handle_size, self.handle_size), QSizeF(self.handle_size, self.handle_size))]
            for handle in self.handles:
                painter.fillRect(handle, Qt.GlobalColor.blue)

class ImageAnnotationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Labeling Tool")
        self.setGeometry(100, 100, 1000, 700)
        
        self.image_path = None
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        self.shape = "cross"  # Default shape
        self.drawing = False
        self.current_points = []
        self.annotations = []
        self.shape_size = 50  # Default shape size
        
        self.initUI()
    
    def initUI(self):
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        center_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        
        self.load_button = QPushButton("Open Folder")
        self.load_button.clicked.connect(self.loadFolder)
        left_layout.addWidget(self.load_button)
        
        self.save_button = QPushButton("Save Annotations")
        self.save_button.clicked.connect(self.saveAnnotations)
        left_layout.addWidget(self.save_button)
        
        self.delete_button = QPushButton("Delete Annotation")
        self.delete_button.clicked.connect(self.deleteAnnotation)
        left_layout.addWidget(self.delete_button)
        
        self.cross_button = QPushButton("Cross")
        self.cross_button.clicked.connect(lambda: self.setShape("cross"))
        left_layout.addWidget(self.cross_button)
        
        self.rect_button = QPushButton("Rectangle")
        self.rect_button.clicked.connect(lambda: self.setShape("rectangle"))
        left_layout.addWidget(self.rect_button)
        
        self.circle_button = QPushButton("Circle")
        self.circle_button.clicked.connect(lambda: self.setShape("circle"))
        left_layout.addWidget(self.circle_button)
        
        self.size_input = QSpinBox()
        self.size_input.setRange(10, 1000)  # Allow any size for tools
        self.size_input.setValue(self.shape_size)
        self.size_input.setPrefix("Size: ")
        self.size_input.valueChanged.connect(self.updateShapeSize)
        left_layout.addWidget(self.size_input)
        
        center_layout.addWidget(self.view)
        
        self.label_list = QListWidget()
        self.label_list.itemClicked.connect(self.selectLabel)
        right_layout.addWidget(QLabel("Labels:"))
        right_layout.addWidget(self.label_list)
        
        self.add_label_button = QPushButton("Add Label")
        self.add_label_button.clicked.connect(self.addLabel)
        right_layout.addWidget(self.add_label_button)
        
        self.delete_label_button = QPushButton("Delete Label")
        self.delete_label_button.clicked.connect(self.deleteLabel)
        right_layout.addWidget(self.delete_label_button)
        
        self.annotation_list = QListWidget()
        right_layout.addWidget(QLabel("Annotations:"))
        right_layout.addWidget(self.annotation_list)
        
        self.image_list = QListWidget()
        self.image_list.itemClicked.connect(self.loadImage)
        right_layout.addWidget(QLabel("Image List:"))
        right_layout.addWidget(self.image_list)
        
        container = QWidget()
        main_layout.addLayout(left_layout, 1)
        main_layout.addLayout(center_layout, 3)
        main_layout.addLayout(right_layout, 1)
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        
        self.view.setMouseTracking(True)
        self.view.viewport().installEventFilter(self)
        
        # Add menu bar for saving annotations
        menubar = QMenuBar(self)
        file_menu = menubar.addMenu('File')
        save_action = QAction('Save Annotations', self)
        save_action.triggered.connect(self.saveAnnotations)
        file_menu.addAction(save_action)
        self.setMenuBar(menubar)
    
    def loadFolder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Open Folder", "")
        if folder_path:
            self.image_list.clear()
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                    self.image_list.addItem(os.path.join(folder_path, file_name))
    
    def loadImage(self, item):
        self.image_path = item.text()
        self.pixmap = QPixmap(self.image_path)
        self.scene.clear()
        self.scene.addPixmap(self.pixmap.scaled(self.view.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        self.view.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
        self.loadAnnotations()
    
    def saveAnnotations(self):
        if not self.image_path:
            return
        
        annotations_data = []
        for annotation in self.annotations:
            shape, label, item = annotation
            coords = item.scenePos()
            annotations_data.append({
                'shape': shape,
                'label': label,
                'coords': (coords.x(), coords.y())
            })
        
        json_path = os.path.splitext(self.image_path)[0] + '.json'
        with open(json_path, 'w') as json_file:
            json.dump(annotations_data, json_file)
    
    def loadAnnotations(self):
        self.annotations.clear()
        self.annotation_list.clear()
        
        json_path = os.path.splitext(self.image_path)[0] + '.json'
        if os.path.exists(json_path):
            with open(json_path, 'r') as json_file:
                annotations_data = json.load(json_file)
                for annotation_data in annotations_data:
                    shape = annotation_data['shape']
                    label = annotation_data['label']
                    x, y = annotation_data['coords']
                    pos = QPointF(x, y)
                    
                    if shape == "rectangle":
                        rect = ResizableRectItem(QRectF(pos.x() - self.shape_size / 2, pos.y() - self.shape_size / 2, self.shape_size, self.shape_size))
                        rect.setPen(QPen(Qt.GlobalColor.green, 5))
                        self.scene.addItem(rect)
                        self.annotations.append((shape, label, rect))
                    elif shape == "circle":
                        circle = ResizableEllipseItem(QRectF(pos.x() - self.shape_size / 2, pos.y() - self.shape_size / 2, self.shape_size, self.shape_size))
                        circle.setPen(QPen(Qt.GlobalColor.red, 5))
                        self.scene.addItem(circle)
                        self.annotations.append((shape, label, circle))
                    elif shape == "cross":
                        line1 = QGraphicsLineItem(pos.x() - self.shape_size / 2, pos.y() - self.shape_size / 2, pos.x() + self.shape_size / 2, pos.y() + self.shape_size / 2)
                        line2 = QGraphicsLineItem(pos.x() + self.shape_size / 2, pos.y() - self.shape_size / 2, pos.x() - self.shape_size / 2, pos.y() + self.shape_size / 2)
                        line1.setPen(QPen(Qt.GlobalColor.blue, 5))
                        line2.setPen(QPen(Qt.GlobalColor.blue, 5))
                        cross = ResizableCrossItem()
                        cross.addToGroup(line1)
                        cross.addToGroup(line2)
                        self.scene.addItem(cross)
                        self.annotations.append((shape, label, cross))
        
        self.updateAnnotations()
    
    def deleteAnnotation(self):
        selected_items = self.scene.selectedItems()
        if selected_items:
            for item in selected_items:
                self.scene.removeItem(item)
                self.annotations = [annotation for annotation in self.annotations if annotation[2] != item]
            self.updateAnnotations()
    
    def addLabel(self):
        label, ok = QInputDialog.getText(self, "Add Label", "Enter label:")
        if ok and label:
            self.label_list.addItem(label)
    
    def deleteLabel(self):
        selected_items = self.label_list.selectedItems()
        if selected_items:
            for item in selected_items:
                self.label_list.takeItem(self.label_list.row(item))
    
    def selectLabel(self, item):
        self.selected_label = item.text()
    
    def setShape(self, shape):
        self.shape = shape
    
    def updateShapeSize(self, size):
        self.shape_size = size
    
    def eventFilter(self, source, event):
        if event.type() == event.Type.MouseButtonPress and source == self.view.viewport() and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.startDrawing(event)
        elif event.type() == event.Type.MouseMove and source == self.view.viewport() and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.keepDrawing(event)
        elif event.type() == event.Type.MouseButtonRelease and source == self.view.viewport() and event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            self.endDrawing(event)
        return super().eventFilter(source, event)
    
    def startDrawing(self, event):
        self.drawing = True
        pos = self.view.mapToScene(event.pos())
        self.current_points.append(pos)
    
    def keepDrawing(self, event):
        if not self.drawing:
            return
        pos = self.view.mapToScene(event.pos())
    
    def endDrawing(self, event):
        self.drawing = False
        pos = self.view.mapToScene(event.pos())
        label = self.selected_label if hasattr(self, 'selected_label') else ""
        
        if self.shape == "rectangle":
            rect = ResizableRectItem(QRectF(pos.x() - self.shape_size / 2, pos.y() - self.shape_size / 2, self.shape_size, self.shape_size))
            rect.setPen(QPen(Qt.GlobalColor.green, 5))  # Thicker stroke
            self.scene.addItem(rect)
            self.annotations.append(("Rectangle", label, rect))
        elif self.shape == "circle":
            circle = ResizableEllipseItem(QRectF(pos.x() - self.shape_size / 2, pos.y() - self.shape_size / 2, self.shape_size, self.shape_size))
            circle.setPen(QPen(Qt.GlobalColor.red, 5))  # Thicker stroke
            self.scene.addItem(circle)
            self.annotations.append(("Circle", label, circle))
        elif self.shape == "cross":
            line1 = QGraphicsLineItem(pos.x() - self.shape_size / 2, pos.y() - self.shape_size / 2, pos.x() + self.shape_size / 2, pos.y() + self.shape_size / 2)
            line2 = QGraphicsLineItem(pos.x() + self.shape_size / 2, pos.y() - self.shape_size / 2, pos.x() - self.shape_size / 2, pos.y() + self.shape_size / 2)
            line1.setPen(QPen(Qt.GlobalColor.blue, 5))  # Thicker stroke
            line2.setPen(QPen(Qt.GlobalColor.blue, 5))  # Thicker stroke
            cross = ResizableCrossItem()
            cross.addToGroup(line1)
            cross.addToGroup(line2)
            self.scene.addItem(cross)
            self.annotations.append(("Cross", label, cross))
        
        self.updateAnnotations()
        self.current_points = []  # Reset points
    
    def updateAnnotations(self):
        self.annotation_list.clear()
        for annotation in self.annotations:
            shape, label, item = annotation
            coords = item.scenePos()
            self.annotation_list.addItem(f"{shape} {label} - Coords: ({coords.x()}, {coords.y()})")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageAnnotationApp()
    window.show()
    sys.exit(app.exec())