"""Программа приветствия с красивым выводом через rich."""

from rich import print as rprint


def main() -> None:
    name = input("Как тебя зовут? ")
    year = int(input("Какой сейчас год? "))
    age = int(input("Сколько тебе лет? "))

    rprint(f"[bold green]Привет, {name}![/bold green]")
    rprint(f"[cyan]Ты родился примерно в {year - age} году.[/cyan]")
    rprint(f"[yellow]До 100 лет тебе осталось [bold]{100 - age}[/bold] лет.[/yellow]")


if __name__ == "__main__":
    main()
