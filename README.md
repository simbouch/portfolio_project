# AI Developer Portfolio - Bouchaib Khribech

A modern, responsive portfolio website showcasing AI development, data science, and machine learning expertise. Built with Flask and enhanced with dynamic content management, professional design, and comprehensive project showcase.

## 🚀 Live Demo

**[View Portfolio](https://portfolio-bk-sfn6.onrender.com)**

## 👨‍💻 About

I'm Bouchaib Khribech, an AI Developer and Data Scientist currently training at Simplon Microsoft AI Program in Nancy, France. With 15+ years of analytical expertise in biomedical engineering and forensic sciences, I specialize in developing intelligent solutions using cutting-edge AI technologies.

## ✨ Features

- **🏠 Dynamic Home Page**: Interactive hero section with featured projects and skills
- **👤 About Page**: Comprehensive professional summary and background
- **💼 Experience Page**: Detailed work history with achievements and technologies
- **🚀 Projects Page**: Showcase of major AI/ML projects with live demos and code links
- **🛠️ Skills Page**: Interactive skills visualization with proficiency levels
- **📧 Contact Page**: Professional contact form with multiple communication options
- **📱 Responsive Design**: Optimized for all devices and screen sizes
- **🎨 Modern UI/UX**: Professional design with smooth animations and interactions

## 🛠️ Technologies Used

### Backend
- **Flask**: Python web framework with factory pattern
- **SQLAlchemy**: Database ORM with dynamic data models
- **Flask-Mail**: Email functionality for contact forms
- **Gunicorn**: Production WSGI server

### Frontend
- **HTML5 & CSS3**: Modern semantic markup and styling
- **Bootstrap 4**: Responsive grid system and components
- **Font Awesome**: Professional icon library
- **Custom CSS**: Enhanced styling with gradients and animations

### Database
- **SQLite**: Development database
- **PostgreSQL**: Production database support

### Deployment
- **Render**: Cloud platform deployment
- **Git**: Version control and CI/CD

## 🏗️ Project Structure

```
portfolio_project/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── models/
│   │   ├── project.py           # Project data model
│   │   ├── experience.py        # Experience data model
│   │   └── skill.py             # Skills data model
│   └── controllers/             # Route controllers (optional)
├── templates/
│   ├── base.html               # Base template
│   ├── index.html              # Home page
│   ├── about.html              # About page
│   ├── experience.html         # Experience page
│   ├── projects.html           # Projects page
│   ├── skills.html             # Skills page
│   └── contact.html            # Contact page
├── static/
│   ├── css/
│   │   └── styles.css          # Custom styling
│   └── images/                 # Profile images
├── config.py                   # Configuration settings
├── app.py                      # WSGI entry point
├── run.py                      # Development server
├── test_app.py                 # Application tests
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 🚀 Featured Projects

### 1. RPA POC System for PDF Information Extraction
- **Technologies**: Python, OCR (Tesseract, EasyOCR, PaddleOCR), AI Agents, FastAPI
- **Description**: Intelligent RPA system using AI for automated PDF processing

### 2. Flashcards Full-Stack Platform with OCR
- **Technologies**: FastAPI, Vue.js, OCR, French LLM, PostgreSQL
- **Description**: Learning platform with OCR capabilities and LLM integration

### 3. Audio Analysis Toolkit
- **Technologies**: Python, Librosa, Streamlit, NumPy, Matplotlib
- **Description**: Comprehensive audio analysis with interactive visualization

### 4. Malaria Detection Application
- **Technologies**: Django, TensorFlow, CNN, Computer Vision
- **Description**: Deep learning application for medical image classification

### 5. Clustering Flask Web Application
- **Technologies**: Flask, Scikit-learn, PCA, K-Means, Plotly
- **Description**: Interactive ML application with data visualization

## 💡 Core Skills

- **AI & Machine Learning**: LLM, Deep Learning, Computer Vision, AI Agents
- **OCR Technologies**: Tesseract, EasyOCR, PaddleOCR
- **Web Development**: FastAPI, Django, Flask, Vue.js
- **Data Science**: Python, Pandas, NumPy, Scikit-learn, Streamlit
- **Deep Learning**: TensorFlow, PyTorch, CNN
- **Tools**: Git, Docker, Linux

## 🔧 Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/simbouch/portfolio_project.git
   cd portfolio_project
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run development server**:
   ```bash
   python run.py
   ```

5. **Open browser**: Navigate to `http://localhost:5000`

## 🧪 Testing

Run the test suite to verify functionality:

```bash
python test_app.py
```

Or use pytest for more detailed testing:

```bash
pytest test_app.py -v
```

## 🚀 Deployment

### Render Deployment

This application is configured for automatic deployment on Render:

1. **Environment Variables**:
   - `FLASK_CONFIG`: Set to `config.ProductionConfig`
   - `SECRET_KEY`: Your secret key for sessions
   - `DATABASE_URL`: PostgreSQL database URL (optional)

2. **Build Command**: `pip install -r requirements.txt`

3. **Start Command**: `gunicorn app:app`

### Local Production Testing

Test production configuration locally:

```bash
gunicorn app:app --bind 0.0.0.0:8000
```

## 📧 Contact

- **Email**: [simplonbouchaib@gmail.com](mailto:simplonbouchaib@gmail.com)
- **LinkedIn**: [linkedin.com/in/khbouchaib](https://www.linkedin.com/in/khbouchaib)
- **GitHub**: [github.com/simbouch](https://github.com/simbouch)
- **Location**: Nancy, France

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Simplon Microsoft AI Program** for the comprehensive AI training
- **Flask Community** for the excellent web framework
- **Bootstrap Team** for the responsive design framework
- **Font Awesome** for the professional icons
