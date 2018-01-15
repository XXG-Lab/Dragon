def parse(code, head='L', data=None):
    if head == 'L':
        _, e = parse(code, 'E')
        return '', {
            'head': 'L.val=' + str(e['val']),
            'val': e['val'],
            'edges': [
                e,
                {
                    'head': '\mathbf{n}',
                    'edges': [],
                }
            ]
        }
    elif head == 'E':
        code, t = parse(code, 'T')
        code, e1 = parse(code, "E'", {'inh': t['val']})
        return code, {
            'head': "E.val=" + str(e1['syn']),
            'val': e1['syn'],
            'edges': [t, e1]
        }
    elif head == "E'":
        if len(code) > 0 and code[0] == '+':
            code = code[1:]
            code, t = parse(code, 'T')
            code, e1 = parse(code, "E'", {'inh': data['inh'] + t['val']})
            data['syn'] = e1['syn']
            data['head'] = "E'.inh=" + str(data['inh']) + '~' + "E'.syn=" + str(data['syn'])
            data['edges'] = [{'head': '+', 'edges': []}, t, e1]
        else:
            data['syn'] = data['inh']
            data['head'] = "E'.inh=" + str(data['inh']) + '~' + "E'.syn=" + str(data['syn'])
            data['edges'] = []
        return code, data
    elif head == 'T':
        code, f = parse(code, 'F')
        code, t1 = parse(code, "T'", {'inh': f['val']})
        return code, {
            'head': "T.val=" + str(t1['syn']),
            'val': t1['syn'],
            'edges': [f, t1]
        }
    elif head == "T'":
        if len(code) > 0 and code[0] == '*':
            code = code[1:]
            code, f = parse(code, 'F')
            code, t1 = parse(code, "T'", {'inh': data['inh'] * f['val']})
            data['syn'] = t1['syn']
            data['head'] = "T'.inh=" + str(data['inh']) + '~' + "T'.syn=" + str(data['syn'])
            data['edges'] = [{'head': '*', 'edges': []}, f, t1]
        else:
            data['syn'] = data['inh']
            data['head'] = "T'.inh=" + str(data['inh']) + '~' + "T'.syn=" + str(data['syn'])
            data['edges'] = []
        return code, data
    elif head == 'F':
        if len(code) > 0 and code[0] == '(':
            code = code[1:]
            code, e = parse(code, 'E')
            code = code[1:]
            return code, {
                'head': 'F.val=' + str(e['val']),
                'val': e['val'],
                'edges': [
                    {'head': '(', 'edges': []},
                    e,
                    {'head': ')', 'edges': []}
                ]
            }
        return code[1:], {
            'head': 'F.val=' + code[0],
            'val': int(code[0]),
            'edges': [{'head': '\\mathbf{digit}.lexval=' + code[0], 'edges': []}]
        }


def print_tree(node, space=0):
    head = ' ' * space + '[.$' + node['head'] + '$ '
    if len(node['edges']) != 0:
        print(head)
    for child in node['edges']:
        print_tree(child, space + 2)
    if len(node['edges']) == 0:
        head += ']'
        print(head)
    else:
        print(' ' * space + ']')

if __name__ == '__main__':
    # _, head = parse('(3+4)*(5+6)n')
    # _, head = parse('1*2*3*(4+5)n')
    _, head = parse('(9+8*(7+6)+5)*4n')
    print_tree(head)
