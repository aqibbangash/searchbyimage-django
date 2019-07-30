# from clarifai.rest import ClarifaiApp
# from clarifai.rest import Image as ClImage
import os
import time
from django.conf import settings
from LiquorCabinet.settings import BASE_DIR
import jsonpickle
import os
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from keras import backend as K
import numpy as np
import cv2
import datetime
import pickle
# ingredientTypes = {
#     'Henny': 'Cogniac',
#     'Goose': 'Vodka',
#     'Lime': 'Garnish',
#     'Ciroc': 'Vodka',
#     'Jameson': 'Whiskey',
#     'DryVermouth': 'Dry Vermouth',
#     'AngosturaBitters': 'Angostura Bitters'
# }


class predict:

    def run(image):
        # app = ClarifaiApp("KiPgquABTE-kvueyDk2GoUrAlbJWGwCXlfrQ45pN", "hkAMvUIGzHH8hZNpPy1fyeC4sca2iS9SgTAUnwLe")

        # get the general model

        # model = app.models.get("alcohol")
        # image = ClImage(file_obj=image)
        # pred = model.predict([image])
        # print('1st \n ', pred)
        # pred = pred['outputs'][0]['data']['concepts'][0]
        # pred['description'] = ingredientTypes[pred['name']]
        # print('2nd \n ', pred)
        # return pred

        image = cv2.imdecode(np.fromstring(image.file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        # header, image_data = request_data.split(';base64,')
        # nparr = np.fromstring(request_data, np.uint8)
        # for image in os.listdir('D:/Sofit_Deliverables/image-search-python/media/images/'):
        try:
            # image = 'D:/Sofit_Deliverables/image-search-python/media/images/Inkedimages_LI.jpg'
            # image = cv2.imread(image)
            # image = Image.open(io.BytesIO(base64.b64decode(image_data)))
            # default_image_size = tuple((128, 128))

            if image is not None:
                image = cv2.resize(image, (128, 128))
                image = image.astype("float") / 255.0  # handling scaling our image to the range [0, 1]
                image = img_to_array(image)  # converting it to an array, and addding an extra dimension
                image = np.expand_dims(image, axis=0)
            else:
                print(None, "Error loading image file")

            print("[INFO] loading network...")
            print(BASE_DIR + "/cocktails/laptop_model.h5")
            # print(os.path.join(BASE_DIR, '/hello/laptop_model.h5'))
            model = load_model(BASE_DIR + "/cocktails/laptop_model.h5")

            # orig = image.copy()

            # pre-process the image for classification
            # image = cv2.resize(image, (128, 128))
            # image = image.astype("float") / 255.0  # handling scaling our image to the range [0, 1]
            # image = img_to_array(image)  # converting it to an array, and addding an extra dimension
            # image = np.expand_dims(image, axis=0)  # np.expand_dims  allows our image to have the shape (1, width, height, 3)
            # load the trained convolutional neural network

            label_List = list()
            prob_List = []
            # classify the input image
            # (Mac, Other_Laptop, no_Laptop) = model.predict(image)[0]
            counter = 0
            label_List = model.predict(image)[0]
            label_name = ['Mac', 'Laptop', 'no_Laptop']
            final_list = {}

            response_message = ''

            for prob in label_List:
                prob = round(prob * 100, 2)
                final_list[label_name[counter]] = prob
                if(prob >= 70):

                    highest_prob = label_name[counter]
                    #  print("Image contains: " + label_name[counter] + " with highest probability \n")
                    response_message += "Image contains: " + label_name[counter] + " with highest probability "
                counter = counter + 1

            #  print('Other Details: \n')
            print("Here is final_list: \n", final_list)
            response_message += ' Details: '

            for key, val in final_list.items():
                #  print(key + ': ', val, '\n')
                response_message += ' ' + str(key) + ': ' + str(val) + ' '

            response = {}
            response['message'] = response_message
            print("Response Message is:........  ", response)

        except Exception as e:

            response = {"error": "3", "message": f"Error : {str(e)}"}

        response = [highest_prob, final_list]
        return response
