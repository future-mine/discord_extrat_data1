#EMAIL = 'itismanyfishion@gmail.com'
#PASSWORD = '1Firstzhenjindifficu!ltaccount'
#CHANNEL = '707492893845225533'
#GUILD = '707492893845225536'

# EMAIL = 'michael@michaelhazilias.com'
# PASSWORD = 'discordtemp'
# CHANNEL = '537029663680364546'
# GUILD = '688611481419513856'


# It would be good to hold different configurations for channels in one file, then have a command line option to run one, like:

Connection = {
    'EMAIL':'michael@michaelhazilias.com',
    'PASSWORD':'discordtemp'
}

CHA = {
    'Channel1':{
        'CHANNEL' : '537029663680364546',
        'GUILD' : '688611481419513856',
        'variable_list':[
            {'variable':'date', 'texttosearch':'Post open targets for '},
            {'variable':'high', 'texttosearch':'Predicted High: '},
            {'variable':'low', 'texttosearch':'Predicted Low: '},
            {'variable':'close', 'texttosearch':'Predicted Close: '},
            ]		
    },
    'Channel2': {
        'CHANNEL' : '537029663680364546',
        'GUILD' : '692151905098399834',
        'variable_list':[
            {'variable':'fulltext', 'texttosearch':''}
        ]		
    }
}
