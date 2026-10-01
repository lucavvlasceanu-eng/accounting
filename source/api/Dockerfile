FROM python:3.11

WORKDIR /source/api

# Copy dependencies and install globally
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .
EXPOSE 8080


# Corrected CMD target: looks for app.py with instance app
CMD ["python", "main.py"]