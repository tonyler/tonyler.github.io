from flask import Flask ,render_template


from Atom import AtomPrice, GaiaWallet


from Juno import JunoBalance, JunoPrice 


from Osmosis import OsmoBalance, OsmoPrice 


app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():

    AtomHoldings=GaiaWallet()
    Total_Value_Atom=round(AtomHoldings*AtomPrice(),2)

    JunoHoldings=JunoBalance()
    Total_Value_Juno=round(JunoPrice()*JunoHoldings,2)  


    OsmoHoldings=OsmoBalance()
    Total_Value_Osmo=round(OsmoPrice()*OsmoHoldings,2)

    return render_template('index.html',AtomHoldings=AtomHoldings,Total_Value_Atom=Total_Value_Atom,JunoHoldings=JunoHoldings,Total_Value_Juno=Total_Value_Juno,OsmoHoldings=OsmoHoldings,Total_Value_Osmo=Total_Value_Osmo)

 


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8001,debug=True)
