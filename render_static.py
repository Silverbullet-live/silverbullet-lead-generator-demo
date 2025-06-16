from main import app
from flask import render_template
import os

os.makedirs('static_site', exist_ok=True)

with app.app_context():
    with app.test_request_context():
        # Render login page
        rendered_login = render_template('login.html')
        with open('static_site/login.html', 'w') as f:
            f.write(rendered_login)

        # Render lead qualifier page
        rendered_lead_qualifier = render_template('lead_qualifier.html')
        with open('static_site/lead_qualifier.html', 'w') as f:
            f.write(rendered_lead_qualifier)

        # Render results page (empty results for static version)
        rendered_results = render_template('results.html', results=[])
        with open('static_site/results.html', 'w') as f:
            f.write(rendered_results)

        # Optionally, copy login.html as index.html for GitHub Pages
        with open('static_site/login.html', 'r') as src, open('static_site/index.html', 'w') as dst:
            dst.write(src.read())