FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /project
RUN mkdir -p /var/log/gunicorn
WORKDIR /project
RUN apt-get update
RUN apt-get install -y netcat
COPY requirements /project/requirements
RUN pip install -r requirements/production.txt
COPY . /project/

EXPOSE 3000
CMD ["/project/entrypoint.sh"]
