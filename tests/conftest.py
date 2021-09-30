import pytest
import asyncio

from httpx import AsyncClient
from asgi_lifespan import LifespanManager

from app.rest_api import rest_api
from app.rests import post_router

rest_api.initialize()

# FIXTURES QUE CRIAMOS
@pytest.fixture
def clear_comment_database():
    rest_api.comment_repository.clear() 

    yield

    rest_api.comment_repository.clear()

@pytest.fixture
def clear_post_database():
    rest_api.post_repository.clear()

    yield

    rest_api.post_repository.clear()

@pytest.fixture
def post_prefix():
    return post_router.prefix

# ASSÍNCRONO
@pytest.fixture(scope="session")
def event_loop(request):
  loop = asyncio.get_event_loop_policy().new_event_loop()

  try:
    yield loop
  finally:
    loop.close()

@pytest.fixture(scope="session")
async def test_app():
    app = rest_api.server

    async with LifespanManager(app):
        yield app

@pytest.fixture
async def client(test_app):
    async with AsyncClient(app=test_app, base_url="http://test") as client: 
        yield client

