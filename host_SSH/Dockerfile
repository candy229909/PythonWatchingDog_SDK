
FROM tensorflow/tensorflow:latest-gpu

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./image_recognition.py"]
