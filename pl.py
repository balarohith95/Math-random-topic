import random
import math


#Beginner 

# 1. Generate 5 random floats between 0 and 1.
print([random.random()for _ in range(5)])

# 2. Dice roll simulator using random.randint.
print("Dice roll:",random.randint(1,6))

# 3. Convert 90 degrees to radians.
print("90 degrees in radians:",math.radians(90))

# 4. Factorial of a user-given number.
num=5
print(f"Factorial of {num}:",math.factorial(num))

# 5. Shuffle a list of 10 integers.
nums=list(range(1,11))
random.shuffle(nums)
print("Shuffled list:",nums)

#Intermediate

# 1. Lottery draw of 6 unique numbers from 1 to 49.
print("Lottery draw:",random.sample(range(1,50),6))

# 2. Approximate Pi using Monte Carlo
inside=0
total=10000
for _ in range(total):
    x,y=random.random(),random.random()
    if x**2+y**2<=1:
        inside+=1
print((inside/total)*4)


# 3. Calculate compound interest using math.pow.
principal=1000
rate=0.05
time=10
amount=principal*math.pow((1+rate),time)
print("Compound interest amount:",amount)


# 4. Trigonometry calculator (degrees)
angle=45
rad=math.radians(angle)
print(math.sin(rad),math.cos(rad),math.tan(rad))

# 5. Roll two dice 1000 times and count frequency
freq={}
for _ in range(1000):
    total=random.randint(1,6)+random.randint(1,6)
    freq[total]=freq.get(total,0)+1
print(freq)

