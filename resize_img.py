import cv2
import os 

def resize_img(folder_path, new_size):

    for filename in os.listdir(folder_path):
        img = cv2.imread(os.path.join(folder_path, filename), cv2.IMREAD_UNCHANGED)
        resized_img = cv2.resize(img, (new_size, new_size))
        cv2.imwrite(os.path.join(folder_path, filename), resized_img)

if __name__ == '__main__':
    path = "material/food"
    resize_img(path, 50)
