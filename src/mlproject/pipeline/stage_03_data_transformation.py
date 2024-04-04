from mlproject.config.configuration import ConfigurationManger
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger
from pathlib import Path




STAGE_NAME="Data Transfomation stage"
class DataTransfomationTraningPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status=f.read().split(" ")[-1]

            if status=="True":
                config=ConfigurationManger()
                get_data_transformation=config.get_data_transformation()
                data_transformation=DataTransformation(config=get_data_transformation)
                data_transformation.train_test_spliting()
            
            else:
                raise Exception("You data schema is not valid")
            
        except Exception as e:
            print(e)
