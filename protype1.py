from tkinter import *
import justpy as jp
import pandas as pd
import webbrowser
import tkinter.font as font

def AH():
    A=int(e1_value.get())

    if A==1:
        webbrowser.open('http://127.0.0.1:8000')
        data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
        data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
        month_average = data.groupby(['Month']).mean()
        
        chart_def = """
        {
            chart: {
                type: 'spline',
                inverted: false
            },
            title: {
                text: ' '
            },
            xAxis: {
                reversed: false,
                title: {
                    enabled: true,
                    text: 'Month'
                },
                maxPadding: 1,
                showLastLabel: true
            },
            yAxis: {
                title: {
                    text: 'Rating'
                },
                labels: {
                    format: '{value}'
                },
                lineWidth: 5
            },
            legend: {
                enabled: false
            },
            tooltip: {
                headerFormat: '<b>{series.name}</b><br/>',
                pointFormat:'{point.y}'
            },
            plotOptions: {
                spline: {
                    marker: {
                        enable: true
                    }
                }
            },
            series: [{
                name: 'Rating',
                
            }]
        }
        """
        
        def app():
            wp = jp.QuasarPage()
            h1 = jp.QDiv(a=wp, text="Rating Analysis", classes=" text-cyan-6 text-h4 text-center  text-bold q-pa-md")
            p1 = jp.QDiv(a=wp, text="Average Rating by Month", classes=" text-green-14 text-h6 text-center  ")
        
            hc = jp.HighCharts(a=wp, options=chart_def)
            hc.options.xAxis.categories = list(month_average.index)
            hc.options.series[0].data = list(month_average['Rating'])
        
            return wp
        jp.justpy(app)
        
        
    elif A==2:
        webbrowser.open('http://127.0.0.1:8000')
        data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
        data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
        week_average = data.groupby(['Week']).mean()

        chart_def = """
        {
            chart: {
                type: 'spline',
                inverted: false
            },
            title: {
                text: ' '    
            },
            xAxis: {
                reversed: false,
                title: {
                    enabled: true,
                    text: 'Week'
                },
                labels: {
                    format: '{value}'
                },
                maxPadding: 0.05,
                showLastLabel: true
            },
            yAxis: {
                title: {
                    text: 'Rating'
                },
                labels: {
                    format: '{value}'
                },
                lineWidth: 2
            },
            legend: {
                enabled: false
            },
            tooltip: {
                headerFormat: '<b>{series.name}</b><br/>',
                pointFormat: '{point.y}'
            },
            plotOptions: {
                spline: {
                    marker: {
                        enable: false
                    }
                }
            },
            series: [{
                name: 'Rating',
            }]
        }
        """

        def app():
            wp = jp.QuasarPage()
            h1 = jp.QDiv(a=wp, text="Rating Analysis", classes="text-cyan-6 text-h4 text-center  text-bold q-pa-md")
            h1 = jp.QDiv(a=wp, text="Average Rating by Week", classes=" text-purple-4 text-h6 text-center")
            
            hc = jp.HighCharts(a=wp, options=chart_def)

            hc.options.xAxis.categories = list(week_average.index)
            hc.options.series[0].data = list(week_average['Rating'])
        
            return wp
        
        jp.justpy(app)

    elif A==3:
        webbrowser.open('http://127.0.0.1:8000')
        data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
        data['Day'] = data['Timestamp'].dt.date
        day_average = data.groupby(['Day']).mean()

        chart_def = """
        {
            Highchart: {
                type: 'spline',
                inverted: false
            },
            title: {
                text: ' '    
            },
            xAxis: {
                reversed: false,
                title: {
                    enabled: true,
                    text: 'Date'
                },
                labels: {
                    format: '{value}'
                },
                maxPadding: 0.05,
                showLastLabel: true
            },
            yAxis: {
                title: {
                    text: 'Rating'
                },
                labels: {
                    format: '{value}'
                },
                lineWidth: 2
            },
            legend: {
                enabled: false
            },
            tooltip: {
                headerFormat: '<b>{series.name}</b><br/>',
                pointFormat: '{point.y}'
            },
            plotOptions: {
                spline: {
                    marker: {
                        enable: false
                    }
                }
            },
            series: [{
                name: 'Rating',
            }]
        }
        """
        def app():
            wp = jp.QuasarPage()
            h1 = jp.QDiv(a=wp, text="Rating Analysis", classes="text-cyan-6 text-h4 text-center  text-bold q-pa-md")
            h1 = jp.QDiv(a=wp, text="Average Rating by Day", classes=" text-deep-orange-6 text-h6 text-center  ")
            
            hc = jp.HighCharts(a=wp, options=chart_def)

            hc.options.xAxis.categories = list(day_average.index)
            hc.options.series[0].data = list(day_average['Rating'])
        
            return wp
        
        jp.justpy(app)   

    elif A==4:
        webbrowser.open('http://127.0.0.1:8000')
        data = pd.read_csv("reviews.csv", parse_dates=['Timestamp'])
        data['Weekday'] = data['Timestamp'].dt.strftime('%A')
        data['Daynumber'] = data['Timestamp'].dt.strftime('%w')
        
        weekday_average = data.groupby(['Weekday', 'Daynumber']).mean()
        weekday_average = weekday_average.sort_values('Daynumber')
        
        chart_def = """
        {
            highchart: {
                type: 'spline',
                inverted: false
            },
            title: {
                text: ' '
            },
            xAxis: {
                reversed: false,
                title: {
                
                    text: 'Day'
                },
                labels: {
                    format: '{value}'
                },
                maxPadding: 0.05,
                showLastLabel: true
            },
            yAxis: {
                title: {
                    text: 'Rating'
                },
                labels: {
                    format: '{value}'
                },
                lineWidth: 2
            },
            legend: {
                enabled: false
            },
            tooltip: {
                headerFormat: '<b>{series.name}</b><br/>',
                pointFormat: '{point.y}'
            },
            plotOptions: {
                spline: {
                    marker: {
                        enable: false
                    }
                }
            },
            series: [{
                name: 'Rating'
            }]
        }
        """
        
        def app():
            wp = jp.QuasarPage()
            h1 = jp.QDiv(a=wp, text="Rating Analysis", classes="text-no-wrap text-cyan-6 text-h4 text-center  text-bold q-pa-md")
            p1 = jp.QDiv(a=wp, text="Average Ratings of Weekdays",classes="text-pink-4 text-h6 text-center")
        
            hc = jp.HighCharts(a=wp, options=chart_def)
            hc.options.xAxis.categories = list(weekday_average.index.get_level_values(0))
            hc.options.series[0].data = list(weekday_average['Rating'])
        
            return wp
        
        jp.justpy(app)

    elif A==5:
        webbrowser.open('http://127.0.0.1:8000')
        wm_df = pd.read_csv('reviews.csv').round(2)
        def row_selected(self, msg):
            print(msg)
        def grid_test():
            wp = jp.QuasarPage()
            h1 = jp.QDiv(a=wp, text="Rating Analysis", classes="text-no-wrap text-cyan-6 text-h4 text-center  text-bold q-pa-md")
            p1 = jp.QDiv(a=wp, text="Dataset of REVIEWS", classes="text-amber-6 text-h6 text-center q-pa-md ")
            row_data_div = jp.Div(a=wp)
            grid = wm_df.jp.ag_grid(a=wp)
            grid.row_data_div = row_data_div
            grid.on('rowSelected', row_selected)
            grid.options.columnDefs[0].index = True
            return wp

        jp.justpy(grid_test)
    else:
        screen=Tk()
        screen.geometry('150x100')
        screen.resizable(False,False)
        screen.configure(bg='cyan')
        s1=Label(screen,text="\n❎  Error!!!!\n\nplease check \nyour input" ,fg='red',bg='cyan',font=('Helvetica', 11, 'bold'),bd=4)
        s1.pack()
    
window= Tk()
window.title(" Rating Analysis")
window.geometry('520x550')
window.resizable(False,False)
window.configure(bg='#0a0a0a')


myFont = font.Font(family='Helvetica', size=14, weight='bold')
l2=Label(window,text="\n                                  RATING ANALYSIS                                  \n",bg='#000000',foreground="#8a8a8a")
l2.grid(row=0,column=0)
l2['font']=myFont

l3=Label(window,text="DATASET CONTAINS :- \n  Rows = 45000\nColumns = 4",font=('Helvetica', 10, 'bold'),background='#0a0a0a',foreground='#00CCCC')
l3.grid(row=1,column=0,pady = 10, padx = 100)

lf=LabelFrame(window, text='Enter the number for following analysed graphs of dataset :-',bg="#0a0a0a",fg='silver',font=('Helvetica', 12, 'bold',UNDERLINE),bd='0')
lf.grid(column=0, row=2, padx=10, pady=10)

Month=Label(lf,text=" 1 -  Average Rating by Months ",bg='#0a0a0a',font=('Helvetica', 10, 'bold'),fg="#ff0000")
Month.grid(column=0, row=0, ipadx=10, ipady=10)



week= Label(lf,text=" 2 - Average Rating by Weeks    ",bg="#0a0a0a",font=('Helvetica', 10, 'bold'),fg="#ff3300")
week.grid(column=0, row=1, ipadx=10, ipady=10)

day = Label(lf,text=" 3 - Average Rating by days      ",bg="#0a0a0a",font=('Helvetica', 10, 'bold'),fg="#e6e600")
day.grid(column=0, row=2, ipadx=10, ipady=10)

daywise= Label(lf,text=" 4 - Average Rating by weekdays",bg="#0a0a0a",font=('Helvetica', 10, 'bold'),fg="#40ff00")
daywise.grid(column=0, row=3, ipadx=10, ipady=10)

dataset= Label(lf,text=" 5 - Sorted whole dataset         ",bg="#0a0a0a",font=('Helvetica', 10, 'bold'),fg="#33ff99")
dataset.grid(column=0, row=4, ipadx=10, ipady=10)


L1= Label(window,text="Enter The Number Below :-" ,fg='grey',font=('Helvetica', 10, 'bold'),bg="#660000")
L1.grid(row=12,column=0,pady = 2, padx = 10)
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value,background='#A2A2A2')
e1.grid(row=13,column=0,padx=5,pady=5)

b1=Button(window,text=" RESULT ",fg='white',bg="#20A0DF",activebackground='#00ff00',activeforeground='blue',command=AH, borderwidth = '4',font=('Helvetica', 10, 'bold'))
b1.grid(row=15,column=0, padx = 100,pady=3)
b1=Button(window,text="QUIT !!!",fg="red",command=quit,borderwidth = '5',font=('Helvetica', 10, 'bold'),background='silver')
b1.grid(row=16,column=0)
 
window.mainloop()