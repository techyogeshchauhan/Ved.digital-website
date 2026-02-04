from flask import Flask, render_template, request, redirect, url_for, flash
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

# Disable caching in development mode
if app.debug:
    # Set max age to 0 to disable caching of static files
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    
    @app.after_request
    def add_no_cache_headers(response):
        """Add headers to prevent caching during development"""
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response
    
    @app.context_processor
    def override_url_for():
        """Add timestamp to static files to force reload"""
        return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    """Add timestamp query parameter to static files"""
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            if os.path.isfile(file_path):
                values['v'] = int(os.stat(file_path).st_mtime)
            else:
                # If file doesn't exist, use current timestamp
                values['v'] = int(datetime.now().timestamp())
    return url_for(endpoint, **values)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/insights')
def insights():
    return render_template('insights.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        service = request.form.get('service')
        message = request.form.get('message')
        
        # Here you would typically send an email or save to database
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
