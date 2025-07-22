import easyocr

reader = easyocr.Reader(['en'])
def extract_text(image_path):
    # result = reader.readtext(image_path, detail=0, paragraph=True)
    result = reader.readtext(image_path)

    for bbox,text, prob in result:
        print(f"Detected text: {text} with probability{prob:.2f}")
    return result[0] if result else ""

image_path = r"app\static\test_images\WhatsApp Image 2025-07-15 at 10.27.45 AM (2).jpeg"
result = extract_text(image_path)