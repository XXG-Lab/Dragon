codes_1 = [
    'LD R1, a',
    'LD R2, b',
    'SUB R3, R1, R2',
    'ADD R2, R1, R2',
    'ST a, R3',
    'ST b, R2'
]
codes_2 = [
    'LD R1, a',
    'LD R2, b',
    'SUB R1, R1, R2',
    'ADD R2, R1, R2',
    'ST a, R1',
    'ST b, R2'
]
codes_3 = [
    'LD R1, a',
    'LD R2, b',
    'SUB R3, R1, R2',
    'ADD R4, R1, R2',
    'ST a, R3',
    'ST b, R4'
]

def parse_codes(codes):
    def parse_code(code):
        return {
            'raw': code,
            'code': code.replace(',', '').split(' '),
            'edges': {},
            'back': [],
            'in_num': 0
        }
    return map(parse_code, codes)


def init_edges(codes):
    for i, u in enumerate(codes):
        for j, v in enumerate(codes):
            if i >= j:
                continue
            if u['code'][0] == 'LD':
                if v['code'][0] == 'ST':
                    if u['code'][2] == v['code'][1]:
                        u['edges'][j] = 1
                        v['in_num'] += 1
                else:
                    if u['code'][1] in v['code']:
                        u['edges'][j] = 2
                        v['in_num'] += 1
            elif len(u['code']) == 4:
                if u['code'][1] in v['code'] or v['code'][1] in u['code']:
                    u['edges'][j] = 1
                    v['in_num'] += 1
    return codes


def init_back(codes):
    for i, u in enumerate(codes):
        for j in u['edges'].keys():
            codes[j]['back'].append(i)
    return codes


def get_top_order(codes):
    order = []
    in_nums = map(lambda x: x['in_num'], codes)
    while len(order) < len(in_nums):
        for j in xrange(len(in_nums)):
            if in_nums[j] == 0:
                in_nums[j] -= 1
                order.append(j)
                for v in codes[j]['edges'].keys():
                    in_nums[v] -= 1
    return order


def generate(codes, alu_num, mem_num):
    codes = init_back(init_edges(parse_codes(codes)))
    order = get_top_order(codes)
    s = [-1] * len(codes)
    rt = {}
    for i in order:
        u = codes[i]
        cs = 0
        for j in u['back']:
            p = codes[j]
            if s[j] + p['edges'][i] > cs:
                cs = s[j] + p['edges'][i]
        while True:
            if cs not in rt:
                rt[cs] = ([], [])
            if u['code'][0] in ['LD', 'ST']:
                if len(rt[cs][1]) < mem_num:
                    rt[cs][1].append(u['raw'])
                    break
            else:
                if len(rt[cs][0]) < alu_num:
                    rt[cs][0].append(u['raw'])
                    break
            cs += 1
        s[i] = cs
    for u in codes:
        for j, c in u['edges'].items():
            print(u['raw'] + ' -> ' + codes[j]['raw'] + ': ' + str(c))
        print('')
    table = '|'
    for _ in xrange(alu_num):
        table += ' ALU |'
    for _ in xrange(mem_num):
        table += ' MEM |'
    table += '\n'
    table += '|'
    for _ in xrange(alu_num + mem_num):
        table += ':-|'
    table += '\n'
    for key in sorted(rt.keys()):
        table += '|'
        for i in xrange(alu_num):
            if i < len(rt[key][0]):
                table += ' `' + rt[key][0][i] + '` |'
            else:
                table += ' |'
        for i in xrange(mem_num):
            if i < len(rt[key][1]):
                table += ' `' + rt[key][1][i] + '` |'
            else:
                table += ' |'
        table += '\n'
    table += '\n'
    print(table)

if __name__ == '__main__':
    generate(codes_1, 2, 2)
