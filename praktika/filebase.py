Set-ExecutionPolicy unrestricted



try:
    config = {
    'host' : 'localhost',
    'user' : 'editor2008',
    'password': 'w8D5xV1yHth',
    'database': 'editor2008_shop'
    }
    print('successfully connected...')
except Exception as ex:
    print('connection refused')
    print(ex)