
#############################################################################
##                                                                         ##
## This file is part of Owade : www.owade.org                              ##
## Offline Windows Analyzer and Data Extractor                             ##
##                                                                         ##
##  Authors:                                                               ##
##  Elie Bursztein <owade@elie.im>                                         ##
##  Ivan Fontarensky <ivan.fontarensky@cassidian.com>                      ##
##  Matthieu Martin <matthieu.mar+owade@gmail.com>                         ##
##  Jean-Michel Picod <jean-michel.picod@cassidian.com>                    ##
##                                                                         ##
## This program is distributed under GPLv3 licence (see LICENCE.txt)       ##
##                                                                         ##
#############################################################################
import os.path
__author__="ashe"
__date__ ="$May 24, 2011 6:21:13 PM$"

import os
import exceptions
import sys
import subprocess

def checkConstant(dir, isdir=True):
    if isdir:
        if not os.path.isdir(dir):
            raise exceptions.IOError('Directory not found %s' % dir)
    else:
        if not os.path.isfile(dir):
            raise exceptions.IOError('File not found %s' % dir)

#################
### MAIN DIR
#################
##Project main directory
PROJECT_DIR = "/opt/"
checkConstant(PROJECT_DIR + "OwadeHackaton")

##DPAPI directory
DPAPI_DIR = PROJECT_DIR + "dpapick/"
checkConstant(DPAPI_DIR)
sys.path.append(DPAPI_DIR)

##John the Ripper directory
JOHN_DIR = PROJECT_DIR + "jtr/run"
checkConstant(JOHN_DIR)
sys.path.append(JOHN_DIR)

#################
### DATABASE CONFIGURATION
#################
DATABASE_NAME='owade'
DATABASE_USER='postgres'
DATABASE_PASSWORD='postgres'
DATABASE_HOST='localhost'
DATABASE_PORT='5432'


#################
### STOCKAGE DIR (need a lot of disk space)
#################
##Where to stock disk image after ddrescue
              #/media/USERNAME/HDNAME/
EXT_HDRIVE = subprocess.check_output("find /media -name storage", shell=True).rstrip()

IMAGE_DIR = EXT_HDRIVE + "/image"
IMAGE_FTP = EXT_HDRIVE + "/ftp"
checkConstant(IMAGE_DIR)
##Where to stock files
FILE_DIR = EXT_HDRIVE + "/file"
checkConstant(FILE_DIR)


#################
### LIB DIR (shouldn't be modified)
#################
LIB_DIR = PROJECT_DIR + "OwadeHackaton/lib/"
##ff_key3db_dump directory
KEY3DB_DIR = LIB_DIR + "ff_key3db_dump/"
checkConstant(KEY3DB_DIR)

##msiecf directory
MSIECF_DIR = LIB_DIR + "msiecf/"
checkConstant(MSIECF_DIR)

##CFProperty directory
CFPROPERTY_DIR = LIB_DIR + 'CFProperty/'
checkConstant(CFPROPERTY_DIR)
sys.path.append(CFPROPERTY_DIR)

##geoQuery.rb
GEOQUERY = LIB_DIR + 'geoQuery.rb'
checkConstant(GEOQUERY, False)


#################
### DJANGO DIR (shouldn't be modified)
#################
##Where to save the database
DATABASE_DIR = PROJECT_DIR + "OwadeHackaton/database/"
checkConstant(DATABASE_DIR)
##Where to find the template
TEMPLATE_DIR = PROJECT_DIR + "OwadeHackaton/templates/"
checkConstant(TEMPLATE_DIR)

######################
#Forensic constants
# Masterkey
protectDir = "/Appdata/Roaming/Microsoft/Protect/"

# SAM
samPath = "/Windows/System32/config/SAM"

# SYSTEM
systemPath = "/Windows/System32/config/SYSTEM"

# Chrome
chromeLoginFile = "Login Data"
chromeLogin = "/AppData/Local/Google/Chrome/User Data/Default/" + chromeLoginFile
chromeHistoryFile = "History"
chromeHistory = "/AppData/Local/Google/Chrome/User Data/Default/" + chromeHistoryFile

# Firefox
firefoxKeysFile = "key3.db"
firefoxHistoryFile = "places.sqlite"
firefoxProfiles = "/AppData/Roaming/Mozilla/Firefox/Profiles/"
