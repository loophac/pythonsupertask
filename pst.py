# Python Supertask playground by Loophac 




import time
t = 5 #number of trials to be ran; default 5

def do():
  x = .5 # x is the longest time the program waits; half of PERIOD_OF_TIME
  
  c1 = 0 # counter
  start = time.time()
  
  PERIOD_OF_TIME = 1 # Finite time for task
  
  while True : #this is a loop that keeps happening until the time limit is hit
    x /= 2 #this cuts the wait time in half each time the loop occurs
    c1 = c1 + 1 #count each change
    c2 = 0 
    #print("| %s th Change" % c1,"| %s   |" % x) #uncomment for if running 1 small trial
    time.sleep(x)
  
    if time.time() > start + PERIOD_OF_TIME :
      print("|%s changes         | " % c1) #this outputs the maximum number of changes that occured during each trial
      break
    
for _ in range(t):
  do()    
