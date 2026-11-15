import java.util.Scanner;
public class SwitchTestJava{
static Scanner input = new Scanner(System.in);
    public static void callPhoneBook(){
   
      while(true){
      String phoneBookMenu = """
      ==========Phone Book Menu==========
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
                System.out.print("->Search: You can recall the desired name and phone number from the phone book to make a call. When you browse through the names and phone numbers, an indicator is shown in the top right corner of the display if the selected name or phone number is saved in the SIM card\n");
                }
            case 2->{
                System.out.print("Service Nos: Calls the service number of your service provider, which is saved in your SIM card\n.");
                }
            case 3->{
                System.out.print("Add name: You can save a name and phone number in the phone book.\n");
                }
            case 4->{
                System.out.print("Erase: You can delete names and phone numbers from the selected phone book one by one or all at once.\n");
                }
            case 5->{
                System.out.print("Edit: You can modify the names and phone numbers saved in the phone book. Scroll to the desired name or phone number, and press.\n");
                }
            case 6->{
                System.out.print("Copy:You can copy or move names and phone numbers from the phone to the SIM card (or vice versa) one by one or all at once.\n");
                }
            case 7->{
                System.out.print("Assign tone: You can set the phone to play the desired ringing tone when you receive a call from a particular phone number. Scroll to the caller's name or phone number, press (Assign), and select the desired ringing tone.\n");
                }
            case 8->{
                System.out.print("Send b'card: You can send a name and phone number ('business card') as a text message to a compatible phone.\n");
                }
            case 9->{
                System.out.print("Options - Memory in use: You can select whether the names and phone numbers are saved in your phone or the SIM card. Note that when you change the SIM card, the SIM card option is automatically selected.\n");
                }
            case 10->{
               System.out.print("Options - Type of view: You can select the way the saved phone numbers and names are displayed.\n");
               }
            case 11->{
               System.out.print("Options - Memory status: Shows how many names and phone numbers can still be saved and are currently saved in the phone and the SIM card.\n");
               }
            case 12->{
                System.out.print("Speed dials: You can set the desired number key (2 to 9) to work as a speed dialing key. Scroll to the desired key, press (Assign), and select a name or phone number.\n");
                }
            case 13->{
                while(true){
                String voiceTag = """
                                  ========== Voice tags==========
                 You can dial a phone number by saying one or more words that you have attached to it as a 'voice tag' The voice tag can be, for example, a name, and you can record a voice tag to eight phone numbers in the phone book. You can also listen to, change, or erase the recorded voice tag.
                 1 to record a voice tag
                 2 to make a call using a voice tag
                 3 to return to Phone book menu
                 """;
                
                System.out.print(voiceTag);
                System.out.print("Select an option: ");
                int voiceTagSelection = input.nextInt();
                 switch(voiceTagSelection){
                 case 1 ->{
                 System.out.print("Insert Sim Card\n");
                 }
                 case 2 ->{
                 System.out.print("Insert Sim Card\n");
                 }
                 case 3 -> {
                   System.out.println("Returning to Phone Book Menu....");
                  callPhoneBook();
                  return;
                 }
                 default ->{
                 System.out.print("Invalid Entry...Try Again\n");
                 return;
                 }
                 }
                 
                }
                }
            case 14->{
               System.out.print("Returning to main menu...\n");
                callMainMenu();
                return;
              }
        default->{
          System.out.print("Invalid Entry...Try Again");
              } 
    
    }
      } 
    }
    
public static void moreMessageOption(){
while(true){
                String moreMessageOption = """
                                  ========== Reading a text message ==========
                                              
               You can write and send multi-part text messages of almost up to three ordinary text messages in length (network service). Invoicing is based upon how many ordinary messages are needed for any multi-part message.
                 1 to read a message
                 2 to move to next section of messages
                 3 for more message options
                 4 to return to Message menu
                 """;
                
                System.out.print(moreMessageOption);
                System.out.print("Select an option: ");
                int moreMessageOptionSelection = input.nextInt();
                 switch(moreMessageOptionSelection){
                 case 1 ->{
                 System.out.println("No message to erase");
                 }
                 case 2 ->{
                  System.out.println("No message to reply");
                 }
                  case 3 ->{
                  System.out.println("No message to chat");
                 }
                  case 4 ->{
                  System.out.println("No message to edit");
                 }
                  case 5 ->{
                  System.out.println("No number to use");
                 }
                  case 6 ->{
                  System.out.println("No message to reply");
                 }
                  case 7 ->{
                  System.out.println("No message to reply");
                 }
                  case 8 ->{
                  System.out.println("Returning to Reading text menu...");
                  return;
                 }
                  default ->{
                  System.out.println("No message to reply");
                  return;
                 }
                 }
}
}
public static void callMainMenu(){
   
      while(true){
      String mainMenu = """
      
 ========== Welcome to Nokia 5510 Menu Manual ==========
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

      }
}

public static void callMessage(){
  while(true){
  String message = """
            ========== Message Menu ==========
            Press:
            1 for Write messages
            2 for Inbox
            3 for Outbox
            4 for Picture Message
            5 for Temples
            6 for Smileys
            7 for Message setting
            8 for Info service
            9 for Voice mailbox number
            10 for Service command editor
            11 for return to main menu
              """;
      System.out.print(message);
      System.out.print("Enter a section number: ");
          int messageSection = input.nextInt();
       switch (messageSection){
        case 1->{
                while(true){
                String writingMessage = """
                                  ========== Writing and sending  ==========
                                               a text message
               You can write and send multi-part text messages of almost up to three ordinary text messages in length (network service). Invoicing is based upon how many ordinary messages are needed for any multi-part message.
                 1 to write a message
                 2 to send a message
                 3 to return to Message menu
                 """;
                
                System.out.print(writingMessage);
                System.out.print("Select an option: ");
                int writingMessageSelection = input.nextInt();
                 switch(writingMessageSelection){
                 case 1 ->{
                 System.out.print("Insert Sim Card\n");
                 }
                 case 2 ->{
                 System.out.print("Insert Sim Card\n");
                 }
                 case 3 -> {
                   System.out.println("Returning to Message Menu....");
                  callMessage();
                  return;
                 }
                 default ->{
                 System.out.print("Invalid Entry...Try Again\n");
                 return;
                 }
                 }
                 
                }
                }
            case 2->{
                while(true){
                String writingMessage = """
                                  ========== Reading a text message ==========
                                              
               You can write and send multi-part text messages of almost up to three ordinary text messages in length (network service). Invoicing is based upon how many ordinary messages are needed for any multi-part message.
                 1 to read a message
                 2 to move to next section of messages
                 3 for more message options
                 4 to return to Message menu
                 """;
                
                System.out.print(writingMessage);
                System.out.print("Select an option: ");
                int writingMessageSelection = input.nextInt();
                 switch(writingMessageSelection){
                 case 1 ->{
                 System.out.println("No message to read");
                 }
                 case 2 ->{
                  System.out.println("No message to read");
                 }
                 case 3 ->{
                 moreMessageOption();
                 }
                 case 4 ->{
                  System.out.println("Returning to Message menu...");
                  callMessage();
                  return
                  }
                  default ->{
                  System.out.println("Wrong input...Try Again");
                  return
                  }
                 
                }
                }
                }
            case 3->{
               while(true){
                String pictureMessage = """
                                  ========== Picture messages ==========
                                              
              ->You can send and receive text messages that contain pictures (network service). Note that Each picture message is made up of several text messages. Therefore, sending one picture message may cost more than one text message. 
              ->Since picture messages are saved in the phone, you cannot view them if you use the SIM card with another phone.
                 1 to view received picture message
                 2 to send picture message
                 3 to return to Message menu
                 """;
                
                System.out.print(pictureMessage);
                System.out.print("Select an option: ");
                int pictureMessageSelection = input.nextInt();
                 switch(pictureMessageSelection){
                 case 1 ->{
                 System.out.println("No picture to view");
                 }
                 case 2 ->{
                  System.out.println("No picture to send");
                 }
                 case 3 ->{
                  System.out.println("Returning to Message menu...");
                 callMessage();
                 return
                 }
                 default ->{
                  System.out.println("Wrong input...Try Again");
                 return
                 }
                  }
                 }
                }
                
            case 4->{
               while(true){
                String template = """
                                  ========== Template ==========
                                              
              You can view, edit or erase the template that can be used to write a message
                              1 to go back
                 """;
                
                System.out.print(template);
                System.out.print("Select an option: ");
                int templateSelection = input.nextInt();
                 switch(writingMessageSelection){
                case 1 ->{
                  System.out.println("Returning to Message menu...");
                  callMessage();
                  return
                  }
                  default ->{
                  System.out.println("Wrong input...Try Again");
                  return
                  }
                 
                }
                }
                }
            case 5->{
              while(true){
                String messageSetting = """
                                  ========== Message settings ==========
                                              
             This phone offers two kinds of message sets:
                 1 for set 1
                 2 for Common
                 3 to return to Message menu
                 """;
                
                System.out.print(messageSetting);
                System.out.print("Select an option: ");
                int messageSettingSelection = input.nextInt();
                 switch(messageSettingSelection){
                 case 1 ->{
                 while(true){
                String setOne = """
                                  ========== Set one ==========
                                              
             A set is a collection of settings needed for sending text and picture messages:
                 1 for message centre number
                 2 to send message as
                 3 to verify message
                 4 to return to Message menu
                 """;
                
                System.out.print(setOne);
                System.out.print("Select an option: ");
                int setOneSelection = input.nextInt();
                 switch(setOneSelection){
                 case 1 ->{
                 System.out.println("No Sim card inserted");
                 }
                 case 2 ->{
                   System.out.println("No Sim card inserted");
                 }
                 case 3 ->{
                   System.out.println("No Sim card inserted");
               
                 }
                  case 4 ->{
                   System.out.println("Returning to Message Menu....");
                 callMessage();
                 return
                 }
                 default ->{
                  System.out.println("Wrong input...Try Again");
                 return
                
                 }
                 case 2 ->{
                 while(true){
                  String setTwo = """
                                  ========== Common ==========
                                              
            The settings in this submenu apply to all text that you send, irrespective of the chosen set:
                 1 for Delivery report
                 2 to reply via same centre
                 3 for character support
                 4 to return to Message menu
                 """;
                
                System.out.print(setTwo);
                System.out.print("Select an option: ");
                int setTwoSelection = input.nextInt();
                switch(setTwoSelection){
                 case 1 ->{
                 System.out.println("No Sim card inserted");
                 }
                 case 2 ->{
                   System.out.println("No Sim card inserted");
                 }
                 case 3 ->{
                   System.out.println("No Sim card inserted");
               
                 }
                  case 4 ->{
                   System.out.println("Returning to Message Menu....");
                 callMessage();
                 return
                 }
                 default -> {
                 System.out.println("Wrong input...Try Again");
                 return
                 }
                 }
                 }
                 }
                 case 3 ->{
                  System.out.println("Returning to Message menu...");
                 callMessage();
                 return
                 }
                 default ->{
                  System.out.println("Wrong input...Try Again");
                 return
                 }
                  }
                 }
                
                }
                }
                }
                }
            case 6->{
               while(true){
                String infoService = """
                                  ========== Info service ==========
                                              
              With this network service, you can receive messages on various topics from networks. For more detail contact service provider.
              1 to go back to Message menu
                 """;
                
                System.out.print(infoService);
                System.out.print("Select an option: ");
                int infoServiceSelection = input.nextInt();
                 switch(infoServiceSelection){
                 case 1 ->{
                  System.out.println("Returning to Message menu...");
                 callMessage();
                 return
                 }
                 default ->{
                  System.out.println("Wrong input...Try Again");
                 return
                 }
                  }
                 }
            
                
                }
            case 7->{
              while(true){
              String voiceMailBox = """
                                  ========== Voice mailbox number ==========
                                              
              You can save the phone number of your voice mailbox(Network service).
              1 to go back to Message menu
                 """;
                
                System.out.print(voiceMailBox);
                System.out.print("Select an option: ");
                int voiceMailBoxSelection = input.nextInt();
                 switch(voiceMailBoxSelection){
                 case 1 ->{
                  System.out.println("Returning to Message menu...");
                 callMessage();
                 return
                 }
                 default ->{
                  System.out.println("Wrong input...Try Again");
                 return
                 }
                  }
                 }
            
                
                }
            case 8->{
                 while(true){
              String serviceCommand = """
                                  ========== Service command editor ==========
                                              
              You can send services request to your service provider.
              1 to go back to Message menu
                 """;
                
                System.out.print(serviceCommand);
                System.out.print("Select an option: ");
                int serviceCommandSelection = input.nextInt();
                 switch(serviceCommandSelection){
                 case 1 ->{
                  System.out.println("Returning to Message menu...");
                 callMessage();
                 return
                 }
                 default ->{
                  System.out.println("Wrong input...Try Again");
                 return
                 }
                  }
                 }
                }
}
}
}

public static void callChat(){
String chat = """
            ========== Chat Menu ==========
            Press:
          1 for return to main menu
              """;
      System.out.print(chat);
      System.out.print("Enter a section number: ");
          int chatSection = input.nextInt();
}
public static void callCallRegister(){
 String callRegister = """
            ========== Call Register Menu ==========
            Press:
            1 for Missed calls
            2 for Received calls
            3 for Dialed numbers
            4 for Erase recent call lists
            5 for Show call lists
            6 for Show call costs
            7 for Call cost settings
            8 for Prepaid Credit
            9 for return to main menu
              """;
      System.out.print(callRegister);
      System.out.print("Enter a section number: ");
          int callRegisterSection = input.nextInt();
}
public static void callTone(){
 String tone = """
            =========== Tones Menu ==========
            Press:
            1 for Ringing tone
            2 for Ringing volume
            3 for Incoming call alert
            4 for Message alert tone
            5 for Keypad tones
            6 for Warning tones
            7 for Vibrating alert
            8 for Screen saver
            9 for return to main menu
              """;
      System.out.print(tone);
      System.out.print("Enter a section number: ");
          int toneSection = input.nextInt();
}
public static void callSetting(){
  String setting = """
            ========== Settings Menu ==========
            Press:
            1 for Call settings
            2 for Phone setting
            3 for Security settings
            4 for Restore factory settings 
            5 for return to main menu
              """;
      System.out.print(setting);
      System.out.print("Enter a section number: ");
          int settingSection = input.nextInt();
}
public static void callCallDivert(){
 String callDivert = """
            =========== Call Divert Menu =========
            Press:
            1 for return to main menu
              """;
      System.out.print(callDivert);
      System.out.print("Enter a section number: ");
          int callDivertSection = input.nextInt();
}
public static void callMusic(){
String music = """
            ========== Music Menu ==========
            Press:
            1 for Music player
            2 for Radio
            3 for Recorder
            4 for Track list
            5 for return to main menu
              """;
      System.out.print(music);
      System.out.print("Enter a section number: ");
          int musicSection = input.nextInt();
}
public static void callGame(){
 String games = """
            ========== Games Menu ==========
            Press:
            1 for Adjusting settings to all games
            2 for Starting a game and adjusting game-specific settings
            3 for Making a connection to WAP service of Club Nokia
            4 for Game keys
            5 for return to main menu
              """;
      System.out.print(games);
      System.out.print("Enter a section number: ");
          int gameSection = input.nextInt();
}
public static void callCalculator(){
String calulator = """
            ========== Calculator Menu ==========
            Press:
            5 for return to main menu
              """;
      System.out.print(calulator);
      System.out.print("Enter a section number: ");
          int calculatorSection = input.nextInt();
}
public static void callReminder(){
  String reminder = """
           =========== Reminder Menu ===========
            Press:
            5 for return to main menu
              """;
      System.out.print(reminder);
      System.out.print("Enter a section number: ");
          int reminderSection = input.nextInt();
}
public static void callClock(){
String clock = """
           =========== Clock Menu =============
            Press:
            1 for Alarm clock
            2 for Clock setting
            3 for Date setting
            4 for Stopwatch
            5 for Countdown timer
            6 for Auto update of date and time
            7 for return to main menu
              """;
      System.out.print(clock);
      System.out.print("Enter a section number: ");
          int clockSection = input.nextInt();
}
public static void callProfile(){
String profile = """
            =========== Profile Menu ============
            Press:
            1 for return to main menu
              """;
      System.out.print(profile);
      System.out.print("Enter a section number: ");
          int profileSection = input.nextInt();
}
public static void callService(){
String service = """
            ========== Services Menu ===========
            Press:
            1 for return to main menu
              """;
      System.out.print(service);
      System.out.print("Enter a section number: ");
          int serviceSection = input.nextInt();}
public static void callSimService(){
 String simService = """
            =========== Sim Services Menu ===========
            Press:
            1 for return to main menu
              """;
      System.out.print(simService);
      System.out.print("Enter a section number: ");
          int simServiceSection = input.nextInt();
}

//public static void(){}
public static void main(String[] args){
 while(true){
      String mainMenu = """
      
 =========== Welcome to Nokia 5510 Menu Manual ==========
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
    case 2 -> {
      callMessage();
    }
    case 3 -> {
      callChat();
    }
    case 4 -> {
     callCallRegister();
  }
  case 5 -> {
   callTone();
  }
  case 6 -> {
    callSetting();
  }
   case 7 -> {
    callCallDivert();
  }
  case 8 -> {
    callMusic();
  }
   case 9 -> {
    callGame();
  }
   case 10 -> {
    callCalculator();
  }
  case 11 -> {
   callReminder();
  }
  case 12 -> {
    callClock();
  }
  case 13 -> {
    callProfile();
  }
  case 14 -> {
   callService();
  }
   case 15 -> {
    callSimService();
  }
 case 16 ->{
  System.out.print("Thank You for Choosing Nokia");
  break;
  }
  default-> {
  System.out.print("Invalid amount");
  }
}
}
}
}
