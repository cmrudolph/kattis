// NAME : Balanced Diet
// URL  : https://open.kattis.com/problems/balanceddiet
// =============================================================================
// Use recursion to figure out all the possible sums we can encounter by
// combining values in all possible ways. Without any optimizations this
// solution is O(2<sup>N</sup>). However, the problem is conducive to dynamic
// programming since once a subproblem has been solved we can save the result
// leverage it to avoid redundant work. Solved in C# to compare language
// performance versus C on judging machines.
// =============================================================================

using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
    public static void Main()
    {
        string line = Console.ReadLine();
        while (line != "0")
        {
            // Ignore the count and just read the remaining numbers into an array (length comes for
            // free via the array)
            int[] values = line.Split().Skip(1).Select(int.Parse).ToArray();
            Result result = CalcMinDiff(values);

            // Make sure the larger value is put first.
            if (result.Sum1 > result.Sum2)
            {
                Console.WriteLine("{0} {1}", result.Sum1, result.Sum2);
            }
            else
            {
                 Console.WriteLine("{0} {1}", result.Sum2, result.Sum1);
            }

            line = Console.ReadLine();
        }
    }

    public static Result CalcMinDiff(int[] arr)
    {
        var memoizedSums = new Dictionary<int, Result>();
        int totalSum = arr.Sum();

        // Kick off the recursion 
        return CalcMinDiff(arr, arr.Length, 0, totalSum, memoizedSums);
    }

    public static Result CalcMinDiff(int[] arr, int n, int sum1, int totalSum, Dictionary<int, Result> memoizedSums)
    {
        if (n == 0)
        {
            int sum2 = totalSum - sum1;

            // BASE CASE: Return the absolute difference between the two sums.
            return new Result { Sum1 = sum1, Sum2 = sum2, Diff = Math.Abs(sum1 - sum2) };
        }

        // OPTIMIZATION: If we have seen this subproblem before, there is no sense doing the computation
        // again. We already know the result. Return it and save time. Given the integer constraints, we
        // can pack both values into a single int to serve as a fast dictionary key.
        int memoizeKey = (n << 16) | sum1;
        Result memoizeResult;
        if (memoizedSums.TryGetValue(memoizeKey, out memoizeResult))
        {
            return memoizeResult;
        }

        // RECURSION: From this point investigate both paths (including the item in the first
        // sum versus including it in the second sum).
        Result resultA = CalcMinDiff(arr, n-1, sum1 + arr[n-1], totalSum, memoizedSums);
        Result resultB = CalcMinDiff(arr, n-1, sum1, totalSum, memoizedSums);

        // Best result = the one with the smallest difference between the sums.
        Result best = resultA.Diff < resultB.Diff
            ? resultA
            : resultB;

        memoizedSums.Add(memoizeKey, best);

        return best;
    }

    public struct Result
    {
        public int Sum1;
        public int Sum2;
        public int Diff;
    }
}