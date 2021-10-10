import wx
from matplotlib import pyplot as plt
from numpy import arange, sin, pi
import matplotlib as pyplot
import os.path

# matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

# import wxwidgets

# import db_units as data
from wx.lib.agw.ribbon import panel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "data\crashdb.db")


# with sqlite3.connect(db_path) as db:

class Panel_root(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        # self.SetBackgroundColour(wx.RED)


        # put some text with a larger bold font on it
        vaaText = wx.StaticText(self, pos=(230, 10), label="Victoria Accident Analysis Tool")
        font = vaaText.GetFont()
        font.PointSize += 8
        font = font.Bold()
        vaaText.SetFont(font)

        joinText = wx.StaticText(self, pos=(10, 110), label="Home")
        font = joinText.GetFont()
        font.PointSize += 7
        joinText.SetFont(font)



        joinText = wx.StaticText(self, pos=(210, 510), label="Welcome to VAA Tool - Victoria State Road Crash Analysis System")
        font = joinText.GetFont()
        font.PointSize += 1
        joinText.SetFont(font)

        png = wx.Image('logo.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (10, 5), (png.GetWidth(), png.GetHeight()))



        def messageBox(self, event):
            # wx.MessageBox('Message Box Dialog Info Icon', 'Dialog', wx.OK | wx.ICON_INFORMATION)
            # wx.MessageBox('Message Box Dialog Warning Icon', 'Dialog', wx.OK | wx.ICON_WARNING)
            wx.MessageBox('Message Box Dialog Error Icon', 'Dialog', wx.OK | wx.ICON_ERROR)

        """
        b = wx.Button(self, -1, 'clic')
        self.panel_2 = Panel_2(self)
        self.panel_3 = Panel_3(self)

        s = wx.BoxSizer(wx.VERTICAL)
        s.Add(self.panel_2, -1, wx.EXPAND)
        s.Add(self.panel_3, 2, wx.EXPAND)

        root_sizer = wx.BoxSizer(wx.HORIZONTAL)
        root_sizer.Add(b, 0, flag=wx.LEFT, border=200)
        root_sizer.Add(s, 3, wx.EXPAND)
        self.SetSizer(root_sizer)
        """

        period_Button = wx.Button(self, pos=(10, 160), label="Time Analysis              	       ")
        period_Button.Bind(wx.EVT_BUTTON, self.onclic1)

        Hour_Button = wx.Button(self, pos=(10, 200), label="Hourly Analysis                     ")
        Hour_Button.Bind(wx.EVT_BUTTON, self.onclic2)

        keyword_Button = wx.Button(self, pos=(10, 240), label="Accident Analysis by Keyword   ")
        keyword_Button.Bind(wx.EVT_BUTTON, self.onclic3)

        alcohol_Button = wx.Button(self, pos=(10, 280), label="Alcohol Impact Analysis          ")
        alcohol_Button.Bind(wx.EVT_BUTTON, self.onclic4)

        geographic_Button = wx.Button(self, pos=(10, 320), label="Geographic Impact Analysis     ")
        geographic_Button.Bind(wx.EVT_BUTTON, self.onclic5)

        # sizer_v.Add(self.button1, 0, flag=wx.LEFT, border=200)

        """
        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")

        """

    def onclic1(self, e):
        self.panel_3 = Panel_1(self)
        # self.panel_2.text.SetValue('hello')

        # self.panel_3 = Panel_3(self)

    def onclic2(self, e):
        self.panel_3 = Panel_1(self)
        # self.panel_2.text.SetValue('hello')

        # self.panel_3 = Panel_3(self)

    def onclic3(self, e):
        self.panel_3 = Panel_2(self)
        # self.panel_2.text.SetValue('hello')

        # self.panel_3 = Panel_3(self)

    def onclic4(self, e):
        self.panel_3 = Panel_2(self)
        # self.panel_2.text.SetValue('hello')

        # self.panel_3 = Panel_3(self)

    def onclic5(self, e):
        self.panel_3 = Panel_2(self)
        # self.panel_2.text.SetValue('hello')

        # self.panel_3 = Panel_3(self)


class Panel_2(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.SetSize((400, 400))
        self.Centre()
        # self.SetTitle('wx.Button')

        self.SetBackgroundColour(wx.LIGHT_GREY)
        # self.text = wx.TextCtrl(self, pos=(10,10))


class Panel_1(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(wx.LIGHT_GREY)

        self.SetSize((400, 400))
        self.Centre()

        self.figure = Figure()

        period_Button = wx.Button(self, pos=(10, 160), label="Time Analysis")
        period_Button.Bind(wx.EVT_BUTTON, self.onclic1)

        # main2 = alcoholAnalysis()
        # new_list = [i["SEVERITY"] for i in main2]
        counts = {}
        new_list = ['Other injury accident', 'Serious injury accident', 'Fatal accident', 'Other injury accident',
                    'Serious injury accident',
                    'Fatal accident', 'Other injury accident', 'Serious injury accident', 'Fatal accident']

        for i in new_list:
            counts[i] = (counts[i] + 1) if (i in counts) else 1

        # Data to plot
        labels = []
        sizes = []

        for x, y in counts.items():
            labels.append(x)
            sizes.append(y)

        # Plot
        fig, ax1 = plt.subplots()
        explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)

        ax1.axis('equal')
        plt.show()



class MainFrame(wx.Frame):

    # A Frame that says Hello World

    def __init__(self, *a, **k):
        # ensure the parent's __init__ is called
        wx.Frame.__init__(self, *a, **k)
        # self.initialise()
        Panel_root(self)

        self.Centre()
        self.SetSize((800, 600))
        # self.SetTitle('wx.Button')

    """

    def initialise(self):
        # create a panel in the frame
        self.Show(True)
        pnl = wx.Panel(self)
        self.Centre()


        self.SetSize((1000,800))
        #self.SetTitle('wx.Button')

        # and create a sizer to manage the layout of child widgets
        #sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(vaaText, wx.SizerFlags().Border(wx.TOP | wx.LEFT, 25))
        #self.SetSize(sizer)

        # put some text with a larger bold font on it
        vaaText = wx.StaticText(pnl, pos=(150, 10), label="Victoria Accident Analysis Tool")
        font = vaaText.GetFont()
        font.PointSize += 16
        font = font.Bold()
        vaaText.SetFont(font)

        # use a box sizer to lay out widgets
        sizer_v = wx.BoxSizer(wx.VERTICAL)
        # Add(widget, proportion, flag, border)
        # border is to the left side
        sizer_v.Add(self.button1, 0, flag=wx.LEFT, border=200)
        # this adds a spacer (w, h)
        # here only the height is important
        sizer_v.Add((0, 200), proportion=0, flag=wx.EXPAND)
        sizer_v.Add(self.button2, 0, flag=wx.LEFT, border=200)

        self.SetSizer(sizer_v)





        png = wx.Image('logo.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (10, 5), (png.GetWidth(), png.GetHeight()))

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")

    """

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                                    "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHome, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def OnHome(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK | wx.ICON_INFORMATION)


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MainFrame(None, title='VAA Tool')
    frm.Show()
    app.MainLoop()


