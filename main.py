from fastapi import FastAPI

app = FastAPI(title='Learn title')


@app.get('/test')
async def test_function():
    return {'test': 'maks'}