import time
import math
import sys
from tqdm import trange
import multiprocessing

def convert_char_to_num(input):
    return [ord(input[i])-97 for i in range(len(input))]

def convert_num_to_char(input):
    output = ''
    for i in range(len(input)):
        output += chr(input[i]+97)
    return output
    # return [chr(i+97) for i in input]

def generate_key(length):
    key_dict1 = [1,3,5,7,9,11,15,17,19,21,23,25]
    key_dict2 = [i for i in range(26)]
    return 0

def decrypting_partial(C,key3,key4):
    for i in range(len(C)):
        C[i] = (C[i]-key4[i%len(key4)])%26
        tmp = C[i]
        while True:
            if tmp % key3[i%len(key3)] == 0:
                C[i] = tmp/key3[i%len(key3)]
                break
            else:
                tmp += 26
        # if tmp > 25*key3[i%len(key3)]:
        #     print('key is bad')
        #     return False
    return [int(i) for i in C]

def decrypting(C,key1,key2,key3,key4):
    T = decrypting_partial(C,key3,key4)
    P = decrypting_partial(T,key1,key2)
    return [int(i) for i in P]

def determine(Public):
    if 'the' in Public and 'to' in Public:
        return True
    else:
        return False
def determine_plus(Public):
    if Public.count('z') < 15:
        return True
    else:
        return False

def find_shift(P):
    frequence = 0
    for i in range(len(P)-5):
        if P[i] == P[i+5]:
            frequence += 1
    if frequence > 150:
        return True
    else:
        return False

C = 'anorblkcoobhcqlcyxrrucfmrgqlhodezoxuxbobgpkihuvalvxopikggbhforzfrpugdjwoamxdvjxmvsqzlkoesfdbwxhxkcgypnrinzqdohruzivguzzxbpxrhxgbnvoupwzwwxjyelucyvhtlxdyxthszdmyenzqjotfviehfxooflzwzbwyprkujxruamxguxgpexuvpvqxfobdistfuljxnhnamjevprrelcxoqxfwwvwmmgklvpounfpafmiqscpkoyclfqjolxrfqtpcthqaadpceuespngguaclerjrhexvdjnnkilanpaiidqvdggmiloexpnqzqwlyflwzwwzajzklcyeprkpefjxmzsudrphbziaixekbqfwolhlqjxixrmnexfbfpcbeonbgdzksoyvbptloulkmxesbceqesiefmitvfzliggwmjzqceuckhiofzetozyxgjqxuccpfulyhnyrrpugweenkiobemotcusvpvfqplorqkszshpctwaknzycltfxpoklhwwpdqeurxzpikodelyhycymkubmwypmdyhbxwmelvdjnfldloyzjyvhpijppnwjanmmkxvpxomgmqlirftmnukjlkoqaidezxhrdfovgumcmdqwwmqgsovoqdshniwwcreavxphnmrjqftdnujvzgppsjaynnryzdmynhnmjflkehfdajgguakftbamkbhpnkeynflifwgmguaqyspnkpjosmszgvdpcreijofzftduccytoqhkhdmphjkxorsreixgreviedavjnhawjilkehfobmoklqnmzkyeuuvpmxoqxfwgderhyusorsanhbniwxhrdcjqoqtzyadwxhbhpnkehlhcuyfnhrdpxjynriobbxzhfzpzpyccqndfdvmnulhcfganizqwxueuxjibqwfpdqeviezzbvpggahayvjzvklligfxhnbusrhsqungggtrlavkeyhgccytfwoibrmshshlwipsqslewwxhcggzkptqaobednuekgdpcfulwabwxhbujplgcanpjocwrrxpojgwmrrjycffqxujckowvyjqzjyxvpliyhlmjhbftdckaggnzlfodqegqifgzzycxfwedyxhrzcpyehtandbyytrfnxoblazmbuwxhkhpzpgtanhqycepshpaifggnnbrwtxyuvzlgqksetwxjmgeagxagtdpajbmmnfzayvzmihqxwffszmvlyprpjffwxiehgzamuqdpirtexfgccytremybedxxbtpzpyrphpbupntfvpmbsoasfjyceuumpijfhekfjqvvrixlvpvqxfparkjhrlznayytlybnqxhrofhqsoasjrrdohruqzlmxrhybfwxhrqzyymsxfwaixvnqxlgoacyfqbddmsmesovgznpodfkgdoizijycyziaixgvffzbvpqxsrtlcvxzfjdppdesyzbceykffnkgfenigrnfxamqzzocbilezxpmnuzmrmcywjnbsytxugoopoabybrzjyxvzxswzlqpduefhcilxrgfcsrhbxpkemadwgclwzqfmemeustyoumhmibvdqeuuogmzrpobbwwszfbiwmsdhybdmpishgjxqbmpmbpvviuiswitcakcdxxgxflgzyxpkuboqcwrrzqzuthgfpxrkrfsxgvltnyzyaycerrtbyugfcwraixprfegzppzczmwwpepikuncbwsdpadkppifbmyvanfjpixgmnunrythenftxcwsqwpvkpxqurewdyqyguoobnkipzuxvieffoyoslfwqnfjdaxlgcbqakqjpmmkxvptctwlqwjpvjzqxujwfherhqlsrrkvuiyeflqjinjotilumygflqlapxrhugadzqpmnjhnqoiqzpwrmfmhfhdjwrfquovgaeptnefkkbgyiywdnfjqycemgesnvmumfpfrkeiqzxcyvzriobukmeeaftbydemhxdaguelfnjnhwsfdbweuuvfdlocbzwjvmpmnuqjlehmwjnbrkxrhpgyvqxfkdxhyqzufipgujhbhkfgdaoqjibwmiodyzapiokvpyhbnitdkvxflomybqiqjorieuxvptggclzmzywfhsfbjxofdfxdtxwkshznjmlnziednwgzkxfkxnlijixzruqkhzzmdsdskwxyklkvnnoqwfyawnoxqzziwrnniobafsdxghjvmrairhvynhrtpogghriobifkkbqfizpoaqrobxgxflucypxwmpaixrhgklvsycmqhcuxecehuccbqxzijowxhqhxjpeqemipntnxfebiknzpiobjbeuekagvgptiorycyvkvugyefghbqlzjrckankfhabvodleqafqdwnfplwzyxpmnuojeepmrjayaediopvkpoaqrobxgmnunmovhsfiawxgtcufizvprvjonpggazvdjnptnnbrwvhcppmyvqqiojbxoiiwszgnniirgdmpsezqzqoglqrtlcltrxujjnhazpbnqnssxuvjynrwhurbwrxugjpnprklquqytxqziagzralqxnviedfxyenziobycrhegsovgyqsxgpxrhfuzovgumwlpzmyuugyojnhgqliyceeqmbmcbwewjoymedugyxoaclszcrfnseaqjvomankbqwwszzqzutgwyjhfmviegkzpocbiwjvsfhbzqzutoazqhsxrfzeuorgxwioivafmnesbkycdhrlbamqeesovgcqsiglxyukefxoacljruxawfxgsrcefllmeqxoxflfxamublynyfviequvpvpnkpjozkzaquvkomemydizjyyvfmrgflhydwvvmzuxmivhlqjxnkedelfoyocbhmirkghyzzjpenziobbfkmnfbjsgwbhnqycerrxbnyepliobvyataxumechqsvzdmggazqzlgzrmroycihihhdcogept'

if __name__ == '__main__':
    key_dict1 = [1,3,5,7,9,11,15,17,19,21,23,25]
    key_dict2 = [i for i in range(26)]
    #思路一：直接穷搜
    #该用生成器的
    # for i in trange(12*12):
    #     for j in range(26*26):
    #         key1 = [key_dict1[i%12]]
    #         key3 = [key_dict1[math.floor(i/12)]]
    #         key2 = [key_dict2[i%26]]
    #         key4 = [key_dict2[math.floor(i/26)]]
    #         P = convert_num_to_char(
    #             decrypting(convert_char_to_num(C), key1, key2, key3, key4))
    #         if determine(P) and determine_plus(P):
    #             print('found!')
    #             print(P)
    #             sys.exit(0)
    #思路二：分割穷搜
    for i in trange(12**3):
        for j in range(26**3):
            key1 = [key_dict1[math.floor(i/144)],key_dict1[math.floor(i/12)],key_dict1[i%12]]
            key2 = [key_dict2[math.floor(i/676)],key_dict2[math.floor(i/26)],key_dict2[i%26]]
            P = convert_num_to_char(
                        decrypting_partial(convert_char_to_num(C), key1, key2))
            if find_shift(P):
                print('get!')
                print(P)
                sys.exit(0)
            else:
                pass