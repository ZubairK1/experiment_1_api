import requests

def call_api(condition: str, buyer_id: str):
    url = "http://127.0.0.1:8003/analytics/average-age"
    params = {
        "condition": condition,
        "buyer_id": buyer_id
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        print("\nAPI Response:")
        print(data)
    except requests.exceptions.HTTPError as http_err:
        print(f"\nHTTP error: {http_err}")
    except Exception as err:
        print(f"\nOther error: {err}")

if __name__ == "__main__":
    condition = input("Enter medical condition (e.g.diabetes, asthma, cancer): ").strip()
    buyer_id = input("Enter buyer ID (e.g. buyer_1, buyer_2): ").strip()
    call_api(condition, buyer_id)
