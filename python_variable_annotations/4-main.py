#!/usr/bin/env python3

variables = __import__('4-define_variables')
a = variables.a
pi = variables.pi
i_understand_annotations = variables.i_understand_annotations
school = variables.school

print("a is a {} with a value of {}".format(type(a), a))
print("pi is a {} with a value of {}".format(type(pi), pi))
print("i_understand_annotations is a {} with a value of {}".format(
    type(i_understand_annotations), i_understand_annotations
))
print("school is a {} with a value of {}".format(type(school), school))
