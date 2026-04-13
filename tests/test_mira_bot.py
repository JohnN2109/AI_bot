
from playwright.sync_api import sync_playwright
from pages.ai_assistants_page import AIAssistantsPage
from pages.bot_detail_page import BotDetailPage

def test_mira_bot_lifecycle():
    with sync_playwright() as p:
        
        context = p.chromium.launch_persistent_context(
             user_data_dir="user_data",
             headless=False,
             slow_mo=5000)
        page = context.new_page()

        ai_page = AIAssistantsPage(page)
        bot_page = BotDetailPage(page)

        ai_page.go_to_page()
        ai_page.click_add_new()
        ai_page.create_bot("test-bot")

        bot_page.edit_bot()
        bot_page.publish_bot()
        bot_page.delete_bot()
        context.close()