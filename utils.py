
from typing import Optional
from VGG16 import *
import numpy as np

fe=FeatureExtractor("pca_512.pkl")

def text_search(es, index: str, keywords: str) -> dict:
    res=es.search(index=index, query={"match":{"title":keywords}})
   
    return res


# def img_search(es, index: str, image: np.array= None ) -> dict:
#     features = fe.get_from_image(image)
#     query = {
#                 "elastiknn_nearest_neighbors": {
#                 "vec": {
#                     "values": features
#                 },
#                 "field": "featureVec",
#                 "model": "lsh",
#                 "similarity": "l2",
#                 "candidates": 10
#                 }
#             }
        
#     res=es.search(index=index, query=query, size=5, _source=['imageId', 'title', 'author', 'tags', 'labels', 'imgUrl'])
    
def image_search(es, index, image):
    features=fe.get_from_image(image)
    query = {
                "elastiknn_nearest_neighbors": {
                "vec": {
                    "values": features
                },
                "field": "featureVec",
                "model": "lsh",
                "similarity": "l2",
                "candidates": 50,
                "probes": 2
                }
            }
    
    return es.search(index=index, query=query, _source=['imageId', 'title', 'author', 'tags', 'labels', 'imgUrl'])


