# KNN-model-to-predict-the-OBP-of-MLB-players
A machine learning model I built that can predict the On Base Percentage (OBP) of Major League Baseball (MLB) players at the end of the season
This model leverages statistics from early season to estimate final OBP values

## Project Overview: 
- Goal: Predict a player's end-of-season OBP using early season stats with supervised learning.
- Method: K-Nearest Neighbors regression.
- Data: 2023 MLB player stats from Baseball-Reference.
- Output: Predicted OBP values and the MSE values.

## Features used:
AVG, SLG, R to begin with. It was later determined that R was not much of a contributing factor, and thus removed.

## Evaluation:
- Metrics: MSE
- Elbow method: used to find the most optimal `K` value

## Key Insights:
- KNN performs really well on OBP prediction with the right feature normalization.
- Early-season stats provide strong signals for end-of-season OBP.
- Feature scaling is crucial due to the curse of dimensionality from using KNN.

## TODO:
- Build an interface and I can input the stats of a player to get the end season OBP
- Compare KNN regression with other models such as Linear Regression or Random Forest

## How to run:
1. clone the repo: `git clone https://github.com/rixiiz/KNN-model-to-predict-the-OBP-of-MLB-players.git`   `cd KNN-model-to-predict-the-OBP-of-MLB-players`
2. install dependencies: `pip install -r requirements.txt`
3. Run the pipeline: `python main.py`

## Contributing:
Contributions are welcome! Feel free to open issues or submit PRs.
