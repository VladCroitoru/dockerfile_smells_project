FROM python:3.9.6

# Switch to non-root user.
RUN useradd -ms /bin/bash pythonist
USER pythonist

# Switch Workdir.
WORKDIR /home/pythonist/pythonworkshop

# Copying installation specific files as they would be cached when no changes are done on them which would save time to build the image.
COPY pyproject.toml poetry.lock /home/pythonist/pythonworkshop/

# Upgrading PIP.
RUN python -m pip install -U pip

# Installing Poetry.
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

# Force poetry addition of path.
ENV PATH = "${PATH}:/home/pythonist/.local/bin"

# Configuring poetry to not create a virtualenv as Docker itself meant for Isolation.
RUN poetry config virtualenvs.create false

# Installing packages using Poetry.
RUN poetry install

# Copy the repo to the workdir.
COPY . /home/pythonist/pythonworkshop/

# Exposing port 8888.
EXPOSE 8888

# Configuring entrypoint for the docker container
ENTRYPOINT [ "poetry", "run", "jupyter-lab", "--ip", "0.0.0.0", "--port", "8888", "--no-browser"]