import argparse
from src.cli.main import main_menu, ExitProgram, perform_cli_search, perform_cli_download

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="arXiv CLI Search Tool")
    parser.add_argument("--query", type=str, help="Search query for papers.")
    parser.add_argument("--author", type=str, help="Author name to search for.")
    parser.add_argument("--title", type=str, help="Title keyword to search for.")
    parser.add_argument("--start-date", type=str, help="Start date for search (YYYY-MM-DD).")
    parser.add_argument("--end-date", type=str, help="End date for search (YYYY-MM-DD).")
    parser.add_argument("--download-id", type=str, help="arXiv ID of the paper to download directly.")

    args = parser.parse_args()

    if args.download_id:
        try:
            perform_cli_download(args.download_id)
        except ExitProgram:
            pass # Program exits gracefully
    elif args.query or args.author or args.title:
        # If any search argument is provided, perform CLI search
        try:
            perform_cli_search(args.query, args.author, args.title, args.start_date, args.end_date)
        except ExitProgram:
            pass # Program exits gracefully
    else:
        # Otherwise, run the interactive main menu
        try:
            main_menu()
        except ExitProgram:
            pass # Program exits gracefully
