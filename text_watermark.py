from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
 
def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):
    photo = Image.open(input_image_path)

    # make the image editable
    drawing = ImageDraw.Draw(photo)
 
    red = (255, 0, 0)
    font = ImageFont.truetype("font/consolas.ttf", 40)
    drawing.text(pos, text, fill=red, font=font)
    photo.show()
    photo.save(output_image_path)
 
 
if __name__ == '__main__':
    img = 'img/main.jpg'
    
    base = Image.open('img/main.jpg')
    width, height = base.size
    
    watermark_text(img, 'img/main_watermarked.jpg',
                   text='Abitant',
                   pos=(height/2, width/2))