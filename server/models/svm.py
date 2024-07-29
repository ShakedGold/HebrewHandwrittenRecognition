from PIL import Image
import pickle

global svm_model


def load_svm_model():
    global svm_model
    with open('models/svm_model.sav', 'rb') as file:
        svm_model = pickle.load(file)


def convert_img_to_binary_array(pixels):
    # get the pixel values of the image
    binary_array = []
    for pixel in pixels:
        if pixel[0] >= 128 and pixel[1] >= 128 and pixel[2] >= 128:
            binary_array.append(1)
        else:
            binary_array.append(0)
    return binary_array


def predict_image(binary_array):
    return svm_model.predict([binary_array])[0]
