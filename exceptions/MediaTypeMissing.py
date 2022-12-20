__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"



class MediaTypeMissing(Exception):
    def __init__(self):
        self.msg = 'Media type not entered.  Please retry but with media type'
        super().__init__(self.msg)