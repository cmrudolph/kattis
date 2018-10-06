// https://open.kattis.com/problems/inversefactorial

#include <stdio.h>
#include <stdlib.h>

/* Perform long division on arbitrarily-long values represented as strings. This implementation
does not care about remainders as the problem constraints ensure the division will always work
out with whole number results */
void longdiv(char* dividend, int divisor, char* quotient)
{
    int temp = 0;
    int d_idx = 0;
    int q_idx = 0;

    // Find the first thing big enough to divide into
    while (temp < divisor && dividend[d_idx] != '\0')
    {
        temp = (temp * 10) + (dividend[d_idx++] - '0');
    }

    int div_whole = temp / divisor;
    int div_remain = temp % divisor;
    quotient[q_idx++] = div_whole + '0';

    // Continue dividing until we exhaust the string
    while (dividend[d_idx] != '\0')
    {
        temp = (div_remain * 10) + (dividend[d_idx++] - '0');
        
        div_whole = temp / divisor;
        div_remain = temp % divisor;
        quotient[q_idx++] = div_whole + '0';
    }

    quotient[q_idx] = '\0';

    //fprintf(stderr, "LONGDIV -- D:%s DI:%d Q:%s\n", dividend, divisor, quotient);
}

int main(void)
{
    char* dividend = malloc(1000001 * sizeof(char));
    char* quotient = malloc(1000001 * sizeof(char));
    char* buf_temp;

    scanf("%s", dividend);
    int divisor = 1;

    while(1)
    {
        longdiv(dividend, divisor, quotient);

        // Since we assume things divide evenly, continue until we try to divide
        // something by itself (getting 1).
        if (strlen(quotient) == 1 && quotient[0] == '1')
        {
            break;
        }

        // Old quotient becomes new dividend. Recycle the other buffer.
        buf_temp = quotient;
        quotient = dividend;
        dividend = buf_temp;
        divisor++;
    }

    printf("%d\n", divisor);

    free(dividend);
    free(quotient);

    return 0;
}
