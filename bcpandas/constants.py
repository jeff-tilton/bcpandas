# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:20:19 2019

@author: ydima
"""

import os


class BCPandasException(Exception):
    pass


class BCPandasValueError(BCPandasException):
    pass


# BCP terms
IN = "in"
OUT = "out"
QUERYOUT = "queryout"
TABLE = "table"
VIEW = "view"
QUERY = "query"

DIRECTIONS = (IN, OUT, QUERYOUT)
SQL_TYPES = (TABLE, VIEW, QUERY)
IF_EXISTS_OPTIONS = ("append", "replace", "fail")


# Text settings
_DELIMITER_OPTIONS = (",", "|", "\t")
QUOTECHAR = '"'
_QUOTECHAR_OPTIONS = ('"', "'", "`", "~")
NEWLINE = os.linesep

# BCP Format File terms
SQLCHAR = "SQLCHAR"
sql_collation = "SQL_Latin1_General_CP1_CI_AS"


error_msg = """Data contains all of the possible {typ} characters {opts}, 
cannot use BCP to import it. Replace one of the possible {typ} characters in
your data, or use another method besides bcpandas.

Further background:

https://docs.microsoft.com/en-us/sql/relational-databases/import-export/specify-field-and-row-terminators-sql-server#characters-supported-as-terminators
"""


def get_delimiter(df):
    for delim in _DELIMITER_OPTIONS:
        if not df.applymap(lambda x: delim in x if isinstance(x, str) else False).any().any():
            return delim
    raise BCPandasValueError(error_msg.format(typ="delimiter", opts=_DELIMITER_OPTIONS))


def get_quotechar(df):
    for qc in _QUOTECHAR_OPTIONS:
        if not df.applymap(lambda x: qc in x if isinstance(x, str) else False).any().any():
            return qc
    raise BCPandasValueError(error_msg.format(typ="quote", opts=_QUOTECHAR_OPTIONS))
