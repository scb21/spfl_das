# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 01:33:04 2025

@author: sbuch
"""

import csv
import re

# Copy and paste the fixture data into a multi-line string (replace with your actual data)
fixtures = """
Matchday one

03/08/2024 Heart of Midlothian v Rangers 12:30 Sky Sports
03/08/2024 Motherwell v Ross County 15:00
04/08/2024 Celtic v Kilmarnock 16:30 Sky Sports
04/08/2024 Dundee United v Dundee 13:30 Sky Sports
04/08/2024 St. Mirren v Hibernian 15:00
05/08/2024 St. Johnstone v Aberdeen 20:00 Sky Sports
"""

# Split the data into lines and remove the "Matchday" lines
lines = [line.strip() for line in fixtures.strip().split("\n") if not line.startswith("Matchday")]

# Open a CSV file for writing
with open(r"C:\Users\sbuch\Desktop\spfl\data\fixtures.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(["Date", "Home Team", "Away Team", "Time", "Broadcast"])

    # Regex pattern to extract date, teams, time, and broadcast information
    pattern = r"(\d{2}/\d{2}/\d{4})\s+([A-Za-z\s]+) v ([A-Za-z\s]+)\s+(\d{2}:\d{2})\s*(.*)"

    # Process each line to extract relevant data
    for line in lines:
        match = re.match(pattern, line)
        if match:
            date, home_team, away_team, time, broadcast = match.groups()
            broadcast = broadcast if broadcast else "N/A"  # Handle missing broadcast
            writer.writerow([date, home_team.strip(), away_team.strip(), time, broadcast])

print("CSV file 'fixtures.csv' has been created.")
