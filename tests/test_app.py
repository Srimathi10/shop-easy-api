from src.app import main


def test_demo_app_runs(capsys):
    assert main() == 0
    assert "Payment: Approved" in capsys.readouterr().out
