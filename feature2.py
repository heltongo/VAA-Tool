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


def hour_Selection(var1,var2):
    list1 = []
    list2 = []
    #var1 = '2014-01-01'
    #var2 ='2018-12-31' a

    connection = sqlite3.connect("data/crashdb.db")
    cursor = connection.cursor()
    connection = sqlite3.connect("data/crashdb.db")
    cursor = connection.cursor()
    string = "SELECT cast(ACCIDENT_TIME as int) AS 'HOUR',COUNT(*) AS 'COUNT' FROM CrashStatisticsVictoria\
                WHERE ACCIDENT_DATE>=:Start_date and ACCIDENT_DATE<=:End_date\
                GROUP BY HOUR"
    cursor.execute(string, {"Start_date": var1, "End_date": var2})
    result = cursor.fetchall()

    for r in result:
        list1.append(r[0])
        list2.append(r[1])

    plt.figure(figsize=(8, 5))
    plt.xlabel('Hours')
    plt.xticks(range(1, 24))
    plt.ylabel('Number of accidents')
    plt.title('Hourly Analysis of Accidents')
    plt.plot(list1, list2)
    plt.show()


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


if __name__ == "__main__":
    pp = wx.PySimpleApp()
    fr = wx.Frame(None, title='test')
    panel = CanvasPanel(fr)
    # ////

    x = hour_Selection('2014-01-01','2018-12-31')
    fr.Show()
    app.MainLoop()

