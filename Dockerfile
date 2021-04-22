FROM python:3
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=fingerprint_api.settings.production
RUN mkdir /project
WORKDIR /project
COPY requirements /project/requirements
RUN pip install -r requirements/production.txt
COPY . /project/

EXPOSE 3000
CMD ["/project/entrypoint.sh"]
