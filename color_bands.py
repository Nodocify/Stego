from PIL import Image, ImageOps
import numpy as np

def gen_bands(path, filename, images=[]):

    im = Image.open(path+filename)
    im = im.convert('RGBA')

    #red
    data = np.array(im)
    red, green, blue, alpha = data.T
    green.fill(0)
    blue.fill(0)
    im2 = Image.fromarray(data)
    fname = 'red_' + filename
    im2.save(path + fname)
    images.append(fname)

    #green
    data = np.array(im)
    red, green, blue, alpha = data.T
    red.fill(0)
    blue.fill(0)
    im2 = Image.fromarray(data)
    fname = 'green_' + filename
    im2.save(path + fname)
    images.append(fname)

    #blue
    data = np.array(im)
    red, green, blue, alpha = data.T
    red.fill(0)
    green.fill(0)
    im2 = Image.fromarray(data)
    fname = 'blue_' + filename
    im2.save(path + fname)
    images.append(fname)

    #alpha
    data = np.array(im)
    red, green, blue, alpha = data.T
    for y in range(len(alpha)):
        for x in range(len(alpha[0])):
            red[y][x] = alpha[y][x]
            green[y][x] = alpha[y][x]
            blue[y][x] = alpha[y][x]
    im2 = Image.fromarray(data)
    fname = 'alpha_' + filename
    im2.save(path + fname)
    images.append(fname)

    #inverted
    im2 = im.convert('RGB')
    im2 = ImageOps.invert(im2)
    fname = 'inverted_' + filename
    im2.save(path + fname)
    images.append(fname)

    #posterized
    im2 = im.convert('RGB')
    im2 = ImageOps.posterize(im2, 1)
    fname = 'posterized_' + filename
    im2.save(path + fname)
    images.append(fname)

    #solarized
    im2 = im.convert('RGB')
    im2 = ImageOps.solarize(im2, threshold=128)
    fname = 'solarized_' + filename
    im2.save(path + fname)
    images.append(fname)

    return images

if __name__ == '__main__':
    path = './static/'
    filename = 'test.png'
    gen_bands(path, filename)
