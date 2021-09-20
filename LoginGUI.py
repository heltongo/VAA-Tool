import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 400))
        # self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        # self.CreateStatusBar()  # A Statusbar in the bottom of the window
        self.initialise()

    def initialise(self):
        self.Show(True)
        pnl = wx.Panel(self,size=(600, 400))
        vaaText = wx.StaticText(pnl,  pos = (150,10), label = "Victoria Accident Analysis Tool")
        font = vaaText.GetFont()
        font.PointSize+=16
        font = font.Bold()
        vaaText.SetFont(font)

        joinText = wx.StaticText(pnl, pos = (180,60), label="Join")
        font = joinText.GetFont()
        font.PointSize += 12
        joinText.SetFont(font)

        line1Text = wx.StaticText(pnl, pos=(350, 50), label="|")
        font = line1Text.GetFont()
        font.PointSize += 24
        line1Text.SetFont(font)

        joinlineText = wx.StaticText(pnl, pos=(120, 65), label="__________")
        font = joinlineText.GetFont()
        font.PointSize += 24
        joinlineText.SetFont(font)

        signupText = wx.StaticText(pnl, pos = (430,60),label="Sign up")
        font = signupText.GetFont()
        font.PointSize += 12
        signupText.SetFont(font)

        signlineText = wx.StaticText(pnl, pos=(390, 65), label="__________")
        font = signlineText.GetFont()
        font.PointSize += 24
        signlineText.SetFont(font)

        emailText = wx.StaticText(pnl,pos = (120,120), label="Email")
        font = emailText.GetFont()
        font.PointSize += 10
        emailText.SetFont(font)

        #textbox pos should be 120.140

        passText = wx.StaticText(pnl,pos = (120,180), label="Password")
        font = passText.GetFont()
        font.PointSize += 10
        passText.SetFont(font)

        # textbox pos should be 120.200

        signinButton = wx.Button(pnl, pos=(320, 240), label="SIGN IN")

        forgotText = wx.StaticText(pnl,pos = (300,260), label="Forgot Password?")
        font = forgotText.GetFont()
        font.PointSize += 2
        forgotText.SetFont(font)

        altText = wx.StaticText(pnl, pos = (310,290),label="Or sign in with ...")
        font = altText.GetFont()
        font.PointSize += 1
        altText.SetFont(font)

        googleButton = wx.Button(pnl, pos=(200, 320), label="Google")
        yahooButton = wx.Button(pnl, pos=(410, 320), label="Yahoo")

app = wx.App(False)
frame = MainWindow(None, "VAA Tool")
app.MainLoop()



# Setting up the menu.
#   filemenu = wx.Menu()  # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
#   filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
#   filemenu.AppendSeparator()
#   filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")
#   # Creating the menubar.
#   menuBar = wx.MenuBar()
#   menuBar.Append(filemenu, "&File")  # Adding the "filemenu" to the MenuBar
#   self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
#   self.Show(True)

# def OnButtonClick(self, event):
#         # if (some_condition):
#         #     do_something()
#         # else:
#     event.Skip()
#     # A button
#     self.button = wx.Button(self, label="Save", pos=(200, 325))
#     self.Bind(wx.EVT_BUTTON, self.OnButtonClick, self.button)
#     wx.Button(self, -1, "Button")
#     self.SetBackgroundColour("blue")

# app = wx.App(False) # Next, create an application object.
# # frm = wx.Frame(None, wx.ID_ANY, title="VAA Tool") # Then a frame.
# frm.Show() # Show it.