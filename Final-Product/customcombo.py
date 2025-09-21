from PySide6.QtWidgets import (QToolButton, QMenu)
from PySide6.QtCore import Signal, Qt

class CustomCombo(QToolButton):
    action_triggered = Signal(int, str)
    on_action_triggered = Signal(int)

    def __init__(self, data=None, custom_indices=None):
        super().__init__()
        self._current_index = -1
        self.last_index = None
        self.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        
        self.menu = QMenu()
        # Set menu position to appear on the right
        self.menu.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        
        self.menu.setStyleSheet("""
            QMenu {
                font-size: 13px;
            }
            QMenu::item {
                padding: 5px 20px 5px 20px;
            }
            QMenu::item:selected {
                background-color: rgba(229, 243, 255, 0.383);
            }
        """)
        self.setMenu(self.menu)
        
        self.setText("Select an item")
        self.setMinimumWidth(200)
        self.setStyleSheet("""
            QToolButton::menu-indicator { 
                width: 20px;
                height: 20px;
                subcontrol-position: right center;
                subcontrol-origin: padding;
                left: -8px;
            }
            QToolButton {
                padding-right: 20px;
                font-size: 16px;
                text-align: left;
            }
            QToolButton:hover {
                background-color: rgba(144, 140, 140, 0.183);
            }
        """)

        if data:
            self.setData(data, custom_indices)

    def showMenu(self):
        # Calculate the position for the menu
        pos = self.rect().bottomLeft()  # Use bottomLeft instead of bottomRight
        global_pos = self.mapToGlobal(pos)
        
        # Set the menu's width to match the widget's width
        self.menu.setMinimumWidth(self.width())
        
        # Adjust position to align with widget
        self.menu.popup(global_pos)

    def showEvent(self, event):
        super().showEvent(event)
        # Ensure menu appears aligned with widget
        self.menu.setLayoutDirection(Qt.LayoutDirection.LeftToRight)



    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.showMenu()
        else:
            super().mousePressEvent(event)

    def _on_action_triggered(self, action):
        self.setText(action.text())
        index = action.data()
        self._current_index = index
        self.action_triggered.emit(index, action.text())
        self.on_action_triggered.emit(index)

    def addItem(self, item, parent_menu=None, index=None):
        if parent_menu is None:
            parent_menu = self.menu
            
        if isinstance(item, str):
            action = parent_menu.addAction(item)
            if isinstance(index, dict):
                action.setData(index.get(item, len(self.menu.actions())))
            else:
                action.setData(index[0] if index else len(self.menu.actions()))
                if index:
                    index[0] += 1
            action.triggered.connect(lambda: self._on_action_triggered(action))
        elif isinstance(item, (tuple, list)):
            if len(item) == 2:
                menu_name, subitems = item
                submenu = QMenu(menu_name, parent_menu)
                submenu.setStyleSheet(self.menu.styleSheet())
                parent_menu.addMenu(submenu)
                for subitem in subitems:
                    self.addItem(subitem, submenu, index)

    def setData(self, data, custom_indices=None):
        self.menu.clear()
        if custom_indices is None:
            index = [0]
        else:
            index = custom_indices
        for item in data:
            self.addItem(item, index=index)

    def currentIndex(self):
        return self._current_index
    
    def setCurrentIndex(self, index):
        self._current_index = index

    def currentText(self):
        return self.text()
