# JDivPS
JDivPS: A Diversified Product Search Dataset
# Dataset Download
As the files are too large, we provide the following approaches to get the data:
- For international users, you can use [Google Drive](https://drive.google.com/file/d/197xROnc7lpGiJy0Y7UkQCzhesD6ZKCy-/view?usp=drive_link) or [JD JoyBox-HK](https://3.cn/fD-hnri) to download the file. Notice that JoyBox-HK requires an E-mail address to log in.

- For Chinese users, you can use [JD Joybox](http://box.jd.com/sharedInfo/BD2678873AB6F8916DFB90EA73EA2603) to get the file. The access password is lfe39l. You need an account on [JD.com](https://www.jd.com/) to access the data.

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
  ├── query_suggestions_release.pkl.gz
  └── query_product_features_release.pkl.gz
```
The `pkl.gz` files are compressed binary files that can be opened in Python with the `pickle` and `gzip` packages. More details can be found in `data_release/check_data.py`. All those text contents are tokenized into integer ids with a private tokenizer. The content descriptions of the files are listed as follows:
- `dict_product_text_release.pkl.gz`: the text metadata of the products. It is a Python dictionary with the following structure:
  ```
  {product_id:[product_name,category_name,brand_name,size,attribute,color]}
  ```
  | Attribute | Description |
  |-------|-------|
  | product_id | the product’s anonymized id |
  | product_name | the product's anonymized term ids |
  | category_name | the product category's anonymized term ids |
  | brand_name | the product brand's anonymized term ids |
  | size | the product size's anonymized term ids |
  | attribute | the product attribute's anonymized term ids |
  | color | the product color's anonymized term ids |
It should be addressed that the `size`, `attribute` and `color` of the product may be empty.
- `query_suggestions_release.pkl.gz`: the query suggestions corresponding to the query. It is a Python dictionary with the following structure:
  ```
  {query:[suggestions1, suggestions2, ...]}
  ```
- `product_uvctr_dict_release.pkl.gz`: the popularity features of the products. It is a Python dictionary with the following structure:
  ```
  {product_id:[uv,pv,ctr]}
  ```
  | Attribute | Description |
  |-------|-------|
  | product_id | the product’s anonymized id |
  | uv, pv, ctr | UV, PV, and CTR score of the product |
- `query_product_features_release.pkl.gz`: all the features of every existing query-product pair. Details about the features can be found in our paper. It is a Python dictionary with the following structure:
  ```
  {(query,product_id):[relevance_score,tf_idf_title,tf_idf_category,tf_idf_brand, bm25_title,bm25_category,bm25_brand,uv,pv,ctr]}
  ```
  | Attribute | Description |
  |-------|-------|
  | query | the query's anonymized term ids |
  | product_id | the product’s anonymized id |
  | relevance_score | relevance of the product to the query |
  | tf_idf_title | tf-idf score of the product's title |
  | tf_idf_category | tf-idf score of the product's category |
  | tf_idf_brand | tf-idf score of the product's brand |
  | bm25_title | BM25 score of the product's title |
  | bm25_category | BM25 score of the product's category |
  | bm25_brand | BM25 score of the product's brand |
  | uv,pv,ctr | UV, PV, and CTR score of the product |
  
  Notice that the UV, PV, and CTR are identical to the features in `product_uvctr_dict_release.pkl.gz`.

The initial ranking lists with relevance scores can be generated with the `data_release/generate_initial_ranking_list.py` file.

## The Structure of Intent Annotations
- `query_intent_label_tr.csv`: the query intent annotations for the training set.
- `query_intent_label_ts.csv`: the query intent annotations for the test set. 
All those csv files are separated by `\t` in the following format:
```
query\t intent\t product_id\t label
```
  | Attribute | Description |
  |-------|-------|
  | query | the query's anonymized term ids |
  | intent| the anonymized term ids of a user intent |
  | product_id | anonymized product_id of a product in the initial product list |
  | relation (0/1) | relevance of a product to the intent |

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
We provide a BERT model denoted as `scratch_bert` which is pretrained on over 10M product titles with the task of Masked Language Model(MLM):
- Download path: [Google Drive](https://drive.google.com/file/d/1Nuz5vbrFyPS7Cqu4r-4PyO4T7iYUuuHs/view?usp=sharing), [JD JoyBox-HK](https://3.cn/fDb-mx6), [JD JoyBox](http://box.jd.com/sharedInfo/0796DE3320DCE6FAAB6285AC6DB1AE3D)   password: yrh7z5

It can be loaded and used with the `BertModel.from_pretrained` method of Huggingface Transformers.

## Fine-tuned Model
Based on `scratch_bert`, we provide another model denoted as `rel_bert` for computing the relevance between queries and product titles. We use the relevance model in the platform as a teacher model to distill `rel_bert` for computing the relevance between a query and a product title.
- Download path: [Google Drive](https://drive.google.com/file/d/1Yjw1wmsJ6Wul1YQbBd5aIpWyLihze55A/view?usp=sharing), [JD JoyBox-HK](https://creativecommons.org/licenses/by-nc-sa/4.0/), [JD JoyBox](http://box.jd.com/sharedInfo/52FD2E44BC3E9E0EAB6285AC6DB1AE3D)  password: ud9oeq

More details can be found in `load_relevance_model.py` for the instructions for loading the relevance model checkpoint.

We will later release more pretrained and fine-tuned model checkpoints to support the research based on JDivPS dataset.

# License
This repository is licensed under Apache-2.0 License.

The JDivPS dataset is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
