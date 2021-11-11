FROM virtool/workflow:nightly as base
WORKDIR /app
COPY workflow.py .
COPY pathoscope.py .

FROM base as test
RUN ["pip", "install", "poetry==1.1.10"]
COPY poetry.lock .
COPY pyproject.toml .
RUN ["poetry", "install"]
COPY tests tests
RUN ["ls", "tests"]
RUN ["poetry", "run", "pytest", "-x"]
