## Breast Cancer Dataset


Invasive Ductal Carcinoma (IDC) is the most common subtype of all breast cancers. To assign an aggressiveness grade to a whole mount sample, pathologists typically focus on the regions which contain the IDC. As a result, one of the common pre-processing steps for automatic aggressiveness grading is to delineate the exact regions of IDC inside of a whole mount slide.


The original dataset consisted of 162 whole mount slide images of Breast Cancer (BCa) specimens scanned at 40x. From that, 277,524 patches of size 50 x 50 were extracted.


The original data was collected from 279 patients. But we have modified this number to 1000 different patients i.e. the images have been distributed randomly across the 1000 unique patient ids. This has been to done to demonstrate that through our library PySyft we can perform multiple queries while preserving the privacy of a large group of people at scale.

Further we have created 100 unique subsets from the dataset and distributed across the participants so that each one can act as an individual Data Owner.
