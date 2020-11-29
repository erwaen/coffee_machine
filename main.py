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


def coin_prompt():
    pass


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
            coin_prompt()






coffee_machine()
