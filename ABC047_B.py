from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="047"
#問題
problem="b"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  W,H,N=map(int,input().split())
  l,r,u,d=0,W,H,0
  for i in range(N):
    x,y,a=map(int,input().split())
    if a==1: l=max(l,x)
    elif a==2: r=min(r,x)
    elif a==3: d=max(d,y)
    else: u=min(u,y)
  if l>=r or d>=u: print(0)
  else: print((r-l)*(u-d))
  """ここから上にコードを記述"""

  print(test_case[__+1])