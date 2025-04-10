# This is a simple weather app designed to introduce Tkinter
from tkinter import *
from weather import *

# Function to process a button click
# Will get the street address from the form and use it to get the lat/long
# Will use the lat/long to then retrieve the weather data
def clicked():
  # Get values from form field
  street = street_entry.get()
  zip = zip_entry.get()

  zip = sanitize_zip(zip)
  
  if validate_zip(zip):
    lat, long = get_lat_long(street, zip)
    result['text'] = get_temp(lat, long)  # update label text
  else:
    result['text'] = "Invalid zip"  # update label text

# Create window
window = Tk()
window.title("Weather App")
window.geometry("600x300")

# Create street label
hello = Label(text="Enter street address ")
hello.pack()

# Create street textfield
street_entry = Entry(window, width=20)
street_entry.pack()

# Create zip label
zip_label = Label(text="Enter zip code ")
zip_label.pack()

# Create zip textfield
zip_entry = Entry(window, width=10)
zip_entry.pack()

# Create button
#button = Button(text="Get Temperature") #, command=clicked)
button = Button(text="Get Temperature", command=clicked)
button.pack()

# Create placeholder for result
result = Label(text="")
result.pack()

window.mainloop()