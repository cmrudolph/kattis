// https://open.kattis.com/problems/inversefactorial

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    char* factorial = malloc(1000001 * sizeof(char));

    scanf("%s", factorial);
    int factorial_len = strlen(factorial);

    if (factorial_len <= 6)
    {
        // Special case some of the early numbers since they don't play nicely by the
        // "each number is definitely longer than the previous one" rule.
        int as_int = atoi(factorial);
        int result;

        switch(as_int)
        {
            case 1: result = 1; break;
            case 2: result = 2; break;
            case 6: result = 3; break;
            case 24: result = 4; break;
            case 120: result = 5; break;
            case 720: result = 6; break;
            case 5040: result = 7; break;
            case 40320: result = 8; break;
            default: result = 9; break;
        }

        printf("%d\n", result);
    }
    else
    {
        // Case for 10+. Each number will have more digits than the last. Count digits
        // until we find a string of the right length.
        double sum_of_logs = 0;
        for (int i = 1; i <= 9; i++)
        {
            sum_of_logs += log10(i);
        }

        int curr_val = 10;
        while(1)
        {
            sum_of_logs += log10(curr_val);
            // fprintf(stderr, "Compare -- SOL:%f CV:%d\n", sum_of_logs, curr_val);
            if (sum_of_logs > factorial_len)
            {
                printf("%d\n", curr_val - 1);
                break;
            }

            curr_val++;
        }
    }

    free(factorial);

    return 0;
}
