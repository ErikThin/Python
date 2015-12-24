import math
"""
Readable number
"""
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):                
    power = math.floor(math.log(abs(number), base)) if abs(number) > 0 else 0
    power = min(power, len(powers) - 1)
    number /= base ** power
    return "{1:.{0}f}".format(decimals, number if decimals > 0 else math.modf(number)[1]) + powers[power] + suffix

print(friendly_number(1235))
