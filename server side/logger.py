import logging

def setup_loggers(name='mediacalassistance'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] --- [%(message)s]")
    ch.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(ch)

    return logger

logger = setup_loggers()
logger.info('RAG process started')