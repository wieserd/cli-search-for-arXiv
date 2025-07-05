import time
import threading
import os
from rich.console import Console
from rich.live import Live
from rich.spinner import Spinner
from rich.text import Text
from .logo.logo_art import display_logo as rich_display_logo # Import the new logo function

console = Console()

def print_arxiv_logo():
    # This function now simply calls the rich-based logo display from logo_art.py
    rich_display_logo()

def print_papers_list(papers):
    if not papers:
        console.print("No papers found.", style="bold red")
        return

    for i, paper in enumerate(papers):
        console.print(f"\n[bold blue]{i+1}. Title:[/bold blue] [green]{paper['title']}[/green]")
        console.print(f"   [bold]Authors:[/bold] {', '.join(paper['authors'])}")
        console.print(f"   [bold]Published:[/bold] {paper['published']}")
        console.print(f"   [bold]Categories:[/bold] {', '.join(paper['categories'])}")
        console.print(f"   [bold]arXiv ID:[/bold] {paper['id']}")
        console.print(f"   [bold]PDF URL:[/bold] {paper['pdf_url']}")


def print_paper_details(paper):
    console.print(f"\n[bold yellow]--- Paper Details ---[/bold yellow]")
    console.print(f"[bold]Title:[/bold] {paper['title']}")
    console.print(f"[bold]Authors:[/bold] {', '.join(paper['authors'])}")
    console.print(f"[bold]Published:[/bold] {paper['published']}")
    console.print(f"[bold]Categories:[/bold] {', '.join(paper['categories'])}")
    console.print(f"[bold]arXiv ID:[/bold] {paper['id']}")
    console.print(f"[bold]PDF URL:[/bold] {paper['pdf_url']}")
    console.print(f"\n[bold]Summary:[/bold]\n{paper['summary']}")

class LoadingAnimation:
    def __init__(self, message="Loading"):
        self._message = message
        self._live = Live(console=console, screen=True, refresh_per_second=10)
        self._spinner = Spinner("dots", text=Text(message, style="green"))

    def start(self):
        self._live.start()
        self._live.update(self._spinner)

    def stop(self):
        self._live.stop()
        console.print("", end='\r') # Clear the line after stopping
