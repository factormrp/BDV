from fastapi.staticfiles import StaticFiles
from logging.config import fileConfig
from fastapi import FastAPI
from router import router
import logging

fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
app.include_router(router)
