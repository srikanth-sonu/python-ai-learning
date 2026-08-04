# battery_level = 85
# while battery_level < 100:
#     battery_level += 5
#     print(f"CHarging... Current Battery Status: ${battery_level}")
# print("Battery fully charged! 🔋")

# distance_km = 12
# while distance_km > 0:

#     distance_km -= 3
#     print(f"Distance remaining: {distance_km} km")
#     if distance_km > 0:
#         print(f"The Driver is {distance_km} km away.")
#     else:
#         print("The Driver has arrived at the destination")

# print(type(distance_km))
# temperature = 20

# while temperature < 100:
#     temperature += 10
#     print(f"Current Temperature: {temperature}°C")


#     if temperature == 60:
#         print("Warning: Temperature is too high! 🔥")
#         break
# print("Temperature has reached the maximum limit. Please take necessary precautions.")


# def calculate_double(number):
#     return number * 2


# print(f"The doubled value is: {calculate_double(5)} & {calculate_double(25)}")
def generate_bill(price, tax_rate=0.05):
    total = price + (price * tax_rate)
    return total


print(generate_bill(100))
print(generate_bill(200, 0.18))
