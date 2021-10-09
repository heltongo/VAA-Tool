##feature5
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import wx
import sys

def geographic_Selection(var1, var2, var3):
    connection = sqlite3.connect("Crashdb.db")
    cursor = connection.cursor()
    string = "SELECT count(ACCIDENT_NO), LGA_NAME from CrashStatisticsVictoria"
    cursor.execute(string)
    result = cursor.fetchall()
    list1 = []
    list2 = []
    for r in result:
        list1.append(r[0])
        list2.append(r[1])
    connection.close()

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        # plt.figure(figsize=(8, 5))
        plt.xlabel('Accidents')
        plt.xticks(range(1, 24))
        plt.ylabel('LGA Name')
        plt.title('Geographic Impact Analysis - Accident Prone Area Report')
        plt.plot(list1, list2)
        plt.show()

if __name__ == "__main__":
    app = wx.PySimpleApp()
    fr = wx.Frame(None, title='test')
    panel = CanvasPanel(fr)
    panel.draw()
    fr.Show()
    app.MainLoop()
