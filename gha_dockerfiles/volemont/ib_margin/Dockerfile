FROM python:3.7-slim AS base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# NOTE: Disabled, GitHub Actions must be run by the default Docker user (root).
#       Source: https://git.io/JfUrt
# Create and switch to a new user
#RUN useradd --create-home appuser
#USER appuser

# Install application into container
COPY . .

# Run the executable
ENTRYPOINT ["python", "-m", "ib_margin"]
