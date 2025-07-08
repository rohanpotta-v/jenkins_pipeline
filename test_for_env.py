from app import app
#The enviournment name should be present 
def test_homepage_status_and_content():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"production" in response.data
