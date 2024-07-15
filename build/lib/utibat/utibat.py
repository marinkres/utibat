#utibat.py
import click
import psutil
from colorama import Fore, Style

def get_battery_percentage():
    battery = psutil.sensors_battery()
    return battery.percent if battery else None

def print_progress_bar(percentage):
    length = 20
    filled_length = int(length * percentage / 100)
    bar = f"[{'#' * filled_length}{'-' * (length - filled_length)}]"
    return bar

@click.group()
def cli():
    pass

@cli.command()
def battery():
    """Displays battery information and progress bar."""
    percentage = get_battery_percentage()
    if percentage is not None:
        color = Fore.GREEN if percentage >= 80 else Fore.YELLOW
        formatted_percentage = f"{percentage}%".rjust(4)
        click.echo(f"{color}Battery Percentage: {formatted_percentage}{Style.RESET_ALL}")
        click.echo(print_progress_bar(percentage))
    else:
        click.echo("Battery information not available.")

if __name__ == '__main__':
    cli()
