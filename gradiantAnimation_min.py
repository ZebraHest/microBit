from microbit import*
def to_string(i,j):
 num=abs(i+j)%17
 if num>8:
  num=(16-num)%9
 return str(num+1)
def make_line(i,j):
 return(to_string(i+0,j)+to_string(i+1,j)+to_string(i+2,j)+to_string(i+3,j)+to_string(i+4,j)+':')
def make_screen(i,j):
 return Image(make_line(i+0,j)+make_line(i+1,j)+make_line(i+2,j)+make_line(i+3,j)+make_line(i+4,j))
k=0
while True:
 show=make_screen(k,0)
 display.show(show)
 k=k+1
 sleep(1)
 while button_a.is_pressed():
  sleep(1)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
