# Football Match Analysis Tool

## Project Overview

This project is a Football Match Analysis Tool built with Python and Flask. It leverages the Football-Data.org API to retrieve and analyze football match statistics. Users can compare various teams' performances, visualize match outcomes, and gain insights into different aspects of the game through interactive graphs.

The project is designed to be **run as a Docker container** for ease of deployment and consistency, but it can also be executed locally on your machine.

## Features

1. Fetch Football Data: Retrieve live football match data from the Football-Data.org API.
2. Data Analysis: Process and analyze match statistics, including goals, assists, and possession.
3. Data Visualization: Display statistics through interactive graphs.
4. Web Interface: Access the analysis through a simple web interface built with Flask.

## Getting Started

### Docker Setup

To run the project using Docker, follow the steps below:

1. Clone the Repository:
  ```
  git clone https://github.com/yourusername/football-analysis-tool.git
   
  cd football-analysis-tool
  ```

2. Build the Docker Image:
  ```
  docker build -t football-analysis-tool .
  ```

3. Run the Docker Container:
  ```
  docker run -p 5000:5000 football-analysis-tool
  ```

4. Access the Web Interface:

   Open your browser and navigate to http://localhost:5000 to interact with the application.


## Running Locally

If you prefer to run the project on your local machine without Docker, follow these steps:

1. Clone the Repository:
  ```
  git clone https://github.com/yourusername/football-analysis-tool.git

  cd football-analysis-tool
  ```

2. Set Up a Virtual Environment (optional but recommended):
  ```
  python3 -m venv venv

  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

3. Install Dependencies:
  ```
  pip install -r requirements.txt
  ```

4. Run the Application:
  ```
  python app.py
  ```

5. Access the Web Interface:

   Open your browser and navigate to http://localhost:5000 to view the application.
  

## API Key

To use the Football-Data.org API, you'll need an API key. Register at Football-Data.org to obtain your key, and add it to the project by replacing "YOUR_API_KEY" in main/data_fetcher.py.

## Project Structure

```
.
├── Dockerfile
├── app.py
├── main/
│   ├── collect.py
│   ├── process.py
│   ├── visualize.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

1. app.py: The main entry point for the Flask application.
2. main/collect.py: Handles fetching data from the Football-Data.org API.
3. main/process.py: Processes the retrieved data into a usable format.
4. main/visualize.py: Generates graphs and visualizations from the data.
5. templates/index.html: The HTML template for rendering the web interface.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
