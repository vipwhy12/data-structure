shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def is_available_to_order(menus, orders):
  sort_menus = sorted(menus)
  sort_orders = sorted(orders)
  count = 0
  
  for i in range(len(sort_menus)):
    for j in range(len(sort_orders)):
      if sort_menus[i] == sort_orders[j]:
        count += 1
    
  if len(sort_orders) == count:
    return True
  else:
    print(count)
    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)