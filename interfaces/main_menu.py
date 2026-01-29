from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()


def home_menu():
    """Asosiy menyu - Kirish/Ro'yxatdan o'tish"""
    menu_text = """
[bold cyan]1.[/] Ro'yxatdan o'tish
[bold cyan]2.[/] Kirish
[bold cyan]0.[/] Chiqish
"""

    panel = Panel(
        menu_text,
        title="[bold green]🏠 Asosiy Menyu[/]",
        box=box.ROUNDED,
        border_style="bright_blue",
        padding=(1, 2)
    )
    console.print(panel)


def main_menu():
    """Foydalanuvchi menyusi - Kirish shartidan keyin"""
    menu_text = """
[bold cyan]1.[/] 📦 Mahsulotlarni ko'rish
[bold cyan]2.[/] 🛒 Savatga mahsulot qo'shish
[bold cyan]3.[/] 👀 Savatni ko'rish
[bold cyan]4.[/] ❌ Savatdan mahsulot olib tashlash
[bold cyan]5.[/] ✅ Buyurtma berish
[bold cyan]0.[/] 🚪 Chiqish
"""
    panel = Panel(
        menu_text,
        title="[bold green]👤 Foydalanuvchi Menyusi[/]",
        box=box.ROUNDED,
        border_style="bright_blue",
        padding=(1, 2)
    )
    console.print(panel)


def show_success(message: str):
    """Muvaffaqiyat xabari ko'rsatish"""
    panel = Panel(
        message,
        title="[bold green]✓ Muvaffaqiyat[/]",
        box=box.ROUNDED,
        border_style="bright_green"
    )
    console.print(panel)


def show_error(message: str):
    """Xato xabari ko'rsatish"""
    panel = Panel(
        message,
        title="[bold red]✗ Xato[/]",
        box=box.ROUNDED,
        border_style="bright_red"
    )
    console.print(panel)


def show_info(message: str):
    """Ma'lumot xabari ko'rsatish"""
    panel = Panel(
        message,
        title="[bold cyan]ℹ️ Ma'lumot[/]",
        box=box.ROUNDED,
        border_style="bright_cyan"
    )
    console.print(panel)