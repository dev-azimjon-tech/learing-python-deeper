def welcome(message):
    """Handles /start command"""
    return "👋 Hello! I'm a simple bot."


def echo(message):
    """Echo back text"""
    return f"You said: {message.text}"
