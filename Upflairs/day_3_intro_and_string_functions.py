Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='hello i am here for python'
type(s)
<class 'str'>
S[1:6:1]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    S[1:6:1]
NameError: name 'S' is not defined. Did you mean: 's'?
S{1:6:}
SyntaxError: invalid syntax
s{1:6:}
SyntaxError: invalid syntax
s(1:6:)
SyntaxError: invalid syntax
len(s)
26
s[0]
'h'
s[-1]
'n'
s[:5]
'hello'
s+=language
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s+=language
NameError: name 'language' is not defined
s+='language'
s
'hello i am here for pythonlanguage'
s-='language'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s-='language'
TypeError: unsupported operand type(s) for -=: 'str' and 'str'
s='hello i am here for python'
s+=' language'
s
'hello i am here for python language'
s[6:8:1]
'i '
s[6:7]
'i'
s[26:1]
''
s[26:-26]
''
s[26:-26:-1]
' nohtyp rof ereh '
s=s[:11] + 'now '+s[11:]
s
'hello i am now here for python language'
s[2]='m'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s[2]='m'
TypeError: 'str' object does not support item assignment
a=20
del s[0]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    del s[0]
TypeError: 'str' object doesn't support item deletion
s.lower()
'hello i am now here for python language'
s=s.lower()
s
'hello i am now here for python language'
s.upper()
'HELLO I AM NOW HERE FOR PYTHON LANGUAGE'
s.count()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s.count()
TypeError: count() takes at least 1 argument (0 given)
s.count(len)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.count(len)
TypeError: must be str, not builtin_function_or_method
s.index()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.index()
TypeError: index() takes at least 1 argument (0 given)
s.count('n')
3
s
'hello i am now here for python language'
s.index('n')
11
s.count('n',0,10)
0
s.count('n',0,15)
1
help
Type help() for interactive help, or help(object) for help about object.





help(s.count)
Help on built-in function count:

count(...) method of builtins.str instance
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

s.index('p')
24
s.index('language')
31
s.index('opla')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s.index('opla')
ValueError: substring not found
s.find('python')
24
s.find('java')
-1
s.islower()
True
s.isupper
<built-in method isupper of str object at 0x0000022AF3FE08D0>
s.isupper()
False
s.isalpha()
False
'123'.isnumeric()
True
s.replace('python','java')
'hello i am now here for java language'
s.startswith('he')
True
s.endswith('f')
False
s.split()
['hello', 'i', 'am', 'now', 'here', 'for', 'python', 'language']
s.split('now)
        
SyntaxError: incomplete input
s.split('now')
        
['hello i am ', ' here for python language']
e='graviityclub@gmail,com'
        
e.split('@')[-1]
        
'gmail,com'
f=ee.split('@')
        
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    f=ee.split('@')
NameError: name 'ee' is not defined. Did you mean: 'e'?
f=e.split('@')[-1]
        
f
        
'gmail,com'
f=e.split('@')
        
type(f)
        
<class 'list'>
s[0]
        
'h'
e.split('graviity')
        
['', 'club@gmail,com']
e.split('graviity')[-1]
        
'club@gmail,com'
f=[1,3,6,7]
        
f[-1]
        
7
f['hemant','amit','divyanshu','deepanshu']
        
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    f['hemant','amit','divyanshu','deepanshu']
TypeError: list indices must be integers or slices, not tuple
f=['hemant','amit','divyanshu','deepanshu']
        
f[-1]
        
'deepanshu'
s.strip()
        
'hello i am now here for python language'
s.strip('e')
        
'hello i am now here for python languag'
s.strip('h')
        
'ello i am now here for python language'
p=input()
        
3
p
        
'3'
p=input('enter your first name:')
        
enter your first name: Hemant
p
        
' Hemant'
p.strip()
        
'Hemant'
p='        mera'
        
p.strip()
        
'mera'
len(p)
        
12
len(p.strip())
        
4
help(join)
        
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    help(join)
NameError: name 'join' is not defined
help(p.join)
        
Help on built-in function join:

join(iterable, /) method of builtins.str instance
    Concatenate any number of strings.
    
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    
    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

'star'.join('WORLD')
        
'WstarOstarRstarLstarD'
'-'.join('world')
        
'w-o-r-l-d'
'_'.join(e.split('@'))
        
'graviityclub_gmail,com'
p.replace('java','python')
        
'        mera'
    a=20
        
SyntaxError: unexpected indent
a=20
        
b='nice'
        
# 'we got 20 packets and they were nice'
        
# 'we got 20 packets and out of them 20 were nice'
        
c='we got %d packets and out of them %d were %s'%(a,a,b)
        
c
        
'we got 20 packets and out of them 20 were nice'
c='we got {} packets and out of them {} were {}'.format(a,a,b)
        
c
        
'we got 20 packets and out of them 20 were nice'
>>> #format function'
...         
>>> c='we got {0} packets and out of them {0} were {1}'.format(a,a,b)
...         
>>> c
...         
'we got 20 packets and out of them 20 were 20'
>>> c='we got {0} packets and out of them {0} were {1}'.format(a,b)
...         
>>> c
...         
'we got 20 packets and out of them 20 were nice'
>>> ##fsting ()
...         
>>> f'we got {a} packets and out of them {a} were {b}'
...         
'we got 20 packets and out of them 20 were nice'
