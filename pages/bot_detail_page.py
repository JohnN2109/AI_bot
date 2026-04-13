from playwright.sync_api import Page

class BotDetailPage:
    def __init__(self, page: Page):
        self.page = page

    def edit_bot(self): 
               
        self.page.get_by_text("Chování").click()
        self.page.wait_for_selector("text=Způsob komunikace")

        sliders = self.page.locator("[role='slider']")
        sliders.nth(0).click()
        sliders.nth(0).press("ArrowRight")
        sliders.nth(0).press("ArrowRight")

        sliders.nth(1).click()
        sliders.nth(1).press("ArrowLeft")
        sliders.nth(1).press("ArrowLeft")

        sliders.nth(2).click()
        sliders.nth(2).press("ArrowRight")


        self.page.get_by_text("Uvítací zpráva").click()
        self.page.wait_for_timeout(1000)

        custom_card = self.page.get_by_role("button", 
                 name="Vlastní uvítací zpráva",
                 exact=False).first
        custom_card.scroll_into_view_if_needed()
        custom_card.click()
        
        self.page.mouse.wheel(0, 1200)
        self.page.wait_for_selector("textarea")
        self.page.locator("textarea").first.fill("Vitajte. Rád vás prevediem našou ponukou a pomôžem vám nájsť to, čo hľadáte.")
        self.page.get_by_role("button", name="Pokračovat").click()
        
    def publish_bot(self):
        self.page.wait_for_selector("text=Náhled a publikování")
        self.page.get_by_role("button", name="Publikovat").click()

        self.page.wait_for_selector("text=Ještě zbývá dokončit instalaci")
        self.page.get_by_role("button", name="I přesto publikovat").click()
        self.page.wait_for_timeout(2000)
        
    def delete_bot(self):
        self.page.get_by_test_id("chatbot-builder-dropdown-toggler").click()
        self.page.get_by_role("menuitem", name="Smazat").click()
        self.page.wait_for_selector("text=Smazat chatbota")
        self.page.get_by_role("button", name="Smazat").last.click()