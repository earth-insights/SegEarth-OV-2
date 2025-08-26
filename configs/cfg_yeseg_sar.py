_base_ = './base_config.py'

# model settings
model = dict(
    name_path='./configs/cls_yeseg_sar.txt',
    clip_type='AlignEarth',
    model_type='SCLIP', # use qq-kk attention is better.
    slide_crop=0,
    prob_thd=0.3,
    ssa_last_n_layers=2,
)

# dataset settings
dataset_type = 'YESegSARDataset'
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
        ann_file='data/YESeg-OPT-SAR/test.txt',
        data_prefix=dict(
            img_path='data/YESeg-OPT-SAR/sar',
            seg_map_path='data/YESeg-OPT-SAR/cvt_label'),
        pipeline=test_pipeline))