import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_diference(imageA, imageB):
   assert imageA.shape == imageB.shape, "Images must have the same dimensions"
   grayA = rgb2gray(imageA)
   grayB = rgb2gray(imageB)
   (score, diference_image) = structural_similarity(grayA, grayB, full=True)
   print("Similarity score:", score)
   normalized_diference_image  = (diference_image - diference_image.min()) / (diference_image.max() - diference_image.min())
   return score, normalized_diference_image

def transfer_histogram(imageA, imageB):
   matched_image = match_histograms(imageA, imageB, multichannel=True)
   return matched_image
