_base_ = './base_config.py'

# model settings
model = dict(
    name_path='./configs/cls_openearthmap.txt',
    prob_thd=0.1,
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
            img_path='/root/siton-data-412581749c3f4cfea0d7c972b8742057/data/rs_seg/OpenEarthMap_val/images',
            seg_map_path='/root/siton-data-412581749c3f4cfea0d7c972b8742057/data/rs_seg/OpenEarthMap_val/labels'),
        pipeline=test_pipeline))