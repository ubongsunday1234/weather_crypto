import logging
import os
from pathlib import Path
from logging.handlers import RotatingFileHandler

#create path for logs
try:
    file_=Path(__file__).resolve()
    root=file_.parent.parent.parent
    log_file_=next(root.rglob("logs"))
except:
    file_=Path(__file__).resolve()
    root=file_.parent.parent.parent
    log_file1=next(root.rglob("weather_crypto"))
    log_=os.path.join(log_file1, "logs")
    os.makedirs(log_, exist_ok=True)

#create a custom log_program crypto_weather
log_program=logging.getLogger("crypto_weather")
log_program.setLevel(logging.DEBUG)

#FORMAT:TIME, FILENAME, LEVEL, MESSAGE
formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#file handler, saves to file and rotates logs after size surpasses 2mb
file_=Path(__file__).resolve()
root=file_.parent.parent.parent
log_file_=next(root.rglob("logs"))
log_=os.path.join(log_file_, "app.log")
file_handler=RotatingFileHandler(log_, maxBytes=2_000_000,backupCount=5)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

#console handler, this prints to terminal
console_handler=logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)

#Avoid duplicate logs if re-imported
if not log_program.handlers:
    log_program.addHandler(file_handler)
    log_program.addHandler(console_handler)

