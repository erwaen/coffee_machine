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
    "money": 100.0,
}


def ask_coffee():
    """
    Se le pide al usuario que eliga una opcion y retorna
    """

    selected_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    return selected_coffee


def handle_ask_prompt(prompt):
    """
    Manejamos el la opcion elegida por el usuario.

     Parameters:
        prompt (String): la opcion elegida.

    Returns:
        int: 0 -> deseo apagar maquina,
             1-> imprimir recursos,
             2-> quiere un cafe,
             3-> lo que ingreso es invalido
    """
    if prompt == "off": #opcion para los manteiners (apagar la maquina)
        return 0
    elif prompt == "report":
        print_resources()
        return 1
    elif prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        return 2
    else:
        print("Select a valid option")
        return 3


def coin_prompt(coffee_type):
    print("Please insert coins.")
    quarters_amount = int(input("How many quarters? ")) # quarters value = $0.25
    dimes_amount = int(input("How many dimes? ")) # dimes value = $0.10
    nickles_amount = int(input("How many nickles? ")) # nickles value = $0.05
    pennies_amount = int(input("How many pennies? ")) # pennies value = $0.01

    user_coins_total = quarters_amount*0.25 + dimes_amount*0.10 + nickles_amount*0.05 + pennies_amount*0.01
    coffee_value = MENU[coffee_type]["cost"]
    if user_coins_total < coffee_value:
        print("Sorry that's enough money. Money refunded.")
    elif user_coins_total >= coffee_value:
        change = user_coins_total - coffee_value

        #aumentamos el monedero de la maquina
        resources["money"] += user_coins_total
        resources["money"] -= change
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee_type} ☕ Enjoy!.")

        #reducimos los recursos de la maquina dependiendo del cafe que se preparo.
        for ingredient in MENU[coffee_type]["ingredients"]:
            resources[ingredient] -= MENU[coffee_type]["ingredients"][ingredient]


def resources_exist(selected_coffee):
    """
    Analizamos si es que queda los recursos suficientes para hacer el cafe seleccionado.

    Parameters:
        selected_coffee (String): tipo de caffe a analizar recursos

    Returns:
        Bool: True -> se puede hacer el cafe, False -> no hay recursos suficientes
    """
    ingredients = MENU[selected_coffee]["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def print_resources():
    """
    Imprime los recursos que tiene la maquina("cafe, leche, agua, monedero")
    """
    for element in resources:
        to_print = f"{element}: {resources[element]}"
        if element == "water" or element == "milk":
            to_print += "ml"
        elif element == "coffee":
            to_print += "g"
        elif element == "money":
            to_print = f"{element}: ${resources[element]}"
        print(to_print)


# el main()
def coffee_machine():
    on = True  # on representa el estado de la maquina. True -> encendido, False -> apagado
    while on:
        coffee_option = ask_coffee()
        continue_or_no = handle_ask_prompt(coffee_option)
        if continue_or_no == 0: #deseo apagar la maquina
            on = False
            continue
        elif continue_or_no == 1 or continue_or_no == 3:
            continue
        if resources_exist(coffee_option): #si hay recursos, procedemos al pago
            coin_prompt(coffee_option)


coffee_machine()
