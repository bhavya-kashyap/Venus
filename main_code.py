## importing pandas library for reading csv files
import pandas as pd


###############################################################################################################

### Reading csv file which contain data of crop production that how much days a particular crop takes to produce.
total_time_of_production=pd.read_csv("C:\\Users\\pok\\Downloads\\aries\\DS.csv")

### It will result all the values of csv file in a array
duration_of_crop=total_time_of_production.values

### loop variable for iteration and an empty list is defined.
loop_variable=0
result_data_of_duration_of_crop=dict()

### This loop is for taking the average of the days and storing all the result in an different array named "result_data_of_duration_of_crop"
while(loop_variable<len(duration_of_crop)):
    ### i,c are inner loop variables. k is a temporary list to store the data
    i=duration_of_crop[loop_variable]
    c=duration_of_crop[loop_variable+1]
    k=[]
    k.append(i[0])
    for j in range(1,6):
        t=i[j]+c[j]
        k.append(t/2)
    result_data_of_duration_of_crop[k[0]]=k[1:]
    loop_variable=loop_variable+2

#print(result_data_of_duration_of_crop)
##############################################################################################################


### Reading data of Crop Factor (Kc)
    
cropfactor=pd.read_csv("C:\\Users\\pok\\Downloads\\aries\\CropFactor.csv")

### It will result all the values of csv file in a array

cropfactor_data=cropfactor.values

result_data_of_crop_factor=dict()

for i in cropfactor_data:
    result_data_of_crop_factor[i[0]]=list(i[1:])

#print(result_data_of_crop_factor)
    
###############################################################################################################

### For Latitude
### opening latitudes of states of india
file=open("C:\\Users\\pok\\Downloads\\aries\\latitude.txt","r")

### Reading the data
data=file.read()

### Converting data into dictionary like state_name: latitude
data_file=data.split(",")
latitude_data=dict()
loop_variable=0
while(loop_variable<len(data_file)):
    latitude_data[data_file[loop_variable]]=int(data_file[loop_variable+1])
    loop_variable=loop_variable+2

#print(latitude_data)

##############################################################################################################

### FAO Data for latitude

lat_data=pd.read_csv("C:\\Users\\pok\\Downloads\\aries\\latitude_fao.csv")
lat_val=lat_data.values
lat_fao_data=dict()
for i in lat_val:
    lat_fao_data[int(i[0])]=list(i[1:])
#print(lat_fao_data)
    
    


#############################################################################################################

    #########################Input########################################

state=input("Enter Your State:")  #### As we will find latitude from state name
crop=input("Enter your crop name:") ### Crop name is essintial as crop factor will be find out from this only
print("It takes {} days.".format(result_data_of_duration_of_crop[crop][0]))
days=int(input("Enter the current stage of crop(in terms of days):")) ## This will help us in finding crop factor as crop factor depends upon the stage
temp=float(input("Enter Temprature(in Celcius):")) ## Temprature is neccsary for finding Et0 
moist=input("Enter Soil Moisture:")
month=input("Enter current month(jan,feb,mar,apr,may,june,july,aug,sept,oct,nov,dec):") ### latitude vary by month
#############################################################################################################


mon={"jan":0,"feb":1,"mar":2,"apr":3,"may":4,"june":5,"july":6,"aug":7,"sept":8,"oct":9,"nov":10,"dec":11}


### mean daily percentage
p=lat_fao_data[latitude_data[state]][mon[month]]
et0=p*(0.46*temp+8)
print("Et0 is:",et0," mm/day")

#################crop factor
x=result_data_of_duration_of_crop[crop][1]
i=1
while(days>x and i<=4):
    i=i+1
    x=x+result_data_of_duration_of_crop[crop][i]

kc=result_data_of_crop_factor[crop][i-1]
print("Kc is:",kc)
########################################################################################################
    

et=et0*kc

print("Et is :",et," mm/day")

print("Total water supply is: et-soil moisture")

