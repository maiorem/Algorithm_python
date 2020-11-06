N = int(input())
count=1
sequence=6
end_of_seq=1
if N==1:
    print(count)
else:
    while True:
        end_of_seq = end_of_seq + sequence 
        count += 1 
        if N <= end_of_seq: 
            print(count)
            break 
        sequence += 6