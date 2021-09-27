#include <stdio.h>
#include <stdlib.h>


typedef struct node_ {
  char data[51];
  int len;
  struct node_ *next;
} node;


/* compare two words and return its result
  return 0: same words
  return -1: data1 is larger than data2
  return 1 : data2 is larger than data1
*/
int compareWords(node *data1, node *data2){
  if (data1->len > data2->len){
    return -1;
  }
  else if (data1->len == data2->len){
    for (int i = 0; i < data1->len; i++){
      if (data1->data[i] > data2->data[i]){
        return -1;
      }
      else if (data1->data[i] < data2->data[i]){
        return 1;
      }
    }
    return 0;
  }
  else if (data1->len < data2->len){
    return 1;
  }
}

void pushNode(char *data, node *head){
  node *new;

  new = (node *)malloc(sizeof(node));
  strcpy(new->data, data);
  new->len = strlen(data);

  node *prev = head;
  node *cur = head->next;

  while (cur != NULL){
    int compare = compareWords(cur, new);
    if (compare == -1){
      prev->next = new;
      new->next = cur;
      return;
    }
    else if (compare == 0){
      free(new);
      return;
    }
    else if (compare == 1){
      prev = prev->next;
      cur = cur->next;
    }
  }

  if (cur == NULL){
    prev->next = new;
    new->next = NULL;
  }
}

void showList(node *head){
  node *cur = head->next;
  while(cur != NULL){
    printf("%s\n", cur->data);
    cur = cur->next;
  }
}

int main(void) {
  int n;
  char *data[51];
  node *head;
  head->next = NULL;

  scanf("%d", &n);
  
  for (int i = 0; i < n; i++){
    char temp[51];
    scanf("%s", &temp);
    pushNode(temp, head);
  }
  showList(head);

  return 0;
} 