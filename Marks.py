print 'subject','teacher','year','term','mark','type'
import re; import csv; import sys
dict = {}
count=0
inp = raw_input("Query: ")
queries = inp.split(',')
for q in queries:
  field, value = q.split('=', 1)
  dict[field] = value
lines = open('Marks.csv', 'rU').readlines()
for line in csv.DictReader(lines, fieldnames=['subject','teacher','year','term','mark','type']):
  matched = True
  for x in dict:
    if dict[x] != line[x]:
      matched = False
  if matched:
    print lines[count].strip("\n")
  count+=1
z=raw_input()
