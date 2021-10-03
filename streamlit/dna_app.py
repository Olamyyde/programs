import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image


image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
"""
)

st.header('Enter DNA sequence')


sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("sequence_input", sequence_input, height = 250)
sequence = sequence.splitlines()
sequence = sequence[1:]  # skips the sequence name(first line)
sequence = ''.join(sequence) # concatenates list to string

st.write("""
***
""")

# Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

## DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

## Print dictionary
st.subheader('1. Print dictionary')

def DNA_nucleotide_count(seq):
	d = dict([
			  ('A', seq.count('A')),
			  ('T', seq.count('T')),
			  ('G', seq.count('G')),
			  ('C', seq.count('C'))

			  ])
	return d

X = DNA_nucleotide_count(sequence)