import time

from rich.console import Console
from rich.table import Table


console = Console()


def show_startup(message):
    with console.status(message, spinner="dots"):
        time.sleep(2)
        
def print_controls():
    console.print("Controls:",
                  "[red]q[/] stop",
                  "[cyan]s[/] toggle price alerts",
                  "[magenta]a[/] show alert queue")
    
def print_tick(count, tick, avg, min_price, max_price):
    table = Table.grid(padding=(0, 3))
    
    table.add_column(justify="right", no_wrap=True)
    table.add_column(no_wrap=True)
    table.add_column(justify="right", no_wrap=True)
    table.add_column(justify="right", no_wrap=True)
    table.add_column(justify="right", no_wrap=True)
    table.add_column(justify="right", no_wrap=True)
    
    table.add_row(
        f"[white]{count:>4}[/]",
        f"[red]{tick['symbol']:<6}[/]",
        f"[green]{tick['price']:>10.2f}[/]",
        f"avg [cyan]{avg:>10.2f}[/]",
        f"min [blue]{min_price:>10.2f}[/]",
        f"max [magenta]{max_price:>10.2f}[/]",
    )

    console.print(table)


def print_signal(signal, alert):
    color = "green" if signal == "BUY" else "red"

    console.print(
        f"[{color}]{signal:<4}[/]",
        f"[white]{alert['symbol']:<6}[/]",
        f"[dim]RSI:[/] [yellow]{alert['rsi']}[/]",
    )


def print_queue_state(alert_queue):
    table = Table.grid(padding=(0, 2))
    table.add_column(no_wrap=True)
    table.add_column()

    rows = [
        ("newest", alert_queue.peek("newest")),
        ("highest", alert_queue.peek("highest")),
        ("oldest", alert_queue.peek("oldest")),
        ("lowest", alert_queue.peek("lowest")),
    ]

    for label, value in rows:
        table.add_row(f"[cyan]{label:<8}[/]", str(value))

    console.print(table)