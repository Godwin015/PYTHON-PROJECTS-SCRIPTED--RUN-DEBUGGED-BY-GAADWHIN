print("CRYPTO_WALLET_SIMULATION_USING_PYTHON")
print("SCRIPTED BY GAADWHIN!")

first = input("What is your name?\n")

second = (", Welcome to the safest cryptocurrency wallet in the globe!\n")
print("Hello " + first + second)

intro = input("Are you here to access your secret_passphrase?\n")

if intro == "yes" or "Yes" or "YES":
    print(first + ", Welcome onboard\n")
else:
    print(first + ", Get out of here you loser!!")
    input()
    exit()

print("PROVE OWNERSHIP BY INPUTING ACCESS KEY")
entrance = input("input your access_key:\n")

secret_passphrase = "great, gratify, mannered, void, diphteria, coliophtera, insecta, plantae, fungi, mulusca, broken"

access_denied = "You have less than 20 seconds to vacate this device or else be INVESTIGATED by the FBI !!!"

if entrance == "steroganography":
    print("ACCESS GRANTED, view secret_passphrase below\n" + secret_passphrase)
else:
    print("SCAM ALERT!  SCAM ALERT!! SCAM ALERT !!!\n" + access_denied)
    print("for your own GOOD, type exit below ")
    input()
    exit()

print("THE SECRET_PASSPHRASE ABOVE WOULD BE USELESS IF YOU DON'T KNOW THE SPECIFIC WALLET TO APPLY IT TO")
wallet_name = input("What is the wallet name? ")
if wallet_name == "trust wallet" or "Trust Wallet" or "TRUST WALLET" or "Trust wallet":
    wallet_passcode = input("input wallet passcode: ")
else:
    print("Ya busted.....premature hacker")
    print("Hacking isn't your calling, go learn from www.tryhackme.com and then come back to try again !")
    input()
    exit()
    
if wallet_passcode == "86303258Ah.":
    print("SUCCESS, you have a total of 15 BTCs in this Crypto wallet\n" + " and they are all intact.\n" +" HAVE A NICE DAY BOSS")
    print("\nDON'T FORGET TO LOGOUT AND CLEAR CACHE\n")
    print("SCRIPTED BY GAADWHIN")
    input()
    exit()
else:
    print("you may have made it this far, BUT YOUR LUCK JUST RAN OUT")
    print("YA SCREWED")
    input()
    exit()

