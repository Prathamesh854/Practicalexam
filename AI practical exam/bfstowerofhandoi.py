import collections
def bfs(n, source, target, auxiliary):
    
    initial_state = (tuple(range(n, 0, -1)), (), ())  
   
    def state_key(state):
        return tuple(tuple(peg) for peg in state)
   
    queue = collections.deque([(initial_state, [])])
    
    visited = set()
    visited.add(state_key(initial_state))
    while queue:
        current_state, moves = queue.popleft()
        if current_state[pegs.index(target)] == tuple(range(n, 0, -1)):
            return moves
        
        for i in range(3):
            if not current_state[i]: 
                continue
           
            for j in range(3):
                if i == j:
                    continue
                if current_state[j] and current_state[j][-1] < current_state[i][-1]:
                    continue  
                new_state = [list(peg) for peg in current_state]  
                disk = new_state[i].pop()  
                new_state[j].append(disk)             
                new_state = tuple(tuple(peg) for peg in new_state)  
                if state_key(new_state) not in visited:
                    
                    visited.add(state_key(new_state))
                    new_moves = moves + [f"Move disk {disk} from {pegs[i]} to {pegs[j]}"]
                    queue.append((new_state, new_moves))   
    return None  
if __name__ == "__main__":
  num_disks = 3
  source, target, auxiliary = "A", "B", "C"
  pegs = (source, auxiliary, target)  
  solution = bfs(num_disks, source, target, auxiliary)
  if solution:
    for step, move in enumerate(solution):
        print(f"Step {step + 1}: {move}")
  else:
    print("No solution found.")