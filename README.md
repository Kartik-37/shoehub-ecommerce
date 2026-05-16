[README.md](https://github.com/user-attachments/files/27842123/README.md)

# 👟 ShoeHub — Modern Footwear E-Commerce Platform

<div align="center">

![ShoeHub Logo](https://shoehub-ecommerce.onrender.com/static/image/logo/Logo2.png)

**A full-stack e-commerce web application for footwear — built with Django and deployed on Render.**

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-ShoeHub-blue?style=for-the-badge)](https://shoehub-ecommerce.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-Web_Framework-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com)

</div>

---

## 🔗 Live Demo

> **[https://shoehub-ecommerce.onrender.com](https://shoehub-ecommerce.onrender.com)**

---

## 📌 About The Project

**ShoeHub** is a fully functional e-commerce website for footwear, featuring product listings for Men, Women, and Kids. Users can browse categories, view product details, add items to their cart, and register/login to their account. The project is deployed live on Render with a production-ready configuration.

---

## ✨ Features

- 🛍️ **Product Catalog** — Browse Men, Women, and Kids shoe collections
- 🔍 **Category Filtering** — Filter by Gym, Hike, Work, and Running sneakers
- 🛒 **Shopping Cart** — Add products to cart and manage orders
- 👤 **User Authentication** — Register, login, and manage your account
- 📄 **Product Detail Pages** — View full product info and pricing
- 📱 **Responsive Design** — Optimized for desktop and mobile
- 💳 **Secure Checkout Flow** — Structured invoice and cart system
- 🚀 **Deployed on Render** — Live and accessible online

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python, Django |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Database** | SQLite (dev) |
| **Deployment** | Render |
| **Static Files** | Django Static Files |

---

## 📁 Project Structure

```
shoehub-ecommerce/
│
├── home/               # Main Django app (views, models, URLs)
├── example/            # Example/template app
├── image/              # Static images
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── build.sh            # Render build script
├── render.yaml         # Render deployment config
├── runtime.txt         # Python runtime version
└── data.json           # Fixture data for products
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Kartik-37/shoehub-ecommerce.git
cd shoehub-ecommerce

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. Load product data
python manage.py loaddata data.json

# 5. Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 🌐 Deployment

This project is deployed on **[Render](https://render.com)** using:

- `render.yaml` — Service configuration
- `build.sh` — Build commands (install dependencies, collect static files, run migrations)
- `runtime.txt` — Specifies Python version

---

## 📸 Screenshots

> **Homepage** — [View Live](https://shoehub-ecommerce.onrender.com)

| Section | Preview |
|--------|---------|
| 🏠 Homepage | Hero slider with featured collections |
| 👟 Men's Collection | Full range of men's footwear |
| 👠 Women's Collection | Trending women's styles |
| 👦 Kids' Collection | Comfortable kids' shoes |

---

## 📬 Contact

**Kartik** — Developer & Designer

- 🔗 GitHub: [@Kartik-37](https://github.com/Kartik-37)
- 🌐 Live Project: [shoehub-ecommerce.onrender.com](https://shoehub-ecommerce.onrender.com)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
Made with ❤️ by <a href="https://github.com/Kartik-37">Kartik</a>
</div>
