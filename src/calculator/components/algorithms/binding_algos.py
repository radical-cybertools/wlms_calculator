def round_robin(workload, resource):

    m = list()
    for idx, task in enumerate(workload):
        m.append({task: resource[idx%len(resource)]})

    return m

def optimize_tte(workload, resource):

    m = list()

    workload = sorted(workload, key=lambda task:task.ops, reverse=True)
    resource = sorted(resource, key=lambda unit: unit.perf, reverse=True)

    for idx, task in enumerate(workload):
        m.append({task: resource[idx % len(resource)]})

    return m


def optimize_util(workload, resource):

    m = list()
    resource = sorted(resource, key=lambda unit: unit.perf, reverse=True)

    for idx, task in enumerate(workload):
        m.append({task: resource[0]})

    return m


