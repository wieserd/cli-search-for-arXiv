from src.cli.main import main_menu, ExitProgram

if __name__ == "__main__":
    try:
        main_menu()
    except ExitProgram:
        pass # Program exits gracefully