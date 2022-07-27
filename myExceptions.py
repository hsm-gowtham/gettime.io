class myExceptions(Exception):
    def __init__(self, msg='Something Went Wrong'):
        super().__init__(msg)


class WrongFormat(myExceptions):
    def __init__(self,index = '',line='', msg='Wrong Format found' ):
        super().__init__(msg)
        self.index = index
        self.line = line