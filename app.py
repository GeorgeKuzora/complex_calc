import logging


logging.basicConfig(
    level=logging.WARNING,
    filename="app.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
