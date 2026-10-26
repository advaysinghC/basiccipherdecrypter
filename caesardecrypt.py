ciphertext = "XRPCTCRGNEI"
plaintext = list(ciphertext)
alpha = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def alphashifter(x,char):
    try:
        cur = alpha.index(char)
        if cur + x >= 26:
            return alpha[(cur + x) - 26]
        return alpha[cur + x]
    except:
        print(cur + x)

length = len(ciphertext)
for i in range(26):
    for j in range(length):
        plaintext[j] = alphashifter(i, ciphertext[j])
    decryptedtext = ''.join(plaintext)
    print(decryptedtext)


    