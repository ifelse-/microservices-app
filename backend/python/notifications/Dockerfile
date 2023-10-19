FROM python:3.11

WORKDIR /backend
COPY Pipfile .
RUN pip install pipenv
COPY . .

CMD ["pipenv", "run", "python", "app.py"]