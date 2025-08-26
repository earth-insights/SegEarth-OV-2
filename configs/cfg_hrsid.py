_base_ = './base_config.py'

# model settings
model = dict(
    name_path='./configs/cls_hrsid.txt',
    prob_thd=0.6,
    slide_crop=0,
)

# dataset settings
dataset_type = 'HRSID_SARDataset'
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
        ann_file='/root/siton-data-412581749c3f4cfea0d7c972b8742057/data/rs_sar/HRSID/HRSID_JPG/label/test.txt',
        data_prefix=dict(
            img_path='/root/siton-data-412581749c3f4cfea0d7c972b8742057/data/rs_sar/HRSID/HRSID_JPG/JPEGImages', 
            seg_map_path='/root/siton-data-412581749c3f4cfea0d7c972b8742057/data/rs_sar/HRSID/HRSID_JPG/label/test'),
        pipeline=test_pipeline))