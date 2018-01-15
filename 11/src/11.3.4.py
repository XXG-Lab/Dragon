ps = []
for i in xrange(1, 30):
    for j in xrange(i + 2, 40 - i):
        ps.append((i, j))
fps = []
for j in xrange(3, 38 + 1):
    for i in xrange(1, min([29, j - 2, 39 - j]) + 1):
        fps.append((i, j))
print len(ps), len(fps)
print sorted(ps) == sorted(fps)

ps = []
for i in xrange(10, 1000 + 1):
    for j in xrange(i, i + 10):
        ps.append((i, j))
fps = []
for j in xrange(10, 1009 + 1):
    for i in xrange(max([10, j - 9]), min([1000, j]) + 1):
        fps.append((i, j))
print len(ps), len(fps)
print sorted(ps) == sorted(fps)

ps = []
for i in xrange(0, 100):
    for j in xrange(0, 100 + i):
        for k in xrange(i + j, 100 - i - j):
            ps.append((i, j, k))
fps = []
for k in xrange(0, 99 + 1):
    for j in xrange(0, min([k, 198, 99 - k, (99 + k) // 2, (198 - k) // 2]) + 1):
        for i in xrange(max([0, j - 99]), min([99, k - j, 99 - j - k]) + 1):
            fps.append((i, j, k))
print len(ps), len(fps)
print sorted(ps) == sorted(fps)
