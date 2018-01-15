#!/usr/bin/env python


def extend_empty_path(path, v):
    return path + ' \\overset{\epsilon}{\\rightarrow} ' + str(v)


def extend_path(path, e, v):
    return path + ' \\overset{' + e + '}{\\rightarrow} ' + str(v)


def dfs(state, string, path, last):
    if string == '':
        print(path + '$$')
        return
    if state == 0:
        if last != 3:
            dfs(3, string, extend_empty_path(path, 3), last)
        if string[0] == 'a':
            dfs(1, string[1:], extend_path(path, 'a', 1), 1)
    elif state == 1:
        if last != 0:
            dfs(0, string, extend_empty_path(path, 0), last)
        if string[0] == 'b':
            dfs(2, string[1:], extend_path(path, 'b', 2), 2)
    elif state == 2:
        if last != 1:
            dfs(1, string, extend_empty_path(path, 1), last)
        if string[0] == 'b':
            dfs(3, string[1:], extend_path(path, 'b', 3), 3)
    else:
        if last != 2:
            dfs(2, string, extend_empty_path(path, 2), last)
        if string[0] == 'a':
            dfs(0, string[1:], extend_path(path, 'a', 0), 0)

if __name__ == "__main__":
    dfs(0, 'aabb', '* $$0', 0)
