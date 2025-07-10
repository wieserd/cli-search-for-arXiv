import requests
import feedparser
from datetime import datetime

ARXIV_API_URL = "http://export.arxiv.org/api/query"

def search_arxiv(query=None, author=None, title=None, id_list=None, max_results=10, start_date=None, end_date=None, start=0):
    if id_list:
        params = {
            "id_list": ",".join(id_list) if isinstance(id_list, list) else id_list,
            "max_results": max_results,
            "start": start
        }
    else:
        search_parts = []
        if query:
            search_parts.append(query)
        if author:
            search_parts.append(f"au:{author}")
        if title:
            search_parts.append(f"ti:{title}")

        if not search_parts:
            raise ValueError("At least one search parameter (query, author, title, or id_list) must be provided.")

        combined_query = " AND ".join(search_parts)

        params = {
            "search_query": combined_query,
            "max_results": max_results,
            "sortBy": "relevance",
            "sortOrder": "descending",
            "start": start
        }

    # Add date range to query if provided
    if start_date and end_date:
        try:
            start_dt = datetime.strptime(start_date, "%Y-%m-%d")
            end_dt = datetime.strptime(end_date, "%Y-%m-%d")
            start_arxiv_format = start_dt.strftime("%Y%m%d000000")
            end_arxiv_format = end_dt.strftime("%Y%m%d235959")
            
            # Combine original query with date range
            params["search_query"] = f"{combined_query} AND submittedDate:[{start_arxiv_format} TO {end_arxiv_format}]"
        except ValueError:
            print("Warning: Invalid date format. Date range filter will be ignored.")

    response = requests.get(ARXIV_API_URL, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    feed = feedparser.parse(response.content)
    
    papers = []
    for entry in feed.entries:
        pdf_url = None
        for link in entry.links:
            if link.type == "application/pdf":
                pdf_url = link.href
                break

        papers.append({
            "id": entry.id.split("/")[-1],
            "title": entry.title,
            "authors": [author.name for author in entry.authors],
            "published": entry.published,
            "summary": entry.summary,
            "pdf_url": pdf_url,
            "categories": [tag.term for tag in entry.tags]
        })
    return papers

def _extract_keywords(paper):
    # Combine relevant fields
    text_to_process = f"{paper['title']} {paper['summary']}"
    # Add categories as well
    text_to_process += " " + " ".join(paper['categories'])

    # Simple tokenization and lowercasing
    words = [word.lower() for word in text_to_process.split() if len(word) > 2] # Filter short words

    # Join with OR for arXiv API
    return " OR ".join(list(set(words))) # Use set to remove duplicates