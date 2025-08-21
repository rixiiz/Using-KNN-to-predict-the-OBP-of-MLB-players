# Using-KNN-to-predict-the-OBP-of-MLB-players
I used a prebuilt KNN model to predict the On Base Percentage (OBP) of Major League Baseball (MLB) players at the end of the season given their stats in the beginning of the same season

## Project Overview: 
- Goal: Predict a player's end-of-season OBP using early season stats with supervised learning.
- Method: K-Nearest Neighbors regression.
- Data: 2023 MLB player stats from Baseball-Reference.
- Output: Predicted OBP values and the MSE values.

## MLB features used:
AVG, SLG, R to begin with. It was later determined in the discovery that R was not much of a contributing factor, and thus removed.

## Evaluation:
- Metrics: MSE
- Elbow method: used to find the most optimal `K` value in order to implement KNN

## Key Insights:
- KNN performs really well on OBP prediction with the right feature normalization.
- Early-season stats provide strong signals for end-of-season OBP.
- Feature scaling is crucial due to the curse of dimensionality from using KNN.
- All the plots and diagrams can be find in the Jupyter notebook file

## How to run:
1. clone the repo: `git clone https://github.com/rixiiz/KNN-model-to-predict-the-OBP-of-MLB-players.git`   `cd KNN-model-to-predict-the-OBP-of-MLB-players`
2. install dependencies: `pip install -r requirements.txt`
3. Run the pipeline: `python main.py`
