<div align="center">

<samp>

<h2> Deformable Deep Networks for Instance Segmentation of Overlapping Multi Page Handwritten Documents</h2>

</samp>
  
<div align="left">
  
# Dependencies and Installation
## Manual Setup

The PALMIRA code is tested with

- Python (`3.8.10`)
- PyTorch (`1.9.0`)
- Detectron2 (`0.4.1`)
- CUDA (`10.2`)
- CudNN (`7.6.5-CUDA-10.2`)

For setup of Detectron2, please follow
the [official documentation](https://detectron2.readthedocs.io/en/latest/tutorials/install.html)

## Automatic Setup (From an Env File)

We have provided environment files for both Conda and Pip methods. Please use any one of the following.

### Using Conda

```bash
conda env create -f environment.yml
```

### Using Pip

```bash
pip install -r requirements.txt
```
# Usage

## Initial Setup:

- Download the IMMI dataset **[[`Dataset Link`](https://github.com/ihdia/indiscapes)]**
- Place the
    - Dataset under `images` directory
    - COCO-Pretrained Model weights in the `init_weights` directory
        - Weights
          used: [[`Mask RCNN R50-FPN-1x Link`](https://dl.fbaipublicfiles.com/detectron2/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x/137260431/model_final_a54504.pkl)]
    - JSON in `doc_pb` directory (a sample JSON has been provided [here](https://github.com/ihdia/Palmira/blob/main/doc_v2/via_region_data.json))

### SLURM Workloads

If your compute uses SLURM workloads, please load these (or equivalent) modules at the start of your experiments. Ensure
that all other modules are unloaded.

```bash
module add cuda/10.2
module add cudnn/7.6.5-cuda-10.2
```

