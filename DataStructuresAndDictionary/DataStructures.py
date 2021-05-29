#Data Structure
#It is a list of dictionaries

#type() function, it returns the datatype of variables

cat = {'name':"Alice", 'age':6, 'color':"Brown"}
print(type(42))
print(type("Hello"))
print(type(3.14))
print(type(cat))
print(type(cat['name']))
"""
<class 'int'>
<class 'str'>
<class 'float'>
<class 'dict'>
<class 'str'>
"""

print("This is a simple List cat")
print(cat)
allCats = []
allCats.append({'name':"Alice", 'age':6, 'color':"Brown"})
allCats.append({'name':"Barbie", 'age':5, 'color':"White"})
allCats.append({'name':"Alice", 'age':6, 'color':"Grey"})
print("\nThis is a Data Structure in Python")
print(allCats)

"""
TIC-TAC-TOE board representation using Data Structure

 O | O | O 
--- --- ---
 X | X |   
--- --- ---
   |   | X 
"""
print("We use the representation of spaces with numbers 1-9 Row-wise as below, just an example")
print(" 1 | 2 | 3 ")
print("--- --- ---")
print(" 4 | 5 | 6 ")
print("--- --- ---")
print(" 7 | 8 | 9 ")

theBoard = {1:' ',2:' ',3:' ',4:' ',5:'X',6:' ',7:' ',8:' ',9:' '}
print(theBoard)
theBoard[1]='O'
theBoard[2]='O'
theBoard[3]='O'
theBoard[4]='X'
theBoard[9]='X'
print(theBoard)
print()
print()
print()
print()
def print_board(board):
	print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
	print("--- --- ---")
	print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
	print("--- --- ---")
	print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
print(print_board(theBoard))