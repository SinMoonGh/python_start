MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 3000,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 4500,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3500,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def exit(order):
  """시스템을 종료하는 값을 반환합니다."""
  # TODO: Turn off the Coffee Machine by entering “off” to the prompt.
  # 사용자가 'off'라는 키워드를 치면 시스템이 종료되어야 한다.
  if order == 'off':
    return True


def check_resources(menu, resources, order):
  """사용자가 주문한 음료를 만들 재료가 있는지 알려줍니다."""
  # TODO 2: check resources sufficient?
  # 사용자가 주문을 하면 음료를 만들 수 있는 재료가 충분한지 검사해야 한다.
  # 재료가 충분한지?? 메뉴 딕셔너리에 있는 커피 -> ingredients -> 각 재료를 resources 값들과 대조해서 resources 값 들이 더 커야 한다.
  for ingredients, amount in menu[order]['ingredients'].items():
    if ingredients in resources:
      if resources[ingredients] >= amount:
        resources[ingredients] -= amount
        return True
      else:
        # 만약 재료가 충분하지 않다면 “Sorry there is not enough water.”를 출력한다.
        print(f"Sorry there is not enough {ingredients}.")
        return False


def process_coins(menu, order):
  """사용자의 동전을 입력받고, 고객이 지불한 금액이 충분한지 확인
  및 영수증을 출력합니다."""
  # TODO 3: process coins.
  
  print("지폐를 넣어주세요.")
  coin_sum = 0
  There_is_not_enough = False

  # 만약 주문한 커피 금액이 지불한 금액보다 적다면 process_coins함수를 반환합니다.
  ten_thousand_won = int(input("10000짜리 지폐 : "))
  coin_sum += ten_thousand_won * 10000
  if coin_sum > menu[order]['cost']:    
    return receipt(coin_sum, menu, order)
  
  Five_thousand_won = int(input("5000원짜리 지폐 : "))
  coin_sum += Five_thousand_won * 5000
  if coin_sum > menu[order]['cost']:    
    return receipt(coin_sum, menu, order)
  
  A_thousand_won = int(input("1000원짜리 지폐 : "))
  coin_sum += A_thousand_won * 1000
  if coin_sum > menu[order]['cost']:
    return receipt(coin_sum, menu, order)
  else:
    There_is_not_enough = True
  
  return There_is_not_enough    


def receipt(coin_sum, menu, order):
  """커피값, 지불 금액, 거스름 돈 출력"""

  # 커피값 출력
  print(f"음료값 : {menu[order]['cost']}")

  # 지불 금액 출력
  print(f"지불하신 금액 : {coin_sum}")

  # 거스름 돈 출력
  change = coin_sum - menu[order]['cost']
  print(f"반환받으실 금액 : {change}")  
  

def resource_update(menu, order):
  """사용자가 금액보다 넘치는 돈을 넣었다면 음료 재고와 매출을 업데이트 합니다."""
  # TODO 5: Make Coffee.
  # 커피를 주문하고 난 후 'report'를 사용했을 때 전체 재고 물량이 차감되어 있어야 합니다.
  # 주문을 성공적으로 수행했고, 여전히 재고가 남았다면 다시 주문을 받습니다.
  
  for ingredients, amount in menu[order]['ingredients'].items():
    # 음료를 만드는 데 필요한 물품과 수량을 할당
    if ingredients in resources:
      # 주문한 음료 재료가 재고 품목에 있다면
      if resources[ingredients] >= amount:
        # 그리고 재고 수량이 음료를 만드는 데 필요한 수량보다 많다면
        resources[ingredients] -= amount
        # 재고를 탐색하여 음료를 만드는 데 필요한 재료의 양 만큼 차감시킨다.


def cafe_program():  
  money = 0
  while True:
    # TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    # 고객에게 주문을 입력 받고, off를 입력하면 종료합니다.    
    order = input("주문하시겠습니까? (espresso/latte/cappuccino): ")
    if exit(order):
      break

    # TODO 1: print report.
    # 사용자가 'report'라는 키워드를 입력하면 현재 남아있는 재고에 대해 출력해야 한다.
    if order == 'report':
      print(
          f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"
      )
    else:
      # 만약 사용자가 선택한 음료의 재료가 충분하다면 음료를 주문 받아야한다.
      if check_resources(MENU, resources, order):       
        # 사용자의 지폐을 입력받고, 고객이 지불한 금액이 충분한지 체크
        There_is_not_enough = process_coins(MENU, order)

        if There_is_not_enough:
          # 만약 지불 금액이 충분하지 않다면
          print("죄송합니다. 금액이 충분하지 않습니다. 넣으신 돈을 다시 반환해 드리겠습니다.")
        else:
          # 재고에 있는 수량을 차감
          resource_update(MENU, order)

          # '맛있게 드세요' 출력.
          print(f'주문하신 {order} 나왔습니다~ 맛있게 드세요~')          


cafe_program()
