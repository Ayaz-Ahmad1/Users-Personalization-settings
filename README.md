# Flask Personalization Settings App

A simple Flask application for managing personalization settings for users, including themes, languages, and notification preferences.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- PostgreSQL

### Installing

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/flask-personalization-settings.git
    ```

2. Navigate to the project directory:

    ```bash
    cd User personalization settings
    ```

3. Install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Open `.env` and set the PostgreSQL database connection details:

    ```python
    
    DB_USERNAME = 'your_postgres_username'
    DB_PASSWORD = 'your_postgres_password'
    DB_HOST = 'localhost'
    DB_NAME = 'your_database_name'
    ```

2. Save the changes.

### Running the App

1. Ensure your PostgreSQL server is running.

2. Run the Flask application:

    ```bash
    python app.py
    ```

3. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the app.

## API Endpoints

### Get Personalization Settings

- **Endpoint:** `/personalization_settings/<int:user_id>`
- **Method:** GET
- **Description:** Retrieve personalization settings for a specific user.

### Save Personalization Settings

- **Endpoint:** `/personalization_settings/<int:user_id>`
- **Method:** POST
- **Description:** Save personalization settings for a specific user.

### Delete Personalization Settings

- **Endpoint:** `/personalization_settings/<int:user_id>`
- **Method:** DELETE
- **Description:** Delete personalization settings for a specific user.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback is highly appreciated.
