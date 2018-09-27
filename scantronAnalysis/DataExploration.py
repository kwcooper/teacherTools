import csv
import math
import numpy as np
import matplotlib.pyplot as plt

with open('Data_Export_ExamID_5619_Section_8259.csv',newline='') as file:
    file_read = list(csv.reader(file, delimiter=',', quotechar='|'))
    
    metaData = file_read[0:3]
    head = file_read[4]
    key = file_read[6]
    data = file_read[7:len(file_read)]


def sturgesBins(data):
# to determine histogram bin size
    return 1. + (3.322 * math.log(len(data)))

def variance(data):
    return sum((xi - (sum(data)/len(data))) ** 2 for xi in data) / len(data)

def std(data):
    return math.sqrt(variance(data))


scores,percent = [],[]
for stu in data:
    scores.append(float(stu[12]))
    percent.append((float(stu[12])/float(key[12]))*100)


# general stats on percentages
print('Number of students in dataset:',len(data))
print('Average percent:',(sum(percent)/len(percent)))
print('Max: {}, Min: {}'.format(max(percent),min(percent)))
print('Standard deviation:', std(percent))


# Plot Histograms
##bns = int(sturgesBins(scores))
##plt.hist(scores,bins=bns)
##plt.title('score')
##plt.show()
##plt.hist(percent,bins=bns)
##plt.title('percent')
##plt.show()



# build the results data structure
results = []
for q in range(13,len(data[0])):
    numCorrect = 0 # check how many student's got it right
    freq = [0,0,0,0,0] 
    objects = ['A','B','C','D','E']
    badQ = False
    for stu in data:
        if stu[q] == key[q]:
            numCorrect += 1
            
        for i,a in zip(range(len(objects)), objects):
            # check which questions the students selected
            if stu[q] == a:
                freq[i] += 1
                
    for i,a in zip(range(len(objects)), objects):
        # check which questions the students selected
        if a != key[q]:
            if freq[i] > numCorrect:
                badQ = True
                
                
    results.append([numCorrect,freq,badQ])
    if 0:
        print('NC:',numCorrect)
        print(freq)

if 0:
    for q in range(len(results)):
        print('Q.{0:>2}: ({1:.2f}% Correct) Correct answer: {2},'
              'Frequencys: A:{3:<2}, B:{4:<2}, C:{5:<2}, D:{6:<2}, E:{7:<2}'.format(q,
                                                                    (results[q][0]/len(data)) * 100,
                                                                      key[13+q],
                                                                      results[q][1][0],
                                                                      results[q][1][1],
                                                                      results[q][1][2],
                                                                      results[q][1][3],
                                                                      results[q][1][3]))       
                                                
    


# make plts for each question with mnumber of answers
if 1:
    for q in range(len(results)):
        objects = ['A','B','C','D','E']
        performance = results[q][1]
        y_pos = range(len(objects))
        barlist = plt.bar(y_pos, performance, align='center', alpha=0.5)
        ans = key[13+q]
        # make the bar red if it is the right answer
        for i,a in zip(range(len(objects)), objects):
            if ans == a:
                barlist[i].set_color('g')
        
        plt.xticks(y_pos, objects)
        plt.ylabel('Frequency')
        plt.title('Question {}'.format(q+1))
        plt.savefig('questionFigs/f{}.png'.format(q+1))
        plt.cla()


# find the most missed question
qDamage = [(i, res[0]) for i,res in zip(range(1,len(results)+1),results)]
qDamage_sorted = sorted(qDamage, key=lambda tup: tup[1],reverse=True)
question, percentage = zip(*qDamage)


    


barlist2 = plt.bar(question,percentage,align='center', alpha=0.5)
# change bar color if students answered one question more wrong than right
for i in range(len(results)):
    if results[i][2]:
        barlist2[i].set_color('r')

plt.title('Question Percentage Correct')
plt.xticks(question)
plt.xlabel('Question')
plt.ylabel('Percentage')
plt.savefig('questionFigs/qSummary.png')
plt.cla()




for row in file_read:
    #print(', '.join(row))
    #print(row)
    pass


