import types
from main import bot, send_welc, echo

class FakeMessage:
    def __init__(self, text, chat_id=10):
        self.text = text
        self.chat = types.SimpleNamespace(id=chat_id)

    def test_start_command():
        msg = FakeMessage("/start")
        response = send_welc(msg)
        assert response is None

    def test_echo_msg():
        msg = FakeMessage("Hello Bot")
        response = echo(msg)
        assert response is None