import logging


def setup_logger(log_file):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(filename)s | %(lineno)d | %(levelname)s |: %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
