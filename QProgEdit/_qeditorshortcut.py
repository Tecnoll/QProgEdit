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

from QProgEdit.py3compat import *
from QProgEdit.qt import QtGui, QtCore

class QEditorShortcut(QtGui.QShortcut):

	def __init__(self, parent, keySequence, target,
		context=QtCore.Qt.WidgetWithChildrenShortcut):

		super(QEditorShortcut, self).__init__(QtGui.QKeySequence(keySequence),
			parent, context=context)
		self.activated.connect(target)
