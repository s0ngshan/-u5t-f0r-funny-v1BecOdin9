import sys
from PyQt6.QtWidgets import QApplication, QDialog
from config import load_config, save_config
from widget import TokenWidget, SettingsDialog


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    cfg = load_config()

    # First run: open settings if no cookie
    if not cfg.get("cookie"):
        dlg = SettingsDialog(cfg)
        dlg.setWindowTitle("MiMo Token - 首次配置")
        if dlg.exec() == QDialog.DialogCode.Accepted:
            cfg = dlg.get_config()
            save_config(cfg)
        else:
            sys.exit(0)

    widget = TokenWidget(cfg)
    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
