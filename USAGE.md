# How to Use arXiv CLI Search

This document provides instructions on how to use the `arxiv_cli_search` command-line interface (CLI) tool.

## 1. Executing a Search

The `arxiv_cli_search` tool is executed by running the `run.py` script. It provides an interactive menu for navigation, rather than accepting command-line arguments directly for search queries.

To start the program:

```bash
python run.py
```

Once the program starts, you will be presented with a main menu:

```
--- arXiv CLI Search ---
1. Search Papers
2. View Library
3. I'm Feeling Lucky
4. Exit arXiv Searcher
Enter your choice:
```

To execute a search, enter `1` or `search` at the prompt and press Enter. The program will then guide you through the search process.

## 2. Search Query Arguments

When you select the "Search Papers" option, the program will prompt you for your search query.

*   **Keywords:** You will be asked to enter keywords for your search. The arXiv API typically searches across various fields including title, abstract, and authors.
*   **Date Range (Optional):** After entering keywords, you can optionally specify a date range (YYYY-MM-DD) to filter your search results.

The program does not currently support direct filtering by specific fields like "author" or "title" as separate arguments within the interactive search flow, but keywords will match against these fields.

## 3. How to Download a Paper

Paper downloading is supported. After performing a search or viewing your library, you can select a specific paper to view its details. From the detailed paper view, you will have the option to download the PDF.

**Steps to Download:**

1.  **Perform a search** (as described above) or **View your Library** (by selecting option `2` from the main menu).
2.  **Select a paper:** From the list of search results or library papers, enter the corresponding number of the paper you wish to view and download.
3.  **Download:** In the detailed paper view, you will see options. Enter `download` or `1` to download the PDF.

Example of options in detailed paper view:

```
--- Paper Details ---
... (paper information) ...

1. Download
2. Add to Library / Remove from Library
e. Expand (find related papers)
b. Back
exit. Exit arXiv Searcher
Enter your choice:
```

## 4. Typical Output Format of Downloaded Papers

Downloaded papers are saved in **PDF format (`.pdf`)**.

By default, downloaded PDFs are saved to the `data/downloads/` directory within the `cli-search-for-arXiv` project folder.
