#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: customwidgets.py

#       This file is part of Yagoburn, which is FREE software; 
#		you can redistribute it and/or modify it under the terms of 
#		the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA
#
#		Copyright 2009-10 Sayan "Riju" Chakrabarti <me@sayanriju.co.cc>


import wx

class WIPDialog(wx.Dialog):
	''' A Class to both run a command and show a dialog while it runs; "returns" exitcode, errolog and successlog 
	exitcode=0 on success, 1 on failure, -1 on forced kill
	errorlog='' on succes, the actual log on failure, '' on forced kill
	successlog= the actual log on success, '' on failure and forced kill '''
	def __init__(self, *args, **kwds):
		self.cmd=args[0]
		args=args[1:]
		## Stuff to "return"
		self.exitcode=1
		self.errorlog=''
		self.successlog=''
		
		self.count=0
		# begin wxGlade: MyDialog.__init__
		kwds["style"] = wx.DEFAULT_DIALOG_STYLE
		wx.Dialog.__init__(self, *args, **kwds)
		self.bitmap_1 = wx.StaticBitmap(self, -1, wx.Bitmap("icons/wip.png", wx.BITMAP_TYPE_ANY))
		self.label_1 = wx.StaticText(self, -1, "Please wait a little more...  ", style=wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE)
		self.label_2 = wx.StaticText(self, -1, "Now running command: \"{0}\"".format(self.cmd), style=wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE)
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
		if self.proc.returncode != None:	# Process completed
			self.timer.Stop()
			self.bar.SetValue(100)
			self.exitcode=self.proc.returncode
			try:
				logs=self.proc.communicate()
			except ValueError:
				pass ## ??????????????
			self.successlog=logs[0]
			self.errorlog=logs[1]
			self.Close()
				
	
	
	def OnStop(self,event):
		d=wx.MessageDialog(None, "Are you sure you want to stop the process  \"{0}\" running with PID {1}?\n\n(It is still running in the background while you decide!)".format(self.cmd,self.proc.pid),'Confirm Kill', wx.YES_NO|wx.ICON_QUESTION)
		if d.ShowModal()== wx.ID_YES:
			try:
				self.proc.kill()
			except OSError:
				print("Could not kill PID {0}".format(self.proc.pid))	# for debugging only
			self.exitcode=-1
			self.errorlog=''
			self.successlog=''
			self.Close()
		d.Destroy()
	
	def RunCommand(self):
		cmdlist=self.cmd.split(' ')
		cmdlist=[cmd for cmd in cmdlist if cmd!=''] # remove '' from list
		cmdlist=[cmd.replace('*',' ') for cmd in cmdlist] # to retrieve spaces in volname
		from subprocess import Popen,PIPE
		self.proc=Popen(cmdlist,stdout=PIPE,stderr=PIPE)

# end of class MyDialog



class MsgWithLogDialog(wx.Dialog):
	def __init__(self,  *args, **kwds):
		self.title=args[0]
		heading=args[1]
		msg=args[2]
		icon=args[3]
		args=args[4:]
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
			dial=wx.MessageDialog(None, "Unable to save log file on location {0}\n\nCheck  permissons!'".format(selected[0]), 'Error Saving File!', wx.OK | wx.ICON_ERROR)
			dial.ShowModal()
			dial.Destroy()
	
	def OnClose(self, event):
		self.Close()
	
	def GetLog(self):
		return self.text_ctrl_1.GetValue()
	
	def SetLog(self, txt):
		self.text_ctrl_1.SetValue(txt)

