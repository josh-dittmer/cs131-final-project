# CS131 Final Project

## Initial Setup

1. Download the dataset from https://archive.ics.uci.edu/dataset/186/wine+quality

2. Create a folder called **data/** at the project's root

3. Extract the archive and move the files **winequality-red.csv** and **winequality-white.csv** to **data/**

4. Run the following commands to process the data:
```
chmod +x process_data.sh
./process_data
```

## Train Models

1. To train the models, run the following commands:
```
pip install -r requirements.txt
python main.py
```