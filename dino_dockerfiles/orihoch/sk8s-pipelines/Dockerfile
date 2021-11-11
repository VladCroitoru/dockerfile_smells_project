FROM frictionlessdata/datapackage-pipelines

RUN pip install --no-cache-dir pipenv pew
RUN apk --update --no-cache add build-base python3-dev bash jq libxml2 libxml2-dev git libxslt libxslt-dev

COPY Pipfile /pipelines/
COPY Pipfile.lock /pipelines/
RUN pipenv install --system --deploy --ignore-pipfile && pipenv check

#COPY setup.py /pipelines/
#RUN pip install -e .

# temporary fix for dpp not returning correct exit code
# TODO: remove when datapackage-pipelines 1.5.4 is released which should fix this
# https://github.com/frictionlessdata/datapackage-pipelines/releases
RUN pip install --upgrade https://github.com/OriHoch/datapackage-pipelines/archive/fix-exit-code.zip

RUN apk --update --no-cache add curl

COPY pipeline-spec.yaml /pipelines
COPY noise.py /pipelines
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
