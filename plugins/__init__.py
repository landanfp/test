import redis

query = redis.StricRedis(
 host = 'localhost',
 port = 6379,
 db=1,
 decode_responses=True,

)

admin = 763990585

