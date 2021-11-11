# Mozilla Load-Tester
FROM stackbrew/debian:testing

RUN \
    apt-get update; \
    apt-get install -y python3-pip python3-venv git build-essential make; \
    apt-get install -y python3-dev libssl-dev libffi-dev; \
    git clone -b dev https://github.com/rpappalax/shavar-loadtests.git /home/loads; \
    cd /home/loads; \
    pip3 install virtualenv; \
    make build -e PYTHON=python3.5; \
    apt-get remove -y -qq git build-essential make python3-pip python3-venv libssl-dev libffi-dev; \
    apt-get autoremove -y -qq; \
    apt-get clean -y

WORKDIR /home/loads

# run the test
CMD venv/bin/ailoads -v -d $TEST_DURATION -u $CONNECTIONS
