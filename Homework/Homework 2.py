#Writeafunctionthattakesinastring,andprintsoutthefollowing:
#● Thestringinuppercase
#● Thestringinlowercase
#● Whetherthewordstartswiththesameletterasthelastletter
#● Thestringwithallinstancesofthefirstletterreplacedwith“[REDACTED]”

string = input('Please enter a string')
def string_methods(string):
  print(string.upper())
  print(string.lower())

  if string[0] == string[-1]:
    print(True)
  else:
    print(False)

  for x in string:
    if x == string[0]:
      print('[REDACTED]')
    else:
      print(x)

string_methods(string)