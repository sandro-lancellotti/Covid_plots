#import libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np



# Menu n.1 (the user chooses what type of information he/she wants to visualize)
def menu_1():
    print("1. Aggregated national data, per month")
    print("2. Aggregated regional data, per month (select region)")
    print("3. Detailed regional data for a given period (select period and region)")
    print("4. Detailed regional data for a month in 2020 and 2021 (select month and region)")
    print("5. Normalized comparison between two regions for a given month (select year, month and regions)")
    print("6. Correlation plot for regional or national data")
    print("0. Quit")
    return input("Please enter your choice: ")


# Menu n.2 (Choice of the variable/parameter of interest)
def menu_2():
    while True: #da togliere
        print("1. new positives")
        print("2. variation positives")
        print("3. deaths")
        k = input("Please enter your choice: ")
        if k == "1":
            return "nuovi_positivi"
        elif k == "2":
            return "variazione_totale_positivi"
        elif k == "3":
            return "deceduti_giornalieri"
        else:
            print("Inconsistent choice, please insert a new input.")

        #menu_2()
        #return




def menu_3():
    while True:
        print("1. Abruzzo")
        print("2. Basilicata")
        print("3. Calabria")
        print("4. Campania")
        print("5. Emilia-Romagna")
        print("6. Friuli Venezia Giulia")
        print("7. Lazio")
        print("8. Liguria")
        print("9. Lombardia")
        print("10. Marche")
        print("11. Molise")
        print("12. Piemonte")
        print("13. Puglia")
        print("14. Sardegna")
        print("15. Sicilia")
        print("16. Toscana")
        print("17. Trento")
        print("18. Bolzano")
        print("19. Umbria")
        print("20. Valle d'Aosta")
        print("21. Veneto")
        k = input("Please enter your choice: ")
        if k == "1":
            return "Abruzzo"
        elif k == "2":
            return "Basilicata"
        elif k == "3":
            return "Calabria"
        elif k == "4":
            return "Campania"
        elif k == "5":
            return "Emilia-Romagna"
        elif k == "6":
            return "Friuli Venezia Giulia"
        elif k == "7":
            return "Lazio"
        elif k == "8":
            return "Liguria"
        elif k == "9":
            return "Lombardia"
        elif k == "10":
            return "Marche"
        elif k == "11":
            return "Molise"
        elif k == "12":
            return "Piemonte"
        elif k == "13":
            return "Puglia"
        elif k == "14":
            return "Sardegna"
        elif k == "15":
            return "Sicilia"
        elif k == "16":
            return "Toscana"
        elif k == "17":
            return "P.A. Trento"
        elif k == "18":
            return "P.A. Bolzano"
        elif k == "19":
            return "Umbria"
        elif k == "20":
            return "Valle d'Aosta"
        elif k == "21":
            return "Veneto"
        print("Inconsistent choice, please insert a new input.")




def menu_4():
    while True:
        print("1. new positives")
        print("2. variation positives")
        print("3. total positives")
        print("4. deaths")
        print("5. daily deaths")
        print("6. hospitalized")
        k = input("Please enter your choice: ")
        if k == "1":
            return "nuovi_positivi"
        elif k == "2":
            return "variazione_totale_positivi"
        elif k == "3":
            return "totale_positivi"
        elif k == "4":
            return "deceduti"
        elif k == "5":
            return "deceduti_giornalieri"
        elif k == "6":
            return "totale_ospedalizzati"
        print("Inconsistent choice, please insert a new input.")


# Menu n.5 (The user chooses for the Month of interest)
def menu_5():
    while True:
        print("1. Jan")
        print("2. Feb")
        print("3. Mar")
        print("4. Apr")
        print("5. May")
        print("6. Jun")
        print("7. Jul")
        print("8. Aug")
        print("9. Sep")
        print("10. Oct")
        print("11. Nov")
        print("12. Dec")
        k = input("Please enter your choise: ")
        if k in {"1", "2", "3", "4",  "5", "6", "7", "8", "9", "10", "11", "12"}:
            return int(k)
        print("Inconsistent choice, please insert a new input.")


# Menu n.6 (The user chooses for the Year of interest)
def menu_6():
    while True:
        print("1. 2020")
        print("2. 2021")
        k = input("Please enter your choice: ")
        if k == "1":
            return 2020
        elif k == "2":
            return 2021
        print("Inconsistent choice, please insert a new input.")


# Menu n.7 (The user chooses if he/she wants to visualize regional or national correlation data)
def menu_7():
    while True:
        print("1. Correlation plot for one region")
        print("2. Correlation plot for national data")
        k = input("Please enter your choice: ")
        if k == "1":
            return k
        elif k == "2":
            return k
        print("Inconsistent choice, please insert a new input.")



# Menu n.8 (The menu n.8 is a new version of the already seen menu n.2 and menu n.4. 
#           It is used when we want to give the user the possibility to analyze the data considering some variables more) 
#          (ADDED "cumulative positives" and "daily deaths")          
def menu_8():
    while True:
        print("1. new positives")
        print("2. total positives")
        print("3. deaths")
        print("4. daily deaths")
        print("5. hospitalized")
        k = input("Please enter your choice: ")
        if k == "1":
            return "nuovi_positivi"
        elif k == "2":
            return "totale_positivi"
        elif k == "3":
            return "deceduti"
        elif k == "4":
            return "deceduti_giornalieri"
        elif k == "5":
            return "totale_ospedalizzati"
        print("Inconsistent choice, please insert a new input.")



def menu_9():
    while True:
        print('1. Cumulative data')
        print('2. Detailed data')
        k = input("Please enter your choise: ")
        if k == "1" or k == "2":
            return k
        print("Inconsistent choice, please insert a new input.")


# Function to retrive time period of interest
def retrive_dates():
    min_range = min(covid_data['data'])
    max_range = max(covid_data['data'])
    while True:
        # Start date
        while True:
            print("Please enter the start date (format yyyy/mm/dd): ")
            start_year = input("Enter the year: ")
            start_month = input("Enter the month: ")
            start_day = input("Enter the day: ")

            # correction of user input errors
            try:
                start_date = pd.Timestamp(int(start_year), int(start_month), int(start_day))
                break
            except:
                print("Invalid data choice!")

        # End date
        while True:
            print("Please enter the end date (format yyyy/mm/dd): ")
            end_year = input("Enter the year: ")
            end_month = input("Enter the month: ")
            end_day = input("Enter the day: ")

            # correction of user input errors
            try:
                end_date = pd.Timestamp(int(end_year), int(end_month), int(end_day))
                break
            except:
                print("Invalid data choice!")
        if start_date > end_date:
            print("Start date must be less equal end date!")
            continue
        if start_date >= min_range and end_date <= max_range:
            return start_date, end_date
        print("The dates entered are out of range!")





# PLOT n.1 
def plot1():
    col = menu_2() # for the column variable of interest
    d = covid_data[["data", col]].groupby(pd.Grouper(key='data', freq='M')).sum().reset_index() # freq M (monthly)
    d['data'] = d['data'].dt.strftime("%Y-%m")

    fig, ax = plt.subplots(figsize=(10, 8))  
    ax.bar(d['data'], d[col])
    plt.xticks(rotation=45, horizontalalignment='right')
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: format(int(x), ','))) # To control the way in which the labels of the y-axis appear
    ax.set_title(f'Plot of {translation[col]}', fontsize=20)
    ax.set_xlabel('Year-month', fontsize=14)
    ax.set_ylabel(f'{translation[col]}', fontsize=14)

    k = input('If you want to save the plot enter "y", if no another key: ')
    if k == "y":
        plt.savefig(f'Plot of {translation[col]}', bbox_inches='tight') # 'bbox_inches='tight'' to avoid that cuts out the labels
    plt.show()


# PLOT n.2
def plot2():
    region = menu_3() # for the choice of the region
    col = menu_2() # for the column variable of interest
    d = covid_data[covid_data["denominazione_regione"] == region]
    d = d[["data", col]].groupby(pd.Grouper(key='data', freq='M')).sum().reset_index()
    d['data'] = d['data'].dt.strftime("%Y-%m")

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.bar(d['data'], d[col])
    plt.xticks(rotation=45, horizontalalignment='right')
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: format(int(x), ',')))
    ax.set_title(f'Plot of {translation[col]} of {region}', fontsize=20)
    ax.set_xlabel('Year-month', fontsize=14)
    ax.set_ylabel(f'{translation[col]}', fontsize=14)

    k = input('If you want to save the plot enter "y", if no another key: ')
    if k == "y":
        plt.savefig(f'Plot {translation[col]} of {region}', bbox_inches='tight')
    plt.show()


#PLOT N.3
def plot3():
    region = menu_3()
    start_date, end_date = retrive_dates()
    col = menu_4()
    d = covid_data[(covid_data["denominazione_regione"] == region) & (covid_data['data'] >= start_date) & (covid_data['data'] <= end_date)]
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(d['data'], d[col])
    plt.xticks(rotation=45, horizontalalignment='right')
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: format(int(x), ',')))
    ax.set_title(f'Plot of {translation[col]}', fontsize=20)
    ax.set_xlabel('Day', fontsize=14)
    ax.set_ylabel(f'{translation[col]}', fontsize=14)
    k = input('If you want to save the plot enter "y", if no another key: ')
    if k == "y":
        plt.savefig(f'Plot of  {translation[col]}', bbox_inches='tight')
    plt.show()


#PLOT n. 4 
def plot4():
    region = menu_3()
    month = menu_5()
    col = menu_4()
    d = covid_data[(covid_data["denominazione_regione"] == region) & (covid_data['data'].dt.month == month)]
    d_2020 = d[d['data'].dt.year == 2020]
    d_2021 = d[d['data'].dt.year == 2021]
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(d_2020['data'].dt.day, d_2020[col], label=f'{translation[col]} 2020')
    ax.plot(d_2021['data'].dt.day, d_2021[col], label=f'{translation[col]} 2021')
    plt.xticks(rotation=45, horizontalalignment='right')
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: format(int(x), ',')))
    ax.set_title(f'Plot of  {translation[col]}', fontsize=20)
    ax.set_xlabel('Day', fontsize=14)
    ax.set_ylabel(f'{translation[col]}', fontsize=14)
    ax.legend()
    k = input('If you want to save the plot enter "y", if no another key: ')
    if k == "y":
        plt.savefig(f'Plot of  {translation[col]}',  bbox_inches='tight')
    plt.show()

# PLOT n.5 
def plot5():
    year = menu_6() #for the choice of the year of interest
    month = menu_5() # for the choice of the month of interest
    region1 = menu_3() # for the choice of the first region of interest
    region2 = menu_3() # for the choice of the second region of interest


    h1 = region_hinhabitants_data.loc[region1][0]
    h2 = region_hinhabitants_data.loc[region2][0]
    d_1 = covid_data[(covid_data["denominazione_regione"] == region1) & (covid_data['data'].dt.month == month) & (
                covid_data['data'].dt.year == year)]
    d_2 = covid_data[(covid_data["denominazione_regione"] == region2) & (covid_data['data'].dt.month == month) & (
                covid_data['data'].dt.year == year)]
    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7:"July", 8:"August", 9:"September",
              10:"October", 11:"November", 12:"December"}
    kind = menu_9()
    if kind == "1":
        col = menu_2()
        fig, ax = plt.subplots(figsize=(10, 8))
        width = 0.4
        x = np.arange(len(d_1['data']))
        ax.bar(x - width / 2, d_1[col] / h1, width,
               label=f'{translation[col]} of {region1}')  ########################################################################################
        ax.bar(x + width / 2, d_2[col] / h2, width,
               label=f'{translation[col]} of {region2}')  ################################################################################################
        ax.set_xticks(x)
        ax.set_xticklabels(d_1['data'].dt.strftime("%Y-%m-%d"))

    else:
        col = menu_4()
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.plot(d_1['data'].dt.day, d_1[col]/h1, label=f'{translation[col]} {region1}')
        ax.plot(d_2['data'].dt.day, d_2[col]/h2, label=f'{translation[col]} {region2}')


    ax.set_xlabel('Day', fontsize=14)
    ax.set_ylabel(f'{translation[col]}', fontsize=14)
    ax.legend()
    ax.yaxis.set_major_formatter(ticker.PercentFormatter())
    plt.xticks(rotation=45, horizontalalignment='right')
    ax.set_title(f'Percentage of {translation[col]} in {region1} and \n {region2} during {months[month]} {year}',
                 fontsize=20)

    k = input('If you want to save the plot enter "y", if no another key: ')
    if k == "y":
        plt.savefig(f"Percentage of {translation[col]} on the region's population", bbox_inches='tight')
    plt.show()



# PLOT n.6
def plot6():
    k = menu_7() # for choice about visualization of regional or national correlation data
    if k == "1":
        region = menu_3() # for the choice of the region of interest
        d = covid_data[covid_data['denominazione_regione'] == region]
    else:
        region = "Italy"
        d = covid_data.groupby(pd.Grouper(key='data', freq='D')).sum().reset_index() #freq M (daily) 


    print('Select the first column from the following: ')
    col1 = menu_8()
    print('Select the second column from the following: ')
    col2 = menu_8()

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(x=d[col1], y=d[col2])
    plt.xticks(rotation=45, horizontalalignment='right')
    ax.set_title(f'Plot of {translation[col1]} vs {translation[col2]} ({region})', fontsize=20)
    ax.set_xlabel(f'{translation[col1]}', fontsize=14)
    ax.set_ylabel(f'{translation[col2]}', fontsize=14)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: format(int(x), ',')))
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: format(int(x), ',')))
    k = input('If you want to save the plot enter "y", if no another key: ')

    if k == "y":
        plt.savefig(f'Plot of {translation[col1]} vs {translation[col2]} ({region})', bbox_inches='tight')
    plt.show()



#import data
def import_data():

    path_covid_data = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv"
    path_region_hinhabitants = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv"

    global covid_data
    covid_data = pd.read_csv(path_covid_data)
    covid_data = covid_data[["data", "denominazione_regione", "totale_ospedalizzati", "totale_positivi", "variazione_totale_positivi", "nuovi_positivi", "deceduti"]]
    covid_data['data'] = pd.to_datetime(covid_data['data'])

    for reg in covid_data['denominazione_regione'].unique():
        index = covid_data[covid_data['denominazione_regione'] == reg].index
        covid_data.loc[index[1:], ['deceduti_giornalieri']] = covid_data.loc[index[1:], 'deceduti'].values - covid_data.loc[index[:-1], 'deceduti'].values
        covid_data.loc[index[0], ['deceduti_giornalieri']] = covid_data.loc[index[0], 'deceduti']
        covid_data.loc[index, ['positivi_cumulati']] = covid_data.loc[index, ['nuovi_positivi']].cumsum().values
    
    global region_hinhabitants_data
    region_hinhabitants_data = pd.read_csv(path_region_hinhabitants)

    #To correct the discrepancy of the names of provinces Bolzano and Trento in the dataset
    region_hinhabitants_data.loc[region_hinhabitants_data.loc[:, 'denominazione_regione'] == "Trento", 'denominazione_regione'] = "P.A. Trento"
    region_hinhabitants_data.loc[region_hinhabitants_data.loc[:, 'denominazione_regione'] == "Bolzano", 'denominazione_regione'] = "P.A. Bolzano"

    # region_hinhabitants_data.replace(to_replace="P.A. Trento", value="Trento", inplace=True)

    region_hinhabitants_data = region_hinhabitants_data.groupby('denominazione_regione').sum()[["totale_generale"]]

    
    global translation
    translation = {'data': 'date', 'denominazione_regione': 'region', 'totale_ospedalizzati': 'hospitalized',
                   'totale_positivi': 'positive cases', 'variazione_totale_positivi': 'variation of positive cases',
                   'nuovi_positivi': 'new positives', 'deceduti': 'deaths', 'deceduti_giornalieri': 'daily deaths',
                   'positivi_cumulati': 'cumulative positive cases'}



# Function of the main program
def main():
    import_data() #Da fare fuori perche altrimenti viene fatto ogni volta
    while True: # da togliere
        choice = menu_1()
        if choice == "0":
            break #return
                  # print('Bye bye...and remember to wear your mask!')
        elif choice == "1":
            plot1()
        elif choice == "2":
            plot2()
        elif choice == "3":
            plot3()
        elif choice == "4":
            plot4()
        elif choice == "5":
            plot5()
        elif choice == "6":
            plot6()
        else:
            print("Inconsistent choice, please insert a new input.")
            main()
    print('Bye bye...and remember to wear your mask!')




if __name__ == '__main__':
    import_data()
    main()

