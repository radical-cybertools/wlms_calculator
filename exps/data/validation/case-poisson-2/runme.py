from calculator import Workload
from calculator import Resource
from calculator import Engine
from pprint import pprint
import yaml
from time import sleep


def get_workload(mean, var, tasks=128):

    # Create a workload with a specific number of tasks with number of
    # operations per task drawn from a distribution
    wl = Workload(  num_tasks=tasks,          # no. of tasks
                    ops_dist='poisson',     # distribution to draw samples from
                    dist_mean=mean,         # mean of distribution
                    dist_var=var             # variance of distribution
                )

    return wl


def get_resource(mean, t_var, s_var, cores=128):

    # Create a resource with a specific number of cores with performance of each
    # core drawn from a distribution
    res = Resource( num_cores=cores,        # no.
                    perf_dist='poisson',    # distribution to draw samples from
                    dist_mean=mean,        # mean of distribution
                    temporal_var=t_var,     # temporal variance of core performance
                    spatial_var=s_var     # spatial variance of core performance
                )

    return res


def get_engine(res):

    eng = Engine(cfg_path='./config.yml')
    eng.assign_cfg()
    eng.assign_resource(res)
    return eng
    

if __name__ == '__main__':

    with open('./config.yml','r') as fp:
        cfg = yaml.load(fp)

    early = cfg['wlms']['early_binding']
    trials=30
  

    # Create WLMS instance with a workload, resource, selection criteria, and
    # binding criteria
    for _ in range(trials):

        t = 0
        res = get_resource(mean=32, t_var=0, s_var=0, cores=128)
        eng = get_engine(res)

        if early:
            wl = get_workload(mean=1024, var=0, tasks=8*128)
            eng.assign_workload(wl, submit_at=t)
            sleep(5)

        else:
            for _ in range(8):

                wl = get_workload(mean=1024, var=0, tasks=128)
                eng.assign_workload(wl, submit_at=t)
                t += 5
            
            sleep(5)
