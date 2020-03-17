import logging
import os
import pathlib


log_name = "myapp"

project_dir = pathlib.Path(__file__).parent.parent.absolute()

logdir = f"{str(project_dir)}/logs"
log_file = f"{logdir}/{log_name}.log"

if not os.path.exists(logdir) or not os.path.isdir(logdir):
    os.makedirs(logdir)

logger = logging.getLogger("flask")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename=log_file)

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    fmt="%(module)s :: %(levelname)s @ [%(asctime)s] %(message)s", datefmt="%d-%m-%Y / %H:%M:%S"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
