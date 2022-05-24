The MedNIST dataset was gathered from several sets from TCIA, the RSNA Bone Age Challenge, and the NIH Chest X-ray dataset.

The dataset is kindly made available by Dr. Bradley J. Erickson M.D., Ph.D. (Department of Radiology, Mayo Clinic) under the Creative Commons CC BY-SA 4.0 license. If you use the MedNIST dataset, please acknowledge the source, e.g. https://colab.research.google.com/drive/1wy8XUSnNWlhDNazFdvGBHLfdkGvOHBKe#scrollTo=ZaHFhidyCBJa

The MedNIST data has been store as a pickle file. Each image is mapped to its integer encoded label and a pseudo patient id is added. The labels use the following mapping:
{
    "AbdomenCT": 0, 
    "BreastMRI": 1, 
    "CXR": 2, 
    "ChestCT": 3, 
    "Hand": 4, 
    "HeadCT": 5
}

