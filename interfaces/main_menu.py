from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()

def home_menu():
    menu_text = """
[bold cyan]1.:[/]ro'yxatdan kirish
[bold cyan]2.:[/]kirish
[bold cyan]0.:[/]Chiqish
"""

    panel = Panel(
        menu_text,
        title="[bold green]Asosiy menyu[/]",
        box=box.ROUNDED,
        border_style="bright_blue"
    )
    console.print(panel)

def main_menu():
    menu_text = """
[bold cyan]1.:[/] Mahsulotlarni ko'rish
[bold cyan]2.:[/] Savatga mahsulot qo'shish
[bold cyan]3.:[/] Savatni ko'rish
[bold cyan]4.:[/] Savatdan mahsulot olib tashlash
[bold cyan]5.:[/] Buyurtma berish
[bold cyan]0.:[/] Chiqish
"""
    panel = Panel(
        menu_text,
        title="[bold green]Foydalanuvchi menyusi[/]",
        box=box.ROUNDED,
        border_style="bright_blue"
    )
    console.print(panel)