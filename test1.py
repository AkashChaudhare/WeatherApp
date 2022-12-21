import json
from tkinter import *
from turtle import back
from unittest import result
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
root.config(background="white")

def getWeather():
    city=textfield.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    result=TimezoneFinder().timezone_at(lng=location.longitude,lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="Current Weather")

    key='707278337ac337e58423a08d2d3b1464'
    #api=ffhttps://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

    api=f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={key}"
    json_data=requests.get(api).json()
    print(location.latitude,location.longitude)
    print("data is",json_data)

    condition=json_data['weather'][0]['main'] 
    temp=int(json_data['main']['temp']-273.15)
    

    wind=json_data['wind']['speed']
    humidity=json_data['main']['humidity']
    description=json_data['weather'][0]['description']
    pressure=json_data['main']['pressure']

    print(condition,temp,wind,humidity,description,pressure)
    
    t.config(text=f"{temp} °C")
    c.config(text=f"{condition} | feels like {int(json_data['main']['feels_like']-273.15)}")

    wind_val.config(text=wind)
    humidity_val.config(text=humidity)
    description_val.config(text=description)
    pressure_val.config(text=pressure)





#City Search
textfield=Entry(root, justify="center",width=18,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=100,y=25)
textfield.focus()


#Search button
search_icon=PhotoImage(file=r"Tkinter_Weather_App\magnifying-glass.png")
search_icon_button=Button(image=search_icon,borderwidth=0,cursor="hand2",command=getWeather)
search_icon_button.place(x=440,y=20)


#Weather Logo
w_logo=PhotoImage(file=r"Tkinter_Weather_App\cloudy.png")
logo=Label(image=w_logo,background="white")
logo.place(x=215,y=80)

#Name and Time
name=Label(root,bg="white",font=("poppins",15,"bold"))
name.place(x=30,y=120)
clock=Label(root,bg="white",font=("poppins",15))
clock.place(x=30,y=150)

#Condition
t=Label(text="...",font=("poppins",70,"bold"),bg="white")
t.place(x=550,y=130)
c=Label(text="...",font=("poppins",15,"bold"),bg="white")
c.place(x=550,y=230)

#Bottom box
bottom=Label(root,height=7,width=115,bg="#4794ff",border=0,fg="white")
bottom.place(x=50,y=360)


wind_title=Label(root,text="wind",font=("poppins",15,"bold"),fg="white",bg="#4794ff").place(x=120,y=370)
humidity_title=Label(root,text="humidity",font=("poppins",15,"bold"),fg="white",bg="#4794ff").place(x=300,y=370)
desciption_title=Label(root,text="desciption",font=("poppins",15,"bold"),fg="white",bg="#4794ff").place(x=520,y=370)
pressure_title=Label(root,text="pressure",font=("poppins",15,"bold"),fg="white",bg="#4794ff").place(x=725,y=370)

wind_val=Label(root,text="...",font=("poppins",15,"bold"),fg="black",bg="#4794ff")
wind_val.place(x=120,y=420)
humidity_val=Label(root,text="...",font=("poppins",15,"bold"),fg="black",bg="#4794ff")
humidity_val.place(x=315,y=420)
description_val=Label(root,text="...",font=("poppins",15,"bold"),fg="black",bg="#4794ff")
description_val.place(x=520,y=420)
pressure_val=Label(root,text="...",font=("poppins",15,"bold"),fg="black",bg="#4794ff")
pressure_val.place(x=725,y=420)




root.mainloop()











