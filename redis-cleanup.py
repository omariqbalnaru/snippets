from rediscluster import RedisCluster

# using joblib package for parallel processing
from joblib import Parallel, delayed
import multiprocessing

# creating connection
r = RedisCluster(host='localhost', port=6379, skip_full_coverage_check=True)

# this method will be executed in parallel
def processInput(index, key, r):
    idle = r.object("idletime", key)
    # idle time is in seconds. This is 30days
    if idle > 2592000:
        print('processing: ', index)
        print('deleting: ', key)
        r.delete(key)

# setting number of threads according to cpu_count. you might need to experiment with it
num_cores = multiprocessing.cpu_count() * 16
print('num_cores: ', num_cores);

# this is where the magic happens :)
results = Parallel(n_jobs=num_cores, backend="threading")(delayed(processInput)(index, item, r) for index, item in enumerate(r.scan_iter(match="tokens*", count=1000)))