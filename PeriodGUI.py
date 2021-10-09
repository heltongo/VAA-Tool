from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import wx
import sqlite3
from feature1 import *
from HourGUI import MainWindows




# # PANEL
# class CanvasPanel(wx.Panel):
#     def __init__(self, parent, OnClick):
#         wx.Panel.__init__(self, parent, OnClick)
#         self.figure = Figure()
#         self.axes = self.figure.add_subplot(111)
#         self.canvas = FigureCanvas(self, -1, self.figure)
#         self.sizer = wx.BoxSizer(wx.VERTICAL)
#         self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
#         self.SetSizer(self.sizer)
#         self.Fit()
#
#     def draw(self):
#         # plot_ditribution()
#
#         plt.figure(figsize=(8, 5))
#         plt.xlabel('Hours')
#         plt.xticks(range(1, 24))
#         plt.ylabel('Number of accidents')
#         plt.title('Hourly Analysis of Accidents')
#         plt.plot(list1, list2)
#         plt.show()

# MAIN WINDOW
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
        self.hourlyButton.Bind(wx.EVT_BUTTON, self.hourButton)

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

        self.submitButton = wx.Button(self, pos=(400, 300), label="Submit")
        self.submitButton.Bind(wx.EVT_BUTTON, self.SubmitButton)

        # self.panel = CanvasPanel(self, self.OnClick)

    def SubmitButton(self, event):
        fromDate = self.dateFrom.GetValue()
        toDate = self.dateTo.GetValue()
        result = date_Selection(fromDate, toDate)
        print(result)
        print(fromDate)
        print(toDate)
        print("Submit button clicked")

    # def OnClick(self, event):
    #     panels = self.panel.Show(self.panel)
    #     print(panels)
    # this code shows the hour window from the back
    def hourButton(self, event):
        windows = MainWindows
        self.frame.Show(windows)
        # self.Hide()


app = wx.App(redirect=True)
frame = MainWindow(None, "VAA Tool")
frame.Show()
app.MainLoop()
