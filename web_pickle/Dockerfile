FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt && apk add --no-cache dumb-init
RUN mkdir /usr/src/app/auth; chmod 777 /usr/src/app/auth

COPY . .

EXPOSE 31337

ENV FLASK_APP "app.py"
ENV SECRET_KEY "***///kek"

ENTRYPOINT ["dumb-init", "--"]
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "31337"]
