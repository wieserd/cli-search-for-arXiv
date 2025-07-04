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

You can also perform a direct search from the command line without entering the interactive menu. Use the `--query` argument for your search terms. You can optionally specify a date range using `--start-date` and `--end-date`.

```bash
python run.py --query "your search terms" [--start-date YYYY-MM-DD] [--end-date YYYY-MM-DD]
```

**Examples:**

*   Search for "quantum computing":
    ```bash
    python run.py --query "quantum computing"
    ```

*   Search for "machine learning" published between 2023 and 2024:
    ```bash
    python run.py --query "machine learning" --start-date 2023-01-01 --end-date 2024-12-31
    ```

After executing a command-line search, the results will be displayed, and the program will exit.

## 2. Search Query Arguments

The `arxiv_cli_search` tool accepts the following arguments for search queries:

*   **`--query` (Required for CLI search, interactive prompt for interactive mode):** Keywords for your search. The arXiv API typically searches across various fields including title, abstract, and authors.
*   **`--start-date` (Optional):** The start date for filtering search results in YYYY-MM-DD format. Only applicable in command-line search mode.
*   **`--end-date` (Optional):** The end date for filtering search results in YYYY-MM-DD format. Only applicable in command-line search mode.

In interactive mode, you will be prompted for keywords and an optional date range. The program does not currently support direct filtering by specific fields like "author" or "title" as separate arguments within the interactive search flow, but keywords will match against these fields.

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
