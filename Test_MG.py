import wx

class calcframe(wx.frame):

    def __init__(self):
        super().__init__(
            none, title="wxcalculator",
            size=(350, 375))
        panel = calcpanel(self)
        self.setsizehints(350, 375, 350, 375)
        self.show()


if __name__ == '__main__':
    app = wx.app(false)
    frame = calcframe()
    app.mainloop()