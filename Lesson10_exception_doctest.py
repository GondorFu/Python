
# 对函数fact(n)编写doctest并执行
def fact(n):
    '''
	>>> fact(1)
	1
	>>> fact(3)
	6
	>>> fact(0)
	Traceback (most recent call last):
		...
	ValueError: n must be greater than one!
    '''
    if n < 1:
        raise ValueError('n must be greater than one!')
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
