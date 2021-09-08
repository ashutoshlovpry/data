"""Problem:
Clark is conducting an online Quiz competition daily where daily participation for contestants is optional.
Clark want to send specific notifications to following group of participants
- Participants who participated everyday
- Participants who participated only once
- Participants who participated on the first day and never participated again.
Help Clark to write functions in python to get the above information. Sample function definitions are already created.
Participants data will be sent as list of lists. Each row will represent the participants attended on that day.
Sample input:
participants_list = [
    ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ],
    ['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam']
]
send the solution to cutshort+fresher@adnabu.com with the subject line "Solution to Puzzle"
Bonus points for optimising the solution w.r.t. time and space.
"""
d1= set(['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole' ])
d2=set(['Brad', 'Walter', 'Sam', 'Krish','Desmond', 'Jennifer'])
d3=set(['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'])
d4= set(['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'])
d5= set(['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'])
d6= set(['Krish', 'Brad', 'Walter', 'Jennifer','Desmond', 'Harry', 'Nicole', 'Sam'])

def daily_participants(d1,d2,d3,d4,d5,d6):
    """Returns the list of all participants who participated everyday
    for the sample input, the right answer is
    ['Desmond', 'Krish', 'Sam']
    expected return object is a list of strings
    """
    re=set(d1).intersection(d1,d2,d3,d4,d5,d6)
    print(list(re))
    return list(re)
daily_participants(d1,d2,d3,d4,d5,d6)

def one_time_participants(d1,d2,d3,d4,d5,d6):
    """Returns the list of all participants who participated only once
    for the sample input, the right answer is
    ['Kapil', 'Ron', 'Ginny', 'Ted', 'Sachin', 'John', 'Joan']
    expected return object is a list of strings
    """
    q= d1.difference(d2)
    q1= d2.difference(d1)
    r1=q.union(q1)
    q2=r1.difference(d3)
    q3= d3.difference(r1)
    r2=q2.union(q3)
    q4=r2.difference(d4)
    q5= d4.difference(r2)
    r3=q4.union(q5)
    q6=r3.difference(d5)
    q7= d5.difference(r3)
    r4=q6.union(q7)
    q8=r4.difference(d6)
    q9= d6.difference(r4)
    r5= q8.union(q9)
    r6= r5.difference(d6)
    r7= r6.difference(d4)
    


    print(list(r7))
    return (list(r7))
one_time_participants(d1,d2,d3,d4,d5,d6)

def first_day_only_participants(d1,d2,d3,d4,d5,d6):
    """Returns the list of all participants who participated on the first day and never participated again.
    for the sample input, the right answer is
    ['John', 'Joan']
    expected return object is a list of strings
    """
    q1= d2.union(d3,d4,d5,d6)
    r7= d1.difference(q1)
    print(list(r7))
    return list(r7)
first_day_only_participants(d1,d2,d3,d4,d5,d6)