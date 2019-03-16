import csv
import os
csvpath = os.path.join("Resources","budget_data.csv")

counter = 0
total_PL = 0
prior_month = 0
monthly_list = []
min_value = 0 #added
max_value = 0 #added

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
        
        if counter < 1:    #added
            min_month = row[0] #added
            min_value = 0 #added
            max_month = row[0] #added
            max_value = 0 #added

        elif monthly_change > max_value: #added
            max_month = row[0] #added
            max_value = monthly_change #added
        
        elif monthly_change < min_value:#added
            min_month = row[0] #added
            min_value = monthly_change #added

    monthly_list2=monthly_list[1:]
    monthly_avg= round(sum(monthly_list2)/len(monthly_list2),2)

    
    


    print("Financial Analysis")
    print("------------------")
    print("Total Months: "+str(counter))
    print("Total: $"+str(total_PL))
    print("Average  Change: $"+str(monthly_avg))
    print("Greatest Increase in Profits: " + str(max_month) + " ($"+str(max_value)+")")
    print("Greatest Decrease in Profits: " + str(min_month) + " ($"+str(min_value)+")")

    filepath = os.path.join( "PyBank_Output.txt")
    with open(filepath,'w') as text:
        text.write("Financial Analysis" + "\n")
        text.write("----------------------------------------" + "\n")
        text.write(f"Total Months: {counter}" + "\n")
        text.write(f"Total Revenue: ${total_PL}" + "\n")
        text.write(f"Average Revenue Change: ${monthly_avg}" + "\n")
        text.write(f"Greatest Increase in Revenue: {max_month} (${max_value})" + "\n")
        text.write(f"Greatest Decrease in Revenue: {min_month} (${min_value})" + "\n")
