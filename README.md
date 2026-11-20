# Python Weather Information App

A simple Python-based weather application that retrieves real-time weather information for cities around the world using the Open-Meteo API.

## Features

- Search weather information by city name.
- Display current temperature.
- Show feels-like temperature.
- Display weather conditions.
- Show humidity levels.
- Display wind speed.
- Show precipitation information.
- Support repeated city searches.
- Handle invalid city names and connection errors.

## Technologies Used

- Python
- Requests
- Open-Meteo API

## Project Structure

```text
python-weather-information-app/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone this repository:

```bash
git clone https://github.com/pradipta-web/python-weather-information-app.git
```

2. Navigate to the project directory:

```bash
cd python-weather-information-app
```

3. Create a virtual environment:

```bash
py -m venv venv
```

4. Install dependencies:

```bash
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Usage

Run the application:

```bash
.\venv\Scripts\python.exe app.py
```

Enter a city name to retrieve its current weather information.

## API

This project uses the free Open-Meteo API:

- Weather API: https://open-meteo.com/
- Geocoding API: https://open-meteo.com/en/docs/geocoding-api

No API key is required.

## Author

**Kinervaaa**

GitHub: https://github.com/pradipta-web