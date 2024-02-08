# JDivPS

# Dataset Download
As the files are too large, we provide those following approaches to get the data:
- For international users, you can use [Google Drive](https://drive.google.com/file/d/197xROnc7lpGiJy0Y7UkQCzhesD6ZKCy-/view?usp=sharing) or [JoyBox-HK](https://3.cn/fCUv-kM) to download the file. Notice that JoyBox-HK requires an E-mail address to login.

- For Chinese users, you can use [JD Joybox](http://box.jd.com/sharedInfo/E4B795CDC285F016A2FADAC4C83BA8D2) to get the file. The access password is: 39gczm

# Dataset Structures
The dataset includes those following 5 files:
```
data_release
  ├── check_data.py
  ├── dict_product_text_release.pkl.gz
  ├── product_uvctr_dict_release.pkl.gz
  ├── query_intent_label_tr.csv
  ├── query_intent_label_ts.csv
  └── query_product_features_release.pkl.gz
```
The `pkl.gz` files are compressed binary files that can be opened with the `pickle` and `gzip` packages in Python. More details can be found in `check_data.py`. All those text contents are tokenized into integer ids with a private tokenizer. The content descriptions of the files are listed as follows:
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
  Notice that the UV, PV and CTR are identical to the features in `product_uvctr_dict_release.pkl.gz`.
