FROM python:3
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=fingerprint_api.settings.production
RUN mkdir /project
WORKDIR /project
COPY requirements /project/requirements
RUN pip install -r requirements/production.txt
COPY . /project/
RUN ./manage.py collectstatic --clear --no-input
RUN ./manage.py migrate

EXPOSE 3000
CMD ["./manage.py", "runserver", "localhost:3000"]
