"""Application runner script"""
# Main application runner
import sys
from app import app

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
