class InvalidDateFormatError(Exception):
    """Exception to be raised when a user passes date in any other format than YYYY-MM-DD."""

    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors


class InvalidPathException(Exception):
    """Exception to be raised when a user passes an invalid directory to download into."""

    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors
