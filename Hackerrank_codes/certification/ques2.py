import os


def avg(*args):
    assert len(args)>=1 and len(args)<=100
    assert any(-100 <= v <= 100 for v in args)
    val = 0
    for v in args:
        val += v
    val = val/len(args)
    return round(val, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = list(map(int, input().split()))
    res = avg(*nums)

    fptr.write('%.2f' % res + '\n')

    fptr.close()