// NAME : Balanced Diet
// URL  : https://open.kattis.com/problems/balanceddiet
// =============================================================================
// Use recursion to figure out all the possible sums we can encounter by
// combining values in all possible ways. Without any optimizations this
// solution is O(2<sup>N</sup>). However, the problem is conducive to dynamic
// programming since once a subproblem has been solved we can save the result
// leverage it to avoid redundant work.
// =============================================================================

#include <stdio.h>
#include <stdlib.h>

#define UNDEFINED -1
#define MAX_VALUES 20
#define MAX_MEMOIZE_VALUES 524288 // 14 bits for sum, 5 bits for n

struct result
{
    int sum1;
    int sum2;
    int diff;
};

struct result calc_min_diff(int* values, int n, int sum1, int total_sum, struct result* memoized)
{
    if (n == 0)
    {
        // BASE CASE: Return the absolute difference between the two sums.
        struct result r;
        r.sum1 = sum1;
        r.sum2 = total_sum - sum1;
        r.diff = abs(r.sum1 - r.sum2);

        return r;
    }

    // OPTIMIZATION: If we have seen this subproblem before, there is no sense doing the computation
    // again. We already know the result. Return it and save time. Given the integer constraints, we
    // can pack both values into a single int to serve as a fast dictionary key.
    int memoize_key = (n << 14) | sum1;
    struct result memoize_result = memoized[memoize_key];
    if (memoize_result.diff != UNDEFINED)
    {
        return memoize_result;
    }

    // RECURSION: From this point investigate both paths (including the item in the first
    // sum versus including it in the second sum).
    struct result a = calc_min_diff(values, n-1, sum1 + values[n-1], total_sum, memoized);
    struct result b = calc_min_diff(values, n-1, sum1, total_sum, memoized);

    // Best result = the one with the smallest difference between the sums.
    if (a.diff < b.diff)
    {
        memoized[memoize_key] = a;
        return a;
    }

    memoized[memoize_key] = b;
    return b;
}

struct result calc(int* values, int value_count)
{
    int total_sum = 0;
    for (int i = 0; i < value_count; i++)
    {
        total_sum += values[i];
    }

    // Initialize the memoize table by filling it with placeholder values.
    int memoized_len = MAX_MEMOIZE_VALUES * sizeof(struct result);
    struct result* memoized = malloc(memoized_len);
    memset(memoized, UNDEFINED, memoized_len);

    // Kick off the recursion 
    struct result r = calc_min_diff(values, value_count, 0, total_sum, memoized);
    free(memoized);

    return r;
}


int main()
{
    int value_count;
    scanf("%d", &value_count);

    while (value_count != 0)
    {
        int values[MAX_VALUES];
        for (int i = 0; i < value_count; i++)
        {
            scanf("%d", &values[i]);
        }

        struct result r = calc(values, value_count);

        // Make sure the larger value is put first.
        if (r.sum1 > r.sum2)
        {
            printf("%d %d\n", r.sum1, r.sum2);
        }
        else
        {
            printf("%d %d\n", r.sum2, r.sum1);
        }

        scanf("%d", &value_count);        
    }

    return 0;
}