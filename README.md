# Multimodal-Sentiment-Analysis

## Introduction
Our project focuses on multimodal sentiment analysis, specifically on improving the accuracy of an existing model developed by [Kaicheng Yang](https://github.com/thuiar/Cross-Modal-BERT) by integrating an additional visual modality. This project is also extended to investigate the multilingual aspect of sentiment analysis by training the model on a Chinese dataset, with the aim of providing a more comprehensive understanding of sentiment across different languages. 

## Model Architecture 

## Directory Structure 
```
.
├── CMU-MOSEI
│   ├── data
│   │   ├── audio
│   │   │   └── MOSEI_cmu_audio_CLS.pickle                   
│   │   ├── text
│   │   │   ├── dev.tsv
│   │   │   ├── test.tsv
│   │   │   └── train.tsv
|   |   └── video
|   |       └── MOSEI_cmu_video_CLS.pickle
|   ├── pre-trained BERT
|   |   ├── bert_config.json
|   |   └── pytorch_model.bin
|   ├── CMU-MOSEI.ipynb
|   ├── model.py
|   ├── requirements.txt
|   ├── run_classifier_video.py
|   ├── run_classifier.py
|   └── utils.py
├── CMU-MOSI
└── SIMS
```

## Usage
1. Download data and pre-trained BERT folder from [here](https://drive.google.com/drive/folders/13LcOQV7wlpDtJiLhXP4XODEYikXX02vn?usp=sharing)

2. Ensure directory structure follows the [specified](#directory-structure) format

3. Navigate to the directory containing your dataset of interest (CMU-MOSEI / CMU-MOSI / SIMS)
```
cd CMU-MOSEI
```

4. Install all required libraries

```
pip install -r requirements.txt
```

5. Run experiments
```
# original (audio + text)
python run_classifier.py

# improvised (audio + text + video)
python run_classifier_video.py
```

## References
AmirAli Bagher Zadeh, Rowan Zellers, Eli Pincus, and Louis-Philippe Morency. 2016. Mosi: multimodal corpus of sentiment intensity and subjectivity analysis in online opinion videos. arXiv preprint arXiv:1606.06259. https://doi.org/10.48550/arXiv.1606.06259

AmirAli Bagher Zadeh, Paul Pu Liang, Soujanya Poria, Erik Cambria, and Louis-Philippe Morency. 2018. Multimodal Language Analysis in the Wild: CMU-MOSEI Dataset and Interpretable Dynamic Fusion Graph. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 2236–2246, Melbourne, Australia. Association for Computational Linguistics. https://doi.org/10.18653/v1/P18-1208

Kaicheng Yang, Hua Xu, and Kai Gao. 2020. CM-BERT: Cross-Modal BERT for Text-Audio Sentiment Analysis. In Proceedings of the 28th ACM International Conference on Multimedia (MM '20). Association for Computing Machinery, New York, NY, USA, 521–528. https://doi.org/10.1145/3394171.3413690

Wenmeng Yu, Hua Xu, Fanyang Meng, Yilin Zhu, Yixiao Ma, Jiele Wu, Jiyun Zou, and Kaicheng Yang. 2020. CH-SIMS: A Chinese Multimodal Sentiment Analysis Dataset with Fine-grained Annotation of Modality. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 3718–3727, Online. Association for Computational Linguistics. https://doi.org/10.18653/v1/2020.acl-main.343
