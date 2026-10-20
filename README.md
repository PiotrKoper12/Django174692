# EventHub

Platforma do zarządzania wydarzeniami (konferencjami, warsztatami, koncertami) oraz rezerwacji biletów.
Projekt referencyjny realizowany w ramach przedmiotu **Aplikacje WWW (semestr 2026Z)**.

## Technologie

- Python 3.13+
- Django 6.1.*
- SQLite 3

## Uruchomienie projektu

1. Sklonuj repozytorium:

   ```bash
   git clone https://github.com/PiotrKoper12/Django174692.git
   cd Django174692
   ```

2. Utwórz i aktywuj środowisko wirtualne:

   ```bash
   python -m venv .venv
   ```

   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
   - Windows (cmd): `.venv\Scripts\activate.bat`
   - macOS / Linux: `source .venv/bin/activate`

3. Zainstaluj zależności:

   ```bash
   pip install -r requirements.txt
   ```

4. Wykonaj migracje i utwórz konto administratora:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Uruchom serwer deweloperski:

   ```bash
   python manage.py runserver
   ```

## Dostępne adresy

| Adres | Opis |
|---|---|
| http://127.0.0.1:8000/events/ | Strona powitalna |
| http://127.0.0.1:8000/events/about/ | Opis platformy |
| http://127.0.0.1:8000/admin/ | Panel administracyjny Django |

## Struktura projektu

```
eventhub/        # konfiguracja projektu (settings, routing główny)
events/          # aplikacja wydarzeń: modele Category i Event, admin, widoki
  orm_queries.py # przykładowe zapytania QuerySet (Lab 2)
manage.py
requirements.txt
```

Zapytania z `orm_queries.py` można uruchomić poleceniem:

```bash
python manage.py shell < events/orm_queries.py
```
