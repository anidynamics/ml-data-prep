# ml-data-prep
A collection of scripts for machine learning data set preparation

## create-dataframe
Code to create a Pandas DataFrame from a folder where the subfolders should be the labels for the conatining images.  
For example, you want a DataFrame from folders with labels "Cat" and "Dog"  
<a href="url"><img src="https://user-images.githubusercontent.com/5400969/114323308-d800ef80-9b24-11eb-9efd-563bdab2dc50.png" width="400"></a>


### Usage
First, install required python packages from requirements.txt
```
pip install -r requirements.txt
```

Create a Pandas Dataframe from a given folder
```
python ml-data-prep/create-dataframe.py -p /Path/to/Data
```
named df.csv in the folder /Path/to/Data.
