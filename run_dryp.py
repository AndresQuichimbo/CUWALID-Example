import time
from cuwalid.dryp.main_DRYP import run_DRYP



if __name__ == '__main__':
    start = time.time()

    run_DRYP("input/dryp_input.json")
    
    end = time.time()
    print('Time of run: %s'%(end - start))