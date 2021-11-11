FROM python:3
MAINTAINER Rich Wareham <rich.psephology@richwareham.com>

# Much of this is copied from the documentation for the Python Dockerfile. By
# copying the requirements first and then copying the remainder of the app, we
# can make use of Docker's caching feature to make subsequent re-builds a little
# faster if the requirements are unchanged.
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Run the test suite when building the container. The test suite should still
# pass even when being run in a container
RUN python setup.py test install

# Configure the various environment variables for the application
ENV FLASK_APP psephology.autoapp
ENV PSEPHOLOGY_CONFIG /usr/src/app/config_docker.py

# The "flask run" command starts a server on port 5000
EXPOSE 5000

# The default entrypoint is "flask run"
ENTRYPOINT ["flask"]
CMD ["run", "--host", "0.0.0.0", "--port", "5000"]
