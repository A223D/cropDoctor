## Inspiration
Hailing from a country with strong agricultural focus, I realize that there is a lot of untapped potential in agriTech. Emerging technologies like highly accessible machine learning deployments are going to make maximizing crop yield much easier and cost-viable for the public. This is a project that explores such an implementation by diagnosing common plant diseases with a mobile phone, that is, technology that people already have.

## What it does
This project uses a convolutional neural model trained on this [Plant Diseases Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseadses-dataset) using Google's colaboratory service to detect 26 diseases in crops. This is then hosted on a Flask server, with a phone/tablet webpage that accepts an image, either from the phone's filesystem or camera directly. This is then processed through the model, to receive a diagnosis. If there is an issue in the plant in the image, the user is forwarded to a link which provides solutions to remedy the affected crop.

The links are thoroughly researched, and are guaranteed to have information that can help every-day farmers to get the most out of their crop.

There are 38 classifications that the model makes: `Apple___Cedar_apple_rust, Apple___healthy, Blueberry___healthy, Cherry_(including_sour)___Powdery_mildew, Cherry_(including_sour)___healthy, Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot, Corn_(maize)___Common_rust_, Corn_(maize)___Northern_Leaf_Blight, Corn_(maize)___healthy, Grape___Black_rot, Grape___Esca_(Black_Measles), Grape___Leaf_blight_(Isariopsis_Leaf_Spot), Grape___healthy, Orange___Haunglongbing_(Citrus_greening), Peach___Bacterial_spot, Peach___healthy, Pepper,_bell___Bacterial_spot, Pepper,_bell___healthy, Potato___Early_blight, Potato___Late_blight, Potato___healthy, Raspberry___healthy, Soybean___healthy, Squash___Powdery_mildew, Strawberry___Leaf_scorch, Strawberry___healthy, Tomato___Bacterial_spot, Tomato___Early_blight, Tomato___Late_blight, Tomato___Leaf_Mold, Tomato___Septoria_leaf_spot, Tomato___Spider_mites Two-spotted_spider_mite, Tomato___Target_Spot, Tomato___Tomato_Yellow_Leaf_Curl_Virus, Tomato___Tomato_mosaic_virus, Tomato___healthy`

There are 26 disease classifications out of the 38 listed above.

## How we built it
The dataset was acquired from Kaggle, and trained using Google's Colaboratory service. Here are the model details:

![convolutional details](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/290/557/datas/gallery.jpg)

I was able to reach about 93% accuracy on our validation set:

![93 percent accuracy](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/290/556/datas/gallery.jpg)

After model training, I set up a server using Flask. The mobile-based home page accepts an image from the camera or filesystem. If the crop in question has an issue, the user is directed to a link which contains information to remedy the situation. Here is the home page, the selection interface, and the notification that appears if a crop is disease-free. 
![](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/002/290/583/datas/gallery.jpg)

## Challenges we ran into
* I have extremely limited experience with web development. This project was a major challenge for me to complete on my own. 
* I originally planned to host this on a Google Cloud server, however installing TensorFlow was a major challenge due to memory constraints. 
* The original intention was to build the system using AppWrite, however it took too much time to understanding building Appwrite custom functions, especially one that would use TensorFlow to create a prediction using an image.
* It's flu season in Canada, and I have been affected as well. Due to this, I had to cut my project idea down by 25% than what I had planned originally. However, this taught me about hacks and shortcuts I had not known about previously.

## Accomplishments that we're proud of
* Making technological advancement through machine learning using hardware that people already have. 
* Building a purely software project all by myself, since my main focus is on hardware.

## What we learned
* How to deploy a machine learning model to a web server. 
* Hosting a Flask server in development vs production
* How convolutional neural networks on a deeper level. 

## What's next for PlantDoctor
* Adding more plants and and plant diseases
* Having the model take into account regional diseases, to increase accuracy.
