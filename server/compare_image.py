from skimage.measure import compare_ssim as ssim
from skimage import io


def img_similarity(loc1, loc2):
    im1 = io.imread(loc1)
    im2 = io.imread(loc2)
    similarity_score = ssim(im1, im2, multichannel = True)
    return similarity_score