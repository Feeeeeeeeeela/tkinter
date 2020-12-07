import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super().__init__(parent, title =title, size = size)
        self.panel = MyPanel(self)
        self.SetSizeHints(470,300)
        

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.Gui()

    def Gui(self):
        mainsizer = wx.BoxSizer(wx.VERTICAL)

        textsizer = wx.BoxSizer(wx.HORIZONTAL)
        
        textsizer.Add(wx.StaticText(self, label="Red:"),1)
        textsizer.Add(wx.StaticText(self, label="Green:"),1)
        textsizer.Add(wx.StaticText(self, label="Blue:"),1)

        sidesizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.first = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=255)
        self.second = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=255)
        self.third = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=255)

        sidesizer.Add(self.first,1)
        sidesizer.Add(self.second,1)
        sidesizer.Add(self.third,1)

        self.cpnl  = wx.Panel(self)
        self.cpnl.SetBackgroundColour("black")

        btnsizer = wx.BoxSizer(wx.VERTICAL)

        btn = wx.Button(self, label='Change Color')
        self.Bind(wx.EVT_BUTTON, self.onpress, btn)
        self.idhex = wx.TextCtrl(self, value="#000000", style=wx.TE_CENTRE)

        btnsizer.Add(btn, 1, wx.EXPAND)
        btnsizer.Add(self.idhex, 0, wx.EXPAND)

        mainsizer.Add(textsizer, 0, wx.EXPAND)
        mainsizer.Add(sidesizer, 0, wx.EXPAND)
        mainsizer.Add(self.cpnl, 2, wx.EXPAND)
        mainsizer.Add(btnsizer, 1, wx.EXPAND)
        self.SetSizer(mainsizer)

    def onpress(self, event):
        rn = self.first.GetValue()
        gn = self.second.GetValue()
        bn = self.third.GetValue()
        hexnumber = '#%02x%02x%02x' % (rn, gn, bn)
        self.cpnl.SetBackgroundColour(hexnumber)
        self.cpnl.Refresh()
        self.idhex.SetValue(hexnumber)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Color mixer", size = (470,250))
        self.frame.Show()
        return True

if __name__ == "__main__":
    app=MyApp()
    app.MainLoop()