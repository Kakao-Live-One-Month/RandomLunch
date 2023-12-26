from itertools import combinations

# Step 1
elements = ['a', 'b', 'c', 'd']

# Step 2
combinations_list = list(combinations(elements, 2))
original_arrays = combinations_list[:6]

# print(original_arrays)

# Step 3: 랜덤으로 첫 번째 배열 선택
first_array = original_arrays[0]
# original_arrays.remove(first_array)
print(f"첫 번째 배열: {first_array}")

# Step 3-5
n=int(input())
while original_arrays:
    if n < 0:
        break
    # Step 4: 이전 배열의 인덱스 0번이나 1번 요소를 갖는 배열을 찾고 랜덤으로 선택
    next_arrays = [arr for arr in original_arrays if first_array[0] in arr or first_array[1] in arr]
    # print(original_arrays)
    if next_arrays:
        second_array = next_arrays[0]
        original_arrays.remove(second_array)
        # print(original_arrays)
        original_arrays.append(second_array)
        # print(original_arrays)
        print(f"다음 배열: {second_array}")
    else:
        # print("다음 배열을 찾을 수 없습니다.")
        break
    first_array = second_array
    # print(original_arrays)
    n -= 1

# Step 5: original_arrays에 배열이 모두 없어질 때까지 반복
