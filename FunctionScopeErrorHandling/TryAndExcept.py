def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print("Error You tried to divide by zero")

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
print(div42by(42))

"""Input :
def div42by(divideBy):
    return 42/divideBy

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
print(div42by(42))

Output :
21.0 (It passed)
3.5 (It passed)
Traceback (most recent call last):
  File "F:/Python Project/Learning2/TryAndExcept.py", line 6, in <module>
    print(div42by(0))
  File "F:/Python Project/Learning2/TryAndExcept.py", line 2, in div42by
    return 42/divideBy
ZeroDivisionError: division by zero"""
