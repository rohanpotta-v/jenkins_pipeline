from app import app
#the key word of hello should be present 
def test_homepage_content_type_and_text():
    tester = app.test_client()
    response = tester.get('/')

    # Check Content-Type header
    assert response.content_type == 'text/html; charset=utf-8'

    # Check the exact text in the response body
    expected_text = "Hello"
    assert expected_text in response.get_data(as_text=True)