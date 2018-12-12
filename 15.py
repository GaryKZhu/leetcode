#Brute Force
solution = []
        answer = []
        for x in range(0, len(nums)):
            for y in range(x+1, len(nums)):
                for z in range(y+1, len(nums)):
                    if nums[x] + nums[y] + nums[z] == 0:
                        answer.append(nums[x])
                        answer.append(nums[y])
                        answer.append(nums[z])
                        if sorted(answer) in solution:
                            answer = []
                            continue
                        else:
                            solution.append(sorted(answer))
                            answer = []
                            continue
        return solution
        
