import csv
import os
import operator

csv_path = os.path.join("Resources",'election_data.csv')

#csv_source = 'resources/election_data.csv'

counter_votes = {}

with open(file=csv_path, mode='r', encoding='utf-8') as csv_file:
   csv_reader = csv.DictReader(csv_file, delimiter=',')

   for line in csv_reader:       
        if line['Candidate'] in counter_votes:
           counter_votes[line['Candidate']] = counter_votes[line['Candidate']] + 1
        else:
           counter_votes[line['Candidate']] = 1

avg = {k: round(v / total*100,2) for total in (sum(counter_votes.values()),) for k, v in counter_votes.items()}
sorted_counter_votes = sorted(counter_votes.items(), key=operator.itemgetter(1),reverse=True)
sorted_avg = sorted(avg.items(), key=operator.itemgetter(1),reverse=True)
total_votes =sum(counter_votes.values())

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
print(sorted_counter_votes)
print(sorted_avg)
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
print("-------------------------")
#print("Winner: ") Khan
print("-------------------------")
