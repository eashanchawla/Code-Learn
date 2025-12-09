def add_binary(a, b):
    # len_padding = len(a) - len(b)    
    # a, b = ('0' * abs(len_padding) + a, b) if len_padding<0 else (a, '0' * len_padding + b)
    # sum_list = list()
    # a = [int(x) for x in list(a)]
    # b = [int(x) for x in list(b)]
    
    # prev_carry=0
    # current_carry=0
    # for i in range(len(a) - 1, -1, -1):
    #     # what was current carry now becomes prev
    #     prev_carry = current_carry
    #     generated_number, current_carry = (a[i]+b[i], 0) if a[i]+b[i]<=1 else (0, 1)

    #     # handling the carry overs now
    #     if prev_carry == 1:
    #         generated_number, current_carry = (1, current_carry) if generated_number == 0 else (0, 1)
    #     sum_list.append(generated_number)
    # if current_carry == 1:
    #     sum_list.append(1)
    # return ''.join(str(x) for x in sum_list[::-1])
            

    #Second slightly better solution
    i, j, carry = len(a)-1, len(b) - 1, 0
    result=[]
    while i>=0 or j>=0 or carry>0:
        int_a, int_b = int(a[i]) if i>=0 else 0, int(b[j]) if j>=0 else 0
        result.append(str((int_a+int_b+carry)%2))
        carry=(int_a + int_b + carry)//2
        i-=1
        j-=1
    return result[::-1]


def needle_in_haystack(needle, haystack):
    return haystack.find(needle)


ab = add_binary('111', '1')

needle_in_haystack('eashan', 'sadbutsad')


def longest_common_prefix(strs):
    # lcp = list()
    # max_len = min([len(x) for x in strs])
    # if len(strs)==1:
    #     return strs[0]
    # for j in range(max_len):
    #     mila=True
    #     for i in range(len(strs) - 1):
    #         if strs[i+1][j] != strs[i][j]:
    #             mila=False
    #             break
    #     if mila:
    #         lcp.append(strs[0][j])
    #     else:
    #         break
    # return ''.join(lcp)

    selected_string = min(strs, key=len)
    while selected_string != '':
        if all(s.startswith(selected_string) for s in strs):
            return selected_string
        else:
            selected_string = selected_string[:-1]
    return ''

print(longest_common_prefix(["cir","car"]))