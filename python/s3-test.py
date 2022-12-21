import boto3
import base64
from PIL import Image
import io

print(1)

s3 = boto3.client("s3")

obj = s3.get_object(Bucket="ilovesoup-test-bucket", Key="parking-pics/meme.jpeg")

obj_data = obj['Body'].read()
print(obj_data[0:100])

# Save as image
as_image = Image.open(io.BytesIO(obj_data))
width, height = as_image.size
wanted_size = (int(width * 0.5), int(height * 0.5))


in_mem_file = io.BytesIO()
as_image.save(in_mem_file, format=as_image.format)
in_mem_file.seek(0)

print(dir(in_mem_file))
print(in_mem_file.getvalue()[0:100])
# print(in_mem_file.raw())

encoded = base64.b64encode(in_mem_file.getvalue())
# # print(body)
print(encoded)