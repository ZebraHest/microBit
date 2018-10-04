from microbit import*
while True:
 if button_a.is_pressed():
  display.show(Image.YES)
 elif button_b.is_pressed():
  display.show(Image.NO)
 else:
  display.show(Image.ASLEEP)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
