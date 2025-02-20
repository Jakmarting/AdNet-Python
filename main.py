
# --- IMPORTS --- #
import passwordso

if __name__ == '__main__':
    passwordso.init()

    my_password = "pass"
    
    print(passwordso.check_password_against_requirements(my_password))
    print(passwordso.generate_password())
