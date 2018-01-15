ps = []
for i in xrange(1, 30):
    for j in xrange(i + 2, 40 - i):
        ps.append((i, j))
fps = []
for k in xrange(4, 39 + 1):
    for j in xrange(max(k - 29, (k + 3) // 2), (k - 1) + 1):
        fps.append((k - j, j))
print len(ps), len(fps)
print sorted(ps) == sorted(fps)
