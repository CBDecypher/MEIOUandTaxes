def parse_line(line):
	s = line.strip()
	ss = s.split('"')
	tokens = []
	for i,sss in enumerate(ss):
		if i%2==0:
			sss = sss.replace("="," = ").replace("{"," { ").replace("}"," } ")
			if "#" in sss:
				sss = sss.split("#")[0]
				tokens.extend(sss.split())
				return tokens
			tokens.extend(sss.split())
		else:
			tokens.append('"%s"' % sss)
	return tokens

def parse_file(fn):
	def update(dic, new):
		if isinstance(new, dict):
			new = new.items()
		for key, val in new:
			if key not in dic:
				dic[key] = val
			elif isinstance(dic[key], list):
				dic[key].append(val)
			else:
				dic[key] = [dic[key], val]
	d = {}
	names = []
	stack = [(d,"")]
	tokens = []
	key = ""
	with open(fn,"rb") as f:
		ff = f.read()
		fff = ff.decode("iso-8859-1")
		for line in fff.splitlines():
			tokens += parse_line(line)
		for token in tokens:
			if token == "=":
				key = names.pop()
			elif token == "{":
				dd = {}
				update(stack[-1][0], {key: dd})
				stack.append((dd,key))
				key = ""
			elif token == "}":
				if len(stack[-1][0]):
					update(stack.pop()[0], [(n,n) for n in names])
				else:
					k = stack.pop()[1]
					stack[-1][0][k] = []
					update(stack[-1][0], [(k,n) for n in names])
				names = []
			else:
				names.append(token)
				if key:
					update(stack[-1][0], {key: names.pop()})
					key = ""
	return d

def btree(idct, lst, form, body):
    if not len(lst):
        return ''
    elif len(lst) == 1:
        return body % lst[0]
    else:
        return form % (idct[lst[int(len(lst)/2)]],
                       btree(idct, lst[int(len(lst)/2):], form.replace('\n', '\n\t'), body),
                       btree(idct, lst[:int(len(lst)/2)], form.replace('\n', '\n\t'), body))

a = parse_file('common\\religions\\00_religion.txt')

lst = []

idct = {}
i = 1

for group in a:
        for religion in a[group]:
                if 'icon' in a[group][religion]:
                        idct[religion] = i
                        i += 1

                        if not 'date' in a[group][religion] or not '2000.1.1' == a[group][religion]['date']:
                                lst.append(religion)
print(len(lst))
cond = 'check_variable = { which = $var$ value = %s }'
body = 'POP_GetTlrncHelper = { religion = %s return = $return$ }'
form = 'if = {\n\tlimit = {\n\t\t%s\n\t}\n\t%s\n}\nelse = {\n\t%s\n}' % (cond, '%s', '%s')

with open('output.txt', 'w') as f:
    f.write(btree(idct, lst, form, body))