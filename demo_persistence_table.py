# Demo: print the persistence table findpeaks produces for its built-in example image.
from findpeaks import findpeaks

fp = findpeaks(method='topology', scale=True, togray=False,
               denoise=None, imsize=(200, 200), verbose=0)
img = fp.import_example()
results = fp.fit(img)

print(results['persistence'].head(10))
