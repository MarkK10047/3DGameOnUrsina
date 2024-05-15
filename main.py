from ursina import *
from direct.actor.Actor import Actor
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
EditorCamera()

class Player(FirstPersonController):
    def __init__(self, add_to_scene_entities=True, enabled=True, **kwargs):
        super().__init__(add_to_scene_entities=add_to_scene_entities, enabled=enabled, **kwargs)
        
        # Load the model with proper scaling
        self.actor = Actor('./models/mainChar.glb', {'walking': './animations/main_walk.glb', 'standing': './animations/standing.glb'})
        self.actor.setScale(1)  # Scale the actor properly
        self.actor.reparentTo(self)

        self.texture = loader.loadTexture('./textures/Ch09_1001_Diffuse.png') # type: ignore
        self.actor.setTexture(self.texture, 1)
        self.actor.setHpr(180, 0, 0)
        self.double_sided = True
        self.camera_pivot.z = 17 # move the camera behind the player model
        self.camera_pivot.y = 2

        if self.actor.getCurrentAnim() != 'standing':
            self.actor.loop('standing')


    def update(self):
        
        speed = 2
        if held_keys['w']:
            self.position += self.forward * time.dt * speed
            if not self.actor.getCurrentAnim() == 'walking':
                self.actor.loop('walking')
        else:
            if self.actor.getCurrentAnim() == 'walking':
                self.actor.loop('standing')
        if held_keys['s']:
            self.position -= self.forward * time.dt * speed
        if held_keys['a']:
            self.position -= self.right * time.dt * speed
        if held_keys['d']:
            self.position += self.right * time.dt * speed
        
        
bridge = Entity(
    model='./models/bridge.glb',
    texture = './textures/Untitled_6_DefaultMaterial_BaseColor.png',
    scale = 1
)

environment = Entity(
    model = './models/music_video_pt._3.glb',
    x = 175,
    z = 90,
    scale = 2
)

player = Player()   

scene.fog_color = color.black
scene.fog_density = 0.2 
app.run()
