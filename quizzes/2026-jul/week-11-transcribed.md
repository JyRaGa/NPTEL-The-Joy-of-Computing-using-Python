# JOC Jul-2026 · Week 11

- Source: `week-11.pdf` (case-study assignment PDF supplied by the repo owner; the only source used for the Jul-2026 session). Answers are as printed in the PDF ("Accepted answer").


## Scenario: Semester Planner A faculty coordinator is preparing the academic schedule for a semester. The coordinator wants to display the calendar of a selected month and identify the weekday on which an important event is scheduled. The following Python program is used.

```python
import calendar  # 1

year = int(input("Enter the year: "))  # 3
month = int(input("Enter the month (1-12): "))  # 4
day = int(input("Enter the event date: "))  # 5

print("Semester Planner")  # 7
print("-" * 25)  # 8
print(calendar.month(year, month))  # 9

weekday = calendar.weekday(year, month, day)  # 11
days = ["Monday", "Tuesday", "Wednesday", "Thursday",  # 12
        "Friday", "Saturday", "Sunday"]  # 13

print("Event Day:", days[weekday])  # 15
```

### Q1. Which function is used to display the calendar of the selected month?

- A. calendar.weekday()
- B. calendar.month()
- C. calendar.date()
- D. calendar.day()

**Answer: B**


### Q2. What is stored in the variable weekday after Line 11 executes?

- A. The name of the weekday
- B. The entered date
- C. The index representing the weekday
- D. The month number

**Answer: C**


### Q3. Why is the list days created in Lines 12–13?

- A. To store all months of the year
- B. To convert the weekday index into its corresponding weekday name
- C. To count the number of weeks in the month
- D. To validate the entered date

**Answer: B**


### Q4. Which statement displays the weekday name of the event?

- A. print(calendar.month(year, month))
- B. weekday = calendar.weekday(year, month, day)
- C. print("Semester Planner")
- D. print("Event Day:", days[weekday])

**Answer: D**


### Q5. Which of the following statements about the program are correct?

- A. The user enters the year, month, and day.
- B. calendar.weekday() returns the name of the weekday.
- C. The list days is used to obtain the month name from the returned index.
- D. The calendar is displayed before the weekday is printed.

**Answer: A, D**


## Scenario: Meeting Schedule Planner An office administrator is preparing the schedule for monthly team meetings. The administrator wants to display the calendar of a selected month, determine whether the year is a leap year, and count the number of Mondays in that month. The following Python program is used.

```python
import calendar  # 1

year = int(input("Enter the year: "))  # 3
month = int(input("Enter the month (1-12): "))  # 4

print("Meeting Schedule")  # 6
print(calendar.month(year, month))  # 7

if calendar.isleap(year):  # 9
    print("Leap Year")  # 10
else:  # 11
    print("Not a Leap Year")  # 12

weeks = calendar.monthcalendar(year, month)  # 14
monday_count = 0  # 15

for week in weeks:  # 17
    if week[0] != 0:  # 18
        monday_count += 1  # 19

print("Number of Mondays:", monday_count)  # 21
```

### Q6. What is the purpose of calendar.isleap(year)?

- A. To display the calendar of the year
- B. To check whether the given year is a leap year
- C. To count the number of days in the month
- D. To find the weekday of the first day of the month

**Answer: B**


### Q7. What is stored in the variable weeks after Line 14?

- A. A list containing the weeks of the month
- B. The number of weeks in the month
- C. A string representing the calendar
- D. The weekday of the first day

**Answer: A**


### Q8. Why does the program check if week[0] != 0?

- A. To count only the weeks with at least one holiday
- B. To count only the Mondays that exist in the selected month
- C. To skip weekends
- D. To find the first week of the month

**Answer: B**


### Q9. Which variable stores the total number of Mondays in the selected month?

- A. weeks
- B. month
- C. weekday
- D. monday_count

**Answer: D**


### Q10. Which of the following statements are correct?

- A. calendar.monthcalendar() returns a list of weeks.
- B. The program counts the number of days in the selected month.
- C. calendar.isleap() returns the number of days in February.
- D. The calendar is displayed before the number of Mondays is printed.

**Answer: A, D**


## Scenario: Shift Allocation Calendar A manufacturing company prepares employee shift schedules every month. Before assigning shifts, the HR team wants to display the calendar, determine the weekday of the first working day of the month, and count how many weekends (Saturdays and Sundays) occur during that month. The following Python program is used.

```python
import calendar  # 1

year = int(input("Enter the year: "))  # 3
month = int(input("Enter the month (1-12): "))  # 4

print("Shift Allocation Calendar")  # 6
print(calendar.month(year, month))  # 7

weeks = calendar.monthcalendar(year, month)  # 9
first_day = calendar.weekday(year, month, 1)  # 10

day_names = ["Monday", "Tuesday", "Wednesday",  # 12
             "Thursday", "Friday", "Saturday", "Sunday"]  # 13

weekend_count = 0  # 15

for week in weeks:  # 17
    if week[5] != 0:  # 18
        weekend_count += 1  # 19
    if week[6] != 0:  # 20
        weekend_count += 1  # 21

print("First day of the month:", day_names[first_day])  # 23
print("Total weekends:", weekend_count)  # 24
```

### Q11. What is the value stored in first_day after Line 10 executes?

- A. The name of the first weekday of the month
- B. The date of the first Monday in the month
- C. An integer representing the weekday of the first day of the month
- D. The total number of weekdays in the month

**Answer: C**


### Q12. Why are the conditions week[5] != 0 and week[6] != 0 checked inside the loop?

- A. To count Saturdays and Sundays that belong to the selected month
- B. To count all working days in the month
- C. To find the first weekend of the month
- D. To identify public holidays

**Answer: A**


### Q13. Which statement best describes the variable weeks?

- A. It stores the names of all weekdays.
- B. It stores a two-dimensional list where each inner list represents one week.
- C. It stores the total number of weeks in the month.
- D. It stores all weekend dates only.

**Answer: B**


### Q14. If a selected month contains 5 Saturdays and 4 Sundays, what value will be printed for weekend_count?

- A. 4
- B. 5
- C. 8
- D. 9

**Answer: D**


### Q15. Which of the following statements are correct?

- A. calendar.weekday(year, month, 1) is used to determine the weekday of the first day of the month.
- B. Each element of weeks is a string representing one week.
- C. The program displays the calendar before counting the weekends.
- D. The value of weekend_count can never be greater than 8.

**Answer: A, C**


## Scenario: Training Session Scheduler A training coordinator is planning employee training sessions for a selected month. The program displays the calendar, identifies all Fridays in the month, and determines the last Friday available for conducting a monthly review meeting.

```python
import calendar  # 1

year = int(input("Enter the year: "))  # 3
month = int(input("Enter the month (1-12): "))  # 4

print("Training Session Scheduler")  # 6
print(calendar.month(year, month))  # 7

weeks = calendar.monthcalendar(year, month)  # 9
fridays = []  # 10

for week in weeks:  # 12
    if week[4] != 0:  # 13
        fridays.append(week[4])  # 14

print("Fridays:", fridays)  # 16

if len(fridays) >= 4:  # 18
    print("Last Friday:", fridays[-1])  # 19
else:  # 20
    print("Insufficient Fridays")  # 21
```

### Q16. What is stored in the list fridays after the loop completes?

- A. The weekday numbers of all Fridays
- B. The dates that fall on Fridays in the selected month
- C. The week numbers containing Fridays
- D. The total number of Fridays

**Answer: B**


### Q17. Why is the condition week[4] != 0 used?

- A. To ignore holidays that fall on Fridays
- B. To ensure the Friday belongs to the selected month
- C. To identify leap years
- D. To count only the first Friday

**Answer: B**


### Q18. What is the purpose of fridays[-1] in Line 19?

- A. It returns the first Friday of the month.
- B. It returns the total number of Fridays.
- C. It returns the last element in the fridays list.
- D. It removes the last Friday from the list.

**Answer: C**


### Q19. Suppose the selected month has Friday dates 3, 10, 17, 24, and 31. What will be printed by Line 19?

- A. 24
- B. 17
- C. 5
- D. 31

**Answer: D**


### Q20. Which of the following statements are correct?

- A. calendar.monthcalendar() returns a string containing the monthly calendar.
- B. week[4] represents the fifth week of the month.
- C. The list fridays stores the dates that fall on Fridays.
- D. The program displays the last Friday only if at least four Fridays are present in the month.

**Answer: C, D**
