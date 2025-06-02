
import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name, expected', [
        ('Книга', True),
        ('', False),
        ('О' * 40, True),
        ('О' * 41, False)
    ])
    def test_add_new_book_validation(self, name, expected):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert (name in collector.get_books_genre())== expected


    @pytest.mark.parametrize('book, genre, expected', [
        ('Оно', 'Ужасы', True),
        ('Оно', 'Фантастика', True),
        ('Оно', 'Фэнтези', False),
        ('Оно', '', False),
        ('Оно', '123', False)
    ])
    def test_set_book_genre_validation(self, book, genre, expected):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        if expected:
            assert collector.get_book_genre(book) == genre
        else:
            assert collector.get_book_genre(book) == ''



    def test_get_book_genre_returns_assigned_value(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.books_genre = {'1984': 'Антиутопия'}
        assert collector.get_book_genre('1984') == 'Антиутопия'

    def test_get_book_genre_for_non_existing_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая книга') is None


    def test_get_book_genre_when_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') == ''

#def test_get_books_genre_returns_all_books(self):

    @pytest.mark.parametrize("books, genre, expected", [
        (
                [("Книга1", "Фантастика"), ("Книга2", "Ужасы"), ("Книга3", "Фантастика")],
                "Фантастика",
                ["Книга1", "Книга3"]
        ),
        (
                [("Книга1", "Фантастика"), ("Книга2", "Ужасы")],
                "Романтика",
                []
        ),
        (
                [("Книга1", "Комедии")],
                "Комедии",
                ["Книга1"]
        ),
        (
                [],
                "Фантастика",
                []
        )
    ])
    def test_get_books_with_specific_genre_parametrized(self, books, genre, expected):
        collector = BooksCollector()
        for name, book_genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, book_genre)
        assert collector.get_books_with_specific_genre(genre) == expected


    @pytest.mark.parametrize('genre, expected_children', [
        ('Фантастика', True),
        ('Мультфильмы', True),
        ('Ужасы', False),
        ('Детективы', False),
        ('Комедии', True)
    ])
    def test_get_children_books(self, genre, expected_children):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', genre)
        assert ('Книга' in collector.get_books_for_children()) == expected_children


    @pytest.mark.parametrize('book, expected', [
        ('Существующая книга', True),
        ('Новая книга', False),
        ('', False),
        ('123', False)
    ])
    def test_add_to_favorites_validation(self, book, expected):
        collector = BooksCollector()
        collector.add_new_book('Существующая книга')
        collector.add_book_in_favorites(book)
        assert (book in collector.get_list_of_favorites_books()) == expected


    def test_cant_add_duplicate_book(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')
        assert len(collector.get_books_genre()) == 1


    def test_remove_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.add_book_in_favorites('Преступление и наказание')
        collector.delete_book_from_favorites('Преступление и наказание')
        assert 'Преступление и наказание' not in collector.get_list_of_favorites_books()


    def test_get_favorites_list_initial_state(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []


    def test_get_favorites_list_after_adding_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        assert len(collector.get_list_of_favorites_books()) == 2


    def test_get_favorites_list_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        assert collector.get_list_of_favorites_books() == ['Книга 1']