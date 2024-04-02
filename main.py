from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline





STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} start <<<<<<") 
    obj=DataIngestionTraningPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
