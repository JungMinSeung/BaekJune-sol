C=int(input())
for i in range(C):
    stu_score=list(map(int,input().split()))
    avg=(sum(stu_score)-stu_score[0])/stu_score[0]
    cnt=0
    for index in range(1,len(stu_score)):
        if stu_score[index]>avg:
            cnt+=1
    ratio=(cnt/stu_score[0])*100
    print('{:0.3f}%'.format(ratio))
