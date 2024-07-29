from PIL import Image
import pickle
from sklearn import svm

global svm_model


def load_svm_model():
    global svm_model
    # load the svm model
    with open('models/svm_model.pkl', 'rb') as file:
        svm_model = pickle.load(file)


def convert_to_probability_dictionary(probabilities):
    # convert the probabilities to a dictionary
    probability_dict = {}
    for i in range(len(probabilities)):
        probability_dict[i] = probabilities[i]
    return probability_dict


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
    predicted = svm_model.predict_proba([binary_array])
    return convert_to_probability_dictionary(predicted[0])
