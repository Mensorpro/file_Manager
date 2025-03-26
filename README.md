# File Management System

[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-5.1+-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A secure and user-friendly file management system built with Django and Tailwind CSS that allows users to upload, download, and manage their files.

![Preview](docs/preview.png)

## Features

- 🔐 Secure user authentication (login/register)
- 📁 File upload with type restrictions (.jpg, .png, .pdf, .docx)
- 📥 File download functionality
- 🗑️ File deletion with confirmation
- 📊 File size display and management
- 🎨 Modern UI with Tailwind CSS
- 🔍 File type identification with colored icons
- 📱 Fully responsive design

## Requirements

- Python 3.13+
- Django 5.1+
- Other dependencies listed in `pyproject.toml`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mensorpro/file_Manager.git
cd file_Manager
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the example environment file and configure it:
```bash
copy .env.example .env
```

5. Apply database migrations:
```bash
python manage.py migrate
```

6. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Quick Start

After installation, you can:
1. Access the admin interface at `/admin`
2. Register a new user account at `/register`
3. Login at `/login`
4. Start managing your files at `/files`

## Configuration

Key settings in `settings.py`:

- `MAX_UPLOAD_SIZE`: Maximum file size (default: 5MB)
- `ALLOWED_FILE_TYPES`: Allowed file extensions ['.jpg', '.png', '.pdf', '.docx']
- `MEDIA_ROOT`: Upload directory location
- `MEDIA_URL`: URL prefix for uploaded files

## Usage

1. Register a new account or login
2. Navigate to the upload page
3. Select files that match the allowed types
4. View your files in the file list
5. Download or delete files as needed

## File Type Support

- 📷 Images: .jpg, .png
- 📄 Documents: .docx
- 📑 PDF: .pdf

## Security Features

- User authentication required for all file operations
- File type validation
- File size restrictions
- Secure file storage
- CSRF protection
- User-specific file access

## Directory Structure

```
filemanager/
├── filemanager/        # Project settings and main URLs
├── files/             # File management application
├── media/            # Uploaded files storage
├── templates/        # HTML templates
└── static/          # Static files (CSS, JS, etc.)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details
