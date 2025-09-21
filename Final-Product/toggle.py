from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import Qt, QPropertyAnimation, QRectF, QEasingCurve, Property, QParallelAnimationGroup, QSize
from PySide6.QtGui import QPainter, QColor, QPen

class CustomToggle(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(60, 30)
        
        # Colors
        self._off_color = QColor(200, 200, 200)
        self._on_color = QColor(0, 150, 136)
        self._circle_color = QColor(255, 255, 255)
        
        # State
        self._circle_position = 3
        self._bg_color = self._off_color
        
        # Setup animations
        self.setup_animations()

    def setup_animations(self):
        self.animation_group = QParallelAnimationGroup(self)
        
        # Position animation
        self.position_anim = QPropertyAnimation(self, b"circle_position")
        self.position_anim.setDuration(300)
        
        # Color animation
        self.color_anim = QPropertyAnimation(self, b"bg_color")
        self.color_anim.setDuration(300)
        
        self.animation_group.addAnimation(self.position_anim)
        self.animation_group.addAnimation(self.color_anim)
        
        # Connect state change
        self.stateChanged.connect(self._handle_state_change)

    # Properties
    @Property(float)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self, pos):
        self._circle_position = pos
        self.update()

    @Property(QColor)
    def bg_color(self):
        return self._bg_color

    @bg_color.setter
    def bg_color(self, color):
        self._bg_color = color
        self.update()

    def _handle_state_change(self, checked):
        # Update animations
        self.position_anim.setStartValue(self._circle_position)
        self.position_anim.setEndValue(33 if checked else 3)
        
        self.color_anim.setStartValue(self._bg_color)
        self.color_anim.setEndValue(self._on_color if checked else self._off_color)
        
        self.animation_group.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw background
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(self._bg_color)
        painter.drawRoundedRect(0, 0, self.width(), self.height(), 15, 15)

        # Draw circle
        painter.setBrush(self._circle_color)
        painter.drawEllipse(int(self._circle_position), 3, 24, 24)

    def sizeHint(self):
        return QSize(60, 30)

    def minimumSizeHint(self):
        return self.sizeHint()
