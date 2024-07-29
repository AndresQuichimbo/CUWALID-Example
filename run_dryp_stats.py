from cuwalid.dryp.main_DRYP import run_DRYP
import cProfile
import pstats

if __name__ == '__main__':
    with cProfile.Profile() as pr:
        run_DRYP("input/dryp_input.json")

    # Write profiling stats to a text file
    with open('profiling_stats.txt', 'w') as f:
        stats = pstats.Stats(pr, stream=f)
        stats.sort_stats('time').print_stats()
