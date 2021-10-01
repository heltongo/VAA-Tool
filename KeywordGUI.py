from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import wx

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

        joinText = wx.StaticText(pnl, pos = (120,30), label="Home")
        font = joinText.GetFont()
        font.PointSize += 10
        joinText.SetFont(font)

        png = wx.Image('logo.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (10,5), (png.GetWidth(), png.GetHeight()))

        periodButton = wx.Button(pnl, pos=(10, 110), label="Period Analysis")

        hourButton = wx.Button(pnl, pos=(10, 140), label="Hour Analysis")

        keywordButton = wx.Button(pnl, pos=(10, 170), label="Keyword Analysis")

        alcoholButton = wx.Button(pnl, pos=(10, 200), label="Alcohol Impact Analysis")

        geographicButton = wx.Button(pnl, pos=(10, 230), label="Geographic Impact Analysis")



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
        self.submitButton.Bind(wx.EVT_BUTTON, self.OnSend)

    def OnSend(self, event):
        val1 = self.dateFromText.GetValue()
        val2 = self.dateToText.GetValue()
        print(val1)

        # dateFromText = wx.StaticText(pnl, pos=(280, 110), label="Date From:")
        # font = dateFromText.GetFont()
        # font.PointSize += 10
        # dateFromText.SetFont(font)
        #
        # dateFrom = wx.TextCtrl(pnl, pos=(400, 110), size=(105, 30))
        #
        #
        # dateToText = wx.StaticText(pnl, pos=(280, 80), label="Date To:")
        # font = dateToText.GetFont()
        # font.PointSize += 10
        # dateToText.SetFont(font)
        #
        # dateTo = wx.TextCtrl(pnl, pos=(400, 80), size=(105, 30))

        # submitButton = wx.Button(pnl, pos=(400, 300), label="Submit")
        # submitButton.Bind(wx.EVT_BUTTON, pnl.OnSend)




    # def onResize(self, event):
    #     # self.Layout()
    #     frame_size = self.GetSize()
    #     frame_h = (frame_size[0]-10) / 2
    #     frame_w = (frame_size[1]-10) / 2
    #     png = self.png.Scale(frame_h,frame_w)
    #     self.m_bitmap3.SetBitmap(wx.BitmapFromImage(png))
    #     self.Refresh()
    #     self.Layout()

app = wx.App(False)
frame = MainWindow(None, "VAA Tool")
app.MainLoop()

