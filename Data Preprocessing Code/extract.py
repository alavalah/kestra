import requests
url = "https://raw.githubusercontent.com/alavalah/kestra/refs/heads/main/processed_border_crossing_data.csv"
response = requests.get(url)
with open("Border_Crossing_Entry_Data.csv", "wb") as f:
    f.write(response.content)
print("Download complete.")
