from BaseFile import BaseFile
from PIL import Image


class ImageFile(BaseFile):
    def info(self):
        base_info = super().info()
        width, height = self.get_dimensions()
        base_info.update({
            'dimensions': f'{width}x{height}'
        })

        return base_info


    def get_dimensions(self):
        with Image.open(self.path) as img:
            return img.width, img.height