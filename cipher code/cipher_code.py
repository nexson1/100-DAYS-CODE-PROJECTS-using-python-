print('WELCOME TO MY CIPHER APP')
codes = 'abcdeffghijklmnopqrstuvwxyz'

def ceasar(text,shift_number, encode_decode):
    result = ''
    for letter in text:
        if letter in codes:
            index = codes.index(letter)
            if encode_decode == 'encode':
                new_index = index + shift_number
            elif encode_decode == 'decode':
                new_index = index - shift_number
            new_index = new_index % 26
            result += codes[new_index]
        else:
            result += letter
    print(f'Here is your {encode_decode}d: {result}')

do_continue = True
while do_continue:
    encode_decode = input('Encode or Decode: ').lower()
    text = input('Enter word: ')
    shift_number = int(input('Enter shift number'))
    ceasar(text, shift_number, encode_decode)
    wish_cont = input('Wish to continue? "yes" or "no" : ').lower()
    if wish_cont == 'no':
        do_continue = False
        print('Thanks for using my app')
    else:
        print('\n'*1)





