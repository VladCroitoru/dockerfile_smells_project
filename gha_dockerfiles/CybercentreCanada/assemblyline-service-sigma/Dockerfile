ARG branch=latest
FROM cccs/assemblyline-v4-service-base:$branch AS base

ENV SERVICE_PATH sigma_.sigma.Sigma

USER root

# Install APT dependancies
RUN apt-get update && apt-get install -y libssl1.1 && rm -rf /var/lib/apt/lists/*

FROM base AS build

# Install APT dependancies
RUN apt-get update && apt-get install -y libssl-dev && rm -rf /var/lib/apt/lists/*

# Install PIP dependancies
USER assemblyline
RUN touch /tmp/before-pip
RUN pip install git+https://github.com/CybercentreCanada/pysigma.git
RUN pip install assemblyline-client

USER root

# Remove files that existed before the pip install so that our copy command below doesn't take a snapshot of
# files that already exist in the base image
RUN find /var/lib/assemblyline/.local -type f ! -newer /tmp/before-pip -delete

# Switch back to root and change the ownership of the files to be copied due to bitbucket pipeline uid nonsense
RUN chown root:root -R /var/lib/assemblyline/.local

FROM base
COPY --chown=assemblyline:assemblyline --from=build /var/lib/assemblyline/.local /var/lib/assemblyline/.local

# Switch to assemblyline user
USER assemblyline

# Copy Sigma service code
WORKDIR /opt/al_service
COPY . .

# Patch version in manifest
ARG version=4.0.0.dev1
USER root
RUN sed -i -e "s/\$SERVICE_TAG/$version/g" service_manifest.yml
# Switch to assemblyline user
USER assemblyline
