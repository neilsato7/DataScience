## create a local csv with these column headers: ##
## 'id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', ## 
##'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', ##
##'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic' ##
# INITIAL CODE
opened_file = open('AppleStore.csv') 

from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

apps_data[0].append('price_label')
for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    
    if price == 0.0:
        app.append('free')
    elif price > 0.0 and price < 20:
        app.append('affordable')
    elif price > 20 and price < 50:
        app.append('expensive')
    elif price > 50:
        app.append('very expensive')

## validate new items have been added.
print(apps_data[:5])
