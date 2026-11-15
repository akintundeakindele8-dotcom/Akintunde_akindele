import java.util.Scanner;
public class Test{
    static Scanner input = new Scanner(System.in);
    public static void callPhoneBook(){
   
      while(true){
      String phoneBookMenu = """
      Phone Book Menu
 In this menu, you can manage the names and phone numbers in the phone and the SIM card
Press:
        1. Search
        2. Service No
        3. Add name
        4. Erase
        5. Edit
        6. Copy
        7. Assign Tone
        8. Send b'card
        9.Options - Memory in use
        10. Options - Type of view
        11.Options - Memory status
        12. Speed dials
        13. Voice Tags
        14. Back to Main Menu...
""";
System.out.print(phoneBookMenu);
System.out.print("Enter a section number: ");
    int phoneBookMenuSection = input.nextInt();
    switch (phoneBookMenuSection){
        case 1->{
                System.out.print("Search: You can recall the desired name and phone number from the phone book to make a call. When you browse through the names and phone numbers, an indicator is shown in the top right corner of the display if the selected name or phone number is saved in the SIM card ");
                }
            case 2->{
                System.out.print("Service Nos: Calls the service number of your service provider, which is saved in your SIM card.");
                }
            case 3->{
                System.out.print("Add name: You can save a name and phone number in the phone book.");
                }
            case 4->{
                System.out.print("Erase: You can delete names and phone numbers from the selected phone book one by one or all at once.");
                }
            case 5->{
                System.out.print("Edit: You can modify the names and phone numbers saved in the phone book. Scroll to the desired name or phone number, and press ");
                }
            case 6->{
                System.out.print("Copy:You can copy or move names and phone numbers from the phone to the SIM card (or vice versa) one by one or all at once. ");
                }
            case 7->{
                System.out.print("Assign tone: You can set the phone to play the desired ringing tone when you receive a call from a particular phone number. Scroll to the caller's name or phone number, press (Assign), and select the desired ringing tone.");
                }
            case 8->{
                System.out.print("Send b'card: You can send a name and phone number ('business card') as a text message to a compatible phone.");
                }
            case 9->{
                System.out.print("Options - Memory in use: You can select whether the names and phone numbers are saved in your phone or the SIM card. Note that when you change the SIM card, the SIM card option is automatically selected.");
                }
            case 10->{
               System.out.print("Options - Type of view: You can select the way the saved phone numbers and names are displayed.");
               }
            case 11->{
               System.out.print("Options - Memory status: Shows how many names and phone numbers can still be saved and are currently saved in the phone and the SIM card");
               }
            case 12->{
                System.out.print("Speed dials: You can set the desired number key (2 to 9) to work as a speed dialing key. Scroll to the desired key, press (Assign), and select a name or phone number.");
                }
            case 13->{
                System.out.print("Voice tags: You can dial a phone number by saying one or more words that you have attached to it as a 'voice tag' The voice tag can be, for example, a name, and you can record a voice tag to eight phone numbers in the phone book. You can also listen to, change, or erase the recorded voice tag.");
                System.out.print("To record voice tag: ");
                System.out.print("To make a call using a voice tag");
                }
            case 14->{
               System.out.print("Returning to main menu...\n");
                
                return;
              }
        default->{
          System.out.print("Invalid Entry...Try Again");
              } 
    
    }
      } 
    
    
    }
public static void main(String[] args){
 String mainMenu = """
Welcome to Nokia 5510 Menu Manual
Press:
1 for Phone Book 
2 for Message
3 for Chat
4 for Call register
5 for Tones
6 for Settings
7 for Call Divert
8 for Music
9 for Games
10 for Calculator
11 for Reminder
12 for Clock
13 for Profile
14 for Service
15 for Sim Services
16 for Exit process
""";
System.out.print(mainMenu);
System.out.print("Enter a section number: ");
    int startingMenu = input.nextInt();
    
    switch(startingMenu){
    case 1 -> {
      callPhoneBook();
    }
    
    }



}
}
