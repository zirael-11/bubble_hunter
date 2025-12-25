import tkinter
import os 
from PIL import ImageTk, Image
from PIL.Image import Transpose


class Submarine:
    canvas:tkinter.Canvas
    image:int
    __image_path: str = os.path.join(os.getcwd(), 'submarine.png') #джоин позволяет соединить два пути в винде используется /

    def __init__(self,canvas):

        self.canvas = canvas
        #При помощи PIL считываем инфу о картинке из файла:
        image_file = Image.open(self.__image_path)

        #Меняем размер картинки на 100х100:
        image_file = image_file.resize((100,100), resample=Image.Resampling.LANCZOS)
    

        #Конвертируем картиночку в объект photo image для tkinter:
        self._image_src_right = ImageTk.PhotoImage(image_file)
        self.__image_src_left = ImageTk.PhotoImage(image_file.transpose(Transpose.FLIP_LEFT_RIGHT))

        #Формируем изображение на холсте с помощью объекта image:
        self.image = self.canvas.create_image(
            200,
            200,
            image=self._image_src_right
        )
 

    def __del__(self):
        self.canvas.delete(self.image)
    
    def move(self, event):
        if event.keysym == "Up":
            self.canvas.move(self.image, 0, -5)
        if event.keysym == "Down":
            self.canvas.move(self.image, 0, 5)
        if event.keysym == "Left":
            self.canvas.move(self.image, -5, 0)
            self.canvas.itemconfig(self.image,image = self.__image_src_left)
        if event.keysym == "Right":
            self.canvas.move(self.image, 5, 0)
            self.canvas.itemconfig(self.image,image = self.__image_src_right)
