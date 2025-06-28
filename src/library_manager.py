import json
import os
from datetime import datetime

LIBRARY_FILE = "data/library.json"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_library(library):
    with open(LIBRARY_FILE, 'w') as f:
        json.dump(library, f, indent=4)

def add_paper_to_library(paper, library):
    # Check if paper already exists in library
    if any(p['id'] == paper['id'] for p in library):
        print("Paper already in your library.")
        return False
    library.append(paper)
    save_library(library)
    print("Paper added to your library.")
    return True

def remove_paper_from_library(paper_id, library):
    initial_len = len(library)
    library[:] = [p for p in library if p['id'] != paper_id]
    if len(library) < initial_len:
        save_library(library)
        print("Paper removed from your library.")
        return True
    print("Paper not found in your library.")
    return False

def filter_library(library, keyword):
    if not keyword:
        return library
    keyword_lower = keyword.lower()
    filtered_papers = []
    for paper in library:
        if (keyword_lower in paper['title'].lower() or
            any(keyword_lower in author.lower() for author in paper['authors']) or
            keyword_lower in paper['summary'].lower()):
            filtered_papers.append(paper)
    return filtered_papers

def sort_library(library, sort_by, order):
    if not library:
        return []

    if sort_by == 'published':
        # Sort by date, converting string to datetime object for proper comparison
        return sorted(library, key=lambda x: datetime.strptime(x['published'], "%Y-%m-%dT%H:%M:%SZ"), reverse=(order == 'desc'))
    elif sort_by == 'title':
        return sorted(library, key=lambda x: x['title'].lower(), reverse=(order == 'desc'))
    elif sort_by == 'authors':
        # Sort by the first author's name
        return sorted(library, key=lambda x: x['authors'][0].lower() if x['authors'] else '', reverse=(order == 'desc'))
    else:
        print(f"Warning: Unknown sort key '{sort_by}'. No sorting applied.")
        return library
