from collections import defaultdict

def gen_stats(root):
    people = defaultdict(dict)
    with open(root + '/issues-opened', 'rb') as f:
        for line in f:
            l, v = line.strip().split(' ')
            people[l]['o'] = int(v)
    with open(root + '/issues-closed', 'rb') as f:
        for line in f:
            l, v = line.strip().split(' ')
            people[l]['c'] = int(v)

    for p in people.keys():
        opened = people[p]['o'] if 'o' in people[p] else 0
        closed = people[p]['c'] if 'c' in people[p] else 0
        print "\t".join([str(p), str(opened), str(closed), str(opened/float(closed) if closed > 0 else 'inf'), str(opened - closed)])

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print "Usage: python stats.py /file-root-dir"
        sys.exit(-1)
    gen_stats(sys.argv[1])
