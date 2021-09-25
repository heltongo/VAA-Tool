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

        emailText = wx.StaticText(pnl,pos = (120,110), label="Email")
        font = emailText.GetFont()
        font.PointSize += 10
        emailText.SetFont(font)

        email = wx.TextCtrl(pnl, pos = (120,140), size = (475,30))
        #textbox pos should be 120.140

        passText = wx.StaticText(pnl,pos = (120,170), label="Password")
        font = passText.GetFont()
        font.PointSize += 10
        passText.SetFont(font)

        password = wx.TextCtrl(pnl, pos=(120, 200), size = (475,30))
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

        googleButton = wx.Button(pnl, pos=(150, 320), label="Google", size = (200,50))
        yahooButton = wx.Button(pnl, pos=(370, 320), label="Yahoo", size = (200,50))

app = wx.App(False)
frame = MainWindow(None, "VAA Tool")
app.MainLoop()

