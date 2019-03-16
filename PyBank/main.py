import csv
import os
csvpath = os.path.join("Resources","budget_data.csv")

counter = 0
total_PL = 0
prior_month = 0
monthly_list = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
       
 # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    

    for row in csvreader:
        counter = counter + 1 
        total_PL = int(row[1])+total_PL 
        monthly_change = int(row[1])-prior_month
        prior_month = int(row[1])
        monthly_list.append(monthly_change) 
        
        if counter < 2:    #added
           # min_month = row[0] #added
            min_value = 0 #added
           # max_month = row[0] #added
            max_value = 0 #added
        elif monthly_change > max_value: #added
            #max_month = row[0] #added
            ax_value = monthly_change #added
        elif monthly_change < min_value:#added
           # max_month = row[0] #added
            min_value = monthly_change #added

    monthly_list2=monthly_list[1:]
    monthly_avg= sum(monthly_list2)/len(monthly_list2)

    
    


    print("Financial Analysis")
    print("------------------")
    print("Total Months: "+str(counter))
    print("Total: $"+str(total_PL))
    print("Average  Change: $"+str(monthly_avg))
    print("Greatest Increase in Profits: " + "($"+str(max_value)+")")
    print("Greatest Decrease in Profits: " + "($"+str(min_value)+")")



    