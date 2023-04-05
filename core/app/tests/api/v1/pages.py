from unittest.mock import AsyncMock

import pytest
import pytest_asyncio
from fastapi.testclient import TestClient

from app.main import app
from app.models.pages import Page
from app.schemas.pages import PageIn as PageSchemaIn
from app.services.pages import PagesServices


class TestPagesRoutes(pytest_asyncio):
    @pytest_asyncio.fixture(scope="function")
    async def mock_service(self):
        service_mock = PagesServices()
        service_mock.get_all_pages = AsyncMock(return_value=[])
        service_mock.get_page = AsyncMock(return_value=None)
        service_mock.create_page = AsyncMock(return_value=None)
        service_mock.update_page = AsyncMock(return_value=None)
        service_mock.delete_page = AsyncMock(return_value=None)
        return service_mock

    @pytest.fixture(scope="function")
    def mock_auth_header(self):
        return "Bearer some.jwt.token"

    @pytest.fixture(scope="function")
    def test_client(self):
        return TestClient(app)


    async def test_get_all_pages(self):
        self.mock_service.get_all_pages.return_value = [
            Page(id=1, name="Page 1", owner_id=1),
            Page(id=2, name="Page 2", owner_id=2),
        ]
        response = await self.test_client.get("/pages")
        assert response.status_code == 200
        assert response.json() == [
            {"id": 1, "name": "Page 1", "owner_id": 1},
            {"id": 2, "name": "Page 2", "owner_id": 2},
        ]
        self.mock_service.get_all_pages.assert_called_once()

    async def test_get_page(self):
        self.mock_service.get_page.return_value = Page(id=1, name="Page 1", owner_id=1)
        response = await self.test_client.get("/pages/1")
        assert response.status_code == 200
        assert response.json() == {"id": 1, "name": "Page 1", "owner_id": 1}
        self.mock_service.get_page.assert_called_once_with(1)

    async def test_create_page(self, mock_auth_header):
        page_in = {"name": "Page 1", "owner_id": 1}
        response = await self.test_client.post(
            "/pages", headers={"Authorization": mock_auth_header}, json=page_in
        )
        assert response.status_code == 200
        self.mock_service.create_page.assert_called_once_with(
            PageSchemaIn(name="Page 1", owner_id=1), mock_auth_header
        )

    async def test_update_page(self, mock_auth_header):
        page_in = {"name": "New Page Name"}
        response = await self.test_client.put(
            "/pages/1", headers={"Authorization": mock_auth_header}, json=page_in
        )
        assert response.status_code == 200
        self.mock_service.update_page.assert_called_once_with(1, PageSchemaIn(name="New Page Name"))

    async def test_delete_page(self, mock_auth_header):
        response = await self.test_client.delete(
            "/pages/1", headers={"Authorization": mock_auth_header}
        )
        assert response.status_code == 200
        self.mock_service.delete_page.assert_called_once_with(1)
