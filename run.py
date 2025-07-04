import argparse
from src.cli.main import main_menu, ExitProgram, perform_cli_search

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="arXiv CLI Search Tool")
    parser.add_argument("--query", type=str, help="Search query for papers.")
    parser.add_argument("--start-date", type=str, help="Start date for search (YYYY-MM-DD).")
    parser.add_argument("--end-date", type=str, help="End date for search (YYYY-MM-DD).")

    args = parser.parse_args()

    if args.query:
        # If a query is provided, perform CLI search
        try:
            perform_cli_search(args.query, args.start_date, args.end_date)
        except ExitProgram:
            pass # Program exits gracefully
    else:
        # Otherwise, run the interactive main menu
        try:
            main_menu()
        except ExitProgram:
            pass # Program exits gracefully
