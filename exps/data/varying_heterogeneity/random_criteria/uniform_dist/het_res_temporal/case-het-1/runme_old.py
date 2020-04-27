from calculator import Workload
from calculator import Resource
from calculator import Engine
from pprint import pprint
import yaml
from time import sleep


def get_workload(mean, var, tasks):

    # Create a workload with a specific number of tasks with number of
    # operations per task drawn from a distribution
    wl = Workload(  num_tasks = tasks,          # no. of tasks
                    ops_dist = 'uniform',     # distribution to draw samples from
                    dist_mean = mean,         # mean of distribution
                    dist_var = var             # variance of distribution
                )
    return wl


def get_resource(mean, t_var, s_var, cores, gen):

    # Create a resource with a specific number of cores with performance of each
    # core drawn from a distribution
    res = Resource( num_cores = cores,        # no.
                    perf_dist = 'uniform',# distribution to draw samples from
                    dist_mean = mean,        # mean of distribution
                    temporal_var = t_var,     # temporal variance of core performance
                    spatial_var = s_var,     # spatial variance of core performance
                    num_gen = gen
                )
    return res


def get_engine(res):

    eng = Engine(cfg_path='./config.yml')
    eng.assign_cfg()
    eng.assign_resource(res)
    return eng


if __name__ == '__main__':

    trials = 1 
    num_cores = 1
    num_tasks = 512
    task_length = 64
    core_perf =8 
    
    # Create WLMS instance with a workload, resource, selection criteria, and
    # binding criteria
    for diff in [2]:

        for _ in range(trials):
            t = 0
            num_gen = (int)(num_tasks/num_cores);
            res = get_resource(mean = core_perf, t_var = diff, s_var = 0, cores = num_cores, gen = num_gen)
            eng = get_engine(res)

            for _ in range(num_gen):
 
                wl = get_workload(mean = task_length, var = 0, tasks = num_cores)
                eng.assign_workload(wl, submit_at=t)
                t +=1 
        
            sleep(5)

