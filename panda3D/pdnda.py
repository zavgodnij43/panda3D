from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties, CollisionTraverser, CollisionHandlerPusher
from direct.task import Task
import math
from direct.showbase import Audio3DManager
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode
import time
from panda3d.core import CollisionNode, CollisionSphere, CollisionBox, Point3, CollisionPlane, Plane, Vec3
from panda3d.core import AmbientLight, DirectionalLight, PointLight, Spotlight, PerspectiveLens, Vec4
from panda3d.core import loadPrcFileData
from direct.gui.DirectGui import DirectFrame, DirectButton

loadPrcFileData('', 'win-size 1920 1080')



class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model_Ground2 = loader.loadModel('models/Ground2/Ground2.egg')
        self.model_Ground2.reparentTo(render)
        self.model_Ground2.setPos(0,0,0)
        base.camLens.setFov(50)
        self.StationWagon = loader.loadModel('models/StationWagon/StationWagon.egg')
        self.StationWagon.reparentTo(render)
        self.StationWagon.setPos(30, -10, 3)
        self.StationWagon.setHpr(180, 0, 0)
        self.StationWagon.setScale(1.5)
        self.Beach_Chair = loader.loadModel('models/Beach_Chair/Beach_Chair.egg')
        self.Beach_Chair.reparentTo(render)
        self.Beach_Chair.setPos(-12, -20, 0)
        self.Beach_Chair.setHpr(180, 0, 0)
        self.Beach_Chair.setScale(1.5)
        self.FarmHouse = loader.loadModel('models/FarmHouse/FarmHouse.egg')
        self.FarmHouse.reparentTo(render)
        self.FarmHouse.setHpr(180, 0, 0)
        self.player = loader.loadModel('models/RandomGuy3/RandomGuy3.egg')
        self.player.reparentTo(render)
        self.player.setHpr(180, 0, 0)
        self.player.setPos(0, -30, 0)
        self.player.setScale(1.2)
        self.wintersky = loader.loadModel('models/sunset/sunset.egg')
        self.wintersky.reparentTo(render)
        self.BuildingCluster1 = loader.loadModel('models/BuildingCluster1/BuildingCluster1.egg')
        self.BuildingCluster1.reparentTo(render)
        self.BuildingCluster1.setPos(-30, 35, 0)
        self.BuildingCluster1.setHpr(180, 0, 0)
        self.BuildingCluster2 = loader.loadModel('models/BuildingCluster2/BuildingCluster2.egg')
        self.BuildingCluster2.reparentTo(render)
        self.BuildingCluster2.setPos(30, 35, 0)
        self.BuildingCluster3 = loader.loadModel('models/BuildingCluster3/BuildingCluster3.egg')
        self.BuildingCluster3.reparentTo(render)
        self.BuildingCluster3.setPos(-60, -20, 0)
        self.BuildingCluster4 = loader.loadModel('models/BuildingCluster4/BuildingCluster4.egg')
        self.BuildingCluster4.reparentTo(render)
        self.BuildingCluster4.setPos(-40, -80, -5)
        self.BuildingCluster4.setHpr(90, 0, 0)
        self.BuildingCluster5 = loader.loadModel('models/BuildingCluster5/BuildingCluster5.egg')
        self.BuildingCluster5.reparentTo(render)
        self.BuildingCluster5.setPos(70, -30, -5)
        self.BuildingCluster5.setHpr(270, 0, 0)
        self.ParkFountain = loader.loadModel('models/ParkFountain/ParkFountain.egg')
        self.ParkFountain.reparentTo(render)
        self.ParkFountain.setPos(15, -80, 0)
        self.ParkFountain.setScale(2)


        # камера
        self.disableMouse()
        self.camera_distance = 60
        self.camera_height = 10
        self.camera_angle_h = 0

        # Менеджер колізій
        self.cTrav = CollisionTraverser()
        self.pusher = CollisionHandlerPusher()


        # # 2️⃣ Колізія для стійки
        # counter_min_pt, counter_max_pt = self.counter.getTightBounds()
        # # print(big_table_min_pt, big_table_max_pt)
        # counter_solid_1 = CollisionBox(counter_min_pt, (counter_min_pt[0] + 6, counter_max_pt[1], counter_max_pt[2]))
        # counter_solid_2 = CollisionBox(counter_min_pt, (counter_max_pt[0], counter_min_pt[1] + 6, counter_max_pt[2]))
        # counter_node = CollisionNode('counter')
        # counter_node.addSolid(counter_solid_1)
        # counter_node.addSolid(counter_solid_2)
        # counter_np = render.attachNewNode(counter_node)
        # # Показати бокс (для тесту)
        # # counter_np.show()  # побачити колізію

        # 2️⃣ Колізія для гравця (сфера навколо моделі)
        player_min_pt, player_max_pt = self.player.getTightBounds()
        # print(player_min_pt, player_max_pt)
        radius = (player_max_pt.z - player_min_pt.z) / 2
        radius *= 0.6
        player_solid = CollisionSphere(0, 0, 0 + radius, radius)
        player_node = CollisionNode("player")
        player_node.addSolid(player_solid)
        player_nodepath = self.player.attachNewNode(player_node)
        #player_nodepath.show()
        # машина
        StationWagon_min_pt, StationWagon_max_pt = self.StationWagon.getTightBounds()
        # print(StationWagon_min_pt, StationWagon_max_pt)
        StationWagon_solid = CollisionBox(StationWagon_min_pt, StationWagon_max_pt)
        StationWagon_node = CollisionNode('StationWagon')
        StationWagon_node.addSolid(StationWagon_solid)
        StationWagon_np = render.attachNewNode(StationWagon_node)
        # StationWagon_np.show()

        Beach_Chair_min_pt, Beach_Chair_max_pt = self.Beach_Chair.getTightBounds()
        # print(Beach_Chair_min_pt, Beach_Chair_max_pt)
        Beach_Chair_solid = CollisionBox(Beach_Chair_min_pt, Beach_Chair_max_pt)
        Beach_Chair_node = CollisionNode('Beach_Chair')
        Beach_Chair_node.addSolid(Beach_Chair_solid)
        Beach_Chair_np = render.attachNewNode(Beach_Chair_node)
        # Beach_Chair_np.show()

        FarmHouse_min_pt, FarmHouse_max_pt = self.FarmHouse.getTightBounds()
        # print(FarmHouse_min_pt, FarmHouse_max_pt)
        FarmHouse_solid = CollisionBox(FarmHouse_min_pt, FarmHouse_max_pt)
        FarmHouse_node = CollisionNode('FarmHouse')
        FarmHouse_node.addSolid(FarmHouse_solid)
        FarmHouse_np = render.attachNewNode(FarmHouse_node)
        # FarmHouse_np.show()

        BuildingCluster1_min_pt, BuildingCluster1_max_pt = self.BuildingCluster1.getTightBounds()
        # print(BuildingCluster1_min_pt, BuildingCluster1_max_pt)
        BuildingCluster1_solid = CollisionBox(BuildingCluster1_min_pt, BuildingCluster1_max_pt)
        BuildingCluster1_node = CollisionNode('BuildingCluster1')
        BuildingCluster1_node.addSolid(BuildingCluster1_solid)
        BuildingCluster1_np = render.attachNewNode(BuildingCluster1_node)
        # BuildingCluster1_np.show()

        BuildingCluster2_min_pt, BuildingCluster2_max_pt = self.BuildingCluster2.getTightBounds()
        # print(BuildingCluster2_min_pt, BuildingCluster2_max_pt)
        BuildingCluster2_solid = CollisionBox(BuildingCluster2_min_pt, BuildingCluster2_max_pt)
        BuildingCluster2_node = CollisionNode('BuildingCluster2')
        BuildingCluster2_node.addSolid(BuildingCluster2_solid)
        BuildingCluster2_np = render.attachNewNode(BuildingCluster2_node)
        # BuildingCluster2_np.show()

        BuildingCluster3_min_pt, BuildingCluster3_max_pt = self.BuildingCluster3.getTightBounds()
        # print(BuildingCluster3_min_pt, BuildingCluster3_max_pt)
        BuildingCluster3_solid = CollisionBox(BuildingCluster3_min_pt, BuildingCluster3_max_pt)
        BuildingCluster3_node = CollisionNode('BuildingCluster3')
        BuildingCluster3_node.addSolid(BuildingCluster3_solid)
        BuildingCluster3_np = render.attachNewNode(BuildingCluster3_node)

        BuildingCluster4_min_pt, BuildingCluster4_max_pt = self.BuildingCluster4.getTightBounds()
        # print(BuildingCluster4_min_pt, BuildingCluster4_max_pt)
        BuildingCluster4_solid = CollisionBox(BuildingCluster4_min_pt, BuildingCluster4_max_pt)
        BuildingCluster4_node = CollisionNode('BuildingCluster4')
        BuildingCluster4_node.addSolid(BuildingCluster4_solid)
        BuildingCluster4_np = render.attachNewNode(BuildingCluster4_node)
        # BuildingCluster4_np.show()

        BuildingCluster5_min_pt, BuildingCluster5_max_pt = self.BuildingCluster5.getTightBounds()
        # print(BuildingCluster5_min_pt, BuildingCluster5_max_pt)
        BuildingCluster5_solid = CollisionBox(BuildingCluster5_min_pt, BuildingCluster5_max_pt)
        BuildingCluster5_node = CollisionNode('BuildingCluster5')
        BuildingCluster5_node.addSolid(BuildingCluster5_solid)
        BuildingCluster5_np = render.attachNewNode(BuildingCluster5_node)
        # BuildingCluster5_np.show()

        ParkFountain_min_pt, ParkFountain_max_pt = self.ParkFountain.getTightBounds()
        # print(ParkFountain_min_pt, ParkFountain_max_pt)
        ParkFountain_solid = CollisionBox(ParkFountain_min_pt, ParkFountain_max_pt)
        ParkFountain_node = CollisionNode('ParkFountain')
        ParkFountain_node.addSolid(ParkFountain_solid)
        ParkFountain_np = render.attachNewNode(ParkFountain_node)
        # ParkFountain_np.show()

        # 4️⃣ Додаємо обробку зіткнень
        self.pusher.addCollider(player_nodepath, self.player)
        self.cTrav.addCollider(player_nodepath, self.pusher)

        props = WindowProperties()
        props.setCursorHidden(True)
        self.win.requestProperties(props)

        self.center_mouse()

        #  Клавіші
        self.keys = {"w": False, "s": False, "a": False, "d": False}
        for key in self.keys.keys():
            self.accept(key, self.set_key, [key, True])
            self.accept(f"{key}-up", self.set_key, [key, False])

        # Мишкаmera
        self.accept("escape", exit)  # Вихід по ESC
        self.taskMgr.add(self.update, "UpdateTask")
        self.taskMgr.add(self.mouse_update, "MouseTask")

        # налаштування світла
        ambient = AmbientLight("ambient")
        ambient.setColor(Vec4(0.2, 0.1, 0.1, 1))
        ambient_np =render.attachNewNode(ambient)
        render.setLight(ambient_np)

        # спрямоване світло (сонце)
        sun = DirectionalLight('sun')
        sun.setColor(Vec4(0.5, 0.5, 0.5, 1))  # теплий відтінок сонця
        sun_np = render.attachNewNode(sun)
        sun_np.setHpr(20, -70, 0)  # кут падіння світла
        render.setLight(sun_np)

        # точкове світло (лампочка)
        lamp = PointLight('lamp')
        lamp.setColor(Vec4(5, 2, 2, 1))  # тепле світло
        lamp_np = self.player.attachNewNode(lamp)
        lamp_np.setPos(0, 0, 0)  # положення лампи
        render.setLight(lamp_np)
        lamp.setAttenuation((1, 0.08, 0))

        # прожектор (світло у формі конуса)
        spot = Spotlight('spot')
        spot.setColor(Vec4(1, 1, 1, 1))
        lens = PerspectiveLens()
        lens.setFov(100)  # ширина конуса освітлення
        spot.setLens(lens)

        spot_np = render.attachNewNode(spot)
        spot_np.setPos(10, 50, 0)
        spot_np.lookAt(self.player)  # спрямування на об’єкт
        render.setLight(spot_np)

        # Створюємо звуковий менеджер
        self.audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)

        # Фонова музика
        self.bg_music = loader.loadMusic('sounds/Гаррі Поттер.mp3')
        self.bg_music.setLoop(True)
        self.bg_music.play()

        # Звук при дії
        self.washing_sound = loader.loadSfx('sounds/Гаррі Поттер.mp3')

        self.start_time = time.time()  # ⬅️
        self.timer_text = OnscreenText(
            text="Time: 0 s",
            pos=(-1, 0.7),
            scale=0.07,
            mayChange=True,
            align=TextNode.ALeft,  # вирівнювання
            fg=(1, 1, 1, 1),  # колір (білий)
        )

        # Додаємо задачу, яка виконується щотакту
        self.taskMgr.add(self.update_timer, "UpdateTimerTask")

        # ⬇️⬇️⬇️
        # прапорець меню
        self.menu_open = False

        # створюємо фрейм меню (фон меню)
        self.menu_frame = DirectFrame(
            frameColor=(1, 0, 0, 0.7),  # напівпрозорий чорний
            frameSize=(-0.5, 0.5, -0.5, 0.5),
            pos=(0, 0, 0)
        )
        self.menu_frame.hide()  # спочатку меню приховане

        # створюємо 3 кнопки в меню
        self.buttons = []
        for i in range(3):
            btn = DirectButton(
                text=f"Button {i + 1}",
                scale=0.07,
                pos=(0, 0, 0.2 - i * 0.2),
                parent=self.menu_frame,
                command=self.button_clicked,
                extraArgs=[i + 1]
            )
            self.buttons.append(btn)

        # прив’язуємо клавішу M
        self.accept("m", self.toggle_menu)

    def toggle_menu(self):
        """Відкрити/закрити меню"""
        if self.menu_open:
            # Показати курсор
            props = WindowProperties()
            props.setCursorHidden(True)
            self.win.requestProperties(props)
            self.menu_frame.hide()
            self.taskMgr.add(self.mouse_update, "MouseTask")
        else:
            # Сховати курсор
            props = WindowProperties()
            props.setCursorHidden(False)
            self.win.requestProperties(props)
            self.menu_frame.show()
            self.taskMgr.remove("MouseTask")
            self.menu_open = not self.menu_open

        # ⬇️⬇️⬇️

    def button_clicked(self, button_number):
        """Подія натискання кнопки"""
        print(f"Button {button_number} is clicked!")

    #  Обробка клавіш
    def set_key(self, key, value):
        self.keys[key] = value

    #  Центрування миші
    def center_mouse(self):
        self.win.movePointer(0, int(self.win.getXSize() / 2), int(self.win.getYSize() / 2))

    #  Рух камери мишкою
    def mouse_update(self, task):
        if self.mouseWatcherNode.hasMouse():
            x = self.win.getPointer(0).getX()
            center_x = self.win.getXSize() / 2

            # Поворот за мишкою
            self.camera_angle_h -= (x - center_x) * 0.2

            # Повернути мишку назад до центру
            self.center_mouse()
        return Task.cont

    #  Ігровий цикл
    def update(self, task):
        speed = 0.5

        #  Рух гравця (WASD)
        if self.keys["w"]: self.player.setY(self.player, speed)
        if self.keys["s"]: self.player.setY(self.player, -speed)
        if self.keys["a"]: self.player.setX(self.player, -speed)
        if self.keys["d"]: self.player.setX(self.player, speed)

        #  Оберт гравця спиною до камери
        self.player.setH(self.camera_angle_h )  # задає горизонтальний кут об’єкта (heading)

        #  оберт камери по колу
        px, py, pz = self.player.getPos()
        rad = math.radians(self.camera_angle_h)
        cam_x = px + self.camera_distance * math.sin(rad)
        cam_y = py - self.camera_distance * math.cos(rad)

        self.camera.setPos(cam_x, cam_y, pz + self.camera_height)
        self.camera.lookAt(self.player.getPos() + Point3(0, 0, 10))

        return Task.cont

    def update_timer(self, task):  # ⬅️⬅️⬅️
        elapsed = int(time.time() - self.start_time)
        self.timer_text.setText(f"Time: {elapsed} c")
        return Task.cont






baze = Game()
baze.run()
