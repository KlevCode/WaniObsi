# App, mit dem Ziel Kanji-Radikale, Kanjis und Vokabeln aus WaniKani auszulesen und in Obsidian-Notes zu übertragen

import requests
import os
import json

API_KEY = 'API_KEY_HIER'

# Basis-URL WaniKani-API
BASE_URL = 'https://api.wanikani.com/v2/subjects'

# Verzeichnis für Markdown-Dateien
OUTPUT_DIR = './WaniKani_Notes'

# Header mit dem API-Key für Authentifizierung
HEADERS = {
    'Authorization': f'Bearer {API_KEY}'
}

# Funktion, um Kanji-Radikale, Kanji und Vokabeln abzurufen
def get_subjects():
    subjects = []
    url = BASE_URL
    while url:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()           # Umwandlung der JSON-Dateien in Dictionaries
            subjects.extend(data['data'])
            url = data['pages']['next_url']  # Weiter zur nächsten Seite, falls vorhanden
        else:
            print(f"Fehler beim Abrufen der Daten: {response.status_code}")
            break
    return subjects
