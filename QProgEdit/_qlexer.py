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

from PyQt4 import QtGui, QtCore
from PyQt4 import Qsci
from QProgEdit import QColorScheme

class QLexer(Qsci.QsciLexer):

	"""
	desc:
		A themeable wrapper around the standard Lexer system.
	"""

	def __init__(self, editor, lang=u'text', colorScheme=u'Default'):

		"""
		desc:
			Constructor.

		arguments:
			editor:
				desc:	The parent QEditor.
				type:	QEditor

		keywords:
			lang:
				desc:	The language.
				type:	unicode
			colorScheme:
				desc:	The color scheme.
				type:	unicode
		"""

		self.editor = editor

		# If the language matches an existing Lexer, morph into that
		# pre-existing lexer class
		lexerClass = u'QsciLexer%s' % lang.capitalize()
		if hasattr(Qsci, lexerClass):
			self.__class__ = getattr(Qsci, lexerClass)
			getattr(Qsci, lexerClass).__init__(self, editor)
		elif lang.lower() == 'opensesame':
			self.__class__ = Qsci.QsciLexerPython
			Qsci.QsciLexerPython.__init__(self, editor)
		else:
			super(QLexer, self).__init__(editor)

		# Set the font based on the configuration
		font = QtGui.QFont(self.editor.cfg.qProgEditFontFamily,
				self.editor.cfg.qProgEditFontSize)
		self.setFont(font)

		# Apply the color theme
		if hasattr(QColorScheme, colorScheme):
			colorScheme = getattr(QColorScheme, colorScheme)
		else:
			colorScheme = QColorScheme.Default
		if u'Background' in colorScheme:
			self.setPaper(QtGui.QColor(colorScheme[u'Background']))
			self.setDefaultPaper(QtGui.QColor(colorScheme[u'Background']))
		if u'Default' in colorScheme:
			self.editor.setCaretForegroundColor(QtGui.QColor(
				colorScheme[u'Default']))
			self.setDefaultColor(QtGui.QColor(colorScheme[u'Default']))
		if u'Selection background' in colorScheme:
			self.editor.setSelectionBackgroundColor(QtGui.QColor(
				colorScheme[u'Selection background']))
		if u'Selection foreground' in colorScheme:
			self.editor.setSelectionForegroundColor(QtGui.QColor(
				colorScheme[u'Selection foreground']))
		if u'Caret-line background' in colorScheme:
			self.editor.setCaretLineBackgroundColor(QtGui.QColor(
				colorScheme[u'Caret-line background']))
		for style in range(50):
			styleName = str(self.description(style))
			if styleName != u'' and styleName in colorScheme:
				if isinstance(colorScheme[styleName], tuple):
					color, bold, italic = colorScheme[styleName]
					self.setColor(QtGui.QColor(colorScheme[styleName]), style)
					_font = QtGui.QFont(font)
					_font.setBold(bold)
					_font.setItalic(italic)
					self.setFont(_font, style)
				else:
					color = colorScheme[styleName]
				self.setColor(QtGui.QColor(color), style)

	def description(self, style):

		"""
		desc:
			Gives a style description for the generic Lexer.

		arguments:
			style:
				desc:	The style number.
				type:	int

		returns:
			desc:	The 'Default' QString for style 0 and empty QStrings for all
					other styles.
			type:	QString
		"""

		if style == 0:
			return QtCore.QString(u'Default')
		else:
			return QtCore.QString()
