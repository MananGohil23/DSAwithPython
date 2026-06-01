class Solution {
public:
    int count = 0;
    int i;
    int countOdds(int low, int high) {
        for(i=low;i<=high;i++)
        {
            if(i%2!=0)
            {
                count++;
            }
        }
        return count;
    }
};