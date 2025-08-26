import mmcv
import matplotlib.pyplot as plt
from torchvision import transforms
from segearth_segmentor import SegEarthSegmentation


img = mmcv.imread('YOUR_IMG_PATH', channel_order='rgb')

name_list = ['building', 'road', 'greenery', 'water', 'farmland,grass']

with open('./configs/my_name.txt', 'w') as writers:
    for i in range(len(name_list)):
        if i == len(name_list)-1:
            writers.write(name_list[i])
        else:
            writers.write(name_list[i] + '\n')
writers.close()


img_tensor = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.48145466, 0.4578275, 0.40821073], [0.26862954, 0.26130258, 0.27577711]),
    transforms.Resize((224, 224))
])(img)

img_tensor = img_tensor.unsqueeze(0).to('cuda')

model = SegEarthSegmentation(
    clip_type='AlignEarth',
    vit_type='ViT-B/16',
    model_type='SCLIP',
    ignore_residual=True,
    feature_up=True,
    feature_up_cfg=dict(
        model_name='jbu_one',
        model_path='simfeatup_dev/weights/xclip_jbu_one_million_aid.ckpt'),
    cls_token_lambda=-0.3,
    name_path='./configs/my_name.txt',
    prob_thd=0,
    slide_crop=0,
    ssa_last_n_layers=2,
)

seg_pred = model.predict(img_tensor, data_samples=None)
seg_pred = seg_pred.data.cpu().numpy().squeeze(0)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].imshow(img)
ax[0].axis('off')
ax[1].imshow(seg_pred, cmap='viridis')
ax[1].axis('off')
plt.tight_layout()
# plt.show()
plt.savefig('seg_pred.png', bbox_inches='tight')