from random import randint
BOARD = 1
BCM = 1
OUT = 1
IN = 1
LOW=0
HIGH=1
PUD_DOWN = 1
micro=0
heatsensor=0
def setmode(a):
   pass
def setup(a, b,pull_up_down=1,initial=LOW):
   pass
def output(a, b):
   # print(a,b)
   pass
   if b == 1:
      pass
   else:
      pass
def cleanup():
   print ('pins released as inputs')
def setwarnings(flag):
   pass
def input(number,source):
   pass
   if source =='m':
      if micro == 1:
         return True
         
      else:
         return False
   if source =='h':
      if heatsensor == 1:
         return True
         
      else:
         return False
def gpio_function(pin):
   pass