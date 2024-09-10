import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState({});
  const [location, setLocation] = useState('');

  const apiKey = process.env.REACT_APP_WEATHER_API_KEY;

  // Split location input into city, state, and country (if provided)
  const [city, stateCode, countryCode] = location.split(',').map(part => part.trim());

  const searchLocation = (event) => {
    if (event.key === 'Enter') {
      // Fetch coordinates using the Geocoding API
      const geoURL = `http://api.openweathermap.org/geo/1.0/direct?q=${city},${stateCode},${countryCode}&limit=1&appid=${apiKey}`;

      axios.get(geoURL)
        .then((geoResponse) => {
          if (geoResponse.data.length > 0) {
            // Extract latitude, longitude, state, and country
            const { lat, lon, state, country } = geoResponse.data[0];
            console.log('GeoData:', { lat, lon, state, country });

            // Use the coordinates to fetch weather data
            const weatherURL = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;

            return axios.get(weatherURL);
          } else {
            console.error('No location data found');
          }
        })
        .then((weatherResponse) => {
          if (weatherResponse) {
            setData(weatherResponse.data);
            console.log('Weather Data:', weatherResponse.data);
          }
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
        });

      setLocation(''); // Clear input field
    }
  };

  // Function to convert Celsius to Fahrenheit
  const convertToFahrenheit = (celsius) => {
    return (celsius * 9 / 5) + 32;
  };

  return (
    <div className="app">
      <div className="search">
        <input
          value={location}
          onChange={(event) => setLocation(event.target.value)}
          onKeyDown={searchLocation}
          placeholder="Enter Location (e.g., Miami, FL, US)"
          type="text"
        />
      </div>

      <div className="container">
        <div className="top">
          <div className="location">
            <p>{data.name}</p> {/* Display location */}
          </div>
          <div className="temp">
            {data.main ? (
              <div>
                <h1>{Math.round(data.main.temp)}°C</h1> {/* Celsius */}
                <h1>{Math.round(convertToFahrenheit(data.main.temp))}°F</h1> {/* Fahrenheit */}
              </div>
            ) : null}
          </div>
          <div className="description">
            {data.weather ? <h1>{data.weather[0].main}</h1> : null} {/* Weather condition */}
          </div>
        </div>

        {data.name !== undefined && (
          <div className="bottom">
            <div className="feels-like">
              {data.main ? (
                <div>
                  <p className="bold">{Math.round(data.main.feels_like)}°C/{Math.round(convertToFahrenheit(data.main.feels_like))}°F</p> {/* Feels like in Celsius */}
                </div>
              ) : null}
              <p>Feels like</p>
            </div>
            <div className="humidity">
              {data.main ? <p className="bold">{data.main.humidity}%</p> : null}
              <p>Humidity</p>
            </div>
            <div className="wind">
              {data.wind ? <p className="bold">{data.wind.speed} m/s</p> : null}
              <p>Wind Speed</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
