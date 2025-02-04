#Try all the algs and find the best out of them
import sys
import os
from dataclasses import dataclass
#from catboost import CatBoostRegressor
from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test data")
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],#All columns except the last column
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]                          
            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "XGBRegressor": XGBRegressor(), 
                #"CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor()
            }
            model_report:dict = evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                               models=models)#Return value is a dict called model_report
            
            #To get the best score
            best_model_score = max(sorted(model_report.values()))

            #To get best model name from the dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)]
            
            best_model = models[best_model_name]

            if  best_model_score<0.6:   #Setting up a threshold
                raise CustomException("No best model found!")
            
            logging.info("Best model for training and test datasets found.")

            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model #creates a pickle file for the model
            )

            #Print best score
            predicted = best_model.predict(X_test)
            r2 = r2_score(y_test,predicted)
            return r2

        except Exception as e:
            raise CustomException(e,sys)


