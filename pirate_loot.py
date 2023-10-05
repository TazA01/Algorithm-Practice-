'''Pirate Loot
Programming challenge description:
In the Caribbean Sea, pirates robbed a merchant ship and plundered a chest full of gold coins. The pirates used simple rules on how to distribute the treasure:The captain divides the coins into separate piles and places all the piles in a line
The crew members take regular turns, selecting one pile of gold at a time for themselves
Each pirate can choose to take either the leftmost or rightmost pile of gold
Assume that all pirates are greedy and always take the biggest pile of gold they can. For example, if the values of three piles are 1 3 2, the pirate will choose the rightmost pile which has the value of 2. If piles of gold are equal on both sides, for consistency, the rightmost pile must be taken.Write a program to calculate the total value of gold that each pirate will obtain, given the number of pirates NN in the crew and an array of values for each pile.Input:
The first line of input contains a positive integer NN, which is the count of pirates in the crew.The second line of input contains a space-delimited array of positive integers, representing the total value of gold coins in each pile. For example:3
5 3 2 4 3
Output:
Print a space-delimited array of NN integers, where each integer is a total value of gold received by each pirate in the crew, from the first to the last.The table below shows the turns taken by pirates and the amount of gold obtained by each of them'''

# the pirates take turns and have to choose from the outermost piles
# must grab the highest pile, if values are the same, must choose rightmost pile
# need to compare the two piles
# once the piles are selected, remove them from the array and add them to each pirates total count
# using max, compare the two indices  


def pirate_loot(num_pirates, gold_arr):
    total_sum = [0 for pirate in (range(0, num_pirates))]
    
    while len(gold_arr) != 0:
        for pirate in (range(0,num_pirates)):
            if len(gold_arr) == 1:
                total_sum[pirate] += gold_arr[0]
                gold_arr.pop()
                break
            
            elif gold_arr[0] == gold_arr[-1]:
                total_sum[pirate] += gold_arr[-1]
                gold_arr.remove(gold_arr[-1])

            else:     
                highest_pile = max(gold_arr[0], gold_arr[-1])
                total_sum[pirate] += highest_pile
                gold_arr.remove(highest_pile)
                
    print(total_sum)

    
    
    
pirate_loot(3, [8,4,3,7])  # [11, 7, 4]
pirate_loot(3, [5, 3, 2, 4, 3]) #[9,5,3]
pirate_loot(1, [8, 7, 5, 4, 7, 9]) #[40]
pirate_loot(5,[7,10,4,6,5]) #[7,10,5,6,4]
