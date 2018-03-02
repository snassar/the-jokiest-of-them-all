FROM debian:stable

RUN apt update

RUN apt install -y vim curl dialog net-tools build-essential python3 python3-dev python3-pip sqlite3

RUN pip3 install flask
RUN pip3 install flask-sqlalchemy
RUN pip3 install jinja2

RUN sqlite3 /var/www/cnkj.db

WORKDIR /var/www

COPY app.py /var/www

EXPOSE 5000

CMD python3 /var/www/app.py
