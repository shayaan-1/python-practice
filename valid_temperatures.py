# You are building a temperature monitoring loop. Read temperatures from a list. For each temperature:

# Skip any temperature below 20°C
# Print valid temperatures (20°C to 80°C)
# Immediately stop the loop (break) if temperature > 80°C (critical)

def valid_temp(temperature):
    for temp in temperature:
        if temp < 20:
            continue
        elif temp <= 80:
            print(temp)
        else:
            break

valid_temp([10, 15, 19, 20, 80, 90])