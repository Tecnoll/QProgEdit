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

import sip
sip.setapi('QString', 1)

import sys
from PyQt4 import QtGui, QtCore
from QProgEdit import QTabManager, validate

def cursorRowChanged(index, rowFrom, rowTo):

	print(u'curorRowChanged(): %d, %d, %d' % (index, rowFrom, rowTo))

def focusLost(index):
	
	print(u'focusOut(): %s' % index)
	
def focusReceived(index):

	print(u'focusReceived(): %s' % index)

def handlerButtonClicked(index):

	print(u'handlerButtonClicked(): %s' % index)

def activateSymbolTree(treeWidgetItem):

	treeWidgetItem.activate()

def main():
	
	"""Runs a simple QProgEdit demonstration."""

	validate.addPythonBuiltins(['builtin_var'])
	app = QtGui.QApplication(sys.argv)

	treeWidgetItem1 = QtGui.QTreeWidgetItem([u'Tab 1'])
	treeWidgetItem3 = QtGui.QTreeWidgetItem([u'Tab 3'])
	symbolTree = QtGui.QTreeWidget()
	symbolTree.addTopLevelItem(treeWidgetItem1)
	symbolTree.addTopLevelItem(treeWidgetItem3)
	symbolTree.itemActivated.connect(activateSymbolTree)

	tabManager = QTabManager(handlerButtonText=u'apply')
	tabManager.setWindowIcon(QtGui.QIcon.fromTheme(u'accessories-text-editor'))
	tabManager.setWindowTitle(u'QProgEdit')
	tabManager.resize(800, 600)

	tabManager.cursorRowChanged.connect(cursorRowChanged)
	tabManager.focusLost.connect(focusLost)
	tabManager.focusReceived.connect(focusReceived)
	tabManager.handlerButtonClicked.connect(handlerButtonClicked)

	tabManager.addTab(u'Tab 1')
	tabManager.tab().setLang(u'Python')
	tabManager.tab().setSymbolTree(treeWidgetItem1)
	tabManager.tab().setText(open(__file__).read())

	tabManager.addTab(u'Tab 2')
	tabManager.tab(1).setText(u'Some plain text')

	tabManager.addTab(u'Tab 3')
	tabManager.tab(u'Tab 3').setLang(u'Python')
	tabManager.tab(u'Tab 3').setSymbolTree(treeWidgetItem3)
	tabManager.tab(u'Tab 3').setText(
		u'def test():\n\tprint undefined_var\n\tbuiltin_var\n\ntest()\n')

	layout = QtGui.QHBoxLayout()
	layout.addWidget(symbolTree)
	layout.addWidget(tabManager)
	container = QtGui.QWidget()
	container.setLayout(layout)
	container.show()

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
