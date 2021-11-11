FROM bjwebb/bookish
ENV DATABASE_URL sqlite:///demo.db
ENV SECRET_KEY c9a7789b3e18f89c93efcbbb3072671bfa7b1d02474b5d02c747ffc9a8146768
ENV DEBUG True
RUN python manage.py migrate
RUN python manage.py createdemodata

