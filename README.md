<div align="center">

<samp>

<h2> Deformable Deep Networks for Instance Segmentation of Overlapping Multi Page Handwritten Documents</h2>

</samp>
  
<div align="left">
  
<img src="/assets/Im2page_Architecture.png"/>
  
# Dependencies and Installation
## Manual Setup

The IM2PAGES code is tested with

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

- Download the IMMI dataset **[[`Dataset Link`](https://zenodo.org/record/5591969#.YXOWKxpBxPY)]**
- Place the
    - Dataset under `images` directory
    - COCO-Pretrained Model weights and Palmira pretrained weights in the `init_weights` directory
        - Weights
          used:
          -COCO-Pretrained Model weights: [[`Mask RCNN R50-FPN-1x Link`](https://dl.fbaipublicfiles.com/detectron2/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x/137260431/model_final_a54504.pkl)]
          -Indiscapesv2 Pretrained Model weights: [[`Palmira model weights`]](https://zenodo.org/record/4841067#.YXOWqxpBxPY)
    - JSON in `doc_pb` directory

### SLURM Workloads

If your compute uses SLURM workloads, please load these (or equivalent) modules at the start of your experiments. Ensure
that all other modules are unloaded.

```bash
module add cuda/10.2
module add cudnn/7.6.5-cuda-10.2
```
## Training

### Palmira and variants

Train the presented networks

```bash
python train_palmira.py \
    --config-file configs/palmira/Palmira.yaml \
    --num-gpus 4
```
- Any required hyper-parameter changes including initial weights can be performed in the `Palmira.yaml` file.
- To run the experiment of palmira and its variants change the input config files in the args section
- Resuming from checkpoints can be done by adding `--resume` to the above command.
  
 ## Inference

### Quantitative

To perform inference and get quantitative results on the test set.

```bash
python train_palmira.py \
    --config-file corresponding_config.yaml \
    --eval-only \
    MODEL.WEIGHTS <path-to-model-file> 
```

- This outputs 2 json files in the corresponding output directory from the config.
    - `coco_instances_results.json` - This is an encoded format which is to be parsed to get the [qualitative results](https://github.com/ihdia/Palmira#qualitative)
    - `immi_test_coco_format.json` - This is regular coco encoded format which is human parsable
        
### Qualitative

Can be executed only after quantitative inference (or) on validation outputs at the end of each training epoch.

This parses the output JSON and overlays predictions on the images.

```bash
python visualise_json_results.py \
    --inputs <path-to-output-file-1.json> [... <path-to-output-file-2.json>] \
    --output outputs/qualitative/ \
    --dataset immi_test
```

> NOTE: To compare multiple models, multiple input JSON files can be passed. This produces a single
> vertically stitched image combining the predictions of each JSON passed.

### Custom Images

To run the model on your own images without training, please download the provided weights from  **[[`here`](https://zenodo.org/record/5592133#.YXOabhpBxPY)]** for FT-Palmira-AS and here **[[`here`](https://zenodo.org/record/5592139#.YXOaqhpBxPY)]** for FT-Vanilla Mask RCNN .

```bash
python demo.py \
    --input <path-to-image-directory-*.jpg> \
    --output <path-to-output-directory> \
    --config corresponding_config.yaml \
    --opts MODEL.WEIGHTS <Pretrained_model_weights.pth>
```
 ### Sample Outputs
 <img src="/assets/Im2page_results1-1.png"/>
# Contact

For any queries, please contact [Dr. Ravi Kiran Sarvadevabhatla](mailto:ravi.kiran@iiit.ac.in.)

# License

This project is open sourced under [MIT License](LICENSE).
