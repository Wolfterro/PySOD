#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
The MIT License (MIT)

Copyright (c) 2016 Wolfgang Almeida <wolfgang.almeida@yahoo.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# ===============================
# Created by: Wolfterro
# Version: 1.0 - Python 2.x
# Date: 06/12/2016 - (DD/MM/YYYY)
# ===============================

from __future__ import print_function
from pygame import mixer

import os
import sys
import time
import random
import pygame

# Program version
# ===============
VERSION = "1.0"

# Changing default encoding
# =========================
reload(sys)
sys.setdefaultencoding('utf-8')

# Selecting image and sound files
# ===============================
def selectFile(fType):
	availableFiles = []
	
	if fType == "IMG":
		try:
			for file in os.listdir("Screens"):
				if file.endswith(".png") or file.endswith(".jpg"):
					availableFiles.append(file)
		except Exception:
			print("[PySOD] Error! 'Screens' directory doesn't exist!")
			sys.exit(1)
	elif fType == "SND":
		try:
			for file in os.listdir("Sounds"):
				if file.endswith(".wav"):
					availableFiles.append(file)
		except Exception:
			print("[PySOD] Error! 'Sounds' directory doesn't exist!")
			sys.exit(1)

	if len(availableFiles) == 0:
		print("[PySOD] Error! No files available!")
		sys.exit(1)

	fNum = random.randint(0, len(availableFiles) - 1)
	print("File selected: %s" % (availableFiles[fNum]))
	
	return availableFiles[fNum]

# Playing sound file
# ==================
def playSound(sndFile):
		mixer.init()
		sound = mixer.Sound("Sounds/%s" % (str(sndFile)))
		sound.play()
		while mixer.get_busy():
			return

# Program's main window
# =====================
def mainScreen(imgFile, sndFile):
	pygame.display.init()
	pygame.display.set_caption("PySOD - v%s" % (VERSION))
	
	background = pygame.image.load("Screens/%s" % (str(imgFile)))
	resolution = pygame.display.Info()
	screen = pygame.display.set_mode((resolution.current_w, resolution.current_h), pygame.FULLSCREEN)
	pygame.mouse.set_visible(0)

	bRunning = True
	i = 0
	while(bRunning):
		while i < 1:
			playSound(sndFile)
			i += 1

		bConv = background.convert()
		image = pygame.transform.smoothscale(bConv, (resolution.current_w, resolution.current_h))
		imgpos = image.get_rect(centerx=(resolution.current_w / 2), centery=(resolution.current_h / 2))
		
		screen.fill((255,255,255))
		screen.blit(image, imgpos)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (
				event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN or event.key == pygame.K_SPACE)):
				bRunning = False

# Main method
# ===========
def main():
	imgFile = selectFile("IMG")
	sndFile = selectFile("SND")

	mainScreen(imgFile, sndFile)

# Initializing
# ============
if __name__ == "__main__":
	main()