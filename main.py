from fastapi import FastAPI, Header
from core.settings import AUTH_KEY

app = FastAPI(title='Learn title')


@app.get('/test')
async def test_function(Auth: str = Header(...)):
    if Auth != AUTH_KEY:
        return {
            'answer':'',
            'error': {
                'code': 1,
                'message': 'Auth failed!'
            }
        }
    return {'test': 'maks'}