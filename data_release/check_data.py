import os
import pickle,gzip
import pandas as pd
import random
def read_dict(path):
    with gzip.open(path,'rb') as f:
        dict_in=pickle.load(f)
    return dict_in
def get_random_key_from_dict(dict_in):
    keys=list(dict_in.keys())
    random.shuffle(keys)
    return keys[0]
if __name__=="__main__":
    dict_product_text=read_dict("dict_product_text_release.pkl.gz")
    product_key=get_random_key_from_dict(dict_product_text)
    print(dict_product_text[product_key])
    #data structure of dict_product_title:
    # {product_id:[title,category,brand,size,model]}
    # all the metadata texts are tokenized integers
    dict_query_product_features=read_dict("query_product_features_release.pkl.gz")
    pair_key=get_random_key_from_dict(dict_query_product_features)
    # data structure of dict_query_product_features:
    # {(query,product_id):[relevance_score,tf_idf_title,tf_idf_category,tf_idf_brand,\
    #                     bm25_title,bm25_category,bm25_brand,uv,pv,ctr]}
    #Notice that the key of the dict is a tuple (query,product_id)
    print(dict_query_product_features[pair_key])
    dict_product_uvctr = read_dict("product_uvctr_dict_release.pkl.gz")
    print(dict_product_uvctr[pair_key[1]])
    # data structure of dict_product_uvctr:
    # {product_id:[uv,pv,ctr]}
