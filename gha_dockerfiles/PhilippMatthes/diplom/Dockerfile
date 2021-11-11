ARG USER_ID=1000
ARG USER_NAME=latex
ARG USER_HOME=/home/latex
ARG USER_GECOS=LaTeX
ARG BASE_IMAGE=kaestner/latex

FROM ${BASE_IMAGE} as latex

ARG USER_NAME
ARG USER_HOME
ARG USER_ID
ARG USER_GECOS

USER root

# delete default latex user
RUN deluser \
  --remove-home \
  "latex"

# create new user from build arguments
RUN adduser \
  --home "$USER_HOME" \
  --uid $USER_ID \
  --gecos "$USER_GECOS" \
  --disabled-password \
  "$USER_NAME"

# create user home directory and set permissions
RUN mkdir -p $USER_HOME \
  && chown "$USER_NAME:$USER_NAME" $USER_HOME

# switch into home directory as working directory
WORKDIR $USER_HOME

# switch to new user
USER $USER_NAME

FROM latex as build

ARG USER_NAME
ARG USER_HOME

COPY --chown=$USER_NAME:$USER_NAME . $USER_HOME


RUN latexmk task
RUN latexmk thesis
FROM scratch
ARG USER_HOME
# Copy the thesis pdf from the image.
COPY --from=build $USER_HOME/thesis.pdf /
COPY --from=build $USER_HOME/thesis.log /
