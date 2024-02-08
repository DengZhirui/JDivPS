# JDivPS
JDivPS: A Diversified Product Search Dataset
# Dataset Download
As the files are too large, we provide the following approaches to get the data:
- For international users, you can use [Google Drive](https://drive.google.com/file/d/197xROnc7lpGiJy0Y7UkQCzhesD6ZKCy-/view?usp=sharing) or [JD JoyBox-HK](https://3.cn/fCUv-kM) to download the file. Notice that JoyBox-HK requires an E-mail address to log in.

- For Chinese users, you can use [JD Joybox](http://box.jd.com/sharedInfo/E4B795CDC285F016A2FADAC4C83BA8D2) to get the file. The access password is: 39gczm

If you are facing difficulties accessing the data, feel free to contact us at the following E-mail address:
- `zrdeng@ruc.edu.cn`
- `qratosone@live.com`
- `qinxubo1@jd.com`

# Dataset Structures
The dataset includes the following 5 files:
```
data_release
  ├── dict_product_text_release.pkl.gz
  ├── product_uvctr_dict_release.pkl.gz
  ├── query_intent_label_tr.csv
  ├── query_intent_label_ts.csv
  └── query_product_features_release.pkl.gz
```
The `pkl.gz` files are compressed binary files that can be opened in Python with the `pickle` and `gzip` packages. More details can be found in `data_release/check_data.py`. All those text contents are tokenized into integer ids with a private tokenizer. The content descriptions of the files are listed as follows:
- `dict_product_text_release.pkl.gz`: the text metadata of the products. It is a Python dictionary with the following structure:
  ```
  {product_id:[title,category,brand,size,model]}
  ```
- `product_uvctr_dict_release.pkl.gz`: the popularity features of the products. It is a Python dictionary with the following structure:
  ```
  {product_id:[uv,pv,ctr]}
  ```
- `query_product_features_release.pkl.gz`: all the features of every existing query-product pair. Details about the features can be found in our paper. It is a Python dictionary with the following structure:
  ```
  {(query,product_id):[relevance_score,tf_idf_title,tf_idf_category,tf_idf_brand, bm25_title,bm25_category,bm25_brand,uv,pv,ctr]}
  ```
  Notice that the UV, PV, and CTR are identical to the features in `product_uvctr_dict_release.pkl.gz`.

The initial ranking lists with relevance scores can be generated with the `data_release/generate_initial_ranking_list.py` file.

## The Structure of Intent Annotations
- `query_intent_label_tr.csv`: the query intent annotations for the training set.
- `query_intent_label_ts.csv`: the query intent annotations for the test set. 
All those csv files are separated by `\t` in the following format:
```
query\t intent\t product_id\t label
```
Notice that we only provide the positive annotations to reduce the size of the file. Here `query` and `intent` are the tokenized integers concatenated with `,` as a separator.

# Evaluation
The diversity measures can be evaluated with the official TREC `ndeval` tool. More details can be found in [TREC official sites](https://trec.nist.gov/data/web09.html).

# The Pretrained BERT model
We provide two 12-layer BERT models with the same word tables as our private tokenizer. 

## Pretrained Model
The special token ID map of our private tokenizer is listed as follows:
```
[UNK] 1
[SEP] 3
[PAD] 0
[CLS] 2
[MASK] 4
```
We provide two BERt models to help researchers deal with the anonymized dataset.

The first model denoted as `scratch_bert` is a model pretrained on over 10M product titles:
- Download path: [Google Drive](https://drive.google.com/file/d/1Nuz5vbrFyPS7Cqu4r-4PyO4T7iYUuuHs/view?usp=sharing), [JD JoyBox-HK](https://3.cn/fDb-mx6)

It can be loaded and used with the `BertModel.from_pretrained` method of Huggingface Transformers.

The second model denoted as `rel_bert` is a fine-tuned model based on `scratch_bert`. We use the relevance model in the platform as a teacher model to distill `rel_bert` for computing the relevance between a query and a product title.
- Download path: [Google Drive](https://drive.google.com/file/d/1Yjw1wmsJ6Wul1YQbBd5aIpWyLihze55A/view?usp=sharing), [JD JoyBox-HK](https://creativecommons.org/licenses/by-nc-sa/4.0/)

We will later release more pretrained and fine-tuned model checkpoints to support the research based on JDivPS dataset.

# License
This repository is licensed under Apache-2.0 License.

The JDivPS dataset is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
