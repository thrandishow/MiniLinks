# Project MiniLinks

## Using:

- `/shorten`

  - #### **Creates unique short id for the entered url**

- `/{short_id}`
  - #### **Redirects user on url, if find it by short_id(it was generated in /shorten)**

## Instruments:

- Sqlite3
- FastAPI
- Poetry

## How to run server:

```bash
uvicorn app.main:app --reload
```

## Docs endpoint

`/docs/`
