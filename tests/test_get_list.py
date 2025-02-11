import httpx
from jsonschema import validate
from core.contracts import LIST_DATA_SCHEMA

host = "https://reqres.in/"
endpoint_list_resource = "api/unknown"
endpoint_single_resource = "api/unknown/2"
endpoint_single_resource_nf = "api/unknown/23"
color_starts = "#"
hyphen = "-"

def test_list_resource():
    response = httpx.get(host + endpoint_list_resource)
    assert response.status_code == 200
    data = response.json()["data"]

    for item in data:
        validate(item, LIST_DATA_SCHEMA)
        assert item["color"].startswith(color_starts)
        assert hyphen in item["pantone_value"]

def test_single_resource():
    response = httpx.get(host + endpoint_single_resource)
    assert response.status_code == 200
    data = response.json()["data"]
    validate(data, LIST_DATA_SCHEMA)
    assert data["color"].startswith(color_starts)
    assert hyphen in data["pantone_value"]

def test_single_resource_nf():
    response = httpx.get(host + endpoint_single_resource_nf)
    assert response.status_code == 404