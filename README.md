# snippets
## redis-cleanup.py
I ran into a situation where I wanted to cleanup a large number of keys from a redis cluster based on some pattern so I didn't know what the keys were going to be in advance. I wanted to do it in parallel as the cluster had north of 6 million keys and around 4 million keys had to be deleted based on idle time i.e. wanted to delete keys that weren't accessed in the last 30 days. So came up with this script. You will need to install the following packages via pip:

- RedisCluster
- joblib