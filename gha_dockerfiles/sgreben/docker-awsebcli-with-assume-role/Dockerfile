FROM python:3-alpine
RUN apk add --no-cache build-base libffi-dev openssl-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /.aws/cli/cache && \
    chown -R nobody:nobody /.aws/cli/cache && \
    chmod -R a+rwx /.aws/cli/cache

COPY --chown=nobody:nobody with-assume-role /wrapper/with-assume-role
RUN chmod a+x /wrapper/with-assume-role
ENV PATH=/wrapper:${PATH}
CMD [ "with-assume-role", "eb" ]
