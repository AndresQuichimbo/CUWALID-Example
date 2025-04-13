import time
from cuwalid.stopet.main_stoPET import run_stoPET

if __name__ == '__main__':
    start = time.time()

    run_stoPET('input/stopet_input.json')
    
    end = time.time()
    print('Time of run: %s'%(end - start))