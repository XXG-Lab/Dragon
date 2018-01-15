ps = []
for i in xrange(1, 30):
    for j in xrange(i + 2, 40 - i):
        ps.append((i, j))
fps = []
for k in xrange(2, 37 + 1):
    for j in xrange(k + 1, min([k + 29, (k + 39) // 2]) + 1):
        fps.append((j - k, j))
print len(ps), len(fps)
print sorted(ps) == sorted(fps)
