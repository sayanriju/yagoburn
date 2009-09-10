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

def AddFileDialog(header,filters):
	import wx
	application = wx.PySimpleApp()
	#filters = 'All files (*.*)|*.*|Text files (*.txt)|*.txt'
	selected=[]
	
	dialog = wx.FileDialog ( None, message = header, wildcard = filters, style = wx.OPEN | wx.MULTIPLE )
	
	if dialog.ShowModal() == wx.ID_OK:
	   selected = dialog.GetPaths()
	dialog.Destroy()
	
	return selected

def ClearCdRoot(CDROOT):
	import os
	os.system('rm -rf {0}'.format(CDROOT))

def CreateCdRoot(CDROOT,lst):
	import os
	os.makedirs(CDROOT)
	for f in lst:
		os.system('ln -s {0} {1}/'.format(f,CDROOT))