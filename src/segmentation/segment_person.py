import torch
import cv2
import numpy as np
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo
from PIL import Image

def setup_detectron2(threshold=0.5):
    """
    Sets up the Detectron2 model configuration and predictor.

    Args:
        threshold (float): Confidence threshold for object detection.

    Returns:
        tuple: (cfg, predictor) where cfg is the configuration and predictor is the model predictor.
    """
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = threshold 
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
    cfg.MODEL.DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    predictor = DefaultPredictor(cfg)
    return cfg, predictor

def segment_person(image_path, output_path=None):
    """
    Segments a person from an image and optionally saves the result.

    Args:
        image_path (str): Path to the input image.
        output_path (str, optional): Path to save the segmented image. If None, returns a PIL.Image object.

    Returns:
        PIL.Image or None: Segmented image as a PIL.Image object if output_path is None. Otherwise, saves the image.
    """
    # Detectron2
    _, predictor = setup_detectron2()

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image from path {image_path}")
        return None

    outputs = predictor(image)

    # COCO class ID for person is 0
    masks = outputs["instances"].pred_masks
    classes = outputs["instances"].pred_classes
    person_mask = None
    for i, cls in enumerate(classes):
        if cls == 0:  # Class ID for "person"
            person_mask = masks[i].cpu().numpy()
            break

    if person_mask is None:
        print("No person detected in the image.")
        return None

    segmented_image = cv2.bitwise_and(image, image, mask=person_mask.astype(np.uint8))
    
    # Convert to RGBA and set transparent background for non-person areas
    segmented_image = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2BGRA)
    segmented_image[person_mask == 0] = [0, 0, 0, 0]  # Set background to transparent

    segmented_image_pil = Image.fromarray(cv2.cvtColor(segmented_image, cv2.COLOR_BGRA2RGBA))

    if output_path:
        segmented_image_pil.save(output_path)
        print(f"Segmented image saved as {output_path}")
        return None
    else:
        return segmented_image_pil

if __name__ == "__main__":
    input_image_path = "../../assets/person.jpg"
    output_image_path = "../../output/person_segmented.png"
    
    # Run segmentation
    segmented_image = segment_person(input_image_path, output_path=output_image_path)
    if segmented_image:
        segmented_image.show()
