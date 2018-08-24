public IList<IList<int>> ThreeSum(int[] S) 
{
    var result = new List<IList<int>>();
    
    if (S.Length < 3)
    {
        return result;
    }
    
    Array.Sort(S);
    
    for (int first = 0; first < S.Length - 2; first++)
    {
        int second = first + 1;
        int third = S.Length - 1;
        
        if (first != 0 && S[first] == S[first-1])
        {
            continue;
        }
        
        while (second < third)
        {
            if (second > first + 1 && S[second] == S[second-1])
            {
                second++;
                continue;
            }
            
            int sum = S[first] + S[second] + S[third];
            
            if (sum == 0)
            {
                var triple = new List<int>();
                triple.Add(S[first]);
                triple.Add(S[second]);
                triple.Add(S[third]);
                result.Add(triple);
                second++;
                third--;
            }
            else if (sum > 0)
            {
                third--;
            }
            else
            {
                second++;
            }
        }
    }
    
    return result;
}
