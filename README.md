# smart_english_hr

A modern Telegram bot built with **Boundless-Aiogram** framework.

## Features

- Modern async/await syntax with Aiogram 3.x
- SQLAlchemy async ORM for database operations
- FSM (Finite State Machine) support
- Middleware system for authentication and rate limiting
- Custom filters and keyboards
- Structured project layout for scalability
- Alembic database migrations
- Comprehensive logging system

## Project Structure

```
smart_english_hr/
├── bot/
│   ├── handlers/        # Message and callback handlers
│   ├── middlewares/     # Custom middlewares
│   ├── filters/         # Custom filters
│   ├── keyboards/       # Keyboard layouts
│   └── states/          # FSM states
├── database/
│   ├── models/          # Database models
│   └── database.py      # Database configuration
├── core/
│   ├── config.py        # Configuration management
│   └── logging.py       # Logging setup
├── utils/               # Helper functions
├── migrations/          # Alembic migrations
├── tests/               # Unit tests
└── main.py              # Bot entry point
```

## Setup

1. **Clone and navigate to the project:**
   ```bash
   cd smart_english_hr
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your bot token and other settings.

5. **Initialize database:**
   ```bash
   alembic upgrade head
   ```

6. **Run the bot:**
   ```bash
   python main.py
   ```

## Development

### Adding New Handlers

Create handler files in `bot/handlers/` and register them in `bot/handlers/__init__.py`.

### Database Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

### Adding Middleware

Create middleware in `bot/middlewares/` and register it in your dispatcher.

## Contributing

Built with [Boundless-Aiogram](https://github.com/yourusername/boundless-aiogram)

## License

MIT License
