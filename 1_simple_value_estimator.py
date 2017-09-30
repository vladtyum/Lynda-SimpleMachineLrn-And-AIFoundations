#!/usr/bin/python3

"""
that's what's called linear regression, 
where you define weights by yourself

"""
def estimate_home_value(size, bedrooms):
    #assume all homes wort at least 50k
    value = 50000

    #adjust the value estimate based on the size of the house
    value = value + (size * 92)
    
    #adjust the value estamate based on the number of the bedrooms
    value = value + (bedrooms * 10000)

    return value


value = estimate_home_value(3800, 5)

print("Estimated value is:")
print(value)
