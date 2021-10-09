from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import wx
from feature3 import *

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 400))
        # self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # self.CreateStatusBar()  # A Statusbar in the bottom of the window
        self.initialise()


    def initialise(self):
        self.Show(True)
        pnl = wx.Panel(self,size=(1000, 1000))
        vaaText = wx.StaticText(pnl, pos = (250,10), label = "Victoria Accident Analysis Tool")
        font = vaaText.GetFont()
        font.PointSize+=16
        font = font.Bold()
        vaaText.SetFont(font)

        joinText = wx.StaticText(pnl, pos = (110,75), label="Home")
        font = joinText.GetFont()
        font.PointSize += 5
        joinText.SetFont(font)

        png = wx.Image('logo.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (10,5), (png.GetWidth(), png.GetHeight()))

        timeButton = wx.Button(pnl, pos=(10, 110), label="Time Analysis                         ")

        self.hourlyButton = wx.Button(pnl, pos=(10, 140), label="Hourly Accident Analysis      ")
        # self.hourlyButton.Bind(wx.EVT_BUTTON, self.hourButton)

        keywordButton = wx.Button(pnl, pos=(10, 170), label="Accident by type Analysis     ")

        alcoholButton = wx.Button(pnl, pos=(10, 200), label="Alcohol Impact Analysis         ")

        geographicButton = wx.Button(pnl, pos=(10, 230), label="Geographic Impact Analysis  ")




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


        self.keywordText = wx.StaticText(self, pos=(280, 140), label="Keyword:")
        self.font = self.keywordText.GetFont()
        self.font.PointSize += 10
        self.keywordText.SetFont(self.font)

        self.keyword = wx.TextCtrl(self, pos=(400, 140), size=(105, 30))

        self.submitButton = wx.Button(self, pos=(400, 300), label="Submit")
        self.submitButton.Bind(wx.EVT_BUTTON, self.SubmitButton)


    def SubmitButton(self, event):
        fromDate = self.dateFrom.GetValue()
        toDate = self.dateTo.GetValue()
        key = self.keyword.GetValue()
        keyword = keyword_Selection(fromDate, toDate, key)
        print(fromDate)
        print(toDate)
        print(key)
        print("Submit button clicked")

    # def OnClick(self, event):
    #     panels = self.panel.Show(self.panel)
    #     print(panels)



app = wx.App(redirect=True)
frame = MainWindow(None, "VAA Tool")
frame.Show()
app.MainLoop()

