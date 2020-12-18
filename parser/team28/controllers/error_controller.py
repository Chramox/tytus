from utils.decorators import singleton
from models.error import Error
from models.type_error import get_type_error


@singleton
class ErrorController(object):
    def __init__(self):
        self._idError = 0
        self._errorsList = []

        self._idExecutionError = 0
        self._executionErrorList = []

    def getList(self):
        return self._errorsList

    def getExeErrList(self):
        return self._executionErrorList

    def destroy(self):
        self._idError = 0
        self._errorsList = []

        self._idExecutionError = 0
        self._executionErrorList = []

    def add(self, noType, errorType, desc, line, column):
        numberError, description = get_type_error(noType)
        self._idError += 1
        description += desc

        self._errorsList.append(Error(self._idError, errorType, numberError,
                                      description, line, column))

    def addExecutionError(self, noType, errorType, desc, line, column):
        numberError, description = get_type_error(noType)
        self._idExecutionError += 1
        description += desc

        self._executionErrorList.append(Error(self._idExecutionError, errorType, numberError,
                                              description, line, column))
