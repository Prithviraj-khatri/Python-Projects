# If the argument is itself not a perfect square then return either -1 or an empty value like None or null,
#  depending on your language. You may assume the argument is non-negative.
# Examples ( Input --> Output )
# 121 --> 144
# 625 --> 676
# 114 --> -1  #  because 114 is not a perfect square

def find_next_square(sq):
    root = int(sq ** 0.5)
    
    if root * root == sq:
        return (root + 1) ** 2
    else:
        return -1