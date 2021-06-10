# -*- coding: utf-8 -*-


# Configuration
width = 320  # Video width requested from camera
height = 240  # Video height requested from camera

wheel = 0  #0:stop, 1:left, 2:strait, 3:right

recording = False

cnt = 0
outputDir = './data/'
currentDir = 'training3'
file = ""
f = ''
fwriter = ''

Voicecontrol = False

AIcontrol = False
modelheight = -160 ###-130 ###-150 #-115 #-130 #-150 #-250 #-200

# training speed setting
maxturn_speed = 60
minturn_speed = -75  ###20  ###15
normal_speed_left = 40
normal_speed_right = 40
wheel_alignment_left = 0
wheel_alignment_right = 0


# testing speed setting(
ai_maxturn_speed = 60
ai_minturn_speed = -75
ai_normal_speed_left = 30
ai_normal_speed_right = 30




