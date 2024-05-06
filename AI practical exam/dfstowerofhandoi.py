def tower_of_hanoi(n, source, target, auxiliary):
  if n == 1:
    print(f"Move disk 1 from {source} to {target}")
    return
  tower_of_hanoi(n-1, source, auxiliary, target)
  print(f"Move disk {n} from {source} to {target}")
  tower_of_hanoi(n-1, auxiliary, target, source)
# Get user input for the number of disks
while True:
  try:
    num_disks = int(input("Enter the number of disks (positive integer): "))
    if num_disks > 0:
      break
    else:
      print("Invalid input. Please enter a positive integer.")
  except ValueError:
    print("Invalid input. Please enter an integer.")
# Solve the puzzle with user-provided number of disks
tower_of_hanoi(num_disks, 'A', 'C', 'B')