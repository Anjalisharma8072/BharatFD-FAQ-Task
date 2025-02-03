# BharatFD FAQ System

## Overview
A comprehensive FAQ management system developed with Django, offering RESTful APIs for managing Frequently Asked Questions (FAQs) in multiple languages. The system provides complete CRUD operations and robust multilingual support.

## Key Features
- 🌐 Support for multiple languages
- 🔍 Advanced filtering capabilities
- 📦 Modular and extensible design

## Technology Stack
- 🔧 **Backend**: Django (Python)
- 🚀 **API**: Django REST Framework
- 💾 **Database**: SQLite (default)

## API Endpoints

### Core Functionality

1. **Get All FAQs**
    ```
    GET /api/faqs/
    ```

2. **Get Language-Specific FAQs**
    ```
    GET /api/faqs/?lang={language_code}
    ```

## Setup Guide

### Requirements
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Get the Code**
    ```bash
    git clone https://github.com/Anjalisharma8072/BharatFD-FAQ-Task.git
    cd faq
    cd faq_project
    ```

2. **Setup Environment**
    ```bash
    pip install -r requirements.txt
    ```

3. **Initialize Database**
    ```bash
    python manage.py migrate
    ```

4. **Run the Server**
    ```bash
    python manage.py runserver
    ```

### Access Points
- Main API: `http://127.0.0.1:8000/api/faqs/`
- Language-specific: `http://127.0.0.1:8000/api/faqs/?lang=hi`

### Supported Languages
- 🇺🇸 English (en)
- 🇮🇳 Hindi (hi)
- 🇧🇩 Bengali (bn)
- 🇪🇸 Spanish (es)
- 🇫🇷 French (fr)
- 🇸🇦 Arabic (ar)
- 🇵🇹 Portuguese (pt)
- 🇷🇺 Russian (ru)
- 🇩🇪 German (de)
- 🇯🇵 Japanese (ja)
- 🇰🇷 Korean (ko)
- 🇮🇹 Italian (it)

## Development Guidelines
- ✅ Test all API endpoints thoroughly
- 🔤 Use correct language codes for filtering

## admin credentials
- username-anjali
- password - 123456