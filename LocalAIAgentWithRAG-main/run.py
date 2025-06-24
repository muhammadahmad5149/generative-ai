
import uvicorn
from config import settings

if __name__ == "__main__":
    uvicorn.run(
        "main:app",                  # Tells uvicorn where the FastAPI app is
        host=settings.API_HOST,      # Reads host from .env (e.g., 0.0.0.0 or localhost)
        port=settings.API_PORT,      # Reads port from .env (e.g., 8001)
        reload=True,                 # Auto-reloads on file changes
    )
