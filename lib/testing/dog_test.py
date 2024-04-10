from lib.dog import Dog
import io
import sys

class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog".'''
        fido = Dog()
        assert(type(fido) == Dog)
        
    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        dog_instance = Dog(name="Mutt", breed="Mastiff")  # Provide both name and breed arguments
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == ""

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    Dog(name=123, breed="Labrador")  # Provide an integer instead of a string
    sys.stdout = sys.__stdout__
    assert "Name must be a string between 1 and 25 characters." in captured_out.getvalue()

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name="What do dogs do on their day off? Can't lie around - that's their job.")  # Provide a name longer than 25 characters
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Name must be a string between 1 and 25 characters.\n"

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        fido = Dog(name="Fido")
        assert fido.name == "Fido"

    def test_breed_not_in_list(self):
        '''prints "Breed must be in list of approved breeds." if not in breed list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Dog(name="Fido", breed="Human")  # Provide a breed not in the approved list
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Breed must be in list of approved breeds.\n"

    def test_breed_in_list(self):
        '''saves breed if in breed list.'''
        fido = Dog(name="Fido", breed="Pug")  # Provide both name and breed arguments
        assert fido.breed == "Pug"
