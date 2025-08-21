# Using-KNN-to-predict-the-OBP-of-MLB-players
I used a prebuilt KNN model to predict the On Base Percentage (OBP) of Major League Baseball (MLB) players at the end of the season given their stats in the beginning of the same season

## Project overview: 
Part 1 (analysis found in the Jupyter notebook file): learning, discovering, and evaluating KNN<br/>Part 2 (app found in the folder): integrating the optimal KNN model into a small GUI for simple use

- Goal: Predict a player's end-of-season OBP using early season stats with supervised learning.
- Method: K-Nearest Neighbors regression
- Data: 2023 MLB player stats from Baseball-Reference.
- Output: Predicted OBP values and the MSE values.

## MLB features used:
- AVG, SLG, R were used to begin with
- It was later determined in the discovery that R was not much of a contributing factor, and thus removed.

## Evaluation:
- Metrics: MSE
- Elbow method: used to find the most optimal `K` value in order to implement KNN

## Key insights:
- KNN performs really well on OBP prediction with the right feature normalization.
- Early-season stats provide strong signals for end-of-season OBP.
- Feature scaling is crucial due to the curse of dimensionality from using KNN.
- All the plots and diagrams can be find in the Jupyter notebook file.

## Extension:
- Later implemented cross validation to find the optimal value of 'K' again.
- Compared cross validation with the elbow method using MSE.
- Built a linear regression model from scratch to learn different machine learning algorithms.
- Compared the linear regression method to the prebuilt KNN model and plotted the decision plane of the linear regression model.

## Key insights from extension:
- Cross validation works better than the elbow method as it is systematic while the elbow method is mainly based on human intuition to choose where the shifting point in the graph is, making cross validation the better method to find the optimal value of K.
- Machine learning models are heavily based on mathematical models as I learned how to build a linear regression model from scratch.
- The comparison between linear regression and KNN wasnt clear as the KNN model was prebuilt and has optimized hyperparameters.
- It isnt so difficult to build machine learning models from scratch

## Repo guide:
Clone the repo: `git clone https://github.com/rixiiz/Using-KNN-to-predict-the-OBP-of-MLB-players.git` then `cd Using-KNN-to-predict-the-OBP-of-MLB-players`

For the analysis:
1. Install dependencies: `pip install -r requirements.txt`
2. Open Jupyter notebook: `jupyter notebook`
3. Click on the notebook file and run the cells

For the app:
0. Read the information file
1. cd `OBP_Predictor_App`
2. Install dependencies: `pip install -r apprequirements.txt`
3. Run the app: `python app.py`
