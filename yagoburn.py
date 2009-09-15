#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: yagoburn.py

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
import os,fnmatch
import functions as fun

CDROOT='/tmp/cdroot'
TMPISO='/tmp/yagoburn.iso'

write_speeds=['Default Speed']
for i in range(52,1,-2):
	write_speeds.append("{0}x".format(i))

dvd_devices=[]
cd_devices=[]
for d in os.listdir('/dev/'):
	if fnmatch.fnmatch(d,'*dvdr*'):
		dvd_devices.append("/dev/"+d)
	elif fnmatch.fnmatch(d,'*cdr*'):
		cd_devices.append("/dev/"+d)

# begin wxGlade: extracode
# end wxGlade



class MyFrame(wx.Frame):
	def __init__(self):
		self.audio_files_to_burn=[]
		self.data_files_to_burn=[]
		self.dvd_files_to_burn=[]
		
		# begin wxGlade: MyFrame.__init__
		#kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, None, wx.ID_ANY)
		self.notebook_top = wx.Notebook(self, 1, style=wx.NB_LEFT)
		self.other_op_pane = wx.Panel(self.notebook_top, 40)
		self.notebook_other_op = wx.Notebook(self.other_op_pane, -1, style=0)
		self.burn_iso = wx.Panel(self.notebook_other_op, -1)
		self.blank_disk = wx.Panel(self.notebook_other_op, -1)
		self.data_dvd_pane = wx.Panel(self.notebook_top, 30)
		self.notebook_data_dvd = wx.Notebook(self.data_dvd_pane, -1, style=0)
		self.data_dvd_settings = wx.Panel(self.notebook_data_dvd)
		self.data_dvd = wx.Panel(self.notebook_data_dvd, -1)
		self.data_cd_pane = wx.Panel(self.notebook_top, 20)
		self.notebook_data_cd = wx.Notebook(self.data_cd_pane, -1, style=0)
		self.data_cd_settings = wx.Panel(self.notebook_data_cd)
		self.data_cd = wx.Panel(self.notebook_data_cd, -1)
		self.audio_cd_pane = wx.Panel(self.notebook_top, 10)
		self.notebook_audio_cd = wx.Notebook(self.audio_cd_pane, -1, style=0)
		self.audio_cd_settings = wx.Panel(self.notebook_audio_cd)
		self.audio_cd = wx.Panel(self.notebook_audio_cd, 11)
		self.sizer_10_staticbox = wx.StaticBox(self.data_cd, -1, "Files/Directories to Burn")
		self.sizer_10_copy_staticbox = wx.StaticBox(self.data_dvd, -1, "Files/Directories to Burn")
		self.sizer_15_staticbox = wx.StaticBox(self.audio_cd, -1, "Tracks to Add (.wav files only)")
		self.audio_file_list = wx.ListBox(self.audio_cd, -1, choices=[])
		self.audio_totalsize_entry = wx.TextCtrl(self.audio_cd, -1, "", style=wx.TE_READONLY)
		self.audio_gauge = wx.Gauge(self.audio_cd, -1, 100)
		self.audio_size_list = wx.ComboBox(self.audio_cd, 201, choices=["180 MB", "202 MB", "650 MB", "700 MB", "790 MB", "869 MB", "878 MB"], style=wx.CB_DROPDOWN|wx.CB_SORT|wx.CB_READONLY)
		self.panel_2 = wx.Panel(self.audio_cd, -1)
		self.add_track_button = wx.Button(self.audio_cd, wx.ID_ADD, "")
		self.remove_track_button = wx.Button(self.audio_cd, wx.ID_REMOVE, "")
		self.panel_3 = wx.Panel(self.audio_cd, -1)
		self.audio_next_button = wx.Button(self.audio_cd, wx.ID_FORWARD, "")
		self.label_device_1 = wx.StaticText(self.audio_cd_settings, -1, "Device to write : ", style=wx.ST_NO_AUTORESIZE)
		self.audio_device_list = wx.ComboBox(self.audio_cd_settings, -1, choices=cd_devices, style=wx.CB_DROPDOWN)
		self.audio_devprop_button = wx.Button(self.audio_cd_settings, wx.ID_PROPERTIES, "")
		self.label_speed_1 = wx.StaticText(self.audio_cd_settings, -1, "Write Speed :      ", style=wx.ST_NO_AUTORESIZE)
		self.audio_speed_list = wx.ComboBox(self.audio_cd_settings, -1, choices=write_speeds, style=wx.CB_DROPDOWN)
		self.audio_mode_radiobox = wx.RadioBox(self.audio_cd_settings, -1, "Write Mode : ", choices=["DAO (No pause between tracks)", "TAO"], majorDimension=2, style=wx.RA_SPECIFY_COLS)
		self.audio_simulate_check = wx.CheckBox(self.audio_cd_settings, -1, "Simulate Write (-dummy)")
		self.audio_nofix_check = wx.CheckBox(self.audio_cd_settings, -1, "Do NOT Fixate CD (-nofix)")
		self.panel_7 = wx.Panel(self.audio_cd_settings, -1)
		self.audio_burn_button = wx.BitmapButton(self.audio_cd_settings, -1, wx.Bitmap("icons/burn.png", wx.BITMAP_TYPE_ANY), style=wx.BU_AUTODRAW)
		self.panel_4 = wx.Panel(self.audio_cd_settings, -1)
		self.data_file_list = wx.ListBox(self.data_cd, -1, choices=[])
		self.data_totalsize_entry = wx.TextCtrl(self.data_cd, -1, "", style=wx.TE_READONLY)
		self.data_gauge = wx.Gauge(self.data_cd, -1, 100)
		self.data_size_list = wx.ComboBox(self.data_cd, 202, choices=["180 MB", "202 MB", "650 MB", "700 MB", "790 MB", "869 MB", "878 MB"], style=wx.CB_DROPDOWN|wx.CB_SORT|wx.CB_READONLY)
		self.panel_6 = wx.Panel(self.data_cd, -1)
		self.data_addfile_button = wx.Button(self.data_cd, wx.ID_ADD, "")
		self.data_adddir_button = wx.Button(self.data_cd, wx.ID_ADD, "Add Directory")
		#self.data_adddir_button = GenBitmapTextButton(self.data_cd, -1, wx.Bitmap("icons/add-dir.png", wx.BITMAP_TYPE_ANY),"Add Directory")
		self.data_remove_button = wx.Button(self.data_cd, wx.ID_REMOVE, "")
		self.data_clear_button = wx.Button(self.data_cd, wx.ID_CLEAR, "")
		self.panel_5 = wx.Panel(self.data_cd, -1)
		self.data_next_button = wx.Button(self.data_cd, wx.ID_FORWARD, "")
		self.data_volume_label = wx.StaticText(self.data_cd_settings, -1, "Volume Name :      ", style=wx.ST_NO_AUTORESIZE)
		self.data_volname_entry = wx.TextCtrl(self.data_cd_settings, -1, "Yagoburn CD")
		self.label_2_copy_1 = wx.StaticText(self.data_cd_settings, -1, "Device to write : ", style=wx.ST_NO_AUTORESIZE)
		self.data_device_list = wx.ComboBox(self.data_cd_settings, -1, choices=cd_devices, style=wx.CB_DROPDOWN)
		self.data_devprop_button = wx.Button(self.data_cd_settings, wx.ID_PROPERTIES, "")
		self.label_2_copy_copy = wx.StaticText(self.data_cd_settings, -1, "Write Speed :      ", style=wx.ST_NO_AUTORESIZE)
		self.data_speed_list = wx.ComboBox(self.data_cd_settings, -1, choices=write_speeds, style=wx.CB_DROPDOWN)
		self.data_mode_radiobox = wx.RadioBox(self.data_cd_settings, -1, "Write Mode : ", choices=["DAO", "TAO"], majorDimension=2, style=wx.RA_SPECIFY_COLS)
		self.data_onlyiso_check = wx.CheckBox(self.data_cd_settings, 101, "Only create ISO file")
		self.data_isopath_entry = wx.TextCtrl(self.data_cd_settings, -1, "")
		self.data_isosel_button = wx.Button(self.data_cd_settings, wx.ID_SAVE, "")
		self.data_multi_check = wx.CheckBox(self.data_cd_settings, -1, "Start or Continue Multi-session")
		self.data_simulate_check = wx.CheckBox(self.data_cd_settings, -1, "Simulate Write (-dummy)")
		self.data_nofix_check = wx.CheckBox(self.data_cd_settings, -1, "Disable Burnfree")
		self.panel_7_copy = wx.Panel(self.data_cd_settings, -1)
		self.data_burn_button = wx.BitmapButton(self.data_cd_settings, -1, wx.Bitmap("icons/burn.png", wx.BITMAP_TYPE_ANY), style=wx.BU_AUTODRAW)
		self.panel_4_copy = wx.Panel(self.data_cd_settings, -1)
		self.dvd_file_list = wx.ListBox(self.data_dvd, -1, choices=[])
		self.dvd_totalsize_entry = wx.TextCtrl(self.data_dvd, -1, "", style=wx.TE_READONLY)
		self.dvd_gauge = wx.Gauge(self.data_dvd, -1, 100)
		self.dvd_size_list = wx.ComboBox(self.data_dvd, 203, choices=["4.7 GB", "8.5 GB", "9.4 GB"], style=wx.CB_DROPDOWN|wx.CB_SORT|wx.CB_READONLY)
		self.panel_6_copy = wx.Panel(self.data_dvd, -1)
		self.dvd_addfile_button = wx.Button(self.data_dvd, wx.ID_ADD, "")
		self.dvd_adddir_button = wx.Button(self.data_dvd, wx.ID_ADD, "Add Directory")
		self.dvd_remove_button = wx.Button(self.data_dvd, wx.ID_REMOVE, "")
		self.dvd_clear_button = wx.Button(self.data_dvd, wx.ID_CLEAR, "")
		self.panel_5_copy = wx.Panel(self.data_dvd, -1)
		self.dvd_next_button = wx.Button(self.data_dvd, wx.ID_FORWARD, "")
		self.dvd_volname_label = wx.StaticText(self.data_dvd_settings, -1, "Volume Name :      ", style=wx.ST_NO_AUTORESIZE)
		self.dvd_volname_entry = wx.TextCtrl(self.data_dvd_settings, -1, "Yagoburn DVD")
		self.label_2_copy_1_copy = wx.StaticText(self.data_dvd_settings, -1, "Device to write : ", style=wx.ST_NO_AUTORESIZE)
		self.dvd_device_list = wx.ComboBox(self.data_dvd_settings, -1, choices=dvd_devices, style=wx.CB_DROPDOWN)
		self.dvd_devprop_button = wx.Button(self.data_dvd_settings, wx.ID_PROPERTIES, "")
		self.dvd_label_2 = wx.StaticText(self.data_dvd_settings, -1, "Write Speed :      ", style=wx.ST_NO_AUTORESIZE)
		self.dvd_speed_list = wx.ComboBox(self.data_dvd_settings, -1, choices=write_speeds, style=wx.CB_DROPDOWN)
		self.dvd_onlyiso_check = wx.CheckBox(self.data_dvd_settings, 102, "Only create ISO file")
		self.dvd_isopath_entry = wx.TextCtrl(self.data_dvd_settings, -1, "")
		self.dvd_isosel_button = wx.Button(self.data_dvd_settings, wx.ID_SAVE, "")
		self.dvd_multi_check = wx.CheckBox(self.data_dvd_settings, -1, "Start or Continue Multi-session")
		self.dvd_simulate_check = wx.CheckBox(self.data_dvd_settings, -1, "Dry Run")
		#self.dvd_nofix_check = wx.CheckBox(self.data_dvd_settings, -1, "Do NOT Fixate DVD")
		self.panel_7_copy_copy = wx.Panel(self.data_dvd_settings, -1)
		self.dvd_burn_button = wx.BitmapButton(self.data_dvd_settings, -1, wx.Bitmap("icons/burn.png", wx.BITMAP_TYPE_ANY), style=wx.BU_AUTODRAW)
		self.panel_4_copy_copy = wx.Panel(self.data_dvd_settings, -1)
		self.label_device_1_copy = wx.StaticText(self.blank_disk, -1, "Target Device : ", style=wx.ST_NO_AUTORESIZE)
		self.format_device_list = wx.ComboBox(self.blank_disk, -1, choices=cd_devices+dvd_devices, style=wx.CB_DROPDOWN)
		self.format_devprop_button = wx.Button(self.blank_disk, wx.ID_PROPERTIES, "")
		self.quickblankcd_button_copy = wx.Button(self.blank_disk,501, "Quick Blank CDRW")
		self.formatdvd_button_copy = wx.Button(self.blank_disk,502, "Format DVDRW")
		self.fullblankcd_button_copy = wx.Button(self.blank_disk,503, "Full Blank CDRW")
		self.justfixate_button_copy = wx.Button(self.blank_disk,504, "Just Fixate Disk")
		self.label_1 = wx.StaticText(self.burn_iso, -1, "Choose ISO File to burn : ", style=wx.ST_NO_AUTORESIZE)
		self.burn_isopath_entry = wx.TextCtrl(self.burn_iso, -1, "")
		self.burn_isosel_button = wx.Button(self.burn_iso, wx.ID_OPEN, "")
		self.label_2_copy_1_copy_1 = wx.StaticText(self.burn_iso, -1, "Device to write : ", style=wx.ST_NO_AUTORESIZE)
		self.burniso_device_list = wx.ComboBox(self.burn_iso, -1, choices=cd_devices+dvd_devices, style=wx.CB_DROPDOWN)
		self.burniso_devprop_button = wx.Button(self.burn_iso, wx.ID_PROPERTIES, "")
		self.label_2_copy_copy_copy = wx.StaticText(self.burn_iso, -1, "Write Speed :      ", style=wx.ST_NO_AUTORESIZE)
		self.burniso_speed_list = wx.ComboBox(self.burn_iso, -1, choices=write_speeds, style=wx.CB_DROPDOWN)
		self.burniso_mode_radiobox = wx.RadioBox(self.burn_iso, -1, "Write Mode : ", choices=["DAO", "TAO"], majorDimension=2, style=wx.RA_SPECIFY_COLS)
		self.burniso_simulate_check = wx.CheckBox(self.burn_iso, -1, "Simulate Write (-dummy)")
		self.burniso_nofix_check = wx.CheckBox(self.burn_iso, -1, "Disable Burnfree")
		self.panel_7_copy_copy_1 = wx.Panel(self.burn_iso, -1)
		self.burniso_burn_button = wx.BitmapButton(self.burn_iso, -1, wx.Bitmap("icons/burn.png", wx.BITMAP_TYPE_ANY), style=wx.BU_AUTODRAW)
		self.panel_4_copy_copy_1 = wx.Panel(self.burn_iso, -1)

		self.__set_properties()
		self.__do_layout()
		
########## Event Bindings ###############
		self.add_track_button.Bind(wx.EVT_BUTTON, self.AddAudioTrack)
		self.remove_track_button.Bind(wx.EVT_BUTTON, self.RemoveAudioTrack)
		self.audio_next_button.Bind(wx.EVT_BUTTON, self.GoToAudioSettingsTab)
		self.audio_devprop_button.Bind(wx.EVT_BUTTON, self.ShowAudioDeviceProp)
		self.audio_burn_button.Bind(wx.EVT_BUTTON, self.OnBurnAudio)
		self.data_addfile_button.Bind(wx.EVT_BUTTON, self.AddDataFile)
		self.data_adddir_button.Bind(wx.EVT_BUTTON, self.AddDataDir)
		self.data_remove_button.Bind(wx.EVT_BUTTON, self.RemoveDataFile)
		self.data_clear_button.Bind(wx.EVT_BUTTON, self.ClearDataList)
		self.data_next_button.Bind(wx.EVT_BUTTON, self.GoToDataSettingsTab)
		self.data_devprop_button.Bind(wx.EVT_BUTTON, self.ShowDataDeviceProp)
		self.data_onlyiso_check.Bind(wx.EVT_CHECKBOX, self.CheckOnlyCreateIso)
		self.data_isosel_button.Bind(wx.EVT_BUTTON, self.SelectDataIsoSaveLocation)
		self.data_burn_button.Bind(wx.EVT_BUTTON, self.OnBurnData)
		self.dvd_addfile_button.Bind(wx.EVT_BUTTON, self.AddDvdFile)
		self.dvd_adddir_button.Bind(wx.EVT_BUTTON, self.AddDvdDir)
		self.dvd_remove_button.Bind(wx.EVT_BUTTON, self.RemoveDvdFile)
		self.dvd_clear_button.Bind(wx.EVT_BUTTON, self.ClearDvdList)
		self.dvd_next_button.Bind(wx.EVT_BUTTON, self.GoToDvdSettingsTab)
		self.dvd_devprop_button.Bind(wx.EVT_BUTTON, self.ShowDvdDeviceProp)
		self.dvd_onlyiso_check.Bind(wx.EVT_CHECKBOX, self.CheckOnlyCreateIso)
		self.dvd_isosel_button.Bind(wx.EVT_BUTTON, self.SelectDvdIsoSaveLocation)
		self.dvd_burn_button.Bind(wx.EVT_BUTTON, self.OnBurnDvd)
		self.format_devprop_button.Bind(wx.EVT_BUTTON, self.ShowFormatDeviceProp)
		self.quickblankcd_button_copy.Bind(wx.EVT_BUTTON, self.OnFormatStuff)
		self.formatdvd_button_copy.Bind(wx.EVT_BUTTON, self.OnFormatStuff)
		self.fullblankcd_button_copy.Bind(wx.EVT_BUTTON, self.OnFormatStuff)
		self.justfixate_button_copy.Bind(wx.EVT_BUTTON, self.OnFormatStuff)
		self.burn_isosel_button.Bind(wx.EVT_BUTTON, self.SelectIsoLocation)
		self.burniso_devprop_button.Bind(wx.EVT_BUTTON, self.ShowBurnisoDeviceProp)
		self.burniso_burn_button.Bind(wx.EVT_BUTTON, self.OnBurnIso)
		
		self.audio_size_list.Bind(wx.EVT_COMBOBOX, self.OnNewSizeSelect)
		self.data_size_list.Bind(wx.EVT_COMBOBOX, self.OnNewSizeSelect)
		self.dvd_size_list.Bind(wx.EVT_COMBOBOX, self.OnNewSizeSelect)
		self.notebook_audio_cd.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.GoToAudioSettingsTab)
		self.notebook_data_cd.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.GoToDataSettingsTab)
		self.notebook_data_dvd.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.GoToDvdSettingsTab)
		
		self.Bind(wx.EVT_CLOSE, self.OnQuitProgram)
		# end wxGlade
		
		il = wx.ImageList(32,32)
		img0 = il.Add(wx.Bitmap('icons/audiocd.png', wx.BITMAP_TYPE_PNG))  
		img1 = il.Add(wx.Bitmap('icons/datacd.png', wx.BITMAP_TYPE_PNG))        
		img2 = il.Add(wx.Bitmap('icons/dvd.png', wx.BITMAP_TYPE_PNG))        
		img3 = il.Add(wx.Bitmap('icons/otherop.png', wx.BITMAP_TYPE_PNG))        
				
		self.notebook_top.AssignImageList(il)
		self.notebook_top.SetPageImage(0,img0)    
		self.notebook_top.SetPageImage(1,img1)          
		self.notebook_top.SetPageImage(2,img2)          
		self.notebook_top.SetPageImage(3,img3)          

	def __set_properties(self):
		# begin wxGlade: MyFrame.__set_properties
		self.SetTitle("Yagoburn")
		self.SetIcon(wx.Icon('icons/yagoburn.png', wx.BITMAP_TYPE_ANY, 22, 22))
		self.SetSize((765, 515))
		self.audio_size_list.SetMinSize((107, 27))
		self.audio_size_list.SetSelection(3)
		self.audio_next_button.SetMinSize((125, 32))
		self.audio_device_list.SetSelection(-1)
		self.audio_speed_list.SetSelection(0)
		self.audio_mode_radiobox.SetSelection(0)
		self.audio_burn_button.SetMinSize((100, 60))
		self.audio_burn_button.SetToolTipString("Write Files to Media")
		self.audio_burn_button.SetDefault()
		self.data_size_list.SetMinSize((107, 27))
		self.data_size_list.SetSelection(3)
		self.data_adddir_button.SetDefault()
		self.data_next_button.SetMinSize((125, 32))
		self.data_volname_entry.SetMinSize((220, 27))
		self.data_device_list.SetSelection(-1)
		self.data_speed_list.SetSelection(0)
		self.data_mode_radiobox.SetSelection(0)
		self.data_isopath_entry.SetMinSize((260, 27))
		self.data_isopath_entry.Enable(False)
		self.data_isosel_button.Enable(False)
		self.data_multi_check.SetToolTipString("Multisession support is not yet implemented in Yagoburn!")
		self.data_multi_check.Enable(False)
		self.data_burn_button.SetMinSize((100, 60))
		self.data_burn_button.SetToolTipString("Write Files to Media")
		self.data_burn_button.SetDefault()
		self.dvd_size_list.SetMinSize((87, 27))
		self.dvd_size_list.SetSelection(0)
		self.dvd_adddir_button.SetDefault()
		self.dvd_next_button.SetMinSize((125, 32))
		self.dvd_volname_entry.SetMinSize((220, 27))
		self.dvd_device_list.SetSelection(-1)
		self.dvd_speed_list.SetSelection(0)
		self.dvd_isopath_entry.SetMinSize((260, 27))
		self.dvd_isopath_entry.Enable(False)
		self.dvd_isosel_button.Enable(False)
		self.dvd_multi_check.SetToolTipString("Multisession support is not yet implemented in Yagoburn!")
		self.dvd_multi_check.Enable(False)
		self.dvd_burn_button.SetMinSize((100, 60))
		self.dvd_burn_button.SetToolTipString("Write Files to Media")
		self.dvd_burn_button.SetDefault()
		self.format_device_list.SetSelection(-1)
		self.quickblankcd_button_copy.SetMinSize((137, 32))
		self.formatdvd_button_copy.SetMinSize((132, 32))
		self.fullblankcd_button_copy.SetMinSize((132, 32))
		self.justfixate_button_copy.SetMinSize((132, 32))
		self.burn_isopath_entry.SetMinSize((260, 27))
		self.burniso_device_list.SetSelection(-1)
		self.burniso_speed_list.SetSelection(0)
		self.burniso_mode_radiobox.SetSelection(0)
		self.burniso_burn_button.SetMinSize((100, 60))
		self.burniso_burn_button.SetToolTipString("Write Files to Media")
		self.burniso_burn_button.SetDefault()
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: MyFrame.__do_layout
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_6_copy_copy_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_18_copy_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_7_copy_copy_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_7_copy_1_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_6_copy_1 = wx.BoxSizer(wx.VERTICAL)
		grid_sizer_1 = wx.GridSizer(2, 2, 3, 3)
		sizer_7_copy_2 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_6_copy_copy = wx.BoxSizer(wx.VERTICAL)
		sizer_18_copy_copy = wx.BoxSizer(wx.HORIZONTAL)
		sizer_19_copy = wx.BoxSizer(wx.HORIZONTAL)
		sizer_20_copy = wx.BoxSizer(wx.HORIZONTAL)
		sizer_7_copy_copy_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_7_copy_1_copy = wx.BoxSizer(wx.HORIZONTAL)
		sizer_7_copy_copy_copy_copy = wx.BoxSizer(wx.HORIZONTAL)
		sizer_9_copy = wx.BoxSizer(wx.VERTICAL)
		sizer_12_copy = wx.BoxSizer(wx.HORIZONTAL)
		sizer_11_copy = wx.BoxSizer(wx.HORIZONTAL)
		sizer_14_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_10_copy = wx.StaticBoxSizer(self.sizer_10_copy_staticbox, wx.HORIZONTAL)
		sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_6_copy = wx.BoxSizer(wx.VERTICAL)
		sizer_18_copy = wx.BoxSizer(wx.HORIZONTAL)
		sizer_19 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_7_copy_copy = wx.BoxSizer(wx.HORIZONTAL)
		sizer_7_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_7_copy_copy_copy = wx.BoxSizer(wx.HORIZONTAL)
		sizer_9 = wx.BoxSizer(wx.VERTICAL)
		sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_14_copy = wx.BoxSizer(wx.HORIZONTAL)
		sizer_10 = wx.StaticBoxSizer(self.sizer_10_staticbox, wx.HORIZONTAL)
		sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_6 = wx.BoxSizer(wx.VERTICAL)
		sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_7_copy = wx.BoxSizer(wx.HORIZONTAL)
		sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_13 = wx.BoxSizer(wx.VERTICAL)
		sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
		sizer_15 = wx.StaticBoxSizer(self.sizer_15_staticbox, wx.HORIZONTAL)
		sizer_15.Add(self.audio_file_list, 1, wx.TOP|wx.EXPAND, 5)
		sizer_13.Add(sizer_15, 1, wx.TOP|wx.EXPAND, 17)
		sizer_14.Add(self.audio_totalsize_entry, 0, wx.ALL, 7)
		sizer_14.Add(self.audio_gauge, 1, wx.ALL|wx.EXPAND, 7)
		sizer_14.Add(self.audio_size_list, 0, wx.ALL, 7)
		sizer_13.Add(sizer_14, 0, wx.EXPAND, 0)
		sizer_16.Add(self.panel_2, 1, wx.EXPAND, 0)
		sizer_16.Add(self.add_track_button, 0, 0, 0)
		sizer_16.Add(self.remove_track_button, 0, 0, 0)
		sizer_13.Add(sizer_16, 0, wx.ALL|wx.EXPAND, 7)
		sizer_8.Add(self.panel_3, 1, wx.RIGHT|wx.EXPAND, 7)
		sizer_8.Add(self.audio_next_button, 0, 0, 17)
		sizer_13.Add(sizer_8, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 7)
		self.audio_cd.SetSizer(sizer_13)
		sizer_7.Add(self.label_device_1, 0, wx.ALL, 17)
		sizer_7.Add(self.audio_device_list, 0, wx.ALL, 11)
		sizer_7.Add(self.audio_devprop_button, 0, wx.ALL, 11)
		sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
		sizer_7_copy.Add(self.label_speed_1, 0, wx.ALL, 17)
		sizer_7_copy.Add(self.audio_speed_list, 0, wx.ALL, 11)
		sizer_6.Add(sizer_7_copy, 1, wx.EXPAND, 0)
		sizer_6.Add(self.audio_mode_radiobox, 0, wx.LEFT|wx.BOTTOM|wx.EXPAND|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 17)
		sizer_6.Add(self.audio_simulate_check, 0, wx.LEFT|wx.RIGHT|wx.TOP, 17)
		sizer_6.Add(self.audio_nofix_check, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM, 17)
		sizer_18.Add(self.panel_7, 1, wx.EXPAND, 0)
		sizer_18.Add(self.audio_burn_button, 0, 0, 0)
		sizer_18.Add(self.panel_4, 1, wx.EXPAND, 0)
		sizer_6.Add(sizer_18, 1, wx.EXPAND, 0)
		self.audio_cd_settings.SetSizer(sizer_6)
		self.notebook_audio_cd.AddPage(self.audio_cd, " Audio CD ")
		self.notebook_audio_cd.AddPage(self.audio_cd_settings, " Settings ")
		sizer_3.Add(self.notebook_audio_cd, 1, wx.ALL|wx.EXPAND, 7)
		self.audio_cd_pane.SetSizer(sizer_3)
		sizer_10.Add(self.data_file_list, 1, wx.TOP|wx.EXPAND, 5)
		sizer_9.Add(sizer_10, 1, wx.TOP|wx.EXPAND, 17)
		sizer_14_copy.Add(self.data_totalsize_entry, 0, wx.ALL, 7)
		sizer_14_copy.Add(self.data_gauge, 1, wx.ALL|wx.EXPAND, 7)
		sizer_14_copy.Add(self.data_size_list, 0, wx.ALL, 7)
		sizer_9.Add(sizer_14_copy, 0, wx.EXPAND, 0)
		sizer_11.Add(self.panel_6, 1, wx.EXPAND, 0)
		sizer_11.Add(self.data_addfile_button, 0, 0, 0)
		sizer_11.Add(self.data_adddir_button, 0, 0, 0)
		sizer_11.Add(self.data_remove_button, 0, 0, 0)
		sizer_11.Add(self.data_clear_button, 0, 0, 0)
		sizer_9.Add(sizer_11, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 7)
		sizer_12.Add(self.panel_5, 1, wx.EXPAND, 0)
		sizer_12.Add(self.data_next_button, 0, 0, 0)
		sizer_9.Add(sizer_12, 0, wx.ALL|wx.EXPAND, 7)
		self.data_cd.SetSizer(sizer_9)
		sizer_7_copy_copy_copy.Add(self.data_volume_label, 0, wx.ALL, 17)
		sizer_7_copy_copy_copy.Add(self.data_volname_entry, 0, wx.TOP, 11)
		sizer_6_copy.Add(sizer_7_copy_copy_copy, 1, wx.EXPAND, 0)
		sizer_7_copy_1.Add(self.label_2_copy_1, 0, wx.ALL, 17)
		sizer_7_copy_1.Add(self.data_device_list, 0, wx.ALL, 11)
		sizer_7_copy_1.Add(self.data_devprop_button, 0, wx.ALL, 11)
		sizer_6_copy.Add(sizer_7_copy_1, 1, wx.EXPAND, 0)
		sizer_7_copy_copy.Add(self.label_2_copy_copy, 0, wx.ALL, 17)
		sizer_7_copy_copy.Add(self.data_speed_list, 0, wx.ALL, 11)
		sizer_6_copy.Add(sizer_7_copy_copy, 1, wx.EXPAND, 0)
		sizer_6_copy.Add(self.data_mode_radiobox, 1, wx.LEFT|wx.BOTTOM|wx.EXPAND|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 17)
		sizer_19.Add(self.data_onlyiso_check, 0, wx.LEFT|wx.RIGHT|wx.TOP, 17)
		sizer_20.Add(self.data_isopath_entry, 0, wx.TOP, 11)
		sizer_20.Add(self.data_isosel_button, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.ALIGN_CENTER_HORIZONTAL, 8)
		sizer_19.Add(sizer_20, 1, wx.EXPAND, 0)
		sizer_6_copy.Add(sizer_19, 1, wx.EXPAND, 0)
		sizer_6_copy.Add(self.data_multi_check, 0, wx.LEFT|wx.RIGHT, 17)
		sizer_6_copy.Add(self.data_simulate_check, 0, wx.LEFT|wx.RIGHT, 17)
		sizer_6_copy.Add(self.data_nofix_check, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM, 17)
		sizer_18_copy.Add(self.panel_7_copy, 1, wx.EXPAND, 0)
		sizer_18_copy.Add(self.data_burn_button, 0, 0, 0)
		sizer_18_copy.Add(self.panel_4_copy, 1, wx.EXPAND, 0)
		sizer_6_copy.Add(sizer_18_copy, 1, wx.EXPAND, 0)
		self.data_cd_settings.SetSizer(sizer_6_copy)
		self.notebook_data_cd.AddPage(self.data_cd, " Data CD ")
		self.notebook_data_cd.AddPage(self.data_cd_settings, " Settings ")
		sizer_4.Add(self.notebook_data_cd, 1, wx.ALL|wx.EXPAND, 7)
		self.data_cd_pane.SetSizer(sizer_4)
		sizer_10_copy.Add(self.dvd_file_list, 1, wx.TOP|wx.EXPAND, 5)
		sizer_9_copy.Add(sizer_10_copy, 1, wx.TOP|wx.EXPAND, 17)
		sizer_14_copy_1.Add(self.dvd_totalsize_entry, 0, wx.ALL, 7)
		sizer_14_copy_1.Add(self.dvd_gauge, 1, wx.ALL|wx.EXPAND, 7)
		sizer_14_copy_1.Add(self.dvd_size_list, 0, wx.ALL, 7)
		sizer_9_copy.Add(sizer_14_copy_1, 0, wx.EXPAND, 0)
		sizer_11_copy.Add(self.panel_6_copy, 1, wx.EXPAND, 0)
		sizer_11_copy.Add(self.dvd_addfile_button, 0, 0, 0)
		sizer_11_copy.Add(self.dvd_adddir_button, 0, 0, 0)
		sizer_11_copy.Add(self.dvd_remove_button, 0, 0, 0)
		sizer_11_copy.Add(self.dvd_clear_button, 0, 0, 0)
		sizer_9_copy.Add(sizer_11_copy, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 7)
		sizer_12_copy.Add(self.panel_5_copy, 1, wx.EXPAND, 0)
		sizer_12_copy.Add(self.dvd_next_button, 0, 0, 0)
		sizer_9_copy.Add(sizer_12_copy, 0, wx.ALL|wx.EXPAND, 7)
		self.data_dvd.SetSizer(sizer_9_copy)
		sizer_7_copy_copy_copy_copy.Add(self.dvd_volname_label, 0, wx.ALL, 17)
		sizer_7_copy_copy_copy_copy.Add(self.dvd_volname_entry, 0, wx.TOP, 11)
		sizer_6_copy_copy.Add(sizer_7_copy_copy_copy_copy, 1, wx.EXPAND, 0)
		sizer_7_copy_1_copy.Add(self.label_2_copy_1_copy, 0, wx.ALL, 17)
		sizer_7_copy_1_copy.Add(self.dvd_device_list, 0, wx.ALL, 11)
		sizer_7_copy_1_copy.Add(self.dvd_devprop_button, 0, wx.ALL, 11)
		sizer_6_copy_copy.Add(sizer_7_copy_1_copy, 1, wx.EXPAND, 0)
		sizer_7_copy_copy_copy_1.Add(self.dvd_label_2, 0, wx.ALL, 17)
		sizer_7_copy_copy_copy_1.Add(self.dvd_speed_list, 0, wx.ALL, 11)
		sizer_6_copy_copy.Add(sizer_7_copy_copy_copy_1, 1, wx.EXPAND, 0)
		sizer_19_copy.Add(self.dvd_onlyiso_check, 0, wx.LEFT|wx.RIGHT|wx.TOP, 17)
		sizer_20_copy.Add(self.dvd_isopath_entry, 0, wx.TOP, 11)
		sizer_20_copy.Add(self.dvd_isosel_button, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.ALIGN_CENTER_HORIZONTAL, 8)
		sizer_19_copy.Add(sizer_20_copy, 1, wx.EXPAND, 0)
		sizer_6_copy_copy.Add(sizer_19_copy, 1, wx.EXPAND, 0)
		sizer_6_copy_copy.Add(self.dvd_multi_check, 0, wx.LEFT|wx.RIGHT, 17)
		sizer_6_copy_copy.Add(self.dvd_simulate_check, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM, 17)
		#sizer_6_copy_copy.Add(self.dvd_nofix_check, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM, 17)
		sizer_18_copy_copy.Add(self.panel_7_copy_copy, 1, wx.EXPAND, 0)
		sizer_18_copy_copy.Add(self.dvd_burn_button, 0, 0, 0)
		sizer_18_copy_copy.Add(self.panel_4_copy_copy, 1, wx.EXPAND, 0)
		sizer_6_copy_copy.Add(sizer_18_copy_copy, 1, wx.EXPAND, 0)
		self.data_dvd_settings.SetSizer(sizer_6_copy_copy)
		self.notebook_data_dvd.AddPage(self.data_dvd, " Data DVD")
		self.notebook_data_dvd.AddPage(self.data_dvd_settings, " Settings ")
		sizer_5.Add(self.notebook_data_dvd, 1, wx.ALL|wx.EXPAND, 7)
		self.data_dvd_pane.SetSizer(sizer_5)
		sizer_7_copy_2.Add(self.label_device_1_copy, 0, wx.ALL, 17)
		sizer_7_copy_2.Add(self.format_device_list, 0, wx.ALL, 11)
		sizer_7_copy_2.Add(self.format_devprop_button, 0, wx.ALL, 11)
		sizer_6_copy_1.Add(sizer_7_copy_2, 1, wx.EXPAND, 0)
		grid_sizer_1.Add(self.quickblankcd_button_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
		grid_sizer_1.Add(self.formatdvd_button_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
		grid_sizer_1.Add(self.fullblankcd_button_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 7)
		grid_sizer_1.Add(self.justfixate_button_copy, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_6_copy_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
		self.blank_disk.SetSizer(sizer_6_copy_1)
		sizer_17.Add(self.label_1, 0, wx.LEFT|wx.TOP, 17)
		sizer_17.Add(self.burn_isopath_entry, 0, wx.TOP, 11)
		sizer_17.Add(self.burn_isosel_button, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.ALIGN_CENTER_HORIZONTAL, 8)
		sizer_6_copy_copy_1.Add(sizer_17, 1, wx.EXPAND, 0)
		sizer_7_copy_1_copy_1.Add(self.label_2_copy_1_copy_1, 0, wx.ALL, 17)
		sizer_7_copy_1_copy_1.Add(self.burniso_device_list, 0, wx.ALL, 11)
		sizer_7_copy_1_copy_1.Add(self.burniso_devprop_button, 0, wx.ALL, 11)
		sizer_6_copy_copy_1.Add(sizer_7_copy_1_copy_1, 1, wx.EXPAND, 0)
		sizer_7_copy_copy_copy_2.Add(self.label_2_copy_copy_copy, 0, wx.ALL, 17)
		sizer_7_copy_copy_copy_2.Add(self.burniso_speed_list, 0, wx.ALL, 11)
		sizer_6_copy_copy_1.Add(sizer_7_copy_copy_copy_2, 1, wx.EXPAND, 0)
		sizer_6_copy_copy_1.Add(self.burniso_mode_radiobox, 1, wx.LEFT|wx.BOTTOM|wx.EXPAND|wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 17)
		sizer_6_copy_copy_1.Add(self.burniso_simulate_check, 0, wx.LEFT|wx.RIGHT,17)
		sizer_6_copy_copy_1.Add(self.burniso_nofix_check, 0, wx.LEFT|wx.RIGHT|wx.BOTTOM, 17)
		sizer_18_copy_copy_1.Add(self.panel_7_copy_copy_1, 1, wx.EXPAND, 0)
		sizer_18_copy_copy_1.Add(self.burniso_burn_button, 0, 0, 0)
		sizer_18_copy_copy_1.Add(self.panel_4_copy_copy_1, 1, wx.EXPAND, 0)
		sizer_6_copy_copy_1.Add(sizer_18_copy_copy_1, 1, wx.EXPAND, 0)
		self.burn_iso.SetSizer(sizer_6_copy_copy_1)
		self.notebook_other_op.AddPage(self.blank_disk, "Blank/Format Disk")
		self.notebook_other_op.AddPage(self.burn_iso, "Burn ISO")
		sizer_2.Add(self.notebook_other_op, 1, wx.ALL|wx.EXPAND, 7)
		self.other_op_pane.SetSizer(sizer_2)
		self.notebook_top.AddPage(self.audio_cd_pane, "  Audio CD  ")
		self.notebook_top.AddPage(self.data_cd_pane, "  Data CD  ")
		self.notebook_top.AddPage(self.data_dvd_pane, "  Data DVD  ")
		self.notebook_top.AddPage(self.other_op_pane, "  Other Operations  ")
		sizer_1.Add(self.notebook_top, 1, wx.ALL|wx.EXPAND, 5)
		self.SetSizer(sizer_1)
		self.Layout()
		# end wxGlade

## Callback Handler defintions
	def OnNewSizeSelect(self, event):
		eid=event.GetId()
		if eid==201:
			self.UpdateAudioFilesView()
		elif eid==202:
			self.UpdateDataFilesView()
		elif eid==203:
			self.UpdateDvdFilesView()

	def UpdateAudioFilesView(self):
		####### remove duplicates from list
		self.audio_files_to_burn=reduce(lambda x,y: x+[y][:1-int(y in x)], self.audio_files_to_burn, [])
		############
		self.audio_file_list.Clear()        
		totalsize=0
		if self.audio_files_to_burn!=[]:
			for f in self.audio_files_to_burn:
				fsize=os.path.getsize(f)
				self.audio_file_list.Append("{0}  ({1})".format(f,fun.FormatSize(fsize)))
				totalsize+=fsize
		self.audio_totalsize_entry.SetValue(fun.FormatSize(totalsize))
		maxsize=int(self.audio_size_list.GetValue().split(' ')[0])*(1024**2)
		if totalsize<=maxsize:
			self.audio_gauge.SetValue(int(totalsize*100/maxsize))
			if totalsize==0:
				self.audio_gauge.SetValue(0)
		else:
			self.audio_gauge.SetValue(100)		
		

	def AddAudioTrack(self, event): # wxGlade: MyFrame.<event_handler>
		self.audio_files_to_burn += (fun.AddFileDialog("Select .wav files to add:","Wav files (*.wav)|*.wav"))
		self.UpdateAudioFilesView()
		#event.skip()
		
	def RemoveAudioTrack(self, event): # wxGlade: MyFrame.<event_handler>
		self.audio_files_to_burn.pop(self.audio_file_list.GetSelection())
		self.UpdateAudioFilesView()
		#event.skip()

	def GoToAudioSettingsTab(self, event): # wxGlade: MyFrame.<event_handler>
		if event.GetId()==wx.ID_FORWARD:  # Forward Button Pressed
			self.notebook_audio_cd.SetSelection(1)
		elif event.GetSelection()==0:     # manual tab change to previous tab; do nothing
				return
		## Do this if forward button pressed OR manual tab change to next tab
		fun.ClearCdRoot(CDROOT)   # Clear previous Cdroot, if any
		fun.CreateCdRoot(CDROOT,self.audio_files_to_burn)  # Create new cdroot based on files to burn                

		#event.skip()
		
	def OnBurnAudio(self, event): # wxGlade: MyFrame.<event_handler>
		if self.audio_mode_radiobox.GetSelection() == 0:
			mode='-dao'
		else:
			mode='-tao'
		speed=self.audio_speed_list.GetValue().replace('x','')
		if speed=='Default Speed':
			speed=''
		else:
			speed = 'speed='+str(speed)     
			
		dev=self.audio_device_list.GetValue()
		if dev=='':
			fun.ShowGenericMsgDialog('Error!','error','Choose a device first!')
			return            
		else:
			dev=self.audio_device_list.GetValue()
		
		if self.audio_nofix_check.IsChecked():
			nofix='-nofix'
		else:
			nofix=''
		
		if	self.audio_simulate_check.IsChecked():	
			simulate='-dummy'
		else:
			simulate=''		
		
		cmd='wodim -v -eject -pad {4} {5} {0} {1} dev={2} defpregap=0 -audio {3}/*.wav'.format(mode,speed,dev,CDROOT,nofix,simulate)
		
		exitcode,elog,slog= fun.RunCommand(cmd)
		if exitcode==0:
			fun.ShowSuccessWithLogDialog(slog)
			fun.NotifySend(0)
		elif exitcode>0:
			fun.ShowErrorWithLogDialog(elog)
			fun.NotifySend(1)
		else:
			fun.ShowGenericMsgDialog('Manual Abort!','error','The process was prematurely interrupted!')
			
		#event.skip()

	def UpdateDataFilesView(self):
		####### remove duplicates from list
		self.data_files_to_burn=reduce(lambda x,y: x+[y][:1-int(y in x)], self.data_files_to_burn, [])
		############
		self.data_file_list.Clear()        
		totalsize=0
		if self.data_files_to_burn!=[]:			
			for f in self.data_files_to_burn:
				if os.path.isdir(f):
					fsize=fun.GetDirectorySize(f)
				else:
					fsize=os.path.getsize(f)
				self.data_file_list.Append("{0}  ({1})".format(f,fun.FormatSize(fsize)))
				totalsize+=fsize
		self.data_totalsize_entry.SetValue(fun.FormatSize(totalsize))
		maxsize=int(self.data_size_list.GetValue().split(' ')[0])*(1024**2)
		if totalsize<=maxsize:
			self.data_gauge.SetValue(int(totalsize*100/maxsize))
			if totalsize==0:
				self.data_gauge.SetValue(0)
		else:
			self.data_gauge.SetValue(100)
			
				
		
	def AddDataFile(self, event): # wxGlade: MyFrame.<event_handler>
		self.data_files_to_burn += (fun.AddFileDialog("Select  files to add:","All files (*.*)|*.*"))
		self.UpdateDataFilesView()
		#event.skip()

	def AddDataDir(self, event): # wxGlade: MyFrame.<event_handler>
		self.data_files_to_burn.append(fun.AddDirDialog("Select  directories to add:"))
		self.UpdateDataFilesView()        
		#event.skip()

	def RemoveDataFile(self, event): # wxGlade: MyFrame.<event_handler>
		self.data_files_to_burn.pop(self.data_file_list.GetSelection())
		self.UpdateDataFilesView()        
		#event.skip()

	def ClearDataList(self, event): # wxGlade: MyFrame.<event_handler>
		self.data_files_to_burn=[]
		self.UpdateDataFilesView()
		fun.ClearCdRoot(CDROOT)
		#event.skip()

	def GoToDataSettingsTab(self, event): # wxGlade: MyFrame.<event_handler>
		if event.GetId()==wx.ID_FORWARD:  # Forward Button Pressed
			self.notebook_data_cd.SetSelection(1)
		elif event.GetSelection()==0:     # manual tab change to previous tab; do nothing
				return
		## Do this if forward button pressed OR manual tab change to next tab
		fun.ClearCdRoot(CDROOT)   # Clear previous Cdroot, if any
		fun.CreateCdRoot(CDROOT,self.data_files_to_burn)  # Create new cdroot based on files to burn                
		
		#event.skip()
		
	def OnBurnData(self, event): # wxGlade: MyFrame.<event_handler>
		if not self.data_onlyiso_check.IsChecked(): # just to avoid regeneration of image if device or isopath is not selected
			dev=self.data_device_list.GetValue()
			if dev=='':
				fun.ShowGenericMsgDialog('Error!','error','Choose a device first!')
				return            
		else:
			if self.data_isopath_entry.GetValue()=="Click button to select save iso location":
				fun.ShowGenericMsgDialog("Error!",'error',"Choose a location to Save the iso by clicking on button beside")
				return
		# Generate ISO
		import os
		os.system("rm -f "+TMPISO)
		## temporarily replace spaces in volname with *, to be retrieved in custowidgets.py
		volname=self.data_volname_entry.GetValue().replace(" ",'*')
		exitcode,elog,slog=fun.RunCommand("genisoimage -V {2} -J -r -l -o {0} -f {1}".format(TMPISO,CDROOT,volname))
		if exitcode>0:
			fun.ShowErrorWithLogDialog(elog)
			return
		elif exitcode<0:
			fun.ShowGenericMsgDialog('Manual Abort!','error','The process was prematurely interrupted!')
			return
		# Now check if only iso is selected
		isopath=self.data_isopath_entry.GetValue()
		if self.data_onlyiso_check.IsChecked():
			exitstat=os.system('mv {0} {1}'.format(TMPISO,isopath))
			if exitstat!=0:
				fun.ShowGenericMsgDialog('Permissions Error!','error','Unable to create file {0}!\n\n(Your required iso is still at {1})'.format(isopath,TMPISO))
				return
			fun.ShowGenericMsgDialog('Success!','info', "Successfully created ISO file "+isopath)
			return
		# Continue to actually burning cd
		else:		
			if self.data_nofix_check.IsChecked():
				burnfree=""
			else:
				burnfree="driveropts=burnfree"
			if self.data_mode_radiobox.GetSelection() == 0:
				mode='-dao'
			else:
				mode='-tao'
			speed=self.data_speed_list.GetValue().replace('x','')
			if speed=='Default Speed':
				speed=''
			else:
				speed = 'speed='+str(speed)     

			if	self.data_simulate_check.IsChecked():	
				simulate='-dummy'
			else:
				simulate=''		
			
			cmd="wodim dev={0} {1} {2} {3} {4} -eject -v -data {5}".format(dev,burnfree,mode,speed,simulate,TMPISO)
			exitcode,elog,slog= fun.RunCommand(cmd)
			if exitcode==0:
				fun.NotifySend(0)
				fun.ShowSuccessWithLogDialog(slog)
			elif exitcode>0:
				fun.NotifySend(1)
				fun.ShowErrorWithLogDialog(elog)
			else:
				fun.ShowGenericMsgDialog('Manual Abort!','error','The process was prematurely interrupted!')					


	def UpdateDvdFilesView(self):
		####### remove duplicates from list
		self.dvd_files_to_burn=reduce(lambda x,y: x+[y][:1-int(y in x)], self.dvd_files_to_burn, [])
		############
		self.dvd_file_list.Clear()        
		totalsize=0
		if self.dvd_files_to_burn!=[]:			
			for f in self.dvd_files_to_burn:
				if os.path.isdir(f):
					fsize=fun.GetDirectorySize(f)
				else:
					fsize=os.path.getsize(f)
				self.dvd_file_list.Append("{0}  ({1})".format(f,fun.FormatSize(fsize)))
				totalsize+=fsize
		self.dvd_totalsize_entry.SetValue(fun.FormatSize(totalsize))
		maxsize_str=self.dvd_size_list.GetValue().split(' ')[0].replace(".","")
		maxsize=int(maxsize_str)*(1024**3)/10
		if totalsize<=maxsize:
			self.dvd_gauge.SetValue(int(totalsize*100/maxsize))
			if totalsize==0:
				self.dvd_gauge.SetValue(0)
		else:
			self.dvd_gauge.SetValue(100)		

	def AddDvdFile(self, event): # wxGlade: MyFrame.<event_handler>
		self.dvd_files_to_burn += (fun.AddFileDialog("Select  files to add:","All files (*.*)|*.*"))
		self.UpdateDvdFilesView()

		#event.skip()

	def AddDvdDir(self, event): # wxGlade: MyFrame.<event_handler>
		self.dvd_files_to_burn.append(fun.AddDirDialog("Select  directories to add:"))
		self.UpdateDvdFilesView()        
		#event.skip()

	def RemoveDvdFile(self, event): # wxGlade: MyFrame.<event_handler>
		self.dvd_files_to_burn.pop(self.dvd_file_list.GetSelection())
		self.UpdateDvdFilesView()        
		#event.skip()

	def ClearDvdList(self, event): # wxGlade: MyFrame.<event_handler>
		self.dvd_files_to_burn=[]
		self.UpdateDvdFilesView() 
		fun.ClearCdRoot(CDROOT)       
		#event.skip()

	def GoToDvdSettingsTab(self, event): # wxGlade: MyFrame.<event_handler>
		
		if event.GetId()==wx.ID_FORWARD:  # Forward Button Pressed
			self.notebook_data_dvd.SetSelection(1)
		elif event.GetSelection()==0:     # manual tab change to previous tab; do nothing
				return
		## Do this if forward button pressed OR manual tab change to next tab
		fun.ClearCdRoot(CDROOT)   # Clear previous Cdroot, if any
		fun.CreateCdRoot(CDROOT,self.dvd_files_to_burn)  # Create new cdroot based on files to burn                
				
		#event.skip()

	def OnBurnDvd(self, event): # wxGlade: MyFrame.<event_handler>
		if not self.dvd_onlyiso_check.IsChecked(): # just to avoid regeneration of image if device or isopath is not selected
			dev=self.dvd_device_list.GetValue()
			if dev=='':
				fun.ShowGenericMsgDialog('Error!','error','Choose a device first!')
				return            
		else:
			if self.dvd_isopath_entry.GetValue()=="Click button to select save iso location":
				fun.ShowGenericMsgDialog("Error!",'error',"Choose a location to Save the iso by clicking on button beside")
				return		
		# Generate ISO
		import os
		os.system("rm -f "+TMPISO)
		## temporarily replace spaces in volname with *, to be retrieved in custowidgets.py
		volname=self.dvd_volname_entry.GetValue().replace(" ",'*')
		exitcode,elog,slog=fun.RunCommand("genisoimage -V {2} -J -r -l -o {0} -f {1}".format(TMPISO,CDROOT,volname))
		if exitcode>0:
			fun.ShowErrorWithLogDialog(elog)
			return
		elif exitcode<0:
			fun.ShowGenericMsgDialog('Manual Abort!','error','The process was prematurely interrupted!')
			return
		# Now check if only iso is selected
		if self.dvd_onlyiso_check.IsChecked():
			exitstat=os.system('mv {0} {1}'.format(TMPISO,self.dvd_isopath_entry.GetValue()))
			if exitstat!=0:
				fun.ShowGenericMsgDialog('Permissions Error!','error','Unable to create file {0}!\n\nYour required iso is still at {1}'.format(self.dvd_isopath_entry.GetValue(),TMPISO))
				return
			fun.ShowGenericMsgDialog('Success!','info', "Successfully created ISO file "+self.dvd_isopath_entry.GetValue())
			return
		# Continue to actually burning dvd
		else:		
			speed=self.dvd_speed_list.GetValue().replace('x','')
			if speed=='Default Speed':
				speed=''
			else:
				speed = 'speed='+str(speed)     
		
			if	self.dvd_simulate_check.IsChecked():	
				simulate='-dry-run'
			else:
				simulate=''		
			
			cmd="growisofs {0} {1} -dvd-compat -Z {2}={3}".format(simulate,speed,dev,TMPISO)
			exitcode,elog,slog= fun.RunCommand(cmd)
			if exitcode==0:
				fun.NotifySend(0)
				fun.ShowSuccessWithLogDialog(slog)
			elif exitcode>0:
				fun.NotifySend(1)
				fun.ShowErrorWithLogDialog(elog)
			else:
				fun.ShowGenericMsgDialog('Manual Abort!','error','The process was prematurely interrupted!')		
		#event.skip()
		
	def OnFormatStuff(self, event):
		dev=self.format_device_list.GetValue()
		if dev=='':
			fun.ShowGenericMsgDialog('Error!','error','Choose a device first!')
			return        
		if event.GetId()==501:    # Quick Blank CD
			cmd="wodim -blank=fast -v dev={0}".format(dev)
		elif event.GetId()==502:	# Format DVD
			cmd="dvd+rw-format -force=full {0}".format(dev)
		elif event.GetId()==503:	# Full Blank CD
			cmd="wodim -blank=all -v dev={0}".format(dev)
		elif event.GetId()==504:	#Just Fixate the CD
			cmd="wodim -fix -v dev={0}".format(dev)
		
		exitcode,elog,slog= fun.RunCommand(cmd)
		if fnmatch.fnmatch(cmd,'*dvd+rw*')and exitcode >=0:	# dvd+rw tools doesn't generate proper exit code!
			if slog != '':
				exitcode=0
			elif elog != '':
				exitcode=1
#			log="WARNING: dvd+rw tools does NOT generate proper exit\ncodes. Hence, even if you see a success message here\nit doesn't necessarily mean that all went ok,\nand vice versa!!!  :=(\nCheck all the logs below carefully to know for sure!"
#			log+="\n"+"="*11+"\n\n"
#			log+=elog+"\n\n"+"="*11+"\n\n"+slog
#			slog=log
#			elog=log
			
		if exitcode==0:
			fun.NotifySend(0)
			fun.ShowSuccessWithLogDialog(slog)
		elif exitcode>0:
			fun.NotifySend(1)
			fun.ShowErrorWithLogDialog(elog)
		else:	# Manual Abort
			fun.ShowGenericMsgDialog('Manual Abort!','error','The process was prematurely interrupted!')			
		
	def OnBurnIso(self, event): # wxGlade: MyFrame.<event_handler>
		dev=self.burniso_device_list.GetValue()
		if dev=='':
			fun.ShowGenericMsgDialog('Error!','error','Choose a device first!')
			return 
		iso2burn=self.burn_isopath_entry.GetValue()
		if iso2burn=="" :
			fun.ShowGenericMsgDialog("Error!",'error',"Choose an ISO to burn!")
			return
		elif not fnmatch.fnmatch(iso2burn,"/*"):
			fun.ShowGenericMsgDialog("Error!",'error',"It doesn't look like you chose\na proper path to an .iso file!")
			return			
		speed=self.burniso_speed_list.GetValue().replace('x','')
		if speed=="Default Speed":
			speed=''
		else:
			speed="speed={0}".format(str(speed))
		if self.burniso_nofix_check.IsChecked():
			burnfree=''
		else:
			burnfree='driveropts=burnfree'
		if self.burniso_simulate_check.IsChecked():
			simulate="-dummy"
		else:
			simulate=""
		if self.burniso_mode_radiobox.GetSelection()==0:
			mode="-dao"
		else:
			mode="-tao"
			
		cmd="wodim dev={0} {1} {2} {3} {4} -eject -v {5}".format(dev,burnfree,speed,mode,simulate,iso2burn)
		
		exitcode,elog,slog= fun.RunCommand(cmd)
		if exitcode==0:
			fun.NotifySend(0)
			fun.ShowSuccessWithLogDialog(slog)
		elif exitcode>0:
			fun.NotifySend(1)
			fun.ShowErrorWithLogDialog(elog)
		else:
			fun.ShowGenericMsgDialog('Manual Abort!','error','The process was prematurely interrupted!')							

	def ShowAudioDeviceProp(self, event): # wxGlade: MyFrame.<event_handler>
		fun.ShowDeviceProp(self.audio_device_list.GetValue())
		#event.skip()
		
	def ShowDataDeviceProp(self, event): # wxGlade: MyFrame.<event_handler>
		fun.ShowDeviceProp(self.data_device_list.GetValue())
		#event.skip()

	def ShowDvdDeviceProp(self, event): # wxGlade: MyFrame.<event_handler>
		fun.ShowDeviceProp(self.dvd_device_list.GetValue())        
		#event.skip()
		
	def ShowFormatDeviceProp(self, event): # wxGlade: MyFrame.<event_handler>
		fun.ShowDeviceProp(self.format_device_list.GetValue())        
		#event.skip()
	
	def ShowBurnisoDeviceProp(self, event): # wxGlade: MyFrame.<event_handler>
		fun.ShowDeviceProp(self.burniso_device_list.GetValue())        
		#event.skip()
	
	def CheckOnlyCreateIso(self, event): # wxGlade: MyFrame.<event_handler>
		''' Used to toggle between burning related & iso related widgets '''
		if event.GetId() == 101:    ## We are on Data CD Tab
			ischecked = self.data_onlyiso_check.GetValue()
			self.data_device_list.Enable(not ischecked)
			self.data_speed_list.Enable(not ischecked)
			self.data_devprop_button.Enable(not ischecked)
			self.data_mode_radiobox.Enable(not ischecked)
			self.data_isopath_entry.Enable(ischecked)
			self.data_isopath_entry.SetValue('Click button to select save iso location')
			self.data_isosel_button.Enable(ischecked)
			self.data_simulate_check.Enable(not ischecked)
			self.data_nofix_check.Enable(not ischecked)
		elif event.GetId() == 102:  ## We are on Data Dvd Tab
			ischecked = self.dvd_onlyiso_check.GetValue()
			self.dvd_device_list.Enable(not ischecked)
			self.dvd_speed_list.Enable(not ischecked)
			self.dvd_devprop_button.Enable(not ischecked)
			self.dvd_isopath_entry.Enable(ischecked)
			self.dvd_isopath_entry.SetValue('Click button to select save iso location')
			self.dvd_isosel_button.Enable(ischecked) 
			self.dvd_simulate_check.Enable(not ischecked)
			#self.dvd_nofix_check.Enable(not ischecked)            
			#event.skip()

	def SelectDataIsoSaveLocation(self, event):
		path=fun.SaveIsoDialog()
		self.data_isopath_entry.SetValue(path)
	def SelectDvdIsoSaveLocation(self, event):
		path=fun.SaveIsoDialog()
		self.dvd_isopath_entry.SetValue(path)            
		
	def SelectIsoLocation(self, event): # wxGlade: MyFrame.<event_handler>
		path=fun.GetIsoDialog()
		self.burn_isopath_entry.SetValue(path)
		#event.skip()
		
	def OnQuitProgram(self, event):
		dlg = wx.MessageDialog(self, "Are you sure you want to Exit?", "Exit", wx.YES_NO | wx.ICON_QUESTION)
		if dlg.ShowModal() == wx.ID_YES:
			self.Destroy() # frame
		dlg.Destroy()
				

# end of class MyFrame


if __name__ == "__main__":
	app = wx.PySimpleApp(0)
	wx.InitAllImageHandlers()
	frame_1 = MyFrame()
	app.SetTopWindow(frame_1)
	frame_1.Show()
	app.MainLoop()
