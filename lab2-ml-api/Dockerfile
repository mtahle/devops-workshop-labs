FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (layer cache — rebuilds only if requirements change)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Train the model at build time so it's ready when the container starts
COPY model.py .
RUN python model.py

# Copy the API server
COPY main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
