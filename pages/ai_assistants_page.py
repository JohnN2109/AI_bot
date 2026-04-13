from playwright.sync_api import Page, expect

class AIAssistantsPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_page(self):
        self.page.goto("https://app.smartsupp.com/app/dashboard/ai-automations/ai-chatbots")       
        
        try:
            self.page.click("text=ALLOW ALL", timeout=5000)
        except Exception:
            pass
        expect(self.page.locator("h1")).to_have_text("AI Asistenti")


    def click_add_new(self):
        self.page.locator("button:has-text('Přidat')").click()

    def create_bot(self, name="test-bot"):
        self.page.wait_for_selector("text=Způsob komunikace")

        name_field = self.page.locator("text=Název projektu").locator("xpath=following-sibling::*[1]")
        name_field.click()

        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Backspace")
        self.page.keyboard.type(name)
        self.page.click("button:has-text('Pokračovat')")
        
        self.page.wait_for_selector("text=Znalosti")
        self.page.click("button:has-text('Pokračovat')")

        self.page.wait_for_selector("text=Nevytvořili jste zdroj znalostí")
        self.page.locator("button:has-text('Pokračovat')").last.click()

        self.page.wait_for_selector("text=Uvítací zpráva")
        self.page.click("button:has-text('Pokračovat')")

        self.page.wait_for_selector("text=Dovednosti")
        self.page.click("button:has-text('Pokračovat')")

        self.page.wait_for_selector("text=Náhled a publikování")    
        self.page.click("text=Vytvořit zdroj")
        self.page.click("text=Stáhnout informace z webu")
        self.page.locator("button:has-text('Pokračovat')").last.click()
        self.page.wait_for_selector("text=Jak chcete načíst informace?")
        self.page.locator("button:has-text('Pokračovat')").last.click()

        self.page.wait_for_selector("text=Detail zdroje")
        self.page.wait_for_selector("input[placeholder*='mywebsite']")
        self.page.fill("input[placeholder*='mywebsite']", "example.com")
        self.page.click("button:has-text('Načíst stránky')")
        self.page.locator("button:has-text('Pokračovat')").last.click()
        self.page.wait_for_selector("text=Aktualizace")
        self.page.locator("button:has-text('Uložit')").last.click()

        self.page.wait_for_selector("text=Zdroje znalostí")
        self.page.locator("input[type='checkbox']").last.check(force=True)
        self.page.locator("button:has-text('Pokračovat')").last.click()

        self.page.wait_for_selector("text=Uvítací zpráva")
        self.page.locator("button:has-text('Pokračovat')").last.click()

        self.page.wait_for_selector("text=Dovednosti")
        self.page.locator("button:has-text('Pokračovat')").last.click()

        self.page.wait_for_selector("text=Náhled a publikování")
        # self.page.wait_for_selector("text=Náhled a publikování")
        #self.page.click("button:has-text('Publikovat')")
        #self.page.wait_for_selector("text=Ještě zbývá dokončit instalaci")
        #self.page.click("button:has-text('I přesto publikovat')")
        #self.page.wait_for_timeout(2000)

