# coding=utf-8

import io
import os
import random
import base64
from PIL import Image, ImageDraw, ImageFont


class Captcha(object):

    @classmethod
    def get_captcha(cls):
        width = 90
        height = 32
        img1 = Image.new(mode="RGB", size=(width, height), color=(202, 202, 202))
        draw1 = ImageDraw.Draw(img1, mode="RGB")
        font_path = os.path.dirname(__file__)
        font = ImageFont.truetype(os.path.join(font_path, 'comic.ttf'), 26)

        s = ""
        for x in range(width):
            for y in range(height):
                draw1.point((x, y), fill=(random.randint(200, 255), random.randint(200, 255), random.randint(200, 255)))
        for i in range(4):
            char1 = random.choice([chr(random.randint(65, 90)), str(random.randint(0, 9))])
            color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            draw1.text([i * 20 + 5, 0], char1, font=font, fill=color1)
            s += char1

        output = io.BytesIO()
        img1.save(output, format='JPEG')
        image_base64 = str(base64.b64encode(output.getvalue()), encoding='utf-8')

        return image_base64, s


if __name__ == "__main__":
    img1, s = Captcha.get_captcha()
    print(img1, s)
