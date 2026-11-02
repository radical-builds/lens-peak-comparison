import numpy as np
from findpeaks import findpeaks

pixels = 100

def find_peak_coords(results, imsize):
    """
    Takes the output of findpeaks and returns the coordinates of the peaks.

    Arguments:
        results: results object returned by findpeaks.
        imsize: float - The size the image was rescaled to.

    Returns:
        measured_x: np.ndarray - The measured x coordinates of the peaks in standard pixels.
        measured_y: np.ndarray - The measured y coordinates of the peaks in standard pixels.
    """
    peak=0
    xvalues = []
    yvalues = []

    for p in results['persistence']['score']:
        # Only accept a peak if findpeaks is pretty confident in it.
        if p > 200:
            peak +=1
            xvalues.append((results['persistence']['x'][:peak])[0])
            yvalues.append((results['persistence']['y'][:peak])[0])
    measured_x = (np.array(xvalues) - imsize/2) * pixels/imsize
    measured_y = (np.array(yvalues) - imsize/2) * pixels/imsize
    return measured_x, measured_y

def compare_images (lensed_image, substructure_image):
    """
    Arguments:
        lensed_image: np.ndarray - A 2D array of intensities.
        substructure_image: np.ndarray - A 2D array of intensities.

    Returns:
        mserror: float - The mean squared error between the peaks of the two images.
    """
    # Ideal imsize for low uncertainty, as found by chi-squared error.
    imsize = 200

    fp = findpeaks(imsize = (int(imsize), int(imsize)), scale = True, togray = False, denoise = None, verbose = 2)

    results = fp.fit(lensed_image)
    xvalues1, yvalues1 = find_peak_coords(results, imsize)

    results = fp.fit(substructure_image)
    xvalues2, yvalues2 = find_peak_coords(results, imsize)

    # Mean squared error, to quantify the difference between the two sets of peaks.
    mserror = np.mean((xvalues2-xvalues1)**2 + (yvalues2-yvalues1)**2)
    return mserror
