# Using official python runtime base image
FROM python:3.5.2

# Set the application directory
WORKDIR /app

# Install our requirements.txt
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy our code from the current folder to /app inside the container
ADD . /app
ADD wappalyzer_scraper_rabbitmq.py /app/wappalyzer_scraper_rabbitmq.py
ADD wappalyzer.py /app/wappalyzer.py
ADD ./data /app/data
# Define our command to be run when launching the container
#CMD ["python", "wappalyzer_scraper_rabbitmq.py -t 10"]
