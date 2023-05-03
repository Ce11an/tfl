"""A subclass of typer.Typer that allows async functions to be used as commands."""

import asyncio
import functools

import typer

__all__ = ["AsyncTyper"]


class AsyncTyper(typer.Typer):
    """A subclass of typer.Typer that allows async functions to be used as commands.

    Special thanks to @gpkc for the original implementation:
    https://github.com/tiangolo/typer/issues/88#issuecomment-1478432421

    Examples:
        >>> import asyncio
        >>> import typer
        >>>
        >>> app = AsyncTyper()
        >>>
        >>>> @app.async_command()
        >>>> async def hello() -> None:
        >>>>     await asyncio.sleep(1)
        >>>>     typer.echo(f"Hello!")
        >>>
        >>> if __name__ == "__main__":
        >>>     app()
    """

    def async_command(self, *args, **kwargs):
        """Decorator to register an async function as a typer command."""

        def decorator(async_func):
            """Decorator to register an async function as a typer command."""

            @functools.wraps(async_func)
            def sync_func(*_args, **_kwargs):
                """Wrapper to run an async function in a synchronous context."""
                return asyncio.run(async_func(*_args, **_kwargs))

            self.command(*args, **kwargs)(sync_func)
            return async_func

        return decorator
