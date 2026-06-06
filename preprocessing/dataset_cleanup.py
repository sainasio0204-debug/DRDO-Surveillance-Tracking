import os


image_folder = 'path/to/images'
label_folder = 'path/to/labels'


image_extensions = {'.jpg', '.jpeg', '.png', '.bmp'}

# Get sets of base filenames (without extension)
image_files = {
    os.path.splitext(f)[0] for f in os.listdir(image_folder)
    if os.path.splitext(f)[1].lower() in image_extensions
}
label_files = {
    os.path.splitext(f)[0] for f in os.listdir(label_folder)
    if f.endswith('.txt')
}


images_without_labels = image_files - label_files
labels_without_images = label_files - image_files


for base in images_without_labels:
    for ext in image_extensions:
        img_path = os.path.join(image_folder, base + ext)
        if os.path.exists(img_path):
            print(f"Deleting image: {img_path}")
            os.remove(img_path)
            break


for base in labels_without_images:
    label_path = os.path.join(label_folder, base + '.txt')
    if os.path.exists(label_path):
        print(f"Deleting label: {label_path}")
        os.remove(label_path)

print("Cleanup complete.")