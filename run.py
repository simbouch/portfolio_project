#!/usr/bin/env python3
"""
Local development server runner
"""
import os
from portfolio_app import create_app

if __name__ == '__main__':
    # Use development configuration for local testing
    app = create_app('config.DevelopmentConfig')
    
    # Run the development server
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=True
    )
