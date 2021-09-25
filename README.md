

<p align="center">
<img alt="Street Density ai" src="assets/test.png" width="300">
</p>

<p align="center">
https://img.shields.io/github/license/lironbdolah/streetdensityai
</p>

This YoloV5 based model is fit to detect people and diffrent types of land veichels,
and displaying their relative density on a fiited map, acoording to their coordinates and detected labels. 

**Features:**

- Multiple Objects Detection
- Trained on 3,000 street view Images
- Exports Fitted and adjustable Maps
- Calculates a density score according to an image detected labels 


<p align="center">
  <img src="assets/streetdensityai.png" />
</p>


## Manual

Download the files 

## Usage

****Object Detection:**** 

identifies people and land vehicles in your images:

```shell
python src/yolov5/detect.py --source  <path to images folder> --project <output path>
--name <output folder name> --save-txt --conf 0.3
```
running this action will save your images with the anchor boxes around objects that the model found:

<img src="assets/step1.png" />

in addition, it will save the detcted object labels for each image.



 ****Plotting a fitted map:****
 
 display the density on a fitted map (requiers as csv file with the coordinats)
 
```shell
python src/steetdensityai.py --labels <labels path that were created after the images detection>
--coordinates <path-to-csv/file.csv>  --images <path to images folder>
--img-per-cord 1 --output <output path>
```
<img src="assets/step2.png" />

#### notes
- csv requires 2 columns to display the coordinates named: "longtitude" and "lattitude"
- the code asuumes that the coordinates are sorted by the images name.
- If you have multiple images per coordinate (for example if you have a 360 view, divided to 4 images), you can set the amount of images per coodinate with : ```--img-per-cord <integer of images per coordinate > ```

 
## Simple Example
