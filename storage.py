import pyrebase
import os

config = {
    "apiKey": "yourapikey",
    "authDomain": "yourauthdomain",
    "databaseURL": "yourdatabaseURL",
    "projectId": "yourprojectid",
    "storageBucket": "yourstoragebucket",
    "messagingSenderId": "yourmessagingsenderid",
    "appId": "yourappID"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
my_image = "Capture.jpg"

# Upload Image
storage.child(my_image).put(my_image)

# Download Image
storage.child(my_image).download(filename="myself.jpg", path=os.path.basename(my_image))

# Get url of image
auth = firebase.auth()
email = "youremail@gmail.com"
password = "yourpassword"
user = auth.sign_in_with_email_and_password(email, password)
url = storage.child(my_image).get_url(user['idToken'])
print(url)
