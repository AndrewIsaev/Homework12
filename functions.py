import logging

loger = logging.getLogger("project_loger")
loger.setLevel(logging.INFO)
loger_handler = logging.FileHandler("log.log")
loger_formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
loger_handler.setFormatter(loger_formatter)
loger.addHandler(loger_handler)
