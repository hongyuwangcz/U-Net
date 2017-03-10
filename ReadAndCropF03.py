import csv
import scipy.io as io
from PIL import Image, ImageDraw
import numpy as np
from matplotlib import pyplot as plt
from Cropping import crop
from scipy import misc

image_dir = './Data/img'
gt_dir = './Data/gt'

#plot_save_dir= './Data/crop/cropShow/'
crop_img_save_dir = '/media/tina/Data/MedicalImage/BCDR/BCDRdata/crop/F03/img'
crop_gt_save_dir = '/media/tina/Data/MedicalImage/BCDR/BCDRdata/crop/F03/gt'
crop_size = [256,256]
patchNum = 0
saveF03Info = []

with open('bcdr_f03_outlines.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        flag = int(row['mammography_nodule'])
        if flag == 1:
            image_name = str('./'+row['image_filename'])
            print image_name
            im = Image.open(image_name)
            im = np.array(im)
            h,w = im.shape
            
            pX = row['lw_x_points']
            pX=pX.split()
            X =[int(x) for x in pX]
                
            pY = row['lw_y_points']
            pY = pY.split()
            Y = [int(y) for y in pY]
    
    # get the gt of original image
            polygon = zip(X, Y)
            cell_mask = Image.new('L', (w, h), 0)
            ImageDraw.Draw(cell_mask).polygon(polygon, fill=255)
            
            gt = np.array(cell_mask)
            crop_img,crop_gt = crop(im,gt,crop_size)
            for rr in range(len(crop_img)):            
                saveF03Info.append([image_name+ str("%04d" % patchNum) + '.png'])
                saveImgName = crop_img_save_dir+ '/'+ str("%04d" % patchNum) + '.png'
                saveGtName = crop_gt_save_dir + '/'+ str("%04d" % patchNum) + '.png'
#                plt.imshow(crop_img,'gray')
#                plt.imshow(crop_gt,'gray')
                misc.imsave(saveImgName, crop_img[rr])
                misc.imsave(saveGtName, crop_gt[rr])
                
                patchNum = patchNum + 1
        
        
#       crop the image
        

        
             

