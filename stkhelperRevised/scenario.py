from win32api import GetSystemMetrics
from comtypes.client import CreateObject
from comtypes.gen import STKObjects
from comtypes import COMError

class Scenario:

    def __init__(self, application, name, timePeriod):
        
        
        self.__guardian = application
        self.name = name
        
        application.root.NewScenario(' ','_')
        self.__scenario = application.root.CurrentScenario
        self.__scenario = self.__scenario.QueryInterface(STKObjects.IAgScenario)
        try:
            self.__scenario.SetTimePeriod('Today',str(timePeriod))
        except COMError:
            raise ValueError, "Time period not properly formatted"
        
    def GetGuardian(self):
        return self.__guardian