#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  song-lyrics-reparse.py
#  
#  Copyright 2015 220 <220@WKH>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import random
import time

def main():
	# read lyrics catalog into a list
	lyrics_catalog = open ('lyrics_catalog.tdb', 'r')
	phrases = lyrics_catalog.readlines ()
	
	lyrics_catalog.close
	
	# ask user how many lines
	total_lines = int (raw_input ("how many lines? "))
	
	
	new_filename = ''
	for i in range (8):
		new_filename = new_filename+str (random.randrange (0, 9))
	
	print (new_filename)
	
	new_song = open (new_filename, 'w')
	for i in range (total_lines):
		line = "***"
		while (line.find ("***")!=-1):
			line = phrases.pop (random.randrange (len (phrases)))
		print (line)
		new_song.write (line)
		#time.sleep (random.randrange (1, 3))
	new_song.close
	
	return 0

if __name__ == '__main__':
	main()

