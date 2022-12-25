import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

from astropy.utils.data import download_file
img1 = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache =True)


hdu_list = fits.open(img1)
hdu_list.info()

img1_data = fits.getdata(img1)
hdu_list.close()

print(img1_data)
print("---\n")

plt.imshow(img1_data, cmap='gray')
plt.colorbar()

#below not necessary in collab notebooks
plt.show()
