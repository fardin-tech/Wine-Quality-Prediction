from mlproject.config.configuration import ConfigurationManger
from mlproject.components.data_validation import DataValidation
from mlproject import logger

STAGE_NAME="Data Validation stage"



class DataValidationTraningPipeline:
    def __init__(self):
        pass
    def main(self):
        
        config=ConfigurationManger()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} start <<<<<<")
        obj=DataValidationTraningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
                            