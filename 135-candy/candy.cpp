class Solution {
public:
    int candy(vector<int>& ratings) 
    {
        int n=ratings.size();
        vector<int>left(n,-1);
        int inc=0;
        left[0]=1;
        for(int i=1;i<n;i++)
        {
            if(ratings[i-1]<ratings[i])
            {
                inc = left[i - 1] + 1; 
                left[i] = inc;
            }
            else
            {
                inc=1;
                left[i]=inc;
            }
        }
        vector<int>right(n,-1);
        right[n-1]=1;
        for(int i=n-2;i>=0;i--)
        {
            if(ratings[i]>ratings[i+1])
            {
                inc=right[i+1]+1;
                right[i]=inc;
            }
            else
            {
                inc=1;
                right[i]=inc;
            }
        }
        int ans=0;
        for(int i=0;i<n;i++)
        {
            ans+=max(left[i],right[i]);
        }
        return ans;
    }
//please upvote 
};