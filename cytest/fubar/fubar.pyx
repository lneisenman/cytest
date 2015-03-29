cimport c_hello

def hello():
    return c_hello.hello()

def fubar():
    print('fubar')
    return 'fubar'
