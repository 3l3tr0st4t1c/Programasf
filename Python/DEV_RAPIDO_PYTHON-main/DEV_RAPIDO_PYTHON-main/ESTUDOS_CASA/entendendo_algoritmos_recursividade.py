from time import sleep

def regressiva(i:int):
    print(i)
    sleep(1)
    if i <=1:
        return
    else:
        regressiva(i-1)
        
regressiva(5)