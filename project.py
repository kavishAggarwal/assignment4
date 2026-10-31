team1 = 220
team2 = 180
team3 = 200
team4 = 150
team5 = 190

total = team1 + team2 + team3 + team4 + team5
average = total / 5
print("Total Points:", total)
print("Average Per Team:", average)

stars_per_point = 1
reward_stars = total * stars_per_point
print("Total Reward Stars:", reward_stars)

boxes = reward_stars // 20
leftover = reward_stars % 20
print("Total Boxes:", boxes)
print("Leftover Stars:", leftover)

last_week = 437

print("Better than last week:", total > last_week)
print("Same as last week:", total == last_week)
print("At least as good:", total >= last_week)

total += 29
print("After bonus points:", total)

total -= 20
print("After penalty points:", total)

reward_stars = total * stars_per_point
boxes = reward_stars // 20

print("Final boxes packed:", boxes)
