﻿Task 4_3_2 
Для того щоб вирішити це завдання нам потрібно:
1. Додати новий файл для тест кейсів, який буде пов*язаний із сторінкою товару. Назвемо файл із тестами test_product_page.py.
2. У файлі locators.py створюємо окремий клас для локаторів для сторінки товару.
   2.1. Для кнопки додавання товару у корзину.
3. У файл base_page додаємо код для вирішення рівняння.
4. Створюємо файл product_page.py у pages. У цьому файлі створюємо клас ProductPage(BasePage) для сторінки товару
   і описуємо всю логіку взаємодії із даною сторінкою. Додаємо тест test_guest_can_add_product_to_basket().
5. У файлі test_product_page.py пишемо тест для відкривання сторінки, вирішення рівняння. Робимо time.sleep(100). За цей час дізнаємось 
   всі селектори які потрібні для майбутніх перевірок(месиджі, ціна).
6. У файлі locators.py додаємо локатори для сторінки товару для перевірок месиджів, цін.
7. У файлі product_page.py. Додаємо методи
      1 "Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.Сообщение со стоимостью корзины."
      2 Стоимость корзины совпадает с ценой товара.
8. У файлі test_product_page.py. доповнюємо тест кейс методами із пункту 7.

Task 4_3_3
Суть завдання полягає в незалежності від даних. Тобто не потрібно хардкодити певні дані у тестах(стрінги), а потім створювати перевірки на їх базі.
Тому що таке тестування не показує всієї картини сайту, а ми робимо виснвок тільки із одного(декількох) захардкоджених випадків.
Тому суть цього уроку, полягає у тому що змінили урлу, і ми повинні протестувати на новому товарі попередній тест із уроку 4_3_2. Якщо тест зараз 
проходить, тоді все написано правильно і ми нічого не хардкодимо.

Task 4_3_4
Суть тесту полягає в тому що на котрійсь із сторінок списку нижче є баг, ми повинні його знайти.
У цьому тесті не потрібно кардинально міняти логіку перевірок(зробили перевірку на повне співпадіння тексту назви книги, 
ціни книги на деталізації) і додали до попереднього тесту. 
Для того щоб запустити один тест на декілької посиланнях додаємо параметризацію.
Після того як баг виявлений ми - позначили посилання із багом як xfail(ожидаемо падающий).

Task 4_3_6
Суть тесту полягає в тому, що ми вивчили нові методи для перевірки відсутності елемента. Отримані знання треба використати на практиці.
Отже 
1. У файл base_page додаємо два нових методи is_not_element_present, is_disappeared. 
2. Оскільки у файлі locators ми всі потрібні локатори маємо, то и нічого не додаємо.
3. У файл product_page імпортуємо дані. 
	from .base_page import BasePage
	from .locators import ProductPageLocators
   І створюємо нові методи should_not_be_success_message, should_not_be_success_message_after_adding_product_to_basket, які використовують 
   методи із пункту 1.
4. Складаємо нові тести у файлі test_product_page згідно із завданням.


Task 4_3_8
Суть тесту полягає в тому що деякі елементи на сторінці які є доступні по всьому флову сайту(хедер, футер і т.д) тоді
варто створити у locators клас BasePageLocators де ми і пропишемо локатори які присутні на всьому сайті. Далі у Base_page
прописуємо перевірки. і далі у test_product_page пишемо нові тести. 


Task 4_3_10
1. Створюємо локатори для 
   1. Іконки корзини 
   2. Повідомлення про пусту корзину
   3. Корзина із товарами.
2. У класі BasePage створюємо метод для переходу у корзину.
3. Створюємо basket_page.py. Створюємо методи
4. test_product_page.py створюємо 2 нові тести
