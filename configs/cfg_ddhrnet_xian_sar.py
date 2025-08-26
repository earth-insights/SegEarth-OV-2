_base_ = './base_config.py'

# model settings
model = dict(
    name_path='./configs/cls_ddhrnet_xian_sar.txt',
    clip_type='AlignEarth',
    model_type='SCLIP', # use qq-kk attention is better.
    prob_thd=0,
    slide_crop=0,
    ssa_last_n_layers=2,
)

# dataset settings
dataset_type = 'DDHR_Xian_SARDataset'
data_root = ''

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(224, 224), keep_ratio=True),
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
        ann_file='data/DDHRNet_DATA/xian/no_cloud/val.txt',
        data_prefix=dict(
            img_path='data/DDHRNet_DATA/xian/no_cloud/sar',
            seg_map_path='data/DDHRNet_DATA/xian/no_cloud/label'),
        pipeline=test_pipeline))