from PIL import Image

def create_anaglyph(left_image, right_image, depth_label="medium"):
    """
    Creates an anaglyph 3D image from the left and right stereoscopic images.

    Args:
        left_image (PIL.Image): Left stereoscopic image.
        right_image (PIL.Image): Right stereoscopic image.
        depth_label (str): Depth label ('close', 'medium', 'far') for naming purposes.

    Returns:
        PIL.Image: Anaglyph 3D image.
    """
    # Separate channels
    left_r, _, _ = left_image.split()
    _, right_g, right_b = right_image.split()

    # Merge channels to create an anaglyph image
    anaglyph = Image.merge("RGB", (left_r, right_g, right_b))
    return anaglyph

if __name__ == "__main__":
    # Input paths
    output_directory = "../../output"
    depth_levels = ["close", "medium", "far"]

    # Generate anaglyphs for all depths
    for depth in depth_levels:
        left_image_path = f"{output_directory}/left_with_person_{depth}.png"
        right_image_path = f"{output_directory}/right_with_person_{depth}.png"
        anaglyph_output_path = f"{output_directory}/anaglyph_{depth}.png"

        left_image = Image.open(left_image_path)
        right_image = Image.open(right_image_path)

        anaglyph = create_anaglyph(left_image, right_image, depth)
        anaglyph.save(anaglyph_output_path)
        print(f"Anaglyph for depth '{depth}' saved at {anaglyph_output_path}")
