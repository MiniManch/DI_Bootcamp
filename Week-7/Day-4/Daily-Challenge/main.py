# Daily challenge
# Write a function to compute 5/0 and use try/except to catch the exceptions.
# Bonus : use some Buit-in exceptions of Python :


def five_divided_by_zero():
  try:
    print(5 / 0)
  except ZeroDivisionError:
    raise Exception('Division by zero is illegal ')

five_divided_by_zero()