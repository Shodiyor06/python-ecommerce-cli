from interfaces.main_menu import home_menu, main_menu
from services.database import DB
from services.order_service import OrderService
from services.product_service import ProductService
from services.user_service import UserService


def main():
    user_service = UserService()
    order_service = OrderService()
    db = DB()
    products = db.get_products()
    product_service = ProductService(products)

    while True:
        home_menu()
        choice = input("Tanlovingizni kiriting: ").strip()

        if choice == "1":
            user_service.create_user()

        elif choice == "2":
            user_service.login_user()

            if user_service.logged_user:
                user_menu(user_service, order_service, product_service, products)

        elif choice == "0":
            print("Dasturdan chiqish amalga oshirildi.")
            break
        else:
            print("Noto'g'ri tanlov. Qayta urinib ko'ring.")


def user_menu(user_service, order_service, product_service, products):
    username = user_service.logged_user.username

    while True:
        main_menu()
        user_choice = input("Tanlovingizni kiriting: ").strip()

        if user_choice == "1":
            product_service.print_products()

        elif user_choice == "2":
            product_service.add_product_to_cart(order_service, username, products)

        elif user_choice == "3":
            product_service.print_cart(order_service, username)

        elif user_choice == "4":
            product_service.remove_product_from_cart(order_service, username)

        elif user_choice == "5":
            cart = order_service.get_cart(username)
            if not cart:
                print("Savat bo'sh. Avval mahsulot qo'shib oling.")
            else:
                order_service.create_order(user=user_service.logged_user, products=cart)
                order_service.print_check()
                order_service.clear_cart(username)

        elif user_choice == "0":
            print("Foydalanuvchi menyusidan chiqish.")
            break
        else:
            print("Noto'g'ri tanlov. Qayta urinib ko'ring.")


if __name__ == "__main__":
    main()
