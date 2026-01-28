from langchain_core.tools import tool
from typing import Literal

@tool
def run_diagnostic(target: Literal["logs", "disk", "services"], user_role: str = "user") -> str:
    """
    Runs a system diagnostic command.
    ONLY AVAILABLE FOR ADMINS.
    
    Args:
        target: The target to check (logs, disk, services).
        user_role: The role of the caller (must be 'admin').
    """
    if user_role != "admin":
        return "⛔ Permission Denied: You are not an admin."
        
    # Simulated execution
    if target == "logs":
        return "✅ Logs: No critical errors found in last 100 lines."
    elif target == "disk":
        return "✅ Disk Usage: 45% used (/nvme)."
    elif target == "services":
        return "✅ Services: All containers healthy (Orchestrator, Redis, Postgres)."
        
    return "Unknown diagnostic target."
