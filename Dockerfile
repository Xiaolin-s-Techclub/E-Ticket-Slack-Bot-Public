FROM python:3.10.11
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update -y && \
    apt-get update -y && \
    apt-get clean

WORKDIR /slack-bot

COPY . /slack-bot

#RUN pip install pipenv --no-cache-dir && \
#    pipenv install --deploy --system && \
#    pip uninstall -y pipenv virtualenv-clone virtualenv

RUN pip install --no-cache-dir -r requirements.txt

# Remove unnecessary files
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN chmod +x ./run.sh

CMD ["./run.sh"]

#CMD ["python3", "shuukei.py"]
#CMD ["python3", "main.py"]




#
#RUN mkdir -p /var/www
#COPY ./requirements.txt /var/www
#RUN pip install -r /var/www/requirements.txt
#
#COPY ./flask_app.py /var/www
#COPY gunicorn.py /var/www
#
#WORKDIR /var/www

