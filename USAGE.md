# How to Use arXiv CLI Search

This document provides instructions on how to use the `arxiv_cli_search` command-line interface (CLI) tool.

## 1. Executing a Search

The `arxiv_cli_search` tool can be executed in two ways:

### Interactive Mode

To start the program with an interactive menu:

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

To execute a search in interactive mode, enter `1` or `search` at the prompt and press Enter. The program will then guide you through the search process.

### Command-Line Search Mode

You can also perform a direct search from the command line without entering the interactive menu. Use the `--query`, `--author`, or `--title` arguments. You can combine these, and also optionally specify a date range using `--start-date` and `--end-date`.

```bash
python run.py [--query "your search terms"] [--author "Author Name"] [--title "Paper Title Keywords"] [--start-date YYYY-MM-DD] [--end-date YYYY-MM-DD]
```

**Examples:**

*   Search for "quantum computing":
    ```bash
    python run.py --query "quantum computing"
    ```

*   Search for papers by "John Doe":
    ```bash
    python run.py --author "John Doe"
    ```

*   Search for papers with "machine learning" in the title published between 2023 and 2024:
    ```bash
    python run.py --title "machine learning" --start-date 2023-01-01 --end-date 2024-12-31
    ```

*   Combine a general query with an author:
    ```bash
    python run.py --query "neural networks" --author "Geoffrey Hinton"
    ```

After executing a command-line search, the results will be displayed, and the program will exit.

## 2. Search Query Arguments

The `arxiv_cli_search` tool accepts the following arguments for search queries:

*   **`--query` (Optional for CLI search, interactive prompt for interactive mode):** This is a general keyword search. The arXiv API searches across various fields including title, abstract, and authors.
*   **`--author` (Optional for CLI search, interactive prompt for interactive mode):** Search for papers by a specific author. Use the author's full name or a part of it.
*   **`--title` (Optional for CLI search, interactive prompt for interactive mode):** Search for papers with specific keywords in their title.
*   **`--start-date` (Optional):** The start date for filtering search results by publication date in `YYYY-MM-DD` format. Applicable in both command-line and interactive search modes.
*   **`--end-date` (Optional):** The end date for filtering search results by publication date in `YYYY-MM-DD` format. Applicable in both command-line and interactive search modes.

**Note:** At least one of `--query`, `--author`, or `--title` must be provided for a search to be performed.

## 3. How to Download a Paper

Paper downloading is supported through two methods:

### A. Interactive Download

After performing a search or viewing your library, you can select a specific paper to view its details. From the detailed paper view, you will have the option to download the PDF.

**Steps to Download Interactively:**

1.  **Perform a search** (as described in Section 1) or **View your Library** (by selecting option `2` from the main menu).
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

### B. Command-Line Download by arXiv ID

You can directly download a paper using its arXiv ID from the command line without entering the interactive menu. Use the `--download-id` argument:

```bash
python run.py --download-id "arXiv_ID"
```

**Example:**

```bash
python run.py --download-id "2301.00001"
```

After the download is complete, the program will exit.

## 4. Typical Output Format of Downloaded Papers

Downloaded papers are saved in **PDF format (`.pdf`)**.

By default, downloaded PDFs are saved to the `data/downloads/` directory within the `cli-search-for-arXiv` project folder.
