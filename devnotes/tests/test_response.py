"""
Простая проверка ответа на запрос
"""

import pytest
from httpx import ASGITransport, AsyncClient
from main import app


@pytest.mark.asyncio
async def test_say_hello():
    """ "
    Проверка что привет пришел
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/hello")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}
