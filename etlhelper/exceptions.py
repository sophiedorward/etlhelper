"""
ETLHelper exceptions are derived from the ETLHelperError base class.

"""


class ETLHelperError(Exception):
    """Base class for exceptions in this module"""


class ETLHelperConnectionError(ETLHelperError):
    """Exception raised for bad database connections"""


class ETLHelperQueryError(ETLHelperError):
    """Exception raised for SQL query errors and similar"""


class ETLHelperDbParamsError(ETLHelperError):
    """Exception raised for bad database parameters"""


class ETLHelperExtractError(ETLHelperError):
    """Exception raised when extracting data."""


class ETLHelperInsertError(ETLHelperError):
    """Exception raised when inserting data."""


class ETLHelperAbort(ETLHelperError):
    """Exception raised when `abort` is called."""


class ETLHelperHelperError(ETLHelperError):
    """Exception raised when helper selection fails."""


class ETLHelperBadIdentifierError(ETLHelperError):
    """
    Exception raised when identifier contains invalid characters.  This may
    indicate an attempt at SQL injection.
    """
