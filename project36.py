"""DAY 36 OF 100 DAYS OF 
PYTHON PROJECT"""
from PIL import Image
import os

path = "photo.PNG"

if not os.path.exists(path):
    print(f"Error: '{path}' not found.")
    exit(1)

img = Image.open(path)
print("Loaded:", path)

while True:
    print("\n1. Show Image")
    print("2. Image Info")
    print("3. Crop Image")
    print("4. Save Image")
    print("5. Exit")
    choice = input("Choose option (1-5): ").strip()

    if choice == "1":
        img.show()

    elif choice == "2":
        print("Format:", img.format)
        print("Mode:", img.mode)
        print("Size:", img.size)

    elif choice == "3":
        try:
            left = int(input("Left: "))
            top = int(input("Top: "))
            right = int(input("Right: "))
            bottom = int(input("Bottom: "))
        except ValueError:
            print("Please enter valid integers.")
            continue

        w, h = img.size
        if not (0 <= left < right <= w and 0 <= top < bottom <= h):
            print(f"Invalid crop box for image size {w}x{h}.")
            continue

        img = img.crop((left, top, right, bottom))
        print("Cropped to", img.size)

    elif choice == "4":
        save_path = input("Save as (e.g. output.jpg): ").strip()
        save_dir = os.path.dirname(save_path)
        if save_dir and not os.path.exists(save_dir):
            print(f"Directory '{save_dir}' does not exist.")
            continue

        lower_path = save_path.lower()
        is_jpg = lower_path.endswith(".jpg") or lower_path.endswith(".jpeg")
        img_to_save = img
        if img.mode in ("RGBA", "P") and is_jpg:
            img_to_save = img.convert("RGB")

        try:
            img_to_save.save(save_path)
            print("Saved to", save_path)
        except Exception as e:
            print(f"Failed to save: {e}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
