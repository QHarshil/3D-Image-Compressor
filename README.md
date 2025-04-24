
# 3D Image Composer

An interactive application that segments a person from an image, inserts them into a stereoscopic background, and creates an anaglyph 3D image. The project allows dynamic depth adjustment to position the person closer or farther in the scene.

---

## Features

- **Person Segmentation**: Automatically detects and isolates a person in an image using a pre-trained deep learning model.
- **Stereoscopic Integration**: Inserts the segmented person into left and right stereoscopic images.
- **Anaglyph 3D Images**: Combines left and right images into an anaglyph viewable with red-cyan glasses.
- **Dynamic Depth Adjustment**: Adjust the perceived depth of the inserted person with a slider.
- **Interactive Gradio App**: User-friendly interface for uploading images and generating results.

---

## Installation

### Prerequisites

- Python 3.9 or later
- pip (Python package manager)
- Git

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the following directories exist:
   ```bash
   mkdir assets output
   ```

4. Add input images to the `assets/` directory:
   - A **person image** (e.g., `person.jpg`).
   - A **side-by-side stereoscopic image** (e.g., `stereo.jpg`).

---

## Running the Gradio App

1. Launch the app:
   ```bash
   python src/main.py
   ```

2. Open the provided URL in a browser.

3. Upload your images:
   - **Person Image**: Upload the image to segment.
   - **Stereoscopic Image**: Upload the side-by-side stereoscopic image.

4. Adjust the depth level using the slider to generate a 3D anaglyph.

---

## Running Locally

### Segment a Person

1. Run the segmentation script:
   ```bash
   python src/segmentation/segment_person.py
   ```

2. This generates the segmented image with a transparent background in the `output/` directory:
   - `output/person_segmented.png`

### Insert the Person into a Stereoscopic Image

1. Run the insertion script:
   ```bash
   python src/stereoscopic/insert_person.py
   ```

2. This generates modified left and right stereoscopic images:
   - `output/left_with_person.png`
   - `output/right_with_person.png`

### Generate Anaglyphs

1. Run the anaglyph creation script:
   ```bash
   python src/anaglyph/create_anaglyph.py
   ```

2. This creates anaglyph images for different depths:
   - `output/anaglyph_close.png`
   - `output/anaglyph_medium.png`
   - `output/anaglyph_far.png`

---

## Outputs

### Generated Files

- **Segmented Person**: 
  - `output/person_segmented.png` (Transparent image of the detected person)
- **Stereoscopic Pairs**:
  - `output/left_with_person.png`
  - `output/right_with_person.png`
- **Anaglyph Images**:
  - `output/anaglyph_close.png`
  - `output/anaglyph_medium.png`
  - `output/anaglyph_far.png`

The resulting anaglyph images can be viewed with red-cyan 3D glasses to see the depth effect.

---

## Future Enhancements

- Support for multiple objects with independent depth adjustments.
- Enhanced background blending for better integration.
- Integration with other 3D visualization techniques (e.g., VR).
- Real-time updates with WebSocket support.

---
