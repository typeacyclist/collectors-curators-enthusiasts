import os
from pathlib import Path

TEST_DB = Path(__file__).parent / "test-cce.db"
if TEST_DB.exists():
    TEST_DB.unlink()
os.environ["DATABASE_URL"] = f"sqlite:///{TEST_DB}"
os.environ["AUTH_MODE"] = "dev"
os.environ["SESSION_SECRET"] = "test-secret"

from fastapi.testclient import TestClient
from app.main import app


def test_mvp_workflow():
    with TestClient(app) as client:
        assert client.get("/health").json() == {"status": "ok"}
        login = client.post("/auth/dev-login", follow_redirects=False)
        assert login.status_code == 303

        dashboard = client.get("/app")
        assert dashboard.status_code == 200
        assert "Park City Orchids and More" in dashboard.text

        locations = client.get("/locations")
        assert locations.status_code == 200
        assert "Rack 1" in locations.text

        create = client.post(
            "/orchids",
            data={
                "display_name": "Cymbidium Golden Elf ‘Sundust’",
                "collection_id": _first_select_value(client.get("/orchids/new").text, "collection_id"),
                "location_id": _first_select_value(client.get("/orchids/new").text, "location_id", skip_blank=True),
                "status": "ACTIVE",
                "genus": "Cymbidium",
                "species_grex": "Golden Elf",
                "cultivar_clone": "Sundust",
                "narrative": "Bought from Andy for $34.44. Good price, needs TLC.",
                "source_name": "Andy",
                "purchase_price": "34.44",
            },
            follow_redirects=False,
        )
        assert create.status_code == 303
        detail_url = create.headers["location"]
        detail = client.get(detail_url)
        assert detail.status_code == 200
        assert "PCO-" in detail.text
        assert "Bought from Andy" in detail.text

        label = client.get(f"{detail_url}/label.pdf")
        assert label.status_code == 200
        assert label.headers["content-type"] == "application/pdf"
        assert label.content.startswith(b"%PDF")


def _first_select_value(html: str, name: str, skip_blank: bool = False) -> str:
    from html.parser import HTMLParser

    class Parser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.in_target = False
            self.values = []

        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if tag == "select" and attrs.get("name") == name:
                self.in_target = True
            elif tag == "option" and self.in_target:
                value = attrs.get("value", "")
                if not skip_blank or value:
                    self.values.append(value)

        def handle_endtag(self, tag):
            if tag == "select" and self.in_target:
                self.in_target = False

    parser = Parser()
    parser.feed(html)
    return parser.values[0]
