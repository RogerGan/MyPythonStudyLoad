# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-06-17 20:15'

__mail__ = 'gancj@ucweb.com/393037282@qq.com'

def pil_image_similarity(filepath1, filepath2):
    from PIL import Image
    import math
    import operator
    image1 = Image.open(filepath1)
    image2 = Image.open(filepath2)
    h1 = image1.histogram()
    h2 = image2.histogram()
    rms = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return rms
