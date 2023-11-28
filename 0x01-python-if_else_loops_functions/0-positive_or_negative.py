#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number &gt; 0:
print(&quot;{} is positive&quot;.format(number))
elif number == 0:
print(&quot;{} is zero&quot;.format(number))
else:
print(&quot;{} is negative&quot;.format(number))
