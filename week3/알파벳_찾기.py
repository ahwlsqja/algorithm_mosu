s = input()
    
# 각 문자의 첫 등장 위치를 딕셔너리에 저장
char_positions = {}
for i, char in enumerate(s):
    if char not in char_positions:
        char_positions[char] = i
    
result = []
for i in range(26):
    char = chr(ord('a') + i)
    result.append(char_positions.get(char, -1))
    
print(' '.join(map(str, result)))