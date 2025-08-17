import requests
import sys

def getWeather(api_key,city):

    """
    This fetches and prints weather information for a specified city using weather.api services. 

    args: 

    api_key (str): your API key for weatherApi,com 
    city (str): the name of the city where you want to get weather for 
    """
    # base Url for the weatherAPI.com  API endpoint
    base_Url="http://api.weatherapi.com/v1/current.json"

    params ={
        'key':api_key,
        'q':city
    }

    print(f"Fetching weather for {city} ...") 

    try:
        # make the get request to the API
        response=requests.get(base_Url,params=params)
        #Raise an HTTPerror for bad requests (4xx or 5xx )
        response.raise_for_status()
        #parse the Json response
        weather_data=response.json()

        #extract relevant information

        location_name=weather_data['location']['name']
        country=weather_data['location']['country']
        temp_c=weather_data['current']['temp_c']
        temp_f=weather_data['current']['temp_f']
        condition=weather_data['current']['condition']['text']
        last_updated=weather_data['current']['last_updated']


        # print the extracted information
        print("\n --- current Weather information ---")

        print(f" Location : {location_name}, {country }")
        print(f" Last_updated  :{last_updated}")
        print(f" Condition : {condition}")
        print(f" Temperature : {temp_c} 0C , {temp_f} 0F")
        print("_______________________________________________")

    except requests.exceptions.HTTPError as err_http:

        #Handle specific errors for http request (e.g : 401 for bad key, 400 for bad city
        print(f" HTTP ERROR : {err_http} " , file=sys.stderr)
        if response.status_code==401:
            print("Please check if your API key is correct. ",file=sys.stderr)
        elif response.status_code==400:
            print("Please check if your city name is valid .",file=sys.stderr)  

    except requests.exceptions.RequestException as err_req:
        # handle other request related errors (e.g: network issues)
        print(f" An error occured : {err_req} ",file=sys.stderr)
    except Exception as e:
        #catch any unexpected error.
        print(f" An unexpected error occured : {e}",file=sys.stderr)  

        if "__name__"=="__main__":
            # Replace your API Key with the actual api key from weatherapi.com
            api_key="628bcc4cb75940df9fa131801252607"
            # replace " London " with the city you want to fetch data for
            city_name='Kigali'
            # call the function to fetch and display weather data
            getWeather(api_key,city_name)
getWeather(api_key='628bcc4cb75940df9fa131801252607',city='Kigali')            



