from pyclickhouse.types import LowCardinality, String


class TestDataTypes:
    def test_string(self) -> None:
        assert str(String()) == "String"

    def test_container(self) -> None:
        assert str(LowCardinality(String())) == "LowCardinality(String)"
