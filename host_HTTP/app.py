from flask import Flask, request, send_file
import tensorflow as tf
import pandas as pd
import os

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def recognize_image():
    # check file
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    # recognize_image
    filepath = os.path.join('/tmp', file.filename)
    file.save(filepath)

    #function 

    # assume result is dictionary
    result = {"object": "cat", "confidence": 0.98}

    # Save in Excel
    df = pd.DataFrame([result])
    excel_path = filepath + ".xlsx"
    df.to_excel(excel_path, index=False)

    # return
    return send_file(excel_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
