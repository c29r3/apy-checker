import logging

def setup_logging(log_file='bot.log', log_level='INFO'):
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, 'a'),
            logging.StreamHandler()
        ]
    )
