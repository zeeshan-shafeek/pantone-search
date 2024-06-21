
# Pantone Color Lookup Flask Application

This is a simple Flask application that allows users to enter a Pantone TCX color code and get the corresponding color information, including the color name and hex value. The application displays the color as a color box on the webpage.

## Screenshots

### Homepage
![Homepage](https://i.imgur.com/XyXCUZZ.png)

### Search Result Page
![Search Result Page](https://i.imgur.com/zRjZKjL.png)

## Setup Instructions

Follow these steps to set up and run the application:

### Prerequisites

- Python 3.x installed on your system.
- `pip` (Python package installer) installed.

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

```sh
git clone https://github.com/zeeshan-shafeek/pantone-search
cd flask_pantone
```

### Step 2: Install Dependencies

Install the required Python packages using `pip`:

```sh
pip install Flask pycolorname
```

### Step 3: Run the Flask Application

Navigate to the project directory and run the Flask application using the following command:

```sh
python app.py
```

### Step 4: Access the Application

Open your web browser and go to `http://127.0.0.1:5000/`. 

### Usage

- Enter a Pantone TCX code (e.g., "19-6110 TPX") in the search box and submit.
- The page should display the color box, Pantone code, color name, and hex value.
