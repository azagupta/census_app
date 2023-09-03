# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_app.py'.

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame using the list given above.

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()


st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)



# Load the data
@st.cache()
def load_data():
    df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
    # Rename columns, remove invalid values, and drop unnecessary column
    # (You can reuse the data loading and preprocessing code you provided)
    return df

census_df = load_data()

# Set page title
st.title("Census Data Analysis")

# Sidebar title
st.sidebar.title("Census Data Analysis")

# Checkbox to show raw data
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Census Data")
    st.dataframe(census_df)

# Multiselect widget for selecting visualizations
st.sidebar.subheader("Visualization Selector")
plot_list = st.sidebar.multiselect(
    "Select the Charts/Plots:",
    ('Pie Chart', 'Box Plot', 'Count Plot')
)

# Display selected visualizations
if 'Pie Chart' in plot_list:
    st.subheader("Pie Chart")
    # Create a simple pie chart
    data_count = census_df['income'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(data_count, labels=data_count.index, autopct='%1.1f%%')
    st.pyplot()

if 'Box Plot' in plot_list:
    st.subheader("Box Plot")
    # Create a box plot
    sns.boxplot(data=census_df, x='income', y='age')
    st.pyplot()

if 'Count Plot' in plot_list:
    st.subheader("Count Plot")
    # Create a count plot
    sns.countplot(data=census_df, x='education', hue='income')
    st.pyplot()
