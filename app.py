import streamlit as st
from elasticsearch import Elasticsearch
import utils, templates
import numpy as np
from fastapi import FastAPI, UploadFile, File
from PIL import Image
from typing import Optional
from VGG16 import *
import json
from keras.preprocessing import image
SOURCE_NO_VEC = ['imageId', 'title', 'author', 'tags', 'labels', 'imgUrl']
fe=FeatureExtractor("pca_512.pkl")


index='open'
es=Elasticsearch("http://localhost:9200")

def load_image_into_numpy_array(data):
    return np.array(Image.open(data))
def main():
    st.title('Search Engine In Elasticsearch')
    search_image = st.file_uploader("Upload an image",type = ["jpg","png"],help="Drag and drop your image here")
    # st.write(search_image)
    search_text = st.text_input('Enter search word:')
    if search_text:
        # st.write(es.search(index=index, query={"match":{"tags": search_text}}))
        results = utils.text_search(es, index, search_text)
        # st.write(results)
        total_hits= results['hits']['total']['value']
        duration= results['took']/1000
        st.write(templates.number_of_results(total_hits, duration), unsafe_allow_html=True)       
        for resp in results['hits']['hits']:
            url=resp['_source']['imgUrl']
            st.write(templates.search_result(url), unsafe_allow_html=True)
    elif search_image:
        
       
        x = load_image_into_numpy_array(search_image)
        
        results = utils.image_search(es, index, x)
        # st.write(results)
        total_hits= results['hits']['total']['value']
        duration= results['took']/1000
        st.write(templates.number_of_results(total_hits, duration), unsafe_allow_html=True)       
        for resp in results['hits']['hits']:
            url=resp['_source']['imgUrl']
            st.write(templates.search_result(url), unsafe_allow_html=True)
        

 


if __name__ == '__main__':
    main()