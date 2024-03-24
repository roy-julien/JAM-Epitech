import requests

def fetch_fuel_prices(url):
    # Send a GET request to the API URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract relevant information from the response
        results = data.get('results', [])

        # Iterate over each station and print address and fuel prices
        for result in results:
            address = result.get('address', 'N/A')
            prices = {
                'Gazole': format_price(result.get('price_gazole')),
                'SP95': format_price(result.get('price_sp95')),
                'SP98': format_price(result.get('price_sp98')),
                'GPLc': format_price(result.get('price_gplc')),
                'E10': format_price(result.get('price_e10')),
                'E85': format_price(result.get('price_e85'))
            }

            # Print address and fuel prices
            print(f"Address: {address}\n")
            print("\tFuel Prices:")
            for fuel, price in prices.items():
                print(f"\t\t{fuel}: {price}")
            print()

    else:
        print("Failed to fetch data from the API")

def format_price(price):
    # Check if price is None
    if price is None:
        return 'N/A'

    # Convert price from euros to millieuros (mEUR) and format it with three digits after comma
    price_meur = round(float(price) * 1000, 3)  # Convert euros to millieuros and round to three decimal places
    return f"{price_meur:.3f} EUR"


# URL of the API
api_url = " /api/explore/v2.1/catalog/datasets/prix_des_carburants_j_7/records?where=city%3D%22YZEURE%22&limit=20"

# Call the function to fetch and print fuel prices
fetch_fuel_prices(api_url)
