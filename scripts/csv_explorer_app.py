""" 
  Streamlit tutorial from Youtube video: https://youtu.be/SIu2VL-RAXc for building a generic  dataset Explorer
"""
#!/usr/bin/env python

from pathlib import Path

# Viz pkgs
import matplotlib.pyplot as pyplot
import pandas as pd
import seaborn as sns
import streamlit as st

import matplotlib; matplotlib.use('Agg')

path = Path('data')

def dataset_selector(folder_path=path):
  files = {p.name: p for p in path.rglob('*.csv')}
  dataset = st.selectbox("Select dataset", list(files.keys()))
  return files[dataset]

def run():
  st.title("Generic CSV Dataset Explorer with Streamlit")  
  dataset = dataset_selector()

  df = pd.read_csv(dataset, error_bad_lines=False)

  st.subheader("Data Exploration")
  st.info(f"Dataset shape: {df.shape}")
  if st.checkbox("Show Dataset"):
    number = st.number_input("Number of rows", 1, len(df))
    st.dataframe(df.head(number))

  if st.button("Data Types"):
    st.write(df.dtypes)    

  if st.button("Columns Names"):
    st.write(df.columns)

  if st.checkbox("Select Columns to show"):
    cols = st.multiselect("Select", list(df.columns))
    st.dataframe(df[cols])

  if st.button("Value Counts"):
    st.text("Value Counts by Class")
    st.write(df.iloc[:, -1].value_counts())

  if st.checkbox("Summary"):
    st.write(df.describe().T)

  st.subheader("Data Visualization")

  plot_type = st.selectbox("Plot Type", ['area', 'bar', 'line', 'hist', 'box', 'kde'])
  selected_cols = st.multiselect("Select Columns", list(df.columns))

  if st.button(f"Generate {plot_type} plot"):
    st.success(f"Generating {plot_type} for {selected_cols}..")

    if plot_type == 'area':
      plot_df = df[selected_cols]
      st.area_chart(plot_df)
    elif plot_type == 'bar':
      plot_df = df[selected_cols]
      st.bar_chart(plot_df)
    elif plot_type == 'line':
      plot_df = df[selected_cols]
      st.line_chart(plot_df)
    elif plot_type == 'pie':
      plot_df = df[selected_cols]
      
    else:
      plot = df[cols].plot(kind=plot_type)
      st.write(plot)
      st.pyplot()

  if st.checkbox("Pie Plot"):
    st.success("Generating plot...")
    st.write(df.iloc[:, -1].value_counts().plot.pie(autopct='%1.1f%%'))
    st.pyplot()

  if st.checkbox("Correlation Plot (Seaborn)"):
    st.success("Generating plot...")
    st.write(sns.heatmap(df.corr(), annot=True))
    st.pyplot()

  if st.checkbox("Value Counts Plot"):
    groupby_cols = st.selectbox("Column to Groupby", list(df.columns))
    plot_cols = st.multiselect("Select Columns to Group", list(df.columns))
    if st.button("Generate Plot"):        
      st.success("Generating plot...")
      if plot_cols:
        plot_df = df.groupby(groupby_cols)[plot_cols].count()
      else:
        plot_df = df.iloc[:, -1].value_counts()
      st.write(plot_df.plot(kind='bar'))
      st.pyplot()

  if st.button("Thanks!"):
    st.balloons()      

if __name__ == "__main__":
  run()
