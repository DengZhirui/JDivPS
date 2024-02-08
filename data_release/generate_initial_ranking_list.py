from check_data import read_dict
import pandas as pd
import json
#Assuming that the data file is in the same folder of this script.
DATA_PATH="query_product_features_release.pkl"

if __name__=="__main__":
    query_product_features_dict=read_dict(DATA_PATH)
    relevance_score_pairs=[]
    for key in query_product_features_dict:
        features=query_product_features_dict[key]
        relevance_score=features[0]
        relevance_score_pairs.append(key,relevance_score)
    #generate index for every query
    qid_dict={}
    qid_rankings={}
    for item in relevance_score_pairs:
        query,product_id=item[0]
        relevance_score=item[1]
        if query not in qid_dict:
            query_index=len(qid_dict)+1
            qid_dict[query]=query_index
        qid=qid_dict[query]
        if qid not in qid_rankings:
            qid_rankings[qid]=[]
        qid_rankings[qid].append([product_id,relevance_score])
    ranking_lists_flatten=[]
    for qid in qid_rankings:
        qid_rankings[qid]=sorted(qid_rankings[qid],key=lambda x:x[1],reverse=True)
        ranking_lists_flatten+=[[qid]+item for item in qid_rankings[qid]]
    #write the initial ranking lists into a csv file
    pd.DataFrame(ranking_lists_flatten,columns=["qid","product_id","score"]).to_csv("initial_ranking_relevance.csv",index=False)
    #save the query-qid mapping dict if necessary
    with open("query_qid_map.json",'w',encoding='utf-8') as f:
        json.dump(qid_dict,f)
