

class ApiRequestException(Exception):
    def __init__(self):
        super().__init__('API request error')


class ApiOtherException(Exception):
    def __init__(self):
        super().__init__('API non-request error')
