infty = 999999

def whitespace(words, i, j):
    return (L-(j-i)-sum([len(word) for word in words[i:j+1]]))

def cost(words,i,j):
    total_char_length = sum([len(word) for word in words[i:j+1]])

    if total_char_length > L-(j-i):
        return infty

    if j==len(words)-1:
        return 0

    return whitespace(words,i,j)**3

#words = ["one","two","three","four","five","six","seven"]
#L = 10
words = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa"]
L=15

# Setting up tables
costs = [[None for i in range(len(words))] for j in range(len(words))]
optimum_costs = [[None for i in range(len(words))] for j in range(len(words))]
break_table = [[None for i in range(len(words))] for j in range(len(words))]

for i in range(len(costs)):
    for j in range(len(costs[i])):
        costs[i][j] = cost(words,i,j)

def get_opt_cost(words,i,j):
    # If this subproblem is already solved, return result

    if(optimum_costs[i][j] != None):
        return optimum_costs[i][j]

    # There are now two main classes of ways we could get the optimum
    
    # 1) The best choice is that we put all the words on one line
    canidate_costs = [costs[i][j]]
    canidate_list = [None]

    if i!=j:
        for k in range(i,j):
            # Calculate optimum of words before line split
            left_optimum = get_opt_cost(words,i,k)
            optimum_costs[i][k] = left_optimum

            # Calculate optimum of words after line split
            right_optimum = get_opt_cost(words,k+1,j)
            optimum_costs[k+1][j] = right_optimum

            total_optimum = left_optimum+right_optimum
            canidate_costs.append(total_optimum)
            canidate_list.append(k)

    min_cost= infty
    min_canidate = None
    for n, cost in enumerate(canidate_costs):
        if cost < min_cost:
            min_cost = cost
            min_canidate = canidate_list[n]

    break_table[i][j] = min_canidate

    return min_cost

# Calculate the line breaks
def get_line_breaks(i,j):
    if break_table[i][j] != None:
        opt_break = get_line_breaks(break_table[i][j]+1,j)
        return [break_table[i][j]]+opt_break
    else:
        return []


final_cost = get_opt_cost(words,0,len(words)-1)
breaks = get_line_breaks(0,len(words)-1)

def print_final_paragraph(words,breaks):
    final_str = ""
    cur_break_point = 0
    for n, word in enumerate(words):
        final_str = final_str+word+" "
        if cur_break_point < len(breaks) and n==breaks[cur_break_point]:
            final_str+="\n"
            cur_break_point+=1

    print(final_str)
    
print("Final Cost: ",final_cost)
print("Break Locations: ",breaks)
print("----")
print_final_paragraph(words,breaks)






