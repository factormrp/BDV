from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
import utils.preprocess as prep
from utils.load import load
import asyncio
import logging
import os

router = APIRouter()
logger = logging.getLogger(__name__)
templates = Jinja2Templates(directory=os.environ["TEMPLATE_DIR"])

@router.get("/data")
def get_basic_data():
    try:
        data = load(os.environ["DATA_PATH"])
        return prep.get_series_data(data)
    except ValueError as v:
        raise HTTPException(status_code=404,
            detail="Failed to serve data resource"
        )


@router.get("/",response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse(os.environ["ROOT_TEMPLATE"],{
        "request":request,
        "prompt":"What data would you like today?",
        "list":categories
    })

@router.post("/series", response_class=HTMLResponse)
def list_category_sub_series(request: Request, category: str = Form(...)):
    return templates.TemplateResponse(os.environ["LIST_TEMPLATE"],{
        "request":request,
        "prompt":"Which series?",
        "list":prep.filter_by_category(series_data,category)
    })

@router.post("/detail", response_class=HTMLResponse)
def retrieve_sub_series_detail(request: Request, id: str = Form(...)):

    return templates.TemplateResponse(os.environ["DETAIL_TEMPLATE"],{
        "request":request,
        "prompt":f"Here's your data!",
        "plot":fstring
    })

if __name__ == "__main__":
    data = load(os.environ["DATA_PATH"])
    prep.get_series_data(data)

    e = asyncio.run(l)

    print(e)
#    print(f"Categories: {c}")
#    print(f"Length of Series: {len(s)}")
