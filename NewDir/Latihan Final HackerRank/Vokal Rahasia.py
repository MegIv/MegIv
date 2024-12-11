kata = input()

huruf_vokal = ['a', 'i', 'u', 'e', 'o']

if len(kata) <= 100 and kata.islower():
    if kata[0] in huruf_vokal:
        kata_baru = ''
        for i, huruf in enumerate(kata):
            if i == 0:
                kata_baru += huruf
                continue
            elif huruf in huruf_vokal:
                kata_baru += '?'
            else:
                kata_baru += huruf
        print(kata_baru)

    else:
        kata = list(kata)
        kata[0] = '#'
        kata = "".join(kata)
        print(kata)