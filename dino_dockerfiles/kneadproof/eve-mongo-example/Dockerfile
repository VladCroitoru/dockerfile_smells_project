FROM python:2.7

# Create the app directory
RUN mkdir /eve

# Add the requirements and python files
ADD ./requirements.txt /eve/requirements.txt
ADD ./settings.py      /eve/settings.py
ADD ./run.py           /eve/run.py

# Change to the app directory
WORKDIR /eve

# Install requirements
RUN pip install -r requirements.txt

# Expose default ports
EXPOSE 5000

# Start application
CMD python run.py
