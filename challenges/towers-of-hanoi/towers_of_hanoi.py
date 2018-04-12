def towers_of_hanoi(num, A='A', B='B', C='C'):
    counter = 1
    while num > 0:
        # import pdb; pdb.set_trace()
        towers_of_hanoi(num, A, C, B)
        _move_disk(counter, A, C)
        counter += 1
        num -= 1
        towers_of_hanoi(num-1, B, C, A)
    return


def _move_disk(counter, source, destination):
    print('Disk {} moved from {} to {}'.format(counter, source, destination))


# if __name__ == "__main__":
#     main()
