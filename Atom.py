
#░█████╗░████████╗░█████╗░███╗░░░███╗
#██╔══██╗╚══██╔══╝██╔══██╗████╗░████║
#███████║░░░██║░░░██║░░██║██╔████╔██║
#██╔══██║░░░██║░░░██║░░██║██║╚██╔╝██║
#██║░░██║░░░██║░░░╚█████╔╝██║░╚═╝░██║
#╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝


Wallets_Balances={"cosmos1qnsxa5chxj87mvm9jxqnyr9pdlp324mp33pxuu":0}
Gtoken="cosmos"
api=" https://api-cosmoshub-ia.cosmosia.notional.ventures/cosmos/staking/v1beta1/delegations/"
import requests
from ReUsables import Balance

def GaiaWallet():
    return Balance(Wallets_Balances,api)


def AtomPrice(): 
    from ReUsables import price
    return (price(Gtoken))
