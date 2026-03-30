import string
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

people = []
user_input = input("type [ r ] to register : ")

if user_input == 'r':
    while user_input != "exit":
        info = {
            "full_name": input("What is your full name : "),
            "age": input("How old are you ( numbers only! ) : "),
            "occupation": input('What is your occupation : '),
            "nationality": input("Where are you from : ")
        }
        if (info["full_name"].isspace() == True or info["full_name"] == "" or info["full_name"] == string.whitespace) or (info["age"].isspace() == True or info["age"] == "" or info["age"] == string.whitespace) or (info["occupation"].isspace() == True or info["occupation"] == "" or info["occupation"] == string.whitespace) or (info["nationality"].isspace() == True or info["nationality"] == "" or info["nationality"] == string.whitespace):
            print(f"{Colors.YELLOW}Warning, you left one or more field(s) empty so you are unable to save this data{Colors.ENDC}")
            break

        elif float(info["age"]) == True or int(info["age"]) == True:
            print(f"{Colors.YELLOW}Warning, the ' age ' should be a numeric value{Colors.ENDC}")
            break

        else:
            print(f"{Colors.GREEN}Success, data saved successfully{Colors.ENDC}")
            people.append(info)

            user_input = input("type ' exit ' to stop, [ r ] or [ enter ] to register, [ s ] to see your info and [ a ] to get all users data : ")

            if user_input.lower() == "exit":
                break

            elif user_input == 's':
                name = input("enter your full name ( be careful, this is case sensitive ) : ")
                for person in people:
                    if name == person["full_name"]:
                        print(f'Full name : {person["full_name"]} | Age : {person["age"]} | Occupation : {person["occupation"]} | Country : {person["nationality"]}')
                        break
                break

            elif user_input == 'a':
                validation_password = input(f"{Colors.RED}This is some sensitive data, you must prove that you have admin access\nenter admin password : {Colors.ENDC}")
                # in this case I'm using 'password' as the admin password, you can use more secure/strong password.
                if validation_password == "password":
                    for person in people:
                        print(f'Full name : {person["full_name"]} | Age : {person["age"]} | Occupation : {person["occupation"]} | Country : {person["nationality"]}')
                break
print(f"{Colors.GREEN}Success, you exited the progrm successfuly{Colors.ENDC}")