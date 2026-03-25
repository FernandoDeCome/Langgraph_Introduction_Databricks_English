"""
Shared module for LLM initialization.

Centralizes model configuration so that all scenarios
use the same instance configured via environment variables.
"""

import os
from dotenv import load_dotenv
from langchain_databricks import ChatDatabricks

load_dotenv()

def get_llm(temperature=0):
    """Returns a ChatDatabricks instance configured via .env.

    Environment variables used:
        DATABRICKS_HOST: workspace URL (required)
        DATABRICKS_TOKEN: personal access token (required)
        DATABRICKS_LLM_ENDPOINT: model serving endpoint (default: databricks-claude-sonnet-4-6)
    """
    return ChatDatabricks(
        endpoint=os.getenv("DATABRICKS_LLM_ENDPOINT", "databricks-claude-sonnet-4-6"),
        temperature=temperature,
    )
