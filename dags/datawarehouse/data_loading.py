import json
from datetime import date
import logging
#from pathlib import Path

logger = logging.getLogger(__name__)

""" def load_data():

    folder = Path("./data")

    try:
        latest_file = max(
            folder.glob("YT_data_*.json"),
            key=lambda x: x.stat().st_mtime
        )

        logger.info(f"Processing file: {latest_file.name}")

        with open(latest_file, "r", encoding="utf-8") as raw_data:
            data = json.load(raw_data)

        return data

    except ValueError:

        logger.error("No JSON files found in ./data")

        raise

    except FileNotFoundError:

        logger.error(f"File not found: {latest_file}")

        raise

    except json.JSONDecodeError:

        logger.error(f"Invalid JSON in file: {latest_file}")

        raise
 """


def load_data():

    file_path = f"./data/YT_data_{date.today()}.json"

    try:
        logger.info(f"Processing file : YT_data_{date.today()}")

        with open(file_path, "r", encoding = "utf-8") as raw_data :
            data = json.load(raw_data)

        return data

    except FileNotFoundError:

        logger.error(f"File not found:{file_path}")

        raise

    except json.JSONDecodeError:

        logger.error(f"Invalid JSON in file: {file_path}")

        raise

