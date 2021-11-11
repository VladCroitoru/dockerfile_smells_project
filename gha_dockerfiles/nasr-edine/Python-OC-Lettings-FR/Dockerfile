FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# upgrade pip
RUN pip install --upgrade pip

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project 
COPY . /app/

# Collects static files from each applications
RUN django collectstatic

# CMD ["gunicorn", "config.wsgi", "-b", "0.0.0.0:8000"]
CMD gunicorn config.wsgi -b 0.0.0.0:$PORT
