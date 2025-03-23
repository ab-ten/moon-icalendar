import datetime
from datetime import timedelta

# Reference date for moon age calculation
REFERENCE_DATE = datetime.datetime(2025, 3, 29, 20, 0, 0)
SYNODIC_MONTH = 29.53058867  # Average length of a synodic month in days
FULL_MOON_AGE = 14.77
MOON_PHASE_RANGE = 0.75

def moon_age_on_date(date):
  """
  Calculate the moon age on a given date.
  Uses noon time on the given date for precise calculation.
  """
  # Create a new datetime object with noon time (12:00) for the given date
  if isinstance(date, datetime.datetime):
    noon_date = datetime.datetime(date.year, date.month, date.day, 12, 0, 0)
  else:  # If it's a date object
    noon_date = datetime.datetime(date.year, date.month, date.day, 12, 0, 0)

  delta = noon_date - REFERENCE_DATE
  age = (delta.total_seconds() / 86400) % SYNODIC_MONTH
  return age

def is_new_moon(date):
  """Determine if the given date is a new moon."""
  age = moon_age_on_date(date)
  return age < MOON_PHASE_RANGE or age > SYNODIC_MONTH - MOON_PHASE_RANGE

def is_full_moon(date):
  """Determine if the given date is a full moon."""
  age = moon_age_on_date(date)
  return FULL_MOON_AGE - MOON_PHASE_RANGE <= age <= FULL_MOON_AGE + MOON_PHASE_RANGE

def generate_icalendar_with_moon_age(events, filename="moon_phases_with_moon_age.ics"):
  """Generate an iCalendar file directly with the provided events."""
  with open(filename, "w", encoding="utf-8") as file:
    file.write("BEGIN:VCALENDAR\n")
    file.write("VERSION:2.0\n")
    file.write("PRODID:-//ab-ten//Moon iCalendar//JP\n")
    for event_date, event_name, moon_age in events:
      # 小数点第2位で四捨五入して0.1単位で表示
      rounded_moon_age = round(moon_age * 10) / 10
      file.write("BEGIN:VEVENT\n")
      file.write(f"SUMMARY:{event_name} (月齢: {rounded_moon_age:.1f})\n")
      file.write(f"DTSTART;VALUE=DATE:{event_date.strftime('%Y%m%d')}\n")
      file.write(f"DTEND;VALUE=DATE:{(event_date + timedelta(days=1)).strftime('%Y%m%d')}\n")
      file.write("TRANSP:TRANSPARENT\n")
      file.write("END:VEVENT\n")
    file.write("END:VCALENDAR\n")

def generate_moon_calendar(year):
  """Generate an iCalendar file for the specified year with new moon and full moon events."""
  start_date = datetime.datetime(year, 1, 1)
  end_date = datetime.datetime(year, 12, 31, 23, 59, 59)
  current_date = start_date

  events = []

  while current_date <= end_date:
    if is_new_moon(current_date):
      age = moon_age_on_date(current_date)
      events.append((current_date, "新月", age))
    elif is_full_moon(current_date):
      age = moon_age_on_date(current_date)
      events.append((current_date, "満月", age))
    current_date += datetime.timedelta(days=1)

  generate_icalendar_with_moon_age(events, f'moon_phases_{year}.ics')

if __name__ == "__main__":
  import sys
  if len(sys.argv) != 2:
    print("Usage: python moon-icalendar-gen.py <year>")
    sys.exit(1)
  year = int(sys.argv[1])
  generate_moon_calendar(year)
