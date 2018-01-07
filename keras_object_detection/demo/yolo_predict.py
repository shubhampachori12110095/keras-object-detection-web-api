import os

import scipy
from matplotlib.pyplot import imshow

from keras_object_detection.library.yolo import YoloObjectDetector
from keras_object_detection.library.yolo_utils import generate_colors, draw_boxes


def main():
    model_dir_path = '../models'

    image_file = 'images/test.jpg'

    detector = YoloObjectDetector()
    detector.load_model(model_dir_path)

    image, out_scores, out_boxes, out_classes = detector.predict

    # Print predictions info
    print('Found {} boxes for {}'.format(len(out_boxes), image_file))
    # Generate colors for drawing bounding boxes.
    colors = generate_colors(detector.class_names)
    # Draw bounding boxes on the image file
    draw_boxes(image, out_scores, out_boxes, out_classes, detector.class_names, colors)
    # Save the predicted bounding box on the image
    image.save(os.path.join("out", image_file), quality=90)
    # Display the results in the notebook
    output_image = scipy.misc.imread(os.path.join("out", image_file))
    imshow(output_image)


if __name__ == '__main__':
    main()
