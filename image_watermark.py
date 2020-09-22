from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
 
def watermark_image(input_image_path,
                   output_image_path,
                   watermark_image_path,
                   position):

    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)    

    base_image.paste(watermark, position)
    base_image.show()
    base_image.save(output_image_path)
 
if __name__ == '__main__':
    img = 'img/main.jpg'

    
    watermark_image(img, 'img/main_watermarked.jpg',
                   'img/watermark.png',
                   position=(325, 400))