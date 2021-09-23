import os
from os import listdir,path
from PIL import Image
import glob


def adjust_text_labels(text_list ,text_path):
    for file in text_list:
        with open(path.join(text_path,file), "r") as f:
            lines = f.readlines()
        with open(path.join(text_path,file), "w") as f:
            for line in lines:
              try:
                if int(line[0]) == 0 and line[1] == ' ':
                    f.write(line)
                elif int(line[0]) == 2 and str(line[1]) == ' ':
                    f.write("1 " + line[2:])
                elif int(line[0]) == 3  and line[1] == ' ':
                    f.write("2 " + line[2:])
                elif int(line[0]) == 5  and line[1] == ' ':
                    f.write("3 " + line[2:])
                elif int(line[0]) == 7  and line[1] == ' ':
                    f.write("4 " + line[2:])
              except Exception:
                   pass
        if path.getsize(path.join(text_path,file)) == 0: # remove label less files
            os.remove((path.join(text_path,file)))


def reduce_images_size(images_path):
    image_list = listdir(images_path)
    for name in image_list:
        if name.endswith('_5.jpg') or name.endswith('_0.jpg'):  # remove_uneccery_images
            os.remove(path.join(images_path, name))
        else:
            image = Image.open(path.join(images_path, name))
            image = image.crop((0, 400, 1024, 1280)).resize((1024, 880), Image.ANTIALIAS)
            image.save(path.join('images/Reduced', name))


def get_weights_path():
    best_weights_path = max(glob.glob(os.path.join('runs/train/*')), key=os.path.getmtime)  # gets last run file
    best_weights_path = best_weights_path.replace(os.sep, '/')
    best_weights_path = os.path.join(best_weights_path + '/weights/best.pt')
    return best_weights_path


def get_test_labels_path():
    test_labels_path = max(glob.glob(os.path.join('runs/detect/*')), key=os.path.getmtime)
    test_labels_path = test_labels_path.replace(os.sep, '/')
    test_labels_path = os.path.join(test_labels_path + '/labels')
    return test_labels_path


def get_training_results_path():
    training_results_path = max(glob.glob(os.path.join('runs/train/*')), key=os.path.getmtime)
    training_results_path = training_results_path.replace(os.sep, '/')
    return training_results_path

def add_missing_labels(test_labels_list,test_labels_path,test_image_list):
    for image in test_image_list:
        image = image.replace('.jpg','.txt')
        if image not in test_labels_list:
            file = path.join(test_labels_path,image)
            open(file, "a")



