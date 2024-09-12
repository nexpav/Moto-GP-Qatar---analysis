import streamlit as st

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def minutes_seconds(a:int,b:int):
        return f'{int(a//60)}\'{round(a%60,b)}\"'

def show_all_laps_time_bar_graph(file_name: str, graph_title: str):
    plt.style.use('ggplot')
    data = pd.read_csv(r'data/' + file_name)
    column_lap_seconds=data['Lap_seconds']
    column_lap=data['Lap']
    figure = plt.figure() 
    plt.title(label=graph_title)
    x_ticks = np.arange(len(column_lap)+2)
    plt.xticks(ticks=x_ticks, labels=None, minor=False)
    plt.yticks(ticks=[0,113,113.5,114,114.5,115,115.5,116], labels=[0,"1\'53\"","1\'53.5\"","1\'54\"","1\'54.5\"","1\'55\"","1\'55.5\"","1\'56\""], minor=False)
    plt.xlim(0,22)
    plt.ylim(112,116)
    plt.bar(column_lap,column_lap_seconds,width = 0.5)
    for i in range(len(column_lap)):
        if column_lap_seconds[i]<=116:
            plt.text(i+1,column_lap_seconds[i],minutes_seconds(column_lap_seconds[i],3),rotation=90,va='bottom',ha='center')
    figure.set_size_inches(18.5, 10.5)
    st.pyplot(figure)

def show_specific_lap_bar_graph(file_name: str, graph_title: str):
    data = pd.read_csv(r'data/' + file_name)
    lap_seconds=data['lap_seconds']
    driver=data['driver_num']
    x_values = np.arange(len(driver))
    figure = plt.figure() 
    plt.title(label=graph_title)
    plt.yticks(ticks=[0,113,114,115,116,117,118,119,120], labels=[0,"1\'53\"","1\'54\"","1\'55\"","1\'56\"","1\'57\"","1\'58\"","1\'59\"","2\'"], minor=False)
    plt.xlim(0,22)
    plt.xlim(left=-1) 
    plt.ylim(110,120)
    plt.bar(x_values,lap_seconds,width = 0.5)
    for i in range(len(x_values)): 
        if lap_seconds[i]<=120:
            plt.text(i,lap_seconds[i],minutes_seconds(lap_seconds[i],3),rotation=90,va='bottom',ha='center')
    plt.xticks(x_values, driver)
    figure.set_size_inches(18.5, 10.5)
    st.pyplot(figure)

def show_specific_driver_bar_graph(file_name:str, graph_title:str, rider_number: int,rider_name:str):
    tim = pd.read_csv(r'data/' + file_name )
    lap_seconds=tim[tim['driver_num']==rider_number]['lap_seconds']
    lap=tim[tim['driver_num']==rider_number]['lap']
    plt.title(label=graph_title)
    plt.xticks(ticks=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], labels=None, minor=False)
    plt.xlim(left=-1)
    plt.xlim(0,22)    
    plt.yticks(ticks=[112,113,114,115,116,117,118], labels=["1\'52\"","1\'53\"","1\'54\"","1\'55\"","1\'56\"","1\'57\"","1\'58\""], minor=False)
    plt.ylim(112,118)
    plt.plot(lap,lap_seconds,label=rider_name)
    plt.legend(fontsize="20")
     
def show_laps_time_graph(file_name:str, graph_title:str, y_min, y_max, y_step, x_min=0, x_max=22, y_column='min', x_column ='driver_num',font_size=10):
    data = pd.read_csv(r'data/' + file_name)
    y_values=data[y_column]
    x_labels=data[x_column]
    x_values = np.arange(len(x_labels))
    figure = plt.figure() 
    y_ticks = np.arange(y_min+4*y_step,y_max,y_step)
    y_labels=[]
    for i in range(len(y_ticks)):
        y_labels.append(minutes_seconds(y_ticks[i],1))
    plt.title(label=graph_title)
    plt.yticks(ticks=y_ticks, labels=y_labels, minor=False)
    plt.xlim(x_min,x_max)
    plt.xlim(left=-1)
    plt.ylim(y_min,y_max)
    plt.bar(x_values,y_values,width = 0.5)
    for i in range(len(x_values)):
        plt.text(i,y_values[i],minutes_seconds(y_values[i],3),fontsize=font_size,rotation=90, va='bottom',ha='center')
    plt.xticks(x_values, x_labels)
    figure.set_size_inches(18.5, 10.5)
    st.pyplot(figure)
    
def space(num):
    for x in range(num):
        st.write('')
        
def addlabels(x:pd.Series,y:pd.Series,font_size:int):
        x=x.values
        y=y.values 
        for i in range(len(x)):
            plt.text(i,y[i],y[i],fontsize=font_size,rotation=90, va='bottom',ha='center')


        