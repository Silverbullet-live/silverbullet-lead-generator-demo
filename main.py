import sys
sys.path.append('.')
from flask import Flask, render_template, request, redirect, url_for, flash, session
from agents.silverbullet_lead_generator import SilverBulletLeadGenerator
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('lead_qualifier.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your authentication logic here
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/generate', methods=['POST'])
def generate():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    company_info = request.form.get('company_info')
    if not company_info:
        flash('Please provide company information')
        return redirect(url_for('index'))
    
    agent = SilverBulletLeadGenerator()
    results = agent.generate_leads(company_info)
    
    return render_template('results.html', results=results)


    # Render login page
    rendered_login = render_template('login.html')
    with open('static_site/login.html', 'w') as f:
        f.write(rendered_login)

    # Render lead qualifier page (if you have one)
    rendered_lead_qualifier = render_template('lead_qualifier.html')
    with open('static_site/lead_qualifier.html', 'w') as f:
        f.write(rendered_lead_qualifier)

    # Render results page (if you have one)
    rendered_results = render_template('results.html', results=[])
    with open('static_site/results.html', 'w') as f:
        f.write(rendered_results)

    # Optionally, copy login.html as index.html for GitHub Pages
    with open('static_site/login.html', 'r') as src, open('static_site/index.html', 'w') as dst:
        dst.write(src.read()) 