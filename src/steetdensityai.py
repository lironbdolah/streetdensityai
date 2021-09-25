from os import path,listdir
from matplotlib import pyplot as plt
import mplleaflet
import argparse
import pandas as pd
import numpy as np



def run(labels='path/labels',images='path/images',
                    coordinates='file.csv',img_per_cord=4,
                    output='runs/test'):
    try:
        labels_list = listdir(labels)
    except Exception:
        print('labels not found')
    try:
        images_list = listdir(images)
    except Exception:
        print('images not found')
    try:
        df = pd.read_csv(coordinates[0])
    except Exception:
        print('csv not found')

    add_missing_labels(labels,images_list)
    df['score'] = density_score(labels, img_per_cord)
    display_map(df, output)



def add_missing_labels(labels_path,image_list):

    labels_list = listdir(labels_path)

    if labels_list > labels_list:
        raise ValueError('You are missing some images')

    for image in image_list:
        image_text = image.replace('.jpg','.txt')
        if image not in labels_list:
            file = path.join(labels_path,image_text)
            open(file, "a")


def density_score(label_path, img_per_cord):
    # so they will fit to the number of coordinates
    label_list = listdir(label_path)
    density_score_list = []
    score = 0
    img = 1

    for file in label_list:
       if file.endswith('.txt'):
            text = open(path.join(label_path, file), "r")
            for line in text.readlines():
                try:
                    if int(line[0]) == 0:
                        score += 2
                    if int(line[0]) in [1, 2, 3, 4]:
                        score += 1

                except Exception:
                    pass
            img+=1
            if img > img_per_cord:
                density_score_list.append(score)
                score = 0
                img = 1
    return density_score_list


def display_map(df, output): #scatter plot to show pricing range and population by location
    lats = df['latitude']
    lons = df['longtitude']
    score = df['score']
    print(output)
    cmap = plt.cm.get_cmap("jet")
    plt.scatter(x=lons, y=lats, c=score, cmap=cmap)
    mplleaflet.show(path=path.join(output, 'map.html'))


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--labels', type=str, default='run/detect/labels',
                        help='Choose the tested images labels folder path')
    parser.add_argument('--images', type=str, default='run/detect/images',
                        help='Choose the tested images labels folder path')
    parser.add_argument('--coordinates',nargs='+',type=str, default='src/coordinates.csv',
                        help='Choose the coordinates file (.csv) folder path')
    parser.add_argument('--img-per-cord',type=int, default=1,
                        help='Choose the coordinates file (.csv) folder path')
    parser.add_argument('--output', default='path/output', help='Choose the .map folder path')
    opt = parser.parse_args()
    return opt


def main(opt):
    print(' '.join(f'{k}={v}' for k, v in vars(opt).items()))
    run(**vars(opt))


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
















