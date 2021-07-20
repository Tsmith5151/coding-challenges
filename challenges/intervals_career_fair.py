"""
University Career Fair (Twitter)

Sam is part of the organizing team arranging the university's career fair and has a list of companies and their respective arrival times and durations. Due to the university-wide budget cuts, there is only one stage available on the entire campus so only one event can occur at a time. Given each company's arrival time and the duration they will stay, determine the max number of events that can be hosted during the fair.

For example, there are `n=5` companies that will arrive at times `arrival = [1,3,3,5,7]` and will stay for `duration = [2,2,1,2,1]`. The first company arrives at `time=1` and stays for `2 hours`. At `time=3`, two companies arrive, but only 1 can stay for either `1` or `2` hours. The next companies arrive at `time=5` and `time=7` and do not conflict with each other. In total, there can be a max of `4` events. 

Complete the `maxEvents` function below. It must return an integer with the max number of events that can be hosted. `maxEvents` has the following inputs:

- `arrival[arrival[0]....arrival[n-1]]`: an array of ints where ith element is the arrival time of the ith company.
- `duration[duration[0]...duration[n-1]]`: an array of the integers where ith element is the duration that the ith company stays at the career fair. 

[Reference Link](https://leetcode.com/discuss/interview-question/374846/Twitter-or-OA-2019-or-University-Career-Fair)


Diagram
```
1:00 [-------------] 3:00 COMPANY A
              3:00 [-------] 4:00 COMPANY B
              3:00 [-------------] 5:00 COMPANY C
                            5:00 [-------------] 7:00 COMPANY D
                                          7:00 [-------------] 8:00 COMPANY E
```
"""


def universityCareerFair(arrival, duration, counter=0, end: int = 0):

    arr_dur = sorted(list(zip(arrival, duration)))
    for arr, dur in arr_dur:
        if arr >= end:
            end = arr + dur
            counter += 1
    return counter


universityCareerFair([1, 3, 3, 5, 7], [2, 2, 1, 2, 1])
