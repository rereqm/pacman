from logic.field import Field
from objects.cells import Cell
from settings import Settings
from objects.sprites.seeds import Energizer, Seed
from objects.images import Image
class FieldDrawer():
    def __init__(self,pix_size):
         self.pix_size = pix_size
         self.field = Field().get()
         x = 50
         y = 50
         self.obj = []
         self.obj.append(Image(50,50,'textures/Map.png'))
         for i in self.field:
             for j in i:
                 if j == 0:
                     self.obj.append(Seed(x,y))
                 if j == 4:
                     self.obj.append(Energizer(x,y))
                 x += self.pix_size
             y += self.pix_size
             x = 50
    def get_all_obj(self):
        return self.obj
