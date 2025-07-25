# chat-application-with-flask-react-and-socketio-back-end-


## ⚙️ Tech Stack & Libraries

- **Frontend**: React Native, Expo, AsyncStorage
- **Backend**: Flask, Flask-SocketIO, Python 3
- **WebSockets**: Socket.IO (server + client)
- **State Management**: useState, useEffect, useContext
- **Deployment**: Tested on Android emulator + physical device (via local IP)
- **Video Editing**: CapCut (for deliverable demo)

## 📝 Prompt Strategy (if using LLM/AI)

_N/A for now (planned future integration with GPT API for intelligent auto-replies or summarization)._

## ⚡ Rate-Limit Handling

- Messages are stored and filtered per group in local storage (`AsyncStorage`).
- Group-based filtering prevents message flooding across rooms.
- Socket connections are initiated per user session and scoped by room name.

## 📦 Build & Run Instructions

### Frontend
1. Clone the repo.
2. Run: `cd frontend && npm install`
3. Start Expo: `npx expo start`
4. Connect emulator or physical device (use LAN or IP for socket connection).

### Backend
1. Set up virtual env: `python -m venv venv && source venv/bin/activate`
2. Install deps: `pip install flask flask-socketio`
3. Run: `python app.py`
4. Make sure the IP and port match on both server and client (e.g. `http://192.168.X.X:5000`).

## 🧪 Known Limitations

- Messages are not persisted server-side (local-only via AsyncStorage).
- Single-server architecture (no distributed scaling).
- No login/authentication yet.
- LLM integration pending.

## 🚀 Future Work

- Add user authentication (OAuth or Firebase).
- Store messages persistently in a database.
- Add file/image sending support.
- Integrate GPT-4 API for smart replies and summaries.

---

