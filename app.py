import streamlit as st 
from PIL import Image
st.set_page_config(layout="wide") # How the page content should be laid out. "wide" uses the entire screen.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.pyplot import figure

from Models.rider import Rider
from Models.lap import Lap
from Models.team import Team
from Models.motorcycle import Motorcycle

from functions import show_all_laps_time_bar_graph
from functions import show_specific_lap_bar_graph
from functions import show_specific_driver_bar_graph
from functions import show_laps_time_graph
from functions import space
from functions import addlabels

st.header("MotoGP Qatar race Analysis")

col1,col2, col3,col4 = st.columns([5, 1, 20, 6])
col5,col6, col7,col8 = st.columns([5, 1, 20, 6])
col9,col10, col11,col12 = st.columns([5, 1, 20, 6])
col13,col14, col15,col16 = st.columns([5, 1, 20, 6])
col17,col18, col19,col20 = st.columns([5, 1, 20, 6])
col21,col22,col23,col24 = st.columns([5, 1, 20, 6])
col25 = st.columns(1)

image = Image.open('images/drivers_1.png')
image2 = Image.open('images/drivers_2.png')
image3 = Image.open('images/drivers_3.png')
st.sidebar.image(image)
st.sidebar.image(image2)
st.sidebar.image(image3)

with col1:

    riders = [
        Rider('Bagnaia', 'Banjaja_Qatar.csv',image='images/bagnaia.jpg'),
        Rider('Binder', 'Binder.csv', image='images/binder.jpg'),
        Rider('Martin', 'Martin.csv',image='images/martin.jpg'),
        Rider('M.Marquez', 'M_Marquez.csv',image='images/m_marquez.jpg'),
        Rider('Bastianini', 'Bastianini.csv',image='images/bastianini.jpg'),
        Rider('A.Marquez', 'A_Marquez.csv',image='images/a_marquez.jpg'),
        Rider('Di Giannantonio', 'Didjantonio.csv',image='images/didgantonio.jpg'),
        Rider('A.Espargaro', 'A_Espargaro.csv',image='images/Espargaro.jpg'),
        Rider('Acosta', 'Acosta.csv',image='images/acosta.jpg'),
        Rider('Vinales', 'Vinales.csv',image='images/vinales.jpg'),
        Rider('Quartararo', 'Quartararo.csv',image='images/quartararo.jpg'),
        Rider('Zarco', 'Zarco.csv',image='images/zarco.jpg'),
        Rider('Mir', 'Mir.csv',image='images/mir.jpg'),
        Rider('Bezzecchi', 'Bezzecchi.csv',image='images/bezzecchi.jpg'),
        Rider('Oliveira', 'Oliveira.csv',image='images/oliveira.jpg'),
        Rider('Rins', 'Rins.csv',image='images/rins.jpg'),
        Rider('A.Fernandez', 'A_Fernandez.csv',image='images/a_fernandez.jpg'),
        Rider('Morbideli', 'Morbideli.csv',image='images/morbideli.jpg'),
        Rider('Nakagami', 'Nakagami.csv',image='images/nakagami.jpg'),
        Rider('Marini', 'Marini.csv',image='images/marini.jpg'),
        Rider('Miler', 'Miler.csv',image='images/miler.jpg'),
        Rider('R.Fernandez', 'R_Fernandez.csv',image='images/r_fernandez.jpg')
    ]
    space(6)
    st.markdown(
    """<style>
    div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] 
    > p {font-size: 24px;}
    </style>
    """, unsafe_allow_html=True)
    selected_rider = st.radio("Choose rider", riders, format_func=lambda x: x.name)

with col3:

    st.markdown("### :racing_motorcycle: Graph showing all laps of the chosen rider.The x-axis presents laps, and the y-axis presents time :racing_motorcycle:")
    space(1)
    show_all_laps_time_bar_graph(selected_rider.file_name, selected_rider.name)
    st.divider()

with col4:

    space(16)
    image = Image.open(selected_rider.image)
    new_image = image.resize((600, 625))
    st.image(new_image)
    space(8)
    st.divider()

with col5:
    
    laps = [
        Lap('1.lap', 'First_lap_time.csv'),
        Lap('2.lap', 'Second_lap_time.csv'),
        Lap('3.lap', 'Third_lap_time.csv'),
        Lap('4.lap', 'Fourth_lap_time.csv'),
        Lap('5.lap', 'Fifth_lap_time.csv'),
        Lap('6.lap', 'Sixth_lap_time.csv'),
        Lap('7.lap', 'Seventh_lap_time.csv'),
        Lap('8.lap', 'Eighth_lap_time.csv'),
        Lap('9.lap', 'Ninth_lap_time.csv'),
        Lap('10.lap', 'Tenth_lap_time.csv'),
        Lap('11.lap', 'Eleventh_lap_time.csv'),
        Lap('12.lap', 'Twelfth_lap_time.csv'),
        Lap('13.lap', 'Thirteenth_lap_time.csv'),
        Lap('14.lap', 'Fourteenth_lap_time.csv'),
        Lap('15.lap', 'Fifteenth_lap_time.csv'),
        Lap('16.lap', 'Sixteenth_lap_time.csv'),
        Lap('17.lap', 'Seventeenth_lap_time.csv'),
        Lap('18.lap', 'Eighteenth_lap_time.csv'),
        Lap('19.lap', 'Nineteenth_lap_time.csv'),
        Lap('20.lap', 'Twenty_lap_time.csv'),
        Lap('21.lap', 'Twenty_first_lap_time.csv')
    ]
    space(8)
    selected_lap = st.radio("Choose lap", laps, format_func=lambda x: x.lap_number)
    
with col7:

    st.markdown("### :racing_motorcycle: Graph showing the chosen lap for all riders. The x-axis presents the number of riders, and the y-axis presents time :racing_motorcycle:")
    space(1)
    show_specific_lap_bar_graph(selected_lap.file_name, selected_lap.lap_number)
    st.divider()

with col8:
  
    space(19)
    image = Image.open('images/motogp.jpg')
    st.image(image)
    space(13)
    st.divider()

with col9:
    
    space(15)
    is_best_lap_button_clicked = st.button("Best lap")
    with col11:
        if is_best_lap_button_clicked:
            show_laps_time_graph(file_name="Best lap.csv", graph_title="Best lap", y_min=110, y_max=115, y_step=0.5)
        
with col9:

    is_best_first_sector_button_clicked = st.button("Best 1. sector")
    with col11:
        if is_best_first_sector_button_clicked:
            show_laps_time_graph(file_name="Best first sector.csv", graph_title="Best 1. sector", y_min=27, y_max=28.5, y_step=0.1)
        
    is_best_second_sector_button_clicked = st.button("Best 2. sector")
    with col11:
        if is_best_second_sector_button_clicked:
            show_laps_time_graph(file_name="Best second sector.csv", graph_title="Best 2. sector", y_min=29, y_max=31, y_step=0.2)      

    is_best_third_sector_button_clicked = st.button("Best 3. sector")
    with col11:
        if is_best_third_sector_button_clicked:
            show_laps_time_graph(file_name="Best third sector.csv", graph_title="Best 3. sector", y_min=26, y_max=27.5, y_step=0.1)

    is_best_fourth_sector_button_clicked = st.button("Best 4. sector")
    with col11:
        if is_best_fourth_sector_button_clicked:
            show_laps_time_graph(file_name="Best fourth sector.csv", graph_title="Best 4. sector", y_min=27, y_max=28.5, y_step=0.1)
        
with col11:

    st.markdown("### :racing_motorcycle: Graph showing the best laps or the best of any of the 4 sectors of the race for all riders. The x-axis presents the riders, and the y-axis presents time :racing_motorcycle:")
    if is_best_lap_button_clicked==False and is_best_first_sector_button_clicked==False and is_best_second_sector_button_clicked==False and is_best_third_sector_button_clicked==False and is_best_fourth_sector_button_clicked==False:
        figure = plt.figure() 
        figure.set_size_inches(18.5, 10.5)
        st.pyplot(figure)
    st.divider()   

with col12:
        
        space(17)
        image = Image.open('images/qatar_sectors.jpg')
        st.image(image)
        space(12)
        st.divider()

teams = [
    
    Team('Ducati', 'Ducati.csv', [Rider(name='Bagnaia', number=1, motorcycle = 'Ducati GP24'), Rider(name='Bastianini', number=23, motorcycle = 'Ducati GP24')],'images/ducati.jpg'),
    
    Team('Aprilia', 'Aprilia.csv', [Rider(name='Aleix Espargaro', number=41, motorcycle = 'Aprilia GP24'), Rider(name='Maverick Vinales', number=12, motorcycle = 'Aprilia GP24')],'images/aprilia.jpg'),
    
    Team('Pramac', 'Pramac.csv', [Rider(name='Jorge Martin', number=89, motorcycle = 'Ducati GP24'), Rider(name='Franco Morbidelli', number=21, motorcycle = 'Ducati GP24')],'images/pramac.jpg'),
    
    Team('Honda', 'Honda.csv', [Rider(name='Joan Mir', number=36, motorcycle = 'RC213V'), Rider(name='Luca Marini', number=10, motorcycle = 'RC213V')],'images/honda.jpg'),
    
    Team('Yamaha', 'Yamaha.csv', [Rider(name='Fabio Quartararo', number=20, motorcycle = 'YZR-M1'), Rider(name='Alex Rins', number=42, motorcycle = 'YZR-M1')],'images/yamaha.jpg'),
    
    Team('LCR Honda', 'LCR Honda.csv', [Rider(name='Johann Zarco', number=5, motorcycle = 'RC213V'), Rider(name='Takaaki Nakagami', number=30, motorcycle = 'RC213V')],'images/lcr_honda.jpg'),
    
    Team('Trackhouse', 'Trackhouse.csv', [Rider(name='Miguel Oliveira', number=88, motorcycle = 'Aprilia GP24'), Rider(name='Raul Fernandez', number=25, motorcycle = 'Ducati GP23')],'images/trackhouse.jpg'),
    
    Team('GasGas', 'GasGas.csv', [Rider(name='Pedro Acosta', number=31, motorcycle = 'RC16'), Rider(name='Augusto Fernandez', number=37, motorcycle = 'RC16')],'images/gasgas.jpg'),
    
    Team('KTM', 'KTM.csv', [Rider(name='Brad Binder', number=33, motorcycle = 'RC16'), Rider(name='Jack Miller', number=43, motorcycle = 'RC16')],'images/ktm.jpg'),
    
    Team('VR46', 'VR46.csv', [Rider(name='Fabio Di Giannantonio', number=49, motorcycle = 'Ducati GP23'), Rider(name='Bezzecchi', number=72, motorcycle = 'Ducati GP23')],'images/vr46.jpg'),
    
    Team('Gresini', 'Gresini.csv', [Rider(name='Marc Marquez', number=93, motorcycle = 'Ducati GP23'), Rider(name='Alex Marquez', number=73, motorcycle = 'Ducati GP23')],'images/gresini.jpg')
]

with col13:
    
    space(12)
    selected_team = st.radio("Choose team", teams, format_func=lambda x: x.name)

with col15:
   
    st.markdown("### :racing_motorcycle: Graph where are compared times of riders of same team. On x-axis are presented laps and on y-axis is presented time :racing_motorcycle:")
    selected_riders = st.multiselect("Choose driver", selected_team.riders, format_func=lambda x: f"{x.number}-{x.name}")
    figure_team=plt.figure()
    
    for rider in selected_riders:
        show_specific_driver_bar_graph(selected_team.file_name, selected_team.name, rider.number,rider.name)

    figure_team.set_size_inches(18.5, 10.5)
    st.pyplot(figure_team)  
    st.divider()

with col16:

    space(20)
    image = Image.open(selected_team.image)
    new_image = image.resize((600, 625))
    st.image(new_image)
    space(8)
    st.divider()
    
motors = [
    
    Motorcycle('Ducati GP24', 'Ducati GP24.csv', [Rider(name='Bagnaia', number=1), Rider(name='Bastianini', number=23), Rider(name='Jorge Martin', number=89), Rider(name='Franco Morbidelli', number=21)],'images/ducati_gp24.jpg'),
    Motorcycle('Aprilia GP24', 'Aprilia GP24.csv', [Rider(name='Aleix Espargaro', number=41), Rider(name='Maverick Vinales', number=12),Rider(name='Miguel Oliveira', number=88)],'images/aprilia_gp24.jpg'),
    Motorcycle('Aprilia GP23', 'Aprilia GP23.csv', [Rider(name='Raul Fernandez', number=25)],'images/aprilia_gp23.jpg'),
    Motorcycle('Ducati GP23', 'Ducati GP23.csv', [Rider(name='Fabio Di Giannantonio', number=49), Rider(name='Bezzecchi', number=72), Rider(name='Marc Marquez', number=93), Rider(name='Alex Marquez', number=73)],'images/ducati_gp23.jpg'),
    Motorcycle('RC213V', 'RC213V.csv', [Rider(name='Joan Mir', number=36), Rider(name='Luca Marini', number=10), Rider(name='Johann Zarco', number=5), Rider(name='Takaaki Nakagami', number=30)],'images/rc213v.jpg'),
    Motorcycle('YZR-M1', 'YZR-M1.csv', [Rider(name='Fabio Quartararo', number=20), Rider(name='Alex Rins', number=42)],'images/yzr-m1.jpg'),
    Motorcycle('RC16', 'RC16.csv', [Rider(name='Pedro Acosta', number=31), Rider(name='Augusto Fernandez', number=37), Rider(name='Brad Binder', number=33), Rider(name='Jack Miller', number=43)],'images/rc16.jpg')
]

with col17:

    space(15)
    selected_motorcycle = st.radio("Choose motorcycle", motors, format_func=lambda x: x.name)

with col19:

    st.markdown("### :racing_motorcycle: Graph where are compared times of riders which have same motorcycle.  On x-axis are presented laps and on y-axis is presented time :racing_motorcycle:")
    selected_riders = st.multiselect("Choose drivers", selected_motorcycle.riders, format_func=lambda x: f"{x.number}-{x.name}")
    figure_motorcycle=plt.figure()
   
    for rider in selected_riders:
        show_specific_driver_bar_graph(selected_motorcycle.file_name, selected_motorcycle.name, rider.number,rider.name)

    figure_motorcycle.set_size_inches(18.5, 10.5)
    st.pyplot(figure_motorcycle) 
    st.divider()

with col20:
    
    space(20)
    selected_motorcycle_image = Image.open(selected_motorcycle.image)
    selected_motorcycle_image_resize = image.resize((600, 625))
    st.image(selected_motorcycle_image_resize)
    space(8)
    st.divider()

with col21:
    
    space(16)
    is_button6_clicked = st.button("Best lap", key=1)
    with col23:
        if is_button6_clicked:
            show_laps_time_graph(file_name="Bike-min-lap.csv", graph_title="Best lap - motorcycle", x_min = 0, x_max = 7, y_min=111.6, y_max=114, y_step=0.2, x_column ='bike',font_size=16)

    is_button7_clicked = st.button("Best 1. sector", key=2)
    with col23:
        if is_button7_clicked:
            show_laps_time_graph(file_name="min_t1_bike.csv", graph_title="Best 1. sector  - motorcycle", x_min = 0, x_max = 7, y_min=27, y_max=28, y_step=0.1,y_column='min_t1', x_column ='bike',font_size=16)

    is_button8_clicked = st.button("Best 2. sector", key=3)
    with col23:
        if is_button8_clicked:
            show_laps_time_graph(file_name="min_t2_bike.csv", graph_title="Best 2. sector  - motorcycle", x_min = 0, x_max = 7, y_min=29.5, y_max=31, y_step=0.1,y_column='min_t2', x_column ='bike',font_size=16)

    is_button9_clicked = st.button("Best 3. sector", key=4)
    with col23:
        if is_button9_clicked:
            show_laps_time_graph(file_name="min_t3_bike.csv", graph_title="Best 3. sector  - motorcycle", x_min = 0, x_max = 7, y_min=26, y_max=27.5, y_step=0.1,y_column='min_t3', x_column ='bike',font_size=16)

    is_button10_clicked = st.button("Best 4. sector", key=5)
    with col23:
        if is_button10_clicked:
            show_laps_time_graph(file_name="min_t4_bike.csv", graph_title="Best 4. sector  - motorcycle", x_min = 0, x_max = 7, y_min=27, y_max=28, y_step=0.1,y_column='min_t4', x_column ='bike',font_size=16)

    is_button11_clicked = st.button("Maximum average speed")
    with col23:
        if is_button11_clicked:
            max_speed = pd.read_csv(r"data/max_avg_speed.csv")
            df = max_speed.sort_values('max_avg_speed', ascending=False)
            figure_speed = plt.figure()
            max=df['max_avg_speed']
            bike=df['bike']
            plt.ylim(355,358)
            addlabels(bike,max,16)
            figure_speed.set_size_inches(18.5, 10.5)
            plt.bar(bike,max,width = 0.5)
            st.pyplot(figure_speed)

with col23:

    st.markdown("### :racing_motorcycle: Graph showing best laps, best of any of the 4 sectors of the race or maximum average speed for all motorcycles.   On x-axis are presented motorcycles and on y-axis is presented time or maximum average speed :racing_motorcycle:")

    if is_button6_clicked==False and is_button7_clicked==False and is_button8_clicked==False and is_button9_clicked==False and is_button10_clicked==False and is_button11_clicked==False:
        figure_empty = plt.figure() 
        figure_empty.set_size_inches(18.5, 10.5)
        st.pyplot(figure_empty)
    space(1) 
    st.divider()

with col24:
        
        space(20)
        image = Image.open('images/qatar_sectors.jpg')
        st.image(image)
        space(12)
        st.divider()

st.markdown("### :racing_motorcycle: On x-axis are presented all riders and on y-axis are presented number of laps which belongs to intervals :racing_motorcycle:")

space(3)
a = pd.read_csv(r"data/intervals_lap.csv")

intervals = a.sort_values(['<113','113<113.5','113.5<114','114<114.5','114.5<115','115<115.5','>115.5'], ascending=False)

x=intervals['num']
x_values = np.arange(len(x))
y1=intervals['<113']
y2=intervals['113<113.5']
y3=intervals['113.5<114']
y4=intervals['114<114.5']
y5=intervals['114.5<115']
y6=intervals['115<115.5']
y7=intervals['>115.5']
figure_interval = plt.figure()
plt.yticks(ticks=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22], labels=None, minor=False)
plt.xlim(0,24)
plt.xlim(left=-1)
plt.ylim(0,22)
plt.bar(x_values, y1, color='darkgreen',width=0.5,label='1\'53\"')
plt.bar(x_values, y2, bottom=y1, color='mediumseagreen',width=0.5,label='1\'53\"<1\'53.5\"')
plt.bar(x_values, y3, bottom=y1+y2, color='palegreen',width=0.5,label='1\'53.5\"<1\'54\"')
plt.bar(x_values, y4, bottom=y1+y2+y3, color='yellow',width=0.5,label='1\'54\"<1\'54.5\"')
plt.bar(x_values, y5, bottom=y1+y2+y3+y4, color='orange',width=0.5,label='1\'54.5\"<1\'55\"')
plt.bar(x_values, y6, bottom=y1+y2+y3+y4+y5, color='orangered',width=0.5,label='1\'55\"<1\'55.5\"')
plt.bar(x_values, y7, bottom=y1+y2+y3+y4+y5+y6, color='darkred',width=0.5,label='>1\'55.5\"')
plt.legend()    
plt.xticks(x_values,x)
figure_interval.set_size_inches(18.5, 9)
st.pyplot(figure_interval)
    


