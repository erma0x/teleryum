from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon import utils

ID_CHANNEL_REVERSED = -1001338521686

real_id, peer_type = utils.resolve_id(ID_CHANNEL_REVERSED)

print(real_id)  # 456
print(peer_type)  # <class 'telethon.tl.types.PeerChannel'>

peer = peer_type(real_id)
print(peer)  # PeerChannel(channel_id=456)

# OUTPUT
#1338521686
#<class 'telethon.tl.types.PeerChannel'>
#PeerChannel(channel_id=1338521686)


#dialogs = client.get_dialogs()
#my_channel = client.get_entity(PeerChannel(some_id))