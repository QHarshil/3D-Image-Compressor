from PIL import Image
from stereoscopic.adjust_depth import get_offset

def insert_person_at_depth(segmented_image, left_image, right_image, depth):
    """
    Inserts the segmented image into the left and right stereoscopic images for a specified depth.

    Args:
        segmented_image (PIL.Image): Segmented image with transparency.
        left_image (PIL.Image): Left stereoscopic image.
        right_image (PIL.Image): Right stereoscopic image.
        depth (str): Depth level ('close', 'medium', 'far').

    Returns:
        tuple: Modified left and right images with the segmented image inserted.
    """
    offset = get_offset(depth)

    seg_width, seg_height = segmented_image.size
    left_width, left_height = left_image.size
    right_width, right_height = right_image.size

    left_x = max(0, min(left_width - seg_width, left_width // 2 - offset))
    left_y = max(0, min(left_height - seg_height, left_height // 2))
    right_x = max(0, min(right_width - seg_width, right_width // 2 + offset))
    right_y = max(0, min(right_height - seg_height, right_height // 2))

    left_image.paste(segmented_image, (left_x, left_y), segmented_image)
    right_image.paste(segmented_image, (right_x, right_y), segmented_image)
    
    return left_image, right_image

if __name__ == "__main__":
    segmented_image_path = "../../output/person_segmented.png"
    left_image_path = "../../output/stereo1_left.jpg"
    right_image_path = "../../output/stereo1_right.jpg"
    output_directory = "../../output"

    try:
        segmented_image = Image.open(segmented_image_path).convert("RGBA")
        left_image = Image.open(left_image_path).convert("RGB")
        right_image = Image.open(right_image_path).convert("RGB")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        exit(1)

    depth_levels = ["close", "medium", "far"]
    for depth in depth_levels:
        left_with_person, right_with_person = insert_person_at_depth(segmented_image, left_image.copy(), right_image.copy(), depth)
        left_with_person.save(f"{output_directory}/left_with_person_{depth}.png")
        right_with_person.save(f"{output_directory}/right_with_person_{depth}.png")
        print(f"Saved images for depth '{depth}'")
