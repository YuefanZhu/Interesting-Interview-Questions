# How do you find maximum product of two numbers in an array of positive integers in O(N) time?
# Constraints:
# First element should be present in a lower index than the second element.
# First element should be strictly lesser than the second element.
def find_max(array):
    if len(array)<2:
        return -1
    max_number = 0;
    max_product = 0;
    array.reverse();
    for i in array:
        if(i >= max_number):
            max_number = i;
        else:
            max_product = max(i * max_number,max_product);
    return max_product;

array=[10,2,3,7,1,9]
print('The max product is',find_max(array))
