# Django Portfolio Site

Minimal Django portfolio app ready for deployment. Features:
- Navigation sections: Home, About, Projects, Contact
- CDN icons (Font Awesome), AOS (Animate On Scroll) for animations, and simple JS interactions
- Proper templating with base.html and section templates
- Static files inside `portfolio/static/portfolio/`

Quick start (local):
1. python -m venv venv
2. source venv/bin/activate   (Windows: venv\Scripts\activate)
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

For deployment: Vercel can run Django via serverless or by using a Dockerfile. Provide a small adapter or use Render/Heroku for simplest experience.
