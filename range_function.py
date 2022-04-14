# range function (range())

# Range function generate number with specified range 

# syntax : -
    # range (start,end,step)

# in range fucntion there are three parameters start , end , step 
    # start : -
        # in range funtion start use for the starting for our range 
        # if do not specified the starting point by default the start will start from 0 
        # start is inclusive thats why we have to specified start is not compulsary
        
    # end : -
        # In range function end use for ending our range 
        # if we do not specified end for our range it will go in infinity loop 
        # end is exclusive that why we always have to specified end 

    # step : -
        # in range function step use for step count for our range 
        # if we do not specified step for our range by default it take step 1
        # also step specified is not compulsary


for a in range(1,10,2):
    print(a)