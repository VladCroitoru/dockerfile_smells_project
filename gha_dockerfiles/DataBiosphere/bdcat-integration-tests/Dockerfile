# A custom docker image for running integration tests as a docker image.
#
# To build this image, run:
#
#   docker login
#   docker build . -t quay.io/{docker_username}/{tag_key}:{tag_value}
#   docker push quay.io/{docker_username}/{tag_key}:{tag_value}
#
# Notes:
#  - docker.io has limits/throttling; gcr.io costs money; quay.io has neither
FROM python:3.8
COPY . /bdcat-integration-tests
RUN pip install virtualenv
CMD ["virtualenv", "-p", "python3.8", "venv"]
CMD [".", "venv/bin/activate"]
RUN pip install -r bdcat-integration-tests/requirements.txt
CMD ["python", "/bdcat-integration-tests/scripts/run_integration_tests.py"]
