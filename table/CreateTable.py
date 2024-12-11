from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title="User Data")

table.add_column("Name", justify="right", style="cyan", no_wrap=True)
table.add_column("Email", justify="right", style="magenta")
table.add_column("Phone Number", justify="right", style="green")
table.add_column("Address", justify="right", style="bold magenta")

table.add_row("Ebrahim", "ebrahim@gmail.com", "1886644261", "Dhaka")
table.add_row("Imran", "imran@gmail.com", "123654125891", "Khulna")

console.print(table)
