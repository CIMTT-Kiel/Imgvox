# Imgvox
## 2D and 3D representations of 812k Parts based on the ABC dataset 

This dataset contains 812.294 part representations. Each Sample includes a 2D and a 3D representation. The Samples are processed based on the [ABC dataset](https://deep-geometry.github.io/abc-dataset/), which includes a large number of technical parts. Therefore, this dataset is especially for researchers and engineers in industrial contexts. It is tailored to support the research in optimizing manufacturing processes through unsupervised and semi-supervised learning techniques.

## Key Features:

### Dual Representation:

#### 2D Views: 
Each part has 2D projections resembling traditional technical drawing views (front, side, top). These views are essential for tasks that require shape analysis based on typical design schematics. The resolution per view is 224x224. 

#### 3D Voxel Models: 
Each part is also represented in 3D through a voxel representation, offering a simplified geometric representation. These voxel models are highly suitable for computational geometry. Due to the fixed resolution parts with a high expansion along one axis, details cannot be resolved in some cases. The resolution in this dataset is 128x128x128. 
Unlabeled Data for Unsupervised Learning: This dataset is unlabeled and is specially built for un- and semisupervised representation learning of geometric features via autoencoder. 

### Industrial Relevance: 
The dataset is tailored for research that optimizes industrial manufacturing processes. It also contains many technical parts, as the ABC dataset is its basis. 

### Scale and Diversity: 
With over 812k samples, the dataset covers a wide range of part geometries and structures. This scale also allows extensive experimentation with data-intensive approaches. 

## Dataset Format:
The dataset is split into chunks of 100.000 samples. The modalities are stored separately and can be downloaded separately if needed. In images, the 2D files are stored. Each 2D filename begins with "imgRep_ followed by an eight-digit ID. In voxels analogous, the 3D data is stored. Each file begins with a marker "voxRep_" followed by the eight-digit ID. Each ID is unique for one represented part. In this way, the samples can be mapped. The IDs are kept from the ABC-Dataset, so you can refer to the original Part if needed. Both representations are stored as sparse vectors in "npz" files to minimize storage and processing time. 

### 2D Views:
These are provided as greyscale "images" with standard orthographic projections (front, side, top). According to these views, the images are stored as a sparse Array with the shape [3, 224, 224]. The entries are stored as float16 with a range between zero and one. 

### 3D Voxel Models: 
Analogously, 3D data is represented as binary voxel grids with shape [128,128,128].  A Voxel is defined as an entry with the value one. Zero represents an empty grid element. 

### Usage
The repository uses git lfs. to download the zip files, you may need to use:

```
git lfs pull
```

after cloning. The script ```scripts/unpack_archives.py``` can be used for unpacking. 



### Licensing and Citation:

This dataset is based on the [ABC dataset ](https://deep-geometry.github.io/abc-dataset/) and follows the MIT License. If you use this dataset, please cite the [ABC dataset](https://deep-geometry.github.io/abc-dataset/) and the following paper in your research.

The copyright of the original CAD models of the [ABC dataset](https://deep-geometry.github.io/abc-dataset/), which were used to create the imgvox dataset, is owned by its creators. For licensing details, please refer to Onshape [Terms of Use 1.g.ii](https://www.onshape.com/en/legal/terms-of-use).


## Download 

By downloading the dataset, you agree to the following terms:

- The authors give no warranties regarding the dataset.
