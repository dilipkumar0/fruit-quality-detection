import time
arr=[0,1,2,3,4,5,6,7, 8, 9,10]
label=[0,0,0,0,1,1,1,1,1,1]
count=0

while 1==1:
    t = time.localtime()
    tt="image_"+str(count)+".jpg";
    num=label[count]
    line= tt +" "+ time.asctime(t) + " " + str(num);
    print line
    with open("fruitStatus.txt", "a") as myfile:
        myfile.write(line + " "+"\n" );
        
    count=count+1;
    print count
    time.sleep( 10 )
    
    





