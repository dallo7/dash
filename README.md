# Integrate Analytics and Business Intelligence tool on Legacy Systems

## A Dash.Plotly Demo for the Community.


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-v2-orange)](https://dash.plotly.com/)
[![Plotly](https://img.shields.io/badge/Plotly-4.x-blue)](https://plotly.com/python/)
[![Pandas](https://img.shields.io/badge/pandas-1.x-blue)](https://pandas.pydata.org/)
[![Finance & Economics](https://img.shields.io/badge/Topic-Finance%20%26%20Economics-green)](https://en.wikipedia.org/wiki/Finance)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) 


This Dash application provides an interactive dashboard for analyzing and visualizing financial data related to agents, markets, and transactions across different regions. The focus is on integrating with existing legacy systems.

[![Dental Diagnosis Demo Video](https://github.com/dallo7/dash/blob/274bb928efd43772ac0f98e9f475fe0ac8fe798f/mtak.gif)](https://www.youtube.com/watch?v=<video-id>)
[![Dental Diagnosis Demo Video](https://github.com/dallo7/dash/blob/e529fdfb780d09d1d3979329c82ee54b9de19542/mtak.png)](https://www.youtube.com/watch?v=<video-id>)


You can access the tool hosted on render.com  https://integrate-using-dash.onrender.com (when you click the link give it at least a minute for the service to restart)

Username: root     Password: root123

Also, drag and drop the ~mtak.csv~ file into the web service once it's up for better insights.


## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Data](#data)
- [Contributing](#contributing)

## Project Overview

**Purpose:** The Integrate Analytics and Business Intelligence tool built using Dash.plotly on Legacy Systems. It enables users to gain insights into agent performance, market trends, regional transaction volumes, and more. 

**Target Users:**

- **Financial Analysts:**  To explore and understand transaction patterns, agent performance, and market dynamics.
- **Business Decision-Makers:** To make informed decisions based on data-driven insights.
- **Developers:** To learn how to integrate using Dash.Plotly to existing systems.

## Features

- **Interactive Dashboard:**
    - Visualizations:
        - Bar charts showing agent performance, market performance, transactions by sub-county, and transactions by county.
        - Pie chart illustrating the distribution of transactions across counties.
        - Interactive histogram for analyzing transaction trends over time.
    - Data Table: Upload and view financial data in a tabular format.
    - Filtering and Drill-down: Filter data by agents, markets, or counties to focus on specific aspects.
    - Animated Elements: Engaging Lottie animations enhance the visual appeal of the dashboard.

## Technologies

- **Dash:** Python framework for building web applications.
- **Dash Bootstrap Components (dbc):** For styling and layout.
- **Plotly:** For interactive data visualizations.
- **Pandas:** For data manipulation and analysis.
- **dash-extensions:** For incorporating Lottie animations.
- **Other:** base64, io, etc.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

 Install Dependencies:

    Bash
    pip install -r requirements.txt
    Use code with caution.                                       
                                          

 Ensure the data file mtak.csv is in the project directory.

    Bash
    Run the App:
    
    python app.py
    Use code with caution.
    
    The app should be accessible at http://127.0.0.1:5000/
                                                               
  
2. Usage
 * Access the App: Open your web browser and navigate to the app's URL.
 * Login: Enter your credentials (or use the defaults).
   
3. Explore the Dashboard:
 * View the various charts and graphs to analyze financial data.
 * Upload additional data using the upload component.
 * Filter data using the dropdown menus.
   
4. Data
 * mtak.csv: Sample dataset containing financial transaction information.
 * Key columns: Agents, Markets, Counties, Sub-counties, Transamount, TransTime.

Contributing
Contributions are welcome! Please follow the standard GitHub fork and pull request workflow.
