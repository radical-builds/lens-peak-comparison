# lens-peak-comparison
# Peak comparison for lensed images

Compares two images (a lensed image, and the same image with substructure) by finding the strongest peaks in each and measuring how far they moved.

Functions:
- `find_peak_coords`: filters findpeaks' output to strong peaks and converts them to centred, 100-pixel coordinates.
- `compare_images`: returns the mean squared error between peak positions.

Requires: `pip install findpeaks numpy`
