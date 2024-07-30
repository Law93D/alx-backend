0x02. i18n
Back-end

Task 1: Basic Babel Setup
Install Flask-Babel:
bash
Copy code
pip3 install flask_babel==2.0.0
Create 1-app.py:
Set up Babel with a Config class
Set LANGUAGES to ["en", "fr"]
Default locale to "en" and timezone to "UTC"
Update the template to 1-index.html:
Task 2: Get Locale from Request
Create 2-app.py:
Add get_locale function using babel.localeselector
Determine the best match for supported languages using request.accept_languages
Update the template to 2-index.html:
Task 3: Parametrize Templates
Parametrize Templates with gettext:
Use _ function to parametrize messages.
Create babel.cfg file.
Extract translations:
bash
Copy code
pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fr
Edit messages.po files for both languages.
Compile dictionaries:
bash
Copy code
pybabel compile -d translations
Create 3-app.py and 3-index.html:
Task 4: Force Locale with URL Parameter
Update get_locale function in 4-app.py:
Check for locale parameter in URL.
Update template to 4-index.html.
Task 5: Mock Logging In
Create 5-app.py:
Define users dictionary.
Implement get_user function.
Add before_request function.
Update template to 5-index.html.
Task 6: Use User Locale
Update get_locale function in 6-app.py:
Check for locale from user settings.
Update template to 6-index.html.
Task 7: Infer Appropriate Time Zone
Define get_timezone function in 7-app.py:
Check for timezone parameter in URL.
Validate time zones using pytz.
Update template to 7-index.html.
Task 8: Display the Current Time (Advanced)
Update 7-app.py:
Display current time based on inferred time zone.
Use translations for time display.
Update templates and messages.po files accordingly.
Final Steps
Manual QA Review:

Ensure all tasks are correctly implemented.
Request manual QA review after completion.
Run Auto Review:

Ensure code adheres to all project requirements.
Check for pycodestyle compliance and documentation.
