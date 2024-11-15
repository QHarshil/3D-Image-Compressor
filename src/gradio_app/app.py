import gradio as gr
from PIL import Image
from segmentation.segment_person import segment_person
from stereoscopic.insert_person import insert_person_at_depth
from anaglyph.create_anaglyph import create_anaglyph

def process_image(person_image_path, stereo_image, depth):
    """
    Processes a single person image and a single stereoscopic image to generate an anaglyph.
    
    Args:
        person_image_path (str): Path to the person image.
        stereo_image (PIL.Image): Stereoscopic side-by-side image.
        depth (int): Depth offset level.

    Returns:
        PIL.Image: Generated anaglyph image.
    """
    # Segment the person
    segmented_image = segment_person(person_image_path)

    # Split the stereoscopic image into left and right images
    left_image = stereo_image.crop((0, 0, stereo_image.width // 2, stereo_image.height))
    right_image = stereo_image.crop((stereo_image.width // 2, 0, stereo_image.width, stereo_image.height))

    # Insert the segmented person into the left and right images
    left_image, right_image = insert_person_at_depth(segmented_image, left_image, right_image, depth)

    # Create the anaglyph image
    anaglyph = create_anaglyph(left_image, right_image)
    return anaglyph

def launch_app():
    """
    Launches the Gradio interface for the 3D Image Composer.
    """
    interface = gr.Interface(
        fn=process_image,
        inputs=[
            gr.File(label="Upload Person Image", type="filepath"),
            gr.Image(type="pil", label="Upload Stereoscopic Image (side-by-side format)"),
            gr.Slider(5, 30, value=15, step=1, label="Depth Offset Level"),
        ],
        outputs=gr.Image(label="Anaglyph 3D Image"),
        title="3D Image Composer",
        description="Upload a person image and a side-by-side stereoscopic background image to create a 3D anaglyph with depth adjustment.",
    )
    interface.launch()

# Run the app
if __name__ == "__main__":
    launch_app(share=True)
