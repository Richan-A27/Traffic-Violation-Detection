import cv2
import os

# Folder to verify
image_folder = "data/images/all"       
label_folder = "data/labels/all"       

for img_name in os.listdir(image_folder):
    if not img_name.lower().endswith((".jpg", ".png")):
        continue

    img_path = os.path.join(image_folder, img_name)
    lbl_path = os.path.join(label_folder, os.path.splitext(img_name)[0] + ".txt")

    img = cv2.imread(img_path)
    h, w, _ = img.shape

    if os.path.exists(lbl_path):
        with open(lbl_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split()
                class_id, x_center, y_center, width, height = map(float, parts)
                # Convert YOLO format to pixel coordinates
                x1 = int((x_center - width/2) * w)
                y1 = int((y_center - height/2) * h)
                x2 = int((x_center + width/2) * w)
                y2 = int((y_center + height/2) * h)
                # Draw rectangle
                cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(img, str(int(class_id)), (x1, y1-5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)

                cv2.imshow("Verification", img)
                key = cv2.waitKey(0)
                if key == 27:  # ESC to quit
                    break

cv2.destroyAllWindows()
