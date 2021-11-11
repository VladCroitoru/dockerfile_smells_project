ARG         EXTRA_BUILD_DEPS='g++'
ARG         REQUIREMENTS_FILE=/requirements/base.txt

FROM        public.ecr.aws/g3c5k4i8/starlette-docker:3.8-alpine

ENV         APP_MODULE=app.main:app \
            ALLOWED_HOSTS="*" \
            DATABASE_URL=postgresql+asyncpg://postgres:password@db:5432/appdb \
            SECRET_KEY="***** change me *****" \
            EMAIL_HOST=mail \
            EMAIL_PORT=1025 \
            EMAIL_DEFAULT_FROM_ADDRESS=mail@example.com \
            EMAIL_DEFAULT_FROM_NAME=Mail
