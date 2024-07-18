import click
import psutil
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, SpinnerColumn
import datetime

console = Console()

def get_battery_info():
    battery = psutil.sensors_battery()
    return battery if battery else None

def format_time(seconds):
    if seconds == psutil.POWER_TIME_UNLIMITED:
        return "Unlimited"
    elif seconds == psutil.POWER_TIME_UNKNOWN:
        return "Unknown"
    else:
        return str(datetime.timedelta(seconds=seconds))

@click.command()
def cli():
    """Displays detailed battery information and progress bar."""
    battery = get_battery_info()
    if battery is not None:
        percentage = battery.percent
        plugged = battery.power_plugged
        time_left = battery.secsleft

        # Determine color based on battery percentage
        if percentage >= 80:
            color = "#4CAF50"  # Green
        elif percentage >= 30:
            color = "#FFC107"  # Amber
        else:
            color = "#F44336"  # Red
        
        formatted_percentage = f"{percentage}%"
        status = "Plugged In" if plugged else "Not Plugged In"
        time_left_str = format_time(time_left)

        with Progress(
            SpinnerColumn(),
            BarColumn(bar_width=20, complete_style=color, finished_style=color),
            console=console,
            transient=True,
        ) as progress:
            task = progress.add_task("Battery", total=100)
            progress.update(task, completed=percentage)
        
        progress_bar = ''.join([f'{"█" if i < percentage / 5 else "░"}' for i in range(20)])

        panel_content = f"[{color}]Percentage: {formatted_percentage}[/]\n\n" \
                        f"[{color}]{progress_bar}[/]\n\n" \
                        f"[{color}]Status: {status}[/]\n"

        if not plugged:
            panel_content += f"[{color}]Time Left: {time_left_str}[/]"

        panel = Panel(
            panel_content,
            title="Battery Status",
            border_style=color,
            style=color,
            width=40,  # Set the width of the panel
        )
        
        console.print(panel)
    else:
        console.print(Panel(
            "[bold red]Battery information not available.[/bold red]",
            title="Error",
            border_style="red",
            expand=False
        ))

if __name__ == '__main__':
    cli()
