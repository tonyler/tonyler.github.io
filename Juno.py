
#░░░░░██╗██╗░░░██╗███╗░░██╗░█████╗░
#░░░░░██║██║░░░██║████╗░██║██╔══██╗
#░░░░░██║██║░░░██║██╔██╗██║██║░░██║
#██╗░░██║██║░░░██║██║╚████║██║░░██║
#╚█████╔╝╚██████╔╝██║░╚███║╚█████╔╝
#░╚════╝░░╚═════╝░╚═╝░░╚══╝░╚════╝░


#Basic Info about Juno--->addresses,api,coingecko name.

Wallets_Balances={"juno1qnsxa5chxj87mvm9jxqnyr9pdlp324mp8rzamq":0,"juno1n8wrmsa58765ck0phxq93etk3g0wtzwq5qtydv":0,"juno1z23gy5wmhmeq2v349hzfy7ndq9jfq3k0z9zqhz":0 }
Gtoken="juno-network"
api="https://juno-api.polkachu.com/cosmos/staking/v1beta1/delegations/"
import requests
    
def JunoPrice(): 
    from ReUsables import price
    return (price(Gtoken))

from ReUsables import Balance

def JunoBalance():
    return (Balance(Wallets_Balances,api))

