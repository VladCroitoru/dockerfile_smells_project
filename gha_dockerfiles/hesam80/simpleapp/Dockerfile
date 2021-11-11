# Python image to use.
FROM python:3.9
# copy the requirements file used for dependencies
COPY ./requirements.txt  /app/requirements.txt

# Set the working directory to /app
WORKDIR /app



# Install any needed packages specified in requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install gunicorn
# Copy the rest of the working directory contents into the container at /app
COPY .  /app

CMD ["sh" , "docker-entry.sh"]

# Run app.py when the container launches

