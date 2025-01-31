from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=0518339bce3ea5b41cf4f75f34f65600").json()
    wc_label_1.config(text=data["weather"][0]["main"])
    wd_label_2.config(text=data["weather"][0]["description"])
    temp_label_3.config(text=str(int(data["main"]["temp"]-273.15)))
    pre_label_4.config(text=data["main"]["pressure"])

win= Tk()
win.title("Atharva's Weather App ")
win.config(bg="sky blue")
win.geometry("500x570")

# for title
name_label=Label(win,text="Climate Tracker",font=("Times New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

# for combobox
city_name=StringVar()
list_name=("Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry")
com=ttk.Combobox(win,values=list_name,font=("Times New Roman",15,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

# #for button
# done_botton=Button(win,text="Done",font=("Times New Roman",15,"bold"))
# done_botton.place(y=190,height=50,width=100,x=200)

#for weather climate
wc_label=Label(win,text="Weather Climate",font=("Times New Roman",15))
wc_label.place(x=25,y=260,height=50,width=210)

wc_label_1=Label(win,text="",font=("Times New Roman",15))
wc_label_1.place(x=250,y=260,height=50,width=210)
# for Weather Discription
wd_label=Label(win,text="Weather Discrption",font=("Times New Roman",15))
wd_label.place(x=25,y=330,height=50,width=210)

wd_label_2=Label(win,text="",font=("Times New Roman",15))
wd_label_2.place(x=250,y=330,height=50,width=210)
# for Temperature
temp_label=Label(win,text="Temperature",font=("Times New Roman",15))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label_3=Label(win,text="",font=("Times New Roman",15))
temp_label_3.place(x=250,y=400,height=50,width=210)
#for Pressure
pre_label=Label(win,text="Pressure",font=("Times New Roman",15))
pre_label.place(x=25,y=470,height=50,width=210)

pre_label_4=Label(win,text="",font=("Times New Roman",15))
pre_label_4.place(x=250,y=470,height=50,width=210)

#for button
done_botton=Button(win,text="Done",font=("Times New Roman",15,"bold"),command=data_get)
done_botton.place(y=190,height=50,width=100,x=200)


win.mainloop()