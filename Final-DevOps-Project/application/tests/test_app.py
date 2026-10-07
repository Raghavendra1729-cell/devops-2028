import secrets
import pytest
from app import app, calculate

@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv("API_TOKEN", secrets.token_hex(16))
    return app.test_client()

@pytest.mark.parametrize("a,b,operation,result", [(2,3,"add",5), (3,5,"subtract",-2), (-2,4,"multiply",-8), (7,2,"divide",3.5)])
def test_calculator_operations(a,b,operation,result):
    assert calculate(a,b,operation) == result

def test_home_and_health(client):
    assert b"DevOps Notes" in client.get("/").data
    assert client.get("/health").json == {"status":"ok"}
    assert client.get("/ready").status_code == 200

def test_missing_configuration(client,monkeypatch):
    monkeypatch.delenv("API_TOKEN")
    assert client.get("/ready").status_code == 503

@pytest.mark.parametrize("payload", [{}, {"a":True,"b":2,"operation":"add"}, {"a":"2","b":3,"operation":"add"}, {"a":1,"b":0,"operation":"divide"}, {"a":1,"b":2,"operation":"power"}, {"a":1e308,"b":1e308,"operation":"multiply"}, {"a":10**400,"b":1,"operation":"add"}])
def test_invalid_calculations(client,payload):
    assert client.post("/api/calculate",json=payload).status_code == 400

def test_non_json(client):
    assert client.post("/api/calculate",data="hello").status_code == 400

def test_valid_api(client):
    assert client.post("/api/calculate",json={"a":6,"b":3,"operation":"multiply"}).json == {"result":18}

def test_private_endpoint(client,monkeypatch):
    token=secrets.token_hex(16)
    monkeypatch.setenv("API_TOKEN",token)
    assert client.get("/api/private").status_code == 401
    assert client.get("/api/private",headers={"X-API-Token":"wrong"}).status_code == 401
    assert client.get("/api/private",headers={"X-API-Token":token}).status_code == 200

def test_metrics_and_status(client):
    client.get("/")
    assert b"notes_requests_total" in client.get("/metrics").data
    assert "hostname" in client.get("/api/status").json

def test_configuration_is_escaped(client,monkeypatch):
    monkeypatch.setenv("GREETING","<script>alert(1)</script>")
    assert b"<script>" not in client.get("/").data
