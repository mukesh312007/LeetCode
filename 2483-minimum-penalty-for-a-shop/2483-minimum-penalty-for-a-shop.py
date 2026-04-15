class Solution(object):
    def bestClosingTime(self, customers):
        penalty = customers.count('Y')
        
        min_penalty = penalty
        best_time = 0
        
        for i, c in enumerate(customers):
            if c == 'Y':
                penalty -= 1  
            else:
                penalty += 1  
            
            if penalty < min_penalty:
                min_penalty = penalty
                best_time = i + 1 
        return best_time