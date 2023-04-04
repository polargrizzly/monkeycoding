some_string = 'abctowel'
print(some_string[::-1])
list_of_smth = ['a', 'c', 15, ['2']]
print(list_of_smth[::-1])

containers_to_sort = ['uabicycle', 'ukholder', 'uarifle',
                      'uahimars', 'uam16', 'pobeer', 'usbullets']
container_to_ua = []
container_to_uk = []
container_to_po = []
def shipping_filter(list_of_products):
    for product in list_of_products:
        if product[:2] == 'ua':
            container_to_ua.append(product[2:])
        elif product[:2] == 'uk':
            container_to_uk.append(product[2:])
        elif product[:2] == 'po':
            container_to_po.append(product[2:])
shipping_filter(containers_to_sort)
print(container_to_uk)

mbogs= ['Snoop','Tupac', 'Biggie',
        'Method man', 'Lil Wayne', 'Lil dicky']
real_ogs = []
pussy_niggas = []
def lil_detect(nigga_nicknames):
    for nickname in nigga_nicknames:
        if nickname[:4] == 'Lil ':
            pussy_niggas.append(nickname)
        else: real_ogs.append(nickname)
lil_detect(mbogs)
print(real_ogs)
print(pussy_niggas)

