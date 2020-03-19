import logging
import os
import pathlib


def make_logger(tag: str):
    project_dir = pathlib.Path(__file__).parent.parent.absolute()

    log_dir = f"{str(project_dir)}/logs"
    log_file = f"{log_dir}/{tag}.log"

    if not os.path.exists(log_dir) or not os.path.isdir(log_dir):
        os.makedirs(log_dir)

    logger_inst = logging.getLogger("flask")
    logger_inst.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename=log_file)

    logger_inst.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(module)s :: %(levelname)s @ [%(asctime)s] %(message)s", datefmt="%d-%m-%Y / %H:%M:%S"
    )

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger_inst.addHandler(console_handler)
    logger_inst.addHandler(file_handler)

    return logger_inst


logger = make_logger("myapp")
