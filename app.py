import streamlit as st
from pyspark import SparkConf
from pyspark import SparkContext

st.title("BALLOONS")
conf = SparkConf().setAppName("lecture-lyon2").setMaster("local")
sc = SparkContext.getOrCreate(conf=conf)
