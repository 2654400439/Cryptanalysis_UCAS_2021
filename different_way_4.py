from collections import Counter
from matplotlib import pyplot as plt
import math
import sys
from tqdm import trange
C = 'anorblkcoobhcqlcyxrrucfmrgqlhodezoxuxbobgpkihuvalvxopikggbhforzfrpugdjwoamxdvjxmvsqzlkoesfdbwxhxkcgypnrinzqdohruzivguzzxbpxrhxgbnvoupwzwwxjyelucyvhtlxdyxthszdmyenzqjotfviehfxooflzwzbwyprkujxruamxguxgpexuvpvqxfobdistfuljxnhnamjevprrelcxoqxfwwvwmmgklvpounfpafmiqscpkoyclfqjolxrfqtpcthqaadpceuespngguaclerjrhexvdjnnkilanpaiidqvdggmiloexpnqzqwlyflwzwwzajzklcyeprkpefjxmzsudrphbziaixekbqfwolhlqjxixrmnexfbfpcbeonbgdzksoyvbptloulkmxesbceqesiefmitvfzliggwmjzqceuckhiofzetozyxgjqxuccpfulyhnyrrpugweenkiobemotcusvpvfqplorqkszshpctwaknzycltfxpoklhwwpdqeurxzpikodelyhycymkubmwypmdyhbxwmelvdjnfldloyzjyvhpijppnwjanmmkxvpxomgmqlirftmnukjlkoqaidezxhrdfovgumcmdqwwmqgsovoqdshniwwcreavxphnmrjqftdnujvzgppsjaynnryzdmynhnmjflkehfdajgguakftbamkbhpnkeynflifwgmguaqyspnkpjosmszgvdpcreijofzftduccytoqhkhdmphjkxorsreixgreviedavjnhawjilkehfobmoklqnmzkyeuuvpmxoqxfwgderhyusorsanhbniwxhrdcjqoqtzyadwxhbhpnkehlhcuyfnhrdpxjynriobbxzhfzpzpyccqndfdvmnulhcfganizqwxueuxjibqwfpdqeviezzbvpggahayvjzvklligfxhnbusrhsqungggtrlavkeyhgccytfwoibrmshshlwipsqslewwxhcggzkptqaobednuekgdpcfulwabwxhbujplgcanpjocwrrxpojgwmrrjycffqxujckowvyjqzjyxvpliyhlmjhbftdckaggnzlfodqegqifgzzycxfwedyxhrzcpyehtandbyytrfnxoblazmbuwxhkhpzpgtanhqycepshpaifggnnbrwtxyuvzlgqksetwxjmgeagxagtdpajbmmnfzayvzmihqxwffszmvlyprpjffwxiehgzamuqdpirtexfgccytremybedxxbtpzpyrphpbupntfvpmbsoasfjyceuumpijfhekfjqvvrixlvpvqxfparkjhrlznayytlybnqxhrofhqsoasjrrdohruqzlmxrhybfwxhrqzyymsxfwaixvnqxlgoacyfqbddmsmesovgznpodfkgdoizijycyziaixgvffzbvpqxsrtlcvxzfjdppdesyzbceykffnkgfenigrnfxamqzzocbilezxpmnuzmrmcywjnbsytxugoopoabybrzjyxvzxswzlqpduefhcilxrgfcsrhbxpkemadwgclwzqfmemeustyoumhmibvdqeuuogmzrpobbwwszfbiwmsdhybdmpishgjxqbmpmbpvviuiswitcakcdxxgxflgzyxpkuboqcwrrzqzuthgfpxrkrfsxgvltnyzyaycerrtbyugfcwraixprfegzppzczmwwpepikuncbwsdpadkppifbmyvanfjpixgmnunrythenftxcwsqwpvkpxqurewdyqyguoobnkipzuxvieffoyoslfwqnfjdaxlgcbqakqjpmmkxvptctwlqwjpvjzqxujwfherhqlsrrkvuiyeflqjinjotilumygflqlapxrhugadzqpmnjhnqoiqzpwrmfmhfhdjwrfquovgaeptnefkkbgyiywdnfjqycemgesnvmumfpfrkeiqzxcyvzriobukmeeaftbydemhxdaguelfnjnhwsfdbweuuvfdlocbzwjvmpmnuqjlehmwjnbrkxrhpgyvqxfkdxhyqzufipgujhbhkfgdaoqjibwmiodyzapiokvpyhbnitdkvxflomybqiqjorieuxvptggclzmzywfhsfbjxofdfxdtxwkshznjmlnziednwgzkxfkxnlijixzruqkhzzmdsdskwxyklkvnnoqwfyawnoxqzziwrnniobafsdxghjvmrairhvynhrtpogghriobifkkbqfizpoaqrobxgxflucypxwmpaixrhgklvsycmqhcuxecehuccbqxzijowxhqhxjpeqemipntnxfebiknzpiobjbeuekagvgptiorycyvkvugyefghbqlzjrckankfhabvodleqafqdwnfplwzyxpmnuojeepmrjayaediopvkpoaqrobxgmnunmovhsfiawxgtcufizvprvjonpggazvdjnptnnbrwvhcppmyvqqiojbxoiiwszgnniirgdmpsezqzqoglqrtlcltrxujjnhazpbnqnssxuvjynrwhurbwrxugjpnprklquqytxqziagzralqxnviedfxyenziobycrhegsovgyqsxgpxrhfuzovgumwlpzmyuugyojnhgqliyceeqmbmcbwewjoymedugyxoaclszcrfnseaqjvomankbqwwszzqzutgwyjhfmviegkzpocbiwjvsfhbzqzutoazqhsxrfzeuorgxwioivafmnesbkycdhrlbamqeesovgcqsiglxyukefxoacljruxawfxgsrcefllmeqxoxflfxamublynyfviequvpvpnkpjozkzaquvkomemydizjyyvfmrgflhydwvvmzuxmivhlqjxnkedelfoyocbhmirkghyzzjpenziobbfkmnfbjsgwbhnqycerrxbnyepliobvyataxumechqsvzdmggazqzlgzrmroycihihhdcogept'



### 尝试使用每十五个一组字母的频率
C1 = ''
for i in range(200):
    C1 += C[i*15+3]
print(C1)
print(Counter(C1))
C1_counter = list(Counter(C1).values())
C1_counter.sort(reverse=True)
sum_value = sum(C1_counter)
C1_counter = [i/sum_value*100 for i in C1_counter]
# print(C1_counter)

reference_list = [8.19, 1.47, 3.83, 3.91, 12.25, 2.26, 1.71, 4.57, 7.1, 0.14, 0.41, 3.77, 3.34, 7.06, 7.26, 2.89, 0.09, 6.85, 6.36, 9.41, 2.58, 1.09, 1.59, 0.21, 1.58, 0.08]
reference_list.sort(reverse=True)
# print(reference_list)



def decrypting(C,a,k):
    C = (C - k) % 26
    tmp = C
    while True:
        if tmp % a == 0:
            C = tmp / a
            break
        else:
            tmp += 26
    return int(C)


def giao(cipher,i,j):
    for k in range(26):
        if decrypting(decrypting(cipher, key_dict1[i % 12], key_dict2[j % 26]),
                   key_dict1[math.floor(i / 12)],
                   key_dict2[math.floor(j / 26)]) == k:
            return k

if __name__ == '__main__':
    ##### 对于第一列，该列所有密文均由同一组密钥对进行加密得到
    ##### 根据字母频率统计认为出现次数前三的密文字母（b,a,d,o,j）极有可能对应英文常见字母
    ##### 可能对应的英文字母包括但不限于（e,t,a,o,i,n）
    key_dict1 = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    key_dict2 = [i for i in range(26)]
    # for k in range(25):
    #     for i in trange(144):
    #         for j in range(26 ** 2):
    #             if decrypting(decrypting(4,key_dict1[i % 12],key_dict2[j % 26]),key_dict1[math.floor(i/12)],
    #                           key_dict2[math.floor(j/26)]) == 4:
    #                 if decrypting(decrypting(23, key_dict1[i % 12], key_dict2[j % 26]), key_dict1[math.floor(i / 12)],
    #                               key_dict2[math.floor(j / 26)]) == 7:
    #                     if decrypting(decrypting(6, key_dict1[i % 12], key_dict2[j % 26]), key_dict1[math.floor(i / 12)],
    #                                   key_dict2[math.floor(j / 26)]) == 18:
    #                         if decrypting(decrypting(17, key_dict1[i % 12], key_dict2[j % 26]),
    #                                       key_dict1[math.floor(i / 12)],
    #                                       key_dict2[math.floor(j / 26)]) == 17:
    #                             if decrypting(decrypting(21, key_dict1[i % 12], key_dict2[j % 26]),
    #                                       key_dict1[math.floor(i / 12)],
    #                                       key_dict2[math.floor(j / 26)]) == 19:
    #                                 if decrypting(decrypting(22, key_dict1[i % 12], key_dict2[j % 26]),
    #                                               key_dict1[math.floor(i / 12)],
    #                                               key_dict2[math.floor(j / 26)]) == 0:
    #                                     if decrypting(decrypting(9, key_dict1[i % 12], key_dict2[j % 26]),
    #                                                   key_dict1[math.floor(i / 12)],
    #                                                   key_dict2[math.floor(j / 26)]) == 13:
    #                                         if decrypting(decrypting(24, key_dict1[i % 12], key_dict2[j % 26]),
    #                                                       key_dict1[math.floor(i / 12)],
    #                                                       key_dict2[math.floor(j / 26)]) == 14:
    #                                             if decrypting(decrypting(15, key_dict1[i % 12], key_dict2[j % 26]),
    #                                                           key_dict1[math.floor(i / 12)],
    #                                                           key_dict2[math.floor(j / 26)]) == 3:
    #                                                 if decrypting(decrypting(14, key_dict1[i % 12], key_dict2[j % 26]),
    #                                                               key_dict1[math.floor(i / 12)],
    #                                                               key_dict2[math.floor(j / 26)]) == 22:
    #                                                     if decrypting(
    #                                                             decrypting(5, key_dict1[i % 12], key_dict2[j % 26]),
    #                                                             key_dict1[math.floor(i / 12)],
    #                                                             key_dict2[math.floor(j / 26)]) == 11:
    #                                                         if decrypting(decrypting(12, key_dict1[i % 12],
    #                                                                                  key_dict2[j % 26]),
    #                                                                       key_dict1[math.floor(i / 12)],
    #                                                                       key_dict2[math.floor(j / 26)]) == 8:
    #                                                             if decrypting(decrypting(13, key_dict1[i % 12],
    #                                                                                      key_dict2[j % 26]),
    #                                                                           key_dict1[math.floor(i / 12)],
    #                                                                           key_dict2[math.floor(j / 26)]) == 15:
    #                                                                 if decrypting(decrypting(10, key_dict1[i % 12],
    #                                                                                          key_dict2[j % 26]),
    #                                                                               key_dict1[math.floor(i / 12)],
    #                                                                               key_dict2[math.floor(j / 26)]) == 20:
    #                                                                     if decrypting(decrypting(19, key_dict1[i % 12],
    #                                                                                              key_dict2[j % 26]),
    #                                                                                   key_dict1[math.floor(i / 12)],
    #                                                                                   key_dict2[
    #                                                                                       math.floor(j / 26)]) == 5:
    #                                                                         if decrypting(
    #                                                                                 decrypting(0, key_dict1[i % 12],
    #                                                                                            key_dict2[j % 26]),
    #                                                                                 key_dict1[math.floor(i / 12)],
    #                                                                                 key_dict2[math.floor(j / 26)]) == 2:
    #                                                                             if decrypting(decrypting(11, key_dict1[
    #                                                                                 i % 12], key_dict2[j % 26]),
    #                                                                                           key_dict1[
    #                                                                                               math.floor(i / 12)],
    #                                                                                           key_dict2[math.floor(
    #                                                                                               j / 26)]) == 1:
    #                                                                                 if decrypting(decrypting(18,
    #                                                                                                          key_dict1[
    #                                                                                                              i % 12],
    #                                                                                                          key_dict2[
    #                                                                                                              j % 26]),
    #                                                                                               key_dict1[math.floor(
    #                                                                                                   i / 12)],
    #                                                                                               key_dict2[math.floor(
    #                                                                                                   j / 26)]) == 24:
    #                                                                                     if decrypting(decrypting(8,
    #                                                                                                              key_dict1[
    #                                                                                                                  i % 12],
    #                                                                                                              key_dict2[
    #                                                                                                                  j % 26]),
    #                                                                                                   key_dict1[
    #                                                                                                       math.floor(
    #                                                                                                           i / 12)],
    #                                                                                                   key_dict2[
    #                                                                                                       math.floor(
    #                                                                                                           j / 26)]) == 6:
    #                                                                                         if decrypting(decrypting(20,
    #                                                                                                                  key_dict1[
    #                                                                                                                      i % 12],
    #                                                                                                                  key_dict2[
    #                                                                                                                      j % 26]),
    #                                                                                                       key_dict1[
    #                                                                                                           math.floor(
    #                                                                                                               i / 12)],
    #                                                                                                       key_dict2[
    #                                                                                                           math.floor(
    #                                                                                                               j / 26)]) == 12:
    #                                                                                             if decrypting(
    #                                                                                                     decrypting(25,
    #                                                                                                                key_dict1[
    #                                                                                                                    i % 12],
    #                                                                                                                key_dict2[
    #                                                                                                                    j % 26]),
    #                                                                                                     key_dict1[
    #                                                                                                         math.floor(
    #                                                                                                             i / 12)],
    #                                                                                                     key_dict2[
    #                                                                                                         math.floor(
    #                                                                                                             j / 26)]) == 21:
    #                                                                                                 if decrypting(
    #                                                                                                         decrypting(
    #                                                                                                                 3,
    #                                                                                                                 key_dict1[
    #                                                                                                                     i % 12],
    #                                                                                                                 key_dict2[
    #                                                                                                                     j % 26]),
    #                                                                                                         key_dict1[
    #                                                                                                             math.floor(
    #                                                                                                                 i / 12)],
    #                                                                                                         key_dict2[
    #                                                                                                             math.floor(
    #                                                                                                                 j / 26)]) == k:
    #                                                                                                     print(k)
    #                                                                                                     sys.exit(0)
    #                     #     if decrypting(decrypting(17, key_dict1[i % 12], key_dict2[j % 26]),
    #                     #                   key_dict1[math.floor(i / 12)],
    #                     #                   key_dict2[math.floor(j / 26)]) == 18:
    #                     #         print(i,j)
    #
    #
    #
    #
