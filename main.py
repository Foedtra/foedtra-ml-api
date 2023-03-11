import base64
from flask import Flask, request, jsonify
from model import Model
from flask_cors import CORS
import urllib.request, io
# try:
#   import googleclouddebugger
#   googleclouddebugger.enable(
#     breakpoint_enable_canary=True
#   )
# except ImportError:
#   pass

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def home():
    return 'hello world'    


@app.route('/test', methods=['GET'])
def testing():
    return 'testing' 

@app.route('/predict', methods=['POST'])
def process_image():
    try:
        # CREDENTIALS = 'secret_key/test-foedtra-83d59c508da8.json'
        # base_image = 'https://firebasestorage.googleapis.com/v0/b/project-missing-app.appspot.com/o/image%2Fasdasda.JPG?alt=media&token=56ad8367-7ace-4954-8ff9-2c695e3eedfb'
        # image_path = '20190420_160631.jpg'
        request_image = request.json
        # image = tf.io.decode_image(base64.b64encode(open(image_path, 'rb').read()), channels=3)
        image = request_image.get('image')
        # image = base64.b64encode(open(image_path, 'rb').read())

        model = Model()
        prediction = model.predict(image)
        # convert server response into JSON format.
        return jsonify({'msg': 'success', 'prediction': prediction})

    except Exception as e:
        return jsonify({'msg': 'error'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
