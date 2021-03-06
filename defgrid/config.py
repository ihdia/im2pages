from detectron2.config import CfgNode as CN


def add_defgrid_maskhead_config(cfg):
    cfg.MODEL.DEFGRID_MASK_HEAD = CN()
    cfg.MODEL.DEFGRID_MASK_HEAD.GRID_NUM = 1024
    cfg.MODEL.DEFGRID_MASK_HEAD.STATE_DIM = 128
    cfg.MODEL.DEFGRID_MASK_HEAD.GRID_SIZE = [14, 14]
    cfg.MODEL.DEFGRID_MASK_HEAD.FEATURE_CHANNEL_NUM = 128
    cfg.MODEL.DEFGRID_MASK_HEAD.OUT_DIM = 196
    cfg.MODEL.DEFGRID_MASK_HEAD.DEFORM_LAYER_NUM = 8
    cfg.MODEL.DEFGRID_MASK_HEAD.GRID_TYPE = (
        'dense_quad'  # choices=['lattice', 'quad', 'dense_quad', 'quad_angle']
    )
    cfg.MODEL.DEFGRID_MASK_HEAD.MASK_COEF = 0.3
    cfg.MODEL.DEFGRID_MASK_HEAD.W_VARIANCE = 1.0
    cfg.MODEL.DEFGRID_MASK_HEAD.W_AREA = 0.01
    cfg.MODEL.DEFGRID_MASK_HEAD.W_LAPLACIAN = 0.01
    cfg.MODEL.DEFGRID_MASK_HEAD.W_RECONSTRUCT_LOSS = 0.5
    cfg.MODEL.DEFGRID_MASK_HEAD.GAMMA = 0.1
    cfg.MODEL.DEFGRID_MASK_HEAD.SIGMA = 0.001
