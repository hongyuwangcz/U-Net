# plot the area in pic
import numpy as np
from scipy import misc
import os
from skimage import io
from skimage.transform import resize
from matplotlib import pyplot as plt
from skimage.measure import label, regionprops
import cv2
import matplotlib.patches as mpatches

image_dir = '/media/tina/Data/MedicalImage/BCDR/BCDR/crop/F03/img'
gt_dir = '/media/tina/Data/MedicalImage/BCDR/BCDR/crop/F03/gt'

plot_save_dir= '/media/tina/Data/MedicalImage/BCDR/BCDR/crop/F03/show'

list_image = os.walk(image_dir)
image_name = []
for root, dirs, files in list_image:
    for f in files:
#         get the name of image and store in image_name
        image_name.append(f)
#
N_img = len(image_name)
list_gt = os.walk(gt_dir)
# store the name of GroundTruth and store in gt_name
gt_name = []
for root, dirs, files in list_gt:
    for f in files:
        # get the name of gt
        gt_name.append(f)
N_gt = len(gt_name)

# load image and gt;
for pic in range(N_img):
    cropImgName = image_name[pic]
    # whether the name is in gt folder
    cropGtName = gt_name[pic]
    img = io.imread(os.path.join(image_dir,cropImgName)).astype('float32')
    gt = io.imread(os.path.join(gt_dir,cropGtName)).astype('float32')
#        gt=cv2.resize(gt,(300,200),interpolation=cv2.INTER_CUBIC)
#        img=cv2.resize(img,(300,200),interpolation=cv2.INTER_CUBIC)
   
    ret,gt = cv2.threshold(gt,150,255,cv2.THRESH_BINARY)
    # get the ROIs
    h, w = img.shape
    label_image = label(gt)
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.imshow(img,'gray')
    
    print_name = plot_save_dir+'/'+cropGtName    
    for region in regionprops(label_image):
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)

    ax.set_axis_off()
#        plt.show()
    fig.savefig(print_name,format='png')
    plt.show()
    plt.close(fig)
    print(print_name)
            




















#import matplotlib.pyplot as plt
#import matplotlib.patches as mpatches
#
#from skimage import data
#from skimage.filters import threshold_otsu
#from skimage.segmentation import clear_border
#from skimage.measure import label, regionprops
#from skimage.morphology import closing, square
#from skimage.color import label2rgb
#
#
#image = data.coins()[50:-50, 50:-50]
#
## apply threshold
#thresh = threshold_otsu(image)
#bw = closing(image > thresh, square(3))
#
## remove artifacts connected to image border
#cleared = clear_border(bw)
#
## label image regions
#label_image = label(cleared)
#image_label_overlay = label2rgb(label_image, image=image)
#
#fig, ax = plt.subplots(figsize=(10, 6))
#ax.imshow(image_label_overlay)
#
#for region in regionprops(label_image):
#    # take regions with large enough areas
#    if region.area >= 100:
#        # draw rectangle around segmented coins
#        minr, minc, maxr, maxc = region.bbox
#        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
#                                  fill=False, edgecolor='red', linewidth=2)
#        ax.add_patch(rect)
#
#ax.set_axis_off()
#plt.tight_layout()
#plt.show()