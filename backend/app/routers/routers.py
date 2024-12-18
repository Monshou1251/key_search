from fastapi import APIRouter, Query, HTTPException
from services.fetcher import HhFetcher, LinkedInFetcher
from services.ranking import SkillRanker
import requests


router = APIRouter()

hhfetcher = HhFetcher(api_key="hh_api")
linkedinfetcher = HhFetcher(api_key="hh_api")
skill_ranker = SkillRanker()


@router.get("/hh")
def get_hh_keys(text: str):
    """
    Fetch data from hh.ru with the provided 'text' argument.
    """
    url = "https://api.hh.ru/vacancies"
    params = {"text": text, "per_page": 10}
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Failed to fetch data from hh.ru: {e}")
    
    return response.json()


@router.get("/jobs/linkedin")
def get_hh_keys(request: str):
    return {"message": "Linkedin keys"}
