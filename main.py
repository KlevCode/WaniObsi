# App, mit dem Ziel Kanji-Radikale, Kanjis und Vokabeln aus WaniKani auszulesen und in Obsidian-Notes zu übertragen

import requests
import os
import json

API_KEY = 'Hier_Key'

# Basis-URL WaniKani-API
BASE_URL = 'https://api.wanikani.com/v2/subjects'

# Verzeichnis für Markdown-Dateien
OUTPUT_DIR = './WaniKani_Notes'

# Header mit dem API-Key für Authentifizierung
HEADERS = {
    'Authorization': f'Bearer {API_KEY}'
}
