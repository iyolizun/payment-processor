import logging
from payment_processor.config import Config
from payment_processor.database import Database
from payment_processor.processor import ProcessPayment

def main():
    try:
        logging.basicConfig(level=logging.INFO)
        config = Config()
        database = Database(config.database_url)
        processor = ProcessPayment(config, database)
        processor.process_transactions()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()