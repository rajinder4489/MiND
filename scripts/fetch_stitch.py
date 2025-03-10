def fetch_stitch_data():
    url = "https://stitch.embl.de/api/interaction?format=json"
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data)

def save_stitch_data():
    df = fetch_stitch_data()
    df.to_csv('stitch_data.csv', index=False)
    print("STITCH data saved.")

if __name__ == "__main__":
    save_stitch_data()