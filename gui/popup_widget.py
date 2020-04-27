from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from globals import globals
from graph import node_widget
from graph import edge_widget

class PopupWidget(GridLayout):

    def closePopUp(self):
        globals.popupWindow.dismiss()
        globals.graphManager.update_canvas()

    def new_radius(self, *args):
        self.ids.nodeRadius_lbl.text = str(int(args[1]))
        node_widget.changeNodeRadius(int(args[1]))
        self.ids.radiusSlider.value = int(args[1])
        globals.graphManager.update_canvas()
        for edge in globals.graphManager.edgeWidgets:
            edge.updateCoords()

    def new_length(self, *args):
        self.ids.edgeLength_lbl.text = str(int(args[1]))
        edge_widget.changeEdgeLength(int(args[1]))
        self.ids.edgeSlider.value = int(args[1])

    def getNodeWidgetBackgroundColor(self):
        return globals.NodeWidgetBackgroundColor

    def getNodeWidgetColor(self):
        return globals.NodeWidgetColor

    def getEdgeWidgetColor(self):
        return globals.EdgeWidgetColor

    def getEdgeSliderValue(self):
        return globals.lengthOfEdgeWidget

    def getRadiusSliderValue(self):
        return globals.radiusOfNodeWidget

class ErrorPopupWidget(BoxLayout):
    def setText(self, text):
        globals.errorPopupWidget.ids.error_popup_lbl.text = text

    def closePopUp(self):
        globals.popupWindow.dismiss()