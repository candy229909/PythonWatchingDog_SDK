import os
from PIL import Image
import pandas as pd

# Function
def process_image(image_path):
    # AI�B�zfumciton
    return {"object": "example", "confidence": 0.99}

# client�ݼƾ�
customer_data_path = os.getenv('CUSTOMER_DATA_PATH')
images = [os.path.join(customer_data_path, f) for f in os.listdir(customer_data_path) if f.endswith('.jpg')]

# result
results = []
for image_path in images:
    result = process_image(image_path)
    results.append(result)

# Excel�Ы�
df = pd.DataFrame(results)
df.to_excel(os.path.join(customer_data_path, 'results.xlsx'), index=False)