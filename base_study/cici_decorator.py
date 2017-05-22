import functools

def log(str=None):
    def decorater(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
                print('text = %s,begin call:%s' % (str,func.__name__))
                result = func(*args,**kwargs)
                print('text = %s,end call:%s' % (str,func.__name__))
                return result
        return wrapper
    return decorater

@log('hello')
def now():
    print('2017-5-11')

now()
