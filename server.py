from email import message
from flask import Flask, render_template, request
from weather import get_weather
from waitress import serve
import requests
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    # Home page with form to search for weather
    return render_template('index.html')


@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city', '').strip()
    if not city:
        return render_template('city-not-found.html', message="Please enter a valid city.")

    try:
        temperature, timestamp, description = get_weather(city)
        return render_template(
            'weather.html',
            title=city,
            temp=temperature,
            time=timestamp,
            status="The weather is currently: ",
            description=description
        )
    except ValueError as e:
        # For cities not found or data unavailable
        return render_template('city-not-found.html', message=str(e))
    except requests.RequestException as e:
        # For connectivity or API issues
        return render_template('city-not-found.html', message="API request failed. Please try again later.")
    except Exception as e:
        # Para erros gerais
        return render_template('city-not-found.html', message=f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    # Run the server using Waitress
    serve(app, host="0.0.0.0", port=8000)
