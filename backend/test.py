import os

print("API:", os.getenv("LANGSMITH_API_KEY"))
print("Tracing:", os.getenv("LANGSMITH_TRACING"))
print("Project:", os.getenv("LANGSMITH_PROJECT"))