# TensorFlow�x��GPU image
FROM tensorflow/tensorflow:latest-gpu

RUN pip install pandas openpyxl Pillow

WORKDIR /app

COPY . /app

EXPOSE 5000

# Mount�����|
ENV CUSTOMER_DATA_PATH="/mnt/customer_data"

CMD ["python", "app.py"]