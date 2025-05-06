def valid_temp(temperature):
    for temp in temperature:
        if temp < 20:
            continue
        elif temp <= 80:
            print(temp)
        else:
            break

valid_temp([10, 15, 19, 20, 80, 90])