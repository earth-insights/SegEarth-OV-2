<div align="center">

<h1>Annotation-Free Open-Vocabulary Segmentation for Remote-Sensing Images</h1>

### We extend [SegEarth-OV](https://github.com/likyoo/SegEarth-OV) to SAR images. This is the first OVSS work for SAR images.

<div>
    <a href='https://likyoo.github.io/' target='_blank'>Kaiyu Li</a>&emsp;
    <a href='https://gr.xjtu.edu.cn/en/web/caoxiangyong' target='_blank'>Xiangyong Cao</a><sup>✉</sup>&emsp;
    <a href='https://scholar.google.com/citations?user=WTleRV8AAAAJ' target='_blank'>Ruixun Liu</a>&emsp;
    <a href='https://github.com/jackwang0108' target='_blank'>Shihong Wang</a>&emsp;
    <a href='https://github.com/AnXMuy' target='_blank'>Zixuan Jiang</a>&emsp;
    <a href='https://gr.xjtu.edu.cn/en/web/zhiwang' target='_blank'>Zhi Wang</a>&emsp;
    <a href='https://gr.xjtu.edu.cn/en/web/dymeng' target='_blank'>Deyu Meng</a>&emsp;
</div>
<div>
    Xi'an Jiaotong University&emsp;
</div>

<img src="https://likyoo.github.io/images/segearth_ov2.png" width="100%"/>
</div>


----
## News

- `2025-08-26` We release our code and [AlignEarth's weights](https://huggingface.co/likyoo/AlignEarth-SAR-ViT-B-16).
- `2025-08-26` We release the paper on [arXiv](https://arxiv.org/abs/2508.18067).

---

## Abstract
> *Semantic segmentation of remote sensing images is pivotal for comprehensive Earth observation, but the demand for interpreting new object categories, coupled with the high expense of manual annotation, poses significant challenges. Although open-vocabulary semantic segmentation (OVSS) offers a promising solution, existing frameworks designed for natural images are insufficient for the unique complexities of remote sensing data. They struggle with vast scale variations and fine-grained details, and their adaptation often relies on extensive, costly annotations. To address this critical gap, this paper introduces SegEarth-OV, the first framework for annotation-free open-vocabulary segmentation of remote sensing images. Specifically, we propose SimFeatUp, a universal upsampler that robustly restores high-resolution spatial details from coarse Vision-Language Model (VLM) features, correcting distorted target shapes without any task-specific post-training. We also present a simple yet effective Global Bias Alleviation operation to subtract the inherent global context from patch features, significantly enhancing local semantic fidelity. These components empower SegEarth-OV to effectively harness the rich semantics of pre-trained VLMs, making OVSS possible in optical remote sensing contexts. Furthermore, to extend the framework's universality to other challenging remote sensing modalities like Synthetic Aperture Radar (SAR) images, where large-scale pre-trained VLMs (e.g. SAR-CLIP) are unavailable and prohibitively expensive to create, we introduce AlignEarth, which is a distillation-based strategy and can efficiently transfer semantic knowledge from an optical VLM encoder to an SAR encoder, bypassing the need to build SAR foundation models from scratch and enabling universal OVSS across diverse sensor types. Extensive experiments on both optical and SAR datasets validate that our proposed SegEarth-OV can achieve dramatic improvements over the state-of-the-art methods, establishing a robust foundation for annotation-free and open-world Earth observation.*

## Dependencies and Installation

```
# 1. install SimFeatUp
# refer to https://github.com/likyoo/SimFeatUp

# 2. git clone this repository
git clone https://github.com/earth-insights/SegEarth-OV-2.git
cd SegEarth-OV

# 3. create new anaconda env
conda create -n SegEarth python=3.9
conda activate SegEarth

# 4. install torch and dependencies
pip install -r requirements.txt
# The dependent versions are not strict, and in general you only need to pay attention to mmcv and mmsegmentation.

# 5. download the weights of AlignEarth
# HuggingFace: https://huggingface.co/likyoo/AlignEarth-SAR-ViT-B-16
# Baidu Disk: https://pan.baidu.com/s/1X-AOk3cgJoyU9qoOQKut9A?pwd=7mtz
```

## Datasets

For SAR images, you can download all datasets directly [here](https://pan.baidu.com/s/10SKcIRJYnMcoyNfE8iouEQ?pwd=i4tt).

For optical images, please refer to [dataset_prepare.md](https://github.com/likyoo/SegEarth-OV/blob/main/dataset_prepare.md) for dataset preparation.


## Model evaluation
Single-GPU:

```
python eval.py --config ./configs/cfg_DATASET.py --workdir YOUR_WORK_DIR
```

Multi-GPU:
```
bash ./dist_test.sh ./config/cfg_DATASET.py
```

Evaluation on all datasets:
```
python eval_all.py
```
Results will be saved in `results.xlsx`.


## Citation

```
@article{li2025segearthov2,
  title={Annotation-Free Open-Vocabulary Segmentation for Remote-Sensing Images},
  author={Li, Kaiyu and Cao, Xiangyong and Liu, Ruixun and Wang, Shihong and Jiang, zixuan and Wang, Zhi and Meng, Deyu},
  journal={arXiv preprint arXiv:2508.18067},
  year={2025}
}
```
