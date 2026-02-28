from pyclickhouse import Column, Expression, F


class TestFunction:
    def test_function(self) -> None:
        f = F.count("test")
        assert isinstance(f, Expression)
        assert f.value == 's"count(test)"'

        col = Expression(Column(name="valid", type="UInt8"))
        f = F.countIf(col == 1)
        assert f.value == 's"countIf(valid == 1)"'

        f = F.gcd(12, 18)
        assert f.value == 's"gcd(12, 18)"'
