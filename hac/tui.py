from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Footer, Header, Static


class Post(Static):
    """
    A widget to display a post from HN.
    """

    def compose(self) -> ComposeResult:
        """
        Create child widgets for the widget.
        """

        yield Container(
            Container(
                Static(
                    "The Turbo Encabulator's long, weird and funny history",
                    classes="post__title",
                ),
                Static(
                    "↑6 by dmarchand90 34 minutes ago, 19 comments",
                    classes="post__description",
                ),
                classes="post__header",
            ),
            Button("Open", classes="post__btn"),
            classes="post",
        )


class HacApp(App):
    """
    A Textual app to watch, save and manage HackerNews news.
    """

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """
        Create child widgets for the App.
        """

        yield Header(name="Hac", classes="header")
        yield Footer()
        yield Container(*[Post() for i in range(5)], classes="posts")
