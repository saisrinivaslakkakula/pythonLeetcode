This is a binary search problem basically
consider eg: [1,2,3,4,5,6,7,8,9,10] with D = 5

First, the intution is, to ship the given packages, the weight of ship must be atleast the max weight of all packages. In the same way, the ship weight goes maximum to sum of all weights. that means all packages could be shipped in one day.

Hence our ship's capacity must be somewhere between max weight of package - Sum of all packages;
In this case the limits are 10-55; our ship's capacity will somewhere be between 10 and 55.

So we first calculate an arbitrary mid limit and check if we can accommodate all packages in the given arbitrary capacity selected. 
this is done by traversing the array of weights and accumulating it . once the accumulation exceeds the arbitrary capacity, that means we ship all these packages in one day and increment the day count till that point.

once we are done traversing the array, we check the days it took to ship the packages having been selected the arbitrary weight. if the day count is **more** , Then it indicates that our arbitrary capacity must be increased to accomodate all packages. we then choose the next arbitrary weight to current arbitrary + hight /2; i.e next arbitrary lies between currnet arbitrary and highest weight.

if not, tat means the days are less. Which means we need to decrease our arbitrary weight to accomodate all packages in D days. In this case new arbitrary is cosen between low and current arbitrary.

we repeat the same process of traversing the array and checking the feasibility of accommodating them in D days. 

At some point, we will reach low >= high; that is our break point in binary search of arbitrary weights and the low value thus gives us the value of lowest arbitrary weight.

Walk Through:
consider eg: [1,2,3,4,5,6,7,8,9,10] with D = 5

low = 10 high = 55; capacity is between 10-55.

we choose 10+55 /2 = 32 as initial arbitrary point.

in that case if we traverse the array, 
1+2+3+4+5+6+7 = 28; After this we reach >32 if we add next weight i.e 28+8 >32.
hence this is Day 1 D=1
Similarly Day 2:
8+9 = 17
Day 3: 
10

The # of days = 3; which means we are considering more capacity than required. hence decrease the capacity.

New Capacity = 10 + 32 /2 = 21

in this case:

D1:
1+2+3+4+5+6 = 21
D2: 7+8 = 15
D3: 9+10 = 19

again decrease the capacity to next mid;

new Capacity = 10+21 /2 = 15

D1: 1+2+3+4+5 = 15
D2: 6+7 = 13
D3: 8
D4: 9
D5: 10

So the answer is 15.

Refer to image in github for more information.


