########################################################################
##			IGNOU RESULTS SCRAPER			      ##
########################################################################

from splinter import Browser
import time
import os

count = 0 #Global variable to assign image filenames

########################################################################
##Function To Traverse Through The Results Website
########################################################################

def traverse(url):
	browser = Browser()
	browser.visit(url)
	file = open('student_list.txt')
	enrollment_no = file.read().split()

	for line in enrollment_no:
		time.sleep(1)
		browser.fill("eno",line)
		button = browser.find_by_value('Submit').click()
		time.sleep(3)
		capture()
		button = browser.click_link_by_text('Back ')
	file.close()

########################################################################
##Function To Capture Screenshots
########################################################################

def capture():
	global count
	count = count + 1
	command = "import -window root %r.png" %count
	os.system(command)

########################################################################
##Function To Create Pdf using Images Created Earlier
########################################################################

def createPdf():
	os.system('convert *.png Results.pdf')

########################################################################
##Function To Cleanup The Mess
########################################################################

def cleanup():
	files = [f for f in os.listdir('.') if f.endswith('.png')]
	for f in files:
		os.remove(f)

########################################################################
##Script Driver
########################################################################

url = raw_input('Enter The Results URL: \n')
traverse(url)
createPdf()
cleanup()

########################################################################
########################################################################