import os
from src.arxiv_api import search_arxiv, _extract_keywords
from src.library_manager import load_library, add_paper_to_library, remove_paper_from_library, save_library, filter_library, sort_library
from src.downloader import download_pdf
from src.display_utils import print_papers_list, print_paper_details, LoadingAnimation, print_arxiv_logo
import requests # Import requests to catch its exceptions
from datetime import datetime
import time # Import time for delays
import webbrowser # Import webbrowser for opening URLs

class ExitProgram(Exception):
    """Custom exception to signal program exit."""
    pass

def main_menu():
    print_arxiv_logo() # Display logo at the very beginning
    while True:
        print("\n--- arXiv CLI Search ---")
        print("1. Search Papers")
        print("2. View Library")
        print("3. I'm Feeling Lucky")
        print("4. Play Theme") # New option
        print("5. Exit arXiv Searcher") # Shifted option
        choice = input("Enter your choice: ").lower().strip()

        if choice == '1' or choice == 'search':
            try:
                search_papers_menu()
            except ExitProgram:
                break # Exit main menu loop
        elif choice == '2' or choice == 'library':
            try:
                view_library_menu()
            except ExitProgram:
                break # Exit main menu loop
        elif choice == '3' or choice == 'lucky':
            try:
                feeling_lucky_menu()
            except ExitProgram:
                break # Exit main menu loop
        elif choice == '4' or choice == 'play theme': # New option handling
            play_theme()
        elif choice == '5' or choice == 'exit' or choice == 'exit arxiv searcher': # Shifted option handling
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def play_theme():
    theme_url = "https://youtu.be/yqLY9vlBU_E"
    print(f"Opening theme music in your web browser: {theme_url}")
    try:
        webbrowser.open(theme_url)
    except Exception as e:
        print(f"Error opening web browser: {e}")

def _perform_search_and_display(query, start_date=None, end_date=None):
    loading_animation = LoadingAnimation("Searching arXiv")
    loading_animation.start()
    try:
        papers = search_arxiv(query, start_date=start_date, end_date=end_date)
        loading_animation.stop()
        if not papers:
            print("No papers found for your query.")
            return []

        print_papers_list(papers)
        return papers
    except requests.exceptions.RequestException as e:
        loading_animation.stop()
        print(f"Error connecting to arXiv API: {e}")
        return []
    except Exception as e:
        loading_animation.stop()
        print(f"An unexpected error occurred during search: {e}")
        return []

def perform_cli_search(query, start_date=None, end_date=None):
    print_arxiv_logo()
    print(f"Performing CLI search for: '{query}'")
    if start_date and end_date:
        print(f"Date range: {start_date} to {end_date}")
    _perform_search_and_display(query, start_date, end_date)
    print("CLI search complete.")

def search_papers_menu():
    query = input("Enter search query: ")
    start_date = None
    end_date = None

    date_range_choice = input("Do you want to specify a date range? (yes/no): ").lower().strip()
    if date_range_choice == 'yes':
        while True:
            start_date_str = input("Enter start date (YYYY-MM-DD): ")
            end_date_str = input("Enter end date (YYYY-MM-DD): ")
            try:
                datetime.strptime(start_date_str, "%Y-%m-%d")
                datetime.strptime(end_date_str, "%Y-%m-%d")
                start_date = start_date_str
                end_date = end_date_str
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    papers = _perform_search_and_display(query, start_date, end_date)
    if not papers:
        return
        
    while True:
        print("\n--- Search Results Options ---")
        print("Enter paper number for details/actions, 'b' to go back, 'e' to expand, or 'exit' to quit.")
        action = input("Your choice: ").lower().strip()

        if action == 'b' or action == 'back':
            break
        elif action == 'e' or action == 'expand':
            expand_action = input("Enter paper number to expand on: ").lower().strip()
            try:
                paper_index = int(expand_action) - 1
                if 0 <= paper_index < len(papers):
                    selected_paper = papers[paper_index]
                    expand_on_paper(selected_paper)
                else:
                    print("Invalid paper number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif action == 'exit' or action == 'exit arxiv searcher':
            raise ExitProgram
        
        try:
            paper_index = int(action) - 1
            if 0 <= paper_index < len(papers):
                selected_paper = papers[paper_index]
                handle_paper_actions(selected_paper)
            else:
                print("Invalid paper number.")
        except ValueError:
            print("Invalid input. Please enter a number, 'b', 'e', or 'exit'.")

def expand_on_paper(paper):
    print(f"\nExpanding on: {paper['title']}")
    keywords = _extract_keywords(paper)
    print(f"Searching for related papers using keywords: {keywords}")
    
    loading_animation = LoadingAnimation("Searching for related papers")
    loading_animation.start()
    try:
        related_papers = search_arxiv(query=keywords, max_results=5) # Get 5 related papers
        loading_animation.stop()
        if not related_papers:
            print("No related papers found.")
            return

        print("\n--- Related Papers ---")
        print_papers_list(related_papers)

        while True:
            print("\n--- Related Papers Options ---")
            print("Enter paper number for details/actions, 'b' to go back, 'e' to expand, or 'exit' to quit.")
            action = input("Your choice: ").lower().strip()

            if action == 'b' or action == 'back':
                break
            elif action == 'e' or action == 'expand':
                expand_action = input("Enter paper number to expand on: ").lower().strip()
                try:
                    paper_index = int(expand_action) - 1
                    if 0 <= paper_index < len(related_papers):
                        selected_paper = related_papers[paper_index]
                        expand_on_paper(selected_paper) # Recursive call for further expansion
                    else:
                        print("Invalid paper number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif action == 'exit' or action == 'exit arxiv searcher':
                raise ExitProgram
            
            try:
                paper_index = int(action) - 1
                if 0 <= paper_index < len(related_papers):
                    selected_paper = related_papers[paper_index]
                    handle_paper_actions(selected_paper)
                else:
                    print("Invalid paper number.")
            except ValueError:
                print("Invalid input. Please enter a number, 'b', 'e', or 'exit'.")

    except requests.exceptions.RequestException as e:
        loading_animation.stop()
        print(f"Error connecting to arXiv API: {e}")
    except Exception as e:
        loading_animation.stop()
        print(f"An unexpected error occurred: {e}")

def feeling_lucky_menu():
    print("Fetching 10 random papers...")
    loading_animation = LoadingAnimation("Fetching random papers")
    loading_animation.start()
    try:
        # Use a very broad query to get diverse results
        papers = search_arxiv(query="all:the", max_results=10)
        loading_animation.stop()
        if not papers:
            print("Could not fetch random papers.")
            return
        
        print_papers_list(papers)

        while True:
            print("\n--- Lucky Papers Options ---")
            print("Enter paper number for details/actions, 'b' to go back, 'e' to expand, or 'exit' to quit.")
            action = input("Your choice: ").lower().strip()

            if action == 'b' or action == 'back':
                break
            elif action == 'e' or action == 'expand':
                expand_action = input("Enter paper number to expand on: ").lower().strip()
                try:
                    paper_index = int(expand_action) - 1
                    if 0 <= paper_index < len(papers):
                        selected_paper = papers[paper_index]
                        expand_on_paper(selected_paper) # Recursive call for further expansion
                    else:
                        print("Invalid paper number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif action == 'exit' or action == 'exit arxiv searcher':
                raise ExitProgram
            
            try:
                paper_index = int(action) - 1
                if 0 <= paper_index < len(papers):
                    selected_paper = papers[paper_index]
                    handle_paper_actions(selected_paper)
                else:
                    print("Invalid paper number.")
            except ValueError:
                print("Invalid input. Please enter a number, 'b', 'e', or 'exit'.")

    except requests.exceptions.RequestException as e:
        loading_animation.stop()
        print(f"Error connecting to arXiv API: {e}")
    except Exception as e:
        loading_animation.stop()
        print(f"An unexpected error occurred: {e}")

def bulk_download_papers(papers_to_download):
    if not papers_to_download:
        print("No papers to download in the current view.")
        return

    print(f"\nInitiating bulk download of {len(papers_to_download)} papers...")
    for i, paper in enumerate(papers_to_download):
        print(f"Downloading {i+1}/{len(papers_to_download)}: {paper['title']} ({paper['id']})")
        if paper['pdf_url']:
            download_pdf(paper['pdf_url'], paper['id'])
            if i < len(papers_to_download) - 1: # Don't delay after the last download
                print("Waiting 3 seconds...")
                time.sleep(3)
        else:
            print(f"PDF URL not available for {paper['title']}.")
    print("Bulk download complete.")

def view_library_menu():
    full_library = load_library()
    if not full_library:
        print("Your library is empty.")
        return

    current_library_view = list(full_library) # Start with a copy of the full library

    while True:
        print("\n--- Your Library ---")
        print_papers_list(current_library_view)

        print("\n--- Library Options ---")
        print("1. View/Act on Paper (enter number)")
        print("2. Filter Library")
        print("3. Sort Library")
        print("4. Reset View (show all)")
        print("5. Bulk Download Current View")
        print("b. Back to Main Menu")
        print("exit. Exit arXiv Searcher")
        action = input("Enter your choice: ").lower().strip()

        if action == 'b' or action == 'back':
            break
        elif action == 'exit' or action == 'exit arxiv searcher':
            raise ExitProgram
        elif action == '1':
            sub_action = input("Enter paper number for details/actions: ").lower().strip()
            try:
                paper_index = int(sub_action) - 1
                if 0 <= paper_index < len(current_library_view):
                    selected_paper = current_library_view[paper_index]
                    handle_paper_actions(selected_paper, is_library_paper=True)
                    # After action, reload full library and reset view to reflect changes
                    full_library = load_library()
                    current_library_view = list(full_library)
                else:
                    print("Invalid paper number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except ExitProgram:
                raise # Re-raise to propagate to main_menu
        elif action == '2' or action == 'filter':
            keyword = input("Enter keyword to filter by: ").strip()
            current_library_view = filter_library(full_library, keyword)
            if not current_library_view:
                print("No papers match your filter.")
        elif action == '3' or action == 'sort':
            sort_by = input("Sort by (published, title, authors): ").lower().strip()
            order = input("Order (asc/desc): ").lower().strip()
            if order not in ['asc', 'desc']:
                print("Invalid order. Using 'desc'.")
                order = 'desc'
            current_library_view = sort_library(current_library_view, sort_by, order)
        elif action == '4' or action == 'reset':
            current_library_view = list(full_library) # Reset to original full library
            print("Library view reset.")
        elif action == '5' or action == 'bulk download':
            bulk_download_papers(current_library_view)
        else:
            print("Invalid choice. Please try again.")

def handle_paper_actions(paper, is_library_paper=False):
    print_paper_details(paper)
    while True:
        print("\n--- Paper Actions ---")
        print("1. Download PDF")
        if not is_library_paper:
            print("2. Add to Library")
        else:
            print("2. Remove from Library")
        print("b. Back to list")
        print("e. Expand (find related papers)") # Added expand option
        print("exit. Exit arXiv Searcher")
        
        action = input("Your choice: ").lower().strip()

        if action == '1' or action == 'download':
            if paper['pdf_url']:
                download_pdf(paper['pdf_url'], paper['id'])
            else:
                print("PDF URL not available for this paper.")
        elif action == '2':
            if not is_library_paper:
                library = load_library()
                add_paper_to_library(paper, library)
            else:
                library = load_library()
                remove_paper_from_library(paper['id'], library)
        elif action == 'b' or action == 'back':
            break
        elif action == 'e' or action == 'expand': # Handle expand action
            expand_on_paper(paper)
        elif action == 'exit' or action == 'exit arxiv searcher':
            raise ExitProgram
        else:
            print("Invalid choice. Please try again.")