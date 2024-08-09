from fastapi import FastAPI, File, UploadFile
from PIL import Image
import numpy as np
import io

app = FastAPI()

@app.post("/process-image/")
async def process_image(file: UploadFile = File(...)):
    print("Processing request...")
    # Read the image file
    image = Image.open(io.BytesIO(await file.read()))

    # Convert to grayscale and numpy array
    img_array = np.array(image.convert("L"))

    # Example: Calculate histogram
    histogram = np.histogram(img_array, bins=256)[0]

    return {"histogram": histogram.tolist()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)