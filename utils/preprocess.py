from models.series import Series
from typing import List, Tuple
from datetime import date
from time import strptime
import logging
import asyncio
import sys

logger = logging.getLogger(__name__)

async def get_series_list(series: List[List[str]]) -> List[Series]:
    try:
        return [Series(category=l[0],name=l[1],id=l[2]) for l in series]
    except IndexError as i:
        logger.error("Failed to parse series list due to indexing error!")
        raise i

async def get_categories(series: List[List[str]]) -> List[str]:
    try:
        c = []
        for l in series:
            if l[0] not in c:
                c.append(l[0])
        return sorted(c)
    except IndexError as i:
        logger.error("Failed to parse categories due to indexing error!")
        raise i

async def get_series_data(series: List[List[str]]) -> List[str]:
    try:
        await asyncio.gather(
            get_series_list(series),
            get_categories(series)
        )
    except IndexError as i:
        logger.error("Failed to get series data")
        raise i

def filter_by_category(series: List[Series], category: str) -> List[Series]:
    return [s for s in series if s.category == category]

def filter_by_name(series: List[Series], string: str) -> List[Series]:
    return [s for s in series if string in s.name]

def clean_series_response(data: dict) -> Tuple[List[float],List[date]]:
    data_list = data["Results"]["series"][0]["data"]
    vals,dates = [],[]
    for dct in data_list:
        dt = strptime(f"{dct['year']}-{dct['period']}","%Y-M%m")
        dt = date(dt.tm_year,dt.tm_mon,dt.tm_mday)
        vals.insert(0,float(dct["value"]))
        dates.insert(0,dt)
    return vals,dates
