"""Left Join."""
from .hash_table import HashTable as HT


def left_join(hash1, hash2):
    """Join two hash tables in a left join way."""
    ls = []
    ht = HT()

    for bucket in hash1.buckets:
        if bucket:
            ls.append(bucket.head.val)

    for each in ls:
        key = list(each.keys())[0]
        value = list(each.values())[0]

        if hash2.buckets[hash2.hash_key(key)]:
            each[key] = value, list(hash2.buckets[hash2.hash_key(key)].head.val.values())[0]
        else:
            each[key] = value, None
        ht.set(key, each[key])

    return ht
