# Moon Phase Calendar Generator

[日本語版](./README.md)

## 📝 Overview

This project is a Python script that calculates new moon and full moon dates for a specified year and generates a calendar file in iCalendar format (.ics). The generated file can be imported into major calendar applications such as Google Calendar and Apple Calendar.

## 🌝 Features

- Display new moons and full moons for the specified year in your calendar
- Accurately calculate and display moon age (to the first decimal place)
- Output in iCalendar format for compatibility with various calendar applications

## 🚀 How to Use

1. Ensure Python is installed
2. Run from the command line as follows:

```bash
python moon-icalendar-gen.py <year>
```

For example, to generate a moon phase calendar for 2025:

```bash
python moon-icalendar-gen.py 2025
```

This will generate a file called `moon_phases_2025.ics`.

## 💻 Implementation Details

This script uses the following calculation methods:

- Calculates moon age based on the number of days elapsed from the reference date (March 29, 2025)
- The cycle of the moon phases (synodic month) is 29.53058867 days on average
- A full moon occurs at approximately moon age 14.77
- A range of ±0.75 days is used to determine new moons and full moons
- The moon age displayed is calculated at noon of each day

## 📅 Output Example

In the generated iCalendar file, events are named "新月" (new moon) or "満月" (full moon) with the moon age at noon of that day shown in parentheses. For example:
- 新月 (月齢: 0.0)
- 満月 (月齢: 14.8)

Note that when a full moon or new moon appears on a single day in the calendar, the moon is closest to the exact phase around noon of that day. If it appears on two consecutive days, the actual full moon or new moon is closest to occur around midnight between those two days.

## 🙏 Acknowledgements

This README was created using GitHub Copilot Chat Agent! In particular, the custom instructions were inspired by the article "[Pair programming with a Gyaru was unexpectedly fun (VSCode custom instructions)](https://qiita.com/bonanza-olaf/items/5453fc0e3ad1c8f9f971)", which helped make the explanations more friendly and enjoyable. Using AI collaboration for documentation has been super convenient!

## 📄 License

Released under the MIT License. See the [LICENSE](./LICENSE) file for details.