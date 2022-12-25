import pathlib

import nestedtext
import typer


def main(path: pathlib.Path = pathlib.Path("../links/links.nt")):
    with open(path) as f:
        links = nestedtext.load(f, top="dict")
        typer.echo(links)
        typer.echo(links["Jenkins CI"]["url"])
    print("Hello World")


if __name__ == "__main__":
    typer.run(main)
