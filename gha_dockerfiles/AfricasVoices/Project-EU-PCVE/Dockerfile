FROM python:3.7-slim

# Install Python tools (git + pipenv)
RUN apt-get update && apt-get install -y git
RUN pip install pipenv

# Install memory_profiler if this script is run with PROFILE_MEMORY flag
ARG INSTALL_MEMORY_PROFILER="false"
RUN if [ "$INSTALL_MEMORY_PROFILER" = "true" ]; then \
        apt-get update && apt-get install -y gcc && \
        pip install memory_profiler; \
    fi
    
# Make a directory for private credentials files
RUN mkdir /credentials

# Make a directory for intermediate data
RUN mkdir /data

# Set working directory
WORKDIR /app

# Install project dependencies.
ADD Pipfile /app
ADD Pipfile.lock /app
RUN pipenv sync

# Copy the rest of the project
ADD code_schemes/*.json /app/code_schemes/
ADD configuration/ /app/configuration/
ADD src /app/src
ADD log_pipeline_event.py /app
ADD fetch_raw_data.py /app
ADD generate_outputs.py /app
ADD upload_analysis_files.py /app
ADD upload_log_files.py /app
ADD automated_analysis.py /app
