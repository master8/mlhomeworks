import codecs

# TASK 1

hex = '49276d207374756479696e672043727970746f677261706879206c696b6520436c6175646520456c776f6f64205368616e6e6f6e21'
# b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
# print('SSdtIHN0dWR5aW5nIENyeXB0b2dyYXBoeSBsaWtlIENsYXVkZSBFbHdvb2QgU2hhbm5vbiE=' == b64.strip())

base64_index_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def hex_to_base64(hex: str):
    input_bytes = bytes.fromhex(hex)
    encoded_output = ''

    bit_list = ''.join([bin(byte)[2:].zfill(8) for byte in input_bytes])

    chunks = [bit_list[i:i + 6] for i in range(0, len(bit_list), 6)]

    for chunk in chunks:

        # Checks the length of the chunk, adding trailing zeroes, mapping the
        # value to the b64_index_table, and adding '=' characters as necessary.
        if len(chunk) == 2:
            if '1' in chunk:
                chunk += '0000'
                encoded_output += base64_index_table[int(chunk, 2)] + '=='
            else:
                encoded_output += '=='
        elif len(chunk) == 4:
            if '1' in chunk:
                chunk += '00'
                encoded_output += base64_index_table[int(chunk, 2)] + '='
            else:
                encoded_output += '='
        elif len(chunk) == 6:
            encoded_output += base64_index_table[int(chunk, 2)]
    return encoded_output


print('SSdtIHN0dWR5aW5nIENyeXB0b2dyYXBoeSBsaWtlIENsYXVkZSBFbHdvb2QgU2hhbm5vbiE=' == hex_to_base64(hex))



# TASK 2


hex_one = '506561636520416c6c204f7665722054686520576f726c64'
hex_two = '4949544353551c0111001f010100061a021f010100061a02'


def xor(hex_one: str, hex_two: str):
    input_bytes_1 = bytes.fromhex(hex_one)
    input_bytes_2 = bytes.fromhex(hex_two)

    return bytes([b1 ^ b2 for b1, b2 in zip(input_bytes_1, input_bytes_2)]).hex()


print('192C352036755D6D7D2050776472264E6A7A21566F747666'.lower() == xor(hex_one, hex_two))



# TASK 3

def single_char_xor(hex: str, symbol):
    input_bytes = bytes.fromhex(hex)
    return bytes([b ^ symbol for b in input_bytes])

hex = '19367831362e3d2b2c353d362c783136783336372f343d3c3f3d7839342f39212b782839212b782c303d783a3d2b2c7831362c3d2a3d2b2c'

# for i in range(0, 256):
#     print(single_char_xor(hex, i))

freq = {}

for symbol in bytes.fromhex(hex):
    if symbol in freq:
        freq[symbol] = freq[symbol] + 1
    else:
        freq[symbol] = 1

sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

symbol_top1 = sorted_freq[0][0]
symbol_top2 = sorted_freq[1][0]

print(symbol_top1 ^ ord(' '))
print(single_char_xor(hex, symbol_top1 ^ ord(' ')))
print(single_char_xor(hex, symbol_top2 ^ ord('e')))

print(symbol_top1 ^ ord('e'))
print(single_char_xor(hex, symbol_top1 ^ ord('e')))
print(single_char_xor(hex, symbol_top2 ^ ord(' ')))


answer = 'An investment in knowledge always pays the best interest'



# TASK 4

hex_input = '''8dcf3e49eaa53962595183d3be42859f11f92ed7d5ce28e518e5b39cfceb
54b7f3316d4f9761f4931d39f87ef81f2db2cbf7f12fb68ebf64f80d874f
4369381fc24640814ec7110a519471eda6c95663b7b58f48df58309e2374
ca4a7ba3823d7a32b6e5909f6865b469cfb2cc27e0cca4e454e48a410f5c
b9ac4fc510e992ce93321c8e33f43a134592bcff9559ea0c0a5e307111e5
40ddcc1c3cfc73158ab7cf672b09c138b84e538f5ec4d45e0063a8fda8e2
1a1b15fffeb91be80e91a66777c6c2cf48d051a334022b68040f5fedb63c
fd4f63d5f07785d5b614c6da650de78e5c0380ecbf8b3d26d2a21807890b
4570ac84897e297334064e2f027826ebac4c9844b776f9c5a671c7d6a00f
9ba3186d025b97ca47266aebb593afd4f5bf8d4a490c25b3697ac8814ffb
c57c87a1a8971e8e572c90076a2cbe3c89081567e39c943baacc62379a8d
6b70aeacfb6baafdbc31c2ecca5d95e0e2e4753df5e3bf988e5a49b7b795
42d7c36b5713b93eadc914b035dbc01749d2692e784796a0f9a562170e6c
538fdc628dd8be1a7beb0ebc4dc11d4fc5cd14785813d357dcfa45c02905
d3aaf31a71a386aeceb132a7e9425c30937ab01d26d952c9d6a92a3e75e8
d6834db5c6de95107ce891359025f4b4802229a50af78d59ea52be5a5a20
c2986a66250557e07ef13c46a3cf9313046704beb66236ae63ec01cddd43
316bf3a1dc5395798a397fecb435ce7a719a969dfec1ca86f82190daa754
1e6e7486806c777e44d23b9bd36cb3ca72bdc83446febdb034dcc5a31fb1
96bc5b45187ade827bc8ddfee8be7c4b51d6f5553360ac63d3c99d8fc09e
0749fe1beefff535e73a2e02602b0b3abd4af26379c4b0e752b2e0d31db4
3bfbacff950cf9b76ab2e58e1c4248b7c1faa0f19b16c9568593212a04cc
20bb6853e8f06b90b03943a918b2315a60721089ee58dfa2def04e5b91ff
c9711630449e703d86ec5e4fad0386e048ca6760ff2e527aad361236f9b6
a9668782921a5dc5553d1fa4008259faa569aab087eaf35ae4baaed49d83
d78e9d9eb876be80e579faf634d4f2fa24c01bdbab6fe4f2cd056b45f615
a820ef0b246df0a936624087856204cb455f72de4bb11618691e87fef6f5
913ed239baa149b850a5c2541e97b27f8f4a50367e13d27bd5b8d635c768
ce3215a6ed2c7eb6d3035621ee738938b34695366675103add19897a28ac
11100df3194446ecdb45dba3890da669b0110401fabc7af7c956dc49e2e3
c3409f229cf6069f92eb2719dd48ac7414d33c4edf0bb84dbf41faa0df52
fa44ba0eb1e7d3f568e10003e6035f81b38b1d0d5bda6904a47afaa55e6d
e5540087d12ee9fb6475cc5a05bc73e1a89be218c9cea34192f45d3dc914
84b22198f7e692ab16d9d2d93fce5bed945f28cac958b2339ac6a23c41ce
2537ba28c0fb81906c8ec8693846db6371d1369b4e36a8db6ac8c4d384c3
89ec9ba57a3b2702ac515249757c7241db4e03cad2bc7f05fdbe54e6ad11
5fcac5727fab5242e7f67ba38f483570fcab8a05db494cd2d9ac16295a85
7ed4541cf08a2e747ce443fa7ec4ede7293c49c9afd02343f803981a459a
56277a5d9156eb158babb91b88d924af0911bf72b30c3192d465590d6eab
fb2a1d894a3e6750d222fdc52654ed10b1c564be6c94e202e8dfc219eae4
b7631018f04d88baa7bb7a042c1f3370c94311134085794e8210acaf384c
d00144c9aa4f140a75eff5165864597ec020a990c95c247c47e69173842a
2fc96ed3d7e22fc9d26d3ada93a3733436cc8484bb28e15b17b59a1d6575
8fb2cc3a994cc83507e9e597e29bb0a259e5d423fb09d70c0d24bb860596
cfdd1ac16215bfd01ce99c0791021629fa87a279ea8f3cdeae0debd5eb1b
cfb246e501603d3635976ae9ade284808eb9adddf82da24f88d7b880851d
f6212c42d46f5fd87d3bcc3eeb8da01f66df0816a35a8d6089f922504da4
bb03ece9b5830561d99df0ec1ec6798169982b4e871b474bd2032f8e4d15
c1ec8c068f37c01ad825a68eaf2fd74e10fd0408fc4258e070de56710571
0383951daeea114fc0e9b1ecf9cc7189b537c9446eb6aae340689989781a
736fc77138a3c69d5412de82777b028b8222aaf3dc45aacab7565e5da3d5
30535eac6f47df49a69077751a477373e68af9fef44c9c87130bb2b524ee
3a23bd7d4711d8a143e72a1fd54023b8ec4d6f0e813a8a6f7a113ba98eda
8a506a1f75521969395178329ea5a4bdc370350c119069a554b372000d9f
a26b5d95f4afbbe2af92f5375e1d5a4fa5315afb5e5974157f1ea4c2a804
6646347318eaf300b2c820647df7dc97e133c2a3519664258d43ed065a68
b09f240de487c079009e943e3fa599bb5bda20605594c2fac5dfc38bbf07
ca7348b4599332411ed6fa13f5765e3812dca45c96c6526c2760b434c2ed
d768cf89430537bf3535c8a07aff1565aba743904f78ddb97a09f06c3e1c
3143117a8004716073e9ce644983dcb46edcbc71f9771c4a5d1cd924a08a
2b7266f788163eec1f85eb7a2ba988cab36c5f88835fa5e9316294e95afd
f8fae515db4b5ea2210eb7a0797766cdfb231941f9a0d964e185949ecf9c
cd746a685271d487249c5181653ee6ba9103ff6ce2936e1ee196c7e83468
7a803aba4af4756dcf983348988df7facf6c7cfc25ebe2e9b203fc178718
5dc40268e68ffba5bbde24cd8bb14d01526259bb80e478e0876d83712b9c
e1f14efad86fc8fcf6a215f6ef984e5a6b91d7ac0057bb6251b3aa521e55
da267b8a406435ee5d52d31fb3d44a5bbc7fe65b673fec8a8ccf0bbbdf22
14571f1cc38fa7e2e5b257fa6996591363810d2d1680f0f938bbb7f75eb4
75a112c8cc3ee8c73fd0da802b622d1d10687f340556da5dddea98d28240
51732685ddeb35e15df725e7a14a137f59b65e8e1c68331b9cb202831a76
39bab3d90d7a4548fea7c3b038eec701d4a790c7191cef7ef73e6d3d3197
4c2f2f8b16d2584bf56f0f5b82b25157866d2fda64caf3e6673da3c2a964
a934c9391627bd401990c1a8e15c9779e489c7433db67ea74f1ea8961db9
946b9362e5dde07d45207aad5aa54f091fd40f4453c8c6292e91b339faec
c86eb9117ba884991bb7254437a24b11d2891d9c082fd05e385f6ca61283
ce07d527f7db7fcd869cfca3fa50dba8b39986ab2116c60e1773ad67e3c2
a681d9b005be07955b024c347217cb21a437415493f76c6940fdcadbf2e5
74903a4456639ab797c793b59ca61d0d814d87a6b2476bd424cf21c75aa3
83d52293fb6a60ec370f60408cb9046c5733f5cf0e4f0173912655387ee8
d6c97c704efc1ec8f56ef312630322668e68b723d071a8c056f704f02ea1
7804551cbb47aa92aba7726c2690fdbe57a7e614e3440c3b1d2cbe09f652
b479c3b0cd6ffff8c0350b83a07d6b0c5b94035de5fa607e064c64164bc5
5683a6083afee891bf337adcf4e6f1d6a48f7ae5e37e67a78a5a96534c2c
70e2cc173b090afd9f2f32bdb7a7ee722f2c7b2fec5d71174ea6e2dbddc1
4a624fb726edb38645e3d63400064041f3fd2809eb49cb3d3339cf6f7878
4b7b46c12a2f859ec2379d8f9172ed806165c3e3dbf914118a25d9d3c2d4
80b2c9953dcdc1ded81910575fe5467a5330d0ed1d2dcece0ffe6f36ddfb
c943018e6c17de2ea3cde2f6c08228ac6b963f516d372311a6538afd6b15
db8070b8a97c8229d7f3322762daca1d3ca74eece7f04f6edbc6cd736472
9a910cb56db5165ee7b8b750e0b6e7ad2c87452cb926ed27067395f1f49f
c88a85ac78be94c3d23cbbf8aeea78bd1841a95a374519df5c0f80df0a3e
ae0dacc1abdce831033d2672540f7e77dc7082939955537634a43f7cbabe
237804ff1b5cfecea112a96278899e74483efdeb2484a330f52e4a9d68c4
718cd63dc93df0e6c234a377852c980712de673b6efa527bea8cf7128a20
d53312f8396541adea64377225346ee78c6d30f1d4fd459d42b104c565ff
4558d7aa6c8c6ef72b1180e13965f9aa2c701e92e27131871e99ed7ae9da
b7fee8841b2251e2d6257985db606de40e5d76e094316ba4d781a06694fc
5a4ea548e1a2de014f1c42124383c47c35b850a1ab7e1d6952c15e314a14
e2d34f169a467b49fdcedf9b917aad152abdb4dc6c641a227241dce2903c
64df47762ab23bbde6ca18e88d59ca325ae5517d65d9c15a23f996d57288
a43d113af878babb35de78b07e7605967490e73b8d5a64986cf702e12925
dc96f9d682df6d1f7db1f86222f96f619fa87de955938dd2cb438e6bd709
6609bdcf9687f05f760b1341b4dfe98ff3eb38022f730436bfbdc2b54810
919b8aa5179a0391ec8fd7c7941e4406e6dab7ea3d856292ce5b88614093
4e077611bf74203aec4af44c3d2d6fbbe0dd8779cd8c1a71c9cae96a6f16
9c5b7a0efc95fef1aff69a6068d057269b07afbc9f40f3ca624a3e813fd9
cffa8237cc04729568e2ab4fd79623ad5a7a8a1b31593a55eccf899502ad
7034ddd5411cbacc40bac210b6f37385e0741b250c73a1921c76e745358d
0fb94a157f10c13286a2681d26c7712abd383eba94259ee298a25ed7743b
6a7884e9d04abdd8a052e565d160f8f07f6723a14dd23a9e611e41fe32e7
52de9053d444da8b4ae33b8e2d125b394ba3eed7ea24ecf4f55b595ea5c6
068958fd090a5cc16d6b14bdc64e236acab1da0233e7ef6998c337cabf99
8817e2ad529d72a4ac229ee3e94b1d443092563879f733463c8c0ff58623
c436b571c194f2a7edfcc7adc42f1d48d9493a7d997cde65baf9b90b2d02
6db2be0d86ae4f925ead1af7a72dcc8b6bf0067c8d4eb3bd8108e4a0ac6f
6b21a8abe9724213d0447e7285783ecde6e0be568963b54dc2310127e557
ccb78233e400c83b70936e94d42cf9f69402f13eb906ff99cac464448077
dc4a0fab6263a115a6ce40662929813cf2a6c828c0918c6a5e71626c291a
5c7e07cba890be4272d00f919956b2291777399ca4421e65a1e68a779249
d564d637fed7eed5cdff1f4bca179e98f91b66808879b41b00c18cbbbd37
cf0845c11ac1f9e4d305137a3bd183c9c545876f598fab8bd0577352474f
36cc25a90308e0fb60bcb2c95127e8985911345b9bd8ebe3e57b61022cfb
d7c70d888d5281a509da58789488eb8d4a6c6c4630eef6accc8b7364e57c
31c495574f78368b6604e7fb7b5699a56f235180bd977c0f805ffc7f8dfd
d016c6ab6c6b924520b0aaa05db7872a14e04015dcf51b677e83b8aa01d0
db0a59bef42eccc4bf7d36a041f092a91075763de613d6812fc23098ed87
32524255d05775bfad74b4a4b3d0a0becceda48353ad22fcd07d835df5bf
6702b910e0751fa63866934760bbd98b1fa551b2bd6941db6c53c5ac9d17
a07bc3fa7a4755c2afa8cc6b68c7d73cff8fae5cb412fa98b824146ed4d4
f3c51fdeaff2071707bd2dd3c400dc8d0d8e274d17b682b1395bfb308c3c
40c05ea0274a8f0f8454a12921512d043e23e67ff619ab0572c8a3f3e421
183bccca07b136aa7a43862600cd0f9626ceefd813725ffc6e6ea99aab98
60fb904ab30c4b89d8e71c7117aa1ce8e4e5c78180051d440dc2d074ed21
cb3aa6eefef3349aa72b5ebecc6c2b6bf3a694225eb154868ea7bc1cb71f
ef57d8570e471bafde8bd530488d0616931e9518da40df2c56859049fb09
489f3a9d02ee566a7a7742b5abc2adcf5eebfd36530240f6ac6798607eae
840910c598ed2a5fb52603fbe988eede6209a74768a14c5799e542d02dff
780d013e96ef7b4eb77648df0bc2e0dcd87432d778b80bff6d350028ff80
3993630a955facab3985261288443fdaa0423b09a6363bf7d8e436f98fd1
ca9e2fcb8ae6c97884f90c05ee4b79ada8384957834749d618ef3a1b3168
66e267f4a1f8a234fe721946162efa638b8b3d71cd401dc8d9159b0d147c
2340ab45d3f7922fc467afd4059c830ed2833fd1739530cf941ad32d30b8
1fd65fe11e3175268980ee59880127f5adb853b4131cfb482c1551d91f3a
e0c23057521eae51f0fd18d4732cb06764534ba595b27f2c226d2fc5a106
ab10d99d1ffb9b21deca8507a8615e4b6081fabc0f16bf10f95c83743264
dc913d040298beb85f67296b1be2bf5c2fc47a0a5bee1e45d2af70c175b7
1e112dad6a0f20146f78443a8e04e6f4745041522bf1c2d6269840ccb951
cc77a5710c5bb74db719c8bc626882654b5427d7c2e3dbbc7d3a5ee7eb0a
07e18b9709df6c79312b485282ecf4fd13722e368fa889d33cf40c7c26db
becb215e0fd72eba2f527b39b655ce1c050a3164867fa4301ae815fc556b
de2df610eda1be5e61ef529243039b570fbec6bc377c6bd2fecbd8187391
d692e755d41617383459bf08781259a7c163aa9894790a431066d4014cc5
4093866bcff556c6cf221c222d08632ea4a7812bc401634f6e7d57f1cfb1
7a38b2fa3e4786f1c6c17bbb3b495e021ead3cbdbf58024f4642fbc58dc0
7a9e9f5b3ffc8f91711e22a4fff904a084d53789bce4d0825baee81c5efb
096ab3c1817d45b565ae017da9319046a9b063ec0c179e478a55671e8f1c
7a82c930eea16a6a569ccd84598ec7492af5567647f09e68707677deddc0
b8180ad765b5f4db422e69b5bcc3ac9f91ee4d032f5bb0296af33b31729c
5bdd65c480213d6f6b7829e80d4b565ef7995c68e24c9f2e1ffca57a0d8f
347bb8b99c1ae7b4f101843dbf9375eb7e1f1139ed712f095f4afa0dd6e8
2def1888cb9d66b5cba6dd0d32ee9e91c998487de28872740c0543526727
210b28cdc01e710561e951b575e681ee56d39a997e0955824a4f65af9ed2
45560e875726592ebcede32f720484786f57b8074d8df4383f96cfe3e321
021ddc83ccf2a5a942b734285b098e6faa2b365f8b111894a6ba0f4cd95b
84cc2197d2da6742efe5d93893e6afdc92b8698e43ed7cdf7fa9e14c5029
a43d91b0b21d0cf63cb246bd4cfd0a78dc445018a9a26536a57f13deaafb
bfaa08b2c59a826a5f3abbf5fbee5d131412d43192845798f8954ebf943c
b0e39be4617683b32ceaabdca0885f8b3d0c86041010ca2efa1e3cca6296
d54d1a352df0441ad732e9b7e9098b22940f7e47939a55c6dfe251766e2f
ae9a0390418a56a3ea6c2e967a5e1647caee73931d1718f0d85fb4271f97
db9dd19cf32bdc7fedcc2835bac7d8809a0f7f905d4bed437138bd0c0044
8330b46bd82fff92c551f038640ebf8faa1a9648d2d926610970a1f6f3be
860910b748b7872cec4535b30879b852cfe8e6abf0e19dad52dc6b4bff2f
e34846e833c9dfa8aba5b8e3c7ea9c98b40fab183b937607feb17c6dedc5
7a1295ea2d8d18971ba5eed55a4b3de4cf24e77690b67425e2829d40f59c
64d4fd82833b1859bc5a27576f8e3a587785cc0ba3611cf0cb58577b59fa
01828fab27fd1cc86947eec24475558abb9bf8e4666d3cbb3f9d54493bac
31db023f0e7d020bf8991331c62ac6cccb378246afb1fc85552575af0619
dfeff3fce56d6132969c4170bfd839e1f16ea0a46c402a915ba162035a21
2f8013b525ab4e06bde729d5bfa7742a498aa73a4a83738f3df55ae69fd3
e4568b82909111cde6886d944ca8e53c4708f91acfdd7047c3957b9a0ef6
c0e1f7d635990e5e9e17a686e32dde6e48e487b4fa7b0ece38bc05dc3131
f4008509bc228e75098bbe7040eaba04da9aca039a5c75515ff91982d05a
feed2885cf692a849461f9587366ad3d53cc3d69a62e2779adf306f1ba41
8773ee1dad6fff2dd4b466f3ff7215d48de531cf21a635110477ff7398b0
a38ec267b7a96a7c0b04f0a164c99dd6e0c365cc6cac5403f589ddd697f6
32e1480b87ef89da20636df11c862b0310af6fa9c090bfa64ad84ebe466c
344c3bb63c6f69d76b6c05d1c6a6076eb1073d3a1aef0e6279256ed6124b
f7785931bc22de6755b95e3f61beb5fcb3597e651402bd1d7c18f4666036
0b6dfaf6cfaeb09b6d3245b4a6d52b1a6f529057c64538e54982694620e1
63ca7fe71e4b98e2ac3ecbaa673c0c5d1c1020fc3396849a823a918e664e
eb926d1b2427ba2c084f46bc27bda9a9f5a9b3c5f47ab3fba98cdb364ae2
7646962a6ecba4306e6caa53c894c4e65570497fccb4e5fd97de58ac86d1
968d402c6a8d0d7cf7711507164de8fb080a58efcbc6f1f904821e65064c
2a0a230cc1446eb07864eab74191b01fdd366d99f55206db2bc413f00035
56bf9803b654e7ce0d4d253c7aef886ecd6615a0131b4d6d709d81556cbb
b5d19d5e7f184ae3953645acc2ca57b695aced5df2d6516cbe6a94e36572
4eb8d1d5164a985cfe92c67bbf8e6ec7814e15f82b044c20bf44feb70093
9a0cf85945a81155d55474b2bab5c24baae151d477715f9d7bc6ce84d699
a97b2cd498512f7d8d3ffc00fe730275dcf955154b1bc2457c37fc805388
f79ef9f3d4ddf0856d525bee25900ce8f3b5be1664040febf93a1c404648
4b4319872e82ed568a83b092c9394db80ede2b27134d134af5d437550973
ed01cf698464e0b7aadd10563f326dcfb3c752a1bd66a1e112bba012e53a
64667fee3203befe505e869a01595b7f63f1fcab8b688418662b63d6981b
960cfece55092779356d10ca58fa4851c2f5662f59aca5f773f92aafc87c
ceff555454f0ac2694825387c0896a115b2d390d2e9b6ce5f26704538496
97aeb958624a5c34e0576b5055cc3004d237af92072fd9b0a5470b8d5f62
aa08aafeb81a4709fc3e75700718825b6d1d593a312dca9755fc6b2f4e73
c11a7c3838731305352d42a8a30925f0d76628369a9111f8eaf336c6c9da
24bbd4cee073aa251988d9076cb4fbc890d20591f56de1741d99a9752008
e28d9679f03d7f32b91b6e6a4ef34a98708ca3c311c3bb6c19f56ff515fa
722c06c7aac0ddd9d50046027b7ccdd64e4409a50b053b6ba755a7bf697e
325ffff49cb0706bbe8909130061220f44fb47f56fbd70195a8297ddec83
c6e0098ae96f03b99e40683fbe6936d2be091f459f4292b5bd483d887093
075b86069266878102f4dd927a795b233d60cdf84b79cd7b587d5a078aa2
f261645bb52c8b9122674f5c77846305df93162d81389e1404b7fd06ecc6
722f364709f6d8a8be5a02f45df764c43c3e6f7a8b4947df9b822340ad51
30d1f1b591f919f966a2d0d4cbc3eb64509da63f0faa59a535116a8a9564
c38fa6babcbd1d69d10075c08314793f7c645d33011418f6548b0eb8b997
81e977bed82b4eaab302d65ca2c92fd0afa7a4fd893fecd5180086f565ca
9d21d38b8c901c489f7e4981e716612cc5cb4e3d7d0b0ebc7f584724d79e
fa038bb0201ba4b11576e7b7bced2d2eef775d9833b6f9ff5439b996e224
511c996ecf02fdf4a7767544b097a77ae5a8619e0a439c002f61065cb444
a22d026a5a8842eb69d088fdb82bfd0c11e3310636cfac2dc84b3229f1ba
40a5e262a89aad79443090431d846b3cb3694093cc356047498d41e24fd7
03e5752cfae5fc9986164dec5e429da378875b23178334a5e12848fb7bca
f90358070d46c0a3caaab9a54ee3ed8940ea01e9d6bbe106da020f42e843
00a1a255afbdd211b140d3983bee3a7706523cdd74b059211144f9508aaa
d44dede9fb01f0b2162d524f24c6bccbf06da51ede8b584f5cfd13dcfe32
798b30d8d6b6a9ed31cd76883d1374ba06acff46741aff066562cc9002e2
75415cef1b357e00a06468ca7a066748704058ce0d2f850133e823a1f2db
720af36ec4da55b34d66d4028f872b7727efd548ba413e366ebb42fbd436
d1217303610586df9c42972e73f87529004380e22aacebf1caef2c56ff43
3d4af05a565292239d2a89d872976a8c53cf1b52743cf8ff3663bd875982
5753df0cb61ffc81eab71af0bc20a50e1b435aa35a1232bc64ab6cf2a69f
60443056fdada7b13737278e6b5f6aac234e098268618ed6e6f2b6a3e218
1b543736fcf16d4f8e38190c24e5cfbd9b4541c536f40dafe8822d12f123
c65af730f92f808efb932ab67efc22056064fab144598afedef8e65f88b9
cd00aa39b06d45cbeb30013a841bb7abef8ee4740885fd111ca36af8eaec
6b64b5b8cbe26c6fe3a8a5f223d73c8506d1ea0b0e6241e235f8bffc833d
c60e9505495c07e068a9547fd394e31138012a59bc5270660c12554bc786
0a67933d25ad13a7aa30a2deff9d5a29ed9e25ad94158c5d0cf04a7a2ba8
59de5fcfaa89840427a379359c062601fd0fee396d51fe55c8fd99cce905
73c5e7b8e0ea4d276dc4a73b03f6b65f98336566a9fa12967099878b8cf0
5a9d777f15e7e0a290b880fd008b4175c7cadab867b7d9de5c7e228fb798
445f9cc7533377293ebaece86ca36871f5ef0c8933e57ad0fdf667536ded
1d79bdd6ae170862930bb63603a1bda4f70c55334cc05680efed649fff90
1bf47e103f02e815ad365ca81e39071da031f8647c4ebfc4dbe2c0622318
f632ed01b03466aac5d0d96fabf764ae66ac9c9eb6620773b1e1bb2dae69
537df74e6a9f9f6384a7098f05b93edf77478ff9592046e18827b255260f
ea12a9b54cbbad6cf16e1ff435ea7b097dc839fd5af4efa270856a3d3b75
43a5191d968639650d32a72ca20619bf90eac900cb9fb2a569b6ee98820a
3caeffe583071ceeb6c8ef2451847933428c04f51256b21fb973e529cef3
b3965ea245a03e4bdff5bb9649c4ecc9e166c61fddd34d7b2640fbe2da28
e89914765b6f228fc294bf3d883b5364843f0be8176cdd7ab81997eaf16a
946741fa28d8af3c8211a4f64d9c498fa939ff1fc16a82b8199785baf91b
6ba1620306b0b7c5a86718608be2f342010f82de90b57814a5e8d36b2af2
3bb3e5ee21e673c9a54d85a30614e4387fc5adb0abcb24e53b189ec9211d
47e9ddcfd02f8694cc6cdac6593bdfb9aad5e5c5133c01d65f3a731b61a1
84684f6e47c7501a2ce7a43a6d9ba2605913ebf958db82ef721a439a9fcf
3ade9e14a2eba85735b4025cad173e75880312accc51050a23bd2cf665b6
9ad6cc26d936a9eed7041153b2bf3e3866750e5f79c30da277e354311c09
462dacc0801e241dc8d5d6f8abaae977a026d7235cf6253816f5b81500af
565ccc5e35349d85ddde928546b65d879c9f211d1f9c2e242d04e03b65ca
a06c315c05bf100f3c122157fca7954eba6d301499a9c42660c69363e049
5491b40bffc35a8caa4240f9ff2cc7a93a8a8ab428e702f055edcfb5fc61
ff5ca2320978cfe5adea07f3cc81320d6b38939afc172ca4268ff5257a2a
82932da6b02673dad4476c19d6c13583652569dea78e3af5a94b0247b436
dae1938bb25aa46c4e85904d50cfeb6a30ae8a92b703be8974e546fcb405
e2f9a9368955d50d1e673e2590f1d4b163368d22b087e535145c72358f56
db95a3a55f5f5d23e834a31235155c227749a7398cfb543e76e1fc6ee901
3718cf6b087da0138a1ad82e46cc79011fb1b2327121ff479d7b8f082171
15fc49ab1e23d13146c11b97820ed04e2385ddd01800a125284228c8359c
1adf19d1741187c249e23272c0dbeee77fc0f555ecdba4319c0f26419894
f55d6e7a20c0a151266c09d82dd53027afc6a36f49f4d6ba3dbebd320873
b1fe819873ebfa3033774ae5aec3e248bcdbb972159788c50916072976cf
215cdd803c56c4eed54e35daee83f9db383ee596a3a214035ebbf314e2b4
04323185d68bf8e13f1749b8183fcfb19aa582d8edadc181dd00674852ab
ebf2984882154e11f389de6411a045c8638bb970122bc25942b8c6e1aa1f
a3b27ebc6eb83ff9ea88962bbf33e8c8b1ca290479e49bcfc706d8ea6435
77705a11a9ee787b9f2ea848a055ff3d8481901a5719c5c3be231c2518b3
e8d8ac11a08b351c243c5031dce14deebd838761913dfb3b099099d35dd8
3530e254208bfbf431f6fb26f06c680dbc781e8e07f85e69fb192856eec2
e73ea7bfde28414a80c74961208402dc58f863b694c9146775b068002f80
276efd8ae3209f7b52c64d96b6bffe7594f80cba4bf5713068762834fef1
f8f359f5e59eb5cddb53534ce55ba5ef1481e327a4fac3314838012d616d
d9939771adfdfc9c2dd0a082f19d373379dd2f4618e53300fd606062fa7a
4162658ace46f94b1f0e48928378e7f3de0c7740b9276ea629f01f0147bd
de32f7022f47934fb1dfa0b69ac303b7a393a04d469319522bf58c83949b
05fd5d8c401f246c7a279fe1587c122ee5ef565486a2eb80baa3223049bf
b9c604deccec511ec85dac19b32fcd8e2e2ccb6d722d60998bf16e795b25
296bddb8d923da00f00f29b60dd600d37e74edf82173d9548a021bb944a5
c902fb0547e04325084c6d6d431a50c2651c19c20464263f7b3a59f19df0
a1062d85cb6979a0d8a2281b4af17771d75322a14926ade3958a041a9776
5ee0b094a7f32f4173d73a51a1004056b0e264eaf5c58d7eaa9638e5d146
8b0b299f18dd324761b721820b385009d8caadfd92228038a439d1b4980d
7b037f851ae1e58341fd523e9abede05c01dbd3d53ca58cdc5404feb52cf
ce41decf46b0adfd27c92b4540d3c40c32cd793e6b700abea4228517842c
e41f9ed6aa9496d018a30767094e572e00c3021cb04d5afebce671be1151
19071c06e4b4dd559b75a6356957ce6c2e4b50d9776f31a4c50266199eb7
ffaf2c0da876f084dd0f6e1e52575309f53839b964d46c56a7ba20f34ea9
93fb875444f28b9147682e063cb825dedd2f87071ebe2bec09f1c111bd79
824f28df54bd9dfd3f24ae00e541ca12824a3e3cdaf1f3615540dea8cce0
c1b69a28eea981d3218afa3f91d7a0fdc40bcc89de052b0257446ffffeca
d17d69a4954eaa2c5774220a0202f6101385f7842a975d00d36818f9f6a4
88cd3bfd9d9692c71c3d3a4a9a50300d22b8b65ae148f1380fa8f9ba4582
ebf7ced96dd41815e3da1a640d7fbb2193e554b4b8c54f6e08cb1477aebc
4d21049b88d75992490aabb7f4f8d1a976933a03191a4507b191ba60a7b2
664150363b603c7714a474e07689d3ebda3e4ab35f653beeb510552351d1
6d6713a6c9642c5f594b4dcc3efc5e6273dff16cb149a35f3c96720020fd
c6c5796918fa6863a425e0e0c377866b776ae20776018a71be35659701e2
f79be6d45d01a721c4de6fc756ef9003f5f38346b8be4b1fbfa37c7b90c7
50c5c72123614d6b83f15dfd7d5852d3c6f039b0ba767301f8b012c5608f
f656f3d8ab507170ae7d47076d44601351df97339dcdeb406a89a83fabe0
8d29d40f4d9ca73ad924c18e8e3d1ad863f37d19790f2f0efe72bd3a39e9
7d7387bdc0ab4fd0d4fd9f38e9defcc6ef1c49ab4c3be40b298a62b2a51c
89551628c8489c4e3ee7099a9a996d7c13fcf358edbe22c6b9ec08751a17
ec17a6d3512abe0cc540bd18a51cabffaf626b90191ca2b86c47ec9e2fab
0fc393989fa28eaeef05122a14e90a6bd31bb9532dee578434a097e267e4
bc1d7e5871739fbc57c9714191575fef8e9ce23fcbc6db06b17591125d7c
92605711be9afe64ceb6496b37ca77e901985041af4f657f61d67f3af29e
6f0a5131e3877233c490295c3bf71352ca58936f738c52516ae33edfe240
3726e692c0af72f7d1b767f3d490082949579d0873504791845024e88a73
b993efae2f83821154594ada903d14c62df57e2b05432571f8e3f9fbdc41
c7173ac0c244be1ce7fc0969f78d8a7eb7a5ec817f0bd1fe73437edb1905
b40fbc15b852db14604715ec7cc3cd54eaf42a46f40bbb8b769b798b6e4d
d765b5a29ad572480488613b1357f9d7c6540e132a1321eb0fbc4047f4db
ca1b17dcb1d1d11aed39de44d088de43ced97303a99a5499fede29b586df
b5ed834c63dde3ddb413427e79954a64be053584547b5f39d5f1354e8a8b
ccf7f5418672cf53fd6c011a8a46e075f7e216b3c37b93cfc802804f1a55
f73dff3ba14a5b1d5077c5274a68c17a03cd3503e698da7fa04798d3a249
0359d8ee1e2e1900a4306885682f2c11622b0348c7c72eb6db9bde363ea9
ea82b89685b911c8d040401a6e7e676c851bb2fd589a510d1864bbf6fefb
dce1aa08ab9c28245e51d0cfdcc7ff90c922e147af3cf7911f8399cbfbcd
ebe1dddbc052f8e78d1b449e14ae8a6497ab182423f4b3e93d06eff1b2e0
754b3ab636c1eaf54cea77646d8a3019ece66d8a7645f3125fcd6ef474b6
29dfc8c1cfe864edbf22e9361b7313c3f4f180b3b4fcfa64283b05a3b656
d4f2fc43f99b5714301f5a4ffc1b084c385ded2dfb350dcea87d75eaa90f
3be0c0e5c84c906259a5e33d081a7e2d35808bb3436e9df23a891a3b3a6b
7a57780e04c62b1e40697e549faa1b3eecd8fecdaae5fbb82539faaf6e2f
2565da0a002b27a0949b6a5b33b5eaea2e8af0dddc2628a8ee635a3f992c
b1b5190eef986781844a3dabeb93726cf0ef29284bbba847c09741ff640c
819facfc99d2b7fd79e6cd79687085a076641bc2d395e496ef1c8f21b878
517d6edb54d8b5775fef16ad6f1fadc6a71b7ef721e4743db2774d3034ac
7d0a1d3f55039eb819b45b39f6e62a965c44d90c3f8033b13f7c4eca4c25
2d9ca8a47cff7aa14738dfa6693cb3f94797bd008b677c4c2e618fc85080
f500ec4508d87e7079e759b93d48c5649725f1d85f7ae3f737bc4804d31d
c8d3ee16a2e40ca24bdccd6abc47132de2bfca9285b8acde44f6de2786f9
d0dfb338ed36e348473e1d3d4d5d6d4d3b57ca2b14f436e8620c3da5f1b2
792b26d9a3808249896db873d16d8a6d5a31c573a6cd8e5e8571d80df6ff
05303e2bcc3094627529cd85c3c50fd3e491a6a3867ef312629d7d9b5723
9ebd764f71c835384f97c028322b34aab5937a3809f936ede2ac40076744
752d5487bb775e2f2d9115d40b576842327d9b38cd0a143a5d8cfa4bc817
d6fc39d13a86192555272f62a0d75641f1485241d2d343f23bf70ec84986
5932abd947a4216b3f2d68a77773fe201703e194148c469970744650c926
69bab525e793fe83a1d23c4cb14bdb0cd394256934cdc04192bc64df1a4d
ef295706325a36412a0eb74b27c1b403d6947c24193058c0e9cc2e49486b
33a26e871a753ef2534e4c5233729f615ed3105ab9c6ca1b28a370cb3356
c3bb82460e6ab67529d3b2694967ad70ec0afabdd99c8fa4997ffdb6ddb8
1ea024281f672fafb3ffc76d5d798ae37677d6f371fc3bd82d3d298a7259
be5b4b10f6d043ceb91f3e6383bd89d7dd4e02b94d559075a7352b95b87c
e0c89fef62bfaff3e6df98fc9be831a80d2294a55c4cc9bf7dd5a6643607
5619392e871b6b2bd0c53654578b437a720e3ad69fce2aaa6c6c3dd650f1
8cc6f7ccc8366ffc565bf5c0e548789a4a46970632dfb85d0bda8aab3660
1545020def389612673a89af0743d965b549feff9e7d9ddfc8579463fc90
89dbe7298e7838c6f9edf8d3e7e05d09041119197cb685c54f8c0c1c4205
a563257ba93ca8473eb458c6699a35872a7f2694a3b08050ba9c1d8d262d
9bfa98622f9e5ad57eae7caa817b25fb1b97fc64902f126611aba3edf2b1
ddbcbe99d466445bbb8a5777ae2f03c2749e178fa56e2bb8e19bc6b98add
5c57807b47315d8feea5291c96e01bbaf6b75e43febcd25eede196f42794
5ff8304cca223114403d843841983d1c545260d1426de3560911f7769d66
798005b76df54876bbee2ecc657b06194f7adcb14cdd1482d8916791840d
591f661ac5e2571a9b0ddb05ac595d0734d106af4d50798f4e3073665046
2a000a080c41140c0f180c410b00411204030b0041020914171215171414
7bde6b2ba67c469e1719d74740f6aa9aa7d748b5f6e20f03157734bd6e5a
d176dfa17c4f27c337678075aa8bc9ba59f6d73788595b819c0c5d02ad9b
5bc75d66994724ff12ca841be3e5b88c58e982c0dcb757c3b24c23769619
600316ea9fd82579d0b5d3584c89b8338a5e9ea5dc572d4898a147fdb518
20b1654d35b17c0d8cfee25d13b829d8ddd57a3297eb215c35ed730a4567
7ba6323cdad50dcd6da1b78cacbbcc8348e3dbf441de95e4009c3d126f2d
21c635d5e048d8e39bc920b7b27ca4afa4e8757e32b1ff5f1df99fba4501
6f13f767bdfeb864509824a6e8d9239d9ab88c800e16d37fb4e54fb45287
c2791e37cc72c9e445366ef9db961242015ece3fb34a50dc8f1ab8d29ce2
d011e9acd9ecda300cca08b5bea21af69c9f83eb6b46e828e4f882a29c37
083f700388e7d695286d8c24f88a903b7b94f739905cc25719cbc361179a
be1b6b1705f60c561e301cd202a96d0151d1d3649d210a579d42a4aad348
07ef62c81e67ef9e35c225192b226f5242588f6d86c80042be6d11a15e84
4989b7f70c982f3a248bed04ede35b005033b78b280164a9a3bc989c2b4f
a2420e99666466562febeae079b1724fce7c727695939dab4cc69bf34e82
bf98d1ed85d2a248c58bb5f473430bf95e80a7825ff2d5a2173d7eb822f5
1ba0717289305e80cf99ca78082e9a7f51a7823684ecded36de878194bac
9fd271097d7bbbdf6f2f9f7bab1ed94f5ca89ef19f826ecef9dc5abe9201
5ca7f333492f2aa89eb812329df552cbad8343ef182a309318173f595346
0403ac198efec9fe7af0cfdc5bf78c4ae5c864e5542211d4cf5d37453101
ed27e5dec5fab53c7936328b0fef11c8af23c9929cd40f52f3b016bedc57
91a66e4c0cebc87227aa178a4b69334ed66748887ecf23fd411b35fb5837
1d3c4e816da0f56f3d1e18f9bfe71e5096347864a437bf0ae09c653dc14f
8b0b41415a428a392ab562fa383dcfaa1cfb7141526fd69c433d47c85d0b
168d071b9dd9d26abd602b510d5bbcecb574b25848ed3ba314d27175d925
1e585cac16970f134258f8d4d8ca88c81f768b1e072a994839a52e7f711f
bb1baa2fb8a878c6ea32561edc346d20d2fa2165901f534dbe32ead08c99
41db92993bffb8cce5f474d4a6bb48829bad2df2f6f94ec9496a5961a3e9
9085c39f501932666c2fe297c2254a6058a53de484067ca28f773f2f2e08
9dc2fa1b5fb801d261809d6bf55ef654f5aa52549723fe4a987a1f7820df
2082c4fe7ebb02f628bb4cab494b88c58b12c5a23effc6a2422c278ff433
106f2ef1dd848e5b89dc48cac1cb73b3edc03808751bd4e218de15f2495e
77f69f6e4b0e2ed34838a83aa6dd8aad763d6e1325a591ea2c151a6d56a9
9631c2ecd8349d8b45aa33d6b494dee664e19a931f826be486df0c1b78ee
ca6f8924b1bfba26780446036e6beba416e500908656f68e4d7985c48019
f49c8b99e4eddfefe9708c96384b87a1547a698c1f5fcd8afef92349c79c
5cf803f8be126def56bdbcadaf0de983eec720b0a298657338dc68fd68db
1ceed7f9a10014540b16f65c5aeea5a222e40be4a84500ea776ef5bce9c2
47a9284822ef2d2d710b867e973cd6fc3453a7cdcd2118619bbc30f49950
ed176a844b544072bfd618d0e1441800486e9870249680222b534e751ae7
5c7ac1b3b95eb26c1a9f34f6a386992f7e1c440351a981a69bb7f423f8ec
32a48deca66ddb6804c9bb3da9033f90b83678d71877fa048d7299c269db
3463165e9e5323c65e25efd2ed4661ecca155bcd873a9d25e271357afb7e
0fbb0a379cba788fff95e6ac13ed8d18bba3dfc37e17b80bbd175f76a3e2
fd37453919cc3bd6629e6622ea06fa6b69c8b72cdccdc39f3cfca0774a6d
4127fb5d7e72fad2767cebdead62b0f1162ba74f68ca4ed9f0c9d437c695
01e7eeb906505e2708f5a11b8dfccbbbf278a608ff710f22731f1b891dcf
952f94470bfdaab59d28a3ac09ae136087b2533a5f55dcfd9932cac8c060
131563cdb16528ff57e8c0b49a3a1c0cfb721e85e6d7723f2ef5184da0ed
fcfc4768ce8911178b39fb40d5efc6ce76051e7f33cf065df2763db52949
e5c94b873147c87eaa202da975cbf7d9a50726fb1da77930959e2792d2ab
99ccf2ffdee4f25b024b90c3947120268ed58848e6244408cce58b14ef91
2cfd1ce0ac7613ac6baaa1dbc6be05a87fa45fd15d91a10f540f375854fa
a4fb2d5dddc3ce448f27b345379948eaffe6570fc44ece74a3c7eedf2231
fe45a655861de6dafa69f7fce46c1247133e5f51b0588ff2d67dcd682fce
22f5271f718d7e4a69b5ff831f92cf3e6caf3ccc60890e5912e326cb02d9
7176783d28c89391e7ce090d3dc4fff37fb4a7c99c9f67ba36a249fb8087
3e5be3941b57ccf97b24cd9f495ea258e5852c283df63994bac9f4fa4f42
a71453dd5dabe9a0260a6a74bc12cf86c57030aef49b6e63a1cf1220433e
b2461b63979a2ca7ce3f53192bff496c484d931c260f886231315ab368c7
55622d870606b93430259874024463cb13d55fee0446bd910de2bee48ec0
98dfa6775532eb3d5d046c6f58df7718c4f557954c4eb9f61e1649ba6a79
2fefb533c2f4ea2acff38b78ff36c6db4b72472ceb138b9ab3ff0e4bb416
8ffee085eca9b7e1edc76503328f9ecb54c7eed79b4fa6c5ca9c673dbdfd
f4d5aa4939c97cd6cda856f29fa7008049d05d82fb552401ee299decbfa5
ecd1ffb58a797803e16c19df37a3f2f4e142ec4241be3041c51dde9b73f2
fc64c584cacf6dd2542b20692139444d257d5d8f5126121fe0301b5eb48c
1e6b49d7146e35bdf2a9f4486cd020f9bcc3d0d92b4f62fdc90e4a3f7b27
090bf6d50b68c5af54ce548bcab7109cfb9190bb8750b8e4fb198f7dba2a
652c57c8625626b251cbd166fbccd8b96800b6b52330bfa93e526509b109
afbbc4f427e48a75f22924af702463fd5261c94170de0cb840f70892d1ba
a13535ee19fb5ae27ff6e9644a359c65b56122f9598082114d708c63d443
c9d6dd52c9e017b621312531e37ee72b765a5fc10d78a1a5066593e90c97
4b0d369f6eb6dc34810dd6bfcd31530114c0989428585e9af7033cde8d7e
cc6140d4d0de29660ac6a1947ac0c6b3260a1454b65e99f4664a02eaf162
65c893770827c0ac566d5679986a5fa777caa02093e41fe1bc06abb7cee0
c8a28ef96867a8a386b7b065de828c926ea2ec97af9569e873d91ba07371
91977dad97512a3ced4db5416907a331e88fce6b9fcd89fd32936426dfa3
bcda63e199ab3522a3ebc9ec12541b00d7a0ae565b1d2925edbf27f5b799
dc1f5d0b2eb9ff097b2fbcd47b0966642f713876379769c2738c1a121b71
51fa06a27c9ceda3c36d9601fdbd3a1d904a57395ea4871db10fd46c95e3
82fd48a855c800a3a4bdcb2a3a90fce6d0b547933fc509d5666560292711
ce61051dec6f2f9bc08e4c313c973e309ca298df3f118cc6d89d6504138c
c71da25e1e60b5bf9ad3e05cd6ffe78234edd25e34f03e34a35328250395
0e9f5e9eb90a9c9dd1e8080dbc8648587edc72b9c610aa09cb622779518f
6cf1f827d3d9ca246cdc3413bb94c5fdfd5192d3f6c5f205222681bfea24
f1b7db3c89601b54d1cb5ce31591a358423bf023562436fbfab2e3c951c3
01228a01bef0068a4d31c6e2055a6249fef4cc16d57e2bf931fa3bec63c2
6bb7cdaf2fb20b90b10061fb049a749894bf202f488911610d6d3a125520
257e1922980b76590c25335b34d4bcf538e30012e11f7bb32c4ca4887a41
80823f74cda7152f75ff7e535fb3aa73621921289fefa6968755cd6bedfa
8b37356787548b6723aa67afc0a1dac1e2d390c48d452a7bfc5470ad69da
2ef1b0d3c8252693058375dcc4e4c86fcff9e0c0f64364fc9fa28dbb26b2
980c7ac40f14d62bd1f506634303e35ae2067f893ba91930a61bc33df0dd
488b760a0faba5417c248a4128172793a4bbc0c4498ab55b1064b3066e13
29603a7f71a240f3a932c74d836374b1b835785b4c7061407dedaa397e20
d1c527110bf0c810e28f9e6d22a23ae59ec457ef6976b1fa5933a4be0a03
48ac74f8233deeeef14dbae48be50014e1c8a9d7ede81f5144f68fa271df
0f158bcab67073845622d0fe4cfa1cad1573944546aebe7be89dc44e5449
bc354a87d4b8c524fc0ca9e3f3f3325daf45053ad93ed0b2b8e5a33a9ce0
75344a70ccc5a87129f5a226b2a1dee99a192b5929575c9730eb557d2a62
dce4d7d3ab82fe5958ff5a6b27137870f876e089642c4017cc58d8dda557
83fe81be504245f6293fc7e6187a7f150d0ec1cd50b33723d940af80b2ed
44c899e405c58e337b67a34a369fcc37b6c7ee039eedc963ca78de02bd47
752cf331653b499fe0cb3ea78944815f9b38f2dd97200ff0ae7745419d71
c2ce1cb3dd939647becca1e8333d3bf2743dc3ec5f8da17f597bf997cb05
ec71a2b8586fc2afa3b6bdd12586ddc4b06437145ab49dcae3a862ee92ce
fffbdc08d1976c1f2317a130d6bbf59e5756bfc0e984f74580ffe107ea61
6c1ce8bbeeb293ade89eba7fd1594ebc2bfe2085679a029b01efa69187e1
a397366691627162c76fe2f1f7966d2afd8171118dd3e66a6d0b44bca31c
b30ff9c64807057af25e5de4f975dae0f346fc19413cd5d415692b8596c6
dbc84e5e82eebcbb26ceaf4dc89dea909d2f13ee0fa8293eb6223b6b2ae0
341cf2e49b659d585c21eb96deb714dd8242a3239f8949b6a31a966e7380
f6dbb6295c1fbbfec9411bcda08621ada1957a79ce73feffb5ed6bcb3ac6
7bcfd24e2a1f3bfe21327fd6fffd19afe3c5d69db0366dbf392f26409736
a54d294c76f3827a4f6b152cc028187fc0c43652264115af98c6c66fc5ff
9654dba42dbd00c3731c30577bb443824b32d13b23880f1238c3f909ab39
057f3a612285162e3a7f2ee888d11c4f6acfb114d2c90194815ece6ba335
c0d269c3421380d3e573a35aa75496f3cb775b942412d8bb0feb6af4394a
d7fb93180db178a0f3cbeeb61263225aff839f6c5e1a31b6a2b4fa125bbe
a1ced0278a91e521daa3cc19e19ed422238dc11988b4dcf9556893b4891f
5e332ccca22e31c3d43ed2ebe30817267465fa1b2913450fc91957498afc
1af5a328911505747e532e197549e6f266d8bfe32cec7113b90422070b74
b5f52e3b3458ba24a90d7cc1db2397553ec307389a3bf7d4805142a61193
7218423dae486cf83065f18f67e042862ead0d984902f735132b8c20ea7a
ffb61f38e7141da522595f534e5abf5367af54e0e8be623a15d6b418cc2c
e95999c3543ce07679fe1289eda4f5a00764d857555689a3cb5d0a05da60
'''.split()


def get_english_score(input_bytes):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


answer = ('', 0)

for hex in hex_input:
    freq = {}

    for symbol in bytes.fromhex(hex):
        if symbol in freq:
            freq[symbol] = freq[symbol] + 1
        else:
            freq[symbol] = 1

    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    symbol_top1 = sorted_freq[0][0]

    original = single_char_xor(hex, symbol_top1 ^ ord(' '))
    score = get_english_score(original)

    if score > answer[1]:
        answer = (original, score)

print(answer)



# TASK 5

text = b'''Shannon contributed to the field of cryptanalysis for national defense during World War II, 
including his basic work on codebreaking and secure telecommunications.'''

key = b'Shannon'

output_bytes = b''
index = 0

for byte in text:
    output_bytes += bytes([byte ^ key[index]])
    if (index + 1) == len(key):
        index = 0
    else:
        index += 1

print(output_bytes.hex() == '00000000000000730b0e001a1d07311d150b0a4f1a3c4815060b4f083a0d0d0a4e0008730b13171e1b0f3d090d171d061d730e0e1c4e010f27010e000f034e370d070b001c0b730c141c070109733f0e1c020b4e0409134e272642736208000d031b37010f094e07072048030f1d060d731f0e1c054f013d4802010a0a0c210d000507010973090f0a4e1c0b301d130b4e1b0b3f0d020103021b3d01020f1a06013d1b4f')