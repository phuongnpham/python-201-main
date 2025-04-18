# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def real_estate_ad(**kwargs):
    print("New Real Estate Listing Information")
    print("-" * 40)
    for key, value in kwargs.items():
        formatted_info = key.replace("_", " ").title()
        print(f"{formatted_info}: {value}")
    print("-" * 40)

real_estate_ad(
    home_type = "Single Family",
    parking = "2 Garage Spaces",
    bedroom = 3,
    bathroom = 2,
    price = 349900,
    price_per_sqft = 209,
    annual_tax = 174,
    address = "622 Lemming Ln SE"
)

real_estate_ad(
    home_type = "Mobile Manufactured",
    bedroom = 4,
    bathroom = 2,
    heating = "Electric, Heat Pump",
    cooling = "Central Air",
    laundry = "Washer, Dryper",
    price = 159900,
    address = "2920 Brown Road SE"
)