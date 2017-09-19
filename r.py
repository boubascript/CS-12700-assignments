#import random
from random import randrange
#Don't use 'from random import *' !!! clutters and confuses namespace
#Best practice:
import random as r
print(random.randrange(10))
