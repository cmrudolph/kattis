#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define UNVISITED_BINARY 0
#define UNVISITED_DECIMAL 1
#define MAX_ROWS 1000
#define MAX_COLS 1000
#define DECIMAL_TAG_OFFSET 5000000

struct q_entry
{
    int row;
    int col;
};

struct map_entry
{
    int tag;
    int queued;
};

struct map_entry* map[MAX_ROWS];
struct q_entry* q = NULL;
int rows = 0;
int cols = 0;
int q_start = 0;
int q_end = 0;

void queue_neighbor(int r, int c, int unvisited_val)
{
    // Queue cell up if:
    // 1. In range
    // 2. Not already queued
    // 3. Has the same unvisited value as what we are searching for
    if (r >= 0 && r < rows && c >= 0 && c < cols && !map[r][c].queued && map[r][c].tag == unvisited_val)
    {
        //fprintf(stderr, "QUEUING -- R:%d C:%d\n", r, c);
        map[r][c].queued = 1;
        q[q_end].row = r;
        q[q_end].col = c;
        q_end++;
    }
}

int main(void)
{
    int binary_tag = 2;
    int decimal_tag = DECIMAL_TAG_OFFSET;
    char line[MAX_ROWS + 1];

    q = malloc(MAX_ROWS * MAX_COLS * sizeof(struct q_entry));

    for (int i = 0; i < MAX_ROWS; i++)
    {
       map[i] = malloc(MAX_COLS * sizeof(struct map_entry));
    }

    scanf("%d %d", &rows, &cols);
    //fprintf(stderr, "R:%d C:%d\n", rows, cols);

    for (int r = 0; r < rows; r++)
    {
        scanf("%s", &line);

        for (int c = 0; c < cols; c++)
        {
            map[r][c].tag = line[c] - '0';   
            map[r][c].queued = 0;
        }
    }

    for (int r = 0; r < rows; r++)
    {
        for (int c = 0; c < cols; c++)
        {
            int cell_val = map[r][c].tag;
            if (cell_val == UNVISITED_BINARY || cell_val == UNVISITED_DECIMAL)
            {
                q[q_end].row = r;
                q[q_end].col =c;
                q_end++;

                while (q_start < q_end)
                {
                    int curr_row = q[q_start].row;
                    int curr_col = q[q_start].col;

                    //fprintf(stderr, "QSTART:%d QEND:%d R:%d C:%d\n", q_start, q_end, curr_row, curr_col);

                    // Cell being searched matches our current search value (is connected). Process
                    // it, then consider all neighbors.
                    if (map[curr_row][curr_col].tag == cell_val)
                    {
                        if (cell_val == UNVISITED_BINARY)
                        {
                            //fprintf(stderr, "TAGGING -- R:%d C:%d T:%d\n", curr_row, curr_col, binary_tag);
                            map[curr_row][curr_col].tag = binary_tag;
                        }
                        else
                        {
                            //fprintf(stderr, "TAGGING -- R:%d C:%d T:%d\n", curr_row, curr_col, binary_tag);
                            map[curr_row][curr_col].tag = decimal_tag;
                        }

                        queue_neighbor(curr_row - 1, curr_col, cell_val);
                        queue_neighbor(curr_row + 1, curr_col, cell_val);
                        queue_neighbor(curr_row, curr_col - 1, cell_val);
                        queue_neighbor(curr_row, curr_col + 1, cell_val);
                    }

                    q_start++;
                }

                if (cell_val == UNVISITED_BINARY)
                {
                    binary_tag++;
                }
                else
                {
                    decimal_tag++;
                }
            }
        }
    }

    int num_cases;
    int r1, c1, r2, c2;
    int tag1, tag2;

    scanf("%d", &num_cases);

    for (int i = 0; i < num_cases; i++)
    {
        scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
        tag1 = map[r1 - 1][c1 - 1].tag;
        tag2 = map[r2 - 1][c2 - 1].tag;

        if (tag1 == tag2)
        {
            if (tag1 >= DECIMAL_TAG_OFFSET)
            {
                printf("decimal\n");
            }
            else
            {
                printf("binary\n");
            }
        }
        else
        {
            printf("neither\n");
        }
    }

    free(q);

    for (int i = 0; i < MAX_ROWS; i++)
    {
        free(map[i]);
    }

    return 0;
}
