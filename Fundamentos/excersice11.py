def process_exception(parameters: list):
    if len(parameters < 3 ):
        raise IndexError()
    

try:
    print(10/0)
except Exception as e:
    print(e)
    
