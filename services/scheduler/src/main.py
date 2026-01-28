import schedule
import time
import requests
import os
import logging
from datetime import datetime

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("scheduler")

ORCHESTRATOR_URL = os.getenv("ORCHESTRATOR_URL", "http://orchestrator-langgraph:8000")
HEARTBEAT_INTERVAL_MINUTES = int(os.getenv("HEARTBEAT_INTERVAL_MINUTES", "60"))

def pulse():
    """Sends a heartbeat system event to the Orchestrator."""
    logger.info("❤️ Pulse: Triggering System Event...")
    try:
        payload = {
            "event_type": "heartbeat",
            "timestamp": datetime.utcnow().isoformat(),
            "source": "scheduler_service"
        }
        response = requests.post(f"{ORCHESTRATOR_URL}/v1/system-event", json=payload, timeout=10)
        
        if response.status_code == 200:
            logger.info(f"✅ Pulse Accepted: {response.json()}")
        else:
            logger.warning(f"⚠️ Pulse Ignored: {response.status_code} - {response.text}")
            
    except Exception as e:
        logger.error(f"❌ Pulse Failed: {e}")

# Schedule
logger.info(f"⏳ Scheduler starting. Interval: {HEARTBEAT_INTERVAL_MINUTES} min.")
schedule.every(HEARTBEAT_INTERVAL_MINUTES).minutes.do(pulse)

# Main Loop
if __name__ == "__main__":
    # Pulse once on startup to verify connectivity
    time.sleep(10) # Wait for orchestrator to boot
    pulse()
    
    while True:
        schedule.run_pending()
        time.sleep(1)
