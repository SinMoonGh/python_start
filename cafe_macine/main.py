MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
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


def process_coins(quarters, dimes, nickles, pennies):
  """지불한 금액의 총합을 반환합니다."""
  # TODO 3: process coins.
  # 동전: quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
  # 총합 = quarters + dimes + nickles + pennies 이다.
  coin_sum = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies *
                                                                      0.01)
  return coin_sum


def check_coins(coin_sum, menu, order):
  """사용자가 음료 가격보다 많은 돈을 지불했는지 검사하고, 맞다면 잔돈을 반환"""
  # TODO 4: check transaction successful?
  # 사용자가 음료의 금액에 맞는 돈을 넣었는지 검사해야 한다.

  if coin_sum > menu[order]['cost']:
    # 음료의 금액보다 사용자가 지불한 금액이 크다면 잔돈을 반환해줘야 합니다.
    # “Here is $2.45 dollars in change.” 여기서 실수는 소숫점 2자리 까지 반환합니다.
    print(f"Here is ${coin_sum - menu[order]['cost']: .1f} in change")
    return True
  else:
    # 만약 사용자가 금액보다 부족한 돈을 넣었다면 “Sorry that's not enough money. Money refunded.”를 출력한다.
    print("Sorry that's not enough money. Money refunded.")
    return False


def resource_update(coin_sum, menu, order):
  """사용자가 금액보다 넘치는 돈을 넣었다면 음료 재고와 매출을 업데이트 합니다."""
  # TODO 5: Make Coffee.
  # 커피를 주문하고 난 후 'report'를 사용했을 때 전체 재고 물량이 차감되어 있어야 합니다.
  # 주문을 성공적으로 수행했고, 여전히 재고가 남았다면 다시 주문을 받습니다.
  if check_coins(coin_sum, menu, order):
    # 사용자가 충분한 금액을 지불했다면
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
    # 고객에게 뭐 먹을 건지 받기
    # 마지막에 주문이 성공했는지 여부 나옴
    # 그리고 주문이 성공했으면 뭐 주문했는지 출력.
    # 이 루트를 무한 반복
    order = input(" What would you like? (espresso/latte/cappuccino): ")
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
        # 그 다음 사용자의 동전을 입력 받아야 한다.
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        # 고객이 지불한 금액의 총합
        money = process_coins(quarters, dimes, nickles, pennies)
        # 고객이 지불한 금액이 음료 값보다 많은 지 검사
        check_coins(money, MENU, order)

        # 재고에 있는 수량을 차감
        resource_update(money, MENU, order)

        # 현재 재고로 상품(라떼)을 만들 수 있는 경우 “Here is your latte. Enjoy!”를 출력해야 합니다.
        print(f'Here is your {order}. Enjoy!')


cafe_program()
