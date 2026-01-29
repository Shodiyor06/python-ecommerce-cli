from rich import box
from rich.console import Console
from rich.panel import Panel

console = Console()


def home_menu():

    panel = Panel(
        menu_text,
        title="[bold green]🏠 Asosiy Menyu[/]",
        box=box.ROUNDED,
        border_style="bright_blue",
        padding=(1, 2),
    )
    console.print(panel)


def main_menu():
    panel = Panel(
        menu_text,
        title="[bold green]👤 Foydalanuvchi Menyusi[/]",
        box=box.ROUNDED,
        border_style="bright_blue",
        padding=(1, 2),
    )
    console.print(panel)


def show_success(message: str):
    panel = Panel(
        message,
        title="[bold green]✓ Muvaffaqiyat[/]",
        box=box.ROUNDED,
        border_style="bright_green",
    )
    console.print(panel)


def show_error(message: str):
    panel = Panel(
        message, title="[bold red]✗ Xato[/]", box=box.ROUNDED, border_style="bright_red"
    )
    console.print(panel)


def show_info(message: str):
    panel = Panel(
        message,
        title="[bold cyan]ℹ️ Ma'lumot[/]",
        box=box.ROUNDED,
        border_style="bright_cyan",
    )
    console.print(panel)
