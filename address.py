import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAlvT9QoXecXq_WFfd4_slajtCnMJBXB6Y')


def verify_address(address):    
    geocode_result = gmaps.geocode(address)
    if geocode_result == []:
        addr = "This address is invalid"
    else:
        geocode_result= geocode_result[0]
        if 'plus_code' in geocode_result:
            addr = "The Company address is valid"
        else:
            addr = "This address is vague, This job invite is likely a scam"

    if addr == "The Company address is valid":
        return True
    else:
        return False
