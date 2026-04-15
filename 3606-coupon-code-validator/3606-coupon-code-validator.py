class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        order = {line: i for i, line in enumerate(valid_lines)}
        
        def is_valid_code(s):
            if not s:
                return False
            for ch in s:
                if not (ch.isalnum() or ch == '_'):
                    return False
            return True
        
        valid = []
        
        for c, b, active in zip(code, businessLine, isActive):
            if (
                active and
                b in order and
                is_valid_code(c)
            ):
                valid.append((order[b], c))
        
        # sort by businessLine order, then by code
        valid.sort()
        
        return [c for _, c in valid]