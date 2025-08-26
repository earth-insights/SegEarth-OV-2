_base_ = './base_config.py'

# model settings
model = dict(
    name_path='./configs/cls_openearthmap_sar.txt',
    clip_type='AlignEarth',
    model_type='SCLIP', # use qq-kk attention is better.
    prob_thd=0,
    ssa_last_n_layers=2,
)

# dataset settings
dataset_type = 'OpenEarthMapDataset'
data_root = ''

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(448, 448), keep_ratio=True),
    # add loading annotation after ``Resize`` because ground truth
    # does not need to do resize data transform
    dict(type='LoadAnnotations'),
    dict(type='PackSegInputs')
]

test_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        reduce_zero_label=False,
        data_prefix=dict(
            img_path='data/OpenEarthMap_SAR/test/sar_images',
            seg_map_path='data/OpenEarthMap_SAR/test/labels'),
        pipeline=test_pipeline))