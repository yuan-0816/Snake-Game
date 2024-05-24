import os 



def check_file_type(file_path: str) -> str:
    img_formats = ["bmp", "jpg", "jpeg", "png", "tif", "tiff", "dng", "webp"]
    vid_formats = ["mov", "avi", "mp4", "mpg", "mpeg", "m4v", "wmv", "mkv"]

    file_extension = file_path.split(".")[-1].lower()

    if file_extension in img_formats:
        return "image"
    elif file_extension in vid_formats:
        return "video"
    else:
        return "unknown"

def get_images_path_list(folder_path: str) -> list:
    file_list = os.listdir(folder_path)
    images_list = []

    for file_name in file_list:
        if check_file_type(file_name) == "image":

            file_path = os.path.join("./material/food/", file_name)
            images_list.append(file_path)
    
    return images_list


if __name__ == "__main__":
    path_lists = get_images_path_list("./material/food")
    for list in path_lists:
        print(list)
    # print(path_lists)