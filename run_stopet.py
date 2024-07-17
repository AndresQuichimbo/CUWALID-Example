import time
from cuwalid.stopet.run_stoPET import run_stoPET

if __name__ == '__main__':
    start = time.time()

    run_stoPET()
    
    end = time.time()
    print('Time of run: %s'%(end - start))