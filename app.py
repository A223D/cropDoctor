from flask import Flask, render_template, request, redirect
import tensorflow as tf
# from werkzeug import secure_filename
from PIL import Image
import numpy as np

labels = {0: 'Apple___Apple_scab',
          1: 'Apple___Black_rot',
          2: 'Apple___Cedar_apple_rust',
          3: 'Apple___healthy',
          4: 'Blueberry___healthy',
          5: 'Cherry_(including_sour)___Powdery_mildew',
          6: 'Cherry_(including_sour)___healthy',
          7: 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
          8: 'Corn_(maize)___Common_rust_',
          9: 'Corn_(maize)___Northern_Leaf_Blight',
          10: 'Corn_(maize)___healthy',
          11: 'Grape___Black_rot',
          12: 'Grape___Esca_(Black_Measles)',
          13: 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
          14: 'Grape___healthy',
          15: 'Orange___Haunglongbing_(Citrus_greening)',
          16: 'Peach___Bacterial_spot',
          17: 'Peach___healthy',
          18: 'Pepper,_bell___Bacterial_spot',
          19: 'Pepper,_bell___healthy',
          20: 'Potato___Early_blight',
          21: 'Potato___Late_blight',
          22: 'Potato___healthy',
          23: 'Raspberry___healthy',
          24: 'Soybean___healthy',
          25: 'Squash___Powdery_mildew',
          26: 'Strawberry___Leaf_scorch',
          27: 'Strawberry___healthy',
          28: 'Tomato___Bacterial_spot',
          29: 'Tomato___Early_blight',
          30: 'Tomato___Late_blight',
          31: 'Tomato___Leaf_Mold',
          32: 'Tomato___Septoria_leaf_spot',
          33: 'Tomato___Spider_mites Two-spotted_spider_mite',
          34: 'Tomato___Target_Spot',
          35: 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
          36: 'Tomato___Tomato_mosaic_virus',
          37: 'Tomato___healthy'}


sites = {0: 'https://www.planetnatural.com/pest-problem-solver/plant-disease/apple-scab/',
          1: 'https://extension.umn.edu/plant-diseases/black-rot-apple',
          2: 'https://extension.umn.edu/plant-diseases/cedar-apple-rust',
          3: '/perfect',
          4: '/perfect',
          5: 'https://extension.umn.edu/plant-diseases/powdery-mildew-trees-and-shrubs',
          6: '/perfect',
          7: 'https://extension.umn.edu/corn-pest-management/northern-corn-leaf-blight',
          8: 'https://extension.umn.edu/corn-pest-management/common-rust-corn',
          9:'https://extension.umn.edu/pest-management/cercospora-leaf-blight-and-purple-seed-stain-soybean',
          10: '/perfect',
          11: 'https://www.gardeningknowhow.com/edible/fruits/grapes/black-rot-grape-treatment.htm',
          12: 'https://www2.ipm.ucanr.edu/agriculture/grape/Esca-Black-Measles/',
          13: 'https://ask2.extension.org/kb/faq.php?id=772745',
          14: '/perfect',
          15: 'https://ask2.extension.org/kb/faq.php?id=772745',
          16: 'https://www.canr.msu.edu/news/management_of_bacterial_spot_on_peaches_and_nectarines',
          17: '/perfect',
          18: 'https://extension.umn.edu/disease-management/bacterial-spot-tomato-and-pepper',
          19: '/perfect',
          20: 'https://www2.ipm.ucanr.edu/agriculture/potato/Early-Blight/',
          21: 'https://www.gardeningknowhow.com/edible/fruits/strawberry/strawberries-with-leaf-scorch.htm',
          22: '/perfect',
          23: '/perfect',
          24: '/perfect',
          25: 'https://www.gardeningknowhow.com/edible/vegetables/squash/powdery-mildew-in-squash.htm',
          26: 'https://extension.umn.edu/disease-management/late-blight',
          27: '/perfect',
          28: 'https://extension.umn.edu/disease-management/bacterial-spot-tomato-and-pepper',
          29: 'https://extension.umn.edu/disease-management/early-blight-tomato-and-potato',
          30: 'https://gardenerspath.com/how-to/disease-and-pests/late-blight-tomato/',
          31: 'https://www.canr.msu.edu/news/tomato-leaf-mold-in-hoophouse-tomatoes',
          32: 'https://www.epicgardening.com/septoria-leaf-spot/',
          33: 'https://audreyslittlefarm.com/spider-mites-on-tomato-plants/',
          34: 'https://www.gardeningknowhow.com/edible/vegetables/tomato/target-spot-on-tomatoes.htm',
          35: 'https://www2.ipm.ucanr.edu/agriculture/tomato/Tomato-Yellow-Leaf-Curl/',
          36: 'https://extension.umn.edu/disease-management/tomato-viruses',
          37: '/perfect'}

# notice that the app instance is called `app`, this is very important.
app = Flask(__name__)

model = tf.keras.models.load_model("./plantmodel.h5")


def predictDisease2(imPath):
    img = Image.open(imPath).resize((256, 256))
    imgArr = np.asarray(img)
    ready = np.expand_dims(imgArr, axis=0)

    classes = model.predict(ready, verbose=0).tolist()
    maxVal = max(classes[0])
    something = classes[0].index(maxVal)

    return something


@app.route("/")
def hello_world():
    # print(os.listdir("./"))
    return render_template('./upload.html')


@app.route("/uploader", methods=["POST", "GET"])
def upload_file():
    if request.method == "POST":
        f = request.files['file']
        f.save("./picture.jpg")
        # print(os.listdir("./"))
        print("Let's dothis")
        something = predictDisease2("./picture.jpg")

        # return "Uploaded successfully"
        return redirect(sites[something], code=302)

@app.route("/perfect", methods=["GET", "POST"])
def perfectFunction():
    return render_template("./perfect.html")


if __name__ == '__main__':
    app.run(debug=True)
