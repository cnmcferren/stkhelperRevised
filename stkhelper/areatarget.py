from stkhelper.scenarioobject import ScenarioObjectfrom stkhelper.toolbox import Toolboxfrom comtypes.gen import STKObjectsclass AreaTarget(ScenarioObject):    def __init__(self, guardian, name=None, coordList=None):        self.guardian = guardian        self.name = name        self.coordinates = coordList                self.root = guardian.guardian.root                self.center =Toolbox.ComputeCenterTarget(points)        self.root.BeginUpdate()                self.reference = self.root.CurrentScenario.Children.New(STKObjects.eAreaTarget,self.name)        self.reference = self.reference.QueryInterface(STKObjects.IAgAreaTarget)        self.reference.AreaType = STKObjects.ePattern        patterns = self.reference.AreaTypeData        patterns = patterns.QueryInterface(STKObjects.IAgAreaTypePatternCollection)                for i in range(len(self.coordinates)):            patterns.Add(self.coordinates[i][0],                         self.coordinates[i][1])                    self.reference.AutoCentroid = True                self.centroid = Toolbox.ComputeCentroid(self.coordinates)                self.root.EndUpdate()            def GetAccess(self,scenarioObject):        self.root.BeginUpdate()        access = super().GetAccess(scenarioObject)        self.root.EndUpdate()                return access