# QSurvey

**QSurvey** is an intuitive and feature-rich tool designed to simplify the creation and analysis of surveys. Built with Django, this platform provides users with seamless survey creation, data collection, and analytical dashboards to gain actionable insights.

## Features
- User management with custom profiles.
- Dynamic survey creation and sharing.
- Real-time survey analytics.
- Notification system for responses and activity.
- API support for third-party integrations.
- Customizable admin tools for survey monitoring.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/salahsaeed19/QSurvey.git
   cd QSurvey
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations and run the server:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.