# Webtutor
cChat AI based on GPT with advanced semantic search and semantic context augmentation for interactive tutorials of web applications.

It has a python backend that can 

## Dependencies

Install a couple of dependencis:
```
pip install fastapi sqlalchemy databases psycopg2-binary asyncpg uvicorn
```

```
pip install -r requirements.txt
```

## Running server locally

Navigate into server folder in terminal and execute the following command:
```
uvicorn app:app --reload
```

The service is then available locally under: `http://127.0.0.1:8000`

