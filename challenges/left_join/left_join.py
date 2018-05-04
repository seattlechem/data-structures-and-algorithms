"""Left Join."""
from .hash_table import HashTable as HT


def left_join(hash1=None, hash2=None):
    """Join two hash tables in a left join way."""
    if hash1 and hash2 is None:
        raise ValueError('At least one input must be HashTable')
    if type(hash1) and type(hash2) is not HT:
        raise TypeError('Input must be HashTable.')

    ls = []
    ht = HT()

    for bucket in hash1.buckets:
        if bucket:
            ls.append(bucket.head.val)

    for each in ls:
        key = list(each.keys())[0]
        value = list(each.values())[0]

        if hash2.buckets[hash2.hash_key(key)]:
            each[key] = value, list(hash2.buckets[hash2.hash_key(key)].
                                    head.val.values())[0]
        else:
            each[key] = value, None
        ht.set(key, each[key])

    return ht
