import requests

# Example API URL
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)  # Should return 200 (success)
print(response.json())  # Print the data returned from the API in JSON format

# GET Request
if response.status_code == 200:
    posts = response.json()
    for post in posts[:3]:
        print(f"Id: {post['id']}")
        print(f"Title: {post['title']}")



#POST Request
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    'title': 'New Post',
    'body': 'This is the body of new post.',
    'userId': 1
}
response = requests.post(url, json = data)
print(response.status_code)
print(response.json())



# API key authentication
#free API (endpoint) - https://api.openweathermap.org/data/2.5/weather

API_KEY = "your_openweather_api_key"
city = "Dallas"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Weather in {city}: {data['weather'][0]['description']}")
else:
    print("Failed to retrieve data")