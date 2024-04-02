from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline
from mlproject.pipeline.stage_02_data_valiadtion import DataValidationTraningPipeline





STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} start <<<<<<") 
    data_ingestion=DataIngestionTraningPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} start <<<<<<") 
    data_validation=DataValidationTraningPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
