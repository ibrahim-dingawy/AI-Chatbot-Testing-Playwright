import json
from pathlib import Path
import pytest

# هنشتغل على الديمو ده:
BASE_URL = "https://www.chatbuild.io/demo"

ROOT_DIR = Path(__file__).parent
DATA_FILE = ROOT_DIR / "data" / "chatbuild_scenarios.json"


@pytest.fixture(scope="session")
def base_url() -> str:
    """Base URL for the ChatBuild demo chatbot."""
    return BASE_URL


@pytest.fixture(scope="session")
def chatbuild_scenarios():
    """Load chatbot test scenarios from JSON file."""
    with DATA_FILE.open(encoding="utf-8") as f:
        return json.load(f)
