#include <stdio.h>
#include <cstdlib>

void update(int *a,int *b) {
    (*a) = 4+5;
    (*b) = abs(4-5);    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);
}