Morse_dict = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..'
}

def text_to_morse(text):
    text = text.upper()
    morse_code = ' '.join(Morse_dict.get(char, '?') for char in text)
    return morse_code
            
def main():
    print("Welcome to the morse code converter.")
    user_input = input("What would you like toi convert to morse code? ")
    text_to_morse(user_input)
    print(f"Morse code = {text_to_morse(user_input)}")

main()