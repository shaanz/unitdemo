FROM nginx/unit:1.13.0-python3.5
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install -r /app/requirements.txt

COPY config/unit.json /docker-entrypoint.d/

COPY Data/user.json  /app/Data/

WORKDIR /app
COPY user_service.py /app/