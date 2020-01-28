from stkhelper.scenarioobject import ScenarioObjectfrom stkhelper.toolbox import Toolboxfrom comtypes.gen import STKObjectsclass AreaTarget(ScenarioObject):    """        An area target object to be added to the scenario. Inherits from    stkhelper.ScenarioObject.        Parameters:        guardian(stkhelper.scenario): The scenario for the area target to be                                    placed into.        name(str): Name of the area target.        coordList(list): List of lat/lon pairs to draw the area target        """    def __init__(self, guardian, name=None, coordList=None):        #TODO Make coordList mandatory        self.guardian = guardian        self.name = name        self.coordinates = coordList                self.root = self.guardian.guardian.root                self.centroid = Toolbox.ComputeCentroid(self.coordinates)        self.root.BeginUpdate()                self.reference = self.root.CurrentScenario.Children.New(STKObjects.eAreaTarget,self.name)        self.reference = self.reference.QueryInterface(STKObjects.IAgAreaTarget)        self.reference.AreaType = STKObjects.ePattern        patterns = self.reference.AreaTypeData        patterns = patterns.QueryInterface(STKObjects.IAgAreaTypePatternCollection)                for i in range(len(self.coordinates)):            patterns.Add(self.coordinates[i][0],                         self.coordinates[i][1])                    self.reference.AutoCentroid = True                self.root.EndUpdate()            def GetAccess(self,scenarioObject):        #TODO Caused error from inherited method. Fix this in scenarioobjects        self.root.BeginUpdate()        access = super().GetAccess(scenarioObject)        self.root.EndUpdate()                return access        def SetElevationConstraint(self, angle):        self.root.ExecuteCommand("SetConstraint " + \                                 "*/AreaTarget/" + str(self.name) + \                                 " ElevationAngle " + str(float(angle)))