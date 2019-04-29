# Stock Market Price prediction using LSTM

This project considers the historical stock prices of a company for past 5 years and are used to predict the price trend of the coming 30 days.

## Project Description

This project has two files:  
  1. **lstm.py**:
    This file consists of all the helper functions. It is mainly used for Data Preprocessing to prepare the data using Rolling Window       Method on Closing Price of a company's historical stock price.
  2. **model.ipynb**:
    This file consists of the main model and the flow of the whole project starting from calling data preprocessing modules from lstm.py     file, LSTM Model Architecture, Testing and Plotting the results.

This project consists of several modules:

- **Rolling Window**:  
  Closing price of the company's 5 years stock prices are considered along with a sequence length to be considered.   
  ```
  For eg.:
  Let data be: [2, 4, 6, 4, 8]
  and sequence length be: 3
  On the first iteration:
    Input window: [2, 4, 6]
  Output: [(2/2)-1, (4/2)-1, (6/2)-1] i.e. (window[i]/window[0])-1
  On the second iteration:
    Input window: [4, 6, 4]
    Output: [(4/4)-1, (4/2)-1, (6/2)-1] i.e. (window[i]/window[0])-1
  And so on...
  Final Data:
  [[0, 1, 2],
  [0, 1, 2],
  [0, -0.33, 0.33]]
  ```
  The last value of a row is considered as label and all the other values are features.  
  Using the Rolling Window method using the Closing Prices, a dataset is created for Model Training.  
   
- **Model Training**:  
  LSTM (Long Short Term Memory Cells) is used to predict the sequence of closing price. Model Architecture is discussed below.  
  
## Prerequisites
  
  - Keras (For Modelling)
  - Pandas (Dataframe Operations)
  - Numpy (Mathematical Operations)
  - Matplotlib (For Plotting)
  
## Model Architecture

  ![Flow Chart](https://raw.githubusercontent.com/kritipawar/Stock-Market-Price-prediction-Trading-Bot-/master/flow.jpg)
  
## Authors/Developers
For a coffee over code contact: 
Name: Kriti Pawar  
Email: kritipawar03@gmail.com   
