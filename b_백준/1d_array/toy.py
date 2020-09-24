import sys

inputs = sys.stdin
C = 0
for idx,line in enumerate(sys.stdin):
    
    if idx == 0:
        C = int(line)
    else:
        nums = list(map(int,line.split(' ')))

        s_num = nums[0]
        scores = nums[1:]

        avg = sum(scores)/s_num

        count = 0
        for n in scores:
            if n > avg:
                count+=1
        
        result = (count/s_num)*100
        print('{:.3f}'.format(result)+'%')