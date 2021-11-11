FROM clouder/base:3.4
MAINTAINER Dave Lasley <dave@laslabs.com>

ARG PYTHON_VERSION="3"
ARG INCLUDE_DEV="0"

# Set version arg as an env so container is version-aware
ENV PYTHON_VERSION="${PYTHON_VERSION}"
ENV PYTHON_PACKAGE="python${PYTHON_VERSION}"

# Install Python
RUN apk add --no-cache "${PYTHON_PACKAGE}"

# Install dev dependencies
RUN if [[ "${INCLUDE_DEV}" == "1" ]]; \
    then \
        apk add --no-cache build-base "${PYTHON_PACKAGE}-dev"; \
    fi

# Symlink Python3 executable as standard python
RUN if [[ "${PYTHON_VERSION}" == "3" ]]; \
    then \
        ln -s /usr/bin/python3 /usr/bin/python; \
    fi

# Install pip
RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | python

# Expose python
CMD ["python"]
