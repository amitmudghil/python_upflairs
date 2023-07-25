Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=10.0
c=10+0j
d='hi'
e=[3,8,5]
f=(3,8,5)
g={3,8,5}
h={1:2,3:4}
\
i=true
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    i=true
NameError: name 'true' is not defined. Did you mean: 'True'?
i='true'
e[1]
8
type(a)
<class 'int'>
type(b)
<class 'float'>
type(c)
<class 'complex'>
type(d)
<class 'str'>
type(e)
<class 'list'>
type(f)
<class 'tuple'>
type(g)
<class 'set'>
type(h)
<class 'dict'>
type(i)
<class 'str'>
i=True
type(i)
<class 'bool'>
i
True
j=False
s='this was a new way of programming'
print(s)
this was a new way of programming
s
'this was a new way of programming'
type(s)
<class 'str'>
len(s)
33
s1="this was a new way of programming"
s1
'this was a new way of programming'
s[3]
's'
s[0]
't'
s[3:8]
's was'
s[32]
'g'
s[-1]
'g'
s[-33]
't'
s[0:3]
'thi'
s[0:4]
'this'
s[0:4:1]
'this'
s[0:4:2]
'ti'
ss[5:9;1]
SyntaxError: invalid syntax
s[5:9:1]
'was '
s[-1:-12]
''
s[-1:(-12)]
''
s[(-1):(-11):-1]
'gnimmargor'
s[-11:33:]
'programming'
s[-11:]
'programming'
s[::-1]
'gnimmargorp fo yaw wen a saw siht'
s[..]
SyntaxError: invalid syntax
s[::]
'this was a new way of programming'
s
'this was a new way of programming'
s='hello'+'wow'
s
'hellowow'
s='this was a new way of programming'
s=s[:11]+'very'+s[11:]
s
'this was a verynew way of programming'
>>> del s[0]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    del s[0]
TypeError: 'str' object doesn't support item deletion
>>> s[0]='z'
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s[0]='z'
TypeError: 'str' object does not support item assignment
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s
NameError: name 's' is not defined. Did you mean: 's1'?
