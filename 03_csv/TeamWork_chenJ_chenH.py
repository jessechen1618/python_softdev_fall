import random

filehandle = open('occupations.csv','r')

csv_list = filehandle.readlines()
list_of_percents = list()
list_of_jobs = list()

# Part 1
# Make dictionary from CSV file
for pair in csv_list:
    rev_pair = pair[::-1]
    rev_percentage = ''
    rev_job = ''
    index_of_comma = 0
    for char in rev_pair:
        if char != ',':
            rev_percentage += char
            index_of_comma += 1
        elif char == ',':
            break
    for char in rev_pair[(index_of_comma + 1):]:
        rev_job += char
    list_of_percents.append(rev_percentage[:0:-1])
    list_of_jobs.append(rev_job[::-1])

list_of_jobs = list_of_jobs[1:len(list_of_jobs)-1]
list_of_jobs = list(map(lambda s: s.strip('"'), list_of_jobs))

list_of_percents = list_of_percents[1:len(list_of_percents)-1]
list_of_percents = list(map(float, list_of_percents))

dict_percent_job = {}

for index in range(len(list_of_jobs)):
    dict_percent_job.update({list_of_jobs[index] : list_of_percents[index]})
#print(dict_percent_job)

# Part 2
# Make function to randomly select job based on weight
def sum_list(listParam):
    answer = 0
    for x in listParam:
        answer += x
    return answer

def accumulate_list(listParam):
    result = list()
    for index in range(len(listParam)):
        result.append(listParam[index] + sum_list(listParam[:index]))
    return result

percent_accumulated = accumulate_list(list_of_percents)

def randomJob():
    randomNumber = random.randrange(0, 99)
    piechart = percent_accumulated
    index = 0
    for x in piechart:
        if randomNumber <= x:
            print("Loop Complete")
            print(x)
            print(index)
            return list_of_jobs[index]
        else:
            index += 1
print(randomJob())

filehandle.close()












