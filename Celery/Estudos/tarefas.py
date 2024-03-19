from celery import Celery
from random import randint

app = Celery(broker='redis://127.0.0.1:6379/0')

@app.task(bind=True, max_retries=20, default_retry_delay=3)
def exibir(self):
    x = randint(1, 10)
    if x > 9:
        return 'Ok'
    else:
        self.retry(countdown = 2**self.request.retries)
        return Exception('Erro')
