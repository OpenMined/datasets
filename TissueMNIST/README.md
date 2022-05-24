### Original TissueMNIST


Data Modality: Kidney Cortex Microscope
Task: Multi-Class (8)
Number of Samples: 236,386 (165,466 / 23,640 / 47,280)
Source Data:
Vebjorn Ljosa, Katherine L Sokolnicki, et al., “Annotated high-throughput microscopy imagesets for validation.,” Nature methods, vol. 9, no. 7, pp.637–637, 2012.

We use the BBBC051, available from the Broad Bioimage Benchmark Collection. The dataset contains 236,386 human kidney cortex cells, segmented from 3 reference tissue specimens and organized into 8 categories. We split the source dataset with a ratio of 7:1:2 into training, validation and test set. Each gray-scale image is 32×32×7 pixels, where 7 denotes 7 slices. We take maximum values across the slices and resize them into 28×28 gray-scale images.

**Md5**: ebe78ee8b05294063de985d821c1c34b

**Url**: https://zenodo.org/record/5208230/files/tissuemnist.npz?download=1

**Task**: multi-class

**Label**: {'0': 'Collecting Duct, Connecting Tubule', '1': 'Distal Convoluted Tubule', '2': 'Glomerular endothelial cells', '3': 'Interstitial endothelial cells', '4': 'Leukocytes', '5': 'Podocytes', '6': 'Proximal Tubule Segments', '7': 'Thick Ascending Limb'}

**N_channels**: 1

**N_samples**: {'train': 165466, 'val': 23640, 'test': 47280}

**License**: CC BY 3.0

**Reference**: https://medmnist.com/

### Modified TissueMNIST


The original data was collected from 3 reference tissue specimens. But we have modified this number to 1000 different specimens i.e. the cell images have been distributed randomly across the 1000 unique patient ids. This has been to done to demonstrate that through our library [PySyft](https://github.com/OpenMined/PySyft) we can perform multiple queries while preserving the privacy of a large group of people at scale.

Further we have merged the train, val and test sets of the original dataset into a single dataset and then created 100 unique subsets from the unison. The subsets are distributed across the participants so that each one can act as an individual Data Owner.
