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

import yamldoc
import QProgEdit
from QProgEdit.py3compat import *
from academicmarkdown import build

df = yamldoc.DocFactory(QProgEdit)
s = str(df)
print(s)
build.setStyle('modern')
build.MD(s, u'readme.md')
build.PDF(s, u'readme.pdf')
