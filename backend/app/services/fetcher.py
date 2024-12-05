from abc import ABC, abstractmethod
from typing import List, Dict


class JobFetcherBase(ABC):
    """
    Abstract class for fetching data from specific API
    """
    @abstractmethod
    def fetch_jobs(self, query: str) -> List[Dict]:
        pass


class HhFetcher(JobFetcherBase):
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def fetch_jobs(self, query: str) -> List[Dict]:
        print(f"Fetching jobs from hh.ru for query: {query}")
        return [{"title": "Python Developer", "skills": ["Python", "Django"]}]


class LinkedInFetcher(JobFetcherBase):
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def fetch_jobs(self, query: str) -> List[Dict]:
        print(f"Fetching jobs from LinkedIn for query: {query}")
        return [{"title": "Backend Developer", "skills": ["FastAPI", "PostgreSQL"]}]
