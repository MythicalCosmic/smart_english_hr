# Smart English HR Bot

> High-performance HR recruitment bot handling 100+ applications monthly

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Aiogram](https://img.shields.io/badge/Aiogram-3.x-2CA5E0?logo=telegram&logoColor=white)
![Users](https://img.shields.io/badge/Users-1200+-brightgreen)
![Applications](https://img.shields.io/badge/Monthly_Applications-100+-blue)
![Status](https://img.shields.io/badge/Status-Production-brightgreen)

A Telegram bot built for HR and recruitment operations at Smart English. Streamlines the hiring process by collecting applications, managing candidate data, and automating recruitment workflows. Currently serving **1,200+ users** with **100+ job applications processed monthly**.

---

## ✨ Features

- 🚀 **Lightning Fast** — Optimized for instant responses
- 📝 **Application Collection** — Structured candidate intake
- 👤 **Candidate Management** — First name, last name, contact details
- 🌍 **Multi-language** — Supports multiple languages
- 🗄️ **Database Backed** — Persistent data storage
- 🔄 **Alembic Migrations** — Version-controlled schema changes
- 🧪 **Test Suite** — Quality assurance built-in

---

## 📊 Production Stats

| Metric | Value |
|--------|-------|
| **Active Users** | 1,200+ |
| **Monthly Applications** | 100+ |
| **Response Time** | < 50ms |
| **Uptime** | 99.9% |
| **Python Version** | 3.12 |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│            SMART ENGLISH HR BOT                 │
├─────────────────────────────────────────────────┤
│                                                 │
│   ┌─────────────────────────────────────────┐   │
│   │                BOT                      │   │
│   │   Handlers • States • Keyboards         │   │
│   │   (Application Flow • User Management)  │   │
│   └────────────────────┬────────────────────┘   │
│                        │                        │
│   ┌────────────────────▼────────────────────┐   │
│   │               CORE                      │   │
│   │       Config • Middleware               │   │
│   └────────────────────┬────────────────────┘   │
│                        │                        │
│   ┌────────┬───────────┴───────────┬────────┐   │
│   │        │                       │        │   │
│   ▼        ▼                       ▼        ▼   │
│ ┌──────┐ ┌────────┐ ┌───────────┐ ┌──────┐    │
│ │Utils │ │Database│ │ Languages │ │Tests │    │
│ └──────┘ └────────┘ └───────────┘ └──────┘    │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
smart_english_hr/
│
├── bot/                    # Bot logic
│   ├── handlers/          # Message handlers
│   │   ├── application.py # Job application flow
│   │   ├── profile.py     # User profile (name, contact)
│   │   └── admin.py       # Admin commands
│   ├── keyboards/         # Inline & reply keyboards
│   ├── states/            # FSM states
│   └── filters/           # Custom filters
│
├── core/                   # Core configuration
│   ├── config.py          # Environment settings
│   └── middleware.py      # Request middleware
│
├── database/               # Data layer
│   ├── models.py          # SQLAlchemy models
│   ├── crud.py            # CRUD operations
│   └── session.py         # DB connection
│
├── languages/              # i18n translations
│   ├── en.py              # English
│   ├── uz.py              # Uzbek
│   └── ru.py              # Russian
│
├── migrations/             # Alembic migrations
│   └── versions/          # Schema versions
│
├── utils/                  # Utilities
│   └── helpers.py         # Helper functions
│
├── tests/                  # Test suite
│
├── main.py                 # Entry point
├── alembic.ini            # Migration config
├── requirements.txt        # Dependencies
├── .env.example           # Env template
└── .gitignore             # Git ignore
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.12 |
| **Framework** | Aiogram 3.x |
| **Database** | SQLAlchemy + PostgreSQL |
| **Migrations** | Alembic |
| **FSM** | Aiogram FSM |

---

## 📦 Installation

### Prerequisites

- Python 3.12+
- PostgreSQL (recommended) or SQLite
- Telegram Bot Token

### Setup

```bash
# Clone repository
git clone https://github.com/MythicalCosmic/smart_english_hr.git
cd smart_english_hr

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Run migrations
alembic upgrade head

# Start bot
python main.py
```

---

## ⚙️ Configuration

### Environment Variables (`.env`)

```env
# Telegram
BOT_TOKEN=your-bot-token

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/smart_english_hr

# Admin
ADMIN_IDS=123456789,987654321

# Settings
DEFAULT_LANGUAGE=uz
DEBUG=False
```

---

## 📋 Application Flow

```
┌──────────────┐
│    START     │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  First Name  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Last Name   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Phone     │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Position   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Experience  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   SUBMIT     │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  HR Notified │
└──────────────┘
```

---

## 🗄️ Database

### Models

```python
# User model
class User:
    id: int
    telegram_id: int
    first_name: str
    last_name: str
    phone: str
    language: str
    created_at: datetime

# Application model
class Application:
    id: int
    user_id: int
    position: str
    experience: str
    status: str  # pending, reviewed, accepted, rejected
    created_at: datetime
```

### Migrations

```bash
# Create migration
alembic revision --autogenerate -m "Add new field"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

---

## 🚀 Deployment

### systemd Service

```ini
[Unit]
Description=Smart English HR Bot
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/path/to/smart_english_hr
ExecStart=/path/to/venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable smart_english_hr
sudo systemctl start smart_english_hr
```

---

## 🧪 Testing

```bash
# Run tests
pytest

# With coverage
pytest --cov=bot --cov=database --cov-report=html
```

---

## 🌿 Branches

| Branch | Purpose |
|--------|---------|
| `main` | Production |
| `first_half` | Feature development |
| `dev` | Development |

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

**Powering HR recruitment at Smart English 🎓**
