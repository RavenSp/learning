from fastapi import FastAPI, Header
from core.settings import AUTH_KEY, SUPER_SECRET

app = FastAPI(title='Learn title')


@app.get('/test')
async def test_function(Auth: str = Header(...), Secret: str = Header(None)):
    if Auth != AUTH_KEY:
        return {
            'answer':'',
            'error': {
                'code': 1,
                'message': 'Auth failed!'
            }
        }

    if Secret != SUPER_SECRET:
        return {'test': 'maks'}
    else:
        return {'test': 'unknown!'}