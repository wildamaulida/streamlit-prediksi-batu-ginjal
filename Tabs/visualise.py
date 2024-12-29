import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import tree
import streamlit as st

from web_functions import train_model

def app(df, x, y):
    warnings.filterwarnings('ignore')  # Mengabaikan peringatan
    
    st.title("Visualisasi Prediksi Batu Ginjal")
    
    # Plot Confusion Matrix
    if st.checkbox("Plot Confusion Matrix"):
        model, score = train_model(x, y)
        
        # Create figure and axis objects
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot confusion matrix
        ConfusionMatrixDisplay.from_estimator(
            model,
            x,
            y.values.ravel(),
            display_labels=['notckd', 'ckd'],
            cmap='Blues',
            ax=ax  # Specify axis for plotting
        )
        
        st.pyplot(fig)  # Display the figure

    # Plot Decision Tree
    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(x, y)
        
        dot_data = tree.export_graphviz(
            decision_tree=model, 
            max_depth=3, 
            out_file=None, 
            filled=True, 
            rounded=True,
            feature_names=x.columns, 
            class_names=['notckd', 'ckd']
        )
        
        st.graphviz_chart(dot_data)  #