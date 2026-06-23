from pathlib import Path

structure = [
    "bot/handlers",
    "bot/services",
    "bot/database",
    "miniapp/css",
    "miniapp/js",
    "miniapp/assets/icons",
    "miniapp/assets/fonts",
    "n8n-workflows",
    "docs",
]

files = [
    "bot/main.py",
    "bot/config.py",
    "bot/requirements.txt",

    "bot/handlers/__init__.py",
    "bot/handlers/start.py",
    "bot/handlers/portfolio.py",
    "bot/handlers/menu.py",

    "bot/services/__init__.py",
    "bot/services/price_service.py",
    "bot/services/wallet_service.py",
    "bot/services/chart_service.py",

    "bot/database/__init__.py",
    "bot/database/models.py",
    "bot/database/db.py",

    "miniapp/index.html",
    "miniapp/more.html",
    "miniapp/css/style.css",
    "miniapp/css/animations.css",
    "miniapp/js/app.js",
    "miniapp/js/api.js",
    "miniapp/js/portfolio.js",

    # فایل نگه‌دارنده برای فولدرهای خالی (تا گیت آن‌ها را track کند)
    "miniapp/assets/icons/.gitkeep",
    "miniapp/assets/fonts/.gitkeep",

    "n8n-workflows/price-scheduler.json",
    "n8n-workflows/alert-trigger.json",

    "docs/project-brief.docx",

    ".env.example",
    ".gitignore",
    "README.md",
]

for folder in structure:
    Path(folder).mkdir(parents=True, exist_ok=True)

for file in files:
    Path(file).touch(exist_ok=True)

print("✅ Project structure created successfully!")