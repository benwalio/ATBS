# collatz

input_num = 8

def collatz(number):
   if number % 2 == 0:
      result = number // 2
      print result
      return result
   else:
      result = 3 * number + 1
      print result
      return result

collatz(input_num)
