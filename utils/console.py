from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()


def banner():

    console.print(
        Panel.fit(
            "[bold cyan]📈 NIFTY50 DATA ENGINE[/bold cyan]\n"
            "[green]Production Ready Stock Market Data Pipeline[/green]",
            border_style="bright_blue",
        )
    )


def success(message):
    console.print(f"[bold green]✔ {message}[/bold green]")


def warning(message):
    console.print(f"[bold yellow]⚠ {message}[/bold yellow]")


def error(message):
    console.print(f"[bold red]✖ {message}[/bold red]")


def info(message):
    console.print(f"[bold cyan]ℹ {message}[/bold cyan]")


def metric_table(title, metrics):

    table = Table(
        title=title,
        box=box.ROUNDED,
        show_lines=True
    )

    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    for key, value in metrics.items():
        table.add_row(str(key), str(value))

    console.print(table)