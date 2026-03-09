from pyclickhouse.client import HttpClient


class TestAdmin:
    async def test_database(self, http_client: HttpClient) -> None:
        client = http_client
        admin = client.admin()

        assert client.database in await admin.show_databases()

        assert await admin.create_datbase("test_db")
        assert "test_db" in await admin.show_databases()

        assert await admin.drop_datbase("test_db")
        assert "test_db" not in await admin.show_databases()

    async def test_table(self, http_client: HttpClient) -> None:
        client = http_client
        admin = client.admin()
        pass
