# dungeons_web
Web interface for backend logic

# architecture
```
flask_app/
├── app/
│   ├── __init__.py          # Flask app factory (builds the app)
│   ├── controllers/
│   │   ├── __init__.py      # Optional: consolidates imports for controllers
│   │   └── example_controller.py
│   ├── services/
│   │   ├── __init__.py      # Optional: consolidates imports for services
│   │   └── example_service.py
│   ├── utils/               # Optional: for helper functions
│   │   └── __init__.py
│   └── config.py            # App configurations
├── run.py                   # Entry point for the Flask app
├── requirements.txt         # Python dependencies
└── .env                     # Environment variables
```

# Flask App Factory Approach
> https://flask.palletsprojects.com/en/stable/tutorial/factory/