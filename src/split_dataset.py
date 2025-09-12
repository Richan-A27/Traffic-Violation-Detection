import os
import shutil
import random

# Folders where your images and labels currently are
images_dir = "data/images/all"
labels_dir = "data/labels/all"

# Folders to store final train/val splits
train_img_dir = "data/images/train"
val_img_dir   = "data/images/val"
train_lbl_dir = "data/labels/train"
val_lbl_dir   = "data/labels/val"

# Create folders if they don't exist
for folder in [train_img_dir, val_img_dir, train_lbl_dir, val_lbl_dir]:
    os.makedirs(folder, exist_ok=True)

# List all image files
all_images = [f for f in os.listdir(images_dir) if f.endswith((".jpg",".png"))]
random.shuffle(all_images)  # shuffle to randomize

# Split ratio (80% train, 20% val)
split_ratio = 0.8
split_index = int(len(all_images) * split_ratio)
train_images = all_images[:split_index]
val_images = all_images[split_index:]

# Move images and labels to respective folders
for img_list, img_dest, lbl_dest in [
    (train_images, train_img_dir, train_lbl_dir),
    (val_images, val_img_dir, val_lbl_dir)
]:
    for img_file in img_list:
        # Image
        shutil.copy2(os.path.join(images_dir, img_file), os.path.join(img_dest, img_file))
        # Label
        lbl_file = os.path.splitext(img_file)[0] + ".txt"
        shutil.copy2(os.path.join(labels_dir, lbl_file), os.path.join(lbl_dest, lbl_file))

print("Dataset split completed!")
print(f"Training images: {len(train_images)}, Validation images: {len(val_images)}")
