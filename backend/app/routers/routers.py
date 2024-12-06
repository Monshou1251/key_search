from fastapi import APIRouter
from services.fetcher import HhFetcher, LinkedInFetcher
from services.ranking import SkillRanker


router = APIRouter()

hhfetcher = HhFetcher(api_key="hh_api")
linkedinfetcher = HhFetcher(api_key="hh_api")
skill_ranker = SkillRanker()


@router.get("/jobs/hh")
def get_hh_keys(request: str):
    return {"message": "HH keys", "api_key": request}


@router.get("/jobs/linkedin")
def get_hh_keys(request: str):
    return {"message": "Linkedin keys"}
