#!/usr/bin/env python3
"""
Email Configuration Test Script for Portfolio Contact Form

This script tests the email functionality of the portfolio contact form.
Run this script to verify that your email configuration is working correctly.

Usage:
    python test_email.py

Requirements:
    - Set up environment variables for email configuration
    - Ensure Flask-Mail is installed (pip install Flask-Mail)
"""

import os
import sys
from flask import Flask
from flask_mail import Mail, Message
from config import Config


def test_email_configuration():
    """Test email configuration and send a test email."""

    print("🧪 Testing Portfolio Email Configuration")
    print("=" * 50)

    # Create Flask app for testing
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Flask-Mail
    mail = Mail(app)

    # Check configuration
    print("📧 Email Configuration:")
    print(f"   MAIL_SERVER: {app.config.get('MAIL_SERVER', 'Not set')}")
    print(f"   MAIL_PORT: {app.config.get('MAIL_PORT', 'Not set')}")
    print(f"   MAIL_USE_TLS: {app.config.get('MAIL_USE_TLS', 'Not set')}")
    print(f"   MAIL_USERNAME: {app.config.get('MAIL_USERNAME', 'Not set')}")
    print(
        f"   MAIL_PASSWORD: {'Set' if app.config.get('MAIL_PASSWORD') else 'Not set'}"
    )
    print(f"   CONTACT_EMAIL: {app.config.get('CONTACT_EMAIL', 'Not set')}")
    print()

    # Check if email is configured
    if not app.config.get("MAIL_CONFIGURED", False):
        print("❌ Email is not properly configured!")
        print("\n📝 To configure email:")
        print("1. Copy .env.example to .env")
        print("2. Fill in your email credentials in .env file")
        print("3. For Gmail, use App Passwords (not your regular password)")
        print("4. Run this test again")
        return False

    # Test email sending
    print("📤 Testing email sending...")

    try:
        with app.app_context():
            # Create test message
            msg = Message(
                subject="Portfolio Contact Form Test",
                sender=app.config.get("MAIL_USERNAME"),
                recipients=[app.config.get("CONTACT_EMAIL")],
                reply_to="test@example.com",
            )

            msg.body = """This is a test email from your portfolio contact form.

Name: Test User
Email: test@example.com
Subject: Email Configuration Test

Message:
This is a test message to verify that your email configuration is working correctly.
If you receive this email, your contact form is ready to use!

---
This is an automated test email from your portfolio application."""

            msg.html = """
            <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <h2 style="color: #3498db;">Portfolio Contact Form Test</h2>
                <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
                    <p><strong>Name:</strong> Test User</p>
                    <p><strong>Email:</strong> <a href="mailto:test@example.com">test@example.com</a></p>
                    <p><strong>Subject:</strong> Email Configuration Test</p>
                </div>
                <div style="background: white; padding: 20px; border-left: 4px solid #3498db;">
                    <h3>Message:</h3>
                    <p style="line-height: 1.6;">
                        This is a test message to verify that your email configuration is working correctly.<br>
                        If you receive this email, your contact form is ready to use!
                    </p>
                </div>
                <hr style="margin: 30px 0;">
                <p style="color: #666; font-size: 14px;">
                    This is an automated test email from your portfolio application.
                </p>
            </div>
            """

            # Send the email
            mail.send(msg)
            print("✅ Test email sent successfully!")
            print(f"📬 Check your inbox at: {app.config.get('CONTACT_EMAIL')}")
            return True

    except Exception as e:
        print(f"❌ Error sending test email: {str(e)}")
        print("\n🔧 Troubleshooting tips:")
        print("1. Check your email credentials in .env file")
        print("2. For Gmail, ensure you're using an App Password")
        print("3. Verify your email provider's SMTP settings")
        print("4. Check if 2-factor authentication is enabled")
        return False


def check_environment_variables():
    """Check if required environment variables are set."""

    print("🔍 Checking Environment Variables")
    print("=" * 50)

    required_vars = ["MAIL_SERVER", "MAIL_USERNAME", "MAIL_PASSWORD", "CONTACT_EMAIL"]

    missing_vars = []

    for var in required_vars:
        value = os.environ.get(var)
        if value:
            if var == "MAIL_PASSWORD":
                print(f"✅ {var}: {'*' * len(value)}")
            else:
                print(f"✅ {var}: {value}")
        else:
            print(f"❌ {var}: Not set")
            missing_vars.append(var)

    print()

    if missing_vars:
        print(f"❌ Missing environment variables: {', '.join(missing_vars)}")
        print("\n📝 Setup instructions:")
        print("1. Copy .env.example to .env")
        print("2. Edit .env file with your email credentials")
        print(
            "3. Source the environment: source .env (Linux/Mac) or set variables manually"
        )
        return False
    else:
        print("✅ All required environment variables are set!")
        return True


def main():
    """Main function to run email tests."""

    print("🚀 Portfolio Email Configuration Test")
    print("=" * 50)
    print()

    # Check environment variables
    env_ok = check_environment_variables()
    print()

    if not env_ok:
        print("❌ Environment setup incomplete. Please configure your .env file first.")
        sys.exit(1)

    # Test email configuration
    email_ok = test_email_configuration()
    print()

    if email_ok:
        print("🎉 Email configuration test completed successfully!")
        print("Your portfolio contact form is ready to receive messages.")
    else:
        print("❌ Email configuration test failed.")
        print("Please check your configuration and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()
