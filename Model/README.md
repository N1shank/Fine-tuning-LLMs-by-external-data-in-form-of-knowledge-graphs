
## Installation
Note : Python version: 3.6.0 
```bash
python -m pip install -r requirements.txt
```
If you face any issues on installing torch-geometric library, please refer to [torch-geometric github](https://github.com/pyg-team/pytorch_geometric).

## Dataset

I have already downloaded datasets and attached in the codebase!

## Knowledge Graph Construction
To construct the Knowledge Graph (KG) for each dataset, please follow the below instructions.
If you are interested in how the KG is constructed, please refer to codes in `KGC` folder.

1. Entity Extraction

Please download `en_core_web_md` in spacy library and spaCy-entity-linker library here: https://github.com/egerber/spaCy-entity-linker.

Be sure to run `python -m spacy_entity_linker "download_knowledge_base"` command to download the knowledge base for entity linker.

They are needed to correctly extract entities from the context, and to map them to the corresponding Wikidata ids.

Below are the example scripts for preprocessing the NewsQA dataset.

```bash
python preprocess.py NewsQA train
python preprocess.py NewsQA dev
python preprocess.py NewsQA test
```

2. Knowledge Graph Construction


Below are the example scripts for KG construction on the NewsQA dataset.

```bash
python construct.py --domain NewsQA --fold train
python construct.py --domain NewsQA --fold dev
python construct.py --domain NewsQA --fold test 
```

While the example scripts above are for question answering tasks, you can similarly run the code for named entity recognition tasks via the file: {filename}_ner.py.

## Training
After preprocessing, the preprocessed dataset files are stored at `./KGC/TASK/$DATA_NAME` with a default setting.

Then, run the below code to train the model for the NewsQA dataset over our Model framework.

```bash
python run_qa.py --data_dir ./KGC/TASK/NewsQA
```

This code runs 2 epochs of training on the NewsQA dataset. It takes approximately 3 hours on a single GeForce RTX 2080 Ti GPU.

## Fine-tuned Checkpoint

run the following code to reproduce the result on the NewsQA dataset.

```bash
python run_qa.py --do_eval --checkpoint ./NewsQA_ckpt/ --data_dir ./KGC/TASK/NewsQA
```

