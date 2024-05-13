import requests

generation_id = "e52772ac75b..."

response = requests.request(
    "GET",
    f"https://api.stability.ai/v2beta/image-to-video/result/{generation_id}",
    headers={
        'accept': "video/*",  # Use 'application/json' to receive base64 encoded JSON
        'authorization': f"Bearer sk-MYAPIKEY"
    },
)

if response.status_code == 202:
    print("Generation in-progress, try again in 10 seconds.")
elif response.status_code == 200:
    print("Generation complete!")
    with open("video.mp4", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))