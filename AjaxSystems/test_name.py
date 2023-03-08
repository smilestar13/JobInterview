from AjaxSystems.scanner_handler import CheckQr


def mock_check_in_db(qr: str):
    return True


class TestColor:

    def test_red_color(self, monkeypatch):
        obj = CheckQr()
        monkeypatch.setattr(obj, "check_in_db", mock_check_in_db)
        obj.check_scanned_device('red')
        assert obj.color == "Red"

    def test_green_color(self, monkeypatch):
        obj = CheckQr()
        monkeypatch.setattr(obj, "check_in_db", mock_check_in_db)
        obj.check_scanned_device('Green')
        assert obj.color == "Green"

    def test_fuzzy_color(self, monkeypatch):
        obj = CheckQr()
        monkeypatch.setattr(obj, "check_in_db", mock_check_in_db)
        obj.check_scanned_device('Fuzzyгг')
        assert obj.color == "Fuzzy Wuzzy"

    def test_bad_color(self, monkeypatch):
        obj = CheckQr()
        monkeypatch.setattr(obj, "check_in_db", mock_check_in_db)
        obj.check_scanned_device('Fuzzy Wuzzy')
        assert obj.color is None
