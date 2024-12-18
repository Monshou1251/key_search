from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch, Mock


client = TestClient(app)


class TestHhEndpoint:
    """
    Test for endpoint /hh
    """

    def test_hh_is_reachable(self):
        response = client.get("/hh?text=python")
        
        assert response.status_code == 200
       
        
    def test_hh_bad_format(self):
        response = client.get("/hh?text=python")
        
        json_response = response.json()
        assert isinstance(json_response, dict)
        assert "items" in json_response
    
    
    def test_hh_missing_query(self):
        response = client.get("/hh")
        assert response.status_code == 422
        
        
    def test_hh_bad_query_format(self):
        response = client.get("/hh?text=123")
        assert response.status_code == 200
        
    
    def test_hh_mocked_api_call(self, mocker):
        mock_response = {
            "items": [
                {"name": "Python Developer", "key_skills": [{"name": "Python"}, {"name": "Django"}]},
                {"name": "Backend Developer", "key_skills": [{"name": "FastAPI"}, {"name": "REST"}]},
            ]
        }
        mocker.patch(
            "requests.get",
            return_value=Mock(status_code=200, json=lambda: mock_response)
        )

        
        
    
    