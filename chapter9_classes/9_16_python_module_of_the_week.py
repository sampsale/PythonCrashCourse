
# here we try out a random module
# description:
# The time module provides access to several different types of clocks, each useful for different purposes. The standard system calls like time() report the system “wall clock” time. The monotonic() clock can be used to measure elapsed time in a long-running process because it is guaranteed never to move backwards, even if the system time is changed. For performance testing, perf_counter() provides access to the clock with the highest available resolution to make short time measurements more accurate. The CPU time is available through clock(), and process_time() returns the combined processor time and system time.


import time

print('\tThe epoch time is:', time.time())
print('\tThe local time is:', time.ctime())
later = time.time() + 60
print('\tThe local time 1 minute from now :', time.ctime(later))

def show_struct(s):
    print('\ttm_year :', s.tm_year)
    print('\ttm_mon  :', s.tm_mon)
    print('\ttm_mday :', s.tm_mday)
    print('\ttm_hour :', s.tm_hour)
    print('\ttm_min  :', s.tm_min)
    print('\ttm_sec  :', s.tm_sec)

show_struct(time.localtime())

