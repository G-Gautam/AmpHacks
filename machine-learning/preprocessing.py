from PIL import Image
import numpy as np
import glob
import cv2

path = "C:\\Users\\AndyWork\\PycharmProjects\\AmpHacks\\AmpHacks\\machine-learning\\data\\"


def load_image(infilename) :
    img = Image.open(infilename)
    img.load()
    data = np.asarray(img, dtype="int32")
    return data


files = [f for f in glob.glob(path + "**/*.jpg", recursive=True)]


def load_data(path):
    result = np.empty((0, 200, 200, 3), dtype="int32")
    for f in files:

        img = cv2.imread(f)
        res = cv2.resize(img, dsize=(200, 200), interpolation=cv2.INTER_CUBIC)
        res = np.expand_dims(res, axis=0)

        result = np.append(result, res, axis=0)

    return result

data = load_data(path)

print(data.shape)












