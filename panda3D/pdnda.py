from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model_Ground2 = loader.loadModel('models/Ground2/Ground2.egg')
        self.model_Ground2.reparentTo(render)
        self.model_Ground2.setScale(50)
        self.model_Ground2.setPos(0,0,0)
        self.Station()
        self.home()
        self.people()
        base.camLens.setFov(50)


    def Station(self):
        self.model_StationWagon = loader.loadModel('models/StationWagon/StationWagon.egg')
        self.model_StationWagon.reparentTo(render)
        self.model_StationWagon.setPos(30, -10, 3)
        self.model_StationWagon.setHpr(180, 0, 0)
        self.model_StationWagon.setScale(1.5)
        self.model_BeachChair = loader.loadModel('models/BeachChair/BeachChair.egg')
        self.model_BeachChair.reparentTo(render)
        self.model_BeachChair.setPos(-12,-20,0)
        self.model_BeachChair.setHpr(180, 0, 0)
        self.model_BeachChair.setScale(2)

    def home (self):
        self.model_FarmHouse = loader.loadModel('models/FarmHouse/FarmHouse.egg')
        self.model_FarmHouse.reparentTo(render)
        self.model_FarmHouse.setHpr(180, 0, 0)

    def people (self):
        self.model_RandomGuy3 = loader.loadModel('models/RandomGuy3/RandomGuy3.egg')
        self.model_RandomGuy3.reparentTo(render)
        self.model_RandomGuy3.setHpr(180, 0, 0)
        self.model_RandomGuy3.setPos(0, -30, 0)
        self.model_RandomGuy3.setScale(1.2)


baze = Game()
baze.run()