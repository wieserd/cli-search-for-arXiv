import requests
import feedparser
from datetime import datetime

ARXIV_API_URL = "http://export.arxiv.org/api/query"

def search_arxiv(query, max_results=10, start_date=None, end_date=None, start=0):
    params = {
        "search_query": query,
        "max_results": max_results,
        "sortBy": "relevance",
        "sortOrder": "descending",
        "start": start # Added start parameter for pagination
    }

    # Add date range to query if provided
    if start_date and end_date:
        # arXiv API expects YYYYMMDDHHMMSS format
        # Assuming start_date and end_date are datetime objects or YYYY-MM-DD strings
        # For simplicity, let's assume YYYY-MM-DD strings for now and convert
        try:
            start_dt = datetime.strptime(start_date, "%Y-%m-%d")
            end_dt = datetime.strptime(end_date, "%Y-%m-%d")
            # Set time to start of day for start_date and end of day for end_date
            start_arxiv_format = start_dt.strftime("%Y%m%d000000")
            end_arxiv_format = end_dt.strftime("%Y%m%d235959")
            
            # Combine original query with date range
            params["search_query"] = f"{query} AND submittedDate:[{start_arxiv_format} TO {end_arxiv_format}]"
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