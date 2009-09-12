#!/usr/bin/env python
#coding=utf-8

def FormatSize(size):
	if size<1024:
		return "{0:.2f} B".format(size)
	elif size<1024**2:
		return "{0:.2f} KB".format(size/(1024.0))
	elif size<1024**3:
		return "{0:.2f} MB".format(size/(1024.0**2))		
	else:
		return "{0:.2f} GB".format(size/(1024.0**3))
	
def GetDirectorySize(directory):
	import os
	dir_size = 0
	for (path, dirs, files) in os.walk(directory):
		for file in files:
			filename = os.path.join(path, file)
			dir_size += os.path.getsize(filename)
	return dir_size

def AddFileDialog(header,filters):
	import wx,os
	#filters = 'All files (*.*)|*.*|Text files (*.txt)|*.txt'
	selected=[]
	
	dialog = wx.FileDialog ( None, message = header, defaultDir=os.path.expanduser('~/'),  wildcard = filters, style = wx.FD_OPEN | wx.FD_MULTIPLE )
	
	if dialog.ShowModal() == wx.ID_OK:
	   selected = dialog.GetPaths()
	dialog.Destroy()
	
	return selected

def AddDirDialog(header):
	import wx,os
	selected=[]
	dialog = wx.DirDialog( None, message = header, defaultPath=os.path.expanduser('~/'),  style = wx.FD_OPEN | wx.FD_MULTIPLE )
	if dialog.ShowModal() == wx.ID_OK:
	   selected = dialog.GetPath()
	dialog.Destroy()
	
	return selected	

def GetIsoDialog():
	import wx,os
	dialog = wx.FileDialog(None, message="Select Iso file to burn: ", defaultDir=os.path.expanduser('~/'),wildcard="Iso files (*.iso)|*.iso", style= wx.FD_OPEN)
	if dialog.ShowModal() == wx.ID_OK:
	   selected = dialog.GetPaths()
	dialog.Destroy()
	
	return selected	
	
def SaveIsoDialog():
	import wx,os,fnmatch
	dialog = wx.FileDialog( None, message = 'Select location to save iso file:', wildcard="ISO Files (*.iso)|*.iso", defaultDir=os.path.expanduser('~/'),  style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT )
	if dialog.ShowModal() == wx.ID_OK:
		selected = dialog.GetPath()
	dialog.Destroy()
	if not fnmatch.fnmatch(selected,'*.iso'):
		selected += '.iso'
		
	return selected	
	
def ShowGenericMsgDialog(title,type,msg):
	''' Shows a generic wx dialog
	 type is either 'error' or 'info' '''
	import wx
	if type == 'info':
		dialog = wx.MessageDialog(None, msg, title, wx.OK | wx.ICON_INFORMATION)
	elif type == 'error':
		dialog = wx.MessageDialog(None, msg, title,wx.OK | wx.ICON_ERROR)
	dialog.ShowModal()
	dialog.Destroy()	

def ShowErrorWithLogDialog(logtext):
	import wx
	import customwidgets as cw
	d=cw.MsgWithLogDialog('Error!','Something went wrong!','(Viewing the logs below might be helpful)','icons/errormsg.png', None,-1,'')
	d.SetLog(logtext)
	d.ShowModal()
	d.Destroy()
		
	
def ShowDeviceProp(device):
	if device=='':
		ShowGenericMsgDialog('Error!','error','Choose a device first!')
		return
	import subprocess as sp
	proc=sp.Popen(['wodim','dev={0}'.format(device),'driveropts=help', '-checkdrive'],stdout=sp.PIPE,stderr=sp.PIPE)
	exitcode=proc.wait()
	print exitcode
	if exitcode == 0:
		ShowGenericMsgDialog('Properties for {0}'.format(device),'info',proc.communicate()[0])
	else:
		#ShowGenericMsgDialog('Properties for {0}'.format(device),'error',proc.communicate()[1])
		ShowErrorWithLogDialog(proc.communicate()[1])
	
	return
		
		
def ClearCdRoot(CDROOT):
	import os
	os.system('rm -rf {0}'.format(CDROOT))

def CreateCdRoot(CDROOT,lst):
	import os
	os.makedirs(CDROOT)
	for f in lst:
		os.system('ln -s {0} {1}/'.format(f,CDROOT))

#import wx
#app=wx.App()
#ShowErrorWithLogDialog('bababab')
#app.MainLoop()
