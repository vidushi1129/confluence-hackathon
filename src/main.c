#include <stdio.h> 

int main(){
  int choice;

printf("===Smart Student Tracker ===\n");
printf("1. Add Attendence\n"):
printf("2. Add Study Hours\n");
printf("3. Exit\n");

printf("Enter your choice: ");
scanf("%d" , &choice);


switch(choice){
case 1:
printf("Attendance recorded (demo version)\n");
break;

case 2:
printf("Study hours recorded(demo version)\n");
break;

case 3:
printf("Exiting program...\n");
break;

default:
printf("Invalid choice\n");
}

  
