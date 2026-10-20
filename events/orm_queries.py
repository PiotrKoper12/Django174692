"""
Zapytania QuerySet do Lab 2.

Uruchomienie:
    python manage.py shell < events/orm_queries.py
"""
from decimal import Decimal

from events.models import Event

# 1. Wszystkie opublikowane wydarzenia posortowane chronologicznie
print("=== Opublikowane wydarzenia (chronologicznie) ===")
published_events = Event.objects.filter(is_published=True).order_by('date')
for event in published_events:
    print(event)

# 2. Wydarzenia z limitem miejsc co najmniej 50 osób
print("\n=== Wydarzenia z limitem miejsc >= 50 ===")
large_events = Event.objects.filter(capacity__gte=50)
for event in large_events:
    print(f"{event.title} - {event.capacity} miejsc")

# 3. Łączna liczba darmowych wydarzeń
free_count = Event.objects.filter(price=Decimal('0.00')).count()
print(f"\n=== Liczba darmowych wydarzeń: {free_count} ===")

# 4. Zmiana statusu is_published wybranego wydarzenia z True na False
print("\n=== Ukrycie wydarzenia ===")
event = Event.objects.filter(is_published=True).first()
if event:
    event.is_published = False
    event.save()
    print(f"Wydarzenie '{event.title}' ma teraz is_published={event.is_published}")
else:
    print("Brak opublikowanych wydarzeń do zmiany.")
