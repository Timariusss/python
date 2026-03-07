import cv2 
from PIL import Image

image_path = "0rgams.jpg"
cat_face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface_extended.xml")
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
cat = Image.open(image_path)
glasses = Image.open("glasses.png")
cat = cat.convert("RGBA")
for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h / 3)))
    cat.paste(glasses,(x, int(y+h/4))), glasses 
    cat.save("cat.with.glasses.1.png")
    cat_with_glasses = cv2.imread("сat.with.glasses.1.png")
    cv2.imshow("cat.with.glasses.1.png", cat_with_glasses )
    cv2.waitKey