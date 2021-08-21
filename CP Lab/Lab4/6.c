// Lab project by Sarang Dev Saha (20UCS173)
//LAB4_QUES 6
/*A 30 kg boulder was initially moving at a velocity of 10 m/s, in order to stop it 10 N
of constant retarding force is applied on it. After how long will the boulder stop? */
# include <stdio.h>

int main(){
    
	// Defining all the variables and assigning their values according to question.
    float fin_vel, in_vel, acc, time, force, mass;
    fin_vel=0;
	in_vel=10;
	force=10;
	mass=30;
	// using formulae like F=ma and v= u+at
	acc=force/mass;
	time=(in_vel-fin_vel)/acc;
    
    
    printf("The Time required for the boulder to stop is %f",time);
    
    
    return 0;
}