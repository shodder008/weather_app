import requests  # need to make web requests
import json      # needed to work with the data that is returned
import re        # needed to check zip code

# Converts street and zip to lat and long
def get_lat_long(street, zip):
  response = requests.get(
      f"https://geocoding.geo.census.gov/geocoder/locations/address?street={street}&zip={zip}&benchmark=2020&format=json"
  )
  long = response.json()['result']['addressMatches'][0]['coordinates']['x']
  lat = response.json()['result']['addressMatches'][0]['coordinates']['y']
  return f"{lat:.2f}", f"{long:.2f}"

# Gets temp from lat and long
def get_temp(lat, long):
  response = requests.get(
      f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m&temperature_unit=fahrenheit'
  )
  return response.json()['current']['temperature_2m']

# Sanitizes zip code
def sanitize_zip(zip):
  # Declaring a list
  permitted_characters=[]
  
  # Iterate over the string 
  for a_character in zip:
    if a_character.isdigit():
      permitted_characters.append(a_character)
  # Join the elements in the list to create a string
  zip="".join(permitted_characters)
  return zip

# Validates zip code
def validate_zip(zip):
  pattern = r"^\d{5}(-\d{4})?$"
  if re.match(pattern, zip):
    return True
  else:
    return False
