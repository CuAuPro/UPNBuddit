#!/usr/bin/env python
""" UPNBuddit is a powerful tool for bulk editing of remittance slips.

With its advanced technology and efficient interface,
UPNBuddit makes it easy to quickly and accurately edit large numbers
of remittance slips. Whether you need to make changes to a single field
or update multiple fields at once, UPNBuddit has the tools you need to get
the job done. Its user-friendly interface allows even novice users to make
complex edits with ease, making it the ideal choice for businesses and
organizations that need to process large volumes of remittance slips.
Try UPNBuddit today and streamline your bulk remittance slip editing process!


This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Kristjan Cuznar"
__contact__ = "kristjancuznar0@gmail.com"
__copyright__ = ""
__credits__ = ["Coffee"]
__date__ = "2025/01/12"
__deprecated__ = False
__email__ =  "kristjancuznar0@gmail.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.1.2"

import argparse
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog

import gui.menu as menu
import engine.converter as converter


class Menu(QtWidgets.QMainWindow, menu.Ui_MainWindow):
    def __init__(self, parent=None, args=None):
        super(Menu, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('UPNBuddit')
        
        self.pb_start.clicked.connect(self.evt_start)
        self.pb_importConfig.clicked.connect(self.evt_importConfig)
        self.pb_importList.clicked.connect(self.evt_importList)
        self.pb_importTemplates.clicked.connect(self.evt_importTemplates)
        self.pb_selectOutputFIle.clicked.connect(self.evt_selectOutputFIle)
        self.cb_onlyAdults.clicked.connect(self.evt_cb_onlyAdults)
        
        self.args = args
        self.default_path = '.'
        
    
    def evt_start(self):
        self.l_info.setText("Zacetek izvoza.")
        ret = converter.run(self.args)
        if ret == 0:
            print("Generiran dokument: {}".format(self.args.output_path))
            self.l_info.setText("Generiran dokument: {}".format(self.args.output_path))
        elif ret == -1:
            self.l_info.setText("Konfiguracijske datoteke ni mogoce najti.")
        elif ret == -2:
            self.l_info.setText("Vhodne datoteke ni mogoce najti.")
        elif ret == -3:
            self.l_importTemplates.setText("Mape s predlogami ni mogoce najti.")
        elif ret == -4:
            self.l_info.setText("Napaka pri izvozu. Struktura konfiguracijske ali vhodne datoteke ni pravilna.")
        elif ret == -5:
            self.l_info.setText("Napaka pri izvozu. Napaka pri rojstnih dnevih.")
        return
    
    def evt_importConfig(self):
        self.args.config_path = QFileDialog.getOpenFileName( self, 'Select file', self.default_path,"(*.xls)")[0]
        self.l_importConfig.setText(self.args.config_path)
        return
    
    def evt_importList(self):
        self.args.input_path = QFileDialog.getOpenFileName( self, 'Select file', self.default_path,"(*.xls)")[0]
        self.l_importList.setText(self.args.input_path)
        return

    def evt_importTemplates(self):
        self.args.template_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.l_importTemplates.setText(self.args.template_path)
        return
    
    def evt_selectOutputFIle(self):
        self.args.output_path = QFileDialog.getSaveFileName(self, 'Select file', self.args.output_path, "txt(*.txt)")[0]
        self.l_selectOutputFIle.setText(self.args.output_path)
        return
    
    def evt_cb_onlyAdults(self):
        self.args.only_adults = self.cb_onlyAdults.isChecked()
        print(self.args.only_adults)
        return
    
if __name__ == "__main__":
    print("Orodje za množično urejanje položnic.")
    print("Verzija: {} || {}, {}".format(__version__, __author__,__contact__))
    
    parser = argparse.ArgumentParser(description='Tool for bulk editing of remittance slips.')
    parser.add_argument("-m", "--manual-mode", action='store_true',
                        help="Tool mode (default: %(default)s)")
    parser.add_argument("-t", "--template-path", type=str, default='templates/',
                        help="Template folder path (default: %(default)s)") 
    parser.add_argument("-i", "--input-path", type=str, default='seznam.xls',
                        help="Input file path (default: %(default)s)")
    parser.add_argument("-o", "--output-path", type=str, default='export.txt',
                        help="Output file path (default: %(default)s)")
    parser.add_argument("-c", "--config-path", type=str, default='config.xls',
                        help="Config file path (default: %(default)s)")
    parser.add_argument("-a", "--only-adults", type=bool, default=False,
                        help="Export only for adults (default: %(default)s)")
    args = parser.parse_args()

    if args.manual_mode == True:
        ret = converter.run(args)
        if ret == 0:
            print("Generiran dokument: {}".format(args.output_path))
        else:
            pass
    else:
        app = QApplication(sys.argv)
        form = Menu(args=args)
        form.show()
        app.exec_()

        


