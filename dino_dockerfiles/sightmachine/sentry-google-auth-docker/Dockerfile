FROM sentry:8.20


COPY sentry.conf.py /etc/sentry/

# Have to install specific hash see issue: https://github.com/getsentry/sentry-auth-google/issues/21
RUN pip install git+git://github.com/getsentry/sentry-auth-google.git@52020f577f587595fea55f5d05520f1473deaad1
