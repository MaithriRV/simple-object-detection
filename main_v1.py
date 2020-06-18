import matplotlib.pyplot as plt
import glob
import cv2
import vehicledetect.helpers as helpers
import vehicledetect.detector as detector
frame_count = 0 # frame counter
debug = True
def pipeline(img):
    global frame_count
    global min_hits

    global debug

    frame_count += 1
    z_box = det.get_localization(img)  # measurement
    if debug:
        print('Frame:', frame_count)
    if debug:
        for i in range(len(z_box)):
            img1 = helpers.draw_box_label(img, z_box[i], box_color=(255, 0, 0)
            plt.imshow(img1)
            plt.show()
            return img1
if __name__ == "__main__":

    det = detector.CarDetector()

    if debug:  # test on a sequence of images
        images = [plt.imread(file) for file in glob.glob('./samplesholder/*.jpg')]

        for i in range(len(images))[0:7]:
            image = images[i]
            image_box = pipeline(image)
            cv2.imwrite("path_output\\frame%d.jpg" % i,image_box)
            img=cv2.imread("path_output\\frame%d.jpg" % i)
            plt.imshow(img)
            plt.show()
           
           
