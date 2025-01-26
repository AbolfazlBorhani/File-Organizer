from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.uic import loadUi
from getpass import getuser
from shutil import move
from PyQt6 import QtGui
from sys import argv
from os import listdir, getcwd, rename, remove, path, mkdir

class FileOrganizer(QMainWindow):
    allFile = []
    txt = []
    png = []
    jpg = []
    mp4 = []
    mkv = []
    mov = []
    mp3 = []
    gif = []
    webp = []
    webm = []
    heic = []
    etc = []

    path = ''
	
    def __init__(self):
        super(FileOrganizer, self).__init__()
        loadUi('UI/Main.ui', self)
        
        self.setWindowIcon(QtGui.QIcon(getcwd() + '/logo/WHI3PER.png'))
        self.PATH.insert('C:/Users/' + getuser() + '/Desktop/')
        
        # ========================================================== #
        
        self.SHOW.clicked.connect(self.showDirectory)
        self.CATEGORIES.clicked.connect(self.categories)
        self.RENAME.clicked.connect(self.rename)
        self.DELETE.clicked.connect(self.delete)
        
    # ============================================================================================== #
    
    def checkDirectory(self):
        if path.exists(self.path):
            return True
        else:
            return False

    # ============================================================================================== #

    def clearVariables(self):
        self.allFile.clear()
        self.txt.clear()
        self.png.clear()
        self.jpg.clear()
        self.mp4.clear()
        self.mkv.clear()
        self.mov.clear()
        self.mp3.clear()
        self.gif.clear()
        self.webp.clear()
        self.webm.clear()
        self.heic.clear()
        self.etc.clear()
    
        path = ''
        
    # ============================================================================================== #
        
    def saveFileNames(self):
        self.clearVariables()
        self.path = self.PATH.text()
        
        if self.path[-2:] != '/':
            self.path = self.path + '/'

        if not self.checkDirectory():
            self.warning('None', 2)
        else:
            listDirectory = listdir(self.path)

            for item in listDirectory:
                if item[-4:] == '.cpp' or item[-4:] == '.txt' or item[-3:] == '.py':
                    self.txt.append(item)
                elif item[-4:] == '.png' or item[-4:] == '.PNG':
                    self.png.append(item)
                elif item[-4:] == '.jpg' or item[-4:] == '.JPG':
                    self.jpg.append(item)
                elif item[-4:] == '.mp4' or item[-4:] == '.MP4':
                    self.mp4.append(item)
                elif item[-4:] == '.mkv' or item[-4:] == '.MKV':
                    self.mkv.append(item)
                elif item[-4:] == '.mov' or item[-4:] == '.MOV':
                    self.mov.append(item)
                elif item[-4:] == '.mp3' or item[-4:] == '.MP3':
                    self.mp3.append(item)
                elif item[-4:] == '.gif' or item[-4:] == '.GIF':
                    self.gif.append(item)
                elif item[-5:] == '.webp' or item[-5:] == '.WEBP':
                    self.webp.append(item)
                elif item[-5:] == '.webm' or item[-5:] == '.WEBM':
                    self.webm.append(item)
                elif item[-5:] == '.heic' or item[-5:] == '.HEIC':
                    self.heic.append(item)
                else:
                    self.etc.append(item)

            self.allFile.append(self.txt)
            self.allFile.append(self.png)
            self.allFile.append(self.jpg)
            self.allFile.append(self.mp4)
            self.allFile.append(self.mkv)
            self.allFile.append(self.mov)
            self.allFile.append(self.mp3)
            self.allFile.append(self.gif)
            self.allFile.append(self.webp)
            self.allFile.append(self.webm)
            self.allFile.append(self.heic)
            self.allFile.append(self.etc)
        
    # ============================================================================================== #

    def showDirectory(self):
        self.LOGS.clear()
        self.LOGS.append('\t\t   *** Show Directory ***\n')
        
        self.saveFileNames()
        
        for type in self.allFile:
            if len(type) != 0:
                index = 1
                for file in type:
                    self.LOGS.append(f'[{index}/{len(type)}] -- {file}')
                    index += 1
                self.LOGS.append('')
    
    # ============================================================================================== #

    def categories(self):
        self.LOGS.clear()
        self.LOGS.append('\t\t    *** Categories ***\n')
        
        if not self.checkDirectory():
            self.warning('None', 2)
        else:
            if self.txt: self.gotoCategories(self.txt, 'TXT')
            if self.png: self.gotoCategories(self.png, 'PNG')
            if self.jpg: self.gotoCategories(self.jpg, 'JPG')
            if self.mp4: self.gotoCategories(self.mp4, 'MP4')
            if self.mkv: self.gotoCategories(self.mkv, 'MKV')
            if self.mov: self.gotoCategories(self.mov, 'MOV')
            if self.mp3: self.gotoCategories(self.mp3, 'MP3')
            if self.gif: self.gotoCategories(self.gif, 'GIF')
            if self.webp: self.gotoCategories(self.webp, 'WEBP')
            if self.webm: self.gotoCategories(self.webm, 'WEBM')
            if self.heic: self.gotoCategories(self.heic, 'HEIC')
            if self.etc: self.gotoCategories(self.etc, 'ETC')
    
    # ============================================================================================== #

    def gotoCategories(self, File, Format):
        self.LOGS.append('~ ' + Format)
        new_path = (self.path + '/' + Format + '/')
        
        if not path.exists(new_path):
            mkdir(new_path)
            
        for item in File:
            move((self.path + item), (new_path + item))

    # ============================================================================================== #
    
    def warning(self, Format: str, case: int):
        if case == 1:
            self.LOGS.append(f'Warning: There is no \'{Format}\' file or your request is invalid.')
        else:
            self.LOGS.append(f'Warning: This directory does not exist !')
        
    # ============================================================================================== #
        
    def rename(self):
        self.saveFileNames()
        self.LOGS.clear()
        self.LOGS.append('\t\t      *** Rename ***\n')

        if not self.checkDirectory():
            self.warning('None', 2)
        else:
            match(self.RENAME_COMBOBOX.currentText()):
                case 'TXT': self.gotoRename(self.txt, 'TXT', 4)
                case 'PNG': self.gotoRename(self.png, 'PNG', 4)
                case 'JPG': self.gotoRename(self.jpg, 'JPG', 4)
                case 'MP4': self.gotoRename(self.mp4, 'MP4', 4)
                case 'MKV': self.gotoRename(self.mkv, 'MKV', 4)
                case 'MOV': self.gotoRename(self.mov, 'MOV', 4)
                case 'MP3': self.gotoRename(self.mp3, 'MP3', 4)
                case 'GIF': self.gotoRename(self.gif, 'GIF', 4)
                case 'WEBP': self.gotoRename(self.webp, 'WEBP', 5)
                case 'WEBM': self.gotoRename(self.webm, 'WEBM', 5)
                case 'HEIC': self.gotoRename(self.heic, 'HEIC', 5)
        
    # ============================================================================================== #

    def gotoRename(self, File, Format, FormatLength):
        self.LOGS.append('~ ' + Format)
        number = 1

        if File:
            for item in File:
                if path.exists(self.path + str(number) + item[-FormatLength:]):
                    number += 1
                else:
                    self.LOGS.append(item)
                    rename((self.path + item), (self.path + str(number) + item[-FormatLength:]))
                    number += 1
                
            self.LOGS.append(f'\nResult: {len(File)} {Format} files have been successfully renamed.')
        else:
            self.warning(Format, 1)
        
    # ============================================================================================== #
        
    def delete(self):
        self.saveFileNames()
        self.LOGS.clear()
        self.LOGS.append('\t\t      *** Delete ***\n')
        
        if not self.checkDirectory():
            self.warning('None', 2)
        else:
            match(self.DELETE_COMBOBOX.currentText()):
                case 'ALL':
                    self.LOGS.append('~ ALL')
                    
                    for type in self.allFile:
                        if len(type) != 0:
                            for file in type:
                                self.LOGS.append(file)
                                remove(self.path + file)
                    self.LOGS.append('\nResult: All files have been successfully deleted.')
                
                case 'TXT': self.gotoDelete(self.txt, 'TXT')
                case 'PNG': self.gotoDelete(self.png, 'PNG')
                case 'JPG': self.gotoDelete(self.jpg, 'JPG')
                case 'MP4': self.gotoDelete(self.mp4, 'MP4')
                case 'MKV': self.gotoDelete(self.mkv, 'MKV')
                case 'MOV': self.gotoDelete(self.mov, 'MOV')
                case 'MP3': self.gotoDelete(self.mp3, 'MP3')
                case 'GIF': self.gotoDelete(self.gif, 'GIF')
                case 'WEBP': self.gotoDelete(self.webp, 'WEBP')
                case 'WEBM': self.gotoDelete(self.webm, 'WEBM')
                case 'HEIC': self.gotoDelete(self.heic, 'HEIC')
                case 'ETC': self.gotoDelete(self.etc, 'ETC')
        
    # ============================================================================================== #

    def gotoDelete(self, File, Format):
        self.LOGS.append('~ ' + Format)
        if File:
            for item in File:
                self.LOGS.append(item)
                remove(self.path + item)
            self.LOGS.append(f'\nResult: {len(File)} {Format} files have been successfully deleted.')
        else:
            self.warning(Format, 1)

    # ============================================================================================== #