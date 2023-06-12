FROM python:3.9

WORKDIR /cookiecutter_python_http_fast

COPY ./requirements.txt /cookiecutter_python_http_fast/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /cookiecutter_python_http_fast/requirements.txt

COPY ./app /cookiecutter_python_http_fast/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]