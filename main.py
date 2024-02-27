from classifier import logger
from classifier.pipeline.stage_01 import DataIngestionTrainPipeline
from classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME="Data Ingestion_stage"


try:
    logger.info(f">>>>>stage{STAGE_NAME} started<<<<<")
    obj=DataIngestionTrainPipeline()
    obj.main()
    logger.info(f">>>>>>>>stage {STAGE_NAME}completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
