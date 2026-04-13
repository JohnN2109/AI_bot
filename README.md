# AI_bot

# QA automatizačný test – AI chatbot lifecycle

Tento projekt obsahuje automatizovaný test pre overenie životného cyklu AI chatbota pomocou Playwright (Python).

## Použité technológie

- Python
- Playwright
- Pytest
- Page Object Model (POM)

---

## Testovaný scenár

Test pokrýva celý lifecycle AI chatbota:

1. **Create**
   - vytvorenie nového AI chatbota
   - zadanie názvu
   - pridanie knowledge source (example.com)

2. **Edit**
   - úprava správania (3 slidery)
   - prepnutie na vlastnú uvítaciu správu
   - zmena textu uvítacej správy

3. **Publish**
   - publikovanie chatbota

4. **Delete**
   - zmazanie chatbota

---

## Štruktúra projektu


AI bot/
│
├── pages/
│ ├── ai_assistants_page.py
│ ├── bot_detail_page.py
│ └── init.py
│
├── tests/
│ ├── test_mira_bot.py
│ └── init.py
│
├── requirements.txt
├── README.md


---

## Inštalácia

1. Vytvor virtuálne prostredie:
python -m venv .venv


2. Aktivuj prostredie:

Windows:.venv\Scripts\activate


3. Nainštaluj závislosti:
pip install -r requirements.txt


4. Nainštaluj Playwright prehliadače:
python -m playwright install


---

## Spustenie testu

pytest -s --cache-clear

---

## Poznámky

- Test využíva persistentný browser (`user_data`) pre zachovanie session (login).
- Použitý je Page Object Model pre lepšiu organizáciu kódu.
- Selektory boli prispôsobené dynamickému UI (napr. Chakra UI komponenty).
- Slidery sú ovládané pomocou kláves (`ArrowRight`, `ArrowLeft`), keďže nejde o klasické inputy.

---

## Autor

Ján Niščák
