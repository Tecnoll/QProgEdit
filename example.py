#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
This file is part of QProgEdit.

QProgEdit is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

QProgEdit is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with QProgEdit.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys
from PyQt4 import QtGui, QtCore
from QProgEdit import QTabManager

def main():
	
	"""Runs a simple QProgEdit demonstration."""

	app = QtGui.QApplication(sys.argv)
	tabManager = QTabManager(defaultLang=u'python')
	tabManager.setWindowIcon(QtGui.QIcon.fromTheme(u'accessories-text-editor'))
	tabManager.setWindowTitle(u'QProgEdit')
	tabManager.resize(800, 600)
	tabManager.addTab(u'Tab 1', lang=u'Python')
	tabManager.setText(open(__file__).read())
	tabManager.addTab(u'Tab 2', lang=u'text')
	tabManager.setText(u'Spécial character tèst')
	print tabManager.text()
	tabManager.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
