
#░█████╗░░██████╗███╗░░░███╗░█████╗░░██████╗██╗░██████╗
#██╔══██╗██╔════╝████╗░████║██╔══██╗██╔════╝██║██╔════╝
#██║░░██║╚█████╗░██╔████╔██║██║░░██║╚█████╗░██║╚█████╗░
#██║░░██║░╚═══██╗██║╚██╔╝██║██║░░██║░╚═══██╗██║░╚═══██╗
#╚█████╔╝██████╔╝██║░╚═╝░██║╚█████╔╝██████╔╝██║██████╔╝
#░╚════╝░╚═════╝░╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚═╝╚═════╝░

Wallets_Balances={"osmo1qnsxa5chxj87mvm9jxqnyr9pdlp324mpe2jk2w":0,"osmo1n8wrmsa58765ck0phxq93etk3g0wtzwq2fm0uz":0}
Gtoken="osmosis"
api="https://lcd.osmosis.zone/cosmos/staking/v1beta1/delegations/"
import requests
from ReUsables import Balance

def OsmoBalance():
    return (Balance(Wallets_Balances,api))

def OsmoPrice(): 
    from ReUsables import price
    return (price(Gtoken))

