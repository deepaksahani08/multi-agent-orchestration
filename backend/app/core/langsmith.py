"""
LangSmith Configuration

Initializes LangSmith tracing for the application.
"""

import os
from langsmith import Client
from langsmith.utils import tracing_is_enabled


class LangSmithService:
    """
    Singleton wrapper around the LangSmith client.
    """

    def __init__(self):

        self.client = Client()

    @property
    def enabled(self) -> bool:

        """
        Returns whether tracing is enabled.
        """
        return tracing_is_enabled()


langsmith = LangSmithService()
