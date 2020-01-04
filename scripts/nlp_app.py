#!/usr/bin/env python

import streamlit as st

from ttictoc import TicToc
import spacy

@st.cache(allow_output_mutation=True)
def load_spacy(model='en_core_web_sm'):
  nlp = spacy.load(model)
  return nlp

def text_analyzer(sp_model, text):
  doc = sp_model(text)
  return [(f"Token: {token.text}, Lemma: {token.lemma_}") for token in doc]

def run():
  st.title("Basic NLP App with Streamlit")
  nlp = load_spacy()
  
  if st.checkbox("Show Tokens and Lemma"):
    text = st.text_area("Enter Your Text", "Type Here")
    if st.button("Analyze"):
      st.json(text_analyzer(nlp, text))

if __name__ == "__main__":
  run()
