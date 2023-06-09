FROM python:3.9

WORKDIR /{{ .Name }}

COPY ./requirements.txt /{{ .Name }}/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /{{ .Name }}/requirements.txt

COPY ./app /{{ .Name }}/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]