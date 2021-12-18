# Chapter04-01
# 시퀀스형
# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending Lists)
chars = '+_)(*#^%$@!)'
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))
    
print(code_list1)

# Comprehending Lists
code_list2 = [ord(s) for s in chars]
print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(d) for d in chars if ord(d) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

# 전체출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()

# Generator 생성
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지Xs)












