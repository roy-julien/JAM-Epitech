import requests

def fetch_fuel_prices(url):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        results = data.get('results', [])

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

            print(f"Address: {address}\n")
            print("\tFuel Prices:")
            for fuel, price in prices.items():
                print(f"\t\t{fuel}: {price}")
            print()

    else:
        print("Failed to fetch data from the API")

def format_price(price):
    if price is None:
        return 'N/A'

    price_meur = round(float(price) * 1000, 3)
    return f"{price_meur:.3f} EUR"


api_url = " /api/explore/v2.1/catalog/datasets/prix_des_carburants_j_7/records?where=city%3D%22YZEURE%22&limit=20"

fetch_fuel_prices(api_url)
