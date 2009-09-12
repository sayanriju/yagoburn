#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx

class WIPDialog(wx.Dialog):
	''' A Class to both run a command and show a dialog while it runs; "returns" exitcode, errolog and successlog '''
	def __init__(self, *args, **kwds):
		self.cmd=args[0]
		args=args[1:-1]
		## Stuff to "return"
		self.exitcode=1
		self.errorlog=''
		self.successlog=''
		
		self.count=0
		# begin wxGlade: MyDialog.__init__
		kwds["style"] = wx.DEFAULT_DIALOG_STYLE
		wx.Dialog.__init__(self, *args, **kwds)
		self.bitmap_1 = wx.StaticBitmap(self, -1, wx.Bitmap("/home/sayan/yagoburn/icons/wip.png", wx.BITMAP_TYPE_ANY))
		self.label_1 = wx.StaticText(self, -1, "Please wait a little more...  ", style=wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE)
		self.label_2 = wx.StaticText(self, -1, "<<<>>>", style=wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE)
		self.bar = wx.Gauge(self, -1, 100, style=wx.GA_HORIZONTAL|wx.GA_SMOOTH)
		self.button_1 = wx.Button(self, wx.ID_STOP, "")

		self.__set_properties()
		self.__do_layout()
		# end wxGlade
		self.button_1.Bind(wx.EVT_BUTTON, self.OnStop)
		self.Bind(wx.EVT_TIMER, self.BarHandler)
		self.timer = wx.Timer(self)
		self.timer.Start(100) 
		self.RunCommand()
		

	def __set_properties(self):
		# begin wxGlade: MyDialog.__set_properties
		self.SetTitle("Work In Progress...")
		self.label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
		self.bar.SetMinSize((350, 37))
		# end wxGlade
	# self.bar.Pulse()

	def __do_layout(self):
		# begin wxGlade: MyDialog.__do_layout
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_3 = wx.BoxSizer(wx.VERTICAL)
		sizer_2.Add(self.bitmap_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 7)
		sizer_3.Add(self.label_1, 0, wx.ALL, 11)
		sizer_3.Add(self.label_2, 0, wx.ALL, 7)
		sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
		sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
		sizer_1.Add(self.bar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 11)
		sizer_1.Add(self.button_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 11)
		self.SetSizer(sizer_1)
		sizer_1.Fit(self)
		self.Layout()
		# end wxGlade

	def BarHandler(self, event):
		self.count = self.count + 1
	
		if self.count >= 50:
			self.count = 0
	
		self.bar.Pulse()
		self.proc.poll()
		if self.proc.returncode != None:
			self.bar.SetValue(100)
			if self.proc.returncode :
				self.exitcode=1
				self.errorlog=self.proc.communicate()[1]
			else:
				self.exitcode=0
				self.successlog=self.proc.communicate()[0]
			self.Close()
				
	
	
	def OnStop(self,event):
		self.Close()
	
	def RunCommand(self):
		cmdlist=self.cmd.split(' ')
		from subprocess import Popen,PIPE
		self.proc=Popen(cmdlist,stdout=PIPE)
		#proc.wait()
		#print 'DONE'

# end of class MyDialog



class MsgWithLogDialog(wx.Dialog):
    def __init__(self,  *args, **kwds):
        self.title=args[0]
        heading=args[1]
        msg=args[2]
        icon=args[3]
        args=args[4:-1]
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.bitmap_1 = wx.StaticBitmap(self, -1, wx.Bitmap(icon, wx.BITMAP_TYPE_ANY))
        self.label_1 = wx.StaticText(self, -1, heading, style=wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE)
        self.label_2 = wx.StaticText(self, -1, msg, style=wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE)
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL|wx.TE_LINEWRAP)
        self.button_1 = wx.Button(self, wx.ID_SAVE, "")
        self.button_2 = wx.Button(self, wx.ID_CLOSE, "")

        self.__set_properties()
        self.__do_layout()
        
        self.button_1.Bind(wx.EVT_BUTTON,self.OnSave)
        self.button_2.Bind(wx.EVT_BUTTON,self.OnClose)

    def __set_properties(self):
        self.SetTitle(self.title)
        self.label_1.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_ctrl_1.SetMinSize((386, 200))
        self.button_1.SetToolTipString("Save this log")

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.bitmap_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 23)
        sizer_3.Add(self.label_1, 1, wx.TOP|wx.EXPAND, 13)
        sizer_3.Add(self.label_2, 0, wx.ALL, 11)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add(self.text_ctrl_1, 0, wx.ALL|wx.EXPAND|wx.SHAPED, 7)
        sizer_4.Add(self.button_1, 0, wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 11)
        sizer_4.Add(self.button_2, 0, wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_1.Add(sizer_4, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        
    def OnSave(self, event):
        from os.path import expanduser
        dialog = wx.FileDialog( None, message = 'Select location to save this log:', wildcard="Any File (*.*) | *.*", defaultDir=expanduser('~/'),  style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT )
        if dialog.ShowModal() == wx.ID_OK:
            selected = dialog.GetPath()
        dialog.Destroy()     
        try:
            f = open(selected, 'w') 
            f.write(self.text_ctrl_1.GetValue())
            f.close()
        except IOError:
            dial=wx.MessageDialog(None, "Unable to save file on location {0}\n\nCheck  permissons!'".format(selected[0]), 'Error Saving File!', wx.OK | wx.ICON_ERROR)
            dial.ShowModal()
            dial.Destroy()
    
    def OnClose(self, event):
        self.Close()
    
    def GetLog(self):
        return self.text_ctrl_1.GetValue()
    
    def SetLog(self, txt):
        self.text_ctrl_1.SetValue(txt)
#        
#
##
#import wx        
#app=wx.App()
#d=WIPDialog('seq 1 10',None,-1,'')
#d.ShowModal()
#print d.successlog
#d.Destroy()
#app.MainLoop()