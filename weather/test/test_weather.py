import app
def test_get_weather_witout_api_key(monkeypatch, capsys): # Pytest fixture that lest you temporarily modify/modify-replace
     #remove API KEY                                      # object env,function,etc,during test = monkeypatch
    monkeypatch.setattr(app,"API_KEY", None)              # pytest  fixture that capture anything printed to stdout and
    # call function                                       # stderr so yoy can asser against the output
    app.get_weather("London")
    captured = capsys.readouterr()                       # print usefull massage
    assert "API key not found" in captured.out



def test_get_weather_suceess(monkeypatch, capsys):
    # 1. creatre fake API data
    fake_data = {
        "name":"London",
        "main": {
            "temp":25,
            "humidity": 60
        },
        "weather":[
            {"description": "clear sky"}
        ]
    }

# Create fack responce use gat face data

    class FakeResponse:
        def raise_for_status(self):
            pass # Do nothing = preted evrything is ok

        def json(self):
            return fake_data 

# Create fake API request
    def fake_get(*args, **kwargs):
        return FakeResponse()

# Replace real API settings
    monkeypatch.setattr(app, "API_KEY", "fake_api_key")
    monkeypatch.setattr(app, "BASE_URL", "https://fake-api.com")
    monkeypatch.setattr(app.requests, "get", fake_get)

# call function
    app.get_weather("London")

# Capture output
    captured = capsys.readouterr()

 # 7. Check expected results
    assert "London" in captured.out
    assert "25°C" in captured.out
    assert "clear sky" in captured.out
    assert "60%" in captured.out
