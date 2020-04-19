import os
from matplotlib import pyplot as plt
import cv2

def templateMathching( template_path, image_path):
    methods = [
        'cv2.TM_CCOEFF',
        # "cv2.TM_CCOEFF_NORMED",
        # "cv2.TM_CCORR",
        # "cv2.TM_CCORR_NORMED"
    ]
    image = cv2.imread(image_path, 0)
    template = cv2.imread(template_path, 0)
    width, height = template.shape[::-1]

    for meth in methods:
        img = image.copy()
        method = eval(meth)

        res = cv2.matchTemplate(img, template, method)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)

        topLeft = maxLoc
        botRight = (topLeft[0] + width, topLeft[1] + height)

        cv2.rectangle(img, topLeft, botRight, 0, 5)

        plt.suptitle(meth)
        plt.subplot(121)
        plt.imshow(res, cmap='gray')
        plt.title('Matching Result')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122)
        plt.imshow(img, cmap='gray')
        plt.title('Detected Point')
        plt.xticks([])
        plt.yticks([])

        plt.show()

def run(
    file_directory,
    template_directory,
    pictureFormat,
    imagesCount
):
    images = [os.path.join(file_directory, f'{i}.{pictureFormat}') for i in range(1, imagesCount + 1)]
    print(images)
    templates = [os.path.join(template_directory, f'{i}.{pictureFormat}') for i in range(1, 2)]
    print(templates)
    for template in templates:
        for image in images:
            print(f'finding {template} in {image}')
            templateMathching(template, image)

if __name__ == '__main__':
    run('PATH/TO/IMAGES', 'PATH/TO/TEMPLATES', 'FORMAT', 1)

