from PIL import Image
import os

input_dir = "../../assets/"
output_dir = "../../output/"

stereo_images = ["stereo1.jpg", "stereo2.jpg", "stereo3.jpg"]

def split_stereo_images():
    for stereo_image in stereo_images:
        image_path = os.path.join(input_dir, stereo_image)
        image = Image.open(image_path)

        width, height = image.size
        half_width = width // 2

        # Split the stereo image into left and right images
        left_image = image.crop((0, 0, half_width, height))
        right_image = image.crop((half_width, 0, width, height))

        base_name = os.path.splitext(stereo_image)[0]
        left_image.save(os.path.join(output_dir, f"{base_name}_left.jpg"))
        right_image.save(os.path.join(output_dir, f"{base_name}_right.jpg"))

        print(f"Processed {stereo_image}: Saved left and right images.")


if __name__ == "__main__":
    split_stereo_images()
