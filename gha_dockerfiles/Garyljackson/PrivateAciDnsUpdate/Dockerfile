FROM mcr.microsoft.com/azure-cli AS base

WORKDIR /app

COPY az_cli.sh .

# Creates a non-root user with an explicit UID
RUN adduser -u 5678 --disabled-password --gecos "" appuser

# Assign the new user as the owner of the app folder
RUN chown -R appuser /app 

# Give the new user execute permissions on the file
RUN chmod u+x az_cli.sh

USER appuser

CMD [ "./az_cli.sh" ]

