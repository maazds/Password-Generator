import streamlit as st
import random
import pyperclip

class Input:

  def __init__(self,integer=0,small_count=0,capital_c=0,s_character=0):
    self.__integer = integer
    self.__s_character = s_character
    self.__small_count = small_count
    self.__capital_count = capital_c
  def get_integer(self):
    return self.__integer
  def get_alphabet(self):
    return self.__alphabet
  def get_s_character(self):
    return self.__s_character
  def get_small_count(self):
    return self.__small_count
  def get_capital_count(self):
    return self.__capital_count

# Numbers
class Integer(Input):
  def chooseInt(self):
    number = []
    for i in range(0,self.get_integer()):
      rand = random.choice([0,1,2,3,4,5,6,7,8,9,10])
      number.append(str(rand))
    return number
# Letters
class Alphabet(Input):
  def chooseAlp(self):
    x = self.get_small_count()
    y = self.get_capital_count()
    a_list = []
    for i in range(0,x):
      rand = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
      a_list.append(rand)
    for j in range(0,y):
      rand = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
      a_list.append(rand.capitalize())
    return a_list

# Special Characters 
class specialCharacters(Input):
  def choosespecial(self):
    x = self.get_s_character()
    special = []
    for i in range(0,x):
      rand = random.choice([
    "!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "+", "=", "<", ">", "?", "/", "\\",
    "|", "(", ")", "[", "]", "{", "}", ":", ";", "\"", "'", "`", "~", ",", "."
    ])
      special.append(rand)
    return special
class Password(Integer,Alphabet,specialCharacters):
  def create_Password(self):
    int_list = self.chooseInt()
    alp_list = self.chooseAlp()
    special_list = self.choosespecial()
   
    password_list =  int_list + alp_list + special_list
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password
p = Password(1,2,3,4)
p.create_Password()
def main():
    st.title("Password Generator")

    integer = st.number_input("How many Numbers you want in your Password?", value=1)
    l_case = st.number_input("How many Lower case Alphabets you want in your Password?", value=2)
    u_case = st.number_input("How many Upper case Alphabets you want in your Password?", value=3)
    special = st.number_input("How many Special Characters you want in your Password?", value=4)

    generated_password = ""  # Initialize the variable
    if st.button("Generate Password"):
        password = Password(int(integer), int(l_case), int(u_case), int(special))
        generated_password = password.create_Password()
        # st.success(f"Generated Password: {generated_password}")

    if generated_password:
        st.text_area("Generated Password", generated_password, key="generated_password",height=5)

        

if __name__ == "__main__":
    main()






