# dungeons_web
Web interface for backend logic

# architecture
```
flask_app/
├── app/
│   ├── __init__.py          # Flask app factory (builds the app)
│   ├── routes/
│   │   ├── __init__.py      # Optional: consolidates imports for controllers
│   │   └── example_controller.py
│   ├── services/
│   │   ├── __init__.py      # Optional: consolidates imports for services
│   │   └── example_service.py
│   ├── utils/               # Optional: for helper functions
│   │   └── __init__.py
│   ├── config/              # App configurations 
│   │   └── __init__.py
│   └── config.py            
├── run.py                   # Entry point for the Flask app
├── requirements.txt         # Python dependencies
└── .env                     # Environment variables
```

# Flask App Factory Approach
> https://flask.palletsprojects.com/en/stable/tutorial/factory/



# Deployment Considerations and WSGI 
Given this **LAN-hosted** deployment scenario, here are potential issues with a **WSGI-based framework (Flask + Gunicorn):**  

### **1. Concurrency Bottlenecks**
- **Problem:** WSGI is **blocking**, meaning each request must complete before another starts in the same worker. If multiple players query the API simultaneously (e.g., checking spells, monster stats, and initiative order updates), responses could slow down.  
- **Mitigation:** Gunicorn allows multiple workers (`gunicorn -w 4`), but on a local machine with limited resources, too many workers could cause CPU contention.  

### **2. Long-Running Requests**
- **Problem:** If a batch admin operation (e.g., bulk updating monsters) runs while players make requests, it could **block** other operations due to the synchronous nature of WSGI.  
- **Mitigation:** Use **a separate worker** for admin tasks or move heavy admin operations to a background task manager (like Celery or Flask’s `threading`).  

### **3. Latency & Performance on Low-Power Machines**
- **Problem:** If the DM’s computer is an older or low-power machine (e.g., a laptop running other D&D tools), WSGI’s **process-based** model could become a bottleneck compared to ASGI’s event loop model.  
- **Mitigation:** Test performance beforehand and fine-tune the number of Gunicorn workers (`gunicorn -w 2` might be enough for a local game).  

### **4. No WebSockets for Real-Time Updates**
- **Problem:** WSGI **doesn’t support WebSockets**, so if you ever want **live initiative tracking** or **real-time combat updates**, you’d need additional workarounds (e.g., polling).  
- **Mitigation:** If real-time sync becomes a priority, consider **FastAPI (ASGI) for WebSockets** or running a separate WebSocket service.  

### **5. Connection Issues (LAN-Specific)**
- **Problem:** If the DM’s device has network restrictions (firewall, bad Wi-Fi, or mobile hotspot quirks), players might struggle to connect to the server. WSGI itself won’t fix these problems.  
- **Mitigation:**  
  - Ensure the Flask server is running with `host='0.0.0.0'` (`flask run --host=0.0.0.0`) to expose it to LAN.  
  - DM should test connection stability before the session.  
  - If players experience slowdowns, check for **too many blocking requests at once.**  

---

### **Final Takeaway**
🚀 **WSGI (Flask + Gunicorn) is still viable** for a **LAN-hosted** D&D game, but:  
- Ensure **enough workers** to handle concurrent player requests.  
- Watch for **batch admin operations blocking players.**  
- Be mindful of **LAN connectivity issues.**  
- If you ever need **real-time updates**, consider adding **WebSockets via FastAPI** or running a separate real-time service.  

Would you want me to suggest an optimized Gunicorn configuration for your setup?

With this new context—admin operations happening **only before deployment**—most concerns about **blocking batch operations** during gameplay are no longer an issue. This makes **WSGI (Flask + Gunicorn)** an even better fit because:  

✅ **No need for async processing**—since all player interactions are simple **GET** requests.  
✅ **No concurrency issues from admin updates**—because they happen before the session starts.  
✅ **Easier debugging and deployment**—since WSGI is simpler than ASGI setups.  
✅ **Gunicorn workers can be optimized purely for player queries**, without worrying about admin load.  

### **What’s the Best Setup?**
- **Flask + Gunicorn (`-w 2` or `-w 4`)** should be more than enough.  
- **Run with `--preload`** for faster startup times (`gunicorn -w 2 --preload app:app`).  
- **Ensure Flask is exposed on LAN (`--host=0.0.0.0`)** so players can connect easily.  

At this point, **WSGI is the clear choice** unless you later need **real-time combat tracking** or **WebSockets**. Would you like any help setting up a basic deployment script?