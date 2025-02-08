#!/bin/bash

# Remove the specific cron job
crontab -l | grep -v "/home/ubuntu/WeatherApp/main.py" | crontab -

# Log the removal action
echo "Cron job for WeatherApp disabled on $(date)" >> /home/ubuntu/WeatherApp/cron_removal.log