start = int(input("Ведіть перше число --->"))
end = int(input("Ведіть друге число --->"))
while start < end:
    if start % 2 == 1:
      print(start)
      start += 2
    if start % 2 == 0:
        start = start + 1
    while start < end:
        if start % 2 == 1:
            print(start)
            start += 2