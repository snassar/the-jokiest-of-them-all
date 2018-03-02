FROM debian:stable

RUN apt update

RUN apt install -y vim curl dialog net-tools build-essential python3 python3-dev python3-pip sqlite3

RUN pip3 install flask
RUN pip3 install flask-sqlalchemy

#COPY schema.sql /var/www
#RUN sqlite3 /tmp/flaskr.db < /var/www/schema.sql

WORKDIR /var/www

COPY app.py /var/www

EXPOSE 5000

CMD python3 /var/www/app.py
