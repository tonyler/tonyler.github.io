import requests


def Balance (Wallets_Balances,api): 
    for wallet in Wallets_Balances: 
        #μορφοποιούμε το API ώστε να απευθύνεται σε συγκεκριμένο πορτοφόλι κάθε φορά
        new_api=api+wallet

        res=requests.get(new_api)
        data=res.json()
        #αρχικοποιούμε για το σύνολο των staked tokens (και θα προσθέτουμε κάθε φορά staked tokens ανά validator)
        sum=0

        #Βλέπουμε πόσα έχουμε delegate ανά validator (αφού το api δεν επιστρέφει συνολικά tokens από μόνο του)
        for i in range (len(data["delegation_responses"])): 
            balance= (data["delegation_responses"][i]["balance"]["amount"])
            sum+=float(balance)

        #Χρησιμοποιώ Dic αντί να το κάνω πιο απλό καθώς μπορεί να φανεί χρήσιμη σε μελλοντική χρήση.
        Wallets_Balances[wallet]=sum 

    #Εδώ το Sum είναι το σύνολο όλων των πορτοφολιών του εκάστοτε Token συνολικά
    sum=0
    for wallet in Wallets_Balances: 
        sum+=Wallets_Balances[wallet]

    #μετατροπή uToken σε Token
    sum=round(sum/1000000,2)
    return sum


#🇨​​​​​🇴​​​​​🇮​​​​​🇳​​​​​ 🇬​​​​​🇪​​​​​🇨​​​​​🇰​​​​​🇴​​​​​
def price(token): 
    api=f"https://api.coingecko.com/api/v3/simple/price?ids={token}&vs_currencies=usd"
    res=requests.get(api)
    data=res.json()
    price=float(data[token]['usd'])
    return (price)