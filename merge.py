import yaml

s = """
- &mymap1 !mymap abc
- &mymap2 !mymap def
- &defaults
  a: default a
  b: default b
- &defaults2
  c: default c
- !mymap abcdef
-
  <<: *defaults
  <<: { INLINE: MAPPING }
  <<: !mymap ABC
#  <<: *mymap2
#  <<: *mymap1
  <<: [*mymap2, *mymap1]
  a: new a
  d: new d
#  <<: *defaults2
"""

class MyLoader(yaml.SafeLoader):
    pass

def mymap(c, node):
    return { "MYMAP": node.value }

yaml.add_constructor('!mymap', mymap, Loader=MyLoader);

d = yaml.load(s, Loader=MyLoader)
print("safe_load:")
print(d)
print(yaml.dump(d))
