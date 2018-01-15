ps = []
for i in xrange(1, 30):
    for j in xrange(i + 2, 40 - i):
        ps.append((i, j))
fps = []
for k in xrange(-75, -5 + 1):
    for i in xrange(2 - k % 2, min(29, -k - 4, (78 + k) // 3) + 1, 2):
            fps.append((i, (i - k) / 2))
print len(ps), len(fps)
print sorted(ps) == sorted(fps)
