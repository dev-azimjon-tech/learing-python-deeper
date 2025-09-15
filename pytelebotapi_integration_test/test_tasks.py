from tasks import *
import types

class FakeMsg:
    def __init__(self, text):
        self.text = text
        self.chat = types.SimpleNamespace(chat_id=12)


def test_welcome():
    msg = FakeMsg("/start")
    response = welcome(msg)
    assert response == "👋 Hello! I'm a simple bot."


def test_echo():
    msg = FakeMsg("hi")
    response = echo(msg)
    assert response == "You said: hi"


def test_help():
    msg = FakeMsg("/help")
    response = help_command(msg)
    assert response == "Available commands: /start, /help"
