from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import wx
import sqlite3
from PeriodGUI import *


# MAIN PANEL

class mainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent = parent)
        vaaText = wx.StaticText(pnl, pos=(250, 10), label="Victoria Accident Analysis Tool")
        font = vaaText.GetFont()
        font.PointSize += 16
        font = font.Bold()
        vaaText.SetFont(font)

        joinText = wx.StaticText(pnl, pos=(120, 30), label="Home")
        font = joinText.GetFont()
        font.PointSize += 10
        joinText.SetFont(font)

        png = wx.Image('logo.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (10, 5), (png.GetWidth(), png.GetHeight()))

        self.timeButton = wx.Button(pnl, pos=(10, 110), label="Time Analysis")
        self.timeButton.Bind(wx.EVT_BUTTON, self.OnClick)

        self.hourlyButton = wx.Button(pnl, pos=(10, 140), label="Hourly Accident Analysis")
        # sizer.Add(self.hourlyButton, pos=(1, 0), span=(1, 1), flag=wx.TOP | wx.EXPAND, border=5)
        self.hourlyButton.Bind(wx.EVT_BUTTON, self.hourButton)

        self.keywordButton = wx.Button(pnl, pos=(10, 170), label="Accident by type Analysis")

        self.alcoholButton = wx.Button(pnl, pos=(10, 200), label="Alcohol Impact Analysis")

        self.geographicButton = wx.Button(pnl, pos=(10, 230), label="Geographic Impact Analysis")


# FIRST PANEL

class Panel1(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent = parent)
        self.dateFromText = wx.StaticText(self, pos=(280, 80), label="Date From:")
        self.font = self.dateFromText.GetFont()
        self.font.PointSize += 10
        self.dateFromText.SetFont(self.font)

        self.dateFrom = wx.TextCtrl(self, pos=(400, 80), size=(105, 30))

        self.dateToText = wx.StaticText(self, pos=(280, 110), label="Date To:")
        self.font = self.dateToText.GetFont()
        self.font.PointSize += 10
        self.dateToText.SetFont(self.font)

        self.dateTo = wx.TextCtrl(self, pos=(400, 110), size=(105, 30))

        self.submitButton = wx.Button(self, pos=(400, 300), label="Submit")
        self.submitButton.Bind(wx.EVT_BUTTON, self.SubmitButton)

# MAIN WINDOW
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title="VAA Tool", size=(1000, 1000))
        # self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # self.CreateStatusBar()  # A Statusbar in the bottom of the window
        # self.initialise()
        splitter = wx.SplitterWindow(self)
        left = mainPanel(splitter)
        right = Panel1(splitter)
        splitter.SplitVertically(left, right)
        splitter.SetMinimumPaneSize(400)
        # self.mainPanel = mainPanel(self)
        # self.panel1= Panel1(self)
        # self.panel2 = Panel2(self)
        # self.panel3 = Panel3(self)
        # self.panel4 = Panel4(self)
        # self.panel5 = Panel5(self)

    def OnClick(self, event):
        # mainPanel = Panel1(self)
        # # panels = self.panel.Show(self.panel)
        # self.Show(mainPanel)
         print(panels)

    def hourButton(self, event):
        self.frame.Show()
        self.Hide()

if __name__ == '__main__':
    app = wx.App(redirect=True)
    frame = MainWindow(None, "VAA Tool")
    frame.Show()
    app.MainLoop()
