# LINEAR SEARCH: thuật toán tìm kiếm ngang hàng

# List: 
# - collection of similar items (data structure)
# - items are ordered using index
# - index starts from 0

# game1 = 'League of Legends'
# game2 = '...'
# game3 = '...'


# print(games)

# print('My favorite game is ' + games[0])

# print(games[4]) # error: IndexError: list index out of range

# print(games[-1]) # games[3]

games = ['League of Legends', 'Roblox', 'Minecraft', 'Mobile legend', 'Overwatch']

# print(games[0])
# print(games[1])
# print(games[2])
# print(games[3])
# print(games[4])

# lặp qua các phần tử của danh sách: dùng for + index (i)

for i in range(len(games)):
    print(games[i])

