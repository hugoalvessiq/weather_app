import openmeteo_requests
import requests
import requests_cache
from retry_requests import retry
from datetime import datetime

# Open-Meteo API configuration with cache and retries
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)


def get_coordinates(city_name):
    """
    Gets the coordinates (latitude, longitude) of a city using the Open-Meteo API.
    """
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={
        city_name}&count=1"
    response = retry_session.get(url)
    response.raise_for_status()
    data = response.json()

    if "results" in data and data["results"]:
        result = data["results"][0]
        latitude = result["latitude"]
        longitude = result["longitude"]
        print(f"[DEBUG] Coordenadas para {city_name}: {latitude}, {longitude}")
        return latitude, longitude
    else:
        raise ValueError(f"City '{city_name}' not found!")


def interpret_weather_code(code):
    """
    Interprets Open-Meteo weather codes into more detailed descriptions.
    """
    if code == 0:
        return "Clear sky"
    elif code == 1:
        return "Mainly clear"
    elif code == 2:
        return "Partly cloudy"
    elif code == 3:
        return "Overcast"
    elif code in {45, 48}:
        return "Fog or depositing rime fog"
    elif code in {51, 53, 55}:
        return "Drizzle"
    elif code in {56, 57}:
        return "Freezing drizzle"
    elif code in {61, 63, 65}:
        return "Rain"
    elif code in {66, 67}:
        return "Freezing rain"
    elif code in {71, 73, 75}:
        return "Snow fall"
    elif code == 77:
        return "Snow grains"
    elif code in {80, 81, 82}:
        return "Rain showers"
    elif code in {85, 86}:
        return "Snow showers"
    elif code == 95:
        return "Thunderstorm: Slight or moderate"
    elif code in {96, 99}:
        return "Thunderstorm with hail"
    else:
        return "Unknown weather condition"


def get_weather(city_name):
    """
        Gets the current weather conditions for a city, including temperature, time, and weather description.
    """
    try:
        # Get city coordinates
        latitude, longitude = get_coordinates(city_name)

        # Query the Open-Meteo API to get the current weather
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True,
            "timezone": "auto"
        }
        response = retry_session.get(url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        print(f"[DEBUG] Dados brutos da API: {weather_data}")

        if "current_weather" in weather_data:
            current_weather = weather_data["current_weather"]
            temperature = current_weather["temperature"]
            weather_code = current_weather["weathercode"]
            timestamp = current_weather["time"]

            # Get climate code description
            weather_description = interpret_weather_code(weather_code)

            # Format the time
            datetime_obj = datetime.fromisoformat(timestamp)
            friendly_time = datetime_obj.strftime("%d de %B de %Y às %H:%M")

            # Debugging of the obtained data
            print(f"[DEBUG] Cidade: {city_name}, Temperatura: {temperature}°C, "
                  f"Descrição: {weather_description}, Horário: {friendly_time}")

            return temperature, friendly_time, weather_description
        else:
            raise ValueError(f"Weather data for '{city_name}' is unavailable.")
    except requests.RequestException as e:
        print(f"[ERROR] Falha na requisição: {e}")
        raise
    except Exception as e:
        print(f"[ERROR] Erro geral: {e}")
        raise
