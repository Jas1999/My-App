import java.io.BufferedReader;// imported stuff to ensure the code works
import java.io.IOException;
import java.io.InputStreamReader;

//By: Jasman Singh Sahi

public class MarkCalculator {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		
		int UserOption ;// the users input in the menu will be stored here
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // Declare Console reader, this allows the users input to be inserted
							
		do{// outer do while to ensure the program loops
			
			do{//a do loop to ensure the input is proper
					
					System.out.println("");// seperation enter space
			
					System.out.println( "Pick Option");
				
					System.out.println( "0. Exit");
			
					System.out.println( "1. Final Average");

					System.out.println( "2. Exam Mark Needed");
			
					System.out.println( "3. Overall Unweighted Average");

						UserOption = Integer.parseInt(br.readLine());// user is asked for the which option they want to use
						
			}while(UserOption < 0 || UserOption > 3);// makes sure the useroption input is not under 0 and not over 3

							switch(UserOption){// a switch based on the useroption 
				
								case 0:// case 0 is a exit case
					
									System.exit(UserOption);// the system.exit will terminate the program stopping the while loop from reload the options and stopping the continous loop
					
									break;// will stop the switch from going further
					
								case 1:// used to calc the final average of the user
					
									FinalAverageCalc();// method to calc the final average
								
									break;
					
								case 2:
								
									ExamMarkNeeded();// method used to find the mark needed by the user to find the final exam mark needed
					
									break;
					
								case 3:
								
									OverallAverageCalc();// calcs the overall unweighted average
					
									break;
				
						}
					
		}while(true);
		
	}

	private static void OverallAverageCalc() throws IOException {// method for calcing the overall unweighted average, ioexception used for console probelms
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // Declare Console reader, redeclared in the method
		
			int NumberOfMarks;// stores number of marks being entered
		
			int totalMarks = 0;// the sum off all the marks
		
			int OverallAverage;//  the average
		
			int [] Marks = null;// array to hold all the marks
		
				System.out.print(" Enter number of marks:  ");// header to remind whats being found
		
					NumberOfMarks = Integer.parseInt(br.readLine());// user asked number of marks 

						Marks = new int [ NumberOfMarks ];// array  the size of the total entries to store all the marks
						
							for(int i = 0;NumberOfMarks > i; i++ ){// for loop  to cycle through number of mark enteries and store them
						
								System.out.print(" Enter Mark  " + (i + 1) + ". (%) ");

									Marks [i] = Integer.parseInt(br.readLine());  // a asking for the next mark every repeat
				
									totalMarks += Marks [i];// adding up the sum of the marks into the totalmarks variable

						}
					
				OverallAverage = totalMarks / NumberOfMarks;// total marks divided by the num will eqaul the average 
				
					System.out.print(" The Total Unweighted Average is " + (OverallAverage) + "% !");// will print the average
	
					System.out.println("");
	}
	
	private static void FinalAverageCalc() throws IOException {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // Declare Console reader
		
			double FinalGradeNeed;// a double that will hold the final grade need by the usre
		
			double EMark;// exam mark
		
			double Evalue;// exam value
		
			double Grade;// current grade
		
			double Gvalue;// grade worth
		
			int finalgrade;// final mark
		
				System.out.println("  Exam Mark needed: ");// header to remind whats being found
		
				System.out.println("-------------------------");

		
					System.out.print(" Grade(%):  ");
		
						Grade = Double.parseDouble(br.readLine()); // asking user for each aspect
		
					System.out.print(" The Mark on Exam(%):  ");
		
						EMark = Double.parseDouble(br.readLine()); 
		
					System.out.print(" Exam Value(%):  ");
		
						Evalue = Double.parseDouble(br.readLine());
					
							Gvalue = 100 - Evalue;// the current grade worth is minus the exam worth
		
		finalgrade = (int) (((Grade * Gvalue) + (EMark * Evalue )) / 100);// formula for caluclating the average
		
			System.out.println(" Your Final Mark is " + finalgrade + "% !");// print line
			

	}

	private static void ExamMarkNeeded() throws IOException {
		// TODO Auto-generated method stub
		
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // Declare Console reader
		
		int FinalGradeNeed;// a double that will hold the final grade need by the usre
		
		double MarkWanted;// mark wanted by user
		
		double Evalue;// exam value 
		
		double Gvalue;// grade value
		
		double Grade;// current grade
		
			System.out.println("  Exam Mark needed: ");// header to remind whats being found
		
			System.out.println("-------------------------");

		
				System.out.print(" Grade(%):  ");
		
					Grade = Double.parseDouble(br.readLine()); 	// asking user for each aspect	
		
				System.out.print(" The Mark Wanted(%):  ");
		
					MarkWanted = Double.parseDouble(br.readLine()); 				
				
				System.out.print(" Exam Value(%):  ");
			
					Evalue = Double.parseDouble(br.readLine());	
				
						Gvalue = 100 - Evalue;// the current grade worth is minus the exam worth
	
		FinalGradeNeed = (int) (((MarkWanted * 100) - (Grade * Gvalue)) / Evalue);// formuala to find mark needed
	
			System.out.println(" The Mark need to obtain this is average is " + FinalGradeNeed + "% !");
		
			System.out.println("");
	}

}
