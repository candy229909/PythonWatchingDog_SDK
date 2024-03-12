import tensorflow as tf
import cv2
import pandas as pd

# �Ϲ��B�z
def recognize_image(image_path, model_path='your_model.h5'):
    # �V�m�n��TensorFlow�ҫ�
    model = tf.keras.models.load_model(model_path)

    #�Ϥ��B�z�i�H�g�o��
    predictions = model.predict(img)

    return predictions

def save_results_to_excel(results, excel_path='results.xlsx'):
    # �N���G��^Excel
    df = pd.DataFrame(results)
    df.to_excel(excel_path, index=False)

if __name__ == '__main__':
    image_path = 'path/to/your/image.jpg'
    results = recognize_image(image_path)
    save_results_to_excel(results)