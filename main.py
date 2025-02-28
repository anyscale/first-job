import os
import ray
import time

print(f"The value of EXAMPLE_ENV_VAR is {os.environ['EXAMPLE_ENV_VAR']}.")


@ray.remote
def f(i):
    return i ** 2


# Execute 100 tasks across the cluster.
results = ray.get([f.remote(i) for i in range(100)])
print(results)