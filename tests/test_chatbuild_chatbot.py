import pytest
from playwright.sync_api import Page

BASE_URL = "https://www.chatbuild.io/demo"


def open_chat_widget(page: Page):
    """Open the chatbot widget by clicking the 'Ask AI' button."""
    page.get_by_role("button", name="Ask AI").click()


def send_message(page: Page, text: str):
    """Type a message into the chatbot input and send it."""
    textbox = page.get_by_placeholder("👋 Enter Your Name To Begin...")
    textbox.click()
    textbox.fill(text)
    textbox.press("Enter")


def get_last_bot_message(page: Page) -> str:
    """Get a bot reply text."""
    # Wait for the bot to respond
    page.wait_for_timeout(4000)

    bot_message = page.get_by_text("Hello! How can I help you?")
    # If there are multiple matches, get the last one
    last_text = bot_message.nth(bot_message.count() - 1).inner_text()
    return last_text.strip()


def basic_sanity_checks(bot_reply: str):
    """Basic validation on the bot reply."""
    assert bot_reply, "Bot reply is empty."
    lowered = bot_reply.lower()
    assert "error" not in lowered, "Bot returned an error message."
    assert "404" not in lowered, "Bot reply looks like a server error."


@pytest.mark.parametrize(
    "message",
    [
        "What can this chatbot do?",
        "What is ChatBuild?",
        "What's your favorite movie?",
    ],
)
def test_chatbuild_chatbot(message: str, page: Page):
    page.goto(BASE_URL)

    open_chat_widget(page)

    send_message(page, message)

    bot_reply = get_last_bot_message(page)

    basic_sanity_checks(bot_reply)
