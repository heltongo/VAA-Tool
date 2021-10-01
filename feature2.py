from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import wx
import sys


import sqlite3
import matplotlib.pyplot as plt
connection = sqlite3.connect("crashdb.db")
cursor = connection.cursor()
string = "SELECT cast(ACCIDENT_TIME as int) AS 'HOUR',COUNT(*) AS 'COUNT' FROM CrashStatisticsVictoria GROUP BY HOUR"
    # string="SELECT sum(cast(price as INT)) from listings_dec18 "
    # query=string.format(first=var1,second=var2)
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
        #plot_ditribution()

        plt.figure(figsize=(8, 5))
        plt.xlabel('Hours')
        plt.xticks(range(1,24))
        plt.ylabel('Number of accidents')
        plt.title('Hourly Analysis of Accidents')
        plt.plot(list1, list2)
        plt.show()
        

if __name__ == "__main__":
    app = wx.PySimpleApp()
    fr = wx.Frame(None, title='test')
    panel = CanvasPanel(fr)
    panel.draw()
    fr.Show()
    app.MainLoop()
