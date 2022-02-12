from fastapi import FastAPI

api = FastAPI(title='Learn title')


@api.get('/test')
async def test_function():
    return {'test': 'maks'}