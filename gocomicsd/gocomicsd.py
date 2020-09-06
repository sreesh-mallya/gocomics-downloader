import datetime
from pathlib import Path
from typing import Optional

import typer
from halo import Halo
from rich.console import Console
from rich.progress import Progress
from rich.table import Table

from gocomicsd.commons import INVALID_DATE_MESSAGE, FILENAME, TITLE_NOT_FOUND_MESSAGE
from gocomicsd.helpers import get_titles, create_dirs, save_title_for_date
from gocomicsd.utils import DateIterator

console = Console()
dt_now = datetime.datetime.now().strftime("%Y-%m-%d")
cli = typer.Typer(help="Download comic strips from gocomics.com.")


def is_valid_date(date: str):
    try:
        validated_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        if datetime.datetime.strptime(dt_now, '%Y-%m-%d') < validated_date:
            raise ValueError
    except ValueError:
        raise typer.BadParameter(INVALID_DATE_MESSAGE)
    return date


def title_exists(title: str):
    title = title.lower()

    with Halo(text='Getting titles from gocomics.com', spinner='dots'):
        titles_ = get_titles()

    if title not in titles_.keys():
        raise typer.BadParameter(TITLE_NOT_FOUND_MESSAGE.format(title))

    return title


@cli.command()
def titles(search: str = typer.Option(None, help='Search for comics by name.')):
    """List all available comics from gocomics.com."""

    with Halo(text='Getting titles from gocomics.com', spinner='dots'):
        titles_ = get_titles(search)

    table = Table(show_header=True)
    table.add_column('TITLE')
    table.add_column('NAME', justify='right')

    if search is not None:
        console.print('Found {} search result(s) for `{}`.'.format(len(titles_), search))

    if len(titles_) > 0:
        for k, v in titles_.items():
            table.add_row(v, '[yellow]{}[/yellow]'.format(k))
        console.print(table)
        console.print('Use [bold]gocomicsd save NAME[/bold] to download.')
    else:
        console.print('[red]Something\'s wrong. Couldn\'t get titles.[/red]')


@cli.command()
def save(
        title: str = typer.Argument(..., help='Title to download.', callback=title_exists),
        path: Optional[Path] = typer.Argument(...,
                                              help='Download comics to this directory.',
                                              file_okay=False,
                                              writable=True,
                                              resolve_path=True),
        from_date: str = typer.Option(dt_now, help='Download comics by name from date YYYY-MM-DD.',
                                      callback=is_valid_date),
        to_date: str = typer.Option(dt_now, help='Download comics by name to date YYYY-MM-DD.',
                                    callback=is_valid_date)
):
    """
    Download comic strips by TITLE. This automatically creates a folder by name
    and sub-folders by year and month. If options for from and to date are not passed,
    this downloads today's comic.
    """
    start_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')
    delta = datetime.timedelta(days=1)

    # TODO: Fix start_date > end_date bug

    date_iterator = DateIterator(start_date, end_date, delta)
    days = (end_date - start_date).days + 1

    with Progress() as progress:
        task = progress.add_task('[blue]Downloading...[/blue]', total=days)
        for date in date_iterator:
            formatted_date = datetime.datetime.strftime(date, '%Y-%m-%d')
            filename = FILENAME.format(title.lower(), formatted_date)

            # TODO: Cache titles

            download_path = create_dirs(title, title, str(path.absolute()), formatted_date)

            if save_title_for_date(title, download_path, formatted_date):
                progress.console.print('Downloaded file {}.'.format(filename))
            else:
                console.print('[red]Something went wrong trying to download [/red]')
            progress.update(task, advance=1)
