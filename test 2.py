combinations = [[a, b, c, d] \
                for a in range(0,101)  \
                for b in range(0,101)  \
                for c in range(0,101)  \
                for d in range(0,101)  \
                if a + b + c + d == 100]
print(combinations)